from sqlalchemy import func, select
from sqlalchemy.orm import Session

from domain.pelicula import Clasificacion, Pelicula
from infrastructure.mappers import pelicula_mapper
from infrastructure.models.pelicula_model import PeliculaModel


class PeliculaRepository:
    """Acceso persistente a películas mediante SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def crear(self, pelicula: Pelicula) -> Pelicula:
        modelo = pelicula_mapper.a_modelo(pelicula)

        self.session.add(modelo)
        self.session.commit()
        self.session.refresh(modelo)

        return pelicula_mapper.a_dominio(modelo)

    def obtener_por_id(self, pelicula_id: int) -> Pelicula | None:
        modelo = self.session.get(PeliculaModel, pelicula_id)

        if modelo is None:
            return None

        return pelicula_mapper.a_dominio(modelo)

    def contar(self) -> int:
        return self.session.scalar(
            select(func.count()).select_from(PeliculaModel)
        )

    def listar_filtrado(
        self,
        genero_id: int | None = None,
        anio: int | None = None,
        clasificacion: Clasificacion | None = None,
        titulo: str | None = None,
        ordenar_por: str = "titulo",
        direccion: str = "asc",
        offset: int = 0,
        limite: int = 10,
    ) -> tuple[list[Pelicula], int]:
        columnas = {
            "titulo": PeliculaModel.titulo,
            "anio_estreno": PeliculaModel.anio_estreno,
            "duracion_min": PeliculaModel.duracion_min,
        }

        columna = columnas[ordenar_por]

        filtros = []

        if genero_id is not None:
            filtros.append(PeliculaModel.genero_id == genero_id)

        if anio is not None:
            filtros.append(PeliculaModel.anio_estreno == anio)

        if clasificacion is not None:
            filtros.append(
                PeliculaModel.clasificacion == clasificacion.value
            )

        if titulo is not None:
            filtros.append(
                PeliculaModel.titulo.icontains(titulo, autoescape=True)
            )

        # El total se calcula sobre todos los registros filtrados,
        # antes de aplicar la paginación.
        total = self.session.scalar(
            select(func.count())
            .select_from(PeliculaModel)
            .where(*filtros)
        )

        orden = (
            columna.desc()
            if direccion == "desc"
            else columna.asc()
        )

        consulta = (
            select(PeliculaModel)
            .where(*filtros)
            .order_by(orden, PeliculaModel.id.asc())
            .offset(offset)
            .limit(limite)
        )

        modelos = self.session.scalars(consulta).all()

        items = [
            pelicula_mapper.a_dominio(modelo)
            for modelo in modelos
        ]

        return items, total

    def actualizar(self, pelicula: Pelicula) -> Pelicula:
        modelo = self.session.get(PeliculaModel, pelicula.id)

        if modelo is None:
            raise LookupError("La película no existe.")

        pelicula_mapper.actualizar_modelo(modelo, pelicula)

        self.session.commit()
        self.session.refresh(modelo)

        return pelicula_mapper.a_dominio(modelo)

    def eliminar(self, pelicula_id: int) -> bool:
        modelo = self.session.get(PeliculaModel, pelicula_id)

        if modelo is None:
            return False

        self.session.delete(modelo)
        self.session.commit()

        return True