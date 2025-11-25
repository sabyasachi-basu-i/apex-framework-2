import React, { useState } from 'react';
import { Layout } from '../components/Layout';
import { PageHeader, SectionCard, APIError } from '../components/ui';
import { apiFetch } from '../lib/api';

const LOGIN_URL = '/auth/login';

export default function LoginPage() {
  const [email, setEmail] = useState('admin@apex.local');
  const [error, setError] = useState<string | null>(null);

  const login = async () => {
    try {
      setError(null);
      const res = await apiFetch(LOGIN_URL, { method: 'POST', body: JSON.stringify({ email }) });
      localStorage.setItem('apex-token', res.token);
    } catch (err: any) {
      setError(err.message);
    }
  };

  return (
    <Layout>
      <PageHeader title="Login" description="Authenticate to call secured APIs" />
      <SectionCard title="JWT Login" actions={<button onClick={login} className="px-4 py-2 rounded-lg bg-primary-600 text-white">Login</button>}>
        {error && <APIError message={error} />}
        <label className="space-y-2 text-sm font-medium text-gray-700 dark:text-gray-200">
          <span>Email</span>
          <input
            className="w-full rounded-lg border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-900 px-3 py-2"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </label>
      </SectionCard>
    </Layout>
  );
}
