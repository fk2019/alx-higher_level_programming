#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];
request(url, (err, response, body) => {
  if (err) console.log(err);
  fs.writeFile(file, body, 'utf8', (err, data) => {
    if (err) { console.log(err); }
  });
});
