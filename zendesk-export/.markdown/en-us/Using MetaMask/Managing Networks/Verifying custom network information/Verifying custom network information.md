When a website requests that you add a custom network to MetaMask, you are presented with the information MetaMask will use to interact with the network. MetaMask performs some basic validation of this information, and will warn you if anything seems wrong or unusual. MetaMask will also prevent the same network from being added more than once. However, **MetaMask does not verify custom networks**, and even if MetaMask’s validation checks out, the network could be malicious or misrepresented by the website that requested it.


**For more information and an introduction to custom networks, see our User Guide [here](https://support.metamask.io/hc/en-us/articles/4404424659995).**


Just like it’s your responsibility to verify the Ethereum addresses you transact with, it is also your responsibility to verify any custom networks you add to MetaMask. In this article, we will share some advice about how to do that.


When a website makes a request to add a custom network, MetaMask displays the following confirmation:


![MetaMask add new network approval](https://support.metamask.io/hc/article_attachments/16213839779227)


 


This confirmation shows **the network information that the website provided**. *There is no guarantee that this information is correct*. Therefore, you should trust the information to the same degree that you trust the website.


If you click “View all details” in the confirmation, you can see all of the network information provided by the website, which includes:


* **Network Name**: The name that MetaMask will associate with the network.
* **Network URL:** The URL that MetaMask will use to access the network.
* **Chain ID:** The chain ID that MetaMask will use to sign transactions for the network.
* **Currency Symbol:** The currency symbol that MetaMask will use for the network’s native currency.
	+ For example, for the Ethereum Mainnet, the currency symbol is ETH, and for the Gnosis Chain, the symbol is xDAI (retained following their merger).
* **Block Explorer URL (optional):** The URL that MetaMask will direct you to in order to inspect your accounts, transactions etc. The equivalent of [etherscan.io](https://etherscan.io), but for the network in question.


If you are for any reason unsure about the correctness of the network information, we recommend that you take the following steps to verify it:


* Visit [Chainlist](https://chainlist.wtf/) and search for the provided chain ID and/or name of the network. If MetaMask is saying that some information isn’t matching, you should be able to identify the problem on Chainlist. If the custom network is not listed at all on Chainlist, it is either extremely new, or possibly of questionable quality.
* Google the name of the network, and try to answer the following questions. The more you can answer with “yes”, the more reason you have to believe that the network is legitimate. Be advised that there are many scams and fake social media channels, especially on Telegram.
+ Does the network have a website? If so, does it seem legitimate? Does it list the network details?
+ Does the network have an official Twitter or other social media account? Do they have a lot of followers? Do they seem reputable? What are people saying about the network?
+ Can you identify any of the people who maintain the network? Are they visible on social media? Do they have a lot of followers?
+ Are there any news articles about the network?


For most networks, it should be pretty obvious whether they are legitimate or not, and whether the website is providing accurate information or not. If you’re still unsure after completing these steps, you should reject the request to add the network, do more research, and perhaps try again later.

