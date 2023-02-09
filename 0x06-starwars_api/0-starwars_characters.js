#!/usr/bin/node
const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (error, response, body) {
  const character = JSON.parse(body).characters;
  printNames(character, 0);
});
function printNames (character, index) {
  request(character[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
    }
    if (index + 1 < character.length) {
      printNames(character, index + 1);
    }
  }
  );
}
