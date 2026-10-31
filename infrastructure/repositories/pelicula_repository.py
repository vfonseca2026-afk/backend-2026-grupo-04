"""TODO(Miguel) — Repositorio de Película.

Patrón a copiar: el recorrido completo de Género (domain -> model -> mapper -> repository -> service -> DTO -> router).
Archivo de referencia: infrastructure/repositories/genero_repository.py

Métodos:
  crear(pelicula) -> Pelicula
  obtener_por_id(pelicula_id) -> Pelicula | None   <- LO USA ResenaService (Danna):
                                                      publícalo en tu primer PR
  listar_filtrado(genero_id, anio, clasificacion, titulo,
                  ordenar_por, direccion, offset, limite) -> tuple[list[Pelicula], int]
  actualizar(pelicula) -> Pelicula
  eliminar(pelicula_id) -> bool

listar_filtrado devuelve (items, total) y DEBE seguir este orden (guía 5.5):
  1) FILTRAR con where() -> 2) calcular total sobre lo filtrado
  3) ORDENAR con order_by() -> 4) PAGINAR con offset()/limit()
Columnas permitidas para ordenar: titulo, anio_estreno, duracion_min
(usar un diccionario nombre -> columna; nunca armar SQL con texto del usuario).
"""
