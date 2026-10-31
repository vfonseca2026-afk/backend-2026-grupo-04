from pydantic import BaseModel, Field


class ErrorDetalleDTO(BaseModel):
    code: str = Field(
        description="Código que identifica el tipo de error.",
        examples=["RESOURCE_NOT_FOUND"],
    )
    message: str = Field(
        description="Explicación del error.",
        examples=["No existe un género con el ID solicitado."],
    )
    details: list[dict] = Field(
        default_factory=list,
        description="Detalles adicionales, como los campos inválidos.",
    )


class ErrorResponseDTO(BaseModel):
    """Formato uniforme de los errores controlados de la API."""

    error: ErrorDetalleDTO


def _respuesta(
    descripcion: str,
    codigo: str,
    mensaje: str,
    detalles: list[dict] | None = None,
) -> dict:
    """Documenta el modelo y un ejemplo completo de respuesta."""
    return {
        "model": ErrorResponseDTO,
        "description": descripcion,
        "content": {
            "application/json": {
                "example": {
                    "error": {
                        "code": codigo,
                        "message": mensaje,
                        "details": detalles if detalles is not None else [],
                    }
                }
            }
        },
    }


# Estas constantes documentan respuestas; no modifican los manejadores HTTP.

RESP_400 = {
    400: _respuesta(
        descripcion="La solicitud viola una regla de negocio.",
        codigo="BUSINESS_RULE_VIOLATION",
        mensaje="Un usuario inactivo no puede publicar reseñas.",
    )
}

RESP_404 = {
    404: _respuesta(
        descripcion="El recurso solicitado no existe.",
        codigo="RESOURCE_NOT_FOUND",
        mensaje="No existe un género con el ID solicitado.",
    )
}

RESP_409 = {
    409: _respuesta(
        descripcion="La operación entra en conflicto con el estado actual.",
        codigo="RESOURCE_CONFLICT",
        mensaje="Ya existe un género con ese nombre.",
    )
}

RESP_422 = {
    422: _respuesta(
        descripcion="Los datos no cumplen el esquema o las validaciones.",
        codigo="VALIDATION_ERROR",
        mensaje="Los datos enviados no cumplen las validaciones.",
        detalles=[
            {
                "campo": "body.nombre",
                "mensaje": "String should have at least 2 characters",
                "tipo": "string_too_short",
            }
        ],
    )
}