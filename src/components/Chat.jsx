import { useState } from "react";
import Message from "./Message";
import { sendMessage } from "../services/api";

export default function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMsg = { role: "user", content: input };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");

    const reply = await sendMessage(input);

    setMessages((prev) => [...prev, { role: "assistant", content: reply }]);
  };

  return (
    <div className="flex flex-col flex-1">
      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-6 space-y-4">
        {messages.map((msg, i) => (
          <Message key={i} {...msg} />
        ))}
      </div>

      {/* Input */}
      <div className="border-t border-gray-700 p-4 bg-[#40414f]">
        <div className="flex gap-2">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask about products..."
            className="flex-1 bg-[#343541] text-white px-4 py-2 rounded-md outline-none"
          />
          <button
            onClick={handleSend}
            className="bg-emerald-500 text-black px-4 py-2 rounded-md hover:bg-emerald-400"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
