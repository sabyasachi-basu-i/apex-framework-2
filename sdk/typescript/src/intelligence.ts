export async function ingest(spaceId: string, content: string, baseUrl?: string): Promise<string> {
  const url = `${baseUrl || process.env.NEXT_PUBLIC_INTELLIGENCE_URL || ''}/memory/ingest`;
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ space_id: spaceId, content })
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.detail || 'Failed to ingest');
  return data.doc_id;
}

export async function query(spaceId: string, queryText: string, topK = 5, baseUrl?: string) {
  const url = `${baseUrl || process.env.NEXT_PUBLIC_INTELLIGENCE_URL || ''}/memory/query`;
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ space_id: spaceId, query: queryText, top_k: topK })
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.detail || 'Failed to query');
  return data.results;
}

export async function completion(prompt: string, maxTokens = 256, baseUrl?: string) {
  const url = `${baseUrl || process.env.NEXT_PUBLIC_INTELLIGENCE_URL || ''}/llm/completions`;
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt, max_tokens: maxTokens })
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.detail || 'Failed to complete');
  return data.completion || data;
}