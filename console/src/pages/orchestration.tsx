import React, { useState } from 'react';
import { Layout } from '../components/Layout';

export default function OrchestrationPage() {
  const [flowPath, setFlowPath] = useState('examples/nrg-production-support/flows/prod_support.yaml');
  const [context, setContext] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  const runFlow = async () => {
    setError(null);
    setContext(null);
    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_ORCHESTRATION_URL}/flows/run`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ flow_path: flowPath, inputs: {} })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || 'Failed to run flow');
      setContext(data.context);
    } catch (err: any) {
      setError(err.message);
    }
  };

  return (
    <Layout>
      <h2 style={{ fontSize: '1.5rem', fontWeight: 600, marginBottom: '1rem' }}>Orchestration</h2>
      <p>Run preconfigured flows defined in YAML files.</p>
      <div style={{ marginBottom: '1rem' }}>
        <label>
          Flow path:
          <input type="text" value={flowPath} onChange={e => setFlowPath(e.target.value)} style={{ marginLeft: '0.5rem', width: '60%' }} />
        </label>
        <button onClick={runFlow} style={{ marginLeft: '0.5rem' }}>Run Flow</button>
      </div>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {context && (
        <pre style={{ background: '#f7fafc', padding: '1rem', borderRadius: '0.5rem' }}>{JSON.stringify(context, null, 2)}</pre>
      )}
    </Layout>
  );
}