from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ResenaUpdateDTO(BaseModel):
    """Campos editables de una reseña. Todos son obligatorios en PUT."""

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        json_schema_extra={
            "example": {
                "puntuacion": 8,
                "titulo": "Una historia recomendable",
                "comentario": "Buenos personajes y una historia entretenida.",
            }
        },
    )

    puntuacion: int = Field(
        ge=1,
        le=10,
        description="Puntuación entre 1 y 10, inclusive.",
    )
    titulo: str = Field(
        min_length=1,
        max_length=100,
        description="Título de la reseña.",
    )
    comentario: str = Field(
        min_length=10,
        max_length=2000,
        description="Comentario de entre 10 y 2000 caracteres.",
    )


class ResenaCreateDTO(ResenaUpdateDTO):
    """Datos necesarios para publicar una reseña."""

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        json_schema_extra={
            "example": {
                "usuario_id": 1,
                "pelicula_id": 1,
                "puntuacion": 8,
                "titulo": "Una historia recomendable",
                "comentario": "Buenos personajes y una historia entretenida.",
            }
        },
    )

    usuario_id: int = Field(
        gt=0,
        description="ID de un usuario existente.",
    )
    pelicula_id: int = Field(
        gt=0,
        description="ID de una película existente.",
    )


class ResenaResponseDTO(BaseModel):
    """Datos devueltos por la API para una reseña persistida."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    usuario_id: int
    pelicula_id: int
    puntuacion: int
    titulo: str
    comentario: str
    fecha: datetime