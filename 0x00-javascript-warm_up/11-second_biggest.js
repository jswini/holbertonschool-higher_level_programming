#!/usr/bin/node
/*
This script will output the second highest number in a list of args
*/
function secondLargest (arr) {
  let largest = -Infinity;
  let compare = -Infinity;
  for (const value of arr) {
    const second = Number(value);
    if (second > largest) {
      [compare, largest] = [largest, second];
    } else if (second < largest && second > compare) {
      compare = second;
    }
  }
  return compare;
}

const array = process.argv;
if ((process.argv[2] == null) || (process.argv[3] == null)) {
  console.log('0');
} else if (array.length > 3) {
  console.log(secondLargest(array));
}
