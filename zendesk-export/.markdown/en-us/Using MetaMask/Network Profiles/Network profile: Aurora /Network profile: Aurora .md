
Network name
Aurora
Token
ETH
RPC
[https://mainnet.aurora.dev](https://mainnet.aurora.dev/)
Chain ID
1313161554
Block explorer

[Aurorascan](https://aurorascan.dev/) 
Website

[aurora.dev](https://aurora.dev/) 

Aurora is a version of the [Ethereum Virtual Machine](https://ethereum.org/en/developers/docs/evm/) (EVM) that exists on [NEAR Protocol](https://near.org/). Although NEAR and Aurora are developed by the same team, Aurora is best conceptualized as a network in its own right due to its EVM compatibility. 


Aurora's objective is to function similarly to NEAR itself, just with the key difference that it can be used to host decentralized applications (dapps) and run smart contracts which were originally written on Ethereum. This makes it highly appealing for developers: in their [own words](https://doc.aurora.dev/#:~:text=provides%20the%20Ethereum%201.0%20development%20experience%2C%20with%20layer%2D2%2Dlike%20speed%20and%20scalability), Aurora "provides the Ethereum 1.0 development experience, with layer-2-like speed and scalability." Creating an appealing space for developers means a higher-quality and more diverse ecosystem, which, in turn, draws in users.


In parallel to smoothing the transition for developers, Aurora is also designed to present a relatively flat learning curve for those more familiar with Ethereum, principally through its native token choice. Rather than having its own native token (the token you use to pay gas fees) like many layer 1 chains, **Aurora simply uses ETH**. 


Since it resides on NEAR, Aurora retains many of the former's core features. These include:


* Low transaction costs (gas fees), typically [$0.02 per transaction](https://doc.aurora.dev/#:~:text=Gas%20fees%E2%80%8B,Transaction%20cost%20~%240.02)
* Faster transaction finality of <3 seconds
* Carbon neutrality.


Another key feature of Aurora is the fact that is governed by [AuroraDAO](https://aurora.dev/dao), a decentralized autonomous organization which votes on high-level matters relating to the network. Governance uses the [AURORA token](https://aurora.dev/tokenomics) (though, as we mentioned earlier, Aurora's *native token* for gas fees is ETH). 


There's also a membership platform available on Aurora called [Aurora+](https://aurora.plus/), promising 50 free transactions per month, AURORA staking, and potential governance involvement.   



**Using Aurora**
----------------




**How do I add Aurora to MetaMask?**

Simply follow our instructions for adding networks [here](https://support.metamask.io/hc/en-us/articles/360043227612). The details you'll need to add it manually, including RPC, chain ID, and token are detailed at the top of this page. 





**What's the relationship between Aurora and NEAR? Why can't I use NEAR with MetaMask?**

Aurora is a version of the Ethereum Virtual Machine that runs *on NEAR,* and is developed by the NEAR Protocol team.


NEAR, by contrast, is a distinct layer-1 blockchain, completely separate from Ethereum, and so cannot be used with MetaMask (which is only usable with EVM-compatible networks). There is a useful graphic [here](https://doc.aurora.dev/) explaining how Aurora interacts with NEAR for each transaction. 





**How do I bridge tokens to and from Aurora?**

The NEAR Protocol team have built the [Rainbow Bridge](https://rainbowbridge.app/transfer) specifically to support transactions between Ethereum mainnet, Aurora, and NEAR.


To use it, head to the site and connect the MetaMask account you want to use and the Aurora or NEAR address you want to transact with.


Bear in mind that not all transfer directions cost the same. As the [Rainbow Bridge FAQs](https://rainbowbridge.app/faq) explain:


*Transfers **between NEAR and Aurora** require a **single transaction,** **cost a few cents** and happen instantaneously.*


*Transfers **from Ethereum** require a **single transaction**, and happen in **about 10 minutes**. The cost will be estimated in MetaMask prior to confirming the transaction.*


*Transfers **to Ethereum**, however, involve **two transactions** — the **kick-off** on Aurora or NEAR, and the **finalization** on Ethereum. The finalization can take up to **16 hours**, and its cost will depend on gas prices at that time, and are therefore **unpredictable**.*


You can read more about how the bridge works [here](https://help.aurora.dev/article/38-how-do-i-confirm-a-transaction) and [here](https://doc.aurora.dev/bridge/bridge-overview).





**Is ETH on Aurora the same as ETH on Ethereum mainnet?**

No.


Although ETH is the native token of both networks, you cannot simply send your ETH from Ethereum mainnet straight to Aurora — it must be bridged first. See the FAQ on bridging immediately above.





**Is my public address the same when using Aurora on MetaMask?**

Yes.


Since Aurora is EVM-compatible, you can use the same Ethereum address (i.e. the type you have in MetaMask) as an existing MetaMask account.


Once you've added Aurora to MetaMask, notice how your address stays the same even when you switch between networks. This means that even if you send some ETH to your MetaMask and haven't bridged it onto the correct network (one of Ethereum mainnet or Aurora), it will still be retrievable in your MetaMask by just switching to the network it's on.


[NEAR has a completely different approach to public addresses.](https://docs.near.org/docs/concepts/account)





**Does Infura's partnership with NEAR mean I can access NEAR with MetaMask?**

The [announcement](https://consensys.net/blog/press-release/leading-ethereum-development-platform-infura-partners-with-near-protocol-marking-expansion-as-a-multi-chain-connector/) simply means that developers can use Infura to easily access the NEAR blockchain.


Although, by default, [MetaMask uses Infura](https://support.metamask.io/hc/en-us/articles/4417315392795) to connect to the blockchain, Infura's compatibility with NEAR does not mean MetaMask does. MetaMask and Infura are different products, and the former can only be used with EVM-compatible networks.






**Useful resources**
--------------------


[Aurora knowledge base](https://help.aurora.dev/) (aimed at users)


[Aurora docs](https://doc.aurora.dev/) (aimed at developers)


[Rainbow Bridge](https://rainbowbridge.app/transfer) (official Ethereum <-> Aurora <-> NEAR bridge developed by NEAR)


[Aurora ecosystem](https://aurora.dev/ecosystem)

