from domain.genero import Genero
from infrastructure.models.genero_model import GeneroModel


def a_dominio(modelo: GeneroModel) -> Genero:
    return Genero(
        id=modelo.id,
        nombre=modelo.nombre,
        descripcion=modelo.descripcion,
        activo=modelo.activo,
        fecha_creacion=modelo.fecha_creacion,
    )


def a_modelo(genero: Genero) -> GeneroModel:
    return GeneroModel(
        id=genero.id,
        nombre=genero.nombre,
        descripcion=genero.descripcion,
        activo=genero.activo,
    )


def actualizar_modelo(modelo: GeneroModel, genero: Genero) -> None:
    modelo.nombre = genero.nombre
    modelo.descripcion = genero.descripcion
    modelo.activo = genero.activo
