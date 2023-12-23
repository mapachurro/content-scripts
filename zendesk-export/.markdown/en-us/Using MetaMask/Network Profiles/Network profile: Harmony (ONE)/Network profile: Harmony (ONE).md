
Network name
Harmony Mainnet
Token
ONE
RPC
https://api.harmony.one
Chain ID
1666600000
Block explorer
[explorer.harmony.one](https://explorer.harmony.one/)
Website
[harmony.one](https://www.harmony.one/)

 


Begun as a startup in 2018, Harmony is an EVM-compatible network with two core objectives: scalability and decentralization. It was the first **sharded** layer 1 (L1) network to launch using a proof-of-stake consensus mechanism.


As it is an L1 network, Harmony **uses its own token, ONE**, to pay for transactions and for validators to stake (and, in turn, receive rewards). 


Having multiple shards simply means the network is partitioned into distinct sections to increase potential throughput. Harmony has four shards, with its nodes distributed equally between them. Sharding is one method of solving the 'blockchain trilemma' of simultaneously achieving scalability, security and decentralization. 


Harmony's key features include:


* **Secure random state sharding**. Network validators are randomly shuffled between shards to maximize security.
* **Two-second finality**, i.e. the ability to confirm blocks within two seconds. They achieve this through their [Fast Byzantine Fault Tolerance (FBFT) consensus algorithm,](https://docs.harmony.one/home/general/technology/consensus) which allows the network to agree on blocks extremely quickly. FBFT's name derives from the [Byzantine Fault problem](https://en.wikipedia.org/wiki/Byzantine_fault) (a.k.a. The Byzantine Generals Problem), which confronts the challenge of how to achieve consensus between multiple parties when some of them are potentially unreliable.
* **Effective Proof-of-Stake (EPoS) consensus** **mechanism**. Designed specifically for the network's sharded design, this system involves electing validators based on their stake: to earn staking rewards, validators need to run more nodes, ensuring each validator does their fair share. EPoS also evenly distributes stakes across shards to ensure a consistent level of security across the network.


Harmony also has a growing ecosystem of dapps, has its own native wallet, and has developed [bridges](https://bridge.harmony.one/erc20) between its own network, Ethereum and BSC. 


 


**Using Harmony**
-----------------




**How do I use Harmony with MetaMask?**

Harmony ONE is already configured as a popular network in MetaMask, so adding it is straightforward. Click 'Add network' and head to the 'Add popular networks' area (instructions [here](https://support.metamask.io/hc/en-us/articles/360043227612)). From here, adding it to MetaMask should only take a few clicks or taps.


Once you're on the correct network, if your tokens aren't appearing, make sure you [add the token](https://support.metamask.io/hc/en-us/articles/360015489031) you want. 


To get tokens onto Harmony, you must then bridge them using the official Harmony bridge. See below for more information. 





**Are my MetaMask address and my Harmony address the same? Which do I need?**

In a way. Your Ethereum address has a corresponding Harmony address -- but you should not regard them as interchangeable. 


Ethereum addresses all begin with the prefix '0x', whereas Harmony addresses begin with 'one1'. You can find your corresponding address using the [Harmony block explorer](https://explorer.harmony.one/); just find the ONE/ETH switch in the top right of the page. 


You should **always use the Ethereum address format on MetaMask** when using the Harmony network. Only use the Harmony address formats when using the Harmony ONE Wallet. For further information, see [here](https://blog.harmony.one/launching-full-ethereum-compatibility-on-harmony/#:~:text=Note%3A%20when%20using,0x%E2%80%99)%20address%20format.). 





**What token do I need?**

ONE is the network's native token. Similarly to how gas fees on Ethereum mainnet are paid in ETH, you need ONE tokens to pay for transactions on Harmony. 


ONE tokens are also used for staking (and associated rewards) and governance. 





**Can I send tokens directly from Ethereum to the Harmony One network?**

No.


You should never send tokens to an address on another network without bridging, otherwise you risk permanently losing the tokens. Even though Harmony One and Ethereum are interoperable by virtue of the former being an EVM-compatible network, they are different blockchains, and you can't move assets between without going through the bridge.





**Using the Harmony 'Horizon' bridge**

Head to the bridge at [bridge.harmony.one](https://bridge.harmony.one/), Horizon.


The bridge works with both Ethereum and BNB Smart Chain (BSC). Although we don't need to get into the technical details, it's essentially a series of smart contracts which 'lock' the original asset (the one you want to transfer to Harmony) and mint an identical quantity of a bridged asset. 10 BUSD bridged from Ethereum will become 10 1BUSD, with the '1' prefix indicating it is a Harmony HRC-20 token that came from Ethereum. 10 BUSD that come from BSC, meanwhile, will become 10 bscBUSD on Harmony, with the prefix similarly indicative of its source.


When you access the page, you'll see you can choose between a range of popular tokens on both BSC and Ethereum. To use the bridge, you need to:


**Connect your wallets**. You will need to connect a source wallet, from which to send the tokens, and a recipient wallet. MetaMask can function as both. 


* If you want to transfer from Harmony back to Ethereum or BSC, you can either select MetaMask (make sure you have the Harmony network selected) or your ONE wallet.


![mceclip0.png](https://support.metamask.io/hc/article_attachments/4416937968283/mceclip0.png)


**Make sure you've selected the right bridging direction in the top left**: 


![mceclip1.png](https://support.metamask.io/hc/article_attachments/4416938039963/mceclip1.png)


**Select the token or token type you want to bridge and input the desired quantity**. 


Then **add the recipient wallet address.**If your MetaMask is already connected, there will be an option to insert the address of the connected account. When you click 'Continue', the transaction details will be displayed for you to confirm, and then you will be prompted to sign the transactions using your wallet. 


Note that **you can only withdraw from Harmony to the network your tokens originally came from**. For example, you can move tokens from Ethereum to Harmony and back, but cannot withdraw those same tokens from Harmony onto BSC. 





 **What are HRC-20, HRC-1155 and HRC-721 tokens? How do they differ from Ethereum token standards?**

As it is EVM-compatible, Harmony deliberately mirrors the token types available on Ethereum. HRC-20, for example, is equivalent ERC-20 tokens, and so on. 


These token types reflect what your tokens will become once bridged over to Harmony: for example, USDT, an ERC-20 stablecoin, will become a HRC-20 token on Harmony. 





**How do I get ONE tokens?**

You can buy ONE from several major exchanges — check the token's markets page on [Coingecko](https://www.coingecko.com/en/coins/harmony#markets) or [Coinmarketcap](https://coinmarketcap.com/currencies/harmony/markets/) to review your options.


You can also buy ONE directly in MetaMask Portfolio, [here](https://portfolio.metamask.io/buy/). Another method is to buy directly on Harmony: <https://www.harmony.one/buy> 


When transferring the ONE you have purchased out of the exchange wallet, make sure to convert to the correct address type. If you're sending to MetaMask, you will need to select the Ethereum address. See above.





### 


**Relevant support articles**
-----------------------------


[User Guide: Custom networks and sidechains](https://support.metamask.io/hc/en-us/articles/4404424659995-User-Guide-Custom-networks-and-sidechains)


[Add a network using Chainlist (Extension or Mobile)](https://support.metamask.io/hc/en-us/articles/360058992772-Add-a-network-using-Chainlist-Extension-or-Mobile-)


 


**Useful resources**
--------------------


[Harmony Bridge FAQ](https://bridge.harmony.one/faq)


[Messari report on Harmony](https://open.harmony.one/messaris-report-on-one) (useful summary)


[Harmony docs](https://docs.harmony.one/home/) (concise and broken down into categories)


 

