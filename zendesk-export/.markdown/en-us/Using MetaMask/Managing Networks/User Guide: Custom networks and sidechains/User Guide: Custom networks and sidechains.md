
#### New to crypto and web3?


Head to [MetaMask Learn](https://learn.metamask.io/) for a straightforward learning experience designed specifically for newcomers to web3. It's completely free, available in multiple languages, and includes useful tools such as simulations to help you find your feet with MetaMask.



As the Ethereum ecosystem grows, a very popular option for building new technologies is to build a **custom network**, or a ***sidechain** —* in other words, another blockchain or network that is compatible with Ethereum — and then allow users to transfer tokens, or value of some kind, between the networks.


![Sidechain network diagram](https://support.metamask.io/hc/article_attachments/18553679937435)


There are many [prominent examples](https://support.metamask.io/hc/en-us/articles/4415750833691), and as Ethereum [scales](https://ethereum.org/en/developers/docs/scaling/), they will no doubt grow and evolve. MetaMask has been, and continues to be, a crucial linchpin allowing users to move more or less seamlessly between networks.


That said, **there are some significant, and common, pitfalls when dealing with sidechains** that you ***want to avoid*****.**This article is written to be a non-definitive guide to best practices when dealing with EVM-compatible chains. We can't hope to capture all the nuances of dealing with every instance of every sidechain; the following are general guidelines. **Troubleshooting tips are further down.**


 


Best practices
--------------


1. ### Do your due diligence


	* **Not all networks are safe.** In order to offer e.g. cheaper and faster transactions, custom networks usually have different security and reliability guarantees than mainnet. Try to understand the risks before moving significant value to a custom network.
	* **Make sure you trust the network provider.** A malicious network provider can lie about the state of the blockchain, withhold transactions, and record your network activity and IP address.
2. ### Ensure accurate and correct custom network information


	* **Find the network on <https://chainlist.wtf/> to add it to MetaMask automatically.**You can also add custom networks to MetaMask manually using a few other methods: see our instructions [here.](https://support.metamask.io/hc/en-us/articles/360043227612)
	* **Always verify custom network information.** When a website asks you to add a custom network, how do you know that you can trust the information? We have some recommendations in our [verification guide](https://support.metamask.io/hc/en-us/articles/360057142392).
3. ### Always use established bridges or portals to move tokens between networks


	* **MetaMask cannot track transactions between networks.** You are responsible for understanding how any cross-network transactions or deposits work. Make sure you trust the network operator and any Ethereum address you send funds to.
4. ### NEVER send tokens directly from one network to another


	* If you attempt to send cryptoassets directly from one network or chain to another, this will most likely result in **permanent and irreversible asset loss**
	* **Although a custom network may be Ethereum-compatible, they are not the same as the Ethereum Mainnet.** You may have the same Ethereum addresses on all networks, but your assets and transactions are specific to each network, unless the custom network provider allows you to move funds in to and out of it.
	* **This means you probably have to use a bridge to move assets from one chain or another**. Read more about [bridges](https://support.metamask.io/hc/en-us/articles/4836913606683) here.
5. ### Be aware of the limitations of technical support


MetaMask is a powerful tool that is open to the world to build upon. That means that many other networks and dapps have, and will, use MetaMask as the link between their dapp and you, the user. That does not mean that MetaMask offers technical support for all of those products and protocols. If you are interacting with a non-Consensys, non-MetaMask third party, seek technical assistance from them first unless you are sure that what you're experiencing is a problem with MetaMask.


Additionally, some popular decentralized exchanges and dapps are, as mentioned, *protocols* — that is, they are smart contracts, software programs that live on the Ethereum blockchain and do not have any centralized authority who *runs* them the way a traditional website or service is run. They are purely peer-to-peer interaction. **This means they may not offer technical support** beyond a users' forum, Slack, or Discord channel. Again, see point #1 above.
6. ### Understand how gas works on different networks


When using or interacting with a sidechain or non-Ethereum mainnet network, please keep in mind that **transaction fees are always paid in the native token currency of the network**, for example: 


	* You need BNB to pay gas fees on Binance
	* On Polygon you would use MATICMake sure you have enough native tokens if you planning to perform send or swap transactions.


 



FAQs
-----


### [Bridging assets to Arbitrum using MetaMask](https://consensys.net/blog/metamask/how-to-bridge-your-assets-to-arbitrum-using-metamask/)


### [How to use the Optimism Bridge](https://consensys.net/blog/metamask/how-to-bridge-tokens-from-ethereum-to-optimism-with-metamask/)


### [Sending assets to Binance (BNB Smart Chain)](https://support.metamask.io/hc/en-us/articles/360059408871)


### [How to send tokens from BSC to Ethereum or other chains](https://support.metamask.io/hc/en-us/articles/4404464724635)


### [Does MetaMask support Polkadot?](https://support.metamask.io/hc/en-us/articles/360060861011)


### [Tips for using MetaMask and Ronin wallets successfully](https://support.metamask.io/hc/en-us/articles/4403684463899-Tips-for-using-MetaMask-and-Ronin-wallets-successfully)


 


Troubleshooting
---------------




**I can't see my tokens on [name of network].**

* Are you connected to the correct network in MetaMask? If you don't see the one you need, add it using these [one of these methods](https://support.metamask.io/hc/en-us/articles/360043227612).
* Did you transfer the tokens correctly? (See points 2 & 3 above)
* Have you [added the token](https://support.metamask.io/hc/en-us/articles/360015489031) to MetaMask?





**How do I get ETH on mainnet?**

See [here](https://support.metamask.io/hc/en-us/articles/360058239311).





**How do I get [custom network token] on [mainnet or custom network]? How do I move them between chains?**

* This is a big topic, with lots of nuances. Certain sidechain tokens, such as MATIC (Polygon network), can be purchased on Ethereum mainnet through MetaMask Swaps.
* Keep in mind that regardless of where you buy a token, **you may still have to move the tokens through a bridge or portal to move them between mainnet and the sidechain.**





**I'm getting the "Internal JSON-RPC error". What do I do?**

See [here](https://support.metamask.io/hc/en-us/articles/360059289871).




