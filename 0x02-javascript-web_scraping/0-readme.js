#!/usr/bin/node
// this script reads a file and prints it to the console
const fs = require('fs');
const path = process.argv[2];
if (path === undefined) {
  console.error('undefined');
} else {
  fs.readFile(path, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}
