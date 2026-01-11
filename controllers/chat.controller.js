const Conversation = require("../model/ConversationModel");
const Message = require("../model/Message");
const callPythonAI = require("../services/api");
const CommonResponse = require("../utils/CommonResponse");
const ResponseStatus = require("../utils/ResponseStatus");

const chat = async (req, res) => {
  const { message, conversationId } = req.body;
  const { userId, role } = req.user;

  const aiRes = await callPythonAI({ role, message });

  let convo;
  if (conversationId) {
    convo = await Conversation.findOne({ _id: conversationId, userId });
  }

  if (!convo) {
    convo = await Conversation.create({ userId });
  }

  await Message.create([
    { conversationId: convo._id, role: "user", content: message },
    { conversationId: convo._id, role: "assistant", content: aiRes.reply },
  ]);

  convo.updatedAt = new Date();
  await convo.save();

  return res
    .status(200)
    .json(
      new CommonResponse(
        "AI RESPONSE",
        { reply: aiRes.reply, conversationId: convo._id },
        ResponseStatus.ACCEPT
      )
    );
};

module.exports = { chat };
