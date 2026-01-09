const jwt = require("jwt");
const CommonResponse = require("../utils/CommonResponse");
const ResponseStatus = require("../utils/ResponseStatus");
const auth = (req, res, next) => {
  try {
    const token = req.headers.authorization;
    if (!token) {
      return res
        .status(403)
        .json(
          new CommonResponse("TOKEN NOT FOUND", null, ResponseStatus.REJECT)
        );
    }
    req.user = jwt.verify(token, process.env.jwt);
    next();
  } catch (error) {
    return res
      .status(401)
      .json(
        new CommonResponse(
          `INTERNAL SERVER ERROR : ${e.message}`,
          e,
          ResponseStatus.FAILED
        )
      );
  }
};
