from domain.usuario import Usuario
from infrastructure.models.usuario_model import UsuarioModel


def a_dominio(modelo: UsuarioModel) -> Usuario:
    return Usuario( 
      id= modelo.id,
      nombre_usuario=modelo.nombre_usuario,
      email=modelo.email,
      activo=modelo.activo,
      fecha_registro=modelo.fecha_registro,    
      )
    
def a_modelo(usuario: Usuario) -> UsuarioModel:
    return UsuarioModel(
      id=usuario.id,
      nombre_usuario=usuario.nombre_usuario,
      email=usuario.email,
      activo=usuario.activo,
    )

def actualizar_modelo(modelo: UsuarioModel, usuario: Usuario) -> None:
    modelo.nombre_usuario = usuario.nombre_usuario
    modelo.email = usuario.email
    modelo.activo = usuario.activo
