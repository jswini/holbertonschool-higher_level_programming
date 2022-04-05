#!/usr/bin/node
/*
This script is designed to output the contents of a const
multiple times based on the argument passed to the console
*/
if ((process.argv[2] == null) || (isNaN(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= process.argv[2]; i++) {
    console.log('C is fun');
  }
}
