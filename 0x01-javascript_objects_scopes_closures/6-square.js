#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let lines = 0; lines < this.height; lines++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
