#!/usr/bin/node
/*
This script will output the factorial of a number submitted
*/
function factorial (num) {
  if ((Number(num) === 0 || (Number(num) === 1))) {
    return 1;
  } else {
    return Number(num) * factorial(Number(num) - 1);
  }
}

const num1 = process.argv[2];
if (isNaN(num1) === true) {
  console.log('1');
} else {
  const fact = factorial(num1);
  console.log(fact);
}
