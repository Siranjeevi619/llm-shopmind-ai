export async function sendMessage(message, conversationId = null) {
  const res = await fetch("http://localhost:3000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
    body: JSON.stringify({
      message,
      conversationId,
    }),
  });

  const data = await res.json();

  return data.data;
}

export async function fetchConversations() {
  const res = await fetch("http://localhost:3000/conversations", {
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
  });

  const data = await res.json();
  return data.data;
}

export async function fetchMessages(conversationId) {
  const res = await fetch(
    `http://localhost:3000/conversations/${conversationId}/messages`,
    {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    }
  );

  const data = await res.json();
  return data.data;
}

export async function createConversation(title) {
  const res = await fetch("http://localhost:3000/conversations", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
    body: JSON.stringify({ title }),
  });

  const data = await res.json();
  return data.data;
}
