*Depending on the method you use, finding a token contract address is one step in the process of adding a custom token to MetaMask. To find out more about adding tokens, head to our [article](https://support.metamask.io/hc/en-us/articles/360015489031) on the subject to see several different methods.*


**What is a token address?**
----------------------------


As you may be aware, tokens on Ethereum mainnet generally conform to the [ERC-20 standard](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/#top). This is a set of requirements for any *fungible*token on Ethereum — meaning one token has to have an identical value as other tokens of the same type, just like how one US dollar = one US dollar. The ERC-20 standard makes it considerably easier for wallets such as MetaMask, dapps, and other platforms to integrate existing and new tokens into their functions. For example, you can add any ERC-20 token to MetaMask. This wouldn't be possible if they didn't all adhere to the same standard.


Every ERC-20 token is created by inputting some details into a template smart contract which then controls and manages the token. In addition to basic functions such as the symbol and name, token creators must also determine total supply and methods for managing the balances of all token holders — one of its core responsibilites. 


When the originator first *deploys* the token's contract on the network, an address is generated that looks similar to the public addresses of Ethereum accounts. This is because the same [cryptographic method](https://en.wikipedia.org/wiki/Ethereum#:~:text=the%20blockchain.%5B66%5D-,Addresses,they%20are%20determined%20by%20sender%20and%20creation%20transaction%20nonce.%5B26%5D,-Virtual%20machine) is used in both situations (with slight nuances). 


Think of it this way: if you want to send or receive from your account, you'd use your public address. Similarly, if you want to send or receive a specific ERC-20 token, you have to do it by interacting with the token's address.



#### ERC-20 on other networks


Outside of Ethereum mainnet, ERC-20 tokens are handled differently depending on the network you're using, and it can quickly get confusing.


Some networks have their own, parallel token standards which essentially equate to ERC-20. BNB Chain/BSC and its [BEP-20](https://academy.binance.com/en/glossary/bep-20) standard is the most prominent example. The equivalence between the two standard means ERC-20 tokens on Ethereum and BEP-20 tokens on BNB Chain are interchangeable. If you transfer 10 ERC-20 tokens to a wallet on BNB Chain, you'll have 10 of the same token on BNB Chain, but in BEP-20 form and 'pegged' to the value of the ERC-20 original.


In other cases, such as Polygon, you can simply use the Polygon bridge (available [here](https://wallet.polygon.technology/) once you connect a wallet) to move tokens across, provided there are smart contracts deployed on both networks. 


**If you want to move ERC-20 tokens across different networks, always do your research to make sure you don't lose funds**, and consider using test transactions before sending large sums.



**Where do I find a token's contract address?**
-----------------------------------------------


There are three main ways to do this:




Block explorer Token listing site MetaMask Extension


Block explorers such as [Etherscan](https://etherscan.io/), [BscScan](https://bscscan.com/), or [Polygonscan](https://polygonscan.com/) hold data on ERC-20 tokens and their equivalents on their respective networks.


To find a token contract address, simply head to the block explorer and search for your desired token. The contract address will be clearly indicated on its page. See below for an example from Etherscan:


![Find contract address block explorer desktop](https://support.metamask.io/hc/article_attachments/10108723196443)


On a desktop browser, you will see the copy to clipboard icon appear when you mouse over. On mobile, it should already be visible (though please note the exact presentation of the contract address will vary depending on the block explorer you're using). 


![Find contract address block explorer desktop](https://support.metamask.io/hc/article_attachments/10108707416603)


Most block explorers have a similar format, and all provide information in the same categories -- just specific to their network.


They will also display the same information on a mobile browser as they do on desktop -- so this method applies equally to both MetaMask Extension and Mobile users.




Token listing sites such [Coingecko](https://www.coingecko.com) and CoinMarketCap hold a registry of all existing ERC-20 tokens. Both of these two main options offer the same functions detailed below.


As an example, we've taken the Uniswap (UNI) token page from Coingecko. From the token's page, its contract address is easy to find, although it differs slightly between MetaMask Extension and Mobile.


Extension
---------


**Find the 'Contract' category on the right**. By default this automatically displays the token's address on Ethereum mainnet, but you can access others by clicking the three dots.


![Find contract address coin listing site desktop](https://support.metamask.io/hc/article_attachments/10108529565083)


Click the copy button (the overlapping squares/sheets of paper) to copy the displayed address to your clipboard, ready to be pasted into MetaMask.


Mobile
------


Open the in-app browser by tapping the hamburger icon in the top left of the homepage, or just open your usual browser, such as Safari on iOS.


Once you're in the browser, find your way to Coingecko, or your preferred alternative. To do this in-app, use the search icon at the bottom of the screen. Search on Coingecko for the name or symbol of the token you're looking to add.


The token page should look like below, with the token address visible in its own category near the bottom:


![Find contract address coin listing site mobile](https://support.metamask.io/hc/article_attachments/10108545523355)


Like on the desktop browser, you can also click the three dots to see the address for different networks:


![Find contract address coin listing site mobile](https://support.metamask.io/hc/article_attachments/10108545532443)


Tap the copy icon next to an address to add it to your clipboard, ready to be added to MetaMask.




On the homepage of MetaMask Extension, under the 'Tokens' tab, click on the token whose contract information you want. Then, click on the vertical three dots menu and select 'View asset in explorer'. This action will take you to the token's contract address on the active network.


![Find contract address extension](https://support.metamask.io/hc/article_attachments/19701332777499)



 


Once you have the token contract address, you're ready to add the token to MetaMask. Head to our [article](https://support.metamask.io/hc/en-us/articles/360015489031) on this for more information. 


