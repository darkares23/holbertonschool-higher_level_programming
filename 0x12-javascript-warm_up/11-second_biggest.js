#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const args = process.argv.slice(2).sort().reverse();
  console.log(paserInt(args[1]));
}
