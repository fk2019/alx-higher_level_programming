#!/usr/bin/node
const args = process.argv;
const str = 'C is fun';
const int = parseInt(args[2], 10);
if (int) {
  for (let i = 0; i < int; i++) {
    console.log(str);
  }
} else {
  console.log('Missing number of occurences');
}
