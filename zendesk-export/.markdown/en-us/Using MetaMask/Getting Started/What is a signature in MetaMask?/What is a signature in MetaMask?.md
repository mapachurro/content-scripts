**Signatures involve using MetaMask to verify that you are the originator of a transaction or message**. MetaMask is a tool for managing your private key(s) and using them to apply your signature to various tasks.


You may have heard the phrase 'not your keys, not your crypto' — well, this is true. To explain this concept, we only need to focus on the 'keys' part specifically. 


The 'keys' are your **public and private key pair**. Every account in MetaMask has a key pair, and when used together, the keys can encrypt and decrypt messages.


When you send a message, the following happens:


1. **You 'hash' the message contents**, producing a long hexadecimal number. (The word 'hash' describes running the message through a hash function, which essentially condenses the message contents into a fixed-size number.)
2. You use your private key to **sign the message**, applying your **digital signature**.
3. The **recipient receives your message and uses *your**public key* to verify it**. Since they used your matching key pair, they can verify that you were the originator of the message.


There's a lot of complexity happening in between—such as assuming that both parties are using the same algorithms for signing and verifying the signatures—but that's the basic process.



#### What's the difference between messages and transactions?


So far here we've talked about messages, mostly; though the eagle-eyed will have noticed that we mentioned transactions in the first sentence of the article.


Transactions and messages are essentially very similar. The main difference to note is that transactions are generally published on the blockchain, while messages are not.



This model, called public (and/or private) key cryptography, is how blockchains work. The ability to apply digital signatures is a vital tool that allows entities to send transactions and messages back and forth without the need to trust that the other person did *actually*send it. 


For comparison: think about receiving an email. Even if the email is sent from your friend's email address, you still cannot be *absolutely*sure it is them. It probably will be, of course; but how can you be sure? With digital signatures on blockchain networks, this guessing game is removed, since the sending and receiving parties don't need to trust that the cryptography and algorithms will work, because they *just do*. 


If you'd like further reading on a deeper technical level, [this article](https://medium.com/mycrypto/the-magic-of-digital-signatures-on-ethereum-98fe184dc9c7) by MetaMask's Maarten Zuidhoorn more than does the trick.

