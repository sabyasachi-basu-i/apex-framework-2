import React from 'react';

interface LayerCardProps {
  title: string;
  description: string;
  link: string;
}

export const LayerCard: React.FC<LayerCardProps> = ({ title, description, link }) => {
  return (
    <div style={{ border: '1px solid #e2e8f0', borderRadius: '0.5rem', padding: '1rem', boxShadow: '0 1px 3px rgba(0,0,0,0.1)' }}>
      <h2 style={{ fontSize: '1.25rem', fontWeight: 600, marginBottom: '0.5rem' }}>{title}</h2>
      <p style={{ fontSize: '0.875rem', marginBottom: '0.5rem' }}>{description}</p>
      <a href={link} style={{ color: '#2563eb', fontSize: '0.875rem' }}>Learn more &rarr;</a>
    </div>
  );
};