import api from "./api";

/**
 * Create new chat
 */
export const createChatApi = () => {
  return api.post("/chats");
};

/**
 * Send message to chat
 */
export const askQuestionApi = (chatId, question) => {
  return api.post("/messages/ask", {
    chat_id: chatId,
    question: question,
  });
};

export const getChatMessagesApi = (chatId) => {
  return api.get(`/messages/chat/${chatId}`);
};

export const uploadDocumentApi = (formData) => {
  return api.post("/documents/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
};