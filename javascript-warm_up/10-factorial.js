#!/usr/bin/node

const process = require('process');

function recursion (number) {
  if (isFinite(number) && number > 0) {
    return number * recursion(number - 1);
  } else {
    return 1;
  }
}

console.log(recursion(process.argv[2]));
