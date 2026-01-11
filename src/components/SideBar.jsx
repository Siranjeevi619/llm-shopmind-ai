import { useEffect, useState } from "react";
import { fetchConversations } from "../services/api";

export default function Sidebar({ onSelect, onNewChat, activeChat }) {
  const [chats, setChats] = useState([]);

  useEffect(() => {
    fetchConversations().then(setChats);
  }, []);

  return (
    <div className="w-72 bg-[#202123] border-r border-white/10 flex flex-col">
      {/* Header */}
      <div className="p-4 border-b border-white/10">
        <button
          onClick={onNewChat}
          className="w-full py-2 text-sm rounded border border-white/20 hover:bg-white/10"
        >
          + New chat
        </button>
      </div>

      {/* Conversations */}
      <div className="flex-1 overflow-y-auto p-2 space-y-1">
        {chats.map((chat) => (
          <div
            key={chat._id}
            onClick={() => onSelect(chat._id)}
            className={`px-3 py-2 rounded text-sm cursor-pointer truncate
              ${activeChat === chat._id ? "bg-white/20" : "hover:bg-white/10"}`}
          >
            {chat.title || "New conversation"}
          </div>
        ))}
      </div>

      {/* Footer */}
      <div className="p-4 border-t border-white/10 text-xs text-gray-400">
        ShopMind AI
      </div>
    </div>
  );
}
