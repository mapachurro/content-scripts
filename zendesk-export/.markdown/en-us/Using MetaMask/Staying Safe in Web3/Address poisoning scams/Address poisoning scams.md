### Contents


* [How address poisoning works](#h_01GPGR9YPJAXM3MBVAV6ZS85GR)
* [How you can stay safe](#h_01GPGRA3FYCA7EEKVJT3ZEGEQY)
* [Summary](#h_01GPGRA8SQJZ1GA7X05TE6S9ZW)


 


**Address poisoning** is an attack vector that, in contrast to other scams — which often use methods that have served many scammers so well, such as unlimited token approvals, phishing for your Secret Recovery Phrase, etc. — **relies on user carelessness and haste above all else**. 


On the one hand, this method is rather innocuous compared to other scam types. However, it can just as easily result in a loss of funds. Let's investigate how this scam is usually structured.


 


How does address poisoning work?
--------------------------------


If you didn't know already, your wallet includes one or more *accounts*, each of which has its own [cryptographically-generated **address**](https://support.metamask.io/hc/en-us/articles/4702972178459). These are long hexadecimal numbers, meaning they use both numerical *and* (a few) alphabetical characters. This is a trait that makes them unintelligible to most people, and — critically — very, **very difficult to remember**. 


This is why, supported by most web3 software, you have most likely come to rely on **copying and pasting addresses**, rather than memorizing them and typing them out. This saves a lot of time and ensures, generally, you don't make any mistakes, and that your funds always go to the right address. MetaMask falls into this category of facilitating copy-and-paste: you can [copy your address with one click/tap](https://support.metamask.io/hc/en-us/articles/360015289512). 


**Address poisoning speculatively exploits this copy-and-paste tendency**. Here's how:


1. You send a regular, everyday, *nothing-to-see-here* transaction to a friend, or to another account you control.
2. The scammer, who has software that monitors transfers of certain tokens (usually stablecoins), notices. **They use a 'vanity' address generator (there are many accessible with a quick web search) to create an address that closely matches yours** (sometimes, it'll match your friend's).  


Since they're so long, crypto wallet addresses are typically shortened. You might see the first lot of characters only, or sometimes you may see the initial 5-10 or so and the final 5-10 or so, skipping the middle. This is how most people recognize addresses: not by knowing every single character, but by becoming familiar with the start and finish. This is the tendency that address poisoning preys on.


![Address poisoning scams](https://support.metamask.io/hc/article_attachments/17277424637467)
3. **The scammer sends you a transaction of negligible value from the dummy account they created** — the 'vanity' address that mimics yours or that of your contact. Usually these are transfers of zero tokens. With this, they've **poisoned**that wallet. (Though, to be clear: this doesn't actually have any negative impacts in itself.)


![Address poisoning scams](https://support.metamask.io/hc/article_attachments/17277408650011)


 


4. Since their dummy address looks so similar to yours, it's entirely possible that, the next time you need your address, **you might inadvertently copy their address from your transaction history and paste it elsewhere.** Naturally, if you paste their address by accident, you'll send funds to them and not yourself/the intended recipient. And since on-chain transactions like this are immutable (cannot be altered once confirmed), the lost funds will be irretrievable.


![Address poisoning scams](https://support.metamask.io/hc/article_attachments/17277408651547)


 


And that's it: all they're hoping for is that you copy the wrong address from your transaction history in your wallet.


 


How can I protect myself?
-------------------------


First off: **there's no way of stopping people — including scammers — from sending transactions to your address**. These are *public*blockchains we're interacting with, so anyone, anywhere can do as they please. 


What we can help, though, is whether we fall victim to the scam by copying the address. This is a tricky one, and awareness is important: even those who consider themselves relatively thorough — and double-check the start and/or end of an address before they copy it — can become victims here.


Here's what we recommend:


* **Above all: check and double-check addresses before you send**. This is self-explanatory. Although it's relevant for any transaction, make particularly sure the address is correct if the assets you're sending have considerable value to you. **Checking every single character** is the only way to be completely safe.
* **Avoid copying addresses from your transaction history,** **and, if you do, check them very carefully**. This goes for both transaction history in your wallet, such as MetaMask, as well as for history shown on the block explorer. Equally, this advice applies to your own address (e.g. if you're moving funds from a centralized exchange to your MetaMask, and need to copy your MetaMask address) as much as it does the addresses of others to whom you may be sending funds.
* **Use a hardware wallet**. Hardware wallets generally require you to check and confirm any address you're sending to before allowing you to complete a transaction. Though it's possible to fall victim to this scam regardless even with this feature, this prompt may help you develop a habit of continual scrutiny of any address you use.
* **Add frequently used addresses to your address book**. In MetaMask, you can find this in Settings > Contacts. If you have a contact's address saved here, you can be confident it's the right one, and won't have to rely on copying and pasting every time you need it.
* **Consider using test transactions**. This involves sending a nominal amount of funds to an address to confirm it's correct before you proceed with a larger transaction. Naturally, this requires gas fees to be paid for two transactions, so depending on the gas price at the time, it may not be appealing.


 


Summary
-------


* Address poisoning involves scammers sending transactions of no value to your account from an address that's very similar to your own.
* Their hope is that you will then absent-mindedly copy this address from your transaction history in future. You or whoever you're passing your address onto will then send tokens directly to them, and not to the correct address.
* Develop a habit of thoroughly checking **every single character**of an address before you send a transaction. This is the only way to be completely sure you're sending to the right place.


If you have any questions about this subject, feel free to head to the [MetaMask Community](https://community.metamask.io/) or get in touch with Support via the 'Start a Conversation' button on the homepage of this site. 

