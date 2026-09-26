# Helpdesk API

API REST de help desk para empresas gerenciarem chamados de suporte: tickets com máquina de estados, SLA monitorado por worker, notificações em tempo real e controle de acesso por papel (RBAC).

> 🚧 Em construção. Veja o [roadmap](#roadmap).

## Stack

- **Python 3.14** + **FastAPI**
- **PostgreSQL 18** com **SQLAlchemy 2** (async, asyncpg) e **Alembic** para migrations
- **Redis** (fila de jobs, pub/sub, rate limit)
- **pytest**, **ruff**, **Docker Compose**

## Rodando localmente

Pré-requisitos: [uv](https://docs.astral.sh/uv/) e [Docker](https://www.docker.com/).

```bash
cp .env.example .env              # variáveis de ambiente locais
docker compose up -d              # sobe Postgres e Redis
uv sync                           # cria o .venv e instala as dependências
uv run alembic upgrade head       # aplica as migrations
uv run fastapi dev app/main.py    # API em http://localhost:8000
```

Documentação interativa: http://localhost:8000/docs

## Testes e qualidade

```bash
uv run pytest
uv run ruff check .
uv run ruff format .
```

## Modelo de dados

O modelo está em [`docs/database.dbml`](docs/database.dbml). Cole o conteúdo em [dbdiagram.io](https://dbdiagram.io) para ver o diagrama.

## Roadmap

- [x] **Fase 0:** estrutura, Docker Compose, configuração
- [ ] **Fase 1:** models e migrations
- [ ] **Fase 2:** autenticação (JWT + refresh token) e RBAC
- [ ] **Fase 3:** tickets, máquina de estados, comentários e histórico
- [ ] **Fase 4:** SLA com worker em background
- [ ] **Fase 5:** notificações (outbox) e WebSocket
- [ ] **Fase 6:** anexos (MinIO/S3), busca full-text e métricas
