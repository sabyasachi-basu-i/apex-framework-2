import React from 'react';
import { Layout } from '../components/Layout';
import { LayerCard } from '../components/LayerCard';

export default function Home() {
  const layers = [
    {
      title: 'Intelligence',
      description: 'Reasoning, memory and RAG. Ingest and query documents.',
      link: '/intelligence'
    },
    {
      title: 'Integration',
      description: 'Connect to databases, CRMs and other systems.',
      link: '/integration'
    },
    {
      title: 'Orchestration',
      description: 'Build and run multi-step flows and agents.',
      link: '/orchestration'
    },
    {
      title: 'Governance',
      description: 'Manage users, roles and view audit logs.',
      link: '/governance'
    }
  ];
  return (
    <Layout>
      <h2 style={{ fontSize: '1.5rem', fontWeight: 600, marginBottom: '1rem' }}>Welcome to APEX</h2>
      <p style={{ marginBottom: '2rem' }}>
        APEX is a framework for building and running agentic workflows. Select a layer below to begin exploring.
      </p>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1rem' }}>
        {layers.map(layer => (
          <LayerCard key={layer.title} title={layer.title} description={layer.description} link={layer.link} />
        ))}
      </div>
    </Layout>
  );
}