
#### Want to bridge to a network you've never used before? Read this first!


Before you move your funds onto another network, remember that you'll need **native tokens** on that network to use them further. One option is to buy them through our [Buy feature](https://support.metamask.io/hc/en-us/articles/360058239311).



 


#### Contents:


* [What is a bridge?](#h_01GGSRENNBAPG0GRC02PADY8MC)
* [Where can I find the bridge?](#h_01GGSREV2RPPVYTKXJY5S4ZGBC)
* [How does it work?](#h_01GGSQCS0PPG6YDH964VC6ZJNR)
* [What are the benefits?](#h_01GGSRF4NYJTP6R01WGJBEWQE3)
* [FAQs](#h_01GGSRF9FCZR53YCNSME5TMMY2)


 


The Bridge feature in MetaMask Portfolio does exactly what it says on the tin: it pulls together bridging quotes for you to choose from. From here, you can pick the best quote for you and move your tokens to the network you need.


Think of it as an aggregator of aggregators, or meta-aggregator. It’s analogous to visiting travel sites that find you the cheapest flight from numerous airlines, or — slightly closer to home — using MetaMask Swaps to find you the cheapest token swap quote from decentralized exchanges.


 


What is a bridge?
-----------------


A bridge allows you to transfer your tokens between different blockchain networks. For example, perhaps you want to use a dapp or a game on the Polygon network, but most of your funds are on Ethereum mainnet. You can use a bridge to transfer some ETH, USDC, or other tokens from Ethereum to Polygon — retaining their value — and start to use them with dapps on Polygon.


### To dive a bit deeper:


At their most basic level, bridges are platforms with contracts on the chains you're transferring to and from. Though the exact system varies, each bridge has a mechanism to validate your deposit on one network and issue equivalent tokens on another network.


When you request to move Ethereum from Mainnet to Polygon, for example, the first thing the bridge will need to do is have you deposit the ETH to the bridge. The bridge will prompt you to sign a transaction to send the tokens to their address (for tokens other than ETH, this assumes you've already signed an approval granting it access to your tokens).


 


![MetaMask Portfolio bridge diagram](https://support.metamask.io/hc/article_attachments/15957006840347)


 


The deposit may be validated in a few different ways depending on the bridge, but this process essentially buys you the right to have your target address credited with the agreed amount of tokens (that is: the token you're bridging to). The bridge honors this request by minting or sending the tokens to the account you specified on the destination network.


 


Where can I find it?
--------------------


You can find the Bridge page in MetaMask Portfolio, available at [portfolio.metamask.io/bridge](https://portfolio.metamask.io/bridge). You can also hit the 'Bridge' button from the homepage of MetaMask Extension.


![MetaMask Portfolio Dapp Bridge](https://support.metamask.io/hc/article_attachments/12706140781211)


 


How does it work?
-----------------


The bridge takes the data you input and runs it through existing bridge aggregators. For every transaction, you’ll need a:


* Source network
* Destination network
* Token type and quantity.


Once we're finished trawling the aggregators, you’ll be presented with a recommended quote, as determined by our algorithm. If you want to choose an alternative route, you can view and select other quotes too.


Additionally, although we request your bridge transfer through an aggregator, we’re also only using the aggregators to access a select list of bridges that meet our requirements for trust minimization.


Here’s our **step-by-step guide**:


1. Make sure your [wallet is connected](https://support.metamask.io/hc/en-us/articles/8324584621083) and that you’ve selected the account that has the tokens you want to bridge.
2. Select the network from which you want to move tokens under the ‘From this network’ field.
3. Input the details of the token you want to bridge under ‘You send’. The drop-down list in this field is divided into tokens that are ‘Able to bridge’ and those that you’re ‘Unable to bridge’. The category each token belongs to depends on:
	* Whether we currently support that token
	* Whether you hold that token in your wallet.
4. Pick the network to which you want to bridge the tokens under ‘To this network’.


![MetaMask Portfolio Dapp Bridge UI](https://support.metamask.io/hc/article_attachments/13140997494299)
5. **If you're bridging to the same token:** When you input a token and an amount to send, the aggregator will start to find quotes. Once it’s done, you’ll see how much of the token you’ll receive on the destination network, and your quote is listed under ‘Recommended Bridge’ below.


**If you're bridging to a different token:** Thanks to a recent upgrade, you can receive a different token on the destination network, if you choose, by selecting a different token under 'You receive'. Read more [here](https://support.metamask.io/hc/en-us/articles/19810799583643).
6. Assess the quote and its estimated timings and fees by clicking the drop-down arrow on its right side. The quote will refresh every minute to ensure you get up-to-date information.
7. If you want to view other quotes, hit ‘Choose a different quote’ in the top-right of the quote field. Click on one to select it.
8. When you’re happy with the quote, click the ‘Select’ button. This will call up a window that asks you to sign a message using your wallet. Follow the prompt and MetaMask will open to allow you to do so, and then proceed through to initiate the bridge.


Note that you may need to approve MetaMask Portfolio's access to your tokens before you can bridge them. [Read more on token approvals here](https://support.metamask.io/hc/en-us/articles/6174898326683).


![MetaMask Portfolio Dapp Bridge UI](https://support.metamask.io/hc/article_attachments/12706619126811)


 


What are the benefits?
----------------------


We’re continually working to make MetaMask a flexible, empowering passport to access all that web3 offers. Efficiently bridging tokens with as little risk as possible is a key pillar of your independence and agency on the decentralized web, where you should have full control of how and where you manage your digital assets and identity. This is why MetaMask, in contrast to the ‘walled gardens’ of web2, will always be free, and why we cannot and will not try and stop you or penalize you if you’d prefer to conduct your activities elsewhere.


A similar logic applies to moving assets between blockchains. Enter bridging, and one of the reasons we want to provide the most seamless, accessible bridging platform we can for MetaMask users.


Here’s why we think you’ll like it:


* **We do the legwork**: No more trawling the web to find the cheapest aggregator that supports the tokens and networks you want.
* **Safety**: Only bridge using platforms which have passed our vetting process, ensuring we’re only presenting you with the most secure platforms we can find.
* **Transparency**: We will always make you aware of the risks of every transaction and provide you with our best estimates of expected duration and price.
* **Reliability**: If you can see an option in the aggregator for a certain path or token, you will be able to use it, and with a high expectation of success. We’ll never pursue choice — unsustainably adding more networks and tokens — at the cost of reliability and quality.


 


FAQs
----




**What networks are supported?**

You can bridge between:


* Ethereum mainnet
* Polygon
* BNB Smart Chain
* Avalanche
* Arbitrum
* Optimism
* Linea
* zkSync Era
* Base.





**What tokens are supported?**

We recently enabled [bridging to different tokens](https://support.metamask.io/hc/en-us/articles/19810799583643). Since this process involves swaps, **you can bridge to any token with sufficient liquidity** on the protocols we use as providers. To see what's available, please check on the [Bridge page](https://portfolio.metamask.io/bridge).





**Does MetaMask take custody of my funds at any point?**

No, we work with third parties to bridge your tokens between networks.





**Do you make money from this?**

Yes. Like MetaMask Swaps, **we apply a 0.875% fee on each transaction**. This is calculated based on the total value of the transaction before fees are subtracted.


So if you want to bridge 1,000 USDT, for example, the MetaMask fee would be 8.75 USDT, and then other fees and costs will be subtracted from the remaining 991.25 USDT.  


This means that when you use the Bridge feature, you pay:


* The MetaMask fee
* Gas fees on the source network
* The difference in the value of the token you send vs. the value of tokens you receive on the destination network. This includes any fees charged by the bridge providers, as well as gas fees on the destination network).





**I haven't received my tokens in the time I should have. What should I do?**

The time we quote is an estimate, and delays can happen for several reasons, such as a change in network conditions. In most cases, the bridge transfer is just delayed and your transfer will still go through automatically.


If you’ve already waited over three hours and your transfer is still in progress, please contact MetaMask Support by clicking the ‘Support’ button in the bottom left of the dapp. If we cannot troubleshoot the problem, we recommend that you contact the bridge’s support to look into getting your transaction unstuck.





**What aggregators and bridges do you use?**

As we described above, our platform sources bridging options through two stages:


* Aggregators, through which we access a selection of:
* Bridge providers, the platforms that actually execute the bridge.


The aggregators we use are LI.FI and Socket. The bridge providers we access through these aggregators are:


* Hop
* Connext
* Celer cBridge
* Polygon PoS Bridge
* Squid (Axelar)
* Across.





**What is the maximum transaction size?**

The maximum value you can bridge at a time is $50,000.





**Something went wrong with my transfer. What do I do?**

Don't panic! Just contact Support via the 'Support' button on MetaMask Portfolio.





**Why does it say I'm on an 'Unsupported network'?**

![Screenshot_2023-05-19_at_10.29.03.png](https://support.metamask.io/hc/article_attachments/15588488490139)


The Bridge feature automatically adopts the same network that your MetaMask wallet is set to. Make sure your wallet is set to one of the supported networks listed above, and then you will be able to bridge.




