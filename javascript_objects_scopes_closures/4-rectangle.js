#!/usr/bin/node
class Rectangle {
  //  Only initialises if params are met
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  //  Doubles the width and height by 2
  double () {
    this.height *= 2;
    this.width *= 2;
  }

  //  Rotate swaps the height to the width and vice versa
  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  //  Prints out the rectangle to the console
  print (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let rectString = '';
      for (let y = 0; y < this.width; y++) {
        rectString += c;
      }
      console.log(rectString);
    }
  }
}

module.exports = Rectangle;
