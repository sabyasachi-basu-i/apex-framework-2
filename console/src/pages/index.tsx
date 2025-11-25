import React from 'react';
import { Layout } from '../components/Layout';
import { PageHeader, MetricCard, SectionCard, DataTable, StatusTag } from '../components/ui';

export default function Home() {
  const metrics = [
    { label: 'Memories', value: '128', trend: '+5 today' },
    { label: 'Flows run', value: '42', trend: '+3 this week' },
    { label: 'Last agent run', value: '1.4s', trend: 'fast path' },
    { label: 'API latency p95', value: '220ms', trend: 'mocked' },
  ];

  const healthRows = [
    ['Intelligence', <StatusTag key="int" status="healthy" />],
    ['Integration', <StatusTag key="ing" status="healthy" />],
    ['Orchestration', <StatusTag key="orc" status="healthy" />],
    ['Governance', <StatusTag key="gov" status="healthy" />],
  ];

  return (
    <Layout>
      <PageHeader title="Dashboard" description="Metrics across the agentic platform" />
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {metrics.map((m) => (
          <MetricCard key={m.label} label={m.label} value={m.value} trend={m.trend} />
        ))}
      </div>
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        <SectionCard title="System Health">
          <DataTable columns={["Service", "Status"]} rows={healthRows} />
        </SectionCard>
        <SectionCard title="Recent Activity">
          <p className="text-sm text-gray-600 dark:text-gray-300">No incidents reported. Mock data for now.</p>
        </SectionCard>
      </div>
    </Layout>
  );
}
