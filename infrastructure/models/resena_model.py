from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database import Base

if TYPE_CHECKING:
    from infrastructure.models.pelicula_model import PeliculaModel
    from infrastructure.models.usuario_model import UsuarioModel


class ResenaModel(Base):
    __tablename__ = "resenas"
    __table_args__ = (
        # Un usuario solo puede reseñar una película una vez.
        UniqueConstraint(
            "usuario_id", "pelicula_id", name="uq_resenas_usuario_pelicula"
        ),
        CheckConstraint(
            "puntuacion BETWEEN 1 AND 10", name="ck_resenas_puntuacion"
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id", ondelete="CASCADE"), index=True
    )
    pelicula_id: Mapped[int] = mapped_column(
        ForeignKey("peliculas.id", ondelete="CASCADE"), index=True
    )
    puntuacion: Mapped[int] = mapped_column(Integer)
    titulo: Mapped[str] = mapped_column(String(100))
    comentario: Mapped[str] = mapped_column(Text)
    fecha: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    usuario: Mapped["UsuarioModel"] = relationship(back_populates="resenas")
    pelicula: Mapped["PeliculaModel"] = relationship(back_populates="resenas")
