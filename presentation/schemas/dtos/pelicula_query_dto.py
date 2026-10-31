"""TODO(Miguel) — Parámetros de consulta de GET /peliculas.

Heredar de PaginacionQueryDTO (ya trae pagina, limite 1-100 y direccion asc/desc)
y agregar:
  genero_id: int | None          -> filtro por género
  anio: int | None               -> filtro por anio_estreno
  clasificacion: Clasificacion | None
  titulo: str | None             -> filtro "contiene" (opcional)
  ordenar_por: Literal["titulo", "anio_estreno", "duracion_min"] = "titulo"

Ejemplo:
  GET /peliculas?genero_id=2&anio=2010&ordenar_por=titulo&direccion=asc&pagina=1&limite=10
En el router se recibe con:  query: Annotated[PeliculaQueryDTO, Query()]
"""
