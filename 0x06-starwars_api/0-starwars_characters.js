#!/usr/bin/node

const request = require('request');

// Function to get movie characters by movie ID
function getMovieCharacters(movieId) {
    const baseUrl = `https://swapi.dev/api/films/${movieId}/`;

    // Fetch the movie data
    request(baseUrl, { json: true }, (err, res, movieData) => {
        if (err) {
            console.error(`Error fetching movie data for ID ${movieId}:`, err.message);
            return;
        }

        // Get the list of character URLs
        const characterUrls = movieData.characters;

        // Fetch and print each character's name
        characterUrls.forEach(characterUrl => {
            request(characterUrl, { json: true }, (err, res, characterData) => {
                if (err) {
                    console.error(`Error fetching character data from ${characterUrl}:`, err.message);
                    return;
                }
                console.log(characterData.name);
            });
        });
    });
}

// Get the movie ID from command-line arguments
const movieId = process.argv[2];

if (!movieId) {
    console.error("Usage: node script.js <movie_id>");
    process.exit(1);
}

// Fetch and print the characters for the given movie ID
getMovieCharacters(movieId);