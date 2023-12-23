Signature phishing is a method where attackers obtain an off-chain signature from users, and then use it later to steal their assets. 


Naturally, there's a lot of blanks to fill in here, so let's begin. 


What is an off-chain signature?
-------------------------------


Signatures are an integral part of using a self-custody wallet like MetaMask. Any action in web3 requires your authentication—via signing—to prove that the message or transaction came from you. 


Every time you interact with a smart contract, such as when swapping on MetaMask, you're signing a message that allows something to happen on your authority. A swap, for example, requires you to sign a message to confirm that you actually *do*want to swap a given amount of token A for a given amount of token B. 



#### Want more on signatures?


For more information on signatures and their role in MetaMask, see [here](https://support.metamask.io/hc/en-us/articles/15756276171163).



The majority of signatures are on chain; that is to say, they are broadcast to the network and recorded *on the blockchain*. 


As Ethereum has evolved, it has become possible to sign transactions **off chain**. This means they are never broadcast to the network. Crucially, in this scam, off-chain signatures allow the dapp collecting the signature to use the signed message at a time of their choosing. 



#### Note:


For a fuller explanation of the difference between on-chain and off-chain transactions, see our article on metatransactions [here](https://support.metamask.io/hc/en-us/articles/12143770005275).



Signature phishing attacks
--------------------------


Here's the general pattern of this scam:


1. **The attacker creates a fake dapp** and somehow manages to achieve some user traffic to the dapp.
2. **The dapp is designed to prompt users to sign off-chain messages**. The dapp will be misleading: the user will likely be told by the dapp that they're signing a message with a completely different function. For example, they may think they are signing to deposit tokens, or list an NFT. In reality, and since transaction data is so rarely readable by humans, they may be inadvertently handing over an unlimited [token approval](https://support.metamask.io/hc/en-us/articles/6174898326683), or allowing all their NFTs to be listed.
3. **The attacker uses the signature** **to steal your assets**.


Let's take a look at the two main contexts in which we've seen this type of attack:


### NFT signature phishing


As we've already mentioned, it's possible for a dapp to request your signature to list NFTs. This is not inherently bad: any NFT marketplace will require your permission to list an asset. 


Things *do* turn bad, though, when you sign a message on a fraudulent dapp.


#### How it works


One example we've seen in the wild involves fraudulent imitations of the NFT marketplace, [Blur](https://blur.io/). As with similar NFT marketplaces, listing an NFT on Blur requires approving the dapp's request to 'spend' your NFT; in other words, give them the authority to list it. 


The specific part of Blur that attackers have taken advantage of is the ability to bulk list your NFTs. This involves signing a 'Root' message, as below: 


![blur_bulk_listing.jpeg](https://support.metamask.io/hc/article_attachments/18405928097435) 


*Image courtesy of ScamSniffer. Thread [here](https://twitter.com/realScamSniffer/status/1673363566043484160).*


Malicious dapps try to get your signature on similar 'Root' messages, allowing them to 'spend' (withdraw) all the NFTs in your account.


#### What to do about it


If you believe you may have signed a malicious request, you may be able to revoke your approval before your NFTs are stolen. 


Visit a tool such as [revoke.cash](https://revoke.cash/), locate the approval in question, and send a transaction to revoke it. You can read more about revoking approvals [here](https://support.metamask.io/hc/en-us/articles/4446106184731).  


In future, always double-check the URL of the site requesting your signature. In the screenshot above, we can clearly see that it shows Blur's legitimate URL. If it's anything unexpected, or isn'tthe same as what you expect, you should probably do additional research before you sign.


### Permit2 signature phishing


#### How it works


*Permit2* is a token approval smart contract designed by Uniswap. It aims to improve the user experience by consolidating the approval and the contract interaction into a single step. This way, the user no longer has to sign a token approval for every dapp they want to use, saving gas fees, admin, and time. Instead, they sign the permit2 approval message and bundle it with the contract interaction, simplifying the usual two-step ERC-20 approval process (*approve* + *transferFrom*, as we explain [here](https://support.metamask.io/hc/en-us/articles/6174898326683)). If you'd like to read more, check out this [Uniswap blog post](https://blog.uniswap.org/permit2-and-universal-router).


Here's how the **ERC-20 approval** process works:


![Signature phishing diagram](https://support.metamask.io/hc/article_attachments/18447240732059)


**Permit2, by contrast, works by using an off-chain signature**. Once the user has signed, dapps that support the permit2 method can use the signature to transfer tokens relatively freely. 


Notice how the user only needs to interact with the contract once, since the off-chain approval message is bundled in when they request an action of the protocol: 


![Signature phishing diagram](https://support.metamask.io/hc/article_attachments/18447240751515)


*Diagrams inspired by [Dragonfly](https://github.com/dragonfly-xyz/useful-solidity-patterns/tree/main/patterns/permit2).*


 


Although permit2 and its implications are positive step for user experience, obtaining a permit2 signature is, naturally, a scammer's dream for multiple reasons. A few, however, stand out:


* **The act of signing is not recorded on chain**. This can make the attack hard to investigate, preventing the fraudulent interaction and dapp from being identified.
* **The attacker may not steal assets immediately**. A permit2 signature can be configured to remain valid for a specified duration. The attacker may leverage this to cover their tracks: a user can interact with a dapp and lose no assets immediately, then conclude it's completely safe. If the approval is set to remain valid for weeks, the attacker can steal the assets later. By the time they do, the user may have interacted with hundreds of sites, making it extremely difficult to identify the culprit.


#### What to do about it


If you have signed a permit2 message that could leave you vulnerable to attack, you can visit [ScamSniffer](https://app.scamsniffer.io/permit2) or [revoke.cash](https://revoke.cash/) to manage your permissions. 


A more extreme option is to [transfer](https://support.metamask.io/hc/en-us/articles/360015488931) any at-risk tokens to a different account. Permit2 operates on a per-account basis, so any permit2 messages you have signed only apply to the account you used at the time, and not any others you may have in MetaMask or other wallets.


 


What else can I do?
-------------------


Here are some options:


* **Enable security alerts in MetaMask**. To do so, head to Settings > Experimental and flick the toggle. You can read more about this feature [here](https://support.metamask.io/hc/en-us/articles/12539282795675).
* Consider using browser extensions such as [Wallet Guard](https://www.walletguard.app/) or [Pocket Universe](https://www.pocketuniverse.app/), which can help you identify fraudulent messages before you sign.
* Make sure you're clued up on closely related concepts:
	+ [What is a token approval?](https://support.metamask.io/hc/en-us/articles/6174898326683)
	+ [Scammers and Phishers: Rugpulls and airdrop scams](https://support.metamask.io/hc/en-us/articles/4407169552667)
	+ [How to customize token approvals with a spending cap](https://support.metamask.io/hc/en-us/articles/6055177143579)
