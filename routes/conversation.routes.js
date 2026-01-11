const express = require("express");
const auth = require("../middleware/auth");
const {
  getConversations,
  getMessages,
  createConversation,
} = require("../controllers/conversation.controller");

const router = express.Router();
router.post("/", auth, createConversation);
router.get("/", auth, getConversations);
router.get("/:id/messages", auth, getMessages);

module.exports = router;
