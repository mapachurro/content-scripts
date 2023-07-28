const fs = require('fs');
const path = require('path');
const extractor = require('markdown-link-extractor');

function updateLinksInMarkdownFiles(directoryA, directoryB) {
  const files = fs.readdirSync(directoryA);

  files.forEach((file) => {
    const filePath = path.join(directoryA, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      updateLinksInMarkdownFiles(filePath, directoryB);
    } else if (path.extname(file).toLowerCase() === '.md' || path.extname(file).toLowerCase() === '.mdx') {
      const content = fs.readFileSync(filePath, 'utf8');
      const links = extractor(content);

      let updatedContent = content;

      links.forEach((link) => {
        if (link.type === 'image') {
          const imagePath = link.href;
          const imageName = path.basename(imagePath);
          const updatedImagePath = findImageFile(imageName, directoryB);

          if (updatedImagePath) {
            updatedContent = updatedContent.replace(link.original, link.original.replace(imagePath, updatedImagePath));
          }
        }
      });

      if (content !== updatedContent) {
        fs.writeFileSync(filePath, updatedContent, 'utf8');
        console.log(`Updated links in file: ${filePath}`);
      }
    }
  });
}

function findImageFile(imageName, directoryB) {
  const files = fs.readdirSync(directoryB);

  for (const file of files) {
    if (file.toLowerCase() === imageName.toLowerCase()) {
      return path.relative(directoryB, path.join(directoryB, file));
    }
  }

  return null;
}

// Usage: node fix-docs-links.js /path/to/directoryA /path/to/directoryB
const directoryA = process.argv[2];
const directoryB = process.argv[3];

updateLinksInMarkdownFiles(directoryA, directoryB);
