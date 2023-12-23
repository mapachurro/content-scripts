### Contents:


* [How the scam works](#h_01GR4DD12KA55CASZ5FWPZBH99)
* [How you can stay safe](#h_01GR4DDAF29YFFPJR7BACA6FQW)
* [Summary](#h_01GR4DDKWGE6MB4N7VAG2F282A)


 


Social engineering — more commonly referred to by the more widely used alternative term *phishing*— is, unfortunately, widespread in web3. With self-custody, even experienced, savvy users can still be manipulated into taking actions that play right into scammers' hands. 


More specifically, social engineering describes a scenario where a scammer psychologically manipulates a victim. As you'll be aware, most commonly in web3 this occurs when users are convinced to hand over their Secret Recovery Phrase (seed phrase), providing the scammer with full control of their wallet and its assets. 


For the scope of this article, however, we're focussing on one specific type of social engineering that revolves around **getting you to unknowingly list valuable NFTs with a price of zero**. 


 


How do NFT listing scams work?
------------------------------


Scammers have the entirety of the internet at their disposal, including all the tools, sites, social media platforms, etc. that it entails. As a result, you may encounter a variant of this scam in the wild that doesn't match up exactly with our description below. So, as with all our scam explainers, please take this article as a blueprint, and stay vigilant for the key points in the sections below. 


Here's how fraudulent NFT listings usually take place:


1. **The social engineering**. To start with, the scammer first has to execute the 'social' element of this step. That is to say, they need to try and engage you in a sociable way — contriving an interaction that feels natural, has some plausible pretext, and, often, benefits you somehow. This could be:


	* Complimenting you on some content you posted
	* Offering you 'alpha' on a new NFT project, token, or dapp
	* Providing access to an allowlist for an NFT drop
	* Asking a genuine, relevant question that seems well thought-out...you get the idea. The main thing is that there has to be something in there that piques your interest.


![curiosity-curious.gif](https://support.metamask.io/hc/article_attachments/12514273927835)


And once they have your attention, they can present you with the means to get scammed. From what we've seen, this is typically a fraudulent dapp, cleverly set up to seem legitimate. The catch is that the backend of the dapp is designed to steal your assets.



#### Warning!


The dapp that the scammer links to doesn't necessarily need to be related to the subject they got in touch about, nor does it have to relate to NFTs, any type of token, or otherwise. It just needs to get you to connect your wallet and interact so that it can propose a transaction for you to sign.
2. **The technical underpinnings**. Even if you've [connected your wallet](https://support.metamask.io/hc/en-us/articles/360059535551) to a scam site, there is not really any damage it can do. All it can do is see your account address, which it can then use to check your balances, and propose transactions for you to sign. *However*, **where it does start to get dangerous is when you start to be presented with things to sign**.


Applying your digital signature to a transaction or message means you give it your irrevocable — you can't take it back — blessing. Usually this translates to total consent for it to do what it needs, as dictated by its smart contract. 


The problem with dapps that the scammers provide you with is that they will usually have **mechanisms hidden in the smart contract code that don't match the actions that the dapp displays in the UI**. This is how they trick you.
3. **The theft**. The most common variant of this kind of scam involves this process:
	1. **Prompting you to sign a transaction** on the fraudulent dapp. This may or may not be related to NFTs, and will usually be entirely misleading about what it actually does.
	2. **What you've actually signed is a transaction that lists your NFT(s) for 0 ETH**. The mechanism can be quite convoluted: it may be that the dapp can only access these NFTs because you've already approved OpenSea's access to them. This is how you can list them with a single signature.
	3. The scammer, aware of the 0 ETH listing before anyone else, **immediately purchases it on OpenSea**.


 


How can I spot NFT listing scams and stay safe?
-----------------------------------------------


Due to the possible complexity of social engineering/phishing, even the most experienced web3 users can fall victim to it. Total avoidance of phishing would mean removing yourself from any kind of online social contact or interaction, which, for many, is either unfeasible or undesirable — and even then you'd probably still be targeted. 


However, you can still prevent this occurring by remembering these key principles: 


* Be ultra-wary of any new dapp ***before***you interact with it. Internalize the methods for [deducing whether a smart contract or a dapp is safe to interact with](https://support.metamask.io/hc/en-us/articles/10143114273563).
* **'Sandbox' your valuable assets** in different wallets. For example, you could have one wallet (i.e. one or more accounts backed up with *one* Secret Recovery Phrase) that you use specifically for interacting with dapps. This could be your 'live' wallet for day-to-day activity, and could hold some ETH for interacting with contracts and paying gas. Meanwhile, your valued assets would be stored elsewhere — 'airgapped' in another MetaMask wallet, or stored in a hardware wallet.
* **Be sceptical of strangers on the internet**. Whilst the internet is full of decent people, anonymity makes it fertile ground for scammers. Although unpleasant, it's best to assume that any unsolicited contact — especially if it relates to web3 — has the potential to involve malicious intentions.


 


Summary
-------


tl;dr: **be careful with new, unfamiliar dapps, as they can mask functions in their smart contracts which make you unknowingly list your NFTs for 0 ETH**. 


* This works through social engineering — a.k.a. phishing. The scammer needs a pretext to share their fraudulent site with you.
* Always do your due diligence on any site you come across. See our [guidance](https://support.metamask.io/hc/en-us/articles/10143114273563).
* Consider distributing your assets across different wallets, so that if one is compromised or if you sign an approval or give your signature to something malicious, you at least haven't lost all of our assets.
