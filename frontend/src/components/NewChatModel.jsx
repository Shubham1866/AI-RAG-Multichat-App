import { useState } from "react";

function NewChatModal({ onClose, onStart }) {
  const [title, setTitle] = useState("");

  return (
    <div className="fixed inset-0 bg-black/60 flex items-center justify-center z-50">
      <div className="bg-gray-800 p-6 rounded-lg w-80 text-white">
        <h3 className="mb-4 text-lg font-semibold">Start New Chat</h3>

        <input
          type="text"
          placeholder="Enter chat title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          style={{ color:"white" }}
          className="w-full mb-4 px-3 py-2 bg-gray-700 border border-gray-600 rounded"
        />

        <div className="flex justify-end gap-2">
          <button
            onClick={onClose}
            className="px-3 py-1 text-sm text-gray-300"
          >
            Cancel
          </button>

          <button
            onClick={() => onStart(title)}
            className="bg-blue-600 hover:bg-blue-700 px-3 py-1 rounded text-sm"
          >
            Start
          </button>
        </div>
      </div>
    </div>
  );
}

export default NewChatModal;
