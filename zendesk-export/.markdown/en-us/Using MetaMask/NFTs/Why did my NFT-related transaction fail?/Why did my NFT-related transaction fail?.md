NFTs are moved between different addresses in a similar way to other cryptoassets like ERC-20 tokens. This means they could be subject to the same reasons that regular transactions fail. To start with, see our article [here](https://support.metamask.io/hc/en-us/articles/4410741657499) for more information on failed transactions generally. 


Although you'll be able to see a transaction's 'Failed' status in MetaMask, you can get more detail about the specific reason by heading to [Etherscan](https://etherscan.io/) (or the block explorer for the network you're using).


There are several error messages you could see on your transaction on the block explorer:


* **Reverted**: This error is thrown when transactions are not completed and the network essentially reverts to a state that reflects how things would be if you hadn't ever submitted it. This is relatively common on NFT marketplaces — such as OpenSea — as it occurs if someone completes an NFT purchase ahead of you. If this happens, check on the marketplace (or look up the NFT on a block explorer using its address) to see if it has already been transferred to a different wallet address.
* **Out of gas**: This means your transaction's gas limit was exceeded before the transaction could be completed. A regular transaction needs a minimum of 21,000 gas units; NFT-related transactions such as purchases can be more complex, and require higher gas limits. If you receive this error, you need to try the transaction again but adjust your gas limit in MetaMask. See our article on this error message [here](https://support.metamask.io/hc/en-us/articles/360038849792).
* **Dropped and replaced**: This message refers to a situation where one transaction is, for various possible reasons, disregarded by the network in favour of another. Transactions can be dropped from the mempool (where they are held before being added to a block) by Ethereum nodes, potentially due to offering lower gas fees than other broadcast transactions or just timing out. See a full explanation in this [Etherscan article](https://info.etherscan.com/transaction-dropped-replaced/). It can also occur if you deliberately attempt to replace a transaction, such as if it's [stuck or pending](https://support.metamask.io/hc/en-us/articles/360015489251).
* **Pending or 'stuck'**: When the total gas fee is too low to incentivize validators to pick it up and add it to a block (usually because the priority fee wasn't high enough), you'll get this error message. You can try to 'unstick' your transaction using the methods outlined [here](https://support.metamask.io/hc/en-us/articles/360015489251).


If you're still unable to resolve your issue within NFT transaction, get in touch with Support using the 'Start a Conversation' button on the homepage of this site.

