import React, { useEffect, useState } from 'react';
import { Layout } from '../components/Layout';
import { PageHeader, SectionCard, LoadingSkeleton, APIError } from '../components/ui';
import { apiFetch } from '../lib/api';

const GOV_BASE = '/governance';

type Graph = { name: string; nodes: { id: string; label: string }[]; edges: { source: string; target: string }[] };

type AgentsResponse = { agents: { id: string; name: string; children: string[] }[] };

export default function GovernancePage() {
  const [flows, setFlows] = useState<Graph | null>(null);
  const [lineage, setLineage] = useState<Graph | null>(null);
  const [agents, setAgents] = useState<AgentsResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const load = async () => {
      try {
        const [f, l, a] = await Promise.all([
          apiFetch(`${GOV_BASE}/flows`),
          apiFetch(`${GOV_BASE}/lineage`),
          apiFetch(`${GOV_BASE}/agents`),
        ]);
        setFlows(f);
        setLineage(l);
        setAgents(a);
      } catch (err: any) {
        setError(err.message);
      }
    };
    load();
  }, []);

  return (
    <Layout>
      <PageHeader title="Governance" description="Flow visualizations and agent lineage" />
      {error && <APIError message={error} />}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        <SectionCard title="Flow Graph">
          {flows ? (
            <pre className="text-xs bg-gray-100 dark:bg-gray-900 p-3 rounded-lg overflow-x-auto">{JSON.stringify(flows, null, 2)}</pre>
          ) : (
            <LoadingSkeleton />
          )}
        </SectionCard>
        <SectionCard title="Lineage">
          {lineage ? (
            <pre className="text-xs bg-gray-100 dark:bg-gray-900 p-3 rounded-lg overflow-x-auto">{JSON.stringify(lineage, null, 2)}</pre>
          ) : (
            <LoadingSkeleton />
          )}
        </SectionCard>
      </div>
      <SectionCard title="Agents">
        {agents ? (
          <ul className="space-y-2 text-sm">
            {agents.agents.map((agent) => (
              <li key={agent.id} className="flex items-center justify-between">
                <span className="font-semibold">{agent.name}</span>
                <span className="text-gray-500">{agent.children.join(', ') || 'leaf'}</span>
              </li>
            ))}
          </ul>
        ) : (
          <LoadingSkeleton />
        )}
      </SectionCard>
    </Layout>
  );
}
