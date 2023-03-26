#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
if (args.length === 5) {
  fs.stat(args[2], (error, stats) => {
    if (error) {
      console.error(error);
    }
    if (stats.size === 0) {
      const readStream2 = fs.createReadStream(args[3]);
      const writeStream = fs.createWriteStream(args[4]);
      readStream2.pipe(writeStream);
    } else {
      const readStream1 = fs.createReadStream(args[2]);
      const readStream2 = fs.createReadStream(args[3]);
      const writeStream = fs.createWriteStream(args[4]);
      readStream1.pipe(writeStream);
      readStream2.pipe(writeStream);
    }
  });
}
