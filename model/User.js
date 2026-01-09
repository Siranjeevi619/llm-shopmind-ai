const mongoose = require("mongoose");
const userSchema = require("../schema/User");

const userModel = mongoose.model("USER", userSchema);
