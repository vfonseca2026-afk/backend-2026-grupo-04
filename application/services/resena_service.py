from domain.exceptions import (
    ConflictoError,
    RecursoNoEncontradoError,
    ReglaNegocioError,
)
from domain.resena import Resena
from infrastructure.repositories.pelicula_repository import PeliculaRepository
from infrastructure.repositories.resena_repository import ResenaRepository
from infrastructure.repositories.usuario_repository import UsuarioRepository


class ResenaService:
    """Coordina reseñas y aplica las reglas de publicación."""

    def __init__(
        self,
        repository: ResenaRepository,
        usuario_repository: UsuarioRepository,
        pelicula_repository: PeliculaRepository,
    ) -> None:
        self.repository = repository
        self.usuario_repository = usuario_repository
        self.pelicula_repository = pelicula_repository

    def crear(
        self,
        usuario_id: int,
        pelicula_id: int,
        puntuacion: int,
        titulo: str,
        comentario: str,
    ) -> Resena:
        self._validar_publicacion(usuario_id, pelicula_id)

        if self.repository.existe_de_usuario_en_pelicula(
            usuario_id,
            pelicula_id,
        ):
            raise ConflictoError(
                "El usuario ya tiene una reseña de esta película."
            )

        resena = Resena(
            usuario_id=usuario_id,
            pelicula_id=pelicula_id,
            puntuacion=puntuacion,
            titulo=titulo,
            comentario=comentario,
        )

        return self.repository.crear(resena)

    def obtener(self, resena_id: int) -> Resena:
        resena = self.repository.obtener_por_id(resena_id)

        if resena is None:
            raise RecursoNoEncontradoError(
                "No existe una reseña con el ID solicitado."
            )

        return resena

    def listar(
        self,
        usuario_id: int | None = None,
        pelicula_id: int | None = None,
        pagina: int = 1,
        limite: int = 10,
    ) -> tuple[list[Resena], int]:
        return self.repository.listar(
            usuario_id=usuario_id,
            pelicula_id=pelicula_id,
            offset=(pagina - 1) * limite,
            limite=limite,
        )

    def listar_por_pelicula(
        self,
        pelicula_id: int,
        pagina: int = 1,
        limite: int = 10,
    ) -> tuple[list[Resena], int]:
        self._obtener_pelicula(pelicula_id)

        return self.repository.listar_por_pelicula(
            pelicula_id=pelicula_id,
            offset=(pagina - 1) * limite,
            limite=limite,
        )

    def actualizar(
        self,
        resena_id: int,
        puntuacion: int,
        titulo: str,
        comentario: str,
    ) -> Resena:
        actual = self.obtener(resena_id)

        # Editar una publicación también exige que su autor siga activo
        # y que la película cumpla el criterio de estreno.
        self._validar_publicacion(
            actual.usuario_id,
            actual.pelicula_id,
        )

        actualizada = Resena(
            id=actual.id,
            usuario_id=actual.usuario_id,
            pelicula_id=actual.pelicula_id,
            puntuacion=puntuacion,
            titulo=titulo,
            comentario=comentario,
            fecha=actual.fecha,
        )

        return self.repository.actualizar(actualizada)

    def eliminar(self, resena_id: int) -> None:
        self.obtener(resena_id)
        self.repository.eliminar(resena_id)

    def _obtener_pelicula(self, pelicula_id: int):
        pelicula = self.pelicula_repository.obtener_por_id(pelicula_id)

        if pelicula is None:
            raise RecursoNoEncontradoError(
                "No existe una película con el ID solicitado."
            )

        return pelicula

    def _validar_publicacion(
        self,
        usuario_id: int,
        pelicula_id: int,
    ) -> None:
        usuario = self.usuario_repository.obtener_por_id(usuario_id)

        if usuario is None:
            raise RecursoNoEncontradoError(
                "No existe un usuario con el ID solicitado."
            )

        pelicula = self._obtener_pelicula(pelicula_id)

        if not usuario.puede_resenar():
            raise ReglaNegocioError(
                "Un usuario inactivo no puede publicar ni editar reseñas."
            )

        if not pelicula.esta_estrenada():
            raise ReglaNegocioError(
                "No se puede reseñar una película cuyo año "
                "de estreno sea posterior al año actual."
            )