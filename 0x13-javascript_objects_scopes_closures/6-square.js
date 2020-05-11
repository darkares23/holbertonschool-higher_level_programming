#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    for (let i = 1; i <= this.height; i++) {
      console.log(c.repeat(parseInt(this.width)));
    }
  }
}
module.exports = Square;
