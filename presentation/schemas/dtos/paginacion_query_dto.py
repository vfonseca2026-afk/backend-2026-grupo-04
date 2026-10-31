from typing import Literal

from pydantic import BaseModel, Field


class PaginacionQueryDTO(BaseModel):
    """Parámetros comunes de paginación y orden (guía 5.5).

    Los DTO de consulta de cada entidad heredan de esta clase y agregan sus
    propios filtros y las columnas permitidas para 'ordenar_por'.
    """

    pagina: int = Field(default=1, ge=1, description="Número de página (desde 1).")
    limite: int = Field(
        default=10, ge=1, le=100, description="Elementos por página (1 a 100)."
    )
    direccion: Literal["asc", "desc"] = Field(
        default="asc", description="Dirección del orden: asc o desc."
    )
