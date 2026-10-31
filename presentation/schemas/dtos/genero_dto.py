from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class GeneroCreateDTO(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        json_schema_extra={
            "example": {
                "nombre": "Ciencia ficción",
                "descripcion": "Películas sobre futuros posibles y tecnología.",
            }
        },
    )

    # Validación de LONGITUD: entre 2 y 50 caracteres.
    nombre: str = Field(min_length=2, max_length=50)
    descripcion: str = Field(default="", max_length=255)


class GeneroUpdateDTO(GeneroCreateDTO):
    """Para actualizar (PUT) se envían todos los campos."""

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        json_schema_extra={
            "example": {
                "nombre": "Ciencia ficción",
                "descripcion": "Futuros posibles, tecnología y espacio.",
                "activo": True,
            }
        },
    )

    activo: bool = True


class GeneroResponseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str
    descripcion: str
    activo: bool
    fecha_creacion: datetime | None
