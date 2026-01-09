const bcryptjs = require("bcryptjs");
const userModel = require("../model/User");
const CommonResponse = require("../utils/CommonResponse");
const ResponseStatus = require("../utils/ResponseStatus");
const jwt = require("jsonwebtoken");

const register = async (req, res) => {
  const { email, password, role } = req.body;

  const hash = await bcryptjs.hash(password, 10);
  await userModel.create({ email, passwordHash: hash, role });

  return res
    .status(201)
    .json(
      new CommonResponse(
        "USER CREATED SUCCESSFULLY",
        null,
        ResponseStatus.ACCEPT
      )
    );
};

const login = async (req, res) => {
  const { email, password } = req.body;

  try {
    const user = await userModel.findOne({ email });
    if (!user) {
      return res
        .status(404)
        .json(
          new CommonResponse("", null, ResponseStatus.REJECT, "USER NOT FOUND")
        );
    }

    const ok = await bcryptjs.compare(password, user.passwordHash);
    if (!ok) {
      return res
        .status(400)
        .json(
          new CommonResponse(
            "",
            null,
            ResponseStatus.REJECT,
            "INVALID PASSWORD"
          )
        );
    }

    const token = jwt.sign(
      {
        userId: user._id,
        role: user.role,
      },
      process.env.JWT_SECRET,
      { expiresIn: "1d" }
    );

    return res
      .status(200)
      .json(
        new CommonResponse(
          "USER LOGGED SUCCESSFULLY",
          { token, role: user.role },
          ResponseStatus.ACCEPT
        )
      );
  } catch (e) {
    return res
      .status(500)
      .json(
        new CommonResponse(
          "",
          null,
          ResponseStatus.REJECT,
          "INTERNAL SERVER ERROR"
        )
      );
  }
};

module.exports = { register, login };
