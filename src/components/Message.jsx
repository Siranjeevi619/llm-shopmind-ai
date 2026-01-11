export default function Message({ role, content }) {
  const isUser = role === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-[60%] px-4 py-3 rounded-lg text-sm
        ${isUser ? "bg-emerald-500 text-black" : "bg-[#444654] text-white"}`}
      >
        {content}
      </div>
    </div>
  );
}
