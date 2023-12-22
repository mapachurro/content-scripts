const fs = require('fs');
const path = require('path');

// List of locales
const locales = ['en', 'zh-cn', 'vi', 'tr', 'tl', 'th', 'ru', 'pt-br', 'pt', 'nl', 'ms', 'ko', 'ja', 'it-it', 'fr-fr', 'es', 'de'];

locales.forEach((locale) => {
  // Read the code.json file
  const data = fs.readFileSync(path.join('i18n', locale, 'code.json'));
  const json = JSON.parse(data);

  // Extract the "message" values
  const words = Object.values(json).map((item) => item.message);

  // Write the words into a dictionary file
  fs.writeFileSync(path.join('dictionaries', `${locale}-words.txt`), words.join('\n'));
});