#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body).results;
  let count = 0;
  data.forEach(element => {
    const characterArray = element.characters;
    characterArray.forEach(element => {
      if (element.includes('18')) {
        count++;
      }
    });
  });
  console.log(count);
});
