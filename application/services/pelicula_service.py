from domain.exceptions import RecursoNoEncontradoError
from domain.pelicula import Clasificacion, Pelicula
from infrastructure.repositories.genero_repository import GeneroRepository
from infrastructure.repositories.pelicula_repository import PeliculaRepository


class PeliculaService:
    """Coordina películas y comprueba la existencia del género relacionado."""

    def __init__(
        self,
        repository: PeliculaRepository,
        genero_repository: GeneroRepository,
    ) -> None:
        self.repository = repository
        self.genero_repository = genero_repository

    def crear(
        self,
        titulo: str,
        anio_estreno: int,
        duracion_min: int,
        director: str,
        clasificacion: Clasificacion,
        genero_id: int,
        sinopsis: str = "",
    ) -> Pelicula:
        self._validar_genero(genero_id)

        pelicula = Pelicula(
            titulo=titulo,
            sinopsis=sinopsis,
            anio_estreno=anio_estreno,
            duracion_min=duracion_min,
            director=director,
            clasificacion=clasificacion,
            genero_id=genero_id,
        )

        return self.repository.crear(pelicula)

    def obtener(self, pelicula_id: int) -> Pelicula:
        pelicula = self.repository.obtener_por_id(pelicula_id)

        if pelicula is None:
            raise RecursoNoEncontradoError(
                "No existe una película con el ID solicitado."
            )

        return pelicula

    def listar(
        self,
        genero_id: int | None = None,
        anio: int | None = None,
        clasificacion: Clasificacion | None = None,
        titulo: str | None = None,
        ordenar_por: str = "titulo",
        direccion: str = "asc",
        pagina: int = 1,
        limite: int = 10,
    ) -> tuple[list[Pelicula], int]:
        offset = (pagina - 1) * limite

        return self.repository.listar_filtrado(
            genero_id=genero_id,
            anio=anio,
            clasificacion=clasificacion,
            titulo=titulo,
            ordenar_por=ordenar_por,
            direccion=direccion,
            offset=offset,
            limite=limite,
        )

    def actualizar(
        self,
        pelicula_id: int,
        titulo: str,
        sinopsis: str,
        anio_estreno: int,
        duracion_min: int,
        director: str,
        clasificacion: Clasificacion,
        genero_id: int,
    ) -> Pelicula:
        actual = self.obtener(pelicula_id)
        self._validar_genero(genero_id)

        pelicula = Pelicula(
            id=actual.id,
            titulo=titulo,
            sinopsis=sinopsis,
            anio_estreno=anio_estreno,
            duracion_min=duracion_min,
            director=director,
            clasificacion=clasificacion,
            genero_id=genero_id,
        )

        return self.repository.actualizar(pelicula)

    def eliminar(self, pelicula_id: int) -> None:
        self.obtener(pelicula_id)
        self.repository.eliminar(pelicula_id)

    def _validar_genero(self, genero_id: int) -> None:
        if self.genero_repository.obtener_por_id(genero_id) is None:
            raise RecursoNoEncontradoError(
                f"No existe el género con ID {genero_id}."
            )