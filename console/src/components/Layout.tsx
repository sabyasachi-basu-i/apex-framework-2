import React, { PropsWithChildren } from 'react';
import Link from 'next/link';

const navItems = [
  { href: '/', label: 'Home' },
  { href: '/intelligence', label: 'Intelligence' },
  { href: '/integration', label: 'Integration' },
  { href: '/orchestration', label: 'Orchestration' },
  { href: '/governance', label: 'Governance' },
  { href: '/agents', label: 'Agents' }
];

export const Layout: React.FC<PropsWithChildren<{}>> = ({ children }) => {
  return (
    <div style={{ display: 'flex', minHeight: '100vh' }}>
      <aside style={{ width: 200, backgroundColor: '#0f172a', color: 'white', padding: '1rem' }}>
        <h1 style={{ fontWeight: 700, marginBottom: '1rem' }}>APEX Console</h1>
        <nav>
          <ul style={{ listStyle: 'none', padding: 0 }}>
            {navItems.map(item => (
              <li key={item.href} style={{ marginBottom: '0.5rem' }}>
                <Link href={item.href} legacyBehavior><a style={{ color: 'inherit', textDecoration: 'none' }}>{item.label}</a></Link>
              </li>
            ))}
          </ul>
        </nav>
      </aside>
      <main style={{ flex: 1, padding: '2rem' }}>
        {children}
      </main>
    </div>
  );
};