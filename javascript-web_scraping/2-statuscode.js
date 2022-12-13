#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = process.argv[2];

request.get(url).on('response', (response) => {
  console.log(`code: ${response.statusCode}`);
});
