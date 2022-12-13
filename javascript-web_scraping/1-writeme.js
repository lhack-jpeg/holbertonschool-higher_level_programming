#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const fileName = process.argv[2];
const dataToWrite = process.argv[3];

fs.writeFile(fileName, dataToWrite, { encoding: 'utf-8' }, (err) => {
  if (err) {
    console.log(err);
  }
});
