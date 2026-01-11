const axios = require("axios");

const callPythonAI = async ({ role, message }) => {
  const res = await axios.post("http://localhost:8000/ai/chat", {
    role,
    message,
  });

  return res.data;
};


module.exports = callPythonAI;
