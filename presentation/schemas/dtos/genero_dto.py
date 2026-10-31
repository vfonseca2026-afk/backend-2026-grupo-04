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

    nombre: str = Field(
        min_length=2,
        max_length=50,
        description="Nombre único del género, sin distinguir mayúsculas.",
    )
    descripcion: str = Field(
        default="",
        max_length=255,
        description="Descripción del género. Es opcional al crear.",
    )


class GeneroUpdateDTO(GeneroCreateDTO):
    """PUT requiere nombre, descripción y estado activo."""

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

    descripcion: str = Field(
        max_length=255,
        description="Descripción que reemplazará la actual. Puede estar vacía.",
    )
    activo: bool = Field(
        description="Indica si el género está activo.",
    )


class GeneroResponseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(description="Identificador único del género.")
    nombre: str = Field(description="Nombre del género.")
    descripcion: str = Field(description="Descripción del género.")
    activo: bool = Field(description="Estado del género.")
    fecha_creacion: datetime | None = Field(
        description="Fecha y hora de creación del género.",
    )