"""TODO(Danna) — Repositorio de Reseña.

Patrón a copiar: el recorrido completo de Género (domain -> model -> mapper -> repository -> service -> DTO -> router).
Archivo de referencia: infrastructure/repositories/genero_repository.py

Métodos:
  crear(resena) -> Resena
  obtener_por_id(resena_id) -> Resena | None
  existe_de_usuario_en_pelicula(usuario_id, pelicula_id) -> bool
  listar(usuario_id, pelicula_id, offset, limite) -> tuple[list[Resena], int]
        (filtros opcionales; devuelve items y total filtrado)
  listar_por_pelicula(pelicula_id, offset, limite) -> tuple[list[Resena], int]
  actualizar(resena) -> Resena
  eliminar(resena_id) -> bool
"""
