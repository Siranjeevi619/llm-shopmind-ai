const mongoose = require("mongoose");
const userSchema = mongoose.Schema({
  email: String,
  passwordHash: String,
  role: {
    type: String,
    enum: ["USER", "ADMIN"],
  },
});

module.exports = userSchema;
