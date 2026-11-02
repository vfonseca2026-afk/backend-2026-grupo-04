"""Carga explícita de datos iniciales.

Ejecutar después de aplicar las migraciones:

    uv run python -m app.seed

Están integrados los seeders de las cuatro entidades.
Cada carga se ejecuta únicamente si su tabla está vacía.
No se completan cargas parciales.

Orden:
géneros -> usuarios -> películas -> reseñas.

Iniciar o reiniciar la API no ejecuta este módulo automáticamente.
"""

from application.services.genero_service import GeneroService
from application.services.pelicula_service import PeliculaService
from application.services.resena_service import ResenaService
from application.services.usuario_service import UsuarioService
from infrastructure.database import SessionLocal
from infrastructure.repositories.genero_repository import GeneroRepository
from infrastructure.repositories.pelicula_repository import PeliculaRepository
from infrastructure.repositories.resena_repository import ResenaRepository
from infrastructure.repositories.usuario_repository import UsuarioRepository
from infrastructure.seeders.genero_seeder import seed_generos
from infrastructure.seeders.pelicula_seeder import seed_peliculas
from infrastructure.seeders.resena_seeder import seed_resenas
from infrastructure.seeders.usuario_seeder import seed_usuarios


def cargar_datos_iniciales() -> None:
    """Carga cada entidad si su tabla está vacía."""
    with SessionLocal() as session:
        genero_repository = GeneroRepository(session)
        usuario_repository = UsuarioRepository(session)
        pelicula_repository = PeliculaRepository(session)
        resena_repository = ResenaRepository(session)

        if genero_repository.contar() == 0:
            seed_generos(GeneroService(genero_repository))
            print("Géneros iniciales cargados.")
        else:
            print(
                "Carga de géneros omitida: "
                "la tabla ya contiene registros."
            )

        if usuario_repository.contar() == 0:
            seed_usuarios(UsuarioService(usuario_repository))
            print("Usuarios iniciales cargados.")
        else:
            print(
                "Carga de usuarios omitida: "
                "la tabla ya contiene registros."
            )

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

        resena_service = ResenaService(
            repository=resena_repository,
            usuario_repository=usuario_repository,
            pelicula_repository=pelicula_repository,
        )

        if resena_repository.contar() == 0:
            seed_resenas(
                service=resena_service,
                usuario_repository=usuario_repository,
                pelicula_repository=pelicula_repository,
            )
            print("Reseñas iniciales cargadas.")
        else:
            print(
                "Carga de reseñas omitida: "
                "la tabla ya contiene registros."
            )


if __name__ == "__main__":
    cargar_datos_iniciales()