const express = require("express");
const auth = require("../middleware/auth");
const {
  getConversations,
  getMessages,
} = require("../controllers/conversation.controller");

const router = express.Router();

router.get("/", auth, getConversations);
router.get("/:id/messages", auth, getMessages);

module.exports = router;
