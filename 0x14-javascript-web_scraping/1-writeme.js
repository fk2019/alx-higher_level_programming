#!/usr/bin/node

const fs = require('fs');
const string = process.argv[2];
const file = 'my_file.txt';
fs.writeFile(file, string, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
