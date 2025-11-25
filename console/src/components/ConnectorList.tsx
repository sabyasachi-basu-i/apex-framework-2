import React from 'react';

interface Connector {
  type: string;
  description: string;
}

interface ConnectorListProps {
  connectors: Connector[];
}

export const ConnectorList: React.FC<ConnectorListProps> = ({ connectors }) => {
  return (
    <ul style={{ listStyle: 'none', padding: 0 }}>
      {connectors.map(conn => (
        <li key={conn.type} style={{ marginBottom: '0.75rem' }}>
          <strong>{conn.type}</strong> &mdash; {conn.description}
        </li>
      ))}
    </ul>
  );
};