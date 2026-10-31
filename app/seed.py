"""Carga explícita de datos iniciales.

Ejecutar después de aplicar las migraciones:

    uv run python -m app.seed

Actualmente solo está implementado el seeder de Géneros.
Se ejecuta únicamente si su tabla está vacía; no completa cargas parciales.

El orden previsto para integrar los demás seeders es:
géneros -> usuarios -> películas -> reseñas.

Iniciar o reiniciar la API no ejecuta este módulo automáticamente.
"""

from application.services.genero_service import GeneroService
from infrastructure.database import SessionLocal
from infrastructure.repositories.genero_repository import GeneroRepository
from infrastructure.seeders.genero_seeder import seed_generos

# TODO(Matías): coordinar imports de los seeders restantes.


def cargar_datos_iniciales() -> None:
    """Carga géneros iniciales si su tabla está vacía."""
    with SessionLocal() as session:
        genero_repository = GeneroRepository(session)

        if genero_repository.contar() == 0:
            seed_generos(GeneroService(genero_repository))
            print("Géneros iniciales cargados.")
        else:
            print("Carga de géneros omitida: la tabla ya contiene registros.")

        # TODO(Matías): sembrar usuarios (si la tabla está vacía).

        # TODO(Miguel): integrar películas después de géneros.

        # TODO(Danna): integrar reseñas después de usuarios y películas.


if __name__ == "__main__":
    cargar_datos_iniciales()