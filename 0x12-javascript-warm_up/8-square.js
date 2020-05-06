#!/usr/bin/node
const myVar = process.argv[2];
if (myVar === undefined || isNaN(myVar)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < myVar) {
    console.log('X'.repeat(myVar));
    i++;
  }
}
