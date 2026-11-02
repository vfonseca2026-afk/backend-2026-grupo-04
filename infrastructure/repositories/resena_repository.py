from sqlalchemy import func, select
from sqlalchemy.orm import Session

from domain.resena import Resena
from infrastructure.mappers import resena_mapper
from infrastructure.models.resena_model import ResenaModel


class ResenaRepository:
    """Acceso persistente a reseñas mediante SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def crear(self, resena: Resena) -> Resena:
        modelo = resena_mapper.a_modelo(resena)

        self.session.add(modelo)
        self.session.commit()
        self.session.refresh(modelo)

        return resena_mapper.a_dominio(modelo)

    def obtener_por_id(self, resena_id: int) -> Resena | None:
        modelo = self.session.get(ResenaModel, resena_id)

        if modelo is None:
            return None

        return resena_mapper.a_dominio(modelo)

    def contar(self) -> int:
        return self.session.scalar(
            select(func.count()).select_from(ResenaModel)
        )

    def existe_de_usuario_en_pelicula(
        self,
        usuario_id: int,
        pelicula_id: int,
    ) -> bool:
        consulta = select(ResenaModel.id).where(
            ResenaModel.usuario_id == usuario_id,
            ResenaModel.pelicula_id == pelicula_id,
        )

        return self.session.scalar(consulta) is not None

    def listar(
        self,
        usuario_id: int | None = None,
        pelicula_id: int | None = None,
        offset: int = 0,
        limite: int = 10,
    ) -> tuple[list[Resena], int]:
        filtros = []

        if usuario_id is not None:
            filtros.append(ResenaModel.usuario_id == usuario_id)

        if pelicula_id is not None:
            filtros.append(ResenaModel.pelicula_id == pelicula_id)

        total = self.session.scalar(
            select(func.count())
            .select_from(ResenaModel)
            .where(*filtros)
        )

        consulta = (
            select(ResenaModel)
            .where(*filtros)
            .order_by(ResenaModel.id.asc())
            .offset(offset)
            .limit(limite)
        )

        modelos = self.session.scalars(consulta).all()

        items = [
            resena_mapper.a_dominio(modelo)
            for modelo in modelos
        ]

        return items, total

    def listar_por_pelicula(
        self,
        pelicula_id: int,
        offset: int = 0,
        limite: int = 10,
    ) -> tuple[list[Resena], int]:
        return self.listar(
            pelicula_id=pelicula_id,
            offset=offset,
            limite=limite,
        )

    def actualizar(self, resena: Resena) -> Resena:
        modelo = self.session.get(ResenaModel, resena.id)

        if modelo is None:
            raise LookupError("La reseña no existe.")

        resena_mapper.actualizar_modelo(modelo, resena)

        self.session.commit()
        self.session.refresh(modelo)

        return resena_mapper.a_dominio(modelo)

    def eliminar(self, resena_id: int) -> bool:
        modelo = self.session.get(ResenaModel, resena_id)

        if modelo is None:
            return False

        self.session.delete(modelo)
        self.session.commit()

        return True