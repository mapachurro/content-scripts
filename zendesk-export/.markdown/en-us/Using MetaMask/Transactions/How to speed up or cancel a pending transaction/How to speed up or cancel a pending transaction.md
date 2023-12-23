
#### Have you tried MetaMask Activity?


MetaMask Activity is a new tool that can analyze your transactions and automatically suggest possible resolutions, and it has a built-in function dedicated to pending transactions. Why not try it out? See [here](https://support.metamask.io/hc/en-us/articles/13460965279003) for more information.



When you submit a transaction on Ethereum or a compatible network, part of the gas you pay is a bid to the network to process your transaction sooner — this element is known as the priority fee.


Although MetaMask will assist you by calculating a total gas fee likely to have your transaction picked up, you can end up waiting a long time if you submit with a low gas price. For advice on what gas prices will result in a transaction being finalized in a reasonable amount of time, please refer to sources such as [Etherscan's gas tracker](https://etherscan.io/gastracker), or a similar tracker for whichever network you're using.


Additionally, there are sometimes circumstances where something goes wrong, and a transaction is just stuck, or pending for a very long time.


No matter how you got to this point, there are a few different ways to address it.


 


**Before you take any further action, your first step should be to exit and close your browser completely, reopen it, and unlock MetaMask (on mobile, just close the app and reopen it). If that doesn't solve the problem, continue with the following:**


 


Speeding up a transaction
-------------------------


![MetaMask speed up pending transaction extension](https://support.metamask.io/hc/article_attachments/17217043760539)


Try one of the options below:


* Wait until the network is willing to process transactions at this price
* If you haven't done so already, click that button that says '**Speed up**'. This will let you re-submit the same transaction, but with a higher gas fee that should allow the transaction to be processed faster. Since this process re-uses the same nonce as the original, you do not need to pay for gas twice.


Bear in mind that **speeding up the transaction will increase the amount you're spending for the transaction**.


 


Canceling a transaction
-----------------------


### Method 1: In-app cancellation


If you haven't done this already, to cancel the transaction, simply select **Cancel**, as in the screenshot above. Please note, **a cancellation can only be *attempted* if the transaction is still pending on the network.**Transactions that have already been confirmed cannot be reversed.


![MetaMask cancel pending transaction extension](https://support.metamask.io/hc/article_attachments/17217065737499)


 


### Method 2: Custom nonce


This process involves sending a new transaction with the same nonce (an identifying number for every transaction, derived from the phrase 'number only used once'). The transaction does not actually have to have any value — e.g. you could send 0 ETH. What matters is that you pay enough gas for the network to prioritize it. 


When using this method, **you will need to work backwards from the oldest pending transaction in the queue that you want to cancel**. For example, you cannot attempt to cancel a transaction with a nonce of 10 before canceling nonce 9. 


Note also that you *may*be able to cancel multiple transactions at once if they have the same nonce. Since a nonce—by definition—can only be used once, cancelling one of them will cancel all that have the same nonce. 


*The screenshots below were taken at different times, so the gas fees shown in them can vary, even from step to step. Don't let this put you off! When you do this yourself, MetaMask will automatically update in real time to show market rates.*




Extension Mobile


1. In advanced settings, turn on **Customize transaction nonce****.** You'll need this turned on so you can send a replacement transaction (using the same nonce). Find out how to locate a transaction's nonce [here](https://support.metamask.io/hc/en-us/articles/15752269372699).


![MetaMask customize transaction nonce settings](https://support.metamask.io/hc/article_attachments/17217065740571)
2. **Send a new transaction**. In the new transaction, send **TO** yourself, meaning your MetaMask public address. **Fill in 'Custom Nonce' with the same nonce as the transaction that is still pending**:


![Metamask custom transaction nonce Extension](https://support.metamask.io/hc/article_attachments/14731609986843)
3. Next to the displayed gas fee on the transaction confirmation screen, you'll see a button that reads 'Market' (it can also read 'Low' or 'Aggressive' depending on your last used setting). Click it, and then click 'Advanced' at the bottom: 


![MetaMask advanced gas controls find](https://support.metamask.io/hc/article_attachments/14731706474011)


To make sure your cancellation request is picked up as a priority, and before the original, **you will need to pay more for gas**. On this screen, follow these instructions:


	* Set your **gas limit** *comparable to or slightly higher* than your original transaction.
	* Set your**priority fee** to *at least 10% higher* (in Gwei) than the gas fee of the original (pending) transaction (e.g. if that transaction had a gas fee of 30 Gwei, set the max priority fee in the replacement/cancellation transaction to 33-35 Gwei).
	* Make sure your **max fee** is at least 30% higher than the max fee of the transaction you're replacing. For example, if your previous fee was 150 Gwei, choose something nearer 200 Gwei this time.Check a gas tracker such as [Etherscan's](https://etherscan.io/gastracker) or [ETH Gas Station](https://ethgasstation.info/) for guidance on recommended max fees.




1. **In Settings > Advanced, turn on 'Customize transaction nonce'.**


![MetaMask customize transaction nonce settings mobile](https://support.metamask.io/hc/article_attachments/17217043774619)
2. **Send a new transaction.** In the new transaction, send TO yourself, meaning your MetaMask public address. **[Set the nonce](https://support.metamask.io/hc/en-us/articles/7417499333531) to the same nonce as the transaction that is still pending**.


To find the custom nonce setting in the app, get to the transaction confirmation screen, which appears after you've entered the token quantity and recipient. Hit 'Edit' to change it:


![MetaMask custom transaction nonce Mobile](https://support.metamask.io/hc/article_attachments/12927068442907)
3. Now you need to make sure your gas settings are configured so that your replacement transaction is processed. From the transaction confirmation screen, tap the highlighted gas value:


![MetaMask advanced gas controls mobile](https://support.metamask.io/hc/article_attachments/12927041593755)


Now access 'Advanced options' from the menu that appears.
4. From here, you can precisely adjust gas to make sure your transaction is picked up. You'll now be looking at a screen that looks like this:


![MetaMask advanced gas controls mobile](https://support.metamask.io/hc/article_attachments/12927063201691)


From here, adjust the gas settings. Follow these instructions to make sure your transaction is picked up:


	* Set your **gas limit** *comparable to or slightly higher* than your original transaction.
	* Set your **max priority fee** to *at least 10% higher* (in Gwei) than the gas fee of the original (pending) transaction (e.g. if that transaction had a gas fee of 30 Gwei, set the max priority fee in the replacement/cancellation transaction to 33-35 Gwei).
	* Make sure your **max fee** is *at least 30% higher* than the max fee of the transaction you're replacing. For example, if your previous fee was 150 Gwei, choose something nearer 200 Gwei this time.Check a gas tracker such as [Etherscan's](https://etherscan.io/gastracker) or [ETH Gas Station](https://ethgasstation.info/) for guidance on recommended max fees.



