import type { NextApiRequest, NextApiResponse } from 'next';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  const { path, ...queryParams } = req.query;
  const pathStr = Array.isArray(path) ? path.join('/') : (path || '');
  const intelligenceBase = process.env.NEXT_PUBLIC_INTELLIGENCE_URL || 'http://localhost:8001';

  // Build URL with query parameters
  const baseUrl = `${intelligenceBase}/memory/${pathStr}`;
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
    const authHeader = req.headers.authorization;
    console.log('[Memory API Proxy] Incoming authorization header:', authHeader ? 'Present' : 'Missing');
    console.log('[Memory API Proxy] All headers:', Object.keys(req.headers));

    if (authHeader) {
      headers['authorization'] = authHeader;
    }

    // Forward Cookie header if present
    const cookieHeader = req.headers.cookie;
    console.log('[Memory API Proxy] Incoming cookie header:', cookieHeader ? 'Present' : 'Missing');

    if (cookieHeader) {
      headers['cookie'] = cookieHeader;
    }

    console.log('[Memory API Proxy] Forwarding to:', url);
    console.log('[Memory API Proxy] Forwarding headers:', headers);

    const response = await fetch(url, {
      method: req.method,
      headers,
      body: req.method !== 'GET' && req.method !== 'HEAD' ? JSON.stringify(req.body) : undefined,
    });

    console.log('[Memory API Proxy] Response status:', response.status);

    const data = await response.json();
    res.status(response.status).json(data);
  } catch (error) {
    console.error('[Memory API Proxy] Error:', error);
    res.status(500).json({ detail: 'Proxy error', error: String(error) });
  }
}
