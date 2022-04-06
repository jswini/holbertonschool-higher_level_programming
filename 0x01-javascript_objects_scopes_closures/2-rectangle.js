#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w <= 0) || (isNaN(w))) {
      // skipped
    } else if ((h <= 0) || (isNaN(h))) {
      // skipped
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
