#!/usr/bin/node

const process = require('process');

function add (a, b) {
  if (isFinite(a) && isFinite(b)) {
    console.log(parseInt(a) + parseInt(b));
  } else {
    console.log(NaN);
  }
}

add(process.argv[2], process.argv[3]);
