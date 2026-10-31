"""Errores del dominio.

Las capas de aplicación y dominio lanzan estas excepciones; NO conocen HTTP.
La capa de presentación (presentation/error_handlers.py) las traduce a códigos
HTTP y al formato JSON uniforme de errores exigido por la guía (5.4).
"""


class DomainError(Exception):
    """Base de todos los errores controlados por el sistema."""

    codigo = "DOMAIN_ERROR"

    def __init__(self, mensaje: str, detalles: list[dict] | None = None) -> None:
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.detalles = detalles or []


class RecursoNoEncontradoError(DomainError):
    """El recurso pedido no existe  -> HTTP 404."""

    codigo = "RESOURCE_NOT_FOUND"


class ConflictoError(DomainError):
    """La operación choca con el estado actual (duplicado, etc.) -> HTTP 409."""

    codigo = "RESOURCE_CONFLICT"


class ReglaNegocioError(DomainError):
    """La solicitud es válida pero viola una regla de negocio -> HTTP 400."""

    codigo = "BUSINESS_RULE_VIOLATION"
