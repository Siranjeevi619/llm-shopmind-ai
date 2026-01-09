import Sidebar from "../components/Sidebar";
import Chat from "../components/Chat";

export default function ChatPage() {
  return (
    <div className="flex h-screen bg-[#343541] text-white">
      <Sidebar />
      <Chat />
    </div>
  );
}
