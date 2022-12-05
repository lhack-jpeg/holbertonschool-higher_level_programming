#!/usr/bin/node

const process = require('process');
const argAmount = process.argv.length;

if (argAmount === 2) {
  console.log('No argument');
} else if (argAmount === 3) {
  console.log(process.argv[2]);
} else {
  //  pass
}
