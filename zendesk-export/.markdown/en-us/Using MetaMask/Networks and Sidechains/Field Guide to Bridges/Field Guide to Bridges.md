
### Potential Loss of Assets


Transferring assets between blockchains is not necessarily a simple task. Some tokens cannot be sent from one network to another — and if you do, **you can lose them forever**.



![sendtokens.jpg](https://support.metamask.io/hc/article_attachments/16533766254875)


What is a bridge?
-----------------


A bridge is an app that allows you to transfer assets (cryptocurrencies, NFTs, or other tokens) between one blockchain and another. For example, transferring from BSC (now BNB Chain) to Ethereum.


![BNB ETH bridge diagram](https://support.metamask.io/hc/article_attachments/16533744376603)


Why do I need to use a bridge?
------------------------------


* Many users use the same address on multiple blockchains, for example by [adding a blockchain connection](https://support.metamask.io/hc/en-us/articles/360043227612) in MetaMask. What if they've got an NFT on Gnosis Chain, but they want to have it on Polygon?
* Conversely, you might have a different address, say on BSC, than what you use on Ethereum. You may think that you can just send tokens from your BSC address directly to your Ethereum address; after all, they're both EVM-compatible, right?


*Wrong.* **The BSC blockchain and Ethereum blockchains are separate networks, with no built-in knowledge of each other.** 


If you send to your Ethereum address from BSC, BSC will send to the address you put in, but *on the BSC network.* For more information on this specific scenario, [see here](https://academy.binance.com/en/articles/how-to-recover-crypto-transferred-to-the-wrong-network-on-binance).


What bridge should I use?
-------------------------



#### MetaMask Bridge


You can now access a curated, straightforward bridging experience in MetaMask Bridge, available at [portfolio.metamask.io](https://portfolio.metamask.io/), or by clicking the 'Bridge' button in MetaMask Extension. Only certain tokens and network combinations are available initially.



You should choose a bridge primarily based on what you're trying to move, where. For example, some bridges only move ERC-20 (currency) tokens; others specifically handle ERC-721 and 1155 (NFTs). The last thing you want to do is try to transfer tokens to a different network, and never receive them.


### There is no definitive listing of bridges.


This is Web3, which is based around permissionless, open development; this means that at any given time, there might be a new bridge between networks. There are also **bridge aggregators**, which are platforms that allow you to use several bridges in conjunction, conveniently transferring assets across platforms.



#### Network Profiles


For detailed information regarding a specific network, see our [Network Profiles](https://support.metamask.io/hc/en-us/sections/4442278744475-Network-Profiles), which include bridge information for each network.



*The following is a non-exhaustive list of bridges and aggregators, in no particular order. MetaMask does not recommend or endorse any of these products; we are providing this information as a starting point for you to do your own research and understand how each bridge works before using it.*


### Bridges




|  |  |  |  |
| --- | --- | --- | --- |
| [Celer Bridge](https://cbridge.celer.network/#/transfer) | [Wormhole's Portal Bridge](https://portalbridge.com/#/transfer) | [Rainbow Bridge](https://rainbowbridge.app/transfer) | [Terra Bridge](https://bridge.terra.money/) |
| [Allbridge](https://allbridge.io/) | [EvoDeFi Bridge](https://bridge.evodefi.com/) | [PolyBridge](https://bridge.poly.network/) |


 


### Bridge Aggregators




|  |  |  |
| --- | --- | --- |
| [Rango Exchange](https://rango.exchange/) | [Li.Fi Bridge Aggregator](https://links.li.finance/) | [movr.network](https://www.movr.network/) |
| [chainswap](https://chainswap.com/) | [Router Protocol](https://www.routerprotocol.com/) |  |


 


How does a bridge work?
-----------------------


There are a number of different mechanisms that bridges use to move assets between networks; often, they are centralized entities that operate almost like an exchange. Others are more decentralized. If you're interested in the nuts and bolts, start with ethereum.org's [documentation here](https://ethereum.org/en/bridges/).


I need step-by-step instructions on how to use a bridge
-------------------------------------------------------


Given the above-mentioned wide variety in bridge platforms, networks, and functionality, we can't provide a step-by-step that will work for *every* bridge. In general, though, this is how it works:


* Navigate to the bridge that you have identified will work for your particular combination of networks and token types
* Log in to the app with your MetaMask wallet
* Choose the network you're going *from* and *to*
* Choose the asset you want to transfer
	+ During these steps, you may need to sign approvals in your MetaMask Wallet. *Make sure you read every transaction or approval you make carefully.*For more on approvals, [see here](https://consensys.net/blog/metamask/the-seal-of-approval-know-what-youre-consenting-to-with-permissions-and-approvals-in-metamask/) or [here](https://support.metamask.io/hc/en-us/articles/6174898326683).
* Initiate the bridging process
* WAIT
	+ Bridging generally is not instantaneous, and can often take five to ten minutes for the transaction to be fully processed on the first chain, and then the second chain.
* Open your wallet on the second chain (If you're managing both chain's assets in MetaMask, make sure you switch networks in MetaMask!) and verify the assets are present; remember, you may need to [add the tokens to be able to see them](https://support.metamask.io/hc/en-us/articles/360015489031).


 


 

