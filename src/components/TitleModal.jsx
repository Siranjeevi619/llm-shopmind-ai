import { useState } from "react";

export default function TitleModal({ open, onClose, onSubmit }) {
  const [title, setTitle] = useState("");

  if (!open) return null;

  const handleCreate = () => {
    if (!title.trim()) return;
    onSubmit(title.trim());
    setTitle("");
  };

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-[#202123] w-full max-w-md rounded-xl p-6 text-white">
        <h2 className="text-lg font-semibold mb-2">New conversation</h2>
        <p className="text-sm text-gray-400 mb-4">
          Give your conversation a title
        </p>

        <input
          autoFocus
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleCreate()}
          placeholder="e.g. Samsung stock enquiry"
          className="w-full px-4 py-3 rounded bg-[#40414f] outline-none mb-4"
        />

        <div className="flex justify-end gap-2">
          <button
            onClick={onClose}
            className="px-4 py-2 text-sm text-gray-400 hover:text-white"
          >
            Cancel
          </button>
          <button
            onClick={handleCreate}
            className="px-4 py-2 rounded bg-white text-black text-sm"
          >
            Create
          </button>
        </div>
      </div>
    </div>
  );
}
