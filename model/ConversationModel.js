const mongoose = require("mongoose");
const schema = require("../schema/conversation");
module.exports = mongoose.model("CONVERSATION", schema);
