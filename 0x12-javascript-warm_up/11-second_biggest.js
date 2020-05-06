#!/usr/bin/node
let myVar = process.argv.slice(2);
const myVar2 = process.argv.length;

if (myVar2 <= 3) {
  console.log('0');
} else {
  myVar = myVar.map(Number);
  const second = myVar.sort(
    function (a, b) {
      return b - a;
    })[1];
  console.log(second);
}
