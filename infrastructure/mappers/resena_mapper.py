from domain.resena import Resena
from infrastructure.models.resena_model import ResenaModel


def a_dominio(modelo: ResenaModel) -> Resena:
    return Resena(
        id=modelo.id,
        usuario_id=modelo.usuario_id,
        pelicula_id=modelo.pelicula_id,
        puntuacion=modelo.puntuacion,
        titulo=modelo.titulo,
        comentario=modelo.comentario,
        fecha=modelo.fecha,
    )


def a_modelo(resena: Resena) -> ResenaModel:
    return ResenaModel(
        id=resena.id,
        usuario_id=resena.usuario_id,
        pelicula_id=resena.pelicula_id,
        puntuacion=resena.puntuacion,
        titulo=resena.titulo,
        comentario=resena.comentario,
    )


def actualizar_modelo(
    modelo: ResenaModel,
    resena: Resena,
) -> None:
    modelo.puntuacion = resena.puntuacion
    modelo.titulo = resena.titulo
    modelo.comentario = resena.comentario