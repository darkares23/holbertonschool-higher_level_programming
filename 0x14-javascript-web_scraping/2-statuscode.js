#!/usr/bin/node
const request = require('request');
const url = process.argv[1];

request
  .get(url)
  .on('response', function (err, res) {
    if (err) { console.log(err); }
    console.log('code: ', res && res.statusCode);
  });
