#!/usr/bin/node

const dict = require('101').dict;
const dic = {};

ocur = function (list, searchElement) {
	let count = 0;
	list.forEach(function (indx) {
	  if (indx === searchElement) { count++; }
	});
	return count;
};