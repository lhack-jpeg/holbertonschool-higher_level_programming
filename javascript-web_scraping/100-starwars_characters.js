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
  characters.forEach(element => {
    request.get(element, (err, response, body) => {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
