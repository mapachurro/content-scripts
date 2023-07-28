const fs = require('fs');
const path = require('path');

const docsDir = path.join(__dirname, '/docs');
const outputFile = path.join(__dirname, 'link-output-file.md');

function getArticleList(dirPath) {
  const files = fs.readdirSync(dirPath);

  const articleList = files
    .filter((file) => (path.extname(file) === '.md' || path.extname(file) === '.mdx'))
    .map((file) => {
      const articlePath = path.join(path.relative(docsDir, dirPath), file);

      const articleContent = fs.readFileSync(path.join(dirPath, file), 'utf8');
      const articleTitleMatch = /title:\s*([^'\n]+)/.exec(articleContent);
      const articleTitle = articleTitleMatch ? articleTitleMatch[1].trim() : '';

      return articleTitle !== '' ? `#### [${articleTitle}](${articlePath})` : '';
    })
    .filter((article) => article !== '');

  return articleList.join('\n');
}

function processDirectories(dirPath) {
  const files = fs.readdirSync(dirPath);

  const linkList = [];

  files.forEach((file) => {
    const filePath = path.join(dirPath, file);

    if (fs.statSync(filePath).isDirectory()) {
      linkList.push(`## Articles in ${file}\n\n${getArticleList(filePath)}`);
      processDirectories(filePath);
    }
  });

  if (linkList.length > 0) {
    fs.appendFileSync(outputFile, linkList.join('\n\n'), 'utf8');
  }
}

fs.writeFileSync(outputFile, '', 'utf8');
processDirectories(docsDir);
