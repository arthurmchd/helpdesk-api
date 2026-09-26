from datetime import datetime

from sqlalchemy import DateTime, MetaData
from sqlalchemy.orm import DeclarativeBase

# Nomes previsíveis para constraints. Sem isso o Postgres inventa nomes
# e o Alembic não consegue alterar ou remover a constraint depois.
# Atenção: "ck" usa %(constraint_name)s, então todo CheckConstraint
# PRECISA de name=... (ex.: name="role_valid" -> ck_users_role_valid).
NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_N_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_N_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=NAMING_CONVENTION)

    # Convenção do projeto: todo Mapped[datetime] vira timestamptz.
    type_annotation_map = {
        datetime: DateTime(timezone=True),
    }
