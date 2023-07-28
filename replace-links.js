const fs = require('fs');
const path = require('path');

function updateInternalLinks(directory) {
  const files = fs.readdirSync(directory);

  files.forEach((file) => {
    const filePath = path.join(directory, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      updateInternalLinks(filePath);
    } else if (path.extname(file).toLowerCase() === '.md' || path.extname(file).toLowerCase() === '.mdx') {
      const content = fs.readFileSync(filePath, 'utf8');
      const updatedContent = content.replace(/\((\.\S+?\.mdx?)\)/g, (match, link) => {
        const updatedLink = path.relative(path.dirname(filePath), path.join(directory, link.replace('.mdx', '.md'))).replace(/\\/g, '/');
        return `(${updatedLink.startsWith('./') ? updatedLink : './' + updatedLink})`;
      });

      if (content !== updatedContent) {
        fs.writeFileSync(filePath, updatedContent, 'utf8');
        console.log(`Updated links in file: ${filePath}`);
      }
    }
  });
}

// Usage: node update-links.js /path/to/directory
const directory = process.argv[2];

updateInternalLinks(directory);
