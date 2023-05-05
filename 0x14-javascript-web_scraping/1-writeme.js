#!/usr/bin/node

const fs = require('fs');
const string = process.argv[3];
const file = process.argv[2];
fs.writeFile(file, string, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
