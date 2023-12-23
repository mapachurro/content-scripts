If you are curious to learn more about gas and what it signifies in Ethereum, we recommend reading [our guide on gas](https://support.metamask.io/hc/en-us/articles/4404600179227) or the [ethereum.org guide](https://ethereum.org/en/developers/docs/gas/) if a little more comfortable already.


A common problem that you may see or have seen is transactions failing with an **"out of gas"** error like in the screenshot below.


![out of gas error](https://support.metamask.io/hc/article_attachments/12804824256539)


This means that all the gas units up to the limit you set were used up before the transaction could be fully processed. 


To avoid another "out of gas" error, you will need to increase the gas limit of your next transaction. This can be done just before sending your next transaction, once you have [enabled Advanced Gas Controls](https://support.metamask.io/hc/en-us/articles/360022895972). 


### Advice from the MetaMask team


The vast majority of the time, the gas limit that MetaMask automatically sets for your transaction will be sufficient.


Selecting a gas limit is mostly a personal preference, but it may be helpful to review recent successful transactions of the executing smart contract to understand what is a sufficient gas limit for your transaction.


Recommended steps:


1. While reviewing your transaction with the "out of gas" error on Etherscan, click the link to the Contract address in the "To:" section directly above the out of gas error
2. Scroll down to the list of Transactions andclick on the Txn Hash of any completed transaction (non-pending)
3. Ensure that the transaction shows Status as **Success**. If not, go back and choose another transaction.
4. Click on **Click to show more**
5. Make a note of the **Gas Limit**that was chosen for the transaction
6. *Optional:*repeat steps 1-4 to better estimate a gas limit that will be sufficient for your transaction
7. Once you have a good idea of a value for your gas limit, make sure to [adjust the gas limit](https://support.metamask.io/hc/en-us/articles/360022895972) when sending out your next transaction.


### Example


In the example below, notice that the transaction with "Status: Fail" used up 100% of the gas:


![out of gas error](https://support.metamask.io/hc/article_attachments/12804797795739)


After reviewing a different transaction for the same smart contract, we discovered that the gas limit of this transaction was set to 32,484 which was enough to complete the transaction. Notice that even though a higher gas limit was used, only around 67% of it was used to complete the transaction:


![out of gas error](https://support.metamask.io/hc/article_attachments/12804798007963)


While you are not required to use the same gas limit as the first successful transaction that you find, you can explore more transactions to generate an idea of what is a sufficient gas limit to ensure that your next transaction is successful. 


 


Cause
-----


The "out of gas" error occurs when all the gas you allotted for the transaction is consumed before the transaction could complete. During the transaction mining process, a portion of the gas is consumed for each operation executed on the Ethereum Virtual Machine (EVM) until the transaction is completed or until the amount of gas consumed reaches the **gas limit.**


The gas limit is the maximum amount of gas you are willing to consume. You can relate the gas limit to putting out a fire with water from a hydrant. If you do not have a large enough water supply, you may run out of water before you can extinguish the fire. As such, you will want to ensure that you include a gas limit high enough to complete your transaction.

