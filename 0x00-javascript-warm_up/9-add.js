#!/usr/bin/node
/*
This script will output the sum of 2 ints passed to it
*/

function add (a, b) {
  return (Number(a) + Number(b));
}

const num1 = process.argv[2];
const num2 = process.argv[3];
if ((num1 == null) || (isNaN(num1))) {
  console.log('NaN');
} else if ((num2 == null) || (isNaN(num2))) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
