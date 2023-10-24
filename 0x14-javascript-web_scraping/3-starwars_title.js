#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiurl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(apiurl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
