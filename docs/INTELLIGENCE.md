# Intelligence Layer

The Intelligence Layer provides reasoning and knowledge retrieval capabilities to agents.  It is implemented by the `intelligence-service` microservice.

## Key capabilities

* **Memory spaces** – Named collections of documents and their embeddings.  You can ingest free‑form text into a space and query it later.
* **Semantic search** – The memory store performs approximate matching to retrieve the most relevant documents for a given query.  The default implementation is a simple in‑memory store; future versions may integrate with vector databases.
* **LLM abstraction** – A pluggable client for large language models.  The current implementation is stubbed but can be extended to call OpenAI, Azure OpenAI or any other provider.
* **RAG** – Retrieval‑augmented generation can be achieved by combining memory queries with LLM completions.  This pattern is left as an exercise for your flows and agents.

## API endpoints

The intelligence service exposes the following endpoints:

| Endpoint          | Method | Description                                      |
|-------------------|-------|--------------------------------------------------|
| `/memory/ingest`  | POST  | Ingests text into a memory space                 |
| `/memory/query`   | POST  | Queries a memory space and returns matches       |
| `/llm/completions`| POST  | (Stub) obtains completions from an LLM provider  |

### Example

```bash
curl -X POST http://localhost:8001/memory/ingest \
  -H "Content-Type: application/json" \
  -d '{"space_id":"docs","content":"APEX is a framework for agents"}'

curl -X POST http://localhost:8001/memory/query \
  -H "Content-Type: application/json" \
  -d '{"space_id":"docs","query":"What is APEX?"}'
```
