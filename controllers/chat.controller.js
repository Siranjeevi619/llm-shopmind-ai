const callPythonAI = require("../services/pythonClient");
const CommonResponse = require("../utils/CommonResponse");
const ResponseStatus = require("../utils/ResponseStatus");

const chat = async (req, res) => {
  const { message } = req.body;
  const { role } = req.user;

  try {
    const aiRes = await callPythonAI({ role, message });

    return res
      .status(200)
      .json(
        new CommonResponse(
          "AI RESPONSE",
          { reply: aiRes.reply },
          ResponseStatus.ACCEPT
        )
      );
  } catch {
    return res
      .status(500)
      .json(
        new CommonResponse("", null, ResponseStatus.REJECT, "AI SERVICE ERROR")
      );
  }
};

module.exports = { chat };
