import React, { useState } from 'react';
import { Layout } from '../components/Layout';
import { PageHeader, SectionCard, LoadingSkeleton } from '../components/ui';
import { apiFetch } from '../lib/api';

const CHAT_URL = `${process.env.NEXT_PUBLIC_ORCHESTRATION_URL || ''}/orchestration/chat`;

type Message = { role: 'user' | 'assistant'; content: string; timestamp: string };

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input) return;
    const newMessage: Message = { role: 'user', content: input, timestamp: new Date().toISOString() };
    setMessages((prev) => [...prev, newMessage]);
    setInput('');
    setLoading(true);
    try {
      const res = await apiFetch(CHAT_URL, { method: 'POST', body: JSON.stringify({ message: newMessage.content }) });
      setMessages((prev) => [...prev, { role: 'assistant', content: res.message, timestamp: res.timestamp }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Layout>
      <PageHeader title="Chat Agent" description="Test the orchestration chat endpoint" />
      <SectionCard title="Conversation">
        <div className="space-y-3 max-h-[480px] overflow-y-auto pr-2">
          {messages.map((msg, idx) => (
            <div key={idx} className={msg.role === 'user' ? 'flex justify-end' : 'flex justify-start'}>
              <div className="max-w-xl rounded-2xl px-4 py-3 bg-gray-100 dark:bg-gray-800">
                <p className="text-sm text-gray-500">{msg.role} · {new Date(msg.timestamp).toLocaleTimeString()}</p>
                <p className="mt-1 leading-relaxed">{msg.content}</p>
              </div>
            </div>
          ))}
          {loading && <LoadingSkeleton lines={2} />}
        </div>
        <div className="flex items-center gap-2 pt-4">
          <input
            className="flex-1 rounded-lg border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-900 px-3 py-2"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask something"
          />
          <button onClick={sendMessage} className="rounded-lg bg-primary-600 text-white px-4 py-2">Send</button>
        </div>
      </SectionCard>
    </Layout>
  );
}
