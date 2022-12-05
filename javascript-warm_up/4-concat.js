#!/usr/bin/node

const process = require('process');

const concatSentence = (firstArg = 'undefined', secondArg = 'undefined') => {
  console.log(`${firstArg} is ${secondArg}`);
};

concatSentence(process.argv[2], process.argv[3]);
