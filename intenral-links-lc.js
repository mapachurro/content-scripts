const fs = require('fs');
const path = require('path');
const { promisify } = require('util');

const readdir = promisify(fs.readdir);
const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);

async function processDirectory(directory) {
  const files = await readdir(directory);

  for (const file of files) {
    const filePath = path.join(directory, file);
    const stats = fs.statSync(filePath);

    if (stats.isDirectory()) {
      await processDirectory(filePath); // Recursively process subdirectory
    } else if (stats.isFile()) {
      const ext = path.extname(filePath);

      if (ext === '.md' || ext === '.mdx') {
        await processFile(filePath); // Process .md and .mdx files
      }
    }
  }
}

async function processFile(filePath) {
  const content = await readFile(filePath, 'utf8');

  // Match and replace links in Markdown format
  const updatedContent = content.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (match, text, url) => {
    const lowercaseUrl = url.toLowerCase();
    return `[${text}](${lowercaseUrl})`;
  });

  await writeFile(filePath, updatedContent, 'utf8');
}

// Provide the directory path where the files are located
const directoryPath = './docs-mm-helpcenter/static/img/getting-started/';

// Call the function to process files recursively in the specified directory
processDirectory(directoryPath)
  .then(() => {
    console.log('Link conversion complete!');
  })
  .catch((error) => {
    console.error('An error occurred:', error);
  });
