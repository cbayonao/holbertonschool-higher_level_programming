#!/usr/bin/node
exports.esrever = function (list) {
  const lirev = [];
  for (let i = list.length - 1; i >= 0; i--) {
    lirev.push(list[i]);
  }
  return lirev;
};
