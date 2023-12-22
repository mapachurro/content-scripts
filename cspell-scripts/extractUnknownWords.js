const fs = require('fs');
const readline = require('readline');

async function extractUnknownWords() {
  const fileStream = fs.createReadStream('cspell-output.txt');

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  const unknownWords = new Set();

  for await (const line of rl) {
    const match = line.match(/Unknown word \((\w+)\)/);
    if (match) {
      unknownWords.add(match[1]);
    }
  }

  fs.writeFileSync('new-words.txt', Array.from(unknownWords).join('\n'));
}

extractUnknownWords();