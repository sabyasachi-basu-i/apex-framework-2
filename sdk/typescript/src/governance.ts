export async function login(email: string, baseUrl?: string) {
  const url = `${baseUrl || process.env.NEXT_PUBLIC_GOVERNANCE_URL || ''}/auth/login`;
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email })
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.detail || 'Failed to login');
  return data;
}

export async function listUsers(baseUrl?: string) {
  const url = `${baseUrl || process.env.NEXT_PUBLIC_GOVERNANCE_URL || ''}/rbac/users`;
  const res = await fetch(url);
  const data = await res.json();
  if (!res.ok) throw new Error(data.detail || 'Failed to list users');
  return data.users;
}

export async function listAuditEvents(baseUrl?: string) {
  const url = `${baseUrl || process.env.NEXT_PUBLIC_GOVERNANCE_URL || ''}/audit/events`;
  const res = await fetch(url);
  const data = await res.json();
  if (!res.ok) throw new Error(data.detail || 'Failed to list events');
  return data.events;
}