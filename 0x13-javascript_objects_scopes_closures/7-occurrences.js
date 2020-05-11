#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(function (indx) {
    if (indx === searchElement) { count++; }
  });
  return count;
};
