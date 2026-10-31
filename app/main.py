from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.seed import cargar_datos_iniciales
from presentation.error_handlers import registrar_manejadores_de_errores
from presentation.routers.genero_router import router as genero_router

# --- Cada integrante reemplaza SU línea cuando termine su router ---
# TODO(Matías): from presentation.routers.usuario_router import router as usuario_router

# TODO(Miguel): from presentation.routers.pelicula_router import router as pelicula_router

# TODO(Danna): from presentation.routers.resena_router import router as resena_router

DESCRIPCION = """
API REST para **reseñar películas** (estilo IMDb).

Las personas aficionadas al cine registran películas por género y publican
reseñas con puntuación de 1 a 10. Todos los errores controlados usan el mismo
formato JSON: `{"error": {"code", "message", "details"}}`.
"""


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    # Las tablas las crea Alembic (uv run alembic upgrade head).
    cargar_datos_iniciales()
    yield


app = FastAPI(
    title="API de Reseñas de Películas",
    version="0.1.0",
    description=DESCRIPCION,
    lifespan=lifespan,
)

registrar_manejadores_de_errores(app)

app.include_router(genero_router)

# TODO(Matías): app.include_router(usuario_router)

# TODO(Miguel): app.include_router(pelicula_router)

# TODO(Danna): app.include_router(resena_router)
