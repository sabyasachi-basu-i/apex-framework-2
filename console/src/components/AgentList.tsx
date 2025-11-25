import React from 'react';

interface Agent {
  id: string;
  name: string;
  description: string;
}

interface AgentListProps {
  agents: Agent[];
}

export const AgentList: React.FC<AgentListProps> = ({ agents }) => {
  if (!agents.length) {
    return <p>No agents found.</p>;
  }
  return (
    <ul style={{ listStyle: 'none', padding: 0 }}>
      {agents.map(agent => (
        <li key={agent.id} style={{ marginBottom: '1rem' }}>
          <strong>{agent.name}</strong>
          <p style={{ margin: 0 }}>{agent.description}</p>
        </li>
      ))}
    </ul>
  );
};