const fs = require('fs');
const path = require('path');
const matter = require('gray-matter');

function processFile(filePath) {
  const fileContent = fs.readFileSync(filePath, 'utf8');
  const { content, data, orig } = matter(fileContent);

  delete data.slug;

  const updatedFrontMatter = matter.stringify(content, data, { orig });

  fs.writeFileSync(filePath, updatedFrontMatter);
}

function processDirectory(dirPath) {
  const files = fs.readdirSync(dirPath);

  files.forEach((file) => {
    const filePath = path.join(dirPath, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      processDirectory(filePath);
    } else if (path.extname(filePath).toLowerCase() === '.md' || path.extname(filePath).toLowerCase() === '.mdx') {
      processFile(filePath);
    }
  });
}

// Specify the directory path to start the recursive iteration
const directoryPath = './docs-mm-helpcenter/docs/';

processDirectory(directoryPath);
