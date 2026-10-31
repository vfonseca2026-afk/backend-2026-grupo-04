import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Lee el archivo .env (busca en esta carpeta y en las superiores).
load_dotenv()


def _variable_requerida(nombre: str) -> str:
    valor = os.environ.get(nombre)

    if not valor:
        raise RuntimeError(
            f"Falta la variable de entorno {nombre}. "
            "Copia .env.example como .env y completa tus datos."
        )

    return valor


url = URL.create(
    "postgresql+psycopg2",
    username=_variable_requerida("DB_USER"),
    password=_variable_requerida("DB_PASSWORD"),
    host=_variable_requerida("DB_HOST"),
    port=int(os.environ.get("DB_PORT", 5432)),
    database=_variable_requerida("DB_NAME"),
)

# echo=True imprime en consola el SQL que genera el ORM (útil para aprender).
engine = create_engine(url, echo=False)

SessionLocal = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    pass


# Las tablas se crean con Alembic: uv run alembic upgrade head
