#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    } else {
      c = 'C';
    }
    for (let i = 1; i <= this.size; i++) {
      console.log(c.repeat(parseInt(this.size)));
    }
  }
}
module.exports = Square;
