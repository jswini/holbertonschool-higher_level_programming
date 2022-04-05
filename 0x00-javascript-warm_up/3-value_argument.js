#!/usr/bin/node
/*
This script is designed to output the first argument from the command line passed to the script
*/
/*
 process.argv.forEach((val, index) => {
  console.log(`${index}: ${val}`);
});
The above code in this comment are from the node.js reference and included for future testing purposes
 */
if (process.argv[2] == null) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
