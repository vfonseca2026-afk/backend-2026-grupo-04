from pydantic import BaseModel, ConfigDict, Field

from domain.pelicula import Clasificacion


class PeliculaCreateDTO(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        json_schema_extra={
            "example": {
                "titulo": "Horizonte lejano",
                "sinopsis": "Una expedición explora un planeta desconocido.",
                "anio_estreno": 2020,
                "duracion_min": 110,
                "director": "Ana Ejemplo",
                "clasificacion": "TP",
                "genero_id": 1,
            }
        },
    )

    titulo: str = Field(
        min_length=1,
        max_length=150,
        description="Título de la película.",
    )
    sinopsis: str = Field(
        default="",
        max_length=2000,
        description="Sinopsis opcional al crear.",
    )
    anio_estreno: int = Field(
        ge=1888,
        description="Año de estreno. Puede ser posterior al actual.",
    )
    duracion_min: int = Field(
        gt=0,
        description="Duración en minutos.",
    )
    director: str = Field(
        min_length=1,
        max_length=100,
        description="Nombre del director o directora.",
    )
    clasificacion: Clasificacion = Field(
        description="Clasificación permitida: TP, +14 o +18.",
    )
    genero_id: int = Field(
        gt=0,
        description="ID de un género existente.",
    )


class PeliculaUpdateDTO(PeliculaCreateDTO):
    """PUT requiere todos los campos editables."""

    sinopsis: str = Field(
        max_length=2000,
        description="Sinopsis que reemplazará la actual. Puede estar vacía.",
    )


class PeliculaResponseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    titulo: str
    sinopsis: str
    anio_estreno: int
    duracion_min: int
    director: str
    clasificacion: Clasificacion
    genero_id: int
