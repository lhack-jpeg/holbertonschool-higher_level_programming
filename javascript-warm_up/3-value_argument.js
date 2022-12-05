#!/usr/bin/node

const process = require('process');
let count = 0;

process.argv.forEach((val) => {
  count++;
});

if (count === 2) {
  console.log('No argument');
} else if (count > 3) {
  process.argv.forEach((val) => {
    console.log(val);
  });
} else {
  //  pass
}
