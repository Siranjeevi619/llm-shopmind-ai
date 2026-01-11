const callPythonAI = require("../services/pythonClient");
const CommonResponse = require("../utils/CommonResponse");
const ResponseStatus = require("../utils/ResponseStatus");
const Conversation = require("../model/ConversationModel");
const Message = require("../model/Message");

const chat = async (req, res) => {
  const { message, conversationId } = req.body;
  const { userId, role } = req.user;

  let convo;

  if (conversationId) {
    convo = await Conversation.findOne({ _id: conversationId, userId });
  }

  if (!convo) {
    convo = await Conversation.create({ userId });
  }

  const history = await Message.find({ conversationId: convo._id })
    .sort({ createdAt: 1 })
    .limit(10);

  const formattedHistory = history.map((m) => ({
    role: m.role,
    content: m.content,
  }));

  const aiRes = await callPythonAI({
    role,
    message,
    history: formattedHistory,
  });

  await Message.create({
    conversationId: convo._id,
    role: "user",
    content: message,
  });

  await Message.create({
    conversationId: convo._id,
    role: "assistant",
    content: aiRes.reply,
  });

  convo.updatedAt = new Date();
  await convo.save();

  return res.status(200).json(
    new CommonResponse(
      "AI RESPONSE",
      {
        reply: aiRes.reply,
        conversationId: convo._id,
      },
      ResponseStatus.ACCEPT
    )
  );
};

module.exports = { chat };
