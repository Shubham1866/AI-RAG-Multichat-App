import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom';
import { runIngestionApi } from '../services/api';

function TopBar() {

  let navigate = useNavigate();

  let [name, setName] = useState("");

  const [loading, setLoading] = useState(false);

  const handleIngestion = async () => {
    try {
      setLoading(true);

      await runIngestionApi();

      alert("Ingestion completed successfully.");

    } catch (error) {
      console.error("Ingestion error:", error);
      alert("Ingestion failed.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(()=>{
    if(localStorage.getItem("name")){
      setName(localStorage.getItem("name"));
    }else{
      navigate("/")
    }
  }, []);

  function logout(){
    localStorage.clear();
    navigate("/");
  }

 return (
    <div className="h-14 flex items-center justify-between px-4 bg-gray-800 border-b border-gray-700">
      {/* Project Name */}
      <h1 className="text-white font-semibold text-lg">
        RAG Chat System
      </h1>

      {/* User Section */}
      <div className="flex items-center gap-4">
         <button
          onClick={() => navigate("/upload")}
          className="bg-blue-600 hover:bg-blue-700 text-white text-sm px-3 py-1 rounded"
        >
          Upload
        </button>
        {/* Ingestion Button */}
        <button
          onClick={handleIngestion}
          disabled={loading}
          className="bg-green-600 hover:bg-green-700 text-white text-sm px-3 py-1 rounded disabled:opacity-50"
        >
          {loading ? "Running..." : "Ingestion"}
        </button>
        <span className="text-gray-300 text-sm">
          { name }
        </span>
        <button onClick={()=>{ logout() }} className="bg-red-600 hover:bg-red-700 text-white text-sm px-3 py-1 rounded">
          Logout
        </button>
      </div>
    </div>
  );
}

export default TopBar