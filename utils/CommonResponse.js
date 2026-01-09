class CommonResponse {
  constructor(message, data, status) {
    this.data = data;
    this.message = message;
    this.status = status;
    this.timeStamp = new Date();
  }
}
module.exports = CommonResponse;
