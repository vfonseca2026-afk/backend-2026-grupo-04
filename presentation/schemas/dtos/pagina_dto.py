import math
from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class PaginaDTO(BaseModel, Generic[T]):
    """Respuesta paginada exigida por la guía (5.5).

    Uso: response_model=PaginaDTO[PeliculaResponseDTO]
    """

    items: list[T]
    total: int
    pagina: int
    limite: int
    total_paginas: int

    @classmethod
    def crear(cls, items: list, total: int, pagina: int, limite: int):
        # total y total_paginas se calculan sobre los registros FILTRADOS.
        total_paginas = math.ceil(total / limite) if total > 0 else 0

        return cls(
            items=items,
            total=total,
            pagina=pagina,
            limite=limite,
            total_paginas=total_paginas,
        )
