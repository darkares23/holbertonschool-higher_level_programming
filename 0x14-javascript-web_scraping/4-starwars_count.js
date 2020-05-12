#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;

function countAppear (listFilms) {
  for (let i = 0; i < listFilms.length; i++) {
    for (let j = 0; j < listFilms[i].characters.length; j++) {
      if (listFilms[i].characters[j].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
}

request(url, (e, r, body) => {
  countAppear(JSON.parse(body).results);
});
