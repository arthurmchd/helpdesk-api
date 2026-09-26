"""Registro dos models.

Todo model novo precisa ser importado aqui: é assim que o Alembic
(migrations/env.py) enxerga as tabelas no autogenerate.
"""

from app.models.base import Base

__all__ = ["Base"]
