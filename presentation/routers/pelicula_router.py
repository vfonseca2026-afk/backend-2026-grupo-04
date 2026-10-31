from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query, Response, status

from application.services.pelicula_service import PeliculaService
from presentation.dependencies import get_pelicula_service
from presentation.schemas.dtos.error_dto import RESP_404, RESP_422
from presentation.schemas.dtos.pagina_dto import PaginaDTO
from presentation.schemas.dtos.pelicula_dto import (
    PeliculaCreateDTO,
    PeliculaResponseDTO,
    PeliculaUpdateDTO,
)
from presentation.schemas.dtos.pelicula_query_dto import PeliculaQueryDTO

router = APIRouter(prefix="/peliculas", tags=["Películas"])

ServiceDep = Annotated[
    PeliculaService,
    Depends(get_pelicula_service),
]

PeliculaId = Annotated[
    int,
    Path(
        gt=0,
        description="Identificador positivo de la película.",
        examples=[1],
    ),
]

EJEMPLO_PELICULA = {
    "id": 1,
    "titulo": "Horizonte lejano",
    "sinopsis": "Una expedición explora un planeta desconocido.",
    "anio_estreno": 2020,
    "duracion_min": 110,
    "director": "Ana Ejemplo",
    "clasificacion": "TP",
    "genero_id": 1,
}

RESPUESTA_NO_ENCONTRADO = {
    404: {
        **RESP_404[404],
        "content": {
            "application/json": {
                "examples": {
                    "pelicula_inexistente": {
                        "summary": "Película inexistente",
                        "value": {
                            "error": {
                                "code": "RESOURCE_NOT_FOUND",
                                "message": (
                                    "No existe una película con el ID solicitado."
                                ),
                                "details": [],
                            }
                        },
                    },
                    "genero_inexistente": {
                        "summary": "Género relacionado inexistente",
                        "value": {
                            "error": {
                                "code": "RESOURCE_NOT_FOUND",
                                "message": "No existe el género con ID 999.",
                                "details": [],
                            }
                        },
                    },
                }
            }
        },
    }
}


def respuesta_pelicula(descripcion: str) -> dict:
    """Documenta una respuesta exitosa con una película."""
    return {
        "description": descripcion,
        "content": {
            "application/json": {
                "example": EJEMPLO_PELICULA,
            }
        },
    }


@router.post(
    "",
    response_model=PeliculaResponseDTO,
    status_code=status.HTTP_201_CREATED,
    summary="Crear una película",
    description=(
        "Registra una película asociada a un género existente. "
        "Se permite registrar películas con año de estreno futuro."
    ),
    responses={
        201: respuesta_pelicula("Película creada correctamente."),
        **RESPUESTA_NO_ENCONTRADO,
        **RESP_422,
    },
)
def crear_pelicula(
    datos: PeliculaCreateDTO,
    service: ServiceDep,
):
    pelicula = service.crear(**datos.model_dump())
    return PeliculaResponseDTO.model_validate(pelicula)


@router.get(
    "",
    response_model=PaginaDTO[PeliculaResponseDTO],
    summary="Listar películas con filtros, orden y paginación",
    description=(
        "Permite combinar filtros por género, año, clasificación y texto "
        "contenido en el título. Primero filtra, después ordena y finalmente "
        "pagina. El total corresponde a todos los registros filtrados. "
        "La página comienza en 1 y el límite admite entre 1 y 100 elementos."
    ),
    responses={
        200: {
            "description": "Página de películas y metadatos de la consulta.",
            "content": {
                "application/json": {
                    "examples": {
                        "con_resultados": {
                            "summary": "Consulta con una coincidencia",
                            "value": {
                                "items": [EJEMPLO_PELICULA],
                                "total": 1,
                                "pagina": 1,
                                "limite": 10,
                                "total_paginas": 1,
                            },
                        },
                        "sin_resultados": {
                            "summary": "Consulta sin coincidencias",
                            "value": {
                                "items": [],
                                "total": 0,
                                "pagina": 1,
                                "limite": 10,
                                "total_paginas": 0,
                            },
                        },
                    }
                }
            },
        },
        **RESP_422,
    },
)
def listar_peliculas(
    query: Annotated[PeliculaQueryDTO, Query()],
    service: ServiceDep,
):
    peliculas, total = service.listar(**query.model_dump())

    items = [
        PeliculaResponseDTO.model_validate(pelicula)
        for pelicula in peliculas
    ]

    return PaginaDTO[PeliculaResponseDTO].crear(
        items=items,
        total=total,
        pagina=query.pagina,
        limite=query.limite,
    )


@router.get(
    "/{pelicula_id}",
    response_model=PeliculaResponseDTO,
    summary="Obtener una película por ID",
    description="Consulta una película mediante su identificador positivo.",
    responses={
        200: respuesta_pelicula("Película encontrada."),
        **RESPUESTA_NO_ENCONTRADO,
        **RESP_422,
    },
)
def obtener_pelicula(
    pelicula_id: PeliculaId,
    service: ServiceDep,
):
    return PeliculaResponseDTO.model_validate(
        service.obtener(pelicula_id)
    )


@router.put(
    "/{pelicula_id}",
    response_model=PeliculaResponseDTO,
    summary="Actualizar una película",
    description=(
        "Reemplaza todos los campos editables de una película existente. "
        "El género indicado debe existir. El ID se conserva."
    ),
    responses={
        200: respuesta_pelicula("Película actualizada correctamente."),
        **RESPUESTA_NO_ENCONTRADO,
        **RESP_422,
    },
)
def actualizar_pelicula(
    pelicula_id: PeliculaId,
    datos: PeliculaUpdateDTO,
    service: ServiceDep,
):
    pelicula = service.actualizar(
        pelicula_id=pelicula_id,
        **datos.model_dump(),
    )
    return PeliculaResponseDTO.model_validate(pelicula)


@router.delete(
    "/{pelicula_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar una película",
    description=(
        "Elimina una película existente y sus reseñas asociadas. "
        "Devuelve una respuesta sin contenido."
    ),
    responses={
        204: {
            "description": "Película eliminada. Sin cuerpo de respuesta.",
        },
        **RESPUESTA_NO_ENCONTRADO,
        **RESP_422,
    },
)
def eliminar_pelicula(
    pelicula_id: PeliculaId,
    service: ServiceDep,
):
    service.eliminar(pelicula_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)