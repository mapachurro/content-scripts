const fs = require('fs');
const path = require('path');

function updateLinks(directory) {
  const files = fs.readdirSync(directory);

  files.forEach((file) => {
    const filePath = path.join(directory, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      updateLinks(filePath);
    } else if (path.extname(file).toLowerCase() === '.md' || path.extname(file).toLowerCase() === '.mdx') {
      const content = fs.readFileSync(filePath, 'utf-8');
      const updatedContent = content.replace(/\(([^(]+)\.(md|mdx)\)/g, '($1/');

      if (content !== updatedContent) {
        fs.writeFileSync(filePath, updatedContent);
        console.log(`Updated links in file: ${filePath}`);
      }
    }
  });
}

// Usage: node update-links.js /path/to/directory
const directory = process.argv[2];

updateLinks(directory);
