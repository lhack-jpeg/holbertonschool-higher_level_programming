#!/usr/bin/node

import { argv } from 'node:process';

const argAmount = length(argv);

if (argAmount === 0) {
  console.log('No argument');
} else if (argAmount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
