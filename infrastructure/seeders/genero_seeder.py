from application.services.genero_service import GeneroService


def seed_generos(service: GeneroService) -> None:
    """Carga géneros de ejemplo (usa el servicio, así respeta las reglas)."""

    generos = [
        ("Acción", "Persecuciones, combates y mucha adrenalina."),
        ("Drama", "Historias intensas centradas en los personajes."),
        ("Comedia", "Películas pensadas para hacer reír."),
        ("Ciencia ficción", "Futuros posibles, tecnología y espacio."),
        ("Terror", "Historias diseñadas para provocar miedo."),
    ]

    for nombre, descripcion in generos:
        service.crear(nombre=nombre, descripcion=descripcion)
