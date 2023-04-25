#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url + process.argv[2], function (error, response, body) {
  if (error == null && body) {
    const info = JSON.parse(body);
    console.log(info.title);
  }
});
