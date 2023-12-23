Thanks to MetaMask's partnership with web3 security specialists [Blockaid](https://www.blockaid.io/), you can now receive transaction security alerts directly in MetaMask Extension whilst maintaining total data privacy. 


The feature is currently **only available on Ethereum mainnet**.


How to turn on Blockaid security alerts
---------------------------------------


This is an opt-in feature, so you'll need to turn it on. Head to 'Settings' by clicking the three vertical dots in the top-right corner of your wallet, and then select 'Experimental'. 


From there, flick the toggle next to 'Security alerts', under the Security category.



#### Note:


Make sure you find the right item in the settings menu: privacy-preserving security alerts are different from the experimental API-based security alerts system whose toggle is labelled as "OpenSea + Blockaid (Beta)". If you want to try out the API-based security alerts system, see our article [here](https://support.metamask.io/hc/en-us/articles/12539282795675) for more information. It's not possible to use both systems at the same time. 



How does it work?
-----------------


Together, Blockaid and MetaMask have developed a security alert system using a **privacy-preserving** system that **simulates transactions locally**, providing warnings in your MetaMask wallet if a transaction is suspected as fraudulent. 


### How does it improve security?


#### Transaction simulation


When security alerts are turned on, your transaction is simulated locally before you sign it, checking whether it could result in you losing funds.


If this check returns a positive — i.e. you're likely to lose funds due to the interaction — you'll see a "This is a deceptive request" warning displayed on the transaction confirmation screen:


![MetaMask Blockaid security alert](https://support.metamask.io/hc/article_attachments/20064734514971)


**The security alerts do not prevent you from losing funds or interacting with fraudulent dapps**. Even though a warning is displayed, you can still confirm the transaction if you choose to. 


Simulating transactions also has the advantage of preventing funds loss if a usually reputable protocol is hacked. When [balancer.fi](https://balancer.fi/) was briefly [compromised](https://rekt.news/balancer-rekt/), for example, Blockaid simulations successfully identified and flagged transactions that would have caused funds loss, even though Balancer was a trusted source.


#### Maintaining a database of fraudulent dapps


As well as simulating transactions, the security system is updated frequently with the latest Blockaid data on fraudulent dapps. The simulation system is, therefore, complemented by warnings whenever you interact with a dapp that Blockaid's continual scanning has already identified as fraudulent. 


Blockaid shares the database to a MetaMask server, which, in turn, is passed on to your MetaMask instance every few hours to make sure your wallet is up to date with the latest threats. 


### Maximizing your privacy


The local simulation process means the credentials of your MetaMask account, your device, and your internet connection (such as IP address) do not need to be exposed to check the transaction. The only external communication is requesting the latest on-chain data from your node provider to get the latest context for the transaction. 


Your transaction therefore ***never leaves your wallet*** until you sign it. 


Additionally, the database of fraudulent sites is configured without any reliance on third parties, so you can be confident in benefiting from the latest web3 security intel without needing to expose any personal information about your device, browser, internet, or MetaMask accounts. 


 

