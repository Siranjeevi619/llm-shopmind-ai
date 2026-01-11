const mongoose = require("mongoose");
const schema = require("../schema/message");
module.exports = mongoose.model("MESSAGE", schema);
