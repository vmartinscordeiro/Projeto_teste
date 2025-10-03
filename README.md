# Brain Agriculture — Teste Técnico (Fullstack)

Este repositório entrega **backend (FastAPI + Postgres + Alembic + Docker)** e **frontend (React + TypeScript + Vite + Redux Toolkit + Tests)**, atendendo aos requisitos do desafio.

## ✅ O que foi implementado

- **Regras de negócio**
  - CRUD de **Produtores** e **Fazendas**.
  - **Validação de CPF/CNPJ** no backend.
  - **Consistência de áreas**: agricultável + vegetação ≤ total.
  - **Safra & Cultura por fazenda** (relações sazonais: Soja/Milho etc.).
  - **Dashboard** com:
    - Total de fazendas.
    - Total de hectares (área total).
    - **Gráficos de pizza**: por **UF**, por **Cultura** e por **Uso do Solo**.

- **Backend**
  - **FastAPI** (Python 3.11) + **SQLAlchemy 2** + **Alembic**.
  - **Postgres** via Docker Compose.
  - **OpenAPI** em `/docs` (Swagger) e `/redoc`.
  - **Observabilidade**: `/metrics` via `prometheus_fastapi_instrumentator` e endpoint `/health`.
  - **Testes** (pytest) — API básica end-to-end.

- **Frontend**
  - **React + TypeScript + Vite** (Node 22+).
  - **Redux Toolkit** (slice de `producers` com testes).
  - **Recharts** para os gráficos.
  - **Testes UI** com **Vitest + Testing Library** (inclui ajustes de JSDOM para gráficos).

## 🧱 Arquitetura & Estrutura

brain-ag-test/
├─ backend/
│ ├─ app/
│ │ ├─ api/
│ │ │ └─ routers/
│ │ │ ├─ producers.py
│ │ │ ├─ farms.py
│ │ │ ├─ farm_crops.py
│ │ │ └─ dashboard.py
│ │ ├─ core/config.py
│ │ ├─ crud/
│ │ │ ├─ producer.py
│ │ │ ├─ farm.py
│ │ │ └─ farm_crop.py
│ │ ├─ db/
│ │ │ ├─ base.py
│ │ │ ├─ session.py
│ │ │ └─ deps.py
│ │ ├─ models/
│ │ │ ├─ producer.py
│ │ │ ├─ farm.py
│ │ │ └─ agronomy.py # Season, Crop, FarmCrop
│ │ ├─ schemas/
│ │ │ ├─ producer.py
│ │ │ ├─ farm.py
│ │ │ └─ farm_crop.py
│ │ ├─ utils/validators.py # cpf/cnpj e áreas
│ │ └─ main.py
│ ├─ alembic/
│ │ └─ versions/
│ │ ├─ 0001_init_producers_farms.py
│ │ └─ 0002_seasons_crops.py
│ ├─ tests/
│ │ └─ test_api.py
│ ├─ Dockerfile
│ └─ alembic.ini
├─ frontend/
│ ├─ src/
│ │ ├─ pages/
│ │ │ ├─ Dashboard.tsx
│ │ │ └─ Producers.tsx
│ │ ├─ features/producers/
│ │ │ ├─ slice.ts
│ │ │ └─ slice.test.ts
│ │ ├─ services/
│ │ │ ├─ api.ts
│ │ │ └─ dashboard.ts
│ │ ├─ tests/
│ │ │ ├─ Dashboard.test.tsx
│ │ │ └─ Producers.test.tsx
│ │ └─ setupTests.ts
│ ├─ vite.config.ts
│ ├─ package.json
│ └─ tsconfig.json
├─ docker-compose.yml
├─ openapi.json
└─ README.md


## 🚀 Como rodar (local)

### 1) Pré-requisitos

- **Docker Desktop** (com Docker Compose).
- **Node.js LTS 22+** (usamos 22.20.0).
- **PowerShell** (Windows) ou seu terminal favorito.

### 2) Backend (API + DB)

Na raiz do projeto:

```powershell
# subir containers (db + api)
docker compose up -d --build

# aplicar migrações do Alembic (se ainda não aplicadas)
docker compose exec api bash -lc "alembic -c alembic.ini upgrade head"

# verificar saúde
curl http://127.0.0.1:8000/health
# -> {"status":"ok","db":"up","env":"..."}
Documentação interativa:

Swagger: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

OpenAPI JSON: http://127.0.0.1:8000/openapi.json

Métricas Prometheus: http://127.0.0.1:8000/metrics

Endpoints principais

POST /producers — cria produtor {cpf_cnpj, name}

GET /producers — lista

GET /producers/{id}, PUT /producers/{id}, DELETE /producers/{id}

POST /farms — cria fazenda {producer_id, name, city, state, area_total, area_agricultavel, area_vegetacao}

GET /farms — lista (+ filtro producer_id)

GET/PUT/DELETE /farms/{id}

POST /farm-crops — vincula cultura/safra {farm_id, season, crop}

GET /farm-crops — lista (+ filtros farm_id, season, crop)

GET /dashboard/summary — { total_farms, total_hectares }

GET /dashboard/pie/state

GET /dashboard/pie/crop

GET /dashboard/pie/landuse

Exemplos rápidos (PowerShell):



# criar produtor
$body = @{ cpf_cnpj = '52998224725'; name = 'João da Silva' } | ConvertTo-Json -Compress
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/producers" -ContentType "application/json; charset=utf-8" -Body ([Text.Encoding]::UTF8.GetBytes($body))

# criar fazenda
$body = @{
  producer_id = 1; name='Fazenda Boa Terra'; city='Sorriso'; state='MT';
  area_total=1000; area_agricultavel=700; area_vegetacao=300
} | ConvertTo-Json -Compress
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/farms" -ContentType "application/json; charset=utf-8" -Body ([Text.Encoding]::UTF8.GetBytes($body))
3) Frontend (Vite)


cd frontend
npm install
npm run dev   # abre em http://127.0.0.1:5173
4) Testes


# backend
docker compose exec api bash -lc "pytest -q /app/tests"

# frontend (modo watch; pressione q para sair)
cd frontend
npm run test
Cobertura dos testes UI:

src/__tests__/Dashboard.test.tsx (mock dos serviços + checa títulos/cards).

src/__tests__/Producers.test.tsx (render e chamada simulada).

src/features/producers/slice.test.ts (reducers do Redux).

🔍 Observabilidade
/health: checagem rápida de DB e ambiente.

/metrics: métricas Prometheus do FastAPI (requests, latências, etc.).

🧩 Decisões & Notas
Validação: app/utils/validators.py contém CPF/CNPJ e check de áreas.

Modelagem: Season, Crop e FarmCrop permitem registrar culturas por safra.

Alembic: migrações 0001 (produtores, fazendas) e 0002 (safras, culturas, vínculos).

Redux: slice de producers com thunks (fetchProducers, createProducer).

Gráficos (Recharts): para testes no JSDOM, setupTests.ts inclui polyfills de ResizeObserver e getBBox.

Dica: para salvar o OpenAPI JSON na raiz:

curl.exe -s http://127.0.0.1:8000/openapi.json -o .\openapi.json
