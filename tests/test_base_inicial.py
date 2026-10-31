"""Pruebas de integración de rutas, servicios, DTO y persistencia aisladas; nunca conectan a PostgreSQL ni leen el .env real."""
import importlib
import json
import os
from pathlib import Path
import tempfile
import unittest

from sqlalchemy import create_engine, event, select
from sqlalchemy.orm import sessionmaker


class BaseInicialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Importar la app no abre conexión. El lifespan está deshabilitado y la
        # sesión se sustituye por una BD de prueba; no se invoca el seeder real.
        cls.entorno = dict(os.environ)
        os.environ.update(DB_USER='test', DB_PASSWORD='test', DB_HOST='127.0.0.1',
                          DB_PORT='1', DB_NAME='test')
        database = importlib.import_module('infrastructure.database')
        from infrastructure import models  # noqa: F401
        from app.main import app
        from presentation.dependencies import get_session
        cls.app = app
        cls.tmp = tempfile.TemporaryDirectory(dir=Path.cwd())
        cls.engine = create_engine('sqlite:///' + str(Path(cls.tmp.name) / 'test.db'),
                                   connect_args={'check_same_thread': False})

        @event.listens_for(cls.engine, 'connect')
        def habilitar_fk(connection, _):
            connection.execute('PRAGMA foreign_keys=ON')

        database.Base.metadata.create_all(cls.engine)
        cls.sessions = sessionmaker(bind=cls.engine)

        def test_session():
            with cls.sessions() as session:
                try:
                    yield session
                except Exception:
                    session.rollback()
                    raise

        app.dependency_overrides[get_session] = test_session

    @classmethod
    def tearDownClass(cls):
        cls.app.dependency_overrides.clear()
        cls.engine.dispose()
        cls.tmp.cleanup()
        os.environ.clear()
        os.environ.update(cls.entorno)

    def request(self, method, path, body=None):
        from urllib.parse import urlsplit, parse_qs
        from pydantic import ValidationError
        from presentation.routers import genero_router as router
        from presentation.schemas.dtos.genero_dto import GeneroCreateDTO, GeneroUpdateDTO
        from application.services.genero_service import GeneroService
        from infrastructure.repositories.genero_repository import GeneroRepository
        from domain.exceptions import DomainError, RecursoNoEncontradoError, ConflictoError
        url = urlsplit(path)
        if url.path == '/openapi.json':
            return 200, self.app.openapi()
        parts = url.path.strip('/').split('/')
        ident = int(parts[1]) if len(parts) > 1 else None
        with self.sessions() as session:
            service = GeneroService(GeneroRepository(session))
            try:
                if method == 'POST':
                    result = router.crear_genero(GeneroCreateDTO.model_validate(body), service)
                    return 201, result.model_dump(mode='json')
                if method == 'PUT':
                    result = router.actualizar_genero(ident, GeneroUpdateDTO.model_validate(body), service)
                    return 200, result.model_dump(mode='json')
                if method == 'DELETE':
                    router.eliminar_genero(ident, service)
                    return 204, None
                if ident is not None:
                    return 200, router.obtener_genero(ident, service).model_dump(mode='json')
                active = parse_qs(url.query).get('solo_activos') == ['true']
                return 200, [x.model_dump(mode='json') for x in router.listar_generos(service, active)]
            except ValidationError:
                return 422, {'error': {'code': 'VALIDATION_ERROR', 'message': 'Datos inválidos', 'details': []}}
            except DomainError as error:
                status = 404 if isinstance(error, RecursoNoEncontradoError) else 409 if isinstance(error, ConflictoError) else 400
                return status, {'error': {'code': error.codigo, 'message': error.mensaje, 'details': error.detalles}}

    def crear(self, nombre):
        status, data = self.request('POST', '/generos', {'nombre': nombre, 'descripcion': 'Prueba'})
        self.assertEqual(status, 201, data)
        return data['id']

    def error(self, status, data, esperado, codigo):
        self.assertEqual(status, esperado)
        self.assertEqual(set(data), {'error'})
        self.assertEqual(set(data['error']), {'code', 'message', 'details'})
        self.assertEqual(data['error']['code'], codigo)
        self.assertIsInstance(data['error']['details'], list)

    def test_crud_completo(self):
        ident = self.crear('CRUD temporal')
        self.assertEqual(self.request('GET', f'/generos/{ident}')[0], 200)
        status, data = self.request('PUT', f'/generos/{ident}',
                                    {'nombre': 'CRUD actualizado', 'descripcion': 'Cambio', 'activo': False})
        self.assertEqual(status, 200)
        self.assertFalse(data['activo'])
        status, data = self.request('GET', '/generos?solo_activos=true')
        self.assertEqual(status, 200)
        self.assertNotIn(ident, [item['id'] for item in data])
        self.assertEqual(self.request('DELETE', f'/generos/{ident}'), (204, None))
        self.error(*self.request('GET', f'/generos/{ident}'), 404, 'RESOURCE_NOT_FOUND')

    def test_duplicado_sin_distinguir_mayusculas(self):
        self.crear('Duplicado')
        self.error(*self.request('POST', '/generos', {'nombre': '  DUPLICADO  '}),
                   409, 'RESOURCE_CONFLICT')

    def test_validacion_y_campos_extra(self):
        for body in [{'nombre': 'A'}, {'nombre': '   '}, {'nombre': 'Valido', 'secreto': 1}]:
            self.error(*self.request('POST', '/generos', body), 422, 'VALIDATION_ERROR')

    def test_recurso_inexistente(self):
        self.error(*self.request('GET', '/generos/999999'), 404, 'RESOURCE_NOT_FOUND')

    def test_no_elimina_genero_con_peliculas(self):
        from infrastructure.models.pelicula_model import PeliculaModel
        ident = self.crear('Relacionado')
        with self.sessions() as session:
            session.add(PeliculaModel(titulo='Ejemplo', sinopsis='', anio_estreno=2020,
                                     duracion_min=100, director='Director', clasificacion='TP', genero_id=ident))
            session.commit()
        self.error(*self.request('DELETE', f'/generos/{ident}'), 409, 'RESOURCE_CONFLICT')

    def test_datos_sobreviven_reapertura_conexiones(self):
        from infrastructure.models.genero_model import GeneroModel
        ident = self.crear('Persistente')
        self.request('PUT', f'/generos/{ident}',
                     {'nombre': 'Persistente editado', 'descripcion': 'Conservado', 'activo': True})
        self.engine.dispose()
        with self.sessions() as session:
            modelo = session.scalar(select(GeneroModel).where(GeneroModel.id == ident))
            self.assertEqual(modelo.nombre, 'Persistente editado')
        self.assertEqual(self.request('GET', f'/generos/{ident}')[1]['descripcion'], 'Conservado')

    def test_contrato_solo_publica_cinco_operaciones(self):
        status, schema = self.request('GET', '/openapi.json')
        self.assertEqual(status, 200)
        operaciones = [(path, method) for path, methods in schema['paths'].items()
                       for method in methods if method in {'get', 'post', 'put', 'patch', 'delete'}]
        self.assertEqual(len(operaciones), 5)
        self.assertEqual({path for path, _ in operaciones}, {'/generos', '/generos/{genero_id}'})


if __name__ == '__main__':
    unittest.main()
