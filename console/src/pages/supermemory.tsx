import React, { useEffect, useState } from 'react';
import { Layout } from '../components/Layout';
import { PageHeader, SectionCard, DataTable, LoadingSkeleton, APIError } from '../components/ui';
import { apiFetch } from '../lib/api';

const MEMORY_BASE = '/api/memory';

type MemoryEntry = { id: string; content: string; space_id: string };

export default function SuperMemoryPage() {
  const [items, setItems] = useState<MemoryEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [form, setForm] = useState({ content: '', space_id: 'default' });

  const load = async () => {
    setLoading(true);
    try {
      const res = await apiFetch(`${MEMORY_BASE}/list`);
      setItems(res.items || []);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    load();
  }, []);

  const add = async () => {
    try {
      setError(null);
      await apiFetch(`${MEMORY_BASE}/add`, { method: 'POST', body: JSON.stringify(form) });
      setForm({ content: '', space_id: form.space_id });
      await load();
    } catch (err: any) {
      setError(err.message);
    }
  };

  const remove = async (id: string) => {
    await apiFetch(`${MEMORY_BASE}/${id}`, { method: 'DELETE' });
    await load();
  };

  return (
    <Layout>
      <PageHeader title="SuperMemory" description="Manage high-signal memories stored in Chroma or in-memory" />
      <SectionCard
        title="Add Memory"
        actions={
          <button onClick={add} className="rounded-lg bg-primary-600 text-white px-4 py-2">
            Save
          </button>
        }
      >
        {error && <APIError message={error} />}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <label className="space-y-1 text-sm font-medium text-gray-700 dark:text-gray-200">
            <span>Space</span>
            <input
              value={form.space_id}
              onChange={(e) => setForm({ ...form, space_id: e.target.value })}
              className="w-full rounded-lg border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-900 px-3 py-2"
            />
          </label>
          <label className="space-y-1 text-sm font-medium text-gray-700 dark:text-gray-200 md:col-span-2">
            <span>Content</span>
            <textarea
              value={form.content}
              onChange={(e) => setForm({ ...form, content: e.target.value })}
              className="w-full rounded-lg border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-900 px-3 py-2"
              rows={3}
            />
          </label>
        </div>
      </SectionCard>

      <SectionCard title="Stored Memories">
        <DataTable
          columns={["ID", "Space", "Content", "Actions"]}
          rows={items.map((item) => [
            <span key={`${item.id}-id`} className="text-xs text-gray-500">{item.id.slice(0, 8)}</span>,
            item.space_id,
            item.content,
            <button
              key={`${item.id}-btn`}
              onClick={() => remove(item.id)}
              className="text-sm text-red-600 hover:underline"
            >
              Delete
            </button>,
          ])}
          loading={loading}
        />
        {loading && <LoadingSkeleton />}
      </SectionCard>
    </Layout>
  );
}
