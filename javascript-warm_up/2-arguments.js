#!/usr/bin/node

const { argv } = require('node:process');

const argAmount = argv.length;

if (argAmount === 0) {
  console.log('No argument');
} else if (argAmount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
