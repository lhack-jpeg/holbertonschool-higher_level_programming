#!/usr/bin/node

const process = require('process');
const request = require('request');

const filmNumber = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${filmNumber}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const characters = JSON.parse(body).characters;
  printCharacter(characters, 0);
});

const printCharacter = (characters, index) => {
  request.get(characters[index], (err, response, body) => {
    if (err) {
      console.log(err);
    }
    console.log(JSON.parse(body).name);
    if (index + 1 < characters.length) {
      printCharacter(characters, index + 1);
    }
  });
};
