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
    int, Path(gt=0, description="ID del género.", examples=[1])
]


@router.post(
    "",
    response_model=GeneroResponseDTO,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un género",
    description=(
        "Registra un nuevo género de películas. El nombre debe ser único "
        "(sin distinguir mayúsculas)."
    ),
    responses={**RESP_409, **RESP_422},
)
def crear_genero(datos: GeneroCreateDTO, service: ServiceDep):
    genero = service.crear(nombre=datos.nombre, descripcion=datos.descripcion)
    return GeneroResponseDTO.model_validate(genero)


@router.get(
    "",
    response_model=list[GeneroResponseDTO],
    summary="Listar géneros",
    description="Devuelve todos los géneros ordenados por nombre.",
    responses={**RESP_422},
)
def listar_generos(
    service: ServiceDep,
    solo_activos: Annotated[
        bool, Query(description="Si es true, excluye los géneros inactivos.")
    ] = False,
):
    generos = service.listar(solo_activos=solo_activos)
    return [GeneroResponseDTO.model_validate(genero) for genero in generos]


@router.get(
    "/{genero_id}",
    response_model=GeneroResponseDTO,
    summary="Obtener un género por ID",
    description="Consulta un género existente mediante su identificador positivo.",
    responses={200: {"description": "Género encontrado.", "content": {"application/json": {"example": {"id": 1, "nombre": "Drama", "descripcion": "Historias centradas en personajes.", "activo": True, "fecha_creacion": "2026-01-01T00:00:00Z"}}}}, **RESP_404, **RESP_422},
)
def obtener_genero(genero_id: GeneroId, service: ServiceDep):
    return GeneroResponseDTO.model_validate(service.obtener(genero_id))


@router.put(
    "/{genero_id}",
    response_model=GeneroResponseDTO,
    summary="Actualizar un género",
    description="Reemplaza los datos del género. Se envían todos los campos.",
    responses={**RESP_404, **RESP_409, **RESP_422},
)
def actualizar_genero(
    genero_id: GeneroId, datos: GeneroUpdateDTO, service: ServiceDep
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
    description="No se puede eliminar un género que tiene películas asociadas.",
    responses={**RESP_404, **RESP_409, **RESP_422},
)
def eliminar_genero(genero_id: GeneroId, service: ServiceDep):
    service.eliminar(genero_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
