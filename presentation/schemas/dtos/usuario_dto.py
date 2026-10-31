from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UsuarioCreateDTO(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        json_schema_extra={
            "example": {
                "nombre_usuario": "cinefilo",
                "email": "cinefilo@example.com",
            }
        },
    )

    nombre_usuario: str = Field(min_length=3, max_length=50)
    email: EmailStr = Field(max_length=254)


class UsuarioUpdateDTO(UsuarioCreateDTO):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        json_schema_extra={
            "example": {
                "nombre_usuario": "cinefilo",
                "email": "cinefilo@example.com",
                "activo": True,
            }
        },
    )

    activo: bool


class UsuarioResponseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre_usuario: str
    email: EmailStr
    activo: bool
    fecha_registro: datetime | None