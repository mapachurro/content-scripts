### Getting the gas price


If you are on Ethereum mainnet you can check [Etherscan's gas tool](https://etherscan.io/gastracker) to estimate today's gas price. Please note the gas price fluctuates; always refer to the gas station to see the current gas prices.


The Ethereum network requires gas to execute transactions. When you send tokens, interact with a contract, send ETH, or do anything else on the blockchain, you must pay for that computation. That payment is calculated in gas, and gas is always paid in ETH.


You are paying for the computation, regardless of whether your transaction succeeds or fails. Even if it fails, validators must finalize and execute your transaction, which takes computational power. You must pay for that computation, just like you would pay for a successful transaction.


 


### Getting the gas limit


So, you know how much each unit of gas costs, but how many units of gas do you need to spend? Well, if it's a simple transaction—say, sending ETH or an ERC-721 token to another address—you should be spending 21,000 units of gas. If you're doing something more complex, a good tool is a block explorer, such as [etherscan.io](https://etherscan.io/). Navigate to the contract you wish to interact with, and start examining transactions made with the contract. This will give you a better idea of how much gas other users actually end up using.



#### Gas calculator


There are a few tools available out there for you to estimate how much gas is going to cost you in fiat currency before you submit a transaction. One example is the [Cryptoneur gas fee calculator](https://www.cryptoneur.xyz/gas-fees-calculator), which lets you input the details of your transaction and produces the estimated gas cost in your local currency, and specific to current demand on that network (you can choose from most major EVM-compatible networks).



### 
Overall gas fee structure


As of [EIP-1559](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1559.md), the overall fee a transaction creator pays is calculated as: **( (base fee + priority fee) x units of gas used)**.


![Estimate gas fee](https://support.metamask.io/hc/article_attachments/15925062359323)


For more information, see [here](https://support.metamask.io/hc/en-us/articles/4404600179227).


 


**Please note this is not a fee that MetaMask receives so we cannot refund it.** This fee is paid to miners or validators for finalizing the transaction, validating it into a block, and securing the blockchain.

