#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  //  Square inherits from rectangle class.
  constructor (size) {
    super(size, size);
  }

  //  charPrint prints out square using char entered or X as default
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let sqrString = '';
      for (let y = 0; y < this.width; y++) {
        sqrString += c;
      }
      console.log(sqrString);
    }
  }
}

module.exports = Square;
