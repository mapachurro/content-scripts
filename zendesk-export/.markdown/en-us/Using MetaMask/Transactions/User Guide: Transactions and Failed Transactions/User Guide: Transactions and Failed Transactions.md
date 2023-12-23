
#### New to crypto and web3?


Head to [MetaMask Learn](https://learn.metamask.io/) for a straightforward learning experience designed specifically for newcomers to web3. It's completely free, available in multiple languages, and includes useful tools such as simulations to help you find your feet with MetaMask.



#### *This article consists of an explanation and links to resources surrounding transactions and why they fail, and further down, links to common failed transaction scenarios and how to address them:*


* [Anatomy of a blockchain transaction](#h_01G79J04D0EN1VD8VS7C7J7KD1)
* [Common problems](#h_01G79J09NWA8CGR4VYC2PT5B6Y)
* [Main fixes](#h_01G79J0J8JTRPM9MRB76EN1GPP)
* [Additional resources and next steps](#h_01G79J0RP8ZMZ1V1SKQY70TXCT)
* [FAQs](#h_01G79J18RBK27GZCF10CGN9GKP)


 


**Anatomy of a blockchain transaction**
---------------------------------------


When we talk about 'transactions' on a public blockchain network, we're usually talking about interactions between two addresses; in other words, tokens, be they fungible or non, or other crypto-assets being 'sent' from one address to another. There are also transactions referred to as "internal transactions", which are interactions that occur between smart contracts, and for the most part fall outside of the scope of this article.



#### Want more info?


For more on blockchain networks and how they work in general, check out our [intro article here](https://support.metamask.io/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-), and if you get stuck on any unfamiliar words, our [glossary is always available](https://consensys.net/knowledge-base/a-blockchain-glossary-for-beginners/).



For clarity's sake, nothing is actually being *sent* anywhere. A smart contract-enabled blockchain network like Ethereum has a number of different components, or functions. One of these is what we would call a "computer": the Ethereum Virtual Machine, or EVM, which is capable of running programs ('smart contracts'). The backbone of the system, however, is a *distributed ledger*: **imagine a spreadsheet that contains, on one side, every single Ethereum wallet address, and each address has a column for each type of crypto-asset that it holds.** 


Let's use an example for illustration. Say that Guillaume wants to send a transaction to Dolores. Guillaume has 1.36 ETH in his account, and he plans on sending Dolores 0.5 ETH. Sounds like a good day for Dolores, even in a bear market. 


Guillaume opens up his MetaMask wallet, enters Dolores' address, configures the gas parameters that he's comfortable with paying, and hits 'send'.


At this point, the transaction enters a local temporary holding status, known as the *local memory pool,*or *local mempool*. The transaction will then get 'picked up' by the closest node in the network; depending on Guillaume's [gas settings](https://support.metamask.io/hc/en-us/articles/360022895972-Using-advanced-gas-controls), his transaction will be prioritized (**the more Guillaume is willing to pay per [unit of gas](https://support.metamask.io/hc/en-us/articles/4404600179227-User-Guide-Gas), the faster his transaction will be processed**), and propagated to other nodes in the network. The nodes will do the work of verifying that Guillaume has the ETH to spend, and then will actually perform the 'transaction': **the ledger will be modified; 0.5 will be debited from Guillaume's balance, and 0.5 will be credited to Dolores'.**


*'The moving hand, having writ, moves on':* ETH didn't move through a network per se; it wasn't an email sent from Guillaume's computer to Dolores' MetaMask inbox or anything of the sort. Guillaume sent a request, **authenticated by his [private keys through MetaMask](https://support.metamask.io/hc/en-us/articles/4404722782107-User-guide-Secret-Recovery-Phrase-password-and-private-keys)**, to the network to debit his account and credit Dolores', and after the verification process programmed into the network's protocols, this was done. 


#### *That's all there is to a transaction: a request to the ledger to reallocate something from one address to another.*


 


**When things go wrong**
------------------------


Things can go wrong for a number of reasons. Often, they're 'software in nature': MetaMask has a bug, or something was misconfigured regarding the network you're trying to use; there was a connectivity error.


A **common issue is that the user, in an attempt to pay less for their transaction, sets a very low gas limit**, and network conditions are so congested that there isn't space in any blocks for such a "cheap" transaction, sometimes for a very long time: eventually, this transaction will become "stale" and will have to be cancelled by the user. 


**If you've sent a transaction and it hasn't been finalized**, its status will be shown as "pending" in MetaMask. 


**If you sent a transaction, and it failed, the most likely cause is a lack of gas**: you "ran out of gas", in other words, the transaction had a cost in gas that, when multiplied by the gas price, resulted in a total amount of the network's native currency that was greater than what you had in your wallet. 



#### Info


For more on calculating gas, consult our [gas guide here](https://support.metamask.io/hc/en-us/articles/4404600179227-User-Guide-Gas).



This can happen for a number of reasons, but one thing to consider is what the transaction is that you're trying to carry out. Minting an NFT during peak network traffic times can be very gas-intensive; if you're trying out a new or experimental transaction, it may be worth trying on a test network before paying real live network fees.


 


**Fixing the problem**
----------------------


### **Key Factor #1: Local or Broadcast to Network**


As you go about diagnosing your transaction issue, especially when it comes to a pending transaction, you need to look at whether the transaction is still in your local mempool, or whether it has made it to the network and is stuck there for whatever reason. If it is just in your local mempool, the solution could be as simple as locking, and unlocking, your MetaMask wallet (**make sure you know your password and have your Secret Recovery Phrase backed up before you do**). If it's made it to the network, the solution could be more complicated.


For more on fixing these problems, see the links below.  
  



### **Key Factor #2: Nonce**


This word can mean a few different things. It's a contraction of "number only used once", and in this context, it roughly means 'transaction number', starting from the first transaction made by the sending address. You can get yourself into real trouble if, for example, you're firing two different transactions from different instances of MetaMask with the same wallet address at the same time. **Your address' transactions need to be in increasing order according to their nonce.**However, just as nonces are capable of causing a stuck transaction, they can be the key to getting a transaction unstuck.


For more on that technique, [see here](https://support.metamask.io/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction).


 


**Next Steps**
--------------


### *If you have a failed or pending transaction, consult the following resources for assistance.*


#### [How to send tokens from your MetaMask wallet](https://support.metamask.io/hc/en-us/articles/360015488931)


#### [How to speed up or cancel a pending transaction](https://support.metamask.io/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction)


#### [Why did my transaction fail with an "Out of Gas" error? How can I fix it?](https://support.metamask.io/hc/en-us/articles/360038849792-Why-did-my-transaction-fail-with-an-Out-of-Gas-error-How-can-I-fix-it-)


#### [Uniswap Troubleshooting](https://support.metamask.io/hc/en-us/articles/360053394291-Uniswap-support-and-troubleshooting-tips)


#### [User Guide: Gas](https://support.metamask.io/hc/en-us/articles/4404600179227-User-Guide-Gas)


#### [Can I reverse an already confirmed transaction?](https://support.metamask.io/hc/en-us/articles/360059957352-Can-I-reverse-an-already-confirmed-transaction-)


 


**FAQs**
--------


#### 
*Q: One account in my wallet has a pending or in-queue transaction. Can I start another transaction from a different account within the same wallet?*A: Yes, you can. The nonce is counted per account, not per wallet.

