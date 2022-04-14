#!/usr/bin/node
const request = require('request');
const path = process.argv[2];
const wedge = '/18/';
request(path, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movies = JSON.parse(body).results;
    let count = 0;
    for (const item in movies) {
      const characters = movies[item].characters;
      for (const charURL in characters) {
        if (characters[charURL].includes(wedge)) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
