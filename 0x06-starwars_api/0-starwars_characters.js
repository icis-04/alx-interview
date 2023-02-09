#!/usr/bin/node
const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (error, response, body) {
  const character = JSON.parse(body).characters;
	 for (let i = 0; i < character.length; i++) {
    request(character[i], function (error, response, body) {
      console.log(JSON.parse(body).name);
    }
    );
  }
});
