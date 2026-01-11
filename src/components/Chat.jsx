import { useEffect, useState } from "react";
import Message from "./Message";
import { sendMessage, fetchMessages } from "../services/api";

export default function Chat({ conversationId }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  useEffect(() => {
    if (!conversationId) {
      setMessages([]);
      return;
    }
    fetchMessages(conversationId).then(setMessages);
  }, [conversationId]);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMsg = { role: "user", content: input };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");

    const res = await sendMessage(input, conversationId);

    setMessages((prev) => [...prev, { role: "assistant", content: res.reply }]);
  };

  return (
    <div className="flex flex-col flex-1">
      <div className="flex-1 overflow-y-auto p-6 space-y-4">
        {messages.map((m, i) => (
          <Message key={i} {...m} />
        ))}
      </div>

      <div className="border-t p-4 bg-[#40414f]">
        <div className="flex gap-2">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            className="flex-1 bg-[#343541] text-white px-4 py-2 rounded"
          />
          <button
            onClick={handleSend}
            className="bg-emerald-500 px-4 py-2 rounded"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
