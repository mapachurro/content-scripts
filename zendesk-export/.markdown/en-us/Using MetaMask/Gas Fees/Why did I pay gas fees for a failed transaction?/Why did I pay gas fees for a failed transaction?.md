**Gas paid is not a fee that MetaMask receives so we cannot refund it.** This fee is paid to validators for finalizing transactions, validating them into blocks, and securing the blockchain.


The Ethereum network [requires gas](https://support.metamask.io/hc/en-us/articles/4404600179227) to execute transactions. When you send tokens, interact with a contract, or do anything else on the blockchain, you must pay for that computation. That payment is calculated in gas, and gas is always paid in ETH.


You are paying for the computation, regardless of whether your transaction succeeds or fails. Even if it fails, validators must verify and execute your transaction, which takes computational power. You must pay for that computation, just like you would pay for a successful transaction.


There are a few other error examples that you could encounter during the transaction failure: 


* A **Dropped and Replaced** transaction, which means the transaction was dropped and replaced by a new one. Please see more information about a dropped and replaced transaction here: <https://info.etherscan.com/transaction-dropped-replaced/>
* **Out of gas** is an error that occurs when the gas limit was set too low. Please read the below article for a better understanding of the gas limit: <https://ethgasstation.info/blog/gas-limit/>. You can retry the transaction, but this time please use [advanced gas controls](https://support.metamask.io/hc/en-us/articles/360022895972) to set the gas limit to a higher value. You can also refer to [this article](https://support.metamask.io/hc/en-us/articles/360038849792-Why-did-my-transaction-fail-with-an-Out-of-Gas-error-How-can-I-fix-it-) to learn more about this error and how to fix it.
