const fs = require('fs');

//This script takes the .json object for the Linea token list (https://raw.githubusercontent.com/Consensys/linea-token-list/main/json/linea-mainnet-token-fulllist.json) and formats it into a Markdown table, associating Ethereum addresses and Linea addresses with the appropriate columns.

// Read your json file
fs.readFile('tokens.json', 'utf8', function(err, data) {
  if (err) throw err;

  var jsonData = JSON.parse(data);
  var tokens = jsonData.tokens;

  var markdownTable = '| Token | Ethereum Address | Linea Address |\n| ----- | ---------------- | ------------- |\n';

  // Loop through each token in your json file
  for (let token of tokens) {
    var ethAddressLink, lineaAddressLink;

    // Check if token has extension property
    if (token.tokenType[0] === "canonical-bridge"){
         ethAddressLink = '[' + token.extension.rootAddress + '](' + token.extension.rootChainURI + token.extension.rootAddress + ')';
         lineaAddressLink = '[' + token.address + '](' + token.tokenId + ')';
    } else if(token.tokenType[0] === "native"){
         ethAddressLink = 'N/A';
         lineaAddressLink = '[' + token.address + '](' + token.tokenId + ')';
    }

    // Add each token data to your Markdown table
    var row = '| ' + token.name + ' | ';
    row += ethAddressLink + ' | ';
    row += lineaAddressLink + ' |\n';

    markdownTable += row;
  }

  // Write it to your markdown file in the current working directory
  fs.writeFile('table.md', markdownTable, function(err){
    if(err) throw err;
    console.log("File is created successfully.");
  });
});