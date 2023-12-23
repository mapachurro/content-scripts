If you're moving tokens around from one network to another, it's best to be careful about what you're doing, and always [use a safe bridge.](https://support.metamask.io/hc/en-us/articles/4836913606683-Field-Guide-to-Bridges)


However, accidents happen, so if you think you sent tokens on the wrong network, here are some steps you can take.


 


### EVM-compatible tokens and networks


One of the cool things about your Secret Recovery Phrase is that it can be used on multiple networks, with the same address, provided the network is *EVM compatible —* in other words, uses the same technical configuration as Ethereum. Many popular networks are EVM compatible, such as Polygon, Arbitrum, Optimism, and Avalanche. Some notable networks that are *not* EVM compatible (or are working on becoming EVM compatible) include Klaytn, Algorand, and StarkNet.


So let's say you meant to send some tokens to a friend on Ethereum, but you sent them on Polygon instead. Good news — all your friend needs to do is switch networks to Polygon, and the tokens you sent should be there. They could then bridge them to Ethereum, and use them as they originally intended. In this scenario, the tokens aren't lost.


 


### Non-EVM tokens and networks


**If you tried sending tokens directly from your MetaMask wallet to a non-EVM network, and the transaction went through, it's entirely possible that your tokens are gone forever.**


**If you're dealing with tokens sent between Binance entities, [check our Binance series here](https://support.metamask.io/hc/en-us/articles/4412308177691-Understanding-BSC-Binance-and-MetaMask).**


Let's say that Address A, created on Ethereum, sends 0.5 ETH through MetaMask on the Ethereum network to Address B, which was created on Algorand.


Both of these addresses are derived mathematically from a series of words; we call it a Secret Recovery Phrase, Algorand calls it a Mnemonic Phrase, but it's the same type of technology: a series of words that represent a very long number, which, when passed through certain processes, will always produce the same public addresses used to send and receive tokens. So we've got two Secret Recovery Phrases here: A, from Ethereum, and B, from Algorand.


The problem is that you sent the tokens on the Ethereum network, and they went to the address that you specified—*on the Ethereum network—*and the mnemonic phrase you have for your Algorand wallet will not work on Ethereum. Or, rather, it won't create the same addresses on Ethereum that it did on Algorand. So if you grab your Algorand mnemonic, [open up MetaMask in a fresh browser profile and import it](https://consensys.net/blog/metamask/how-to-manage-multiple-wallets-with-metamask/), unfortunately, if it even works, you will see different addresses.


 


![MetaMask Different address from same SRP](https://support.metamask.io/hc/article_attachments/15924710377499)


*A seed phrase is linked to a specific network; it will not restore the same address on another network.*


 


Maybe you sent your tokens, accidentally, to someone else's wallet, who owns that address on Ethereum. Much more likely, however, you have sent those tokens to an address that will never be claimed by anyone; the number of potential SRPs and addresses on Ethereum is mind-numbingly large, and the odds are very much against this ever happening.


 


![MetaMask Same address for different network](https://support.metamask.io/hc/article_attachments/15924687415579)


*You cannot send tokens directly between networks. If you do, chances are you've deposited them in a stranger's wallet, or a wallet address that will never be claimed.*


 


### Smart Contracts


Smart contracts are, generally speaking, not good things to send tokens to. They have addresses, but unless you *absolutely know what you are doing*, you should interact with a smart contract through a UI, not by simply sending funds directly to it. Remember: a smart contract is a computer program that runs on the blockchain, and many of them are not set up to be actively accessed and used to send or receive tokens. That said, **if you did accidentally send tokens to a smart contract, don't despair**--reach out for help to the community related to the smart contract in question. [One of the greatest stories ever told in Ethereum](https://www.paradigm.xyz/2020/08/ethereum-is-a-dark-forest) is about getting tokens out of a smart contract.

