#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (w = this.width, h = this.height) {
    for (let i = 1; i <= h; i++) {
      console.log('X'.repeat(parseInt(this.width)));
    }
  }

  double () {
    this.width *= 2; 
    this.height *= 2;
  }

  rotate () {
    this.width = this.height;
    this.height = this.width;
  }
}

module.exports = Rectangle;
