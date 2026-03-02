import React, { useEffect, useState } from 'react'
import { askQuestionApi, getChatMessagesApi } from '../services/chatApi';

function ChatScreen({ chat }) {
  if (!chat) {
    return (
      <div className="flex-1 flex items-center justify-center text-gray-400">
        Start a new chat to begin
      </div>
    );
  }

   const [message, setMessage] = useState("");
   const [messages, setMessages] = useState([]);
   const [loading, setLoading] = useState(false);
  const [loadingMessages, setLoadingMessages] = useState(false);

   // ✅ Load messages when chat changes
  useEffect(() => {
    const fetchMessages = async () => {
      if (!chat?.id) return;

      try {
        setLoadingMessages(true);

        const response = await getChatMessagesApi(chat.id);
        console.log(response.data);
        
        setMessages(response.data);

      } catch (error) {
        console.error("Failed to load messages:", error);
      } finally {
        setLoadingMessages(false);
      }
    };

    fetchMessages();
  }, [chat?.id]);

    const handleSend = async () => {
    if (!message.trim()) return;

    const userMessage = {
      role: "user",
      content: message,
    };

    // Optimistically update UI
    setMessages((prev) => [...prev, userMessage]);
    setMessage("");
    setLoading(true);

    try {
      const response = await askQuestionApi(chat.id, userMessage.content);
      console.log(response.data);
       const aiMessage = {
        role: "assistant",
        content: response.data.answer,
      };
 setMessages((prev) => [...prev, aiMessage]);

    } catch (error) {
      console.error("Ask API error:", error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Something went wrong.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

 return (
      <div className="flex-1 flex flex-col bg-gray-900">

      {/* Chat Title */}
      <div className="h-12 flex items-center px-4 border-b border-gray-700">
        <h2 className="text-white font-medium">
          {chat.title}
        </h2>
      </div>

      {/* Messages Area */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">

        {loadingMessages ? (
          <div className="text-gray-400">Loading messages...</div>
        ) : (
          messages.map((msg) => (
            <div
              key={msg.id}
              className={`flex ${
                msg.role === "user" ? "justify-end" : "justify-start"
              }`}
            >
              <div
                className={`px-4 py-2 rounded-lg max-w-lg text-sm ${
                  msg.role === "user"
                    ? "bg-blue-600 text-white"
                    : "bg-gray-700 text-gray-200"
                }`}
              >
                <p className="whitespace-pre-wrap break-words">
  {msg.content}
</p>

              </div>
            </div>
          ))
        )}

        {loading && (
          <div className="text-gray-400 text-sm">
            AI is typing...
          </div>
        )}
      </div>
      {/* Input Area */}
      <div className="p-4 border-t border-gray-700">
        <div className="flex gap-2">
          <input
            type="text"
            placeholder="Type your message..."
             onChange={(e) => setMessage(e.target.value)}
             value={message}
            className="
              flex-1
              bg-gray-800
              border border-gray-700
              rounded
              px-3 py-2
              text-white
              focus:outline-none
              focus:border-blue-500
            "
          />
          <button onClick={handleSend}  onChange={(e) => setMessage(e.target.value)} className="bg-blue-600 hover:bg-blue-700 text-white px-4 rounded">
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

export default ChatScreen