### MetaMask currently supports five hardware wallets:


* AirGap Vault
* Keystone (available on both Extension and Mobile)
* Lattice
* Ledger
* Trezor.


Unless otherwise stated, these hardware wallets are only supported on MetaMask Extension. We're working to offer more MetaMask Mobile integrations when possible. 



#### Am I in the right place?


If you're looking for an explanation about what a hardware wallet is and why you should have one, keep reading.


If you're looking for support regarding your particular hardware wallet, scroll down to the corresponding section.


If you're setting up a hardware wallet for the first time, **take a look at our [User Guide](https://support.metamask.io/hc/en-us/articles/5450173968283) for our recommended configuration.** 



#### 


What is a hardware wallet? And why should I have one?
-----------------------------------------------------


Understanding hardware wallets means getting 'under the hood' of Ethereum a little bit. Let's first take a look at what we mean when we talk about a 'wallet'. At first glance, it's an intuitive concept: it's a digital container to hold digital money and other things. Just like, in a real wallet, you may have some currency and some pictures of your cat or your family; well, in your MetaMask wallet you have some currency and some CryptoKitties and an animated GIF of a zombie. Pretty similar so far.


Well, it turns out that calling it a 'wallet' is a bit of a metaphor. It's a good one in terms of how we experience it, but it doesn't accurately represent what's happening, technologically. The contents of your 'wallet' actually consists of *the assets assigned to your address on the blockchain*. When we send ETH 'to' someone, it doesn't *go*anywhere; it's simply deducted from the balance of ETH assigned to your address, and reassigned to the balance of the address you're sending it to. Remember, a public blockchain is also called *distributed ledger technology*, and all of our wallets are lines in that ledger; our balances, our holdings, are the columns, and the Ethereum Virtual Machine is our automated bookkeeper.


In this sense, MetaMask is 'simply' a web application that sends requests to the Ethereum blockchain: for information about what assets are assigned to your address; to 'send' tokens from one address to another, and so on. It does this by using your Secret Recovery Phrase.


Your public Ethereum address is one half of a pair: a *cryptographic key pair*, to be precise. The public half, your address, can be given to anyone without fear of them being able to hack in and steal your funds. The private half, the Secret Recovery Phrase (also known as a 'seed phrase'), authenticates whoever holds it as having full and complete access over the address and all accounts associated with it. **Remember: "not your keys, not your coins".**


Now, MetaMask is extremely secure, and as long as no one has access to your Secret Recovery Phrase ([you wrote it down in a safe offline location, right?](https://support.metamask.io/hc/en-us/articles/4404722782107)), your account should be secure. There are many other factors that are outside of the control of MetaMask and its security engineers: how safe your browser is, whether someone gets physical control over your computer, or takes over your computer using a virus, for example.


For this reason, we recommend that if you are storing any significant amount of value in your MetaMask wallet—or simply assets that are important to you—that you use a hardware wallet as a second line of defense. 


With all that background out of the way:



TL;DR
------


### **A hardware wallet is a physical device outside of your computer that secures your wallet's keys, and acts as a firewall between attackers and the contents of your wallet.**


In order to transact with funds secured by a hardware wallet, you will have to interact with the hardware wallet in order to approve the transaction. This way, even if someone somehow gains access to your MetaMask wallet, they will be stopped from moving things out of it.


 


 AirGap Vault
-------------


* [Connect AirGap Vault to MetaMask](https://support.airgap.it/guides/metamask/)
* [AirGap Vault - Android Play Store](https://play.google.com/store/apps/details?id=it.airgap.vault&hl=en_US&gl=US)
* [AirGap Vault - iOS App Store](https://apps.apple.com/us/app/airgap-vault-secure-secrets/id1417126841)


 Keystone
---------


* [Binding your Keystone to your MetaMask Wallet](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/bind-metamask-with-keystone)
* [How to connect Keystone to MetaMask Mobile and send ETH](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile)
* [How to use Keystone with MetaMask Mobile for dApps through Wallet Connect](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile/defi-with-metamask-mobile)
* [How to configure EVM chains on MetaMask Mobile](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile/configuring-evm-chains-on-metamask-mobile)
* [How To Benefit From Hardware Wallet Security Using Transparent QR Codes](https://consensys.net/blog/news/metamask-x-keystone-how-to-benefit-from-hardware-wallet-security-using-transparent-qr-code/)
* For an understanding of Keystone's security value-added proposition, [see here](https://blog.keyst.one/blind-signing-a-security-black-hole-for-the-ethereum-community-13f909b848b6).
* For advanced topics regarding Keystone's security features, including introducing custom entropy, [read here](https://support.keyst.one/general-navigation-guide#advanced-users).


 Lattice
--------


* For first-time Lattice users, make sure you’re properly set up: <https://gridplus.io/setup>
* See GridPlus' documentation on getting started using MetaMask and a Lattice [here](https://docs.gridplus.io/setup/metamask).


 Ledger
-------


 Ledger has broad documentation for users of MetaMask. Here are some that will help get you started:  



* [Set up and use MetaMask to access your Ledger Ethereum (ETH) account](https://support.ledger.com/hc/en-us/articles/4404366864657-Set-up-and-use-MetaMask-to-access-your-Ledger-Ethereum-ETH-account?docs=true)
* [I don't see my BEP-20 tokens in my Ledger Binance Smart Chain (BSC) account, what can I do?](https://support.ledger.com/hc/en-us/articles/4406111561617-I-don-t-see-my-BEP-20-tokens-in-my-Ledger-Binance-Smart-Chain-BSC-account-what-can-I-do-?support=true)
* [How to access your Ledger Polygon account via MetaMask](https://support.ledger.com/hc/en-us/articles/4418394184209-How-to-access-your-Ledger-Polygon-MATIC-account-via-Metamask?docs=true)



#### Having trouble connecting your Ledger to MetaMask in Firefox?


Due to changes rolled out in Firefox v112 onwards, you may have issues connecting your Ledger to MetaMask in Firefox. This is due to the connection method no longer being supported by Firefox. [Ledger support describe a temporary workaround here](https://support.ledger.com/hc/en-us/articles/10371387758493). Alternatively, you could try switching to a Chromium-based browser for using MetaMask.



 Trezor
-------


* See Trezor's documentation regarding operability with MetaMask [here](https://wiki.trezor.io/Apps:MetaMask).
