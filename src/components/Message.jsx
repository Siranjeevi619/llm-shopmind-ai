export default function Message({ role, content }) {
  const isUser = role === "user";

  return (
    <div className="flex">
      <div className="max-w-3xl mx-auto w-full">
        <div
          className={`px-4 py-3 rounded text-sm whitespace-pre-wrap
            ${isUser ? "bg-[#40414f]" : "bg-[#444654]"}`}
        >
          {content}
        </div>
      </div>
    </div>
  );
}
