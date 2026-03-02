import React, { useEffect } from 'react'
import { useState } from "react";
import TopBar from '../components/TopBar'
import ChatList from '../components/ChatList'
import ChatScreen from '../components/ChatScreen'
import NewChatModal from "../components/NewChatModel";
import api, { getChatsApi } from "../services/api";

function ChatLayout() {
  const [chats, setChats] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [activeChat, setActiveChat] = useState(null);

   const fetchChats = async () => {
      try {
        const response = await getChatsApi();
        setChats(response.data);
        
      } catch (error) {
        console.error("Failed to load chats:", error);
      }
    };

    // ✅ Load chats on component mount
  useEffect(() => {   
    fetchChats();
  }, []);

  const startChat = async (title) => {
    if (!title) return;

    try {
      const response = await api.post("/chats/start", {
        title,
      });

      const chatId = response.data.id;

      setActiveChat({id:chatId, title});
      fetchChats();
      setShowModal(false);

    } catch (error) {
      console.error("Error starting chat:", error);
      alert("Failed to start chat");
    }
  };

  return (
    <div className="h-screen flex flex-col bg-gray-900">
      {/* Top Header */}
      <TopBar />

      {/* Main Content */}
      <div className="flex flex-1 overflow-hidden">
        {/* Sidebar */}
        <ChatList  chats={chats} onNewChat={() => setShowModal(true)} activeChat={activeChat} onSelectChat={(chat) => setActiveChat(chat)} />

        {/* Chat Screen */}
        <ChatScreen chat={activeChat}/>

        {showModal && (
        <NewChatModal
          onClose={() => setShowModal(false)}
          onStart={startChat}
        />
      )}
      </div>
    </div>
  );
}

export default ChatLayout