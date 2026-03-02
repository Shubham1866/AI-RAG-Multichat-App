import React from 'react'

function ChatList({ chats, onNewChat, activeChatId, onSelectChat }) {
  return (
    <div className="w-64 bg-gray-850 border-r border-gray-700 flex flex-col">
      
      {/* Chat List */}
      <div className="flex-1 overflow-y-auto">
       {chats.map((chat) => (
          <div
            key={chat.id}
            onClick={() => onSelectChat(chat)}
            className={`
              px-4 py-3 text-sm cursor-pointer
              hover:bg-gray-700
              ${activeChatId === chat.id ? "bg-gray-700 text-white" : "text-gray-300"}
            `}
          >
            {chat.title}
          </div>
        ))}
      </div>

      {/* New Chat Button */}
      <div className="p-4">
        <button onClick={onNewChat} className="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded text-sm">
          + New Chat
        </button>
      </div>
    </div>
  );
}

export default ChatList