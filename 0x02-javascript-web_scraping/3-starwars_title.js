#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const path = 'http://swapi-api.hbtn.io/api/films/' + id;
request(path, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(JSON.parse(body).title);
});
