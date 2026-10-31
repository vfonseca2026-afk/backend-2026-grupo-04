"""Traduce excepciones a respuestas HTTP con el formato JSON uniforme (5.4):

    {"error": {"code": "...", "message": "...", "details": []}}
"""

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from starlette.exceptions import HTTPException as StarletteHTTPException

from domain.exceptions import (
    ConflictoError,
    DomainError,
    RecursoNoEncontradoError,
    ReglaNegocioError,
)

# Qué código HTTP corresponde a cada error del dominio.
_ESTADOS = {
    RecursoNoEncontradoError: status.HTTP_404_NOT_FOUND,
    ConflictoError: status.HTTP_409_CONFLICT,
    ReglaNegocioError: status.HTTP_400_BAD_REQUEST,
}

_CODIGOS_HTTP = {
    404: "RESOURCE_NOT_FOUND",
    405: "METHOD_NOT_ALLOWED",
}


def _error(estado: int, codigo: str, mensaje: str, detalles=None) -> JSONResponse:
    return JSONResponse(
        status_code=estado,
        content={
            "error": {
                "code": codigo,
                "message": mensaje,
                "details": detalles or [],
            }
        },
    )


def registrar_manejadores_de_errores(app: FastAPI) -> None:
    @app.exception_handler(DomainError)
    async def manejar_error_de_dominio(_: Request, error: DomainError):
        estado = _ESTADOS.get(type(error), status.HTTP_400_BAD_REQUEST)
        return _error(estado, error.codigo, error.mensaje, error.detalles)

    @app.exception_handler(RequestValidationError)
    async def manejar_validacion(_: Request, error: RequestValidationError):
        detalles = [
            {
                "campo": ".".join(str(parte) for parte in e["loc"]),
                "mensaje": e["msg"],
                "tipo": e["type"],
            }
            for e in error.errors()
        ]
        return _error(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            "VALIDATION_ERROR",
            "Los datos enviados no cumplen las validaciones.",
            detalles,
        )

    @app.exception_handler(IntegrityError)
    async def manejar_integridad(_: Request, __: IntegrityError):
        # Red de seguridad: la base rechazó la operación (duplicado, FK...).
        return _error(
            status.HTTP_409_CONFLICT,
            "RESOURCE_CONFLICT",
            "La operación viola una restricción de integridad de la base de datos.",
        )

    @app.exception_handler(StarletteHTTPException)
    async def manejar_http(_: Request, error: StarletteHTTPException):
        codigo = _CODIGOS_HTTP.get(error.status_code, "HTTP_ERROR")
        return _error(error.status_code, codigo, str(error.detail))
