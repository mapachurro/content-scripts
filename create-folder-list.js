const fs = require('fs');
const path = require('path');

const docsDir = path.join(__dirname, './docs-mm-helpcenter/docs/');
const outputFilePath = path.join(__dirname, 'directories-lists.md');

function getSubdirectoryList(dirPath) {
  const files = fs.readdirSync(dirPath);

  const subdirectoryList = files
    .filter((file) => fs.statSync(path.join(dirPath, file)).isDirectory())
    .map((subdirectory) => {
      const subdirectoryPath = path.join(path.relative(docsDir, dirPath), subdirectory);
      return `#### [${subdirectory}](${subdirectoryPath})`;
    });

  return subdirectoryList.join('\n');
}

function generateDirectoryLists(dirPath) {
  const directories = fs.readdirSync(dirPath);

  let directoryListsContent = '';

  directories.forEach((directory) => {
    const directoryPath = path.join(dirPath, directory);

    if (fs.statSync(directoryPath).isDirectory()) {
      const subdirectoryList = getSubdirectoryList(directoryPath);

      directoryListsContent += `## Subdirectories in ${directory}\n\n${subdirectoryList}\n\n`;

      directoryListsContent += generateDirectoryLists(directoryPath);
    }
  });

  return directoryListsContent;
}

function writeDirectoryLists() {
  const directoryListsContent = generateDirectoryLists(docsDir);

  fs.writeFileSync(outputFilePath, directoryListsContent, 'utf8');

  console.log(`Directory lists generated and saved to ${outputFilePath}`);
}

writeDirectoryLists();
