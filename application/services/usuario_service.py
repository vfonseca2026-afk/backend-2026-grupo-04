from domain.exceptions import ConflictoError, RecursoNoEncontradoError
from domain.usuario import Usuario
from infrastructure.repositories.usuario_repository import UsuarioRepository


class UsuarioService:
    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository

    def crear(self, nombre_usuario: str, email: str) -> Usuario:
        usuario = Usuario(nombre_usuario=nombre_usuario, email=email)

        self._validar_datos_disponibles(usuario)

        return self.repository.crear(usuario)

    def obtener(self, usuario_id: int) -> Usuario:
        usuario = self.repository.obtener_por_id(usuario_id)

        if usuario is None:
            raise RecursoNoEncontradoError(
                "No existe un usuario con el ID solicitado."
            )

        return usuario

    def listar(
        self, pagina: int, limite: int
    ) -> tuple[list[Usuario], int]:
        offset = (pagina - 1) * limite

        usuarios = self.repository.listar(offset=offset, limite=limite)
        total = self.repository.contar()

        return usuarios, total

    def actualizar(
        self,
        usuario_id: int,
        nombre_usuario: str,
        email: str,
        activo: bool,
    ) -> Usuario:
        actual = self.obtener(usuario_id)

        actualizado = Usuario(
            id=actual.id,
            nombre_usuario=nombre_usuario,
            email=email,
            activo=activo,
            fecha_registro=actual.fecha_registro,
        )

        self._validar_datos_disponibles(actualizado)

        return self.repository.actualizar(actualizado)

    def eliminar(self, usuario_id: int) -> None:
        self.obtener(usuario_id)
        self.repository.eliminar(usuario_id)

    def _validar_datos_disponibles(self, usuario: Usuario) -> None:
        existente = self.repository.obtener_por_email(usuario.email)

        if existente is not None and existente.id != usuario.id:
            raise ConflictoError(
                "Ya existe un usuario con ese correo electrónico."
            )

        existente = self.repository.obtener_por_nombre_usuario(
            usuario.nombre_usuario
        )

        if existente is not None and existente.id != usuario.id:
            raise ConflictoError(
                "Ya existe un usuario con ese nombre de usuario."
            )