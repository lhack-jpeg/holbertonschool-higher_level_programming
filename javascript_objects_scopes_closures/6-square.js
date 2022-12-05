#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  //  charPrint prints out square using char entered or X as default
  charPrint (c = undefined) {
    if (c === undefined) {
      super.print();
    } else {
      super.print(c);
    }
  }
}

module.exports = Square;
