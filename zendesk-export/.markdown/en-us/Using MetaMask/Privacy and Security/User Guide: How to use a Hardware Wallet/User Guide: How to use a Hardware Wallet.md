#### Have you recently acquired a hardware wallet? Are you considering it?








MetaMask recommends the usage of hardware wallets for long-term crypto-asset storage. For an explanation as to what a hardware wallet is, and a directory of the product lines that MetaMask officially supports, see our [Hardware Wallet Hub](https://support.metamask.io/hc/en-us/articles/4408552261275-Hardware-Wallet-Hub).


*Once you've got your hands on a hardware wallet, follow the instructions below to get the most security and functionality out of your device.*


How to configure your hardware wallet
-------------------------------------


#### Regardless of whether you're HODLing, NFT swapping, DAO building or DeFi degen-ing, MetaMask recommends you follow this configuration pattern for maximum security:


1. **Create a *new Secret Recovery Phrase / Seed Phrase* on your Hardware Wallet.** A lot of hardware wallets offer you the option to "import a seed phrase", from MetaMask, for example. While that might sound like what you want to do, *it's not*.  
  

#### *The whole point of having a Hardware Wallet is having a device whose Secret Recovery Phrase is never connected to the internet, even if it's encrypted like it is in MetaMask.*


To get that truly "[airgapped](https://www.techopedia.com/definition/17037/air-gap)" security, you need to create a *new* SRP through your hardware wallet. A few things to remember:  

	* Often, **hardware wallets generate 24-word SRPs**, rather than the 12 you get with MetaMask. Each one of those words, and the order they're in, is crucial!
	* Just like with your SRP from MetaMask, **never share it with anyone**
	* Again, just like with MetaMask, **back it up in a secure location, or several, always offline and never in anyone's cloud.**
2. **Import the accounts from the hardware wallet that you want to use into MetaMask**. Just like with an SRP that you create through MetaMask, your new SRP on your hardware wallet can create a very large number of accounts. Once you've got your SRP all set up on your hardware wallet, import the accounts you want to use in MetaMask following the manufacturer's instructions — check out our [Hardware Wallet Hub](https://support.metamask.io/hc/en-us/articles/4408552261275-Hardware-Wallet-Hub) for links.
3. **Transfer the assets you wish to secure with your hardware wallet** from your existing MetaMask account(s) to the hardware wallet account(s). This is fairly straightforward—you're sending things from one account to another—but here are some tips:  

	* You might not be able to transfer *all* of your ETH out of your original account, because you'll have to pay the gas fee to send the assets; the same goes for BNB, MATIC, etc., depending on the gas token of the chain you're on.
	* Additionally, you may want to leave some assets in your original wallet, depending on how often you transact, and whether you plan on carrying your hardware wallet with you.
	* **Be thoughtful with how you handle NFTs**. A lot of NFTs aren't just cool links to a .jpeg on someone's server — they might issue tokens to you every day, or allow you to play a video game, or allow you access to funds, or control your domain name. As long as your hardware wallet supports NFTs, you'll be fine in the sense that *you'll still have them*, but make sure you have them on the address, and in the wallet, where you'll be *able to use them* the way you want to.
	* If you have a lot of assets that all have to go to the same place, save some gas and check out our [Account Migration Guide.](https://support.metamask.io/hc/en-us/articles/4867408571803-Account-Migration-Guide)
4. Now that you have your assets secured offline, **get comfortable with your HWW's signing procedure**. This is, essentially, how transactions will work:  
Transaction (signature, transfer, etc.) initiated by you on dapp/online platform-->  
-->Transaction sent by MetaMask to Hardware Wallet-->  
-->Transaction signed on Hardware Wallet-->  
-->Signed transaction transferred back to MetaMask-->  
-->MetaMask sends signed transaction to the blockchain network-->  
-->Transaction is registered back at the dapp/platform


However, each hardware wallet, depending on how it is designed, will implement these steps in their own particular way. So before you find yourself in an NFT minting war, trying to authorize funds, make sure you know what to expect!


 





