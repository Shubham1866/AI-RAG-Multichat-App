import { useState } from "react";
import { uploadDocumentApi } from "../services/chatApi";

function UploadDocument() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [responseData, setResponseData] = useState(null);

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file");
      return;
    }
      setLoading(true);

    try {

      const formData = new FormData();
      formData.append("file", file);
      await new Promise(resolve => setTimeout(resolve, 100));
      const response = await uploadDocumentApi(formData);
      console.log(response.data);
      
      setResponseData(response.data);

    } catch (error) {
      console.log(error);
      
      console.error("Upload error:", error);
      alert("Upload failed");
    } finally {
      setLoading(false);
    }

//     } catch (error) {
//       console.log("FULL ERROR:", error);
//       console.log("ERROR RESPONSE:", error?.response);
//       console.log("ERROR DATA:", error?.response?.data);
//       console.log("ERROR MESSAGE:", error?.message);
//       alert("Upload failed");
// }
  };

  return (
    <div className="min-h-screen bg-gray-900 flex items-center justify-center">

      <div className="w-full max-w-md bg-gray-800 p-8 rounded-xl shadow-lg text-white">

        <h2 className="text-2xl font-semibold mb-6 text-center">
          Upload Document
        </h2>

        {/* File Input */}
        <div className="mb-4">
          <label className="block text-sm text-gray-300 mb-2">
            Select PDF or Text File
          </label>

          <input
            type="file"
            accept=".pdf,.txt"
            onChange={(e) => setFile(e.target.files[0])}
            className="w-full text-sm text-gray-300"
          />
        </div>

        {/* Upload Button */}
        <button
          onClick={handleUpload}
          disabled={loading}
          className="w-full bg-blue-600 hover:bg-blue-700 py-2 rounded"
        >
          {loading ? "Uploading..." : "Upload"}
        </button>

        {/* Response Display */}
        {responseData && (
          <div className="mt-6 bg-gray-700 p-4 rounded text-sm space-y-1">
            <p><strong>ID:</strong> {responseData.id}</p>
            <p><strong>Filename:</strong> {responseData.filename}</p>
            <p><strong>File Type:</strong> {responseData.file_type}</p>
            <p><strong>Source:</strong> {responseData.source}</p>
            <p><strong>Total Chunks:</strong> {responseData.total_chunks}</p>
          </div>
        )}

      </div>

    </div>
  );
}

export default UploadDocument;
