#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const apiUrl = {
  url: `https://swapi.dev/api/films/${filmId}/`,
  method: 'GET'
};


request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    printXterNames(characters, 0);
  } else {
    console.log('Failed to fetch movie data');
  }
});

function printXterNames (characters, index) {
  const characterUrl = characters[index];
  request(characterUrl, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);

      if (index + 1 < characters.length) {
        printXterNames(characters, index + 1);
      }
    } else {
      console.log('Failed to fetch character data');
    }
  });
}
