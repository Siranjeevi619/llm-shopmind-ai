import { useState } from "react";
import { logout } from "../services/auth";
import { useNavigate } from "react-router-dom";
import TitleModal from "./TitleModal";

export default function Sidebar({ chats, activeChat, onSelect, onNewChat }) {
  const [showModal, setShowModal] = useState(false);
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/");
  };

  const handleCreateChat = (title) => {
    onNewChat(title);
    setShowModal(false);
  };

  return (
    <>
      <div className="w-72 bg-[#202123] border-r border-white/10 flex flex-col">
        {/* Header */}
        <div className="p-4 border-b border-white/10">
          <button
            onClick={() => setShowModal(true)}
            className="w-full py-2 text-sm rounded border border-white/20 hover:bg-white/10"
          >
            + New chat
          </button>
        </div>

        {/* Chat list */}
        <div className="flex-1 overflow-y-auto p-2 space-y-1">
          {chats.map((chat) => (
            <div
              key={chat._id}
              onClick={() => onSelect(chat._id)}
              className={`px-3 py-2 rounded text-sm cursor-pointer truncate
                ${
                  activeChat === chat._id ? "bg-white/20" : "hover:bg-white/10"
                }`}
            >
              {chat.title || "New conversation"}
            </div>
          ))}
        </div>

        {/* Footer */}
        <div className="p-4 border-t border-white/10 flex justify-between text-xs text-gray-400">
          <span>ShopMind AI</span>
          <button onClick={handleLogout} className="hover:text-white">
            Logout
          </button>
        </div>
      </div>

      <TitleModal
        open={showModal}
        onClose={() => setShowModal(false)}
        onSubmit={handleCreateChat}
      />
    </>
  );
}
