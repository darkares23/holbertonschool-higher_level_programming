#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const outputFile = process.argv[3];

function saveToFile (content, outputFile) {
  fs.writeFile(outputFile, content, 'utf8', (err) => {
    if (err) { console.log(err); }
  });
}

request
  .get(url, 'utf8', (err, res, body) => {
    if (err) { console.log(err); }
    saveToFile(body, outputFile);
  });
