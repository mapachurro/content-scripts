What is sweeping?
-----------------


Sweeping (also known as *scavenging*) involves malicious parties assigning a script to your wallet which monitors transactions broadcast to the network, as well as the *mempool* or *txpool* (transaction pool) where pending transactions are temporarily stored. Once these sweeper scripts identify an incoming or outgoing transaction from the targeted wallet, they intervene to sign a new transaction before the original is complete. The funds can then be intercepted and transferred instead to a wallet written into the script by its owner. 


**Your wallet can only be affected by a sweeper script if you share your secret recovery phrase with a bad actor**. 


They are particularly troublesome for two reasons:


* **The code can react far quicker than a human ever can**. Racing to move your funds through your wallet faster than the script will always result in you coming out second best.
* **It is subtle**. It is not immediately apparent to the user that they've been hacked, as the script works out of sight. If you perform a significant transaction and you or the recipient do not receive the funds, you may at first assume the transaction is stuck or pending, or that MetaMask has misfunctioned.


How might this play out in practice?
------------------------------------


The first and crucial step for a scammer is to obtain your secret recovery phrase. To do so, they may deploy a phishing attack, which could use the spoofing method outlined above. They may pose as a friendly helpdesk engineer offering to help you resolve your issue or attempt to disguise themselves as an official MetaMask support account. Another potential avenue is to set up a seemingly trustworthy dapp—or mimic an established one—and require the user to input their private key or secret recovery phrase to use it.


If they are successful, they will be able to access your wallet, obtain your private key, and write it into the sweeper script. Possession of your private key allows the script to **sign transactions without your knowledge**, allowing it total and unrestrained control over wallet activity. The script will then proceed to monitor transactions coming to and from your account and *sweep* out any tokens you transfer in before you could possibly react. 


Sweeper scripts are a nuisance to dispose of once they have infiltrated your wallet, and require you to employ very complex methods or even recruit whitehat hackers. For example, there are highly specific approaches you can take if you are attempting to [get NFTs out of a compromised wallet](https://medium.com/mycrypto/operation-cryptokitty-rescue-93fd8e00e4f8). 


How can I stay safe?
--------------------


**Keeping your secret recovery phrase secure is the best and most dependable way to avoid falling victim to sweeper scripts.** Without it, malicious actors cannot access your private key and sign transactions that steal your funds. 


Another option—the relevance of which scales with how much you value your crypto holdings—is to **consider** **buying a hardware wallet**. Popular options include Ledger and Trezor. Hardware wallets are termed "cold" wallets as they store your private keys completely offline, a considerable obstacle to hackers. 


As with most things web3, you should also **stay sceptical**. That is to say, whenever you interact with Dapps, do not assume they are reputable and trustworthy. Always do your research and make sure you are comfortable with the risks. 


 


 


*See also: [Fighting back against sweeper bots](https://support.metamask.io/hc/en-us/articles/5716855323675)*

