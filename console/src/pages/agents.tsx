import React from 'react';
import { Layout } from '../components/Layout';
import { PageHeader, SectionCard } from '../components/ui';

export default function Agents() {
  return (
    <Layout>
      <PageHeader title="Agents" description="Manage agent personas and roles" />
      <SectionCard title="Agents">
        <p className="text-sm text-gray-600 dark:text-gray-300">Agent management coming soon.</p>
      </SectionCard>
    </Layout>
  );
}
