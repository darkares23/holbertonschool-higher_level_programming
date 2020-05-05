#!/usr/bin/node

const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  let sq = '';
  for (let i = 1; i <= x; i++) {
    let j;
    for (j = 1; j <= x; j++) {
      sq += 'X';
    }
    if (i < x) { sq += '\n'; }
  }
  console.log(sq);
}
