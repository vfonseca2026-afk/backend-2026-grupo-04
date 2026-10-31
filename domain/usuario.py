from dataclasses import dataclass
from datetime import datetime

from domain.exceptions import ReglaNegocioError


@dataclass
class Usuario:
    """Persona que publica reseñas. 1 usuario -> N reseñas."""

    nombre_usuario: str
    email: str
    id: int | None = None
    activo: bool = True
    fecha_registro: datetime | None = None

    def __post_init__(self) -> None:
        self.nombre_usuario = self.nombre_usuario.strip()
        self.email = self.email.strip().lower()

        if not self.nombre_usuario:
            raise ReglaNegocioError("El nombre de usuario es obligatorio.")

        if not self.email:
            raise ReglaNegocioError("El email es obligatorio.")

    def puede_resenar(self) -> bool:
        """Regla de negocio: un usuario inactivo no puede publicar reseñas."""
        return self.activo
