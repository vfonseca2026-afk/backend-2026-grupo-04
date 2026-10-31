"""TODO(Miguel) — DTO de Película.

Patrón a copiar: el recorrido completo de Género (domain -> model -> mapper -> repository -> service -> DTO -> router).
Archivo de referencia: presentation/schemas/dtos/genero_dto.py

  PeliculaCreateDTO: titulo (LONGITUD 1-150), sinopsis (máx 2000, opcional),
                     anio_estreno (NUMÉRICA: >= 1888), duracion_min (NUMÉRICA: > 0),
                     director (LONGITUD 1-100),
                     clasificacion (VALORES PERMITIDOS: Enum Clasificacion de domain),
                     genero_id (> 0)
  PeliculaUpdateDTO: mismos campos (PUT reemplaza todo)
  PeliculaResponseDTO: todos los campos + id
Incluir json_schema_extra con ejemplo de solicitud.
"""
