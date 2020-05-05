#!/usr/bin/node

function fac (x) {
  if (isNaN(x) || x === undefined || x === 0) {
    return 1;
  } else {
    return x * (fac(x - 1));
  }
}
const x = parseInt(process.argv[2]);
console.log(fac(x));
