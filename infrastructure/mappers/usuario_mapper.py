"""TODO(Matías) — Mapper de Usuario.

Patrón a copiar: el recorrido completo de Género (domain -> model -> mapper -> repository -> service -> DTO -> router).
Archivo de referencia: infrastructure/mappers/genero_mapper.py

Implementar 3 funciones:
  a_dominio(modelo: UsuarioModel) -> Usuario
  a_modelo(usuario: Usuario) -> UsuarioModel
  actualizar_modelo(modelo: UsuarioModel, usuario: Usuario) -> None
Campos: id, nombre_usuario, email, activo, fecha_registro.
"""
