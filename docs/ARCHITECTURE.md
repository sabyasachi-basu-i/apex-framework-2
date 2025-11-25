# APEX Framework Architecture

APEX (Agentic Platform for Enterprise Execution) is composed of six conceptual layers which together provide the infrastructure required to build, run and govern enterprise‑grade agentic systems.  Each layer is implemented by one or more microservices in this repository and exposes a set of APIs for other layers and for external consumers.

## 1. Layer overview

| Layer            | Purpose                                               |
|------------------|-------------------------------------------------------|
| **Intelligence** | Reasoning, memory, retrieval‑augmented generation     |
| **Integration**  | Data and application connectivity                     |
| **Orchestration**| Multi‑step workflow and agent coordination           |
| **Action**       | Triggering external effects (APIs, RPA, webhooks)     |
| **Governance**   | Security, RBAC, audit, observability, compliance      |
| **Experience**   | Human interaction via web, chat, voice or API         |

These layers are loosely coupled: they communicate via REST APIs and do not share state.  Deployments can be scaled independently and extended or replaced as needed.

## 2. High‑level diagram

```
┌───────────────────────────────────────────────────┐
│               Experience Layer                   │
│  (Web console, chat, voice, embedded widgets)    │
└───────────────────────────────────────────────────┘
                ▲                     ▲
                │                     │
┌────────────────┴─────────────────────┴─────────────┐
│                 Governance Layer                    │
│  Auth · RBAC · Policies · Audit · Observability     │
└────────────────┬──────────────────────┬────────────┘
                 │                      │
┌────────────────┴──────────────────────┴────────────┐
│               Orchestration Layer                  │
│   Flow DSL · Multi‑agent routing · Planning       │
└────────────────┬───────────────┬───────────────────┘
                 │               │
┌────────────────┴───────────────┴──────┐
│     Intelligence Layer     │ Action Layer │
│ LLM & RAG · Memory systems │ API & RPA    │
└─────────────────────────────┴─────────────┘
                 │
┌────────────────┴──────────────────────────────┐
│               Integration Layer              │
│ Connectors: databases, SaaS, files, etc.    │
└──────────────────────────────────────────────┘
```

## 3. Service map

APEX implements the layers as four microservices: `intelligence-service`, `integration-service`, `orchestration-service` and `governance-service`.  The Action Layer is handled by the integration and orchestration services depending on the type of action.

### 3.1 intelligence-service

Exposes reasoning and memory capabilities via REST endpoints.  It includes a simple in‑memory vector store for retrieval and a pluggable LLM client (stubbed by default).  Future iterations can integrate with real vector databases and hosted LLMs.

* `/memory/ingest` – ingest raw text into a named memory space.
* `/memory/query` – perform a semantic search across a memory space.
* `/llm/completions` – (observable placeholder) generate completions using configured LLM.

### 3.2 integration-service

Defines connectors to external systems.  Connectors implement a common interface with `test_connection` and `execute` methods.  The provided connectors include a working SQL connector and stubs for Salesforce, Icertis and blob storage.

* `/connectors/execute` – execute an operation on a given connector type (for example, run a SQL query).

### 3.3 orchestration-service

The orchestration engine loads YAML flows from disk and executes each step in order.  Step types include `connector_call` (calling a connector), `llm_call` (query memory or call an LLM) and `api_call` (execute an action).  Execution state is returned as a context dictionary.  Future improvements may include conditional logic, loops and multi‑agent routing.

* `/flows/run` – run a flow defined in a YAML file path.

### 3.4 governance-service

Provides a simple authentication and authorisation layer with JSON Web Tokens (JWT), role‑based access control (RBAC) and audit logging.  The current implementation stores users and logs in memory; you can extend it to persist to a database.

* `/auth/login` – create a user token (placeholder).  In a real deployment, integrate with your SSO provider.
* `/rbac/users` – list users (placeholder).
* `/audit/log` – post audit events.

## 4. Extensibility

This repository is designed to be extended.  You can:

* Replace the in‑memory memory store with a real vector database or knowledge graph.
* Implement additional connectors by subclassing `BaseConnector`.
* Add new step types to the orchestration engine (for example, branching, loops or multi‑agent cooperation).
* Persist governance state and audit logs to a database.
* Enhance the console with charts, management screens and visual flow builders.

The modularity of APEX means you can adopt only the layers you need and integrate them with your existing systems.