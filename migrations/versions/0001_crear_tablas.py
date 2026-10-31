"""crear tablas generos, usuarios, peliculas y resenas

Migración inicial limpia: crea el esquema completo desde cero.

Revision ID: 0001
Revises:
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "generos",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nombre", sa.String(50), nullable=False),
        sa.Column("descripcion", sa.String(255), nullable=False),
        sa.Column("activo", sa.Boolean(), nullable=False),
        sa.Column(
            "fecha_creacion",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )
    op.create_index("ix_generos_nombre", "generos", ["nombre"], unique=True)

    op.create_table(
        "usuarios",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nombre_usuario", sa.String(50), nullable=False),
        sa.Column("email", sa.String(254), nullable=False),
        sa.Column("activo", sa.Boolean(), nullable=False),
        sa.Column(
            "fecha_registro",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )
    op.create_index(
        "ix_usuarios_nombre_usuario", "usuarios", ["nombre_usuario"], unique=True
    )
    op.create_index("ix_usuarios_email", "usuarios", ["email"], unique=True)

    op.create_table(
        "peliculas",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("titulo", sa.String(150), nullable=False),
        sa.Column("sinopsis", sa.Text(), nullable=False),
        sa.Column("anio_estreno", sa.Integer(), nullable=False),
        sa.Column("duracion_min", sa.Integer(), nullable=False),
        sa.Column("director", sa.String(100), nullable=False),
        sa.Column("clasificacion", sa.String(3), nullable=False),
        sa.Column(
            "genero_id",
            sa.Integer(),
            sa.ForeignKey("generos.id", ondelete="RESTRICT"),
            nullable=False,
        ),
        sa.CheckConstraint("duracion_min > 0", name="ck_peliculas_duracion"),
        sa.CheckConstraint(
            "clasificacion IN ('TP', '+14', '+18')",
            name="ck_peliculas_clasificacion",
        ),
    )
    op.create_index("ix_peliculas_titulo", "peliculas", ["titulo"])
    op.create_index("ix_peliculas_anio_estreno", "peliculas", ["anio_estreno"])
    op.create_index("ix_peliculas_genero_id", "peliculas", ["genero_id"])

    op.create_table(
        "resenas",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "usuario_id",
            sa.Integer(),
            sa.ForeignKey("usuarios.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "pelicula_id",
            sa.Integer(),
            sa.ForeignKey("peliculas.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("puntuacion", sa.Integer(), nullable=False),
        sa.Column("titulo", sa.String(100), nullable=False),
        sa.Column("comentario", sa.Text(), nullable=False),
        sa.Column(
            "fecha",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.UniqueConstraint(
            "usuario_id", "pelicula_id", name="uq_resenas_usuario_pelicula"
        ),
        sa.CheckConstraint(
            "puntuacion BETWEEN 1 AND 10", name="ck_resenas_puntuacion"
        ),
    )
    op.create_index("ix_resenas_usuario_id", "resenas", ["usuario_id"])
    op.create_index("ix_resenas_pelicula_id", "resenas", ["pelicula_id"])


def downgrade() -> None:
    op.drop_table("resenas")
    op.drop_table("peliculas")
    op.drop_table("usuarios")
    op.drop_table("generos")
