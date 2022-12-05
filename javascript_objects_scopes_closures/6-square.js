#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  //  Square inherits from rectangle class.
  constructor (size) {
    super(size, size);
  }

  //  charPrint prints out square using char entered or X as default
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    this.print(c);
  }
}

module.exports = Square;
