#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, (err, response, body) => {
  if (err) console.log(err);
  const data = JSON.parse(body).characters;
  data.forEach((id) => {
    request(id, (err, response, body) => {
      if (err) console.log(err);
      const result = JSON.parse(body);
      console.log(result.name);
    });
  });
});
