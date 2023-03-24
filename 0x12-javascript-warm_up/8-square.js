#!/usr/bin/node
const args = process.argv;
const int = parseInt(args[2], 10);
if (int) {
  for (let i = 0; i < int; i++) {
    let row = '';
    for (let j = 0; j < int; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
