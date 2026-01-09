const ResponseStatus = require("./ResponseStatus");

class CommonResponse {
  constructor(
    message = "",
    data = null,
    status = ResponseStatus.ACCEPT,
    error = ""
  ) {
    this.data = data;
    this.message = message;
    this.status = status;
    this.timeStamp = new Date();
    this.error = error;
  }
}
module.exports = CommonResponse;
