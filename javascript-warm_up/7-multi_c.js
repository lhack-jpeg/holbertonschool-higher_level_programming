#!/usr/bin/node

const process = require('process');

const printC = (printTimes) => {
  const isNum = isFinite(printTimes);
  if (isNum) {
    for (let i = 0; i < printTimes; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
};

printC(process.argv[2]);
