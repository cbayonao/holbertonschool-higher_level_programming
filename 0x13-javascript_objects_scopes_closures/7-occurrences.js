#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let cont = 0;
  size = list.length;
  for (let i = 0; i < size; i++) {
    if (searchElement === list[i]) {
      cont++;
    }
  }
  return cont;
}
