What is a metatransaction?
--------------------------


Metatransaction is a term that, simply put, describes a transaction that you instruct a third party to complete on your behalf. 


### On-chain transactions


Before we describe what metatransactions are and how they work, it's necessary to recap what we mean by **signing a transaction**. 


When you interact with Ethereum mainnet and similarly designed networks, most of your activity will be determined by simple transactions. At a basic level, if you want to send funds to another address, you need to *sign* a transaction **on-chain**. Signing a transaction means that:


1. **You are the legitimate originator of the transaction**, i.e. *verification.*
2. **You irreversibly consent to a given amount of an asset being transferred to another address** — referred to academically as *non-repudiation.*
3. **The data in the transaction cannot be modified after you've signed**, i.e. *integrity.*


Metatransactions — essentially just signed messages — share these same characteristics. However, they differ from standard transactions in the extent to which they are processed on-chain. A regular transaction — such as moving funds from one address to another — is computed and recorded on the blockchain. 


### Metatransactions: *off*-chain


Metatransactions, by contrast, conduct one or more steps of the transaction **off-chain**. This is where they get their name: as a prefix, *meta*generally refers to something being beyond, behind, or after something else. 


Why is this significant? Well, conducting activities off-chain comes with benefits. Mainly: **it's cheaper**, at least for the person initiating the transaction, the user. This is because the user doesn't have to shell out gas fees to pay for their transaction to be processed.


Instead, what generally happens is that the transaction is paid for by a **relayer** — a **third party that receives the signed message from the user and then passes it onwards to the network, paying the necessary gas fees.**


Note how we say **message**, and *not* transaction. When you transact via a relayer, you're sending the relayer a signed message, and nothing more — it's only when the relayer then submits your instructions to the network with gas that we can truly refer to a transaction. 



#### Where do relayers get the funds from to pay for gas?


Relayers typically get their funding from the developers or originators of a dapp using their services. More complex funding models are possible — such as issuing your own token to be used as a kind of 'voucher' to be used specifically for paying gas — but generally, this is how it works.


This isn't such a radical model. Think of the infrastructure of web2: the vast farms of servers that process and store the enormous volumes of data the internet generates every day. Web2 platforms don't usually charge you for using the platform. In other words, the infrastructure costs are not paid by the user. Instead, the site itself takes the hit, and seeks to offset this through other revenue streams, such as advertising or paid premium versions.



### What does a relayer do?


Relayers take the details of your signed transaction — the token you want to send, how much of it, and to whom — and incorporate it into another transaction, which they then submit to the network to be computed. 


The metatransaction you sign, therefore, isn't a *complete*transaction, in that it doesn't contain all the usual components necessary to process it on-chain. Most notably, it's missing gas. The transaction that the relayer puts together, however, is complete with gas, and will be processed by validators. 


 


What do metatransactions look like in MetaMask?
-----------------------------------------------


For you, the user, sending a metatransaction will be similar to sending any other. You still sign a transaction that specifies a value, a token, and a recipient address. The difference is that the recipient address is a relayer, rather than the actual end recipient of the funds. **This means that, in practice, you don't really have to do anything differently**. 


The main giveaway of a metatransaction is that it will cost you nothing. You'll just be prompted to 'Sign': 


![MetaMask Metatransaction](https://support.metamask.io/hc/article_attachments/12345029059227)


 


What is EIP-712?
----------------


Whilst not absolutely necessary for understanding metatransactions, a brief look at [EIP-712](https://eips.ethereum.org/EIPS/eip-712) can help explain some of their underpinnings. 


In brief, this EIP (Ethereum Improvement Proposal) makes it possible for wallets to show users readable text relating to the message they're signing, and allow them to sign it. This means that, when you're prompted with a metatransaction to sign in MetaMask, you can be shown human-readable information, rather than a long hexadecimal number of hashed (encrypted) information that's impossible to understand. 


### Why does it matter?


EIP-712 doesn't enable metatransactions, but it makes them much more transparent to the user, and this, in turn, has real benefits for user security. 


Previously, our inability to parse the encrypted hexadecimal string would mean we have to **trust** that the message contains the correct data. This makes us vulnerable to scammers: imagine if you visit a fraudulent dapp and it prompts you to sign a metatransaction. Since you're unable to decipher the hashed, hexademical string, you have no idea whether you're giving you're approving something reasonable or signing a message that gives a scammer a green light to drain your wallet. 


Instead, when the data is converted into a human-readable form — i.e. words — the user can check and confirm the message is what they intended, because it will detail things like:  


* Who or what the recipient is, identifiable by their public address
* If a token is to be transferred, swapped, bought or sold: details of the quantity and token type
* Any other message details relevant to the transaction.


 


Are there any security implications of metatransactions?
--------------------------------------------------------


It's a good habit to maintain scepticism towards any message or approval you're signing with your wallet. However, **metatransactions don't have anything fundamentally insecure or unsafe about them**. 


That being said, they can be used by scammers. As with everything Ethereum (and blockchain in general), part of the trade-off of using a decentralized public network is that malicious actors can also get involved. 


Whenever you're signing a metatransaction, consider the following:


* **Am I on the right website?** Double-check the domain name. If the transaction isn't being proposed by the correct dapp, it could lead to funds loss and/or a compromised wallet.
* **Does the transaction data look correct?** Check the address the signed message lists. Is it the address of the correct smart contract? Does the message detail the correct token and the correct quantity of that token?
