At times, you may interact with a dapp, and expect to see a transaction record in MetaMask, but you don't. Your next step, as always, should be to verify on a block explorer whether the transaction occurred. Even then, though, you might not see it, if it is an *internal transaction.*


### So if you're looking for a transaction and don't see it anywhere, check under the 'Internal Transactions' tab in Etherscan.


To learn how to examine your account on Etherscan, start [here](https://support.metamask.io/hc/en-us/articles/360057536611).


Here's an example of what an internal transaction looks like there:


![Internal Transaction Example](https://support.metamask.io/hc/article_attachments/12927478386075)


*The actual transfer of funds shows up under the “To” field.*


 


### Why aren’t *internal transactions* displayed in my wallet activity/history?


When we talk about a 'transaction', we are referring to the act of an amount being deducted from one account, and that amount being added to the balance of another account: a simple transfer. However, as more sophisticated dapps are created, there are other things that happen on the blockchain that aren't "simple transfers".


An *internal transaction* is an action that is occurring within, or between, one or multiple smart contracts. In other words, it is initiated inside the code itself, rather than *externally*, from a wallet address controlled by a human.


Often, the end result of the internal transaction is that one address or another will end up with more tokens of some kind; for example, if you're minting DAI, or if you're reserving an ENS name (in the latter case, you end up with that ENS name in your wallet).


Currently, MetaMask does not show internal transactions in your transaction activity or history, only standard transactions between addresses.


That said, **there is no difference between tokens received through an internal transaction, and those received through a standard transaction.** The transfer of funds **is** **reflected** in the overall balance of the account.


The reason MetaMask does not show these internal transactions is mainly a technical one; internal transactions, being somewhat "ephemeral" in nature (they occur while the code is running), are not recorded on the blockchain. There are some services, like Etherscan, that track internal transactions.


 

