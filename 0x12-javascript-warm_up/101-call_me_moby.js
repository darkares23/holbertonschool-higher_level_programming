#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let times = 1; times <= x; times++) {
    theFunction();
  }
};
