const Conversation = require("../model/ConversationModel");
const Message = require("../model/Message");
const callPythonAI = require("../services/api");
const CommonResponse = require("../utils/CommonResponse");
const ResponseStatus = require("../utils/ResponseStatus");

const extractAIText = (aiRes) => {
  if (!aiRes || typeof aiRes !== "object") return "";

  if (aiRes.reply) return aiRes.reply;
  if (aiRes.result) return aiRes.result;
  if (aiRes.message) return aiRes.message;
  if (aiRes.summary) return aiRes.summary;

  
  return JSON.stringify(aiRes);
};

const chat = async (req, res) => {
  const { message, conversationId } = req.body;
  const { userId, role } = req.user;

  if (!message || !message.trim()) {
    return res
      .status(400)
      .json(new CommonResponse("EMPTY MESSAGE", null, ResponseStatus.REJECT));
  }

  const aiRes = await callPythonAI({ role, message });
  console.log("AI RESPONSE:", aiRes);

  const aiText = extractAIText(aiRes);

  if (!aiText) {
    return res
      .status(500)
      .json(
        new CommonResponse("AI RESPONSE INVALID", null, ResponseStatus.REJECT)
      );
  }

  let convo;
  if (conversationId) {
    convo = await Conversation.findOne({ _id: conversationId, userId });
  }

  if (!convo) {
    convo = await Conversation.create({ userId });
  }

  await Message.create([
    { conversationId: convo._id, role: "user", content: message },
    { conversationId: convo._id, role: "assistant", content: aiText },
  ]);

  convo.updatedAt = new Date();
  await convo.save();

  return res
    .status(200)
    .json(
      new CommonResponse(
        "AI RESPONSE",
        { reply: aiText, intent: aiRes.intent, conversationId: convo._id },
        ResponseStatus.ACCEPT
      )
    );
};

module.exports = { chat };
