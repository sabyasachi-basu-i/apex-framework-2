import React from 'react';
import classNames from 'classnames';

export const PageHeader: React.FC<{ title: string; description?: string; actions?: React.ReactNode }> = ({
  title,
  description,
  actions,
}) => (
  <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-3">
    <div>
      <p className="section-title">Overview</p>
      <h2 className="text-2xl font-bold">{title}</h2>
      {description && <p className="text-gray-600 dark:text-gray-300 mt-1">{description}</p>}
    </div>
    {actions && <div className="flex items-center gap-2">{actions}</div>}
  </div>
);

export const SectionCard: React.FC<{ title: string; children: React.ReactNode; actions?: React.ReactNode }>
= ({ title, children, actions }) => (
  <div className="card p-4 space-y-3">
    <div className="flex items-center justify-between">
      <h3 className="text-lg font-semibold">{title}</h3>
      {actions}
    </div>
    {children}
  </div>
);

export const MetricCard: React.FC<{ label: string; value: string; trend?: string }>= ({ label, value, trend }) => (
  <div className="card p-4 space-y-2">
    <p className="text-sm text-gray-500">{label}</p>
    <p className="text-3xl font-bold">{value}</p>
    {trend && <p className="text-xs text-green-600 dark:text-green-400">{trend}</p>}
  </div>
);

export const StatusTag: React.FC<{ status: 'healthy' | 'degraded' | 'error' | string }> = ({ status }) => {
  const color =
    status === 'healthy'
      ? 'bg-green-100 text-green-700'
      : status === 'degraded'
        ? 'bg-yellow-100 text-yellow-700'
        : 'bg-red-100 text-red-700';
  return <span className={classNames('px-2 py-1 rounded-full text-xs font-semibold', color)}>{status}</span>;
};

export const LoadingSkeleton: React.FC<{ lines?: number }> = ({ lines = 3 }) => (
  <div className="space-y-2 animate-pulse">
    {Array.from({ length: lines }).map((_, idx) => (
      <div key={idx} className="h-3 bg-gray-200 dark:bg-gray-800 rounded" />
    ))}
  </div>
);

export const APIError: React.FC<{ message: string }> = ({ message }) => (
  <div className="rounded-lg border border-red-200 bg-red-50 text-red-700 p-3">{message}</div>
);

export const DataTable: React.FC<{ columns: string[]; rows: React.ReactNode[][]; loading?: boolean }> = ({
  columns,
  rows,
  loading,
}) => (
  <div className="overflow-x-auto">
    <table className="min-w-full text-sm">
      <thead>
        <tr className="text-left text-gray-500 uppercase text-xs">
          {columns.map((col) => (
            <th key={col} className="px-3 py-2">
              {col}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {loading ? (
          <tr>
            <td colSpan={columns.length} className="px-3 py-4">
              <LoadingSkeleton lines={4} />
            </td>
          </tr>
        ) : (
          rows.map((row, idx) => (
            <tr key={idx} className="border-t border-gray-100 dark:border-gray-800">
              {row.map((cell, cellIdx) => (
                <td key={cellIdx} className="px-3 py-2">
                  {cell}
                </td>
              ))}
            </tr>
          ))
        )}
      </tbody>
    </table>
  </div>
);
