#!/usr/bin/node

const process = require('process');

const checkArg = (num) => {
  const isNum = isFinite(num);

  if (isNum) {
    console.log(`My number: ${Math.floor(num)}`);
  } else {
    console.log('Not a number');
  }
};

checkArg(process.argv[2]);
