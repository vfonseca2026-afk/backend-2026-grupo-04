"""TODO(Danna) — Router de Reseñas (tags=["Reseñas"]).

Patrón a copiar: el recorrido completo de Género (domain -> model -> mapper -> repository -> service -> DTO -> router).
Archivo de referencia: presentation/routers/genero_router.py
(Como en inscripcion_router.py del ejemplo, este router NO lleva prefix fijo
porque incluye una ruta anidada de películas.)

  POST   /resenas                          201  crear (aplica las 5 comprobaciones del servicio)
  GET    /resenas                          200  listar paginado (filtros opcionales usuario_id, pelicula_id)
  GET    /resenas/{resena_id}              200  obtener
  PUT    /resenas/{resena_id}              200  actualizar
  DELETE /resenas/{resena_id}              204  eliminar
  GET    /peliculas/{pelicula_id}/resenas  200  reseñas de una película (paginado)
Al terminar: registrar el router en app/main.py y get_resena_service en
presentation/dependencies.py (reemplazando tus líneas TODO).
"""
