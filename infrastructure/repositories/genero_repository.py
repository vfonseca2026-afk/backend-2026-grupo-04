from sqlalchemy import func, select
from sqlalchemy.orm import Session

from domain.genero import Genero
from infrastructure.mappers import genero_mapper
from infrastructure.models.genero_model import GeneroModel
from infrastructure.models.pelicula_model import PeliculaModel


class GeneroRepository:
    """Acceso a datos de géneros. Es la ÚNICA capa que consulta la BD."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def crear(self, genero: Genero) -> Genero:
        modelo = genero_mapper.a_modelo(genero)

        self.session.add(modelo)
        self.session.commit()
        self.session.refresh(modelo)

        return genero_mapper.a_dominio(modelo)

    def obtener_por_id(self, genero_id: int) -> Genero | None:
        modelo = self.session.get(GeneroModel, genero_id)

        if modelo is None:
            return None

        return genero_mapper.a_dominio(modelo)

    def obtener_por_nombre(self, nombre: str) -> Genero | None:
        modelo = self.session.scalars(
            select(GeneroModel).where(
                func.lower(GeneroModel.nombre) == nombre.strip().lower()
            )
        ).first()

        if modelo is None:
            return None

        return genero_mapper.a_dominio(modelo)

    def listar(self, solo_activos: bool = False) -> list[Genero]:
        consulta = select(GeneroModel).order_by(GeneroModel.nombre)

        if solo_activos:
            consulta = consulta.where(GeneroModel.activo.is_(True))

        modelos = self.session.scalars(consulta).all()

        return [genero_mapper.a_dominio(modelo) for modelo in modelos]

    def contar(self) -> int:
        return self.session.scalar(
            select(func.count()).select_from(GeneroModel)
        )

    def contar_peliculas(self, genero_id: int) -> int:
        """Cuántas películas pertenecen al género (relación 1:N)."""
        return self.session.scalar(
            select(func.count())
            .select_from(PeliculaModel)
            .where(PeliculaModel.genero_id == genero_id)
        )

    def actualizar(self, genero: Genero) -> Genero:
        modelo = self.session.get(GeneroModel, genero.id)

        if modelo is None:
            raise LookupError("El género no existe.")

        genero_mapper.actualizar_modelo(modelo, genero)
        self.session.commit()
        self.session.refresh(modelo)

        return genero_mapper.a_dominio(modelo)

    def eliminar(self, genero_id: int) -> bool:
        modelo = self.session.get(GeneroModel, genero_id)

        if modelo is None:
            return False

        self.session.delete(modelo)
        self.session.commit()
        return True
