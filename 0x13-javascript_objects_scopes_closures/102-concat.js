#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
if (args.length === 5) {
  const readStream1 = fs.createReadStream(args[2]);
  const readStream2 = fs.createReadStream(args[3]);
  const writeStream = fs.createWriteStream(args[4]);
  readStream1.pipe(writeStream);
  readStream2.pipe(writeStream);
}
