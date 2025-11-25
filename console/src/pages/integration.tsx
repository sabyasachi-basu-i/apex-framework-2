import React from 'react';
import { Layout } from '../components/Layout';
import { PageHeader, SectionCard } from '../components/ui';

export default function Integration() {
  return (
    <Layout>
      <PageHeader title="Integration" description="Connectors for external systems" />
      <SectionCard title="Connectors">
        <p className="text-sm text-gray-600 dark:text-gray-300">Connector execution secured by JWT.</p>
      </SectionCard>
    </Layout>
  );
}
