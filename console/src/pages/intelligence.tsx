import React, { useState } from 'react';
import { Layout } from '../components/Layout';

export default function IntelligencePage() {
  const [spaceId, setSpaceId] = useState('demo');
  const [content, setContent] = useState('');
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<any[]>([]);
  const [message, setMessage] = useState<string | null>(null);

  const ingest = async () => {
    setMessage(null);
    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_INTELLIGENCE_URL}/memory/ingest`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ space_id: spaceId, content })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || 'Failed to ingest');
      setMessage(`Ingested document with id ${data.doc_id}`);
      setContent('');
    } catch (err: any) {
      setMessage(err.message);
    }
  };

  const search = async () => {
    setMessage(null);
    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_INTELLIGENCE_URL}/memory/query`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ space_id: spaceId, query, top_k: 5 })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || 'Failed to query');
      setResults(data.results || []);
    } catch (err: any) {
      setMessage(err.message);
    }
  };

  return (
    <Layout>
      <h2 style={{ fontSize: '1.5rem', fontWeight: 600, marginBottom: '1rem' }}>Intelligence</h2>
      <p>Ingest text into a memory space and query it using simple semantic search.</p>
      <div style={{ marginTop: '1rem', marginBottom: '1rem' }}>
        <label>
          Space ID:
          <input type="text" value={spaceId} onChange={e => setSpaceId(e.target.value)} style={{ marginLeft: '0.5rem' }} />
        </label>
      </div>
      <div style={{ marginBottom: '1rem' }}>
        <textarea
          rows={3}
          placeholder="Enter text to ingest"
          value={content}
          onChange={e => setContent(e.target.value)}
          style={{ width: '100%', padding: '0.5rem' }}
        />
        <button onClick={ingest} style={{ marginTop: '0.5rem' }}>Ingest</button>
      </div>
      <div style={{ marginBottom: '1rem' }}>
        <input
          type="text"
          placeholder="Enter query"
          value={query}
          onChange={e => setQuery(e.target.value)}
          style={{ width: '100%', padding: '0.5rem' }}
        />
        <button onClick={search} style={{ marginTop: '0.5rem' }}>Query</button>
      </div>
      {message && <p style={{ color: 'red' }}>{message}</p>}
      {results.length > 0 && (
        <div>
          <h3>Results</h3>
          <ul>
            {results.map((res: any) => (
              <li key={res.doc_id}>
                <strong>{res.doc_id}</strong> (score: {res.score.toFixed(2)})<br />
                {res.content}
              </li>
            ))}
          </ul>
        </div>
      )}
    </Layout>
  );
}