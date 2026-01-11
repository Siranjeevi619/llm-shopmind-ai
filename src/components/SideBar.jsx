export default function Sidebar() {
  const role = localStorage.getItem("role");

  return (
    <div className="w-64 bg-[#202123] p-4 flex flex-col">
      <h1 className="text-lg font-semibold mb-2">ShopMind AI</h1>

      {role === "ADMIN" && (
        <span className="text-xs text-emerald-400 mb-4">● Admin Mode</span>
      )}

      <button className="border border-gray-600 rounded-md px-3 py-2 text-sm hover:bg-gray-700">
        + New Chat
      </button>
    </div>
  );
}
