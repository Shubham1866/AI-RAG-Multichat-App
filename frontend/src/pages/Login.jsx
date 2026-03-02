import { useState } from "react";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import { loginApi } from "../services/authApi";

export default function Login() {

  const navigate = useNavigate();

   let [data, setData] = useState({
      email:"",
      password:""
    });
  
     let [error, setError] = useState({
      email:"",
      password:""
    });
      const [loading, setLoading] = useState(false);

       function handleChange(e){
    setData({...data,[e.target.id]:e.target.value});
  }

  async function handleSubmit(e){
      let isValid = true;
      let emailMessage = "", passwordMessage = "";
     if(data.email.trim() == ""){
        emailMessage = "Email is mandatory";
        isValid = false;
      }
      if(data.password.trim() == ""){
        passwordMessage  = "Password is mandatory";
        isValid = false;
      }
        setError({email:emailMessage, password:passwordMessage});
      try {
        if(isValid){
        //Call API
        setLoading(true);
        console.log(data);
        
         const response = await loginApi(data);
          console.log("Register success:", response.data);

          localStorage.setItem("token", response.data.access_token);
          localStorage.setItem("id", response.data.id);
          localStorage.setItem("name", response.data.name);
          navigate("/chat");
      }
      } catch (error) {
        // console.error("Register error:", error);
        // ✅ Handle 400 - Email already exists
      if (error.response && error.response.status === 400) {
        alert(error.response.data.detail);
      } 
      // Other errors
      else {
        console.log(error);
        
        alert("Login failed. Please try again.");
      }
      } finally {
        setLoading(false);
      }
    }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-900">
      <div className="w-full max-w-md bg-gray-800 p-8 rounded-xl shadow-lg">
        
        {/* Title */}
        <h2 className="text-2xl font-semibold text-white text-center mb-6">
          Login
        </h2>

        {/* Email */}
        <div className="mb-4">
          <label className="block text-sm text-gray-300 mb-1">
            Email <span style={{ color:'red' }}>{ error.email }</span>
          </label>
          <input
            type="email"
             value={data.email}
            id="email"
            onChange={(e)=>{ handleChange(e) }}
            placeholder="Enter your email"
            className="
              w-full
              bg-gray-700
              border border-gray-600
              rounded-md
              px-3 py-2
              text-white
              focus:outline-none
              focus:border-blue-500
            "
          />
        </div>

        {/* Password */}
        <div className="mb-6">
          <label className="block text-sm text-gray-300 mb-1">
            Password <span style={{ color:'red' }}>{ error.password }</span>
          </label>
          <input
            type="password"
            value={data.password}
            id="password"
            onChange={(e)=>{ handleChange(e) }}
            placeholder="Enter your password"
            className="
              w-full
              bg-gray-700
              border border-gray-600
              rounded-md
              px-3 py-2
              text-white
              focus:outline-none
              focus:border-blue-500
            "
          />
        </div>

        {/* Login Button */}
        <button
          className="
            w-full
            bg-blue-600
            hover:bg-blue-700
            text-white
            py-2
            rounded-md
            font-medium
          "
           onClick={(e)=>{ handleSubmit(e) }}
           disabled={loading}
        >
          Login
        </button>

        {/* Footer */}
        <p className="text-sm text-gray-400 mt-4 text-center">
          Don’t have an account?{" "}
          <Link to="/register" className="text-blue-400 cursor-pointer hover:underline">
            Register
          </Link>
        </p>

      </div>
    </div>
  );
}
