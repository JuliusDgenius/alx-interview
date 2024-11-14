#!/usr/bin/node
/* Write a script that prints all characters of a Star Wars movie:
  + The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
  + Display one character name per line in the same order as the “characters” list in the /films/ endpoint
  + You must use the [Star wars API]: https://swapi-api.alx-tools.com/
  + You must use the request module
**/

const request = require('request');
const filmId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(url, async (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    const uris = data.characters;

    for (const uri of uris) {
      await new Promise((resolve, reject) => {
        request(uri, (err, resp, body) => {
          if (err) {
            reject(err);
          } else {
            const charater = JSON.parse(body);
            console.log(charater.name);
            resolve();
          }
        });
      });
    }
  }
});
