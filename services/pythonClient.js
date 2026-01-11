const axios = require("axios");

module.exports = async (payload) => {
  const res = await axios.post(`${process.env.PYTHON_AI_URL}/ai/chat`, payload);
  return res.data;
};
