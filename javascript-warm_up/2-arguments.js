#!/usr/bin/node

const { argv } = require('node:process');
const argAmount = argv.length

if (argAmount === 2) {
    console.log('No argument');
} else if (argAmount === 3) {
    console.log('Argument found');
} else {
  console.log('Arguments found');
}
