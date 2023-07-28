const fs = require('fs');
const path = require('path');
const { promisify } = require('util');

const readdir = promisify(fs.readdir);
const rename = promisify(fs.rename);

async function processDirectory(directory) {
  const files = await readdir(directory);

  for (const file of files) {
    const filePath = path.join(directory, file);
    const stats = fs.statSync(filePath);

    if (stats.isDirectory()) {
      await processDirectory(filePath); // Recursively process subdirectory
    } else if (stats.isFile()) {
      const ext = path.extname(filePath);

      if (ext === '.png' || ext === '.gif') {
        await processFile(filePath); // Process .png and .gif files
      }
    }
  }
}

async function processFile(filePath) {
  const lowercaseFilePath = filePath.toLowerCase();

  if (lowercaseFilePath !== filePath) {
    await rename(filePath, lowercaseFilePath);
    console.log(`Renamed file: ${filePath} -> ${lowercaseFilePath}`);
  }
}

// Provide the directory path where the image files are located
const directoryPath = './docs-mm-helpcenter/static/img/managing-my-tokens/custom-tokens/How-to-display-tokens-in-MetaMask/';

// Call the function to process files recursively in the specified directory
processDirectory(directoryPath)
  .then(() => {
    console.log('Image file renaming complete!');
  })
  .catch((error) => {
    console.error('An error occurred:', error);
  });
