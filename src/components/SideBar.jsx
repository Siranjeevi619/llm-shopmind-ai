import { useEffect, useState } from "react";
import { fetchConversations } from "../services/api";

export default function Sidebar({ onSelect, onNewChat }) {
  const [chats, setChats] = useState([]);

  useEffect(() => {
    fetchConversations().then(setChats);
  }, []);

  return (
    <div className="w-64 bg-[#202123] p-4">
      <h1 className="text-lg mb-4">ShopMind AI</h1>

      <button className="border mb-4 px-2 py-1 w-full" onClick={onNewChat}>
        + New Chat
      </button>

      <div className="space-y-2 text-sm">
        {chats.map((chat) => (
          <div
            key={chat._id}
            onClick={() => onSelect(chat._id)}
            className="truncate text-gray-300 cursor-pointer hover:bg-[#2a2b32] p-1 rounded"
          >
            {chat.title || "New Chat"}
          </div>
        ))}
      </div>
    </div>
  );
}
