from datetime import date

from application.services.pelicula_service import PeliculaService
from domain.pelicula import Clasificacion
from infrastructure.repositories.genero_repository import GeneroRepository


def seed_peliculas(
    service: PeliculaService,
    genero_repository: GeneroRepository,
) -> None:
    """Carga películas ficticias usando géneros existentes."""
    generos = genero_repository.listar(solo_activos=True)

    if len(generos) < 2:
        raise RuntimeError(
            "Se necesitan al menos dos géneros activos "
            "para cargar las películas de ejemplo."
        )

    genero_a = generos[0].id
    genero_b = generos[1].id

    if genero_a is None or genero_b is None:
        raise RuntimeError("Los géneros deben estar guardados en la base.")

    peliculas = [
        {
            "titulo": "Horizonte lejano",
            "anio_estreno": 2020,
            "duracion_min": 110,
            "director": "Ana Ejemplo",
            "genero_id": genero_a,
            "clasificacion": Clasificacion.TODO_PUBLICO,
        },
        {
            "titulo": "Camino al norte",
            "anio_estreno": 2021,
            "duracion_min": 95,
            "director": "Luis Ejemplo",
            "genero_id": genero_a,
            "clasificacion": Clasificacion.MAYORES_14,
        },
        {
            "titulo": "La última estación",
            "anio_estreno": 2022,
            "duracion_min": 125,
            "director": "Marta Ejemplo",
            "genero_id": genero_a,
            "clasificacion": Clasificacion.TODO_PUBLICO,
        },
        {
            "titulo": "Ciudad de sombras",
            "anio_estreno": 2020,
            "duracion_min": 100,
            "director": "Pedro Ejemplo",
            "genero_id": genero_a,
            "clasificacion": Clasificacion.MAYORES_18,
        },
        {
            "titulo": "Un nuevo comienzo",
            "anio_estreno": 2023,
            "duracion_min": 105,
            "director": "Elena Ejemplo",
            "genero_id": genero_a,
            "clasificacion": Clasificacion.TODO_PUBLICO,
        },
        {
            "titulo": "El secreto del puerto",
            "anio_estreno": 2021,
            "duracion_min": 115,
            "director": "Carlos Ejemplo",
            "genero_id": genero_b,
            "clasificacion": Clasificacion.MAYORES_14,
        },
        {
            "titulo": "Días de verano",
            "anio_estreno": 2022,
            "duracion_min": 90,
            "director": "Sofía Ejemplo",
            "genero_id": genero_b,
            "clasificacion": Clasificacion.TODO_PUBLICO,
        },
        {
            "titulo": "Después de medianoche",
            "anio_estreno": 2023,
            "duracion_min": 120,
            "director": "Diego Ejemplo",
            "genero_id": genero_b,
            "clasificacion": Clasificacion.MAYORES_18,
        },
        {
            "titulo": "Una carta pendiente",
            "anio_estreno": 2024,
            "duracion_min": 98,
            "director": "Laura Ejemplo",
            "genero_id": genero_b,
            "clasificacion": Clasificacion.TODO_PUBLICO,
        },
        {
            "titulo": "Mañana comienza todo",
            "anio_estreno": date.today().year + 1,
            "duracion_min": 130,
            "director": "Andrés Ejemplo",
            "genero_id": genero_b,
            "clasificacion": Clasificacion.MAYORES_14,
        },
    ]

    for datos in peliculas:
        service.crear(
            **datos,
            sinopsis=(
                f"Sinopsis ficticia de {datos['titulo']} "
                "para las demostraciones del proyecto."
            ),
        )