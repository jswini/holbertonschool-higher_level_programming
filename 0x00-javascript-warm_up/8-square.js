#!/usr/bin/node
/*
This script will print a square of  'X's based on arg passed
*/
if ((process.argv[2] == null) || (isNaN(process.argv[2]))) {
  console.log('Missing size');
} else {
  const square = process.argv[2];
  for (let lines = 0; lines < square; lines++) {
    console.log('X'.repeat(square));
  }
}
