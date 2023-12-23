When adding MetaMask to your browser, you may see an alert indicating that MetaMask needs permission to **“read and change all your data on the websites you visit**”:


![MetaMask install edge notification](https://support.metamask.io/hc/article_attachments/13271397337627)


*This image was taken from a Microsoft Edge install process; your message may vary based on the browser and OS you're using.*


 


### Why does MetaMask need these permissions?


#### Background:


These permissions are about **Web browsers and what MetaMask needs to work with them**. The explanation is a little bit technical, but we'll try to keep it simple.


MetaMask is a tool that allows you to interact with blockchain networks, like Ethereum. Those interactions consist on a basic level of sending information to those networks, and getting responses back.


But Ethereum isn't just a traditional Web server somewhere, serving up Web pages in HTML. It's a decentralized network of computers that syncs information and keeps track of assets, and isn't really part of the traditional internet. It doesn't receive requests and send information the same way a server does that's hosting a website: and **MetaMask needs your permission to get that information, because in web3, *you are the one in control.***


#### How it Works


Let's say you're on a page that will allow you to mint an NFT. This is what happens, step by step:


* You connect MetaMask to the dapp.
	+ This lets the dapp know what your public address is, for example.
* You enter in pertinent information--say, certain features you want in the NFT, or how many you want.
* **The dapp itself takes the information you put in,** bundles it into a proposed transaction or signature request, and passes it off to MetaMask.
* **You execute that request in MetaMask**, and MetaMask submits it to the network.
	+ This sometimes requires several signatures--for example, authorizing the dapp to request that your tokens be spent, and then actually authorizing the mint.
* The network receives your request, and executes the mint.
* **The dapp is able to detect that transaction** through its own connection to the blockchain network, and displays to you the NFT that you've minted.



#### The bottom line


**At no point is MetaMask itself reading or changing the information on the webpage**. The dapp does all the work of updating information from the blockchain.


The reason MetaMask needs these broad permissions is, quite simply, browsers don't offer any other way to open up a channel of communication between MetaMask and the webpage.



#### Traditional Web browsers weren't made for blockchain data; that's why MetaMask was created, to build that functionality into your browser.


 


### How does this work on a technical level?


In order to enable dapps to access a blockchain network, MetaMask needs to inject a JavaScript object into each page. This allows the dapp to access the blockchain, and fetch publicly-available information specific to your wallet, such as the NFTs you hold, or your transaction history, or your token balances. For more information on how this works, [check out the MetaMask Docs](https://docs.metamask.io/guide/#new-dapp-developers). 


 


### Why should I believe you?


That's the spirit! **Web3 is all about being able to personally verify what others are telling you.**


If you are still not convinced, a good way to experiment and manage your browser is to sandbox your [MetaMask](https://support.metamask.io/hc/en-us/articles/360015289672-Sandboxing-MetaMask): create a [separate browser profile](https://support.metamask.io/hc/en-us/articles/12174759849371) so that MetaMask is only installed there. This will let you get used to MetaMask and Web3 in an environment that's separate from your existing web identity—and gives you greater peace of mind about what MetaMask has access to.


That said, **MetaMask is safe for browsing**; we are industry leaders in security and open-source development; for more information on audits that have been performed, see [our Security page here](https://metamask.io/security/).


###  Welcome — you're joining over 30 million MetaMask users all over the world!

