from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query, Response, status

from application.services.resena_service import ResenaService
from presentation.dependencies import get_resena_service
from presentation.schemas.dtos.error_dto import (
    RESP_400,
    RESP_404,
    RESP_409,
    RESP_422,
)
from presentation.schemas.dtos.pagina_dto import PaginaDTO
from presentation.schemas.dtos.resena_dto import (
    ResenaCreateDTO,
    ResenaResponseDTO,
    ResenaUpdateDTO,
)

router = APIRouter(tags=["Reseñas"])

ServiceDep = Annotated[ResenaService, Depends(get_resena_service)]

ResenaId = Annotated[
    int,
    Path(gt=0, description="ID de la reseña.", examples=[1]),
]

PeliculaId = Annotated[
    int,
    Path(gt=0, description="ID de la película.", examples=[1]),
]

Pagina = Annotated[
    int,
    Query(ge=1, description="Número de página, desde 1."),
]

Limite = Annotated[
    int,
    Query(ge=1, le=100, description="Elementos por página, entre 1 y 100."),
]

EJEMPLO_RESENA = {
    "id": 1,
    "usuario_id": 1,
    "pelicula_id": 1,
    "puntuacion": 8,
    "titulo": "Una historia recomendable",
    "comentario": "Buenos personajes y una historia entretenida.",
    "fecha": "2026-01-01T00:00:00Z",
}


def respuesta_resena(descripcion: str) -> dict:
    return {
        "description": descripcion,
        "content": {
            "application/json": {
                "example": EJEMPLO_RESENA,
            }
        },
    }


def respuesta_pagina() -> dict:
    return {
        "description": "Página de reseñas ordenadas por ID.",
        "content": {
            "application/json": {
                "example": {
                    "items": [EJEMPLO_RESENA],
                    "total": 1,
                    "pagina": 1,
                    "limite": 10,
                    "total_paginas": 1,
                }
            }
        },
    }


def construir_pagina(
    resenas,
    total: int,
    pagina: int,
    limite: int,
) -> PaginaDTO[ResenaResponseDTO]:
    items = [
        ResenaResponseDTO.model_validate(resena)
        for resena in resenas
    ]

    return PaginaDTO[ResenaResponseDTO].crear(
        items=items,
        total=total,
        pagina=pagina,
        limite=limite,
    )


@router.post(
    "/resenas",
    response_model=ResenaResponseDTO,
    status_code=status.HTTP_201_CREATED,
    summary="Crear una reseña",
    description=(
        "Publica una reseña de un usuario activo sobre una película cuyo "
        "año de estreno no sea posterior al actual. Ambos recursos deben "
        "existir y solo se admite una reseña por usuario y película."
    ),
    responses={
        201: respuesta_resena("Reseña creada correctamente."),
        **RESP_400,
        **RESP_404,
        **RESP_409,
        **RESP_422,
    },
)
def crear_resena(datos: ResenaCreateDTO, service: ServiceDep):
    resena = service.crear(**datos.model_dump())
    return ResenaResponseDTO.model_validate(resena)


@router.get(
    "/resenas",
    response_model=PaginaDTO[ResenaResponseDTO],
    summary="Listar reseñas",
    description=(
        "Lista reseñas ordenadas por ID, con filtros opcionales por "
        "usuario y película. El total se calcula sobre las coincidencias "
        "antes de paginar. Un filtro sin coincidencias devuelve una lista vacía."
    ),
    responses={
        200: respuesta_pagina(),
        **RESP_422,
    },
)
def listar_resenas(
    service: ServiceDep,
    pagina: Pagina = 1,
    limite: Limite = 10,
    usuario_id: Annotated[
        int | None,
        Query(gt=0, description="Filtra por ID de usuario."),
    ] = None,
    pelicula_id: Annotated[
        int | None,
        Query(gt=0, description="Filtra por ID de película."),
    ] = None,
):
    resenas, total = service.listar(
        usuario_id=usuario_id,
        pelicula_id=pelicula_id,
        pagina=pagina,
        limite=limite,
    )

    return construir_pagina(resenas, total, pagina, limite)


@router.get(
    "/resenas/{resena_id}",
    response_model=ResenaResponseDTO,
    summary="Obtener una reseña",
    description="Consulta una reseña existente por su identificador positivo.",
    responses={
        200: respuesta_resena("Reseña encontrada."),
        **RESP_404,
        **RESP_422,
    },
)
def obtener_resena(resena_id: ResenaId, service: ServiceDep):
    return ResenaResponseDTO.model_validate(
        service.obtener(resena_id)
    )


@router.put(
    "/resenas/{resena_id}",
    response_model=ResenaResponseDTO,
    summary="Actualizar una reseña",
    description=(
        "Reemplaza puntuación, título y comentario; los tres campos son "
        "obligatorios. Conserva usuario, película, ID y fecha. El autor debe "
        "seguir activo y la película debe cumplir el criterio de estreno."
    ),
    responses={
        200: respuesta_resena("Reseña actualizada correctamente."),
        **RESP_400,
        **RESP_404,
        **RESP_422,
    },
)
def actualizar_resena(
    resena_id: ResenaId,
    datos: ResenaUpdateDTO,
    service: ServiceDep,
):
    resena = service.actualizar(
        resena_id=resena_id,
        **datos.model_dump(),
    )
    return ResenaResponseDTO.model_validate(resena)


@router.delete(
    "/resenas/{resena_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar una reseña",
    description=(
        "Elimina una reseña existente y devuelve una respuesta sin contenido. "
        "No exige que su autor continúe activo."
    ),
    responses={
        204: {"description": "Reseña eliminada. Sin cuerpo de respuesta."},
        **RESP_404,
        **RESP_422,
    },
)
def eliminar_resena(resena_id: ResenaId, service: ServiceDep):
    service.eliminar(resena_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get(
    "/peliculas/{pelicula_id}/resenas",
    response_model=PaginaDTO[ResenaResponseDTO],
    summary="Consultar reseñas de una película",
    description=(
        "Comprueba que la película exista y devuelve sus reseñas paginadas, "
        "ordenadas por ID. Una película existente sin reseñas devuelve "
        "una colección vacía; una película inexistente produce 404."
    ),
    responses={
        200: respuesta_pagina(),
        **RESP_404,
        **RESP_422,
    },
)
def listar_resenas_por_pelicula(
    pelicula_id: PeliculaId,
    service: ServiceDep,
    pagina: Pagina = 1,
    limite: Limite = 10,
):
    resenas, total = service.listar_por_pelicula(
        pelicula_id=pelicula_id,
        pagina=pagina,
        limite=limite,
    )

    return construir_pagina(resenas, total, pagina, limite)