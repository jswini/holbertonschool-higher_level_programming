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

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
    return (this.width, this.height);
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
