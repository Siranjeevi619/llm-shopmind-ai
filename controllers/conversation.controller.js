const Conversation = require("../model/ConversationModel");
const Message = require("../model/Message");
const CommonResponse = require("../utils/CommonResponse");
const ResponseStatus = require("../utils/ResponseStatus");

const getConversations = async (req, res) => {
  const { userId } = req.user;
  const conversations = await Conversation.find({ userId }).sort({
    updatedAt: -1,
  });

  return res
    .status(200)
    .json(
      new CommonResponse("CONVERSATIONS", conversations, ResponseStatus.ACCEPT)
    );
};

const createConversation = async (req, res) => {
  const { userId } = req.user;
  const { title } = req.body;

  const convo = await Conversation.create({
    userId,
    title: title || "New conversation",
  });

  return res
    .status(201)
    .json(
      new CommonResponse("CONVERSATION CREATED", convo, ResponseStatus.ACCEPT)
    );
};

const getMessages = async (req, res) => {
  const { userId } = req.user;
  const { id } = req.params;

  const convo = await Conversation.findOne({ _id: id, userId });
  if (!convo) {
    return res
      .status(404)
      .json(new CommonResponse("NOT FOUND", null, ResponseStatus.REJECT));
  }

  const messages = await Message.find({ conversationId: id }).sort({
    createdAt: 1,
  });

  return res
    .status(200)
    .json(new CommonResponse("MESSAGES", messages, ResponseStatus.ACCEPT));
};

module.exports = { getConversations, getMessages, createConversation };
