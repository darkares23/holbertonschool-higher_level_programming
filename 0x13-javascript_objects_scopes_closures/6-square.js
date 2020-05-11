#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    for (let i = 1; i <= this.height; i++) {
      console.log(c.repeat(parseInt(this.width)));
    }
  }
}
module.exports = Square;
