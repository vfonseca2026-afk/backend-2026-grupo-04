from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database import Base

if TYPE_CHECKING:
    from infrastructure.models.genero_model import GeneroModel
    from infrastructure.models.resena_model import ResenaModel


class PeliculaModel(Base):
    __tablename__ = "peliculas"
    __table_args__ = (
        CheckConstraint("duracion_min > 0", name="ck_peliculas_duracion"),
        CheckConstraint(
            "clasificacion IN ('TP', '+14', '+18')",
            name="ck_peliculas_clasificacion",
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(150), index=True)
    sinopsis: Mapped[str] = mapped_column(Text, default="")
    anio_estreno: Mapped[int] = mapped_column(Integer, index=True)
    duracion_min: Mapped[int] = mapped_column(Integer)
    director: Mapped[str] = mapped_column(String(100))
    clasificacion: Mapped[str] = mapped_column(String(3), default="TP")

    # RESTRICT: la base impide borrar un género que todavía tiene películas.
    genero_id: Mapped[int] = mapped_column(
        ForeignKey("generos.id", ondelete="RESTRICT"), index=True
    )

    genero: Mapped["GeneroModel"] = relationship(back_populates="peliculas")
    resenas: Mapped[list["ResenaModel"]] = relationship(
        back_populates="pelicula", cascade="all, delete-orphan"
    )
