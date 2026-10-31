from dataclasses import dataclass
from datetime import datetime

from domain.exceptions import ReglaNegocioError


@dataclass
class Resena:
    """Opinión de un usuario sobre una película (puntuación de 1 a 10)."""

    usuario_id: int
    pelicula_id: int
    puntuacion: int
    titulo: str
    comentario: str
    id: int | None = None
    fecha: datetime | None = None

    def __post_init__(self) -> None:
        self.titulo = self.titulo.strip()
        self.comentario = self.comentario.strip()

        if not 1 <= self.puntuacion <= 10:
            raise ReglaNegocioError("La puntuación debe estar entre 1 y 10.")
