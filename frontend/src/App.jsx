import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Login from './pages/Login'
import Register from './pages/Register'
import ChatLayout from './layouts/ChatLayout'
import UploadDocument from "./pages/UploadDocument";
import { BrowserRouter, Route, Routes } from 'react-router-dom'

function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
         <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/chat" element={ <ChatLayout /> } />
          <Route path="/upload" element={<UploadDocument />} />
      </Routes> 
    </BrowserRouter>
  )
}

export default App
