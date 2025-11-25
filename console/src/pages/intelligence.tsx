import React from 'react';
import { Layout } from '../components/Layout';
import { PageHeader, SectionCard } from '../components/ui';

export default function Intelligence() {
  return (
    <Layout>
      <PageHeader title="Intelligence" description="LLM and memory capabilities" />
      <SectionCard title="Overview">
        <p className="text-sm text-gray-600 dark:text-gray-300">Use the SuperMemory page to manage memories.</p>
      </SectionCard>
    </Layout>
  );
}
