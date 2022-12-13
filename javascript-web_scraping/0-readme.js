#!/usr/bin/node

const process = require('process');
const fs = require('fs')

const url = process.argv[2]

fs.readFile(url, 'utf-8', function (err, data){
    if (err){
        console.log(err)
    }
    console.log(data);
})