from collections.abc import Iterator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from application.services.genero_service import GeneroService
from infrastructure.database import SessionLocal
from infrastructure.repositories.genero_repository import GeneroRepository

# --- Cada integrante agrega SUS imports y SU función en su bloque ---
from application.services.usuario_service import UsuarioService
from infrastructure.repositories.usuario_repository import UsuarioRepository
# TODO(Miguel): imports de PeliculaService y PeliculaRepository

# TODO(Danna): imports de ResenaService y ResenaRepository


def get_session() -> Iterator[Session]:
    """Abre una sesión por solicitud y la cierra al terminar."""
    session = SessionLocal()

    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


SessionDep = Annotated[Session, Depends(get_session)]


def get_genero_service(session: SessionDep) -> GeneroService:
    return GeneroService(GeneroRepository(session))


def get_usuario_service(session: SessionDep) -> UsuarioService:
    return UsuarioService(UsuarioRepository(session))

# TODO(Miguel): def get_pelicula_service(session: SessionDep) -> PeliculaService
#   (recibe PeliculaRepository y GeneroRepository)

# TODO(Danna): def get_resena_service(session: SessionDep) -> ResenaService
#   (recibe ResenaRepository, UsuarioRepository y PeliculaRepository)
