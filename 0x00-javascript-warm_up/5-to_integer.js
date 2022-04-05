#!/usr/bin/node
/*
This script is designed to output the first argument from the
command line passed to the script if it is an integer
*/
if ((process.argv[2] == null) || (isNaN(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log('%i', process.argv[2]);
}
