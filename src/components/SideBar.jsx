export default function Sidebar() {
  const role = localStorage.getItem("role");

  return (
    <div className="w-64 bg-[#202123] p-4 flex flex-col">
      {/* App Title */}
      <h1 className="text-lg font-semibold mb-1">ShopMind AI</h1>

      {/* ADMIN BADGE */}
      {role === "ADMIN" && (
        <span className="text-xs text-emerald-400 mb-4">● Admin Mode</span>
      )}

      {/* New Chat Button */}
      <button className="border border-gray-600 rounded-md px-3 py-2 text-sm hover:bg-gray-700">
        + New Chat
      </button>
    </div>
  );
}
