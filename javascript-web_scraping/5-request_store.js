#!/usr/bin/node

const process = require('process');
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.stringify(body);
  let myString = data.toString();

  myString = myString.replace(/\\n/g, '\n');
  myString = myString.replace(/"/g, '');

  fs.writeFile(filePath, myString, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
