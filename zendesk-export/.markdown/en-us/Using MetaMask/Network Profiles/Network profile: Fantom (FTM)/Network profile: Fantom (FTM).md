
Network name
Fantom Opera
Token
FTM
RPC
https://rpc.ankr.com/fantom/
Chain ID
250
Block explorer
[FtmScan](https://ftmscan.com/)
Website
[fantom.foundation](https://fantom.foundation/)

Like many of the other smart contract-enabled layer 1 blockchains that hover around the upper echelons of market cap rankings—Solana, Cardano, and Avalanche amongst them—Fantom aims to address the key challenges facing the original smart contract network, Ethereum. This mainly includes **scalability** and **speed**, accommodating greater transaction volumes whilst retaining affordable transaction costs and security. 


Fantom's approach to delivering scalability is **modular**. Whereas transactions on Ethereum (and many other networks) are all on the same network, sharing infrastructure, **Fantom allows new projects to be launched on their own blockchain**, almost as layer 2 (L2) networks over the mainnet. Operating independently avoids new projects clogging up Fantom Opera over time by funnelling ever-higher volumes of high traffic through the same channel. Instead, Fantom's approach is to create a '**[network of networks](https://fantom.foundation/intro-to-fantom/#:~:text=If%20we%20think,network%20of%20networks.)**'. 


So how is this done? Well, the main contributor is what they call **Lachesis**, an **asynchronous byzantine fault tolerance (aBFT) consensus algorithm**. Quite the mouthful. BFT refers to the [Byzantine Generals Problem](https://en.wikipedia.org/wiki/Byzantine_fault), a logic problem commonly cited in crypto circles: how do a set of generals, hampered by the limitations of medieval communication, reach *consensus* on whether or not they should attack a fortress? And, more critically, how can each general trust the others when they say they will attack, especially when a lack of coordination may result in defeat? Applied to decentralized blockchains, BFT essentially refers to the question of how we can trust a decentralized network's validity when there is the possibility of deceitful actors. 


The **Lachesis aBFT consensus mechanism**gets around the challenges of many alternative mechanisms through being *asynchronous.* Rather than syncing a validated block with every other node connected to Lachesis (i.e. the Fantom mainnet)—just as every Ethereum validator syncs with all others—the Lachesis node only has to complete blocks within its own network. You can read more about Lachesis and how it works [here](https://fantom.foundation/lachesis-consensus-algorithm/). 


Fantom uses a **Proof-of-Stake** system to underpin its validator community, and in turn the security and function of the network as a whole. You can stake as little as 1 FTM using the [official Fantom wallet](https://pwawallet.fantom.network/#/), delegating your stake to a validator. To become a validator, you would need to stake at least 1,000,000 FTM. 


Both Fantom mainnet (Opera) and the L2 networks built on top of it (Lachesis nodes, powering dapps) are EVM-compatible, meaning you can interact with them using MetaMask. 


Fantom's native token FTM is necessary to pay for transactions when connected to Fantom Opera. However, constituent blockchains in the 'network of networks' can create and require use of their own native tokens. 


 


**Using Fantom**
----------------




**How to add Fantom to MetaMask**

The easiest way to add Fantom is by following the steps for adding a popular network, detailed [here](https://support.metamask.io/hc/en-us/articles/360043227612). 


Once the network is added, you'll be able to select it at any time in future from your previously accessed networks in MetaMask. 





**How do I switch to Fantom in MetaMask?**

Please note the below instructions assume you have already added Fantom to your MetaMask (see above). 


**On Mobile**: On your wallet page, find where it says the current network you're connected to at the top of the screen. Tap here to open a list of the networks you've already added. Scroll until you find Fantom, and tap to set it as your current network.


![MetaMask Fantom Opera network mobile](https://support.metamask.io/hc/article_attachments/17281219656091) 


**On Extension**: Select the drop-down arrow in the top left corner of the app. It will currently display the network you're connected to, such as 'Ethereum Mainnet', or any other you used last. Scroll through the menu until you find the Fantom network, then click on it to switch.


![MetaMask Fantom Opera network extension](https://support.metamask.io/hc/article_attachments/17281219660827)


 





**Is my MetaMask address on Fantom the same as other networks in MetaMask?**

Yes.


Assuming you are using the same account within MetaMask, your wallet address is the same regardless of the network you're connected to. 


Fantom Opera's EVM-compatibility means MetaMask can connect to it just as you would to Ethereum mainnet. 


However, take care to not confuse your MetaMask address with your address for Fantom Wallet (if you use it). Fantom shares the same address format as Ethereum and EVM-compatible networks (i.e. beginning with 0x) but is [different](https://fantom.foundation/fantom-faq/#:~:text=Note%20that%20Fantom%20Opera%20addresses%20share%20the%20same%20structure%20as%20Ethereum%20addresses%20(0x%E2%80%A6)%2C%20but%20they%20are%20not%20Ethereum%20addresses.).





**Can I stake FTM with MetaMask?**

No. MetaMask can be used to:


* Store FTM (see below for the different forms this token could be in)
* Interact with dapps that are connected to Fantom mainnet.


To stake FTM, you will need to use the [Fantom wallet](https://pwawallet.fantom.network/#/). 





**Types of FTM token, and how to tell which you have**

As explained on the [Fantom FAQ](https://fantom.foundation/fantom-faq/#token), FTM can only exist in three formats:


* **FTM** (native, on Fantom Opera)
* **ERC-20**: On Ethereum
* **BEP-2**: On the Binance Chain.


However, and in contradiction to this list, you may be able to bridge FTM onto other networks which have their own version of the ERC-20 standard. For example, you can get a BEP-20 version of FTM on Binance Smart Chain. 


When you buy FTM on a centralized exchange, you may also have a choice of networks for your withdrawal. Binance, for example, supports FTM withdrawals to BSC (as a BEP-20 token), Ethereum (ERC-20), and Fantom Opera/mainnet itself. See [here](https://support.binance.us/hc/en-us/articles/4418866690199-Binance-US-Now-Supports-Fantom-FTM-Mainnet-for-Deposits-and-Withdrawals-Buy-FTM-Using-Debit-Card-Bank-Account-or-Wire-Transfer-) for more information. 





**Bridging tokens to Fantom**

As with any other network you will use, barring some exceptions, you cannot simply send tokens from one network to another without bridging. In all likelihood, **you will lose your tokens if you don't bridge them.** 


This is because FTM on the Fantom Opera is a fundamentally different token to FTM ERC-20 tokens on Ethereum, for example. Bridging involves moving the token from one format into another.


To do this, Fantom recommend you use [multichain.xyz](https://multichain.xyz/swap). 





 


**Relevant support articles**
-----------------------------


[User Guide: Custom networks and sidechains](https://support.metamask.io/hc/en-us/articles/4404424659995-User-Guide-Custom-networks-and-sidechains)


 


**Useful resources**
--------------------


[The Ultimate Guide to FTM](https://fantom.foundation/blog/the-ultimate-guide-to-the-ftm-token/) (The Fantom Foundation)


 

