
> This article was adapted from a blog post available [here](https://consensys.net/blog/metamask/understanding-and-avoiding-crypto-honeypot-scams/).


Although they have a pleasant-sounding name, honeypot scams aim to steal funds by luring you into interacting with a fraudulently configured wallet. 


Their name references the fact that, at least from the outside, the wallet is highly appealing — just like a pot of honey left outdoors would attract insects and animals. 


### Contents:


* [How honeypot scams work](#h_01GMB85JBJTV7474H5H9S106MH)
* [How to spot honeypot scams](#h_01GMB8HKRWQRD00P8JW4NDQ02K)
* [Summary](#h_01GMB8TBW854KG4AGTQ9AYHRWC)


So how do they work?
--------------------


### Step 1: First contact


Honeypot scams revolve around the principle of dangling the prospect of free money in front of you. They present you with a well-stocked wallet that you can access, hoping that you do indeed to try to access it and send funds out. 


To make sure that you *can*actually access it, a **key element in the ploy is the scammer sharing the wallet's Secret Recovery Phrase (seed phrase)**. Usually, they get in touch to do so, posing as an innocent web3 citizen that needs help with their wallet. For example:


 


![Honeypot scam example](https://support.metamask.io/hc/article_attachments/13271285752603)


They do this in the hope that your thought process will be something like: *Hah, what a noob — I'll just go straight into their wallet and transfer that 6,000 USDT straight to my own wallet. Easy money!*



#### Never, ever share your Secret Recovery Phrase like this


The scammer above has deliberately shared their Secret Recovery Phrase to fool you. To be clear: you should **never** share yours.



### Step 2: You try to move the tokens to your own wallet


Possessing the private key to a wallet with $6,000 worth of tokens sitting in it is tantalizing. But wait: this is where things get a little more complex.


Usually, the value in a honeypot wallet will be tied up in tokens *other than*the network's native token. This means that if you wanted to send them anywhere else, you'd need to somehow get a small amount of the network's native token into the wallet to pay the gas fees for the transfer. In the above screenshot, the scammer "Candi" lets us know the network, telling us that the USDT is a "trx20" token. (*TRX*suggests the Tron network; but even if it were on there, it would actually be a TRC20 token; anyway, let's not get distracted.)


So let's say you load up Candi's wallet on a new browser instance or similar, with the intention of transferring the 6,000 USDT out. You send a little TRX to fund the transaction, and... it's gone. 


What happened?


### Step 3: A script steals the tokens you intended to use for gas


This is where the scammer makes their money. The funds they leave in the wallet as bait are never touched, because no one can ever transfer them out. **The tokens you send to the address to use for gas fees are automatically sent elsewhere by a sweeper script**(a.k.a. sweeper bot) before you can send a transaction yourself. 


If you were to load up the block explorer page for an address that was serving as a honeypot, it would look something like this:


![Honeypot scam example](https://support.metamask.io/hc/article_attachments/13271297172379)


Notice how there are lots of transactions happening within very short, distinct windows: BNB, a native token used to pay for gas, is being transferred out almost as soon as it is being added. 


This is because the script is 'listening' for transfers into the wallet address, and reacting to them virtually immediately by submitting a transaction to *sweep*them out. 


 


How can I spot honeypot scams?
------------------------------


Here are a few things to look out for:


* **Anyone sharing a seed phrase/Secret Recovery Phrase**. This should be an immediate red flag, since anyone using a self-custodial wallet in good faith would never share theirs. (Other than edge cases, such as developers wanting to access the same test wallet.)
* **A transaction history that suggests any transfers *in*are immediately transferred *out*** (or, at least, shortly after). Honeypot scams need a script that will sweep funds out to a third wallet. Look up the wallet on a block explorer and check for these patterns.
* **People sending you direct messages on social platforms**. Scammers rely on social media platforms for direct access to you, the user. Be wary of anyone who contacts you regarding crypto/web3 on these platforms — there is a chance that they're out to harm you. Also look out for bots set up to share these messages, identifiable by the fact they share the same tweet/message repeatedly.


 


Summary
-------


Honeypot scams work by:


1. 1. Sending you the Secret Recovery Phrase/seed phrase to a wallet, claiming to be seeking help
	2. Hoping that you see the valuable funds in the wallet, and want to transfer them out or swap them
	3. Expecting you to send some of the network's native token to the wallet to pay gas fees for the transactions in step 2
	4. Stealing the tokens you send using a sweeper script, which *sweeps*them into a third wallet of the scammer's choosing before you can send your own transaction.


Remember: if you think you've identified a fraudulent address, you can [report it on Etherscan](https://support.metamask.io/hc/en-us/articles/4415323627803). 


If you have any questions about this subject, feel free to head to the [MetaMask Community](https://community.metamask.io/) or get in touch with Support via the 'Start a Conversation' button on the homepage of this site. 

