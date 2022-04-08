#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const path = process.argv[2];
const newFile = process.argv[3];
request(path, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(newFile, body, 'utf-8', err => {
    if (err) {
      console.error(err);
    }
  });
});
