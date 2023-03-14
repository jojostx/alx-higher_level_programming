#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let h = this.height;
    const w = this.width;

    for (; h > 0; h--) {
      console.log('X'.repeat(w));
    }
  }
}

module.exports = Rectangle;
