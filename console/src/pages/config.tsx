import React, { useEffect, useState } from 'react';
import { Layout } from '../components/Layout';
import { PageHeader, SectionCard, APIError } from '../components/ui';
import { apiFetch } from '../lib/api';

const CONFIG_URL = '/api/config';

export default function ConfigPage() {
  const [form, setForm] = useState({
    OPENAI_API_KEY: '',
    MODEL_NAME: 'gpt-4o-mini',
    TEMPERATURE: 0.2,
    MAX_RETRIES: 2,
  });
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    apiFetch(CONFIG_URL)
      .then((data) => setForm(data))
      .catch((err) => setError(err.message));
  }, []);

  const save = async () => {
    try {
      setError(null);
      await apiFetch(CONFIG_URL, { method: 'POST', body: JSON.stringify(form) });
    } catch (err: any) {
      setError(err.message);
    }
  };

  return (
    <Layout>
      <PageHeader title="Runtime Config" description="Edit runtime settings for all services" />
      <SectionCard title="Settings" actions={<button className="px-4 py-2 rounded-lg bg-primary-600 text-white" onClick={save}>Save</button>}>
        {error && <APIError message={error} />}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {Object.entries(form).map(([key, value]) => (
            <label key={key} className="space-y-1 text-sm font-medium text-gray-700 dark:text-gray-200">
              <span>{key}</span>
              <input
                className="w-full rounded-lg border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-900 px-3 py-2"
                value={String(value)}
                onChange={(e) => setForm({ ...form, [key]: e.target.value })}
              />
            </label>
          ))}
        </div>
      </SectionCard>
    </Layout>
  );
}
