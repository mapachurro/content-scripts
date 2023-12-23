### Many users find it useful to perform a manual analysis of their accounts, checking to make sure the transactions align with what they intended.


It can be useful to see how much you spent on gas fees, how your balances rose and fell over time, etc. In accounting, **this is referred to as 'reconciliation'**.


MetaMask doesn't yet have this feature built-in. Instead, given the nature of blockchain technology, it's transparently available on blockchain explorers, such as [Etherscan](https://etherscan.io/) or [BscScan](https://bscscan.com/) (as most block explorers are very similar under the hood, this method also applies to those of other EVM-compatible chains, such as Avalanche's Snowtrace). 


 


**Method 1: Block explorer balance checkers**
---------------------------------------------


Both these platforms have a built-in balance checker (click for the [Etherscan version](https://etherscan.io/balancecheck-tool), or the [BscScan version](https://bscscan.com/balancecheck-tool)), which allows you to request a snapshot of your wallet's contents at any point in the past. These services **only support checks on your ETH and BNB** balances, respectively, so will not be applicable if you're investigating other token balances. Other networks' block explorers are likely to have similar services, however.


You can narrow down the snapshot by date, or, for even more precision (down to ca. 10-15 second timeframes), by block number: 


![Reconciling and keeping track of your accounts balance checker](https://support.metamask.io/hc/article_attachments/12769694722843)


The results will look like the below — detailing the block or date, the quantity of ETH held at that time, and how that quantity compares to the current holdings in your wallet.


![Etherscan balance checker result](https://support.metamask.io/hc/article_attachments/17279215726107)


**If you need help locating the block number** you want to search, see the methods below (applicable to Ethereum, using Etherscan). Similar routes will also apply to other EVM-compatible networks, such as BSC.


Go via the account route:


1. In the MetaMask Extension, click the account dropdown arrow and select the three vertical dots icon for the account you want to view on an explorer. Then, select "View on explorer":


![MetaMask view account on block explorer extension](https://support.metamask.io/hc/article_attachments/17278721912603)


 


On Mobile, hit the ellipses icon on the right side of the screen next to the account address and select 'View on Etherscan':


![MetaMask view account on block explorer mobile](https://support.metamask.io/hc/article_attachments/17278707194779)


2. Find the transaction in your account's list. Its block number will be listed in the same row.


Or go via the transaction route:


1. Locate the transaction:
	* Extension: Access the 'Activity' tab and click on the relevant transaction.
	* Mobile: Tap the hamburger icon and either select 'Transaction History', or select the token on your wallet landing page to view all its transactions.
2. Click/tap on the transaction and select 'View on Etherscan' (Mobile) or 'View on block explorer' (Extension).
3. The block will be listed on the Etherscan transaction page.


 


**Method 2: Downloading a spreadsheet (.csv) history of your wallet transactions**
----------------------------------------------------------------------------------


(for Ethereum mainnet)


* Navigate to [Etherscan](https://etherscan.io/) and search for your [wallet address](https://support.metamask.io/hc/en-us/articles/360015289512).
* Scroll down to the bottom of the page, past all your transactions.
* In the lower right-hand corner, there should be a link to "Download CSV Export":


![Reconciling and keeping track of your accounts CSV](https://support.metamask.io/hc/article_attachments/12769694768411)


* Click on this; you should be presented with a dialogue that allows you to specify the date range you're interested in looking at:


![Etherscan download transactions CSV](https://support.metamask.io/hc/article_attachments/17279180745371)


* Fill out the dates and the captcha and click 'Download'.
* You should have in your downloads location a file titled "export-" plus your wallet address. This file should have a complete listing of all transactions involving your wallet (except for internal transactions) for the timeframe you requested.


See also our [article regarding tax compliance](https://support.metamask.io/hc/en-us/articles/4406001678747-Tax-compliance-and-crypto-assets).


 

