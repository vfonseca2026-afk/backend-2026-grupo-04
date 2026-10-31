"""Carga explícita de datos iniciales.

Ejecutar después de aplicar las migraciones:

    uv run python -m app.seed

Están integrados los seeders de Géneros, Usuarios y Películas.
Cada carga se ejecuta únicamente si su tabla está vacía.
No se completan cargas parciales.

Orden de carga:
géneros -> usuarios -> películas -> reseñas.

El seeder de Reseñas está pendiente de integración.
Iniciar o reiniciar la API no ejecuta este módulo automáticamente.
"""

from application.services.genero_service import GeneroService
from application.services.pelicula_service import PeliculaService
from application.services.usuario_service import UsuarioService
from infrastructure.database import SessionLocal
from infrastructure.repositories.genero_repository import GeneroRepository
from infrastructure.repositories.pelicula_repository import PeliculaRepository
from infrastructure.repositories.usuario_repository import UsuarioRepository
from infrastructure.seeders.genero_seeder import seed_generos
from infrastructure.seeders.pelicula_seeder import seed_peliculas
from infrastructure.seeders.usuario_seeder import seed_usuarios


def cargar_datos_iniciales() -> None:
    """Carga cada entidad implementada si su tabla está vacía."""
    with SessionLocal() as session:
        genero_repository = GeneroRepository(session)

        if genero_repository.contar() == 0:
            seed_generos(GeneroService(genero_repository))
            print("Géneros iniciales cargados.")
        else:
            print(
                "Carga de géneros omitida: "
                "la tabla ya contiene registros."
            )

        usuario_repository = UsuarioRepository(session)

        if usuario_repository.contar() == 0:
            seed_usuarios(UsuarioService(usuario_repository))
            print("Usuarios iniciales cargados.")
        else:
            print(
                "Carga de usuarios omitida: "
                "la tabla ya contiene registros."
            )

        pelicula_repository = PeliculaRepository(session)
        pelicula_service = PeliculaService(
            repository=pelicula_repository,
            genero_repository=genero_repository,
        )

        if pelicula_repository.contar() == 0:
            seed_peliculas(
                service=pelicula_service,
                genero_repository=genero_repository,
            )
            print("Películas iniciales cargadas.")
        else:
            print(
                "Carga de películas omitida: "
                "la tabla ya contiene registros."
            )

        # TODO(Danna): integrar reseñas después de usuarios y películas.


if __name__ == "__main__":
    cargar_datos_iniciales()