import { useState } from "react";
import { login } from "../services/auth";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      await login(email, password);
      navigate("/chat");
    } catch (e) {
      setError(e.message);
    }
  };

  return (
    <div className="h-screen flex items-center justify-center bg-[#343541]">
      <div className="bg-[#202123] p-6 rounded w-80">
        <h2 className="text-xl mb-4 text-white">Login</h2>

        {error && <p className="text-red-400 text-sm mb-2">{error}</p>}

        <input
          className="w-full mb-3 p-2 rounded bg-[#40414f] text-white"
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          className="w-full mb-4 p-2 rounded bg-[#40414f] text-white"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          onClick={handleLogin}
          className="w-full bg-emerald-500 text-black p-2 rounded"
        >
          Login
        </button>
      </div>
    </div>
  );
}
