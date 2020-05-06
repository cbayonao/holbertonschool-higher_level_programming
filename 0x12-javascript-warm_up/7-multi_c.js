#!/usr/bin/node
const myVar = process.argv[2];
if (myVar === undefined || isNaN(myVar)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < myVar) {
    console.log('C is fun');
    i++;
  }
}
