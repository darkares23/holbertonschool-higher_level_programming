#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }

  print () {
    let x = '';
    for (let i = 1; i <= this.height; i++) {
      for (let j = 1; j <= this.width; j++) {
        x += 'X';
      }
      if (i <= this.width) {
        x += '\n';
      }
    }
    console.log(x);
  }
}

module.exports = Rectangle;
