import React, { PropsWithChildren, useEffect, useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/router';
import classNames from 'classnames';

const navItems = [
  { href: '/', label: 'Dashboard' },
  { href: '/chat', label: 'Chat' },
  { href: '/supermemory', label: 'SuperMemory' },
  { href: '/config', label: 'Config' },
  { href: '/governance', label: 'Governance' },
];

export const Layout: React.FC<PropsWithChildren<unknown>> = ({ children }) => {
  const router = useRouter();
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    const stored = localStorage.getItem('apex-theme');
    if (stored === 'dark') {
      setDarkMode(true);
      document.documentElement.classList.add('dark');
    }
  }, []);

  const toggleTheme = () => {
    const next = !darkMode;
    setDarkMode(next);
    if (next) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('apex-theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('apex-theme', 'light');
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-950 text-gray-900 dark:text-gray-50">
      <div className="flex min-h-screen">
        <aside className="hidden md:flex w-64 flex-col bg-gray-900 text-gray-100 p-6 space-y-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-xs uppercase tracking-wide text-gray-400">APEX</p>
              <h1 className="text-xl font-bold">Agentic Platform</h1>
            </div>
          </div>
          <nav className="space-y-2">
            {navItems.map((item) => (
              <Link key={item.href} href={item.href} legacyBehavior>
                <a
                  className={classNames(
                    'block px-3 py-2 rounded-lg hover:bg-gray-800 transition',
                    router.pathname === item.href ? 'bg-gray-800 text-white' : 'text-gray-200'
                  )}
                >
                  {item.label}
                </a>
              </Link>
            ))}
          </nav>
          <button
            onClick={toggleTheme}
            className="mt-auto inline-flex items-center justify-center rounded-lg border border-gray-700 px-3 py-2 text-sm text-gray-100 hover:bg-gray-800"
          >
            {darkMode ? 'Light mode' : 'Dark mode'}
          </button>
        </aside>

        <div className="flex-1 flex flex-col">
          <header className="sticky top-0 z-10 backdrop-blur bg-white/80 dark:bg-gray-900/80 border-b border-gray-200 dark:border-gray-800">
            <div className="flex items-center justify-between px-4 md:px-8 py-4">
              <div className="md:hidden flex items-center space-x-3 text-lg font-semibold">APEX</div>
              <div className="flex items-center space-x-4">
                <span className="text-sm text-gray-500">Multi-service Agentic Platform</span>
              </div>
              <button
                onClick={toggleTheme}
                className="inline-flex items-center justify-center rounded-lg border border-gray-200 dark:border-gray-700 px-3 py-2 text-sm"
              >
                {darkMode ? 'Light' : 'Dark'}
              </button>
            </div>
          </header>

          <main className="px-4 md:px-8 py-6 space-y-6">
            {children}
          </main>
        </div>
      </div>
    </div>
  );
};
