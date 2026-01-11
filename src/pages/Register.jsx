import { useState } from "react";
import { register } from "../services/auth";
import { useNavigate, Link } from "react-router-dom";

export default function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("USER");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleRegister = async () => {
    try {
      await register(email, password, role);
      navigate("/");
    } catch (e) {
      setError(e.message || "Registration failed");
    }
  };

  return (
    <div className="min-h-screen bg-[#343541] flex items-center justify-center text-white">
      <div className="w-full max-w-md px-8 py-10 bg-[#202123] rounded-xl shadow-lg">
        {/* Header */}
        <h1 className="text-2xl font-semibold text-center mb-2">
          Create account
        </h1>
        <p className="text-center text-gray-400 text-sm mb-6">ShopMind AI</p>

        {/* Error */}
        {error && (
          <div className="mb-4 text-sm text-red-400 bg-red-500/10 px-3 py-2 rounded">
            {error}
          </div>
        )}

        {/* Email */}
        <input
          type="email"
          placeholder="Email address"
          className="w-full mb-3 px-4 py-3 rounded bg-[#40414f] outline-none focus:ring-2 focus:ring-emerald-500"
          onChange={(e) => setEmail(e.target.value)}
        />

        {/* Password */}
        <input
          type="password"
          placeholder="Password"
          className="w-full mb-3 px-4 py-3 rounded bg-[#40414f] outline-none focus:ring-2 focus:ring-emerald-500"
          onChange={(e) => setPassword(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleRegister()}
        />

        {/* Role */}
        <select
          className="w-full mb-5 px-4 py-3 rounded bg-[#40414f] outline-none focus:ring-2 focus:ring-emerald-500"
          value={role}
          onChange={(e) => setRole(e.target.value)}
        >
          <option value="USER">User</option>
          <option value="ADMIN">Admin</option>
        </select>

        {/* Button */}
        <button
          onClick={handleRegister}
          className="w-full py-3 rounded bg-white text-black font-medium hover:bg-gray-200 transition"
        >
          Create account
        </button>

        {/* Footer/topic */}
        <p className="mt-6 text-center text-sm text-gray-400">
          Already have an account?{" "}
          <Link to="/" className="text-emerald-400 hover:underline">
            Sign in
          </Link>
        </p>
      </div>
    </div>
  );
}
