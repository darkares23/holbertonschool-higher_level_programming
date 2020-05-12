#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];

request('http://swapi.co/api/films/' + episode, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
