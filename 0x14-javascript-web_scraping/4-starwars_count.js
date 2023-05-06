#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) console.log(err);
  const data = JSON.parse(body);
  const results = data.results;
  let filtered = [];
  for (let i = 0; i < results.length; i++) {
    const chars = results[i].characters.filter((url) => {
      return url.includes('/18');
    });
    filtered.push(chars);
  }
  filtered = filtered.filter((a) => { return a.length !== 0; });
  console.log(filtered.length);
});
