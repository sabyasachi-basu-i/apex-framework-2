# APEX Codex code generation brief

This file describes how to generate code inside the `apex-framework` repository.  When integrating with code generation tools such as OpenAI Codex or GitHub Copilot, include the contents of this file in your system prompt to provide context about the repository structure and coding conventions.

## Repository overview

The `apex-framework` repository is structured as follows:

* `services/` – four independent FastAPI microservices implementing the Intelligence, Integration, Orchestration and Governance layers.
* `console/` – a Next.js web application that provides a user interface for viewing memory, running flows, testing connectors and managing governance.
* `sdk/` – client SDKs for Python and TypeScript.
* `examples/` – sample flows and notebooks demonstrating how to use APEX.
* `infra/` – Kubernetes manifests for deployment.

## Coding conventions

* **Python**: use type hints, docstrings and asynchronous functions.  Organise code into packages under each service.  Use Pydantic models for request/response bodies.  Make new connectors by subclassing `apex_integration.connectors.base.BaseConnector`.
* **FastAPI**: define routers in `routes/` and mount them in `main.py`.  Use path prefixes and tags.
* **JavaScript/TypeScript**: prefer TypeScript for the console; components live in `console/src/components`, pages in `console/src/pages`.  Use React functional components with hooks and Tailwind CSS for styling.
* **SDKs**: implement a class per service in the Python and TypeScript SDKs; each should expose high‑level methods wrapping HTTP calls.  Use environment variables for base URLs.

## Generation tasks

When asked to implement functionality, generate code in all relevant layers:

1. **Back‑end** – add or modify routes, models and services in the appropriate microservice.
2. **SDK** – add corresponding methods to the Python and TypeScript SDKs.
3. **Console** – expose the feature in the web UI with appropriate pages and components.
4. **Tests** – create unit tests under a `tests/` folder (not included by default).
5. **Documentation** – update the docs if the architecture or public APIs change.

Never modify files outside the repository or remove existing documentation.  Always keep the directory structure intact.