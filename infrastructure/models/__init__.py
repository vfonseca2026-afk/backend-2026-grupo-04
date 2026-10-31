# Importar todos los modelos aquí garantiza que SQLAlchemy conozca las cuatro
# tablas (y sus relaciones) apenas se use cualquiera de ellos.
from infrastructure.models import (  # noqa: F401
    genero_model,
    pelicula_model,
    resena_model,
    usuario_model,
)
