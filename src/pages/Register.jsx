import { useState } from "react";
import { register } from "../services/auth";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("USER");
  const navigate = useNavigate();

  const handleRegister = async () => {
    await register(email, password, role);
    navigate("/");
  };

  return (
    <div className="h-screen flex items-center justify-center bg-[#343541]">
      <div className="bg-[#202123] p-6 rounded w-80">
        <h2 className="text-xl mb-4 text-white">Register</h2>

        <input
          className="w-full mb-3 p-2 rounded bg-[#40414f] text-white"
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          className="w-full mb-3 p-2 rounded bg-[#40414f] text-white"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <select
          className="w-full mb-4 p-2 rounded bg-[#40414f] text-white"
          onChange={(e) => setRole(e.target.value)}
        >
          <option value="USER">User</option>
          <option value="ADMIN">Admin</option>
        </select>

        <button
          onClick={handleRegister}
          className="w-full bg-emerald-500 text-black p-2 rounded"
        >
          Register
        </button>
      </div>
    </div>
  );
}
