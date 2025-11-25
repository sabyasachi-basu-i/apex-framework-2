# Integration Layer

The Integration Layer exposes enterprise data sources and systems to agents via a unified connector abstraction.  It is implemented by the `integration-service` microservice.

## Connectors

A connector encapsulates the details of connecting to an external system.  Each connector implements two methods:

* `test_connection()` – returns `True` if the connection can be established.
* `execute(operation: str, payload: dict)` – performs the requested operation (for example, run a SQL query) and returns the result.

Connectors included in this repository:

| Connector    | Description                                                        |
|--------------|--------------------------------------------------------------------|
| `SQL`        | Uses SQLAlchemy to run SQL queries against a database              |
| `Salesforce` | Placeholder for Salesforce integration via REST                   |
| `Icertis`    | Placeholder for Icertis contract management integration           |
| `BlobStorage`| Placeholder for file and blob storage interactions                |

To add your own connector, subclass `apex_integration.connectors.base.BaseConnector` and implement the two methods.  Then register it in the `CONNECTOR_TYPES` dictionary in `apex_integration/connectors/__init__.py`.

## API endpoint

```
POST /connectors/execute
{
  "connector_type": "sql",
  "operation": "query",
  "payload": {
    "query": "SELECT * FROM my_table"
  }
}
```

The integration service will instantiate the appropriate connector and execute the operation.  The response includes the connector's return value.

## Configuration

Set the `APEX_SQL_CONNECTION_STRING` environment variable to configure the default connection string for the SQL connector when running via Docker Compose.  You can override this per request by including credentials in the payload.