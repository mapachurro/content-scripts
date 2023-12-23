
Network name
Avalanche (C-Chain)
Token
AVAX
RPC
https://api.avax.network/ext/bc/C/rpc
Chain ID
43114
Block explorer
[Snowtrace](https://snowtrace.io/)
Website
avax.network

Avalanche is an ecosystem of multiple networks, designed to run smart contracts (similarly to Ethereum). The three networks include:


* The Exchange Chain (X-Chain), which is used for simple transactions
* The Platform Chain (P-Chain), for staking and validator responsibilities
* The Contract Chain (C-Chain), which you'll need to use to interact with dapps.


Additionally, there is also a Primary Network, which validates each of these blockchains. **It is the last of this trio, the C-Chain, which is EVM-compatible, and the network you'll connect to using MetaMask**. 


The key distinguishing feature of Avalanche is its [consensus protocol](https://docs.avax.network/#:~:text=Avalanche%20Consensus%20Protocol,of%20conflicting%20transactions.), which works through validators querying groups of *other*validators whether a transaction should be accepted as valid until consensus is reached. This system is implemented on Avalanche's three networks in the form of the '[Snowman](https://docs.avax.network/#:~:text=Snowman%20Consensus%20Protocol,Snowman%20consensus%20protocol.)' consensus protocol and expedites block validation. 


Supported by these mechanisms, Avalanche's headline features include:


* >4,500tps (transactions per second) throughput capacity
* <2s transaction finality
* Proof-of-stake consensus mechanism
* Thousands of nodes, meaning the network is well decentralized.


The Avalanche team also prioritise interoperability, making the network easier for developers to build on and for users to access. For example, it shares its smart contract programming language, Solidity, with Ethereum. 


Its [ecosystem](https://ecosystem.avax.network/marketplace) also includes a range of dapps, including decentralized and centralized exchanges, DeFi platforms and NFTs. 


To perform any kind of transaction on Avalanche, you will need sufficient quantities of its native token, AVAX, in your wallet. 


 


**Using Avalanche**
-------------------




**Adding Avalanche to MetaMask**

Adding the network is an essential first step to interacting with Avalanche. There are two ways to do this: 


1. [Add it using Chainlist](https://support.metamask.io/hc/en-us/articles/360058992772-Add-a-network-using-Chainlist-Extension-or-Mobile-).
2. [Add it manually](https://support.metamask.io/hc/en-us/articles/360043227612-How-to-add-a-custom-network-RPC). The network details are at the top of this article and available via various Avalanche sources (such as [this one](https://support.avax.network/en/articles/4626956-how-do-i-set-up-metamask-on-avalanche)).


Avalanche have also produced a video tutorial on adding the network that you can find [here](https://support.avax.network/en/articles/4626956-how-do-i-set-up-metamask-on-avalanche). 





**How do I switch to Avalanche in MetaMask?**

Please note the below instructions assume you have already added Avalanche network to your MetaMask (see above). 




Mobile Extension

On your wallet page, find where it says the current network you're connected to at the top of the screen. Tap here to select Avalanche from the networks you've already added.
![MetaMask Avalanche network mobile](https://support.metamask.io/hc/article_attachments/17281223715227) 




Select the drop-down arrow in the top left corner of the app -- it will currently display the network you're connected to, such as 'Ethereum Mainnet', or any other you used last. Scroll through the menu until you find the Avalanche network, then click on it to switch.


![MetaMask Avalanche network extension](https://support.metamask.io/hc/article_attachments/17281177010331)







**Is my Avalanche address different from my MetaMask address?**

Firstly, and for clarity: **you can interact with the majority of dapps on Avalanche C-Chain using MetaMask**. In a lot of cases, you don't need the Avalanche Wallet.


However, if you want to access the X-Chain or P-Chain, you will need the [Avalanche Wallet](https://wallet.avax.network/). Due to the triplicate structure of Avalanche, this single wallet has three addresses -- one for each of the chains. 


The C-Chain address will look like an Ethereum address, beginning with 0x. This is because the C-Chain is an instance (separate occurrence, or version of) the Ethereum Virtual Machine, which is what we mean we say it's EVM-compatible. It essentially functions the same. 


However, and despite both being compatible, the **C-Chain address of your Avalanche wallet will be different to your MetaMask address**.



#### Setting up Avalanche and MetaMask to use the same address: only for the adventurous


It is possible to have MetaMask and the Avalanche Wallet use the same address by exporting your private key from MetaMask and using it to sign into the Avalanche Wallet. We do not recommend this process unless you are aware of the risk involved and know what you're doing. See [here](https://support.avax.network/en/articles/5307228-how-to-send-avax-from-metamask-to-an-exchange#:~:text=Alternatively%2C%20you%20can,access%20your%20funds!) for a how-to from Avalanche, and our [guide](https://support.metamask.io/hc/en-us/articles/360015289632-How-to-Export-an-Account-Private-Key) to the process for further information. Anyone can access your account if they have your private key, so if you do export it -- be careful. Also, be **extremely** wary of anyone asking you to export your private key and give it to them. Our official support channels will never ask your for your private key/Secret Recovery Phrase.



**Never try and send transactions from any other Avalanche chains (X-Chain or P-Chain) to your MetaMask.** You will lose the tokens and not be able to get them back, as these are incompatible blockchains. Always get these assets onto the C-Chain and then bridge them over. 





**Using the Avalanche bridge**

Avalanche's [official bridge](https://bridge.avax.network/) can be used to move ERC-20 tokens to and from the Avalanche C-Chain. It is **only compatible with Ethereum mainnet**. 


You can also use the bridging options at the [MetaMask Portfolio Dapp](https://portfolio.metamask.io/bridge). 


This [video tutorial](https://www.youtube.com/watch?v=RLnNMfINwS0) by Avalanche for using the official bridge is very useful. In short:


1. Access the [bridge](https://bridge.avax.network/).
2. Connect your MetaMask. Make sure you select the account you want to use.
3. Select which ERC-20 token you'd like bridge across, and input the amount. Make sure you have sufficient ETH in your wallet to pay for the transaction (the cost is displayed in the interface).
4. The MetaMask transaction approval window will appear. Make sure you're happy with the details, and click confirm.
5. You'll be taken to a confirmations page that displays the status of your transaction in real time. As the video tutorial explains, there is also a link here to MetaMask which streamlines adding the bridged token to your MetaMask on the Avalanche network.
6. Once the tokens are bridged, they will appear in your MetaMask wallet, provided you have selected the Avalanche Network and added the token (see step 5).


All bridged ERC-20 tokens gain the suffix **.e** on Avalanche, indicating that they have come from Ethereum -- USDT would become USDT.e, for example. These are known as 'AB' (Avalanche Bridge) tokens. 


**If you have AVAX on Avalanche that you want to move to MetaMask, you'll need to**:


1. Make sure the AVAX is on the C-Chain. If it isn't, perform a cross-chain transfer in your Avalanche Wallet to get it there.
2. Transfer the tokens to your MetaMask address.
3. Use the bridge, following the process above.
4. If completed successfully, the bridged tokens will appear in your MetaMask, back on Ethereum.





**Can I bridge tokens from other networks (e.g. BSC, Polygon) to Avalanche?**

Yes. However, you will have to use an unofficial bridge; a few multi-chain bridge options are listed below. 


**Avalanche's official bridge only supports Ethereum <-> Avalanche C-Chain**. Please note this list does not constitute an endorsement of or affiliation with any of these platforms.


* [Multichain](https://app.multichain.org/#/router) (formerly AnySwap)
* [xPollinate](https://xpollinate.io/)
* [Rubic](https://app.rubic.exchange/).


Always make sure you know what you are doing before you sign any transactions on these platforms. Check their FAQs and support pages if unsure, and consider sending trial transactions to start with.





**How do I move AVAX I bought on an exchange to MetaMask?**

Generally, when you buy AVAX on an exchange, your AVAX will be on one of two networks: the X-Chain or the C-Chain.  



#### Do not send tokens straight from an exchange to MetaMask using the X-Chain


You will lose your tokens.



**MetaMask only works with the Avalanche C-Chain**, which is EVM-compatible. Some exchanges, such as Binance, [only support withdrawals to the C-Chain](https://academy.binance.com/en/articles/how-to-use-the-avalanche-wallet#:~:text=Note%20that%20only%20the%20C%2DChain%20is%20compatible%20with%20the%20Binance%20exchange.%20You%20can%20only%20use%20the%20C%2DChain%20to%20transfer%20AVAX%20from%20Binance%20to%20your%20Avalanche%20Wallet.%20Be%20careful!%20If%20you%20select%20the%20wrong%20chain%2C%20you%20might%20lose%20your%20tokens.). Always check these details before making any transactions. Consider sending test transactions of small quantities if you're unsure.


If your exchange does not support C-Chain, and instead uses the X-Chain, to get your AVAX on MetaMask you have to move tokens from one Avalanche network to another using the [Avalanche Wallet](https://wallet.avax.network/).


Within the Avalanche wallet, find the 'Cross Chain' tab to move AVAX between the three Avalanche networks. 





**How do I send AVAX from one of the other Avalanche chains (i.e. not C-Chain) to MetaMask?**

You'll need to do a cross-chain transaction from your Avalanche Wallet.


See this [Avalanche guide](https://support.avax.network/en/articles/6169872-how-to-make-a-cross-chain-transfer-in-the-avalanche-wallet) to the process for more information. 





**I transferred AVAX to my MetaMask from my Avalanche Wallet using the bridge. Why don't I see the tokens?**

Follow the troubleshooting checklist [here](https://support.metamask.io/hc/en-us/articles/4404424659995#:~:text=1.%20I%20can%27t,tokens%20in%20MetaMask%3F): 


1. Have you selected the Avalanche network in MetaMask?
2. Did you transfer the tokens correctly, i.e. use the correct bridge and input the right addresses?
3. Have you added AVAX as a token in MetaMask?


If you're still having problems after checking through this list, contact support through the link on our [support landing page](https://support.metamask.io/hc/en-us/). 






**Relevant support articles**
-----------------------------


[User Guide: Custom networks and sidechains](https://support.metamask.io/hc/en-us/articles/4404424659995-User-Guide-Custom-networks-and-sidechains)  


[How to export an account private key](https://support.metamask.io/hc/en-us/articles/360015289632)


[ERC-20 tokens explainer](https://support.metamask.io/hc/en-us/articles/4405497827355-User-guide-Tokens#:~:text=ERC%2D20%20Tokens,lose%20them%20forever.)


[How to add unlisted tokens (custom tokens) in MetaMask](https://support.metamask.io/hc/en-us/articles/360015489031-How-to-add-unlisted-tokens-custom-tokens-in-MetaMask)


 


**Useful resources**
--------------------


[Avalanche help center](https://support.avax.network/en/) (user-focused)


[Avalanche docs](https://docs.avax.network/) (developer-focused)


[Avalanche Bridge official tutorial videos](https://www.youtube.com/playlist?list=PLRHl-ulWK4-FPRA7SS1OrCOC8cOc2K8sP)


[Avalanche Bridge FAQ](https://docs.avax.network/learn/avalanche-bridge-faq/)


[Pangolin Getting Started guide](https://pangolin.exchange/tutorials/getting-started#set-up-metamask) (Pangolin is a decentralized exchange on Avalanche)

