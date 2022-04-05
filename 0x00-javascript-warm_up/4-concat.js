#!/usr/bin/node
/*
This script is designed to output the first argument from the command line passed to the script
*/
if (process.argv[2] == null) {
  console.log('undefined is undefined');
} else if (process.argv[3] == null) {
  console.log('%s is undefined', process.argv[2]);
} else {
  console.log('%s is %s', process.argv[2], process.argv[3]);
}
