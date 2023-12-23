
#### New to crypto and web3?


Head to [MetaMask Learn](https://learn.metamask.io/) for a straightforward learning experience designed specifically for newcomers to web3. It's completely free, available in multiple languages, and includes useful tools such as simulations to help you find your feet with MetaMask.



Gas is the unit of measure for how much computational work is required to process transactions and smart contracts. Essentially a transaction fee, the term originates from Ethereum, in which context it refers to computation undertaken on the Ethereum Virtual Machine (EVM). Since Ethereum was founded, numerous EVM-compatible (and non-EVM-compatible!) networks have emerged and adopted similar models. 


The term is analogous to the gas that powers a car engine: it's the fluctuating, occasionally expensive cost of operation. More complex smart contracts require more gas to power their computation, just as a bigger, more powerful car takes more gas to run.


The method for calculating gas fees varies depending on the network. For example, calculating gas on Ethereum used to be very complicated, but was considerably simplified with the implementation of Ethereum Improvement Protocol **(EIP) 1559** in August 2021 (also known as the London Upgrade). Essentially, you pay a **base fee** for every unit of gas, which is ***burned*** (read: it is deleted, and disappears) upon successful completion of the transaction. On top of the base fee, you add a **priority fee**, again per unit of gas, the value of which depends on how quickly you want the transaction to go through. 


Across the broad range of EVM-compatible networks available, gas, or similarly-functioning alternatives, have essentially become the standard method of calculating transaction costs. Fees are paid in the network's native token: for example, any transaction on Ethereum requires ETH; using BSC requires BNB; using Polygon requires MATIC. Some networks have adopted Ethereum's EIP-1559 model wholesale, such as Polygon, whilst others have made adjustments, including Avalanche, for their C-Chain (which [burns both the base fee and priority fee](https://docs.avax.network/learn/platform-overview/transaction-fees/#c-chain-fees), rather than just the former).  


If you want to read a more in-depth look at how gas works on Ethereum, see [here](https://ethereum.org/en/developers/docs/gas/). 


 


Here are some **essential details for dealing with gas** **in MetaMask**:


#### **The gas limit (units of gas used)**


The *gas limit* is the **maximum number of units of gas you are willing to pay for** in order to carry out a transaction or EVM operation. Different operations demand different quantities of gas units. A normal transaction sending ETH or a token normally costs **21,000** gas, whereas an ERC-20 token approval requires 45,000. Many networks, such as EVM-compatible blockchain Harmony, use an identical model in which standard transactions also cost 21,000 gas.  



#### Do I need to edit gas limit?


No! MetaMask automatically sets your gas limit depending on the transaction you're trying to execute. In the vast majority of cases, this will be adequate to complete your transaction. If you want to check or edit it, make sure you have [advanced gas controls](https://support.metamask.io/hc/en-us/articles/360022895972) turned on and hit the button next to the gas information on the transaction confirmation screen that reads 'Market', 'Low', or 'Aggressive'.



#### **The base fee**


Every block on the Ethereum network has a base fee determined by network demand: the base fee is based on the block size of the block before it, compared against a target block size (where size refers to the total amount of gas used for all the transactions the block includes). If the size of the previous block exceeds the target, the base fee for the next block increases by 12.5%, leaving you, the user (or your wallet), with absolute certainty as to the base fee of the upcoming block. Your total gas fee must meet this price as a minimum in order to be considered for inclusion in the block. 


#### **The priority fee**


The*priority fee*, also referred to as the "miner tip", incentivizes the miner to prioritize your transaction. 


Naturally, whether this does actually go to a miner depends on the [consensus mechanism](https://support.metamask.io/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) they use: Ethereum mainnet became a Proof of Stake network following the Merge in September 2022, so the priority fee goes to validators instead of miners. 


#### **The max fee**


The max fee is the total, global amount paid for your transaction. It is calculated as: **(****base fee + priority fee) x units of gas used.** MetaMask initially sets this amount based on the previous block’s history. However, users can edit this amount through custom settings (see below). The difference between max fee per gas and (base fee + max priority fee per gas) is “refunded” to the user.


![Estimate gas fee](https://support.metamask.io/hc/article_attachments/16533578755867)


 


### **Additional Concepts**


#### **Gwei**


Gwei is a unit of ether, the smallest denomination, which stands for [gigawei](https://ethgasstation.info/blog/gwei/) (or 1,000,000,000). [Gwei](https://www.investopedia.com/terms/g/gwei-ethereum.asp) is used for gas fees, or rather payments made by users to compensate for the computing energy required to process and validate transactions on the Ethereum blockchain. 


Other networks also tend to calculate costs using gwei — for example, Fantom, Harmony and Avalanche.


#### **Slippage**


Slippage is the expected percentage difference between a quoted and an executed price.


#### **Gas fee**


Gas *fee* refers to the transaction fee on the Ethereum blockchain. It is what users pay to get their transaction validated, or completed. 


#### **Base fee**


Generated by the protocol. Represents the minimum 'gasUsed' multiplier required for a transaction to be included in a block (i.e. for a transaction to be completed). This is the part of the transaction fee that is burnt.


 


### **Advanced Gas Controls**


If you want to get into the nitty-gritty of your gas controls (this can be helpful if you're testing a dapp, for example), MetaMask can do that! See the full article [here](https://support.metamask.io/hc/en-us/articles/360022895972).


 


### **FAQ**


[Why did I pay gas fees for a failed transaction?](https://support.metamask.io/hc/en-us/articles/360045439051)


[Can you refund my gas fees?](https://support.metamask.io/hc/en-us/articles/360058370012)


[How do I speed up or cancel a pending transaction?](https://support.metamask.io/hc/en-us/articles/360015489251)


[How to estimate the gas fee](https://support.metamask.io/hc/en-us/articles/360059562111)


[Why are my gas fees so high?](https://support.metamask.io/hc/en-us/articles/360058751211-Why-my-gas-fees-are-so-high-)


[Error: [ethjs-query] while formatting outputs from RPC (transaction underpriced error)](https://support.metamask.io/hc/en-us/articles/4402538041869)


[How to fix "insufficient funds" error or greyed-out confirm button](https://support.metamask.io/hc/en-us/articles/360044703372)


 


 

