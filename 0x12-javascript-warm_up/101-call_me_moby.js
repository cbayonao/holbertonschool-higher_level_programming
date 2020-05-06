#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let myVar = 0; myVar < x; myVar++) {
    theFunction();
  }
};
