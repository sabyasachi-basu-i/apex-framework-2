# APEX Framework

APEX (Agentic Platform for Enterprise Execution) is an opinionated platform for building production‑grade agentic systems.

This project assembles a complete end‑to‑end system consisting of several microservices, a web console, SDKs, example flows and Kubernetes manifests.  It is intended as a starting point for real‑world enterprise agentic projects and can be extended and customised to suit your needs.

## Getting started

### Prerequisites

* [Docker](https://docs.docker.com/get-docker/) and Docker Compose installed
* [Node.js](https://nodejs.org/) (v18 or newer) if you want to run the console outside of Docker
* Python 3.10 or newer if you want to develop the back end outside of Docker

### Running locally with Docker Compose

The simplest way to run the entire stack is via Docker Compose.  Run the following from the root of the repository:

```bash
# build and start all services
docker compose up --build

# optional: follow logs for a specific service
docker compose logs -f intelligence
```

The following containers will be launched:

| Service              | Port | Description                                    |
|----------------------|------|------------------------------------------------|
| intelligence         | 8001 | Memory store, LLM abstraction and RAG API      |
| integration          | 8002 | Data and system connectors                     |
| orchestration        | 8003 | Flow and agent orchestration engine            |
| governance           | 8004 | RBAC, audit and governance APIs                |
| console              | 3000 | Web console (Next.js)                          |

> **Note**: the microservices expect a running PostgreSQL instance if you enable persistent storage.  For convenience, the default configuration uses in‑memory stores.

### Running services individually

Each microservice can also be started individually for development.  For example, to run the intelligence service:

```bash
cd services/intelligence-service
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

The integration, orchestration and governance services can be started in the same way.

### Starting the console

The console is a [Next.js](https://nextjs.org/) application.  To develop locally:

```bash
cd console
npm install
npm run dev
```

This will start the console on port `3000` and proxy API calls to the local services using the environment variables defined in `.env.example`.

## Repository structure

```
apex-framework/
├─ README.md               # this file
├─ pyproject.toml          # python project metadata and dependencies
├─ package.json            # Node.js console dependencies
├─ docker-compose.yml      # compose file to run the entire system
├─ .env.example            # sample environment variables
├─ docs/                   # architecture and layer documentation
├─ services/               # the microservice implementations
│  ├─ intelligence-service/
│  ├─ integration-service/
│  ├─ orchestration-service/
│  └─ governance-service/
├─ console/                # Next.js console application
├─ sdk/                    # Python and TypeScript client SDKs
├─ examples/               # sample flows and notebooks
└─ infra/                  # Kubernetes manifests and Helm charts
```

See the `docs/ARCHITECTURE.md` and `docs/OVERVIEW.md` files for more detail on the design and the capabilities of each layer.
