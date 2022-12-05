#!/usr/bin/node

const process = require('process');

const myArray = [];

process.argv.forEach((element) => {
  if (isFinite(element)) {
    myArray.push(parseInt(element));
  }
});

myArray.sort(function (a, b) {
  return a - b;
});

if (myArray.length === 0 || myArray.length === 1) {
  console.log(0);
} else {
  console.log(myArray[myArray.length - 2]);
}
