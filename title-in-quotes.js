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
  const titleRegex = /^(title:\s*)(['"]?)(.*?)\2\s*$/m;

  const matches = content.match(frontMatterRegex);
  if (matches && matches.length >= 2) {
    const frontMatter = matches[1];
    const updatedFrontMatter = frontMatter.replace(titleRegex, '$1"$3"');
    const updatedContent = content.replace(frontMatterRegex, `---\n${updatedFrontMatter}\n---\n`);
    return updatedContent;
  }

  return content;
}

// Usage: Specify the root directory to start the recursive search
// make sure you install npm glob
const rootDirectory = './docs-mm-helpcenter/docs/';
processFiles(rootDirectory);
