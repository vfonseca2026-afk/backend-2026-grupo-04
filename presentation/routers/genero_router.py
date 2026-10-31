from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query, Response, status

from application.services.genero_service import GeneroService
from presentation.dependencies import get_genero_service
from presentation.schemas.dtos.error_dto import (
    RESP_404,
    RESP_409,
    RESP_422,
)
from presentation.schemas.dtos.genero_dto import (
    GeneroCreateDTO,
    GeneroResponseDTO,
    GeneroUpdateDTO,
)

router = APIRouter(prefix="/generos", tags=["Géneros"])

# El servicio se construye por solicitud con su propia sesión de base de datos.
ServiceDep = Annotated[GeneroService, Depends(get_genero_service)]

GeneroId = Annotated[
    int,
    Path(gt=0, description="ID del género.", examples=[1]),
]

EJEMPLO_GENERO = {
    "id": 1,
    "nombre": "Drama",
    "descripcion": "Historias centradas en personajes.",
    "activo": True,
    "fecha_creacion": "2026-01-01T00:00:00Z",
}


def respuesta_genero(descripcion: str) -> dict:
    """Construye la documentación de una respuesta con un género."""
    return {
        "description": descripcion,
        "content": {
            "application/json": {
                "example": EJEMPLO_GENERO,
            }
        },
    }


@router.post(
    "",
    response_model=GeneroResponseDTO,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un género",
    description=(
        "Registra un nuevo género de películas. El nombre debe ser único "
        "(sin distinguir mayúsculas)."
    ),
    responses={
        201: respuesta_genero("Género creado correctamente."),
        **RESP_409,
        **RESP_422,
    },
)
def crear_genero(datos: GeneroCreateDTO, service: ServiceDep):
    genero = service.crear(
        nombre=datos.nombre,
        descripcion=datos.descripcion,
    )
    return GeneroResponseDTO.model_validate(genero)


@router.get(
    "",
    response_model=list[GeneroResponseDTO],
    summary="Listar géneros",
    description=(
        "Devuelve los géneros ordenados por nombre. "
        "Si solo_activos es true, devuelve únicamente los géneros activos."
    ),
    responses={
        200: {
            "description": "Lista de géneros ordenada por nombre.",
            "content": {
                "application/json": {
                    "example": [EJEMPLO_GENERO],
                }
            },
        },
        **RESP_422,
    },
)
def listar_generos(
    service: ServiceDep,
    solo_activos: Annotated[
        bool,
        Query(description="Si es true, excluye los géneros inactivos."),
    ] = False,
):
    generos = service.listar(solo_activos=solo_activos)
    return [
        GeneroResponseDTO.model_validate(genero)
        for genero in generos
    ]


@router.get(
    "/{genero_id}",
    response_model=GeneroResponseDTO,
    summary="Obtener un género por ID",
    description=(
        "Consulta un género existente mediante su identificador positivo."
    ),
    responses={
        200: respuesta_genero("Género encontrado."),
        **RESP_404,
        **RESP_422,
    },
)
def obtener_genero(genero_id: GeneroId, service: ServiceDep):
    return GeneroResponseDTO.model_validate(
        service.obtener(genero_id)
    )


@router.put(
    "/{genero_id}",
    response_model=GeneroResponseDTO,
    summary="Actualizar un género",
    description=(
        "Actualiza el nombre, la descripción y el estado activo del género. "
        "El nombre debe continuar siendo único, sin distinguir mayúsculas."
    ),
    responses={
        200: respuesta_genero("Género actualizado correctamente."),
        **RESP_404,
        **RESP_409,
        **RESP_422,
    },
)
def actualizar_genero(
    genero_id: GeneroId,
    datos: GeneroUpdateDTO,
    service: ServiceDep,
):
    genero = service.actualizar(
        genero_id=genero_id,
        nombre=datos.nombre,
        descripcion=datos.descripcion,
        activo=datos.activo,
    )
    return GeneroResponseDTO.model_validate(genero)


@router.delete(
    "/{genero_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un género",
    description=(
        "Elimina un género existente y devuelve una respuesta sin contenido. "
        "No se puede eliminar un género que tiene películas asociadas."
    ),
    responses={
        204: {
            "description": (
                "Género eliminado correctamente. Sin cuerpo de respuesta."
            )
        },
        **RESP_404,
        **RESP_409,
        **RESP_422,
    },
)
def eliminar_genero(genero_id: GeneroId, service: ServiceDep):
    service.eliminar(genero_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)