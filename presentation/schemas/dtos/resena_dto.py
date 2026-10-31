"""TODO(Danna) — DTO de Reseña.

Patrón a copiar: el recorrido completo de Género (domain -> model -> mapper -> repository -> service -> DTO -> router).
Archivo de referencia: presentation/schemas/dtos/genero_dto.py

  ResenaCreateDTO: usuario_id (> 0), pelicula_id (> 0),
                   puntuacion (NUMÉRICA: ge=1, le=10),
                   titulo (LONGITUD 1-100),
                   comentario (LONGITUD: min 10, max 2000)
  ResenaUpdateDTO: puntuacion, titulo, comentario (sin usuario_id ni pelicula_id)
  ResenaResponseDTO: id, usuario_id, pelicula_id, puntuacion, titulo, comentario, fecha
Incluir json_schema_extra con ejemplos de solicitud.
"""
