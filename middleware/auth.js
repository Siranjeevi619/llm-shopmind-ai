const jwt = require("jsonwebtoken");
const CommonResponse = require("../utils/CommonResponse");
const ResponseStatus = require("../utils/ResponseStatus");

const auth = (req, res, next) => {
  try {
    const authHeader = req.headers.authorization;
    if (!authHeader || !authHeader.startsWith("Bearer ")) {
      return res
        .status(403)
        .json(
          new CommonResponse("TOKEN NOT FOUND", null, ResponseStatus.REJECT)
        );
    }

    const token = authHeader.split(" ")[1];
    req.user = jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch (e) {
    return res
      .status(401)
      .json(new CommonResponse("INVALID TOKEN", null, ResponseStatus.REJECT));
  }
};

module.exports = auth;
