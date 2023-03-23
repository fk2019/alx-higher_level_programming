#!/usr/bin/node
const args = process.argv;

function secondBiggest (args) {
  if (args.length <= 3) {
    console.log(0);
  } else {
    const array = [];
    for (let i = 2; i < args.length; i++) {
      array.push(args[i]);
      array.sort();
    }
    console.log(array[array.length - 2]);
  }
}
secondBiggest(args);
