"""TODO(Miguel) — Router de Películas (prefix="/peliculas", tags=["Películas"]).

Patrón a copiar: el recorrido completo de Género (domain -> model -> mapper -> repository -> service -> DTO -> router).
Archivo de referencia: presentation/routers/genero_router.py

  POST   /peliculas                  201  crear
  GET    /peliculas                  200  listar con FILTRO + ORDEN + PAGINACIÓN
                                          response_model=PaginaDTO[PeliculaResponseDTO]
  GET    /peliculas/{pelicula_id}    200  obtener
  PUT    /peliculas/{pelicula_id}    200  actualizar
  DELETE /peliculas/{pelicula_id}    204  eliminar (borra también sus reseñas)
Sin consultas a la BD ni lógica de negocio en el router.
Al terminar: registrar el router en app/main.py y get_pelicula_service en
presentation/dependencies.py (reemplazando tus líneas TODO).
"""
