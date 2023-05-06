#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) console.log(err);
  const data = JSON.parse(body);
  const users = data.filter((u) => { return u.completed === true; });
  const count = {};
  users.forEach((obj) => {
    if (obj.userId in count) {
      count[obj.userId]++;
    } else {
      count[obj.userId] = 1;
    }
  });
  console.log(count);
});
