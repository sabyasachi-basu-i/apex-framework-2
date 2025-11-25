# Governance Layer

The Governance Layer provides security, policy enforcement and observability for agentic systems.  It is implemented by the `governance-service` microservice.

## Capabilities

* **Authentication** – issue and validate JSON Web Tokens (JWT) to identify users and agents.  In production you should integrate with your SSO or identity provider.
* **RBAC** – role‑based access control.  Users can be assigned roles such as `admin`, `architect`, `developer` or `viewer`, and each role grants different permissions.
* **Audit logging** – record every agent run, connector call and system change.  Audit logs include who performed the action, when it occurred and any relevant metadata.  In the current implementation logs are stored in memory; for real deployments connect to a database or a log aggregator.
* **Observability** – placeholder for integration with metrics and tracing systems such as Grafana, Prometheus or Datadog.

## API endpoints

| Endpoint          | Method | Description                                                       |
|-------------------|-------|-------------------------------------------------------------------|
| `/auth/login`     | POST  | Generate a token for a user (placeholder implementation)          |
| `/rbac/users`     | GET   | List users and their roles (placeholder)                          |
| `/audit/log`      | POST  | Record an audit event                                             |

## Configuration

Set the `APEX_SECRET_KEY` environment variable to a strong random value for signing JWTs.  You can also persist users and logs by extending the models in `apex_governance/models.py` and connecting to a database.