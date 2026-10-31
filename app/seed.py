"""Carga explícita de datos iniciales.

Ejecutar después de aplicar las migraciones:

    uv run python -m app.seed

Actualmente solo está implementado el seeder de Géneros.
Se ejecuta únicamente si su tabla está vacía; no completa cargas parciales.

El orden previsto para integrar los demás seeders es:
géneros -> usuarios -> películas -> reseñas.

Iniciar o reiniciar la API no ejecuta este módulo automáticamente.
"""

from application.services.genero_service import GeneroService
from infrastructure.database import SessionLocal
from infrastructure.repositories.genero_repository import GeneroRepository
from infrastructure.seeders.genero_seeder import seed_generos

from application.services.usuario_service import UsuarioService
from infrastructure.repositories.usuario_repository import UsuarioRepository
from infrastructure.seeders.usuario_seeder import seed_usuarios


def cargar_datos_iniciales() -> None:
    """Carga géneros iniciales si su tabla está vacía."""
    with SessionLocal() as session:
        genero_repository = GeneroRepository(session)

        if genero_repository.contar() == 0:
            seed_generos(GeneroService(genero_repository))
            print("Géneros iniciales cargados.")
        else:
            print("Carga de géneros omitida: la tabla ya contiene registros.")

        usuario_repository = UsuarioRepository(session)

        if usuario_repository.contar() == 0:
            seed_usuarios(UsuarioService(usuario_repository))
            print("Usuarios iniciales cargados.")
        else:
            print("Carga de usuarios omitida: la tabla ya contiene registros.")

        # TODO(Miguel): integrar películas después de géneros.

        # TODO(Danna): integrar reseñas después de usuarios y películas.


if __name__ == "__main__":
    cargar_datos_iniciales()