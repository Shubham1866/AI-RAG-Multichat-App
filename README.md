# 🤖 AI RAG Multichat Application

An AI-powered Retrieval-Augmented Generation (RAG) based Multichat Application that allows users to create chat sessions, ask questions, and receive intelligent, context-aware responses in real time using LLM and document retrieval.

---

## 📌 Problem Statement

Organizations deal with large volumes of unstructured data (documents, reports, internal knowledge bases), making it difficult to retrieve accurate information efficiently.

Traditional systems:

Rely on keyword-based search with low relevance
Lack contextual understanding
Do not support conversational interaction
Increase time spent on information retrieval

---

## 💡 Solution

This project implements a RAG-based conversational AI system that:

Retrieves relevant information using vector embeddings
Enhances responses with context-aware LLM generation
Provides a multi-session chat interface
Stores conversations for traceability and continuity

---

## 📈 Business Impact
⏱️ Reduces manual search time significantly
📊 Improves accuracy of retrieved information
🤖 Enables scalable AI-driven knowledge systems
🏢 Applicable across enterprise, support, and internal tools

---

## 🚀 Features

* 💬 Multi-chat session support
* 🤖 LLM-powered intelligent responses
* 📚 Retrieval-Augmented Generation (RAG) pipeline
* 🔐 Secure authentication and chat workflow
* ⚡ Real-time query processing
* 🗄️ SQL database integration for chat history
* 🎨 Interactive and responsive React UI

---

## 🎬 Chat Application Demo

This demo illustrates the end-to-end chat functionality of the application.
A user creates a chat session, submits a question, and the system processes the query using a RAG + LLM pipeline to generate and display an intelligent response in real time through an interactive chat interface.

<p align="center">
  <img src="assets/demo.gif" width="850"/>
</p>

---

## 🔐 Login Page

The login interface enables users to securely access the application before interacting with the AI-powered chat system.

<p align="center">
  <img src="assets/login.png" width="600"/>
</p>

---

## 🖥️ Main UI Dashboard

After successful login, users can create chat sessions, send queries, and view AI-generated responses dynamically within the chat interface.

<p align="center">
  <img src="assets/dashboard.png" width="850"/>
</p>

---

## 🧠 System Architecture (RAG + LLM)

The application follows a Retrieval-Augmented Generation (RAG) architecture that integrates a React-based frontend, FastAPI backend, vector retrieval system, and Large Language Model (LLM) to deliver context-aware responses in real time.

<p align="center">
  <img src="assets/architecture.png" width="900"/>
</p>

### 🔄 Architecture Flow

1. **User Interaction (Frontend - React.js)**

   * User creates a chat session
   * Submits a query through the UI

2. **API Layer (FastAPI Backend)**

   * Receives user query via REST API
   * Handles chat session management
   * Stores chat history in SQL database

3. **RAG Pipeline Execution**

   * Query is converted into embeddings
   * Relevant documents are retrieved from the vector store
   * Context is passed to the LLM

4. **LLM Response Generation**

   * LLM processes the query + retrieved context
   * Generates a contextual and accurate response

5. **Response Delivery**

   * Backend sends the generated response to frontend
   * UI updates the chat interface in real time

---

### 🧩 Core Components

* **Frontend:** React.js (Chat UI & User Interaction)
* **Backend:** FastAPI (API & Business Logic)
* **Database:** SQL (Chat sessions & history storage)
* **Vector Store:** Stores embeddings for semantic retrieval
* **LLM Engine:** Generates intelligent responses using retrieved context
* **RAG Framework:** Enhances accuracy with contextual document retrieval

---

## 🏗️ Project Structure

```
RAG-Multichat-App/
├── frontend/          # React.js Frontend (User Interface)
├── backend/           # FastAPI Backend + RAG Pipeline
├── assets/            # Screenshots, GIFs, Architecture Diagram
│   ├── demo.gif
│   ├── login.png
│   ├── ui.png
│   └── architecture.png
├── README.md
└── requirements.txt
```

---

## 🛠️ Tech Stack

### 🎨 Frontend

* React.js
* Tailwind
* JavaScript (ES6+)

### ⚙️ Backend

* Python
* FastAPI
* SQL Database
* Fast APIs

### 🧠 AI / RAG Stack

* Retrieval-Augmented Generation (RAG)
* Large Language Model (LLM)
* Vector Embeddings
* Semantic Search & Context Retrieval

---

## ⚙️ Backend Setup (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend will run on:

```
http://127.0.0.1:8000
```

---

## 💻 Frontend Setup (React)

```bash
cd frontend
npm install
npm start
```

Frontend will run on:

```
http://localhost:5173
```

---

## 🔄 Application Workflow

1. User logs into the application
2. Creates a new chat session
3. Submits a query/question
4. Backend processes the query using the RAG pipeline
5. Relevant context is retrieved from the vector store
6. LLM generates a contextual response
7. Response is returned and displayed in the chat UI in real time

---

## 📌 Use Cases

* AI Knowledge Assistant
* Enterprise Chatbot Systems
* Document Q&A Applications
* RAG-based Conversational AI Systems

---

## 👨‍💻 Author

**Shubham Bairagi**
AI/ML Engineer
https://github.com/Shubham1866
