from dataclasses import dataclass
from datetime import datetime

from domain.exceptions import ReglaNegocioError


@dataclass
class Genero:
    """Categoría de películas (Acción, Drama...). 1 género -> N películas."""

    nombre: str
    descripcion: str = ""
    id: int | None = None
    activo: bool = True
    fecha_creacion: datetime | None = None

    def __post_init__(self) -> None:
        self.nombre = self.nombre.strip()
        self.descripcion = (self.descripcion or "").strip()

        if not self.nombre:
            raise ReglaNegocioError("El nombre del género es obligatorio.")
