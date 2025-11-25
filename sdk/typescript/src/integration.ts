export async function execute(connectorType: string, operation: string, payload: any, baseUrl?: string) {
  const url = `${baseUrl || process.env.NEXT_PUBLIC_INTEGRATION_URL || ''}/connectors/execute`;
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ connector_type: connectorType, operation, payload })
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.detail || 'Failed to execute');
  return data.result;
}