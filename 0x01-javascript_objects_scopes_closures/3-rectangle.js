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

  print () {
    for (let lines = 0; lines < this.height; lines++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
