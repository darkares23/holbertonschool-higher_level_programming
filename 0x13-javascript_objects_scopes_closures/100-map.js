#!/usr/bin/node

const list = require('./100-data').list;
const newList = list.map((val, indx) => { return val * indx; });

console.log(list);
console.log(newList);
