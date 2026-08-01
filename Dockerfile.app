FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:0.11.8 /uv /uvx /bin/

WORKDIR /app

COPY .python-version ./
COPY pyproject.toml uv.lock ./
COPY README.md ./
COPY alembic.ini ./
COPY alembic/ ./alembic/
COPY data/user_data/ ./data/user_data/
COPY models/trained/ ./models/trained/
COPY tmp/ ./tmp/
COPY scripts/ ./scripts/
COPY src/ ./src/

ENV UV_NO_DEV=1
RUN uv sync --locked --no-dev

# EXPOSE 8000

# CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]