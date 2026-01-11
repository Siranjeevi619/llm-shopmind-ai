import { useState } from "react";
import Chat from "../components/Chat";
import Sidebar from "../components/SideBar";

export default function ChatPage() {
  const [activeChat, setActiveChat] = useState(null);

  return (
    <div className="flex h-screen bg-[#343541] text-white">
      <Sidebar onSelect={setActiveChat} onNewChat={() => setActiveChat(null)} />
      <Chat conversationId={activeChat} />
    </div>
  );
}
