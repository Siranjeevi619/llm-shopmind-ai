import { useState } from "react";
import { login } from "../services/auth";
import { useNavigate, Link } from "react-router-dom";

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
    <div className="h-screen bg-[#343541] flex items-center justify-center">
      <div className="w-full max-w-sm bg-[#202123] p-8 rounded-xl text-white">
        <h1 className="text-2xl font-semibold text-center mb-6">ShopMind AI</h1>

        {error && <p className="text-red-400 text-sm mb-3">{error}</p>}

        <input
          placeholder="Email"
          className="w-full mb-3 px-4 py-3 rounded bg-[#40414f]"
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          className="w-full mb-4 px-4 py-3 rounded bg-[#40414f]"
          onChange={(e) => setPassword(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleLogin()}
        />

        <button
          onClick={handleLogin}
          className="w-full py-3 rounded bg-white text-black"
        >
          Continue
        </button>

        <p className="mt-6 text-center text-sm text-gray-400">
          New here?{" "}
          <Link to="/register" className="underline">
            Create account
          </Link>
        </p>
      </div>
    </div>
  );
}
