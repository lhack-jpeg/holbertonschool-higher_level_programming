#!/usr/bin/node
class Rectangle {
  //  Only initialises if params are met
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  //  Prints out the rectangle to the console
  print () {
    for (let i = 0; i < this.height; i++) {
      let rectString = '';
      for (let y = 0; y < this.width; y++) {
        rectString += 'X';
      }
      console.log(rectString);
    }
  }
}

module.exports = Rectangle;
