from pydantic import BaseModel, Field


class ErrorDetalleDTO(BaseModel):
    code: str = Field(examples=["RESOURCE_NOT_FOUND"])
    message: str = Field(examples=["No existe un género con el ID solicitado."])
    details: list[dict] = Field(default_factory=list)


class ErrorResponseDTO(BaseModel):
    """Formato único de error para TODA la API (guía 5.4)."""

    error: ErrorDetalleDTO


def _respuesta(descripcion: str) -> dict:
    return {"model": ErrorResponseDTO, "description": descripcion}


# Se reutilizan en los routers para documentar los errores en OpenAPI:
#   @router.get(..., responses={**RESP_404, **RESP_422})
RESP_400 = {400: _respuesta("La solicitud viola una regla de negocio.")}
RESP_404 = {404: _respuesta("El recurso solicitado no existe.")}
RESP_409 = {409: _respuesta("Conflicto con el estado actual (duplicado, etc.).")}
RESP_422 = {422: _respuesta("Los datos no cumplen el esquema o las validaciones.")}
