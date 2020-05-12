#!/usr/bin/node

const args = process.argv;
const url = args[2];
const request = require('request');
request(url, function (error, response) {
  if (error) {
    return console.error(error);
  }
  console.log('code:', response && response.statusCode);
});const request = require('request');
const episode = process.argv[2];

request('http://swapi.co/api/films/' + episode, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
