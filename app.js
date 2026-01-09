const express = require("express");

const cors = require("cors");
const dotenv = require("dotenv");
const connectDB = require("./config/db");
connectDB();

const app = express();

app.use(cors());
app.use(express.json());

app.use("/auth");
app.use("/chat");
app.listen(process.env.PORT, () => {
  console.log(`PORT IS RUNNING AT ${process.env.PORT}`);
});
