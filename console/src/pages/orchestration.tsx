import React from 'react';
import { Layout } from '../components/Layout';
import { PageHeader, SectionCard } from '../components/ui';

export default function Orchestration() {
  return (
    <Layout>
      <PageHeader title="Orchestration" description="Run flows and agent conversations" />
      <SectionCard title="Overview">
        <p className="text-sm text-gray-600 dark:text-gray-300">Use the Chat page to exercise orchestration streaming.</p>
      </SectionCard>
    </Layout>
  );
}
