#!/usr/bin/node
const Square0 = require('./5-square');

class Square extends Square0 {
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
