#!/usr/bin/node
const args = process.argv;
const a = parseInt(args[2], 10);
function factorial (a) {
  if (a > 1) {
    return (a * factorial(a - 1));
  }
  return (1);
}
console.log(factorial(a));
