export async function runFlow(flowPath: string, inputs: any = {}, baseUrl?: string) {
  const url = `${baseUrl || process.env.NEXT_PUBLIC_ORCHESTRATION_URL || ''}/flows/run`;
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ flow_path: flowPath, inputs })
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.detail || 'Failed to run flow');
  return data.context;
}