import { useEffect, useState } from "react";
import Sidebar from "../components/SideBar";
import Chat from "../components/Chat";
import { fetchConversations, createConversation } from "../services/api";

export default function ChatPage() {
  const [activeChat, setActiveChat] = useState(null);
  const [chats, setChats] = useState([]);

  useEffect(() => {
    fetchConversations().then(setChats);
  }, []);

  const handleNewChat = async (title) => {
    const convo = await createConversation(title);

    // ✅ IMMEDIATELY update sidebar
    setChats((prev) => [convo, ...prev]);

    // ✅ Select new chat
    setActiveChat(convo._id);
  };

  return (
    <div className="h-screen w-screen flex bg-[#343541] text-white">
      <Sidebar
        chats={chats}
        activeChat={activeChat}
        onSelect={setActiveChat}
        onNewChat={handleNewChat}
      />
      <Chat conversationId={activeChat} />
    </div>
  );
}
