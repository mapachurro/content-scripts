
Network name
Arbitrum One
Token
ETH
RPC
<https://arb1.arbitrum.io/rpc>
Chain ID
42161
Block explorer
[Arbiscan](https://arbiscan.io/)
Website
[portal.arbitrum.one](https://portal.arbitrum.one/)

Developed by Offchain Labs, Arbitrum One was the first live, permissionless Ethereum **layer 2 (L2) network** with full smart contract functionality. Its mainnet, currently in beta, went live in August 2021. At the time of writing, it has the largest market share of all L2s, at over 50%. 


Arbitrum was specifically developed as a scaling solution for Ethereum, designed to provide an experience as close to Ethereum itself as possible (right down to **using the same token, ETH**) whilst minimising fees and improving capacity. As a L2, its network is external to Ethereum but closely linked, running in parallel and on top of mainnet (as their name suggests). Arbitrum handles and executes transactions "off-chain", whilst using layer 1 (L1; Ethereum mainnet) as its "settlement layer", with data on completed transactions is posted to L1. This link means L2s retain the security of Ethereum mainnet whilst dramatically increasing maximum transaction throughput (i.e. capacity). 


L2 solutions such as Arbitrum are often referred to as "**rollups**". The name originates from the fact that **they *roll up*bundles of transactions**, sending them for processing on L1. Combining multiple transactions into one bundle and submitting as a single transaction enables the network to complete significantly more transactions per second (tps) when compared with submitting one-by-one on mainnet.


Similarly to how proof of stake (PoS) blockchains use validators (or similarly named entities) to secure the network, Arbitrum relies on operators to propose valid blocks to the network, which can then be confirmed or challenged by other nodes (operators). 


Arbitrum is an **optimistic rollup**. Its name refers to the fact that it assumes all transactions are valid, instead using a dispute resolution process whereby any operator can challenge a submitted block if they think it is inaccurate. Eliminating the intensive computation necessary to confirm every transaction means optimistic rollups can process transactions at a higher rate: Arbitrum claims to be capable of 40,000tps. If you want to learn more about optimistic rollups, this [Finematics video](https://youtu.be/7pWxCklcNsU?t=266) is a great explainer. 


Since Arbitrum is still in beta, there are a few [administrative controls](https://developer.offchainlabs.com/docs/mainnet#:~:text=Why%20Mainnet%20%22Beta,other%20L2%20systems.) in place, which you should be aware of before using the network. 


 


**Using Arbitrum**
------------------




**How do I use MetaMask with Arbitrum?**

Since Arbitrum is EVM-compatible, you can use your existing MetaMask wallet on its network, should you choose to. Simply make sure you have [added the Arbitrum network to your wallet](https://support.metamask.io/hc/en-us/articles/360043227612), and switch over to it to view any ETH which you have transferred via the bridge.





**Is ETH on Arbitrum the same as ETH on Ethereum?**

No — although Arbitrum uses ETH as its native token to pay for transactions, you need to bridge all tokens—ETH included—to and from Arbitrum. Any existing ETH you hold in MetaMask on Ethereum mainnet will not be usable on Arbitrum. 





**Bridging ETH to Arbitrum**

Bridging involves transferring a token from one network to another. You can exchange ETH on Ethereum mainnet for the exact quantity on Arbitrum, plus transaction fees. 


The official Arbitrum bridge is available at [bridge.arbitrum.io](https://bridge.arbitrum.io/), and there are [alternatives](https://portal.arbitrum.one/#bridgesandonramps) accessible from the Arbitrum portal.





**Other methods of getting ETH onto Arbitrum**

* **Buy directly (on-ramp)**. These services involve buying ETH as you would do for Ethereum, only that the ETH you buy is already on the Arbitrum network, avoiding transaction fees for bridging. You can find them in the 'Bridges & on-ramps' section of the [Arbitrum portal](https://portal.arbitrum.one/). Transak, for example, is amongst them.
* **Buying from an exchange which supports Arbitrum and withdrawing directly to the network**. At the time of writing, major exchanges such as Binance and Crypto.com are listed on the Arbitrum portal. These options enable you to withdraw directly from the exchange wallet into the wallet you want to use on Arbitrum, such as MetaMask, saving the costs of having to withdraw to Ethereum and then pay to bridge to Arbitrum.





**How much do transactions cost on Arbitrum?**

Transaction costs are always a reflection of network congestion, although on Arbitrum will typically be a few USD, paid in ETH.


For a live overview of transaction costs on Arbitrum, check [l2fees.info](https://l2fees.info/). 






**Useful resources**
--------------------


[Arbitrum L2BEAT overview](https://l2beat.com/)


[Optimistic Rollups: the present and future of Ethereum scaling](https://medium.com/offchainlabs/optimistic-rollups-the-present-and-future-of-ethereum-scaling-60fb9067ae87) (Offchain Labs) 


[An Incomplete Guide to Rollups](https://vitalik.ca/general/2021/01/05/rollup.html) (Vitalik Buterin, Ethereum co-founder)


[Layer 2 Scaling Solutions](https://pages.consensys.net/webinar-layer-2-scaling-solutions) (Consensys webinar; signup required)



**Relevant support articles**
-----------------------------


[User Guide: Custom networks and sidechains](https://support.metamask.io/hc/en-us/articles/4404424659995-User-Guide-Custom-networks-and-sidechains) 

