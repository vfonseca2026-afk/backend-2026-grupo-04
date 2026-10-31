from fastapi import FastAPI

from presentation.error_handlers import registrar_manejadores_de_errores
from presentation.routers.genero_router import router as genero_router
from presentation.routers.pelicula_router import router as pelicula_router
from presentation.routers.usuario_router import router as usuario_router

# TODO(Danna): importar resena_router.

DESCRIPCION = """
API REST para **reseñar películas** (estilo IMDb).

Actualmente están disponibles los CRUD de Géneros, Usuarios y Películas.
El catálogo permite filtrar, ordenar y paginar las películas.

La funcionalidad de Reseñas está pendiente de integración.

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
app.include_router(pelicula_router)

# TODO(Danna): app.include_router(resena_router)