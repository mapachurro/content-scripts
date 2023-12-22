const fs = require('fs');
const path = require('path');

// Get the files in the dictionaries directory
const files = fs.readdirSync('./dictionaries');

files.forEach((file) => {
  // Read the file
  const data = fs.readFileSync(path.join('./dictionaries', file), 'utf-8');

  // Split the file into lines
  const lines = data.split('\n');

  // Create an array to hold the updated lines
  const updatedLines = [];

  // Check each line
  lines.forEach((line) => {
    // Split the line into words
    const words = line.split(' ');

    // Add each word as a separate line
    words.forEach((word) => {
      updatedLines.push(word);
    });
  });

  // Write the updated lines back to the file
  fs.writeFileSync(path.join('./dictionaries', file), updatedLines.join('\n'));
});