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
    int, Path(gt=0, description="ID del usuario.", examples=[1])
]


@router.post(
    "",
    response_model=UsuarioResponseDTO,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un usuario",
    description="Registra un usuario con correo y nombre únicos.",
    responses={**RESP_409, **RESP_422},
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
    responses={**RESP_422},
)
def listar_usuarios(
    service: ServiceDep,
    pagina: Annotated[
        int, Query(ge=1, description="Número de página, desde 1.")
    ] = 1,
    limite: Annotated[
        int, Query(ge=1, le=100, description="Usuarios por página, de 1 a 100.")
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
    responses={**RESP_404, **RESP_422},
)
def obtener_usuario(usuario_id: UsuarioId, service: ServiceDep):
    return UsuarioResponseDTO.model_validate(service.obtener(usuario_id))


@router.put(
    "/{usuario_id}",
    response_model=UsuarioResponseDTO,
    summary="Actualizar un usuario",
    description=(
        "Reemplaza el nombre, correo y estado del usuario. "
        "Conserva su ID y fecha de registro."
    ),
    responses={**RESP_404, **RESP_409, **RESP_422},
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
    responses={**RESP_404, **RESP_422},
)
def eliminar_usuario(usuario_id: UsuarioId, service: ServiceDep):
    service.eliminar(usuario_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)