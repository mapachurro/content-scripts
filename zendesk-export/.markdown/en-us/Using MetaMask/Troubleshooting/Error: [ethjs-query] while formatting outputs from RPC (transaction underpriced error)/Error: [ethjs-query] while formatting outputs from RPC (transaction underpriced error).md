**The information in this article is applicable to Ethereum mainnet *and* other networks, such as BSC and Polygon.**


If the gas price has been set too low when attempting to carry out a transaction, this sort of error can occur:


"Transaction <*your transaction # here*> failed! Error: [ethjs-query] while formatting outputs from RPC '{"value": {"code":-32000,"message":"transaction underpriced"}}'"


This can happen when attempting to make a swap via a DEX (decentralized exchange) or simply when sending tokens to an address.


In order to successfully complete the transaction, you should issue a new transaction whilst**raising the amount of gas you pay.**However, before you do so, check on the relevant block explorer (e.g. [Etherscan](https://etherscan.io/), [BscScan](https://bscscan.com/), [Polygonscan](https://polygonscan.com/) etc.) to make sure you are not generating an increasingly longer queue of pending transactions. 


To do this:




Extension Mobile


1. Start a new transaction, using the same recipient details and token amount as the original (assuming you want them to remain the same) and hit 'Next'.
2. Click on the 'Market' icon located above your gas details, and then hit 'Advanced':


![MetaMask find advanced gas controls extension](https://support.metamask.io/hc/article_attachments/17276432323483)
3. You'll now be presented with a set of fields you can adjust, resembling the below:


![MetaMask advanced gas fee settings](https://support.metamask.io/hc/article_attachments/17276432325147)


Here you should:


	* **Input a comparable or slightly higher gas limit** than you did for the transaction that failed
	* Raise the **max priority fee** at least **10% higher (in gwei) than the gas fee of the failed transaction**
	* Set your **max fee** at least **30% higher** than that of the failed transaction.


If you are trying to cancel that pending transaction altogether, you need to send 0 ETH (or equivalent currency) to your own address with the same nonce as the pending transaction. See our [article on cancelling transactions](https://support.metamask.io/hc/en-us/articles/360015489251-How-to-speed-up-or-cancel-a-pending-transaction) for more guidance.




1. Click the wallet actions button in the center of the tab bar. This will bring up a pop-up menu, where you can select the 'Send' button.
2. Input the details of your transaction, such as the recipient address and the quantity of tokens you want to send. These details should be the same as the original (failed) transaction, assuming you still want to send the same amount to the same address. Tap 'Next'. You should now see the screen below. Tap on the highlighted gas fee number:
3. This will bring up an additional menu where you'll be presented with the options to set your gas fee low, medium, or high. Ignore these and tap 'Advanced options' instead.
4. You can now customize your gas settings with more precision to ensure your new transaction goes through.


![MetaMask find advanced gas controls mobile](https://support.metamask.io/hc/article_attachments/17276400744219)


Here you should:


	* **Input a comparable or slightly higher gas limit** than you did for the transaction that failed
	* Raise the **max priority fee** at least **10% higher (in gwei) than the gas fee of the failed transaction**
	* Set your **max fee** at least **30% higher** than that of the failed transaction.


If you are trying to cancel that pending transaction altogether, you need to send 0 ETH (or equivalent currency) to your own address with the same nonce as the pending transaction. See our [article on cancelling transactions](https://support.metamask.io/hc/en-us/articles/360015489251) for more guidance.




For more information on gas, see our [user guide](https://support.metamask.io/hc/en-us/articles/4404600179227-User-Guide-Gas).

