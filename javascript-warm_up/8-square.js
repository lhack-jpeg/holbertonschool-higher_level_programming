#!/usr/bin/node

const process = require('process');

const printC = (printTimes) => {
  const isNum = isFinite(printTimes);
  if (isNum) {
    for (let i = 0; i < printTimes; i++) {
      let stringSquare = '';
      for (let y = 0; y < printTimes; y++) {
        stringSquare += 'X';
      }
      console.log(stringSquare);
    }
  } else {
    console.log('Missing size');
  }
};

printC(process.argv[2]);
