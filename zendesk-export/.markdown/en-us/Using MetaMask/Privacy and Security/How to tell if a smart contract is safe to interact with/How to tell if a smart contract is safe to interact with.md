Smart contracts are the computer programs that run on the Ethereum Virtual Machine (EVM) and similar blockchains. Their name is somewhat misleading: when you interact with them, you're not signing up to a contract, but simply triggering a program to run. 


The [virtually endless possibilities](https://www.geeksforgeeks.org/what-is-meant-by-turing-complete-in-ethereum/) for smart contract functions are what makes Ethereum and web3 so powerful. Accessibility is also a key feature: since web3 is meant to be decentralized and usable by everyone, smart contracts can be created and deployed by anyone who wants to. Inevitably, some try and exploit this freedom to take advantage of other users. 


This is why you should learn how to identify fraudulent smart contracts and stop yourself falling victim to their scams. 


For clarity, smart contracts could represent:


* A token, such as ERC-20 tokens, which are defined and managed by smart contracts, or even an NFT collection
* A function within a dapp, such as a program which oversees a token swap, or even a DAO's governance mechanisms.


 


Connecting vs. approving
------------------------


When using MetaMask in the big wide world, you'll often be prompted to **connect** your wallet. You'll also reasonably often be asked to **approve** certain operations. In this context, it's approvals (also referred to as allowances) you need to focus on: the distinction is important!


* **Connecting your wallet** to a site doesn't allow it to do anything with your funds unless you specifically consent. So whilst this connection will enable a dapp to propose certain transactions or actions to you, nothing will happen to your funds unless you approve the suggested transactions. Read more on connecting your wallet [here](https://support.metamask.io/hc/en-us/articles/360059535551).
* **Approvals**, meanwhile, involve giving a smart contract the ability to interact with a certain token, in a certain quantity, as and when they require. You should always stop and think when being asking to approve something, as it generally involves handing over control of your assets to a computer program that could have been written by anyone. Read more [here](https://support.metamask.io/hc/en-us/articles/6174898326683).



Checking if a smart contract is trustworthy
-------------------------------------------


Let's go through some things to look for when evaluating whether you should trust a smart contract:


1. **Is it asking you to approve access to your tokens**?
	* Other than social engineering to get hold of your Secret Recovery Phrase ([learn how to stay safe](https://support.metamask.io/hc/en-us/articles/360060826432)), token approval scams are one of the most common attack vectors in web3. This is why we explained them in brief above. If you consent to a dapp's token approval, you're handing it control of whatever token (and *quantity*of that token) that you approve. **This alone should make you think twice**.
	* Does the token to which the dapp is requesting access make sense? Is it relevant to the dapp functionality you intended to use?
	* Does the quantity of token being requested make sense? Bear in mind that many popular apps request access to an essentially infinite amount of the token to prevent you having to sign (and pay for) numerous transactions in future. Read more under [here](https://support.metamask.io/hc/en-us/articles/6174898326683).
2. **Look up the address on the relevant block explorer**. All smart contracts have an address. Any reputable dapp, NFT collection, or other party should make this address readily available; either directly on their main site or in docs. MetaMask will also show you the smart contract's address before you sign any transaction.


Input the address into a [block explorer's](https://support.metamask.io/hc/en-us/articles/360057536611) search bar. Many of these, including Etherscan, will tell you if the code is verified or not, as highlighted below. You can also check to see if the contract has a name — if it doesn't it could be either very new or untrustworthy. 


![Smart contract verification Etherscan](https://support.metamask.io/hc/article_attachments/13306514521371)


You could also check the comments section on the block explorer for an indication of user sentiment. Though take this with a pinch of salt, as it could be influenced by fraudulent actors themselves.
3. **Use coin/token listing sites to investigate a token**. Go to [Coingecko](https://www.coingecko.com/), for example, and input the token's name or address. You should be able to see relevant details about the token, such as the project's website and their socials. Here you could check whether the dapp/token/project has a genuine, active community that isn't just full of bots, or look for a white paper on their website that demonstrates that it isn't just a [rugpull](https://support.metamask.io/hc/en-us/articles/4407169552667)-in-waiting. Our guide to [Token safety practices](https://support.metamask.io/hc/en-us/articles/4403988839451) is also very useful in this context.
4. **Check recent contract activity**. Look at the recent transactions listed on the smart contract's page on the block explorer. Whilst block explorers can be overwhelming, just try and focus on **spotting patterns**, and then asking why that pattern might exist. A common fraudulent practice, for example, is to prevent token buyers and holders from selling a token — so if you don't see any *sell*transactions, you may be looking at a honeypot scam, or similar.


Unfortunately, there is no way to be 100% sure of a smart contract's legitimacy, short of spending many hours familiarising yourself with Solidity and related coding languages so that you can audit them yourself. 


**So it bears repeating: always act with caution on web3**. If you're not sure about a specific site or have any further questions, get in touch with us via the 'Start a Conversation' button on the homepage of this site. 

