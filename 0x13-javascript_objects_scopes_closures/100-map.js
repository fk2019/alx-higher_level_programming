#!/usr/bin/node
const list = require('./100-data').list;
const map = function () {
  console.log(list);
  console.log(list.map((index, x) => index * x));
};
map();
