const express = require("express");

const cors = require("cors");
const dotenv = require("dotenv");
const connectDB = require("./config/db");
const chatRoutes = require("./routes/chat.routes");
const authRoutes = require("./routes/auth.routes");
const conversationRoutes = require("./routes/conversation.routes");

dotenv.config();
connectDB();

const app = express();

app.use(cors());
app.use(express.json());

app.use("/auth", authRoutes);
app.use("/chat", chatRoutes);
app.use("/conversations", conversationRoutes);


app.listen(process.env.PORT, () => {
  console.log(`PORT IS RUNNING AT ${process.env.PORT}`);
});
