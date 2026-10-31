"""TODO(Miguel) — Servicio de Película.

Patrón a copiar: el recorrido completo de Género (domain -> model -> mapper -> repository -> service -> DTO -> router).
Archivo de referencia: application/services/genero_service.py

Recibe PeliculaRepository y GeneroRepository.
Métodos: crear, obtener, listar(filtros, orden, pagina, limite), actualizar, eliminar.
Reglas:
  - El genero_id debe existir (EXISTENCIA RELACIONADA) -> RecursoNoEncontradoError (404)
    con un mensaje claro, por ejemplo "No existe el género con ID 99".
  - Película inexistente -> RecursoNoEncontradoError (404).
listar() devuelve (items, total); el router arma PaginaDTO.crear(...).
"""
