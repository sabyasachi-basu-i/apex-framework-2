import React, { useEffect, useState } from 'react';
import { Layout } from '../components/Layout';

export default function GovernancePage() {
  const [users, setUsers] = useState<any[]>([]);
  const [events, setEvents] = useState<any[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const usersRes = await fetch(`${process.env.NEXT_PUBLIC_GOVERNANCE_URL}/rbac/users`);
        const usersData = await usersRes.json();
        setUsers(usersData.users || []);
        const eventsRes = await fetch(`${process.env.NEXT_PUBLIC_GOVERNANCE_URL}/audit/events`);
        const eventsData = await eventsRes.json();
        setEvents(eventsData.events || []);
      } catch (err: any) {
        setError(err.message);
      }
    };
    fetchData();
  }, []);

  return (
    <Layout>
      <h2 style={{ fontSize: '1.5rem', fontWeight: 600, marginBottom: '1rem' }}>Governance</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <div style={{ marginBottom: '1rem' }}>
        <h3>Users</h3>
        <ul>
          {users.map((u: any) => (
            <li key={u.email}>{u.email} – {u.role}</li>
          ))}
        </ul>
      </div>
      <div>
        <h3>Audit events</h3>
        <ul>
          {events.map((e: any, idx: number) => (
            <li key={idx}>{JSON.stringify(e)}</li>
          ))}
        </ul>
      </div>
    </Layout>
  );
}