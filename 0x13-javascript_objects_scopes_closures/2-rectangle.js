#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || Number.isInteger(w) === false || Number.isInteger(h) === false) {
      return {};
    }
    else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
