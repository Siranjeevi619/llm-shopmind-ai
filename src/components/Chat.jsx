import { useEffect, useRef, useState } from "react";
import Message from "./Message";
import { sendMessage, fetchMessages } from "../services/api";

export default function Chat({ conversationId }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const bottomRef = useRef(null);

  useEffect(() => {
    if (!conversationId) {
      setMessages([]);
      return;
    }
    fetchMessages(conversationId).then(setMessages);
  }, [conversationId]);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

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
      {/* Messages */}
      <div className="flex-1 overflow-y-auto px-6 py-8 space-y-6">
        {messages.length === 0 ? (
          <div className="text-center text-gray-400 mt-32">
            <h2 className="text-xl mb-2">How can I help you today?</h2>
            <p className="text-sm">Ask about products, stock, or orders</p>
          </div>
        ) : (
          messages.map((m, i) => <Message key={i} {...m} />)
        )}
        <div ref={bottomRef} />
      </div>

      {/* Input */}
      <div className="border-t border-white/10 p-4 bg-[#343541]">
        <div className="max-w-3xl mx-auto flex gap-2">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            placeholder="Send a message..."
            className="flex-1 bg-[#40414f] px-4 py-3 rounded text-sm outline-none"
          />
          <button
            onClick={handleSend}
            className="px-4 py-3 rounded bg-white text-black text-sm"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
