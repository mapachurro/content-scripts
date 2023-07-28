const fs = require('fs');
const path = require('path');

const directoryPath = '<YOUR_DIRECTORY_PATH>'; // Replace with the directory path you want to search

function processFile(filePath) {
  const extension = path.extname(filePath);
  if (extension === '.md') {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        console.error(`Error reading file: ${filePath}`);
        return;
      }

      const modifiedData = data.replace(/!\[(.*?)\]\((.*?)\)/g, '<div style={{textAlign: \'center\'}}>\n$&\n</div>');

      const modifiedFilePath = filePath.replace('.md', '.mdx');
      fs.writeFile(modifiedFilePath, modifiedData, 'utf8', (err) => {
        if (err) {
          console.error(`Error writing file: ${modifiedFilePath}`);
          return;
        }
        console.log(`File modified: ${modifiedFilePath}`);

        fs.unlink(filePath, (err) => {
          if (err) {
            console.error(`Error deleting file: ${filePath}`);
            return;
          }
          console.log(`File deleted: ${filePath}`);
        });
      });
    });
  }
}

function traverseDirectory(directoryPath) {
  fs.readdir(directoryPath, (err, files) => {
    if (err) {
      console.error(`Error reading directory: ${directoryPath}`);
      return;
    }

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
          processFile(filePath);
        }
      });
    });
  });
}

traverseDirectory(directoryPath);
