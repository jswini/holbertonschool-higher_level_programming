#!/usr/bin/node
// this script reads an input and prints it to a file
const fs = require('fs');
const path = process.argv[2];
const info = process.argv[3];
if (path === undefined) {
  console.error('undefined');
} else {
  fs.writeFile(path, info, 'utf-8', err => {
    if (err) {
      console.error(err);
    }
  });
}
