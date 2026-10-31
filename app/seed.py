"""Carga de datos iniciales (seeders).

Se ejecuta automáticamente al iniciar la API y también a mano:

    uv run python -m app.seed

Cada entidad se siembra SOLO si su tabla está vacía, así que es seguro
ejecutarlo varias veces. El orden importa por las claves foráneas:
géneros -> usuarios -> películas -> reseñas.
"""

from application.services.genero_service import GeneroService
from infrastructure.database import SessionLocal
from infrastructure.repositories.genero_repository import GeneroRepository
from infrastructure.seeders.genero_seeder import seed_generos

# TODO(Matías): imports de los seeders de usuarios, películas y reseñas


def cargar_datos_iniciales() -> None:
    with SessionLocal() as session:
        genero_repository = GeneroRepository(session)

        if genero_repository.contar() == 0:
            seed_generos(GeneroService(genero_repository))

        # TODO(Matías): sembrar usuarios (si la tabla está vacía)

        # TODO(Matías): sembrar películas (necesitan géneros)

        # TODO(Matías): sembrar reseñas (necesitan usuarios y películas)


if __name__ == "__main__":
    cargar_datos_iniciales()
    print("Seeders ejecutados.")
