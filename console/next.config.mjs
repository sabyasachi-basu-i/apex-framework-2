/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  async rewrites() {
    const orchestrationBase = process.env.NEXT_PUBLIC_ORCHESTRATION_URL || 'http://localhost:8003';
    const intelligenceBase = process.env.NEXT_PUBLIC_INTELLIGENCE_URL || 'http://localhost:8001';
    const integrationBase = process.env.NEXT_PUBLIC_INTEGRATION_URL || 'http://localhost:8002';
    const governanceBase = process.env.NEXT_PUBLIC_GOVERNANCE_URL || 'http://localhost:8004';

    return [
      {
        source: '/orchestration/:path*',
        destination: `${orchestrationBase}/orchestration/:path*`,
      },
      {
        source: '/memory/:path*',
        destination: `${intelligenceBase}/memory/:path*`,
      },
      {
        source: '/integration/:path*',
        destination: `${integrationBase}/integration/:path*`,
      },
      {
        source: '/governance/:path*',
        destination: `${governanceBase}/governance/:path*`,
      },
      {
        source: '/config',
        destination: `${governanceBase}/config`,
      },
    ];
  },
};

export default nextConfig;
