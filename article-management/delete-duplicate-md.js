// It would appear taht this deletes duplicate md/mdx files.

const fs = require('fs');
const path = require('path');

const directoryPath = './docs-mm-helpcenter/docs/'; // Replace with the directory path you want to search

function traverseDirectory(directoryPath) {
  fs.readdir(directoryPath, (err, files) => {
    if (err) {
      console.error(`Error reading directory: ${directoryPath}`);
      return;
    }

    const mdFiles = [];
    const mdxFiles = [];

    files.forEach((file) => {
      const filePath = path.join(directoryPath, file);

      fs.stat(filePath, (err, stats) => {
        if (err) {
          console.error(`Error retrieving file stats: ${filePath}`);
          return;
        }

        if (stats.isDirectory()) {
          traverseDirectory(filePath);
        } else {
          const extension = path.extname(filePath);
          if (extension === '.md') {
            mdFiles.push(filePath);
          } else if (extension === '.mdx') {
            mdxFiles.push(filePath);
          }
        }

        if (mdFiles.length > 0 && mdxFiles.length > 0) {
          mdFiles.forEach((mdFile) => {
            const mdxFileName = path.basename(mdFile, '.md') + '.mdx';

            if (mdxFiles.includes(path.join(directoryPath, mdxFileName))) {
              fs.unlink(mdFile, (err) => {
                if (err) {
                  console.error(`Error deleting file: ${mdFile}`);
                  return;
                }
                console.log(`File deleted: ${mdFile}`);
              });
            }
          });
        }
      });
    });
  });
}

traverseDirectory(directoryPath);
