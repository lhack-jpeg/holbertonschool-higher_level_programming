#!/usr/bin/node

const process = require('process');
let count = 0;

process.argv.forEach((val) => {
  count++;
});

if (count === 2) {
  console.log('No argument');
} else if (count === 3) {
  console.log(process.argv[2]);
} else {
  //  pass
}
