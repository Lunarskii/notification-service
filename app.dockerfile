FROM python:3.12-alpine

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry; \
    poetry config virtualenvs.create false; \
    poetry install --only=main --no-interaction --no-ansi;

COPY src ./src

WORKDIR /app/src

ENTRYPOINT ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
