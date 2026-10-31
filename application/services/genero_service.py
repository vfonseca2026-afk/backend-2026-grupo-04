from domain.exceptions import ConflictoError, RecursoNoEncontradoError
from domain.genero import Genero
from infrastructure.repositories.genero_repository import GeneroRepository


class GeneroService:
    """Casos de uso de géneros: aplica reglas y coordina el repositorio.

    Lanza errores de dominio (404/409/400); NO sabe nada de HTTP.
    """

    def __init__(self, repository: GeneroRepository) -> None:
        self.repository = repository

    def crear(self, nombre: str, descripcion: str = "") -> Genero:
        genero = Genero(nombre=nombre, descripcion=descripcion)

        self._validar_nombre_disponible(genero.nombre)

        return self.repository.crear(genero)

    def obtener(self, genero_id: int) -> Genero:
        genero = self.repository.obtener_por_id(genero_id)

        if genero is None:
            raise RecursoNoEncontradoError(
                "No existe un género con el ID solicitado."
            )

        return genero

    def listar(self, solo_activos: bool = False) -> list[Genero]:
        return self.repository.listar(solo_activos=solo_activos)

    def actualizar(
        self,
        genero_id: int,
        nombre: str,
        descripcion: str,
        activo: bool,
    ) -> Genero:
        actual = self.obtener(genero_id)

        actualizado = Genero(
            id=actual.id,
            nombre=nombre,
            descripcion=descripcion,
            activo=activo,
            fecha_creacion=actual.fecha_creacion,
        )

        self._validar_nombre_disponible(actualizado.nombre, genero_id)

        return self.repository.actualizar(actualizado)

    def eliminar(self, genero_id: int) -> None:
        self.obtener(genero_id)

        # Regla de negocio: no se elimina un género que tiene películas.
        if self.repository.contar_peliculas(genero_id) > 0:
            raise ConflictoError(
                "No se puede eliminar un género que tiene películas asociadas."
            )

        self.repository.eliminar(genero_id)

    def _validar_nombre_disponible(
        self, nombre: str, genero_id: int | None = None
    ) -> None:
        existente = self.repository.obtener_por_nombre(nombre)

        if existente is not None and existente.id != genero_id:
            raise ConflictoError("Ya existe un género con ese nombre.")
