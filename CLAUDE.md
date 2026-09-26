# Helpdesk API

## Como trabalhamos (importante)
- Projeto de portfólio **e de aprendizado**. O dono escreve o código de domínio (models, schemas, services, rotas).
- Claude explica o conceito, passa a tarefa com critérios de pronto e revisa. Dicas antes de soluções.
- Claude só escreve código quando pedido. Quando o dono delega uma parte (ex.: configuração, o DBML), Claude faz por completo e explica as decisões não óbvias.
- Conversa em português (Brasil). Nomes de código, tabelas e valores em inglês.

## Decisões já tomadas
- Uma empresa só (sem multi-tenant, por enquanto).
- PK UUIDv7 (`uuidv7()` do Postgres 18); datas sempre `timestamptz`.
- Listas fixas amarradas ao código (`role`, `status`, `event_type`) = varchar + CHECK, mapeadas para `StrEnum`. Prioridades e categorias = tabelas.
- Nada é apagado: `is_active`; FKs no padrão (NO ACTION).
- Modelo completo em `docs/database.dbml`. Naming convention de constraints em `app/models/base.py`: todo CheckConstraint precisa de `name=`.

## Comandos
- `docker compose up -d` · `uv sync` · `uv run pytest` · `uv run ruff check .`
- `uv run alembic revision --autogenerate -m "..."` · `uv run alembic upgrade head`
- `uv run fastapi dev app/main.py`
