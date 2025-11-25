import React from 'react';
import { Layout } from '../components/Layout';
import { ConnectorList } from '../components/ConnectorList';

export default function IntegrationPage() {
  const connectors = [
    { type: 'sql', description: 'Query relational databases via SQLAlchemy' },
    { type: 'salesforce', description: 'Placeholder for Salesforce CRM' },
    { type: 'icertis', description: 'Placeholder for Icertis CLM' },
    { type: 'blob_storage', description: 'Placeholder for file and blob storage' }
  ];
  return (
    <Layout>
      <h2 style={{ fontSize: '1.5rem', fontWeight: 600, marginBottom: '1rem' }}>Integration</h2>
      <p>The Integration layer exposes connectors to external systems.  Below is a list of available connectors.</p>
      <ConnectorList connectors={connectors} />
    </Layout>
  );
}