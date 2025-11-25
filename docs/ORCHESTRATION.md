# Orchestration Layer

The Orchestration Layer coordinates the execution of multi‑step flows and agent interactions.  It is implemented by the `orchestration-service` microservice.

## Flow definition

Flows are defined in YAML files located under `examples/`.  Each flow contains a list of steps.  Supported step types:

* **connector_call** – call a connector operation via the integration layer.  The `connector` field names the type and the `payload` contains the operation parameters.
* **llm_call** – call the intelligence layer.  You can specify `space_id`, `prompt` and `top_k` to perform a memory query or `endpoint` to call the LLM (currently stubbed).
* **api_call** – call an external HTTP API directly.  This step type can be added by extending the engine.

### Example flow

```yaml
id: prod_support_triage
name: Production Support Triage
description: Fetch logs and analyse them.
steps:
  - id: fetch_logs
    type: connector_call
    connector: sql
    operation: query
    payload:
      query: "SELECT * FROM logs LIMIT 10"
  - id: analyse
    type: llm_call
    space_id: prod
    prompt: "Summarise the log lines"
    top_k: 3
```

## Execution

Flows are executed by posting to the `/flows/run` endpoint with the path to the YAML file:

```bash
curl -X POST http://localhost:8003/flows/run \
  -H "Content-Type: application/json" \
  -d '{"flow_path":"examples/nrg-production-support/flows/prod_support.yaml","inputs":{}}'
```

The engine reads the YAML file, executes each step in order and returns a context dictionary containing each step's result.  The current implementation executes steps sequentially; future versions may add concurrency, conditional execution and loops.

## Extensibility

You can add new step types by extending the `FlowEngine` class in `apex_orchestration/engine.py`.  For example, to support conditional branches, implement a new step handler method and dispatch to it based on the step definition.