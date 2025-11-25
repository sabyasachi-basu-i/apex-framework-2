import type { NextApiRequest, NextApiResponse } from 'next';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  const { path, ...queryParams } = req.query;
  const pathStr = Array.isArray(path) ? path.join('/') : (path || '');
  const integrationBase = process.env.NEXT_PUBLIC_INTEGRATION_URL || 'http://localhost:8002';

  // Build URL with query parameters
  const baseUrl = `${integrationBase}/integration/${pathStr}`;
  const queryString = new URLSearchParams(
    Object.entries(queryParams).reduce((acc, [key, value]) => {
      acc[key] = Array.isArray(value) ? value.join(',') : String(value);
      return acc;
    }, {} as Record<string, string>)
  ).toString();
  const url = queryString ? `${baseUrl}?${queryString}` : baseUrl;

  try {
    const headers: HeadersInit = {
      'Content-Type': 'application/json',
    };

    // Forward Authorization header if present
    if (req.headers.authorization) {
      headers['authorization'] = req.headers.authorization;
    }

    const response = await fetch(url, {
      method: req.method,
      headers,
      body: req.method !== 'GET' && req.method !== 'HEAD' ? JSON.stringify(req.body) : undefined,
    });

    const data = await response.json();
    res.status(response.status).json(data);
  } catch (error) {
    res.status(500).json({ detail: 'Proxy error', error: String(error) });
  }
}
