#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log('Failed to fetch movie data');
    return;
  }

  const movieData = JSON.parse(body);

  if (!movieData || !movieData.characters) {
    console.log('No characters found for this movie');
    return;
  }

  movieData.characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.log('Failed to fetch character data');
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
