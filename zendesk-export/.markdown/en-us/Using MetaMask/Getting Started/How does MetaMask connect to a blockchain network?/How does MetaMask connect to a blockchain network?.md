The Internet was originally created as a tool to share information: to pull information out of one database, transfer it remotely, and make it appear on a computer somewhere else. But, in order to do that, you need to have some sort of program to represent that data in the same way, no matter what computer you’re on (and, ideally, make it a pleasant experience): and thus, browsers were born.


Public blockchains like Ethereum are the next evolution of Internet databases, and MetaMask is the next evolution of the browser. Your legacy browser doesn't have the ability to connect to this new kind of network, so MetaMask builds on top of them, pulling and pushing data to and from these public blockchain networks, with all of the interactivity we've come to expect from a Web experience built in. 


 


Choose your own network connection
----------------------------------


Just like pointing your browser to a URL, MetaMask needs to be pointed to what blockchain engineers call an [*RPC*](https://www.w3.org/History/1992/nfs_dxcern_mirror/rpc/doc/Introduction/WhatIs.html) [*endpoint*](https://www.cloudflare.com/learning/security/glossary/what-is-endpoint/). The data transfer standard for legacy Internet traffic is [HTTP](https://www.w3.org/Protocols/); in web3, most public blockchains use a standard called [JSON-RPC](https://www.jsonrpc.org/). This requesting and submitting of data is done through a set of commands that programmers call an [API](https://www.redhat.com/en/topics/api/what-are-application-programming-interfaces). If someone says 'the blockchain API' or 'the blockchain endpoint', they're referring to the same thing: *the place where you can send a request to the blockchain.*


 


![MetaMask connect to blockchain network diagram](https://support.metamask.io/hc/article_attachments/19247762425627)


 



#### JSON-RPC APIs


If you want to know more about how JSON-RPC APIs work with public blockchains, take a look at MetaMask’s [Developer Docs](https://docs.metamask.io/guide/ethereum-provider.html), and ethereum.org’s [documentation](https://ethereum.org/en/developers/docs/apis/json-rpc/).


 



How do you find an API endpoint?
--------------------------------


Well, you have to have a [node](https://support.metamask.io/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) of the blockchain available. Each node is constantly syncing the state of the blockchain, the history of transactions on the network. It's keeping the decentralized database up to date, and you can request—from that database—information it holds. What if you don't have the ability to run a blockchain node?


That's where Infura comes in. Infura provides an instantly available, always on, scalable blockchain API which gives you data access as if you were running your own node, and so much more. Infura offers access to these nodes through API endpoints, through which wallets and applications can send JSON-RPC requests. You could think of Infura, in this way, as a gateway to blockchain data.



#### Scalability and Privacy


Infura offers significant advantages over other blockchain API providers, especially in terms of scalability and insulation against usage spikes, but also meaningful privacy protections for users, which is why MetaMask connects to them by default.



MetaMask, though, has always been designed to be customizable. There are some blockchains that are so new, not widely adopted enough, or haven’t achieved the level of stability required for Infura to support them to their standards of service. Or perhaps you want to connect to a node you host yourself, or another local node of the blockchain. Maybe you’re building your own blockchain! **For this reason, users have always been able to point MetaMask to the RPC endpoint of their choice**. 



#### Run your own node


If you want to run your own Ethereum node, it’s easier than you might think; learn how to get it running with our Knowledge Base article [here](https://support.metamask.io/hc/en-us/articles/360060707952-How-to-run-your-own-Ethereum-node-and-use-it-with-MetaMask), and get it hooked up to MetaMask following instructions [here](https://support.metamask.io/hc/en-us/articles/360015290012-Using-a-Local-Node).



 


MetaMask’s relationship to Infura
---------------------------------


The [relationship between MetaMask and Infura](https://support.metamask.io/hc/en-us/articles/4417315392795) is a long one, and goes back to the beginnings of the ecosystem. Originally, both were projects under what is today known as Consensys Mesh, an incubator for technology built on Ethereum. The two projects were a natural fit, with MetaMask being the use case and Infura the service provider. That relationship continues now that both projects have been folded into the full stack of Web3 products offered by Consensys. 


MetaMask’s core vision is that of a permissionless, privacy-enabling product: rather than an Internet that commodifies you and your data, with your identity residing on someone else’s server, this is an Internet that enables you; you control your data and your identity.


Beyond Infura’s technical capabilities, allowing MetaMask to scale to the tens of millions of users it currently has, MetaMask chooses to ship with Infura as the default blockchain network connection provider because of their commitment to privacy and their work to progressively decentralize over time. 


A JSON-RPC API provider is just like any other server or API provider, in the sense that it takes requests from a computer and serves responses. Just like a traditional server, the technical capacity exists to track IP addresses, allowing for the compilation of behavioral patterns and surveillance techniques. Infura’s competitors have pursued the prominent funding model in Web2: not the provision of the service itself, but taking the user data you extract from that service, and selling the analytics of user behavior. Infura competitors have raised tremendous amounts of investment capital with the mandate that they will monetize the blockchain data itself. Infura, however, is not in the business of selling the analytics of user behavior. 



#### You Own Your Data


Infura shares MetaMask’s core belief that users own their usage data; Infura has not and will not productize and sell usage information to third parties.



 


The future of network connection providers
------------------------------------------


The vision of Web3 is one of liberation and decentralization. It’s possible that there will be tools developed that will take this ecosystem further along this path, breaking away from the model of service providers, toward a model of pure peer-to-peer interaction.


One way that Infura is embracing this future is through constantly expanding their offering of networks supported. Originally built for Ethereum alone, Infura now supports a number of sidechains, Layer 2 networks like Arbitrum, and even non-Ethereum Virtual Machine (EVM) compatible networks like Filecoin. 



#### NFTs Forever


Infura also offers a robust suite of tools surrounding IPFS, enabling the NFT ecosystem easy and reliable access to a persistent, decentralized metadata storage platform.



MetaMask, for their part, have built MetaMask Snaps, further enabling the customization and extensibility of Web3. Snaps allows developers to extend the functionality of MetaMask with custom features like custom blockchains, custom account types, custom messaging and notification protocols, and more, including novel technical solutions such as combining different cryptographic standards; in other words, allowing MetaMask to interact with non-EVM compatible networks. 


Despite the apparent difference, at first blush, between a user-friendly front-end browser experience and a developer-focused API provider, both Infura and MetaMask are united around a core vision of building the protocols and infrastructure of the future, where users always come first.

