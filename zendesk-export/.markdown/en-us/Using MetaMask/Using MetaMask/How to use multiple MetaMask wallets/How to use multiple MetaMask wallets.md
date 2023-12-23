
#### Note


*This article was adapted from our blog post, [here](https://consensys.net/blog/metamask/how-to-manage-multiple-wallets-with-metamask/).*



 


### Contents:


* [What is a wallet, anyway?](#h_01GQ58KQMVE4WPE36KNT16AFW3)
* [Why would I need more than one wallet?](#h_01GQ58KX1WSPDGVESJJBA6VPNY)
* [How to manage multiple wallets](#h_01GQ58M3T5NQ19NYWTQ1C1XS2M)


 


MetaMask is a flexible tool that can be used in numerous ways. One facet of this is that there's nothing stopping you from using MetaMask on multiple devices, with multiple Secret Recovery Phrases and private keys. 


 


Defining 'wallet'
-----------------


Since web3 has a fundamentally different user account structure to the traditional/web2 username + password combination we're all familiar with, it's useful for us to define what 'wallet' does and does not describe:


* **Your wallet should be thought of as the software through which you manage your accounts and assets**: in other words, MetaMask.
* **MetaMask can import one Secret Recovery Phrase, and any number of private keys**. It cannot, however, hold more than one Secret Recovery Phrase at a time.
* **Your account(s) are not the same thing as your SRP**. They have a complex cryptographic relationship you can read more about [here](https://medium.com/mycrypto/the-journey-from-mnemonic-phrase-to-address-6c5e86e11e14), though you don't *need* to understand it. What you *do* need to understand is that your accounts are derived from—created using—your Secret Recovery Phrase, and are therefore bound to it.
* **Each account is represented by a public address**.
* **Your SRP does not have a public address.** And there is no such thing as a "wallet address". What your SRP does have, though, is one or more accounts derived from it (starting with 'Account 1', named so by default), each of which has its own public address (and corresponding private key).


In summary: each MetaMask address you have (which leads to an *account*) is derived from a Secret Recovery Phrase (which you import into your *wallet*). 


For more information on this topic, see our article [*What's the difference between a wallet and an account?*](https://support.metamask.io/hc/en-us/articles/13466457757211) 


 


Why would I need multiple SRPs?
-------------------------------


* **Security**. If you have multiple SRPs, one of them becoming compromised doesn't mean you have lost access to all of your accounts. You haven't placed all your eggs in one basket.
* **Privacy**. Even though you can [derive multiple accounts from one Secret Recovery Phrase](https://support.metamask.io/hc/en-us/articles/360015289452), you might want to further 'sandbox' your digital identities by creating an entirely new SRP. This way you can almost completely anonymize your activity (assuming the addresses have not been linked to you through KYC, somewhere).
* **Professional use cases**. Maybe you use one wallet for professional purposes—e.g. as a developer, or part of an organisation with web3 involvement—and another for personal use. It's wise to keep these separate. Equally, separating wallets could be useful for tax purposes, if, for whatever reason, you need to report different holdings and activity to different tax authorities.
* **Using different types of MetaMask**. MetaMask comes in three flavors: regular (orange fox), [Flask](https://metamask.io/flask/) (purple, for developers), and [Institutional](https://metamask.io/institutions/) (blue). Each variety requires installing a separate extension in your browser. It's possible that you want to use a combination of two (or even three?!) of MetaMask's different types concurrently — for that, you'd need to have multiple instances of MetaMask.


### Can I have multiple types of MetaMask installed in the same browser?


No — you can only have one.


Having more than one type of MetaMask—and, typically, any other wallet extension—active in your browser simultaneously will cause problems, and none of them will work correctly. To address this problem, either deactivate (or turn 'off') the additional extensions until you only have one remaining, or, as we're about to discuss, use multiple browsers or browser profiles to access them separately.



#### EIP 6963: Multi Wallet Discovery


MetaMask now supports EIP 6963, which, when implemented by dapps, means you can choose which browser extension wallet you want to use. This addresses a situation where, without EIP 6963 implementation, wallets would compete to be identified.


This means the problem described above—multiple extension wallets being unable to peacefully coexist—should now become rarer. Naturally, though, this depends on the rate at which dapps build EIP 6963 into their sites. 


Either way, you still cannot have multiple types of MetaMask active simultaneously in one browser profile. Read more [here](https://support.metamask.io/hc/en-us/articles/20220399729435).



How to manage multiple wallets or SRPs
--------------------------------------


There are two ways you can approach this: the first is by using different browsers, and the second involves using different browser *profiles*. Let's take a look:




Different browsers Browser profiles


This option is as straightforward as it sounds: if you’ve only got two or three SRPs, then you can simply install MetaMask in several different browsers, and use a different browser for each one.


Given the open-source nature of the modern web, there’s not a definitive listing of browsers that MetaMask will or won’t work in. The browsers officially supported by MetaMask are:


* Chrome
* Firefox
* Brave
* Edge




The easiest way to manage multiple wallets or SRPs is by using browser profiles. Let’s take a look at how these work with MetaMask in Chrome, as so many browsers are based on it. Chrome’s canonical instructions are available [here](https://support.google.com/chrome/answer/2364824), and the steps are fairly simple:


1. In the top-right corner of your browser, click the profile image (it will have your Google profile image, or if you haven’t logged in, it will have a placeholder image)
2. Under that menu, at the bottom, click on ‘add’:


![Multiple MetaMask Wallets](https://support.metamask.io/hc/article_attachments/12769967416091)
3. Walk through the prompts to create the new profile; you probably don’t need to associate it with another email account, so you can just click ‘Continue without an account’:


![Multiple MetaMask Wallets](https://support.metamask.io/hc/article_attachments/12769967410459)
4. Choose a color scheme, give your profile a name that reminds you which wallet you’re going to use with it, and hit 'Done':


![Multiple MetaMask Wallets](https://support.metamask.io/hc/article_attachments/12769967617947)


Now all that’s left to do is to open a browser window in that new profile, [install MetaMask from our downloads page](https://metamask.io/download/) like you normally would, and follow [these instructions](https://support.metamask.io/hc/en-us/articles/360015289612) to restore from your SRP — or create a new one.



