from domain.pelicula import Clasificacion, Pelicula
from infrastructure.models.pelicula_model import PeliculaModel


def a_dominio(modelo: PeliculaModel) -> Pelicula:
    return Pelicula(
        id=modelo.id,
        titulo=modelo.titulo,
        sinopsis=modelo.sinopsis,
        anio_estreno=modelo.anio_estreno,
        duracion_min=modelo.duracion_min,
        director=modelo.director,
        clasificacion=Clasificacion(modelo.clasificacion),
        genero_id=modelo.genero_id,
    )


def a_modelo(pelicula: Pelicula) -> PeliculaModel:
    return PeliculaModel(
        id=pelicula.id,
        titulo=pelicula.titulo,
        sinopsis=pelicula.sinopsis,
        anio_estreno=pelicula.anio_estreno,
        duracion_min=pelicula.duracion_min,
        director=pelicula.director,
        clasificacion=pelicula.clasificacion.value,
        genero_id=pelicula.genero_id,
    )


def actualizar_modelo(
    modelo: PeliculaModel,
    pelicula: Pelicula,
) -> None:
    modelo.titulo = pelicula.titulo
    modelo.sinopsis = pelicula.sinopsis
    modelo.anio_estreno = pelicula.anio_estreno
    modelo.duracion_min = pelicula.duracion_min
    modelo.director = pelicula.director
    modelo.clasificacion = pelicula.clasificacion.value
    modelo.genero_id = pelicula.genero_id