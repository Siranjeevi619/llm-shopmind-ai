export async function login(email, password) {
  const res = await fetch("http://localhost:3000/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });

  const data = await res.json();

  if (data.status !== "ACCEPT") {
    throw new Error(data.error || "Login failed");
  }

  localStorage.setItem("token", data.data.token);
  localStorage.setItem("role", data.data.role);
}

export async function register(email, password, role) {
  const res = await fetch("http://localhost:3000/auth/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password, role }),
  });

  const data = await res.json();

  if (data.status !== "ACCEPT") {
    throw new Error(data.error || "Register failed");
  }
}

/* ✅ ADD THIS */
export function logout() {
  localStorage.removeItem("token");
  localStorage.removeItem("role");
}
