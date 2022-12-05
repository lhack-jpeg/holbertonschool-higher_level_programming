#!/usr/bin/node

const process = require('process');
const argAmount = process.argv.length;

if (argAmount === 2) {
  console.log('No argument');
} else if (argAmount === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
