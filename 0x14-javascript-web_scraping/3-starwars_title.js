#!/usr/bin/node
const request = require('request');
const integer = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${integer}`;
request(url, (err, response, body) => {
  if (err) console.log(err);
  const data = JSON.parse(body);
  console.log(data.title);
});
