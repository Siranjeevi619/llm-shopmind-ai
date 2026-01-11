const mongoose = require("mongoose");
const conversationSchema = require("../schema/conversation");

module.exports = mongoose.model("CONVERSATION", conversationSchema);
