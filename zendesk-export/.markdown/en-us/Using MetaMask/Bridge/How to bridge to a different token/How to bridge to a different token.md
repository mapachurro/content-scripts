You can now use the MetaMask Portfolio Bridge to not only move your tokens to a different network, but swap them into a different token of your choice, all as part of the same transaction. 



#### Note:


You might see this practice referred to elsewhere as "cross-chain swaps".



This means a process that would normally require up to three transactions is all rolled into one: you can bridge and swap simultaneously, saving you time and gas fees.


Additionally, this feature significantly increases the number of tokens available to bridge. Previously it was only possible to bridge a select number of native tokens and stablecoins. Now, If the token pair is available for a swap on our providers' protocols and has sufficient liquidity, you can bridge to it.  


How to bridge to a different token
----------------------------------


The bridging process is *almost* identical to the standard bridging process (moving a token to its equivalent on another chain). All you need to do differently to bridge to a different token is to select it when configuring your transfer. Here's how to do it:


1. Navigate to [portfolio.metamask.io/bridge](https://portfolio.metamask.io/bridge), and make sure your wallet is connected. Select the account that contains the tokens you want to bridge.
2. Select the network that your preferred source token is on, and then choose the token underneath 'You send':


![MetaMask Portfolio bridge select send token](https://support.metamask.io/hc/article_attachments/20032391130651)
3. Select the destination network. 


As a wise man (?) once said: "This is where the fun begins!". The "fun" being that you can now select the token you want to swap to by opening the dropdown menu underneath 'You receive':


![MetaMask Portfolio bridge select received token](https://support.metamask.io/hc/article_attachments/20032391136283)


Choose your preferred token from the list, and the dapp will start sourcing quotes.
4. After a short wait, the best value quote will be displayed. If you're happy with the quote, you can:


	* **Confirm** the bridge, if you're transferring a network/native token such as ETH, or;
	* **Approve the token**, if you're bridging an ERC-20 token or equivalent.Approving a token enables Portfolio to access the relevant tokens in your account and include them in the transaction. You can expand the quote details by hitting the drop-down arrow on the right, or select 'Choose a different quote' to take a look at your other options:


*You can read more about token approvals [here](https://support.metamask.io/hc/en-us/articles/6174898326683), and setting spending caps for approvals [here](https://support.metamask.io/hc/en-us/articles/6055177143579).*


![MetaMask Portfolio bridge review quote](https://support.metamask.io/hc/article_attachments/20032400208923)


Click 'Approve token' or 'Confirm' to proceed.


![MetaMask Portfolio bridge confirm](https://support.metamask.io/hc/article_attachments/20032391139099)
5. You're now ready to submit the transaction using MetaMask. Follow the prompts in your wallet to sign the transaction and complete the process.


 


FAQs
----




**How does it work?**

Multi-step bridging resembles a normal transaction using the Bridge feature in MetaMask Portfolio, but with swap transactions added either side of the actual bridge transaction. Crucially, however, Portfolio bundles all of these actions into one transaction in MetaMask, so you only need to sign once.


Just like with a regular bridge transfer using Portfolio, the bridging and swapping involved in your transfer are completed by our bridge aggregators, LI.FI and Socket.





**How much does it cost?**
The fees you will pay on each transaction include:
* The gas fee (*not*collected by MetaMask)
* The MetaMask fee of 0.875%, calculated from the original value of tokens you want to bridge.
* The difference in the value of the token you send vs. the value of tokens you receive on the destination network. This includes any fees charged by the bridge providers, as well as gas fees on the destination network.


The total you'll receive on the destination network is displayed in your quote. Note that the MetaMask fee is calculated first, and other costs are then subtracted from the remaining value in order to reach the final amount you'll receive.





**How long does the transaction take?**
The estimated transaction time is displayed in the quote before you confirm. The estimate varies based on the tokens, networks, and bridge providers involved in the transaction. 
If you’ve already waited over three hours and your transfer is still in progress, please contact MetaMask Support by clicking the ‘Support’ button in the bottom left of the dapp. 


**Does this feature use MetaMask Swaps?**
No. The token swaps executed as part of multi-step bridging are carried out by LI.FI and Socket. 


**What tokens can I bridge?**

Before multi-step bridging, you could only use the MetaMask Portfolio Bridge feature for a handful of native tokens and networks, and some stablecoins. Now, you can bridge *to*any token available on our aggregators' exchanges. If the token has sufficient liquidity and is swappable, you can bridge to it.


For this reason, we cannot provide an exhaustive list of what you can and cannot bridge. For the most up-to-date list, input your intended transfer into Portfolio and see what's available. 





**What providers are fulfilling the transaction?**
Multi-step bridge transfers are completed using our bridge aggregators, LI.FI and Socket. They, in turn, use various bridge and swap providers to construct quotes. 

