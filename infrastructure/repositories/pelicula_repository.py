from sqlalchemy import func, select
from sqlalchemy.orm import Session

from domain.pelicula import Pelicula
from infrastructure.mappers import pelicula_mapper
from infrastructure.models.pelicula_model import PeliculaModel


class PeliculaRepository:
    """Acceso persistente a películas mediante SQLAlchemy."""

    def init(self, session: Session) -> None:
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