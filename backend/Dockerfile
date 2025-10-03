FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip
RUN pip install \
    fastapi==0.115.0 \
    uvicorn[standard]==0.30.6 \
    pydantic==2.9.2 \
    pydantic-settings==2.5.2 \
    sqlalchemy==2.0.36 \
    psycopg[binary]==3.2.3 \
    asyncpg==0.29.0 \
    prometheus-fastapi-instrumentator==6.1.0 \
    alembic==1.13.2 \
    pytest==8.3.3 \
    requests==2.32.3

COPY . /app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
