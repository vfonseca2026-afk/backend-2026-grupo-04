from typing import Literal

from pydantic import ConfigDict, Field

from domain.pelicula import Clasificacion
from presentation.schemas.dtos.paginacion_query_dto import (
    PaginacionQueryDTO,
)


class PeliculaQueryDTO(PaginacionQueryDTO):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

    genero_id: int | None = Field(
        default=None,
        gt=0,
        description="Filtra por ID de género.",
    )
    anio: int | None = Field(
        default=None,
        ge=1888,
        description="Filtra por año exacto de estreno.",
    )
    clasificacion: Clasificacion | None = Field(
        default=None,
        description="Filtra por clasificación.",
    )
    titulo: str | None = Field(
        default=None,
        min_length=1,
        max_length=150,
        description="Filtra por texto contenido en el título.",
    )
    ordenar_por: Literal[
        "titulo",
        "anio_estreno",
        "duracion_min",
    ] = Field(
        default="titulo",
        description="Campo utilizado para ordenar los resultados.",
    )