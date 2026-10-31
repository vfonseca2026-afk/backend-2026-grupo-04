"""TODO(Matías) — Servicio de Usuario (casos de uso y reglas de negocio).

Patrón a copiar: el recorrido completo de Género (domain -> model -> mapper -> repository -> service -> DTO -> router).
Archivo de referencia: application/services/genero_service.py

Métodos: crear, obtener, listar(pagina, limite), actualizar, eliminar.
Reglas (lanzan errores de domain/exceptions.py, NO HTTPException):
  - El email no puede repetirse            -> ConflictoError (409)
  - El nombre_usuario no puede repetirse   -> ConflictoError (409)
  - Si el usuario no existe                -> RecursoNoEncontradoError (404)
Eliminar un usuario borra también sus reseñas (ON DELETE CASCADE en la BD).
"""
