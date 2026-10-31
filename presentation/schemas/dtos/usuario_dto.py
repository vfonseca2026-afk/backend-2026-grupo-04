"""TODO(Matías) — DTO de Usuario.

Patrón a copiar: el recorrido completo de Género (domain -> model -> mapper -> repository -> service -> DTO -> router).
Archivo de referencia: presentation/schemas/dtos/genero_dto.py

  UsuarioCreateDTO : nombre_usuario (LONGITUD 3 a 50), email (FORMATO: EmailStr)
  UsuarioUpdateDTO : lo anterior + activo: bool
  UsuarioResponseDTO: id, nombre_usuario, email, activo, fecha_registro
Usar extra="forbid" y un json_schema_extra con un ejemplo (lo pide OpenAPI).
Para listar: response_model=PaginaDTO[UsuarioResponseDTO] (ver pagina_dto.py)
y PaginacionQueryDTO para pagina/limite.
"""
