const fs = require('fs');
const path = require('path');

const directoryPath = './docs-mm-helpcenter/docs/'; // Replace with the directory path you want to search

function processFile(filePath) {
  const extension = path.extname(filePath);
  if (extension === '.md' || extension === '.mdx') {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        console.error(`Error reading file: ${filePath}`);
        return;
      }

      const regex = /<div style={{textAlign: 'center'}}>\n!\[.*?\]\((\/img.*?)\)\n<\/div>/gs;
      const modifiedData = data.replace(regex, (match, imagePath) => {
        const appendedPath = `@site/static${imagePath}`;
        return `<img src={require('${appendedPath}').default}></img>\n<br/>\n`;
      });

      fs.writeFile(filePath, modifiedData, 'utf8', (err) => {
        if (err) {
          console.error(`Error writing file: ${filePath}`);
          return;
        }
        console.log(`File modified: ${filePath}`);
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
