#!/usr/bin/node
const square5 = require('./5-square.js');

class Square extends square5 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let cont;
    for (cont = 0; cont < this.height; cont++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
