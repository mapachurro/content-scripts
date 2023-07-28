const fs = require('fs');
const path = require('path');

function replaceTitleDashes(directory) {
  const files = fs.readdirSync(directory);

  files.forEach((file) => {
    const filePath = path.join(directory, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      replaceTitleDashes(filePath);
    } else if (path.extname(file).toLowerCase() === '.md' || path.extname(file).toLowerCase() === '.mdx') {
      const content = fs.readFileSync(filePath, 'utf-8');
      const updatedContent = content.replace(/(title:\s)".*?"/g, (match) => match.replace(/-/g, ' '));

      if (content !== updatedContent) {
        fs.writeFileSync(filePath, updatedContent);
        console.log(`Replaced dashes with spaces in file: ${filePath}`);
      }
    }
  });
}

// Usage: node script.js /path/to/directory
const directory = process.argv[2] || './image-import/';
replaceTitleDashes(directory);
