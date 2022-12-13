#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = process.argv[2];

const users = new Object();

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const tasks = JSON.parse(body);
  tasks.forEach(element => {
    if (!users.hasOwnProperty(element.userId)){
      users[element.userId] = 0;
    }
  });
  tasks.forEach(element => {
    if (element.completed === true){
      users[element.userId]++
    }
  })
  for (const user in users) {
    if (users[user] === 0){
      delete users[user]
    }
  }
  console.log(users);
});
