from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query, Response, status

from application.services.usuario_service import UsuarioService
from presentation.dependencies import get_usuario_service
from presentation.schemas.dtos.error_dto import RESP_404, RESP_409, RESP_422
from presentation.schemas.dtos.pagina_dto import PaginaDTO
from presentation.schemas.dtos.usuario_dto import (
    UsuarioCreateDTO,
    UsuarioResponseDTO,
    UsuarioUpdateDTO,
)

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

ServiceDep = Annotated[UsuarioService, Depends(get_usuario_service)]

UsuarioId = Annotated[
    int,
    Path(gt=0, description="ID del usuario.", examples=[1]),
]

EJEMPLO_USUARIO = {
    "id": 1,
    "nombre_usuario": "cinefilo",
    "email": "cinefilo@example.com",
    "activo": True,
    "fecha_registro": "2026-01-01T00:00:00Z",
}

EJEMPLO_USUARIO_ACTUALIZADO = {
    **EJEMPLO_USUARIO,
    "nombre_usuario": "cinefilo_actualizado",
    "email": "cinefilo.actualizado@example.com",
    "activo": False,
}


def respuesta_usuario(descripcion: str, ejemplo: dict) -> dict:
    """Documenta una respuesta exitosa con un usuario."""
    return {
        "description": descripcion,
        "content": {
            "application/json": {
                "example": ejemplo,
            }
        },
    }


@router.post(
    "",
    response_model=UsuarioResponseDTO,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un usuario",
    description="Registra un usuario con correo y nombre únicos.",
    responses={
        201: respuesta_usuario(
            "Usuario creado correctamente.",
            EJEMPLO_USUARIO,
        ),
        **RESP_409,
        **RESP_422,
    },
)
def crear_usuario(datos: UsuarioCreateDTO, service: ServiceDep):
    usuario = service.crear(
        nombre_usuario=datos.nombre_usuario,
        email=str(datos.email),
    )
    return UsuarioResponseDTO.model_validate(usuario)


@router.get(
    "",
    response_model=PaginaDTO[UsuarioResponseDTO],
    summary="Listar usuarios",
    description="Devuelve usuarios ordenados por ID, con paginación.",
    responses={
        200: {
            "description": "Página de usuarios y metadatos de paginación.",
            "content": {
                "application/json": {
                    "examples": {
                        "con_resultados": {
                            "summary": "Colección con un usuario",
                            "value": {
                                "items": [EJEMPLO_USUARIO],
                                "total": 1,
                                "pagina": 1,
                                "limite": 10,
                                "total_paginas": 1,
                            },
                        },
                        "sin_resultados": {
                            "summary": "Colección sin usuarios",
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
def listar_usuarios(
    service: ServiceDep,
    pagina: Annotated[
        int,
        Query(ge=1, description="Número de página, desde 1."),
    ] = 1,
    limite: Annotated[
        int,
        Query(
            ge=1,
            le=100,
            description="Usuarios por página, de 1 a 100.",
        ),
    ] = 10,
):
    usuarios, total = service.listar(pagina=pagina, limite=limite)
    items = [
        UsuarioResponseDTO.model_validate(usuario)
        for usuario in usuarios
    ]

    return PaginaDTO[UsuarioResponseDTO].crear(
        items=items,
        total=total,
        pagina=pagina,
        limite=limite,
    )


@router.get(
    "/{usuario_id}",
    response_model=UsuarioResponseDTO,
    summary="Obtener un usuario",
    description="Consulta un usuario mediante su identificador positivo.",
    responses={
        200: respuesta_usuario(
            "Usuario encontrado.",
            EJEMPLO_USUARIO,
        ),
        **RESP_404,
        **RESP_422,
    },
)
def obtener_usuario(usuario_id: UsuarioId, service: ServiceDep):
    return UsuarioResponseDTO.model_validate(
        service.obtener(usuario_id)
    )


@router.put(
    "/{usuario_id}",
    response_model=UsuarioResponseDTO,
    summary="Actualizar un usuario",
    description=(
        "Reemplaza el nombre, correo y estado del usuario. "
        "Conserva su ID y fecha de registro."
    ),
    responses={
        200: respuesta_usuario(
            "Usuario actualizado correctamente.",
            EJEMPLO_USUARIO_ACTUALIZADO,
        ),
        **RESP_404,
        **RESP_409,
        **RESP_422,
    },
)
def actualizar_usuario(
    usuario_id: UsuarioId,
    datos: UsuarioUpdateDTO,
    service: ServiceDep,
):
    usuario = service.actualizar(
        usuario_id=usuario_id,
        nombre_usuario=datos.nombre_usuario,
        email=str(datos.email),
        activo=datos.activo,
    )
    return UsuarioResponseDTO.model_validate(usuario)


@router.delete(
    "/{usuario_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un usuario",
    description="Elimina el usuario y sus reseñas asociadas.",
    responses={
        204: {
            "description": "Usuario eliminado. Sin cuerpo de respuesta.",
        },
        **RESP_404,
        **RESP_422,
    },
)
def eliminar_usuario(usuario_id: UsuarioId, service: ServiceDep):
    service.eliminar(usuario_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)