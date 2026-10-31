from sqlalchemy import func, select
from sqlalchemy.orm import Session

from domain.usuario import Usuario
from infrastructure.mappers import usuario_mapper
from infrastructure.models.usuario_model import UsuarioModel


class UsuarioRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def crear(self, usuario: Usuario) -> Usuario:
        modelo = usuario_mapper.a_modelo(usuario)

        self.session.add(modelo)
        self.session.commit()
        self.session.refresh(modelo)

        return usuario_mapper.a_dominio(modelo)

    def obtener_por_id(self, usuario_id: int) -> Usuario | None:
        modelo = self.session.get(UsuarioModel, usuario_id)

        if modelo is None:
            return None

        return usuario_mapper.a_dominio(modelo)

    def obtener_por_email(self, email: str) -> Usuario | None:
        consulta = select(UsuarioModel).where(
            func.lower(UsuarioModel.email) == email.strip().lower()
        )
        modelo = self.session.scalars(consulta).first()

        if modelo is None:
            return None

        return usuario_mapper.a_dominio(modelo)

    def obtener_por_nombre_usuario(self, nombre: str) -> Usuario | None:
        consulta = select(UsuarioModel).where(
            func.lower(UsuarioModel.nombre_usuario) == nombre.strip().lower()
        )
        modelo = self.session.scalars(consulta).first()

        if modelo is None:
            return None

        return usuario_mapper.a_dominio(modelo)

    def listar(self, offset: int, limite: int) -> list[Usuario]:
        consulta = (
            select(UsuarioModel)
            .order_by(UsuarioModel.id)
            .offset(offset)
            .limit(limite)
        )
        modelos = self.session.scalars(consulta).all()

        return [usuario_mapper.a_dominio(modelo) for modelo in modelos]

    def contar(self) -> int:
        consulta = select(func.count()).select_from(UsuarioModel)
        return self.session.scalar(consulta)

    def actualizar(self, usuario: Usuario) -> Usuario:
        modelo = self.session.get(UsuarioModel, usuario.id)

        if modelo is None:
            raise LookupError("El usuario no existe.")

        usuario_mapper.actualizar_modelo(modelo, usuario)

        self.session.commit()
        self.session.refresh(modelo)

        return usuario_mapper.a_dominio(modelo)

    def eliminar(self, usuario_id: int) -> bool:
        modelo = self.session.get(UsuarioModel, usuario_id)

        if modelo is None:
            return False

        self.session.delete(modelo)
        self.session.commit()

        return True