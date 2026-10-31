from fastapi import FastAPI

from presentation.error_handlers import registrar_manejadores_de_errores
from presentation.routers.genero_router import router as genero_router

# --- Cada integrante reemplaza SU línea cuando termine su router ---
from presentation.routers.usuario_router import router as usuario_router

# TODO(Miguel): from presentation.routers.pelicula_router import router as pelicula_router

# TODO(Danna): from presentation.routers.resena_router import router as resena_router

DESCRIPCION = """
API REST para **reseñar películas** (estilo IMDb).

El proyecto contempla un catálogo de películas y reseñas con puntuación
de 1 a 10. Actualmente está disponible el CRUD de Géneros.

Todos los errores controlados usan la estructura:
`{"error": {"code": "...", "message": "...", "details": []}}`.

Las tablas se preparan mediante migraciones y los datos iniciales se cargan
explícitamente con `uv run python -m app.seed`.
"""

app = FastAPI(
    title="API de Reseñas de Películas",
    version="0.1.0",
    description=DESCRIPCION,
)

registrar_manejadores_de_errores(app)

app.include_router(genero_router)

app.include_router(usuario_router)

# TODO(Miguel): app.include_router(pelicula_router)

# TODO(Danna): app.include_router(resena_router)