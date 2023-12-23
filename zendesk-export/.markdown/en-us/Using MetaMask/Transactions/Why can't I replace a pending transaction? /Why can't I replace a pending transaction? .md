
#### Looking for how to resolve pending transactions?


Pending transactions that are displaying as such on the blockchain (make sure to [check a block explorer](https://support.metamask.io/hc/en-us/articles/360057536611)) can be replaced by sending another transaction with the same nonce, using the method [here](https://support.metamask.io/hc/en-us/articles/360015489251). This article should be your first destination if you're looking for how to replace a pending transaction.



One of the most common reasons your replacement pending transaction will fail is because you **already have multiple pending transactions**. 


In these cases, you need to **replace the oldest transaction first, and proceed through them in reverse order** (from oldest to newest). 


Age is determined by the transaction's nonce, a unique number (*number used only once*) that is assigned to every transaction sent from your wallet. Nonces are assigned in ascending order — so the smallest pending transaction nonce you can find is the oldest. 



#### How do I find pending transactions?


If a transaction is pending, it will be marked as such in your MetaMask transaction history. You can also inspect your history on a [block explorer](https://support.metamask.io/hc/en-us/articles/360057536611).



If you try to replace a pending transaction before resolving older outstanding pending transactions first, your new transactions will continually fail. This is because you need to resolve the oldest first. 

