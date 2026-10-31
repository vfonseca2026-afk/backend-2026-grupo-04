"""TODO(Matías) — Repositorio de Usuario (único lugar que consulta la BD).

Patrón a copiar: el recorrido completo de Género (domain -> model -> mapper -> repository -> service -> DTO -> router).
Archivo de referencia: infrastructure/repositories/genero_repository.py

Clase UsuarioRepository(session) con estos métodos:
  crear(usuario) -> Usuario
  obtener_por_id(usuario_id) -> Usuario | None     <- LO USA ResenaService (Danna):
                                                      publícalo en tu primer PR
  obtener_por_email(email) -> Usuario | None       (comparar en minúsculas)
  obtener_por_nombre_usuario(nombre) -> Usuario | None
  listar(offset, limite) -> list[Usuario]         (ordenado por id)
  contar() -> int
  actualizar(usuario) -> Usuario
  eliminar(usuario_id) -> bool
"""
