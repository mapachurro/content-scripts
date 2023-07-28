const fs = require('fs');
const path = require('path');
const glob = require('glob');

function processFiles(directory) {
  const filePattern = path.join(directory, '**/*.@(md|mdx)');
  const files = glob.sync(filePattern, { nodir: true });

  files.forEach(file => {
    const content = fs.readFileSync(file, 'utf8');
    const updatedContent = updateFrontMatter(content);
    fs.writeFileSync(file, updatedContent, 'utf8');
  });
}

function updateFrontMatter(content) {
  const frontMatterRegex = /^---\s*\n([\s\S]*?)\n---\s*\n*/;
  const titleRegex = /^(title:\s*)(['"]?)(.*?)\2\s*$/gm;
  const interiorQuotesRegex = /"/g;

  const matches = content.match(frontMatterRegex);
  if (matches && matches.length >= 2) {
    const frontMatter = matches[1];
    const updatedFrontMatter = frontMatter.replace(titleRegex, (match, p1, p2, p3) => {
      const updatedTitleValue = p3.replace(interiorQuotesRegex, "'");
      return `${p1}"${updatedTitleValue}"`;
    });
    const updatedContent = content.replace(frontMatterRegex, `---\n${updatedFrontMatter}\n---\n`);
    return updatedContent;
  }

  return content;
}

// Usage: Specify the root directory to start the recursive search
const rootDirectory = './docs-mm-helpcenter/docs/';
processFiles(rootDirectory);
