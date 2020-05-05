#!/usr/bin/node
exports.callMeMoby = (x, theFunction) => {
  for (let times = 1; times <= x; times++) {
    theFunction();
  }
};
