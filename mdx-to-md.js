const fs = require('fs');
const path = require('path');

function renameMdxToMd(directory) {
  const files = fs.readdirSync(directory);

  files.forEach((file) => {
    const filePath = path.join(directory, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      renameMdxToMd(filePath);
    } else if (path.extname(file).toLowerCase() === '.mdx' && file !== 'index.mdx') {
      const newFilePath = path.join(directory, file.replace('.mdx', '.md'));
      fs.renameSync(filePath, newFilePath);
      console.log(`Renamed file: ${filePath} to ${newFilePath}`);
    }
  });
}

// Usage: node rename-files.js /path/to/directory
const directory = process.argv[2];

renameMdxToMd(directory);
