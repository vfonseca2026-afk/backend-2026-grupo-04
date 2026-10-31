from dataclasses import dataclass
from datetime import date
from enum import Enum

from domain.exceptions import ReglaNegocioError


class Clasificacion(str, Enum):
    """Clasificación por edad (validación de 'valores permitidos')."""

    TODO_PUBLICO = "TP"
    MAYORES_14 = "+14"
    MAYORES_18 = "+18"


@dataclass
class Pelicula:
    """Película del catálogo. Pertenece a 1 género y tiene N reseñas."""

    titulo: str
    anio_estreno: int
    duracion_min: int
    director: str
    genero_id: int
    clasificacion: Clasificacion = Clasificacion.TODO_PUBLICO
    sinopsis: str = ""
    id: int | None = None

    def __post_init__(self) -> None:
        self.titulo = self.titulo.strip()
        self.director = self.director.strip()
        self.sinopsis = (self.sinopsis or "").strip()

        if not self.titulo:
            raise ReglaNegocioError("El título de la película es obligatorio.")

        if self.duracion_min <= 0:
            raise ReglaNegocioError("La duración debe ser mayor a 0 minutos.")

    def esta_estrenada(self, anio_actual: int | None = None) -> bool:
        """Regla de negocio: no se puede reseñar una película no estrenada."""
        anio = anio_actual if anio_actual is not None else date.today().year
        return self.anio_estreno <= anio
