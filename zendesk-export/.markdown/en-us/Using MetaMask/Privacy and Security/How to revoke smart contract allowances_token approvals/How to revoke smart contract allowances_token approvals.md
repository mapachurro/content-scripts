*Note: smart contract allowances are different from simply connecting your wallet to a dapp. For information on disconnecting your wallet from dapps, see [here](https://support.metamask.io/hc/en-us/articles/360059535551).*


Smart contract/token allowances, also referred to as approvals, involve you **allowing dapps to access and move tokens in your wallet on your behalf**. When you use a DEX (decentralized exchange), for example, you'll need to sign an approval that allows its smart contract to take tokens to complete your requested trades. Whilst this sounds inherently risky, bear in mind that giving dapps at least *some* allowance is always necessary. If you want to use Web3, you won't be able to avoid them. 



#### Revoking approvals vs. disconnecting apps: what's the difference?


It's easy to confuse these two processes, but they are fundamentally different:


* **Disconnecting your wallet** from a dapp involves cancelling permission for it to see your public address and your token balances, and, depending on what you originally consented to, stopping it from initiating transactions (although *not* executing them) and viewing past activity. See our [article](https://support.metamask.io/hc/en-us/articles/360059535551) for more info.
* **Revoking an approval/allowance** means a dapp can no longer access the contents of your wallet and move them around.


See also: our [Twitter thread](https://twitter.com/MetaMask/status/1499848000549515265) covering the distinction between these two actions, and our [article on token approvals](https://support.metamask.io/hc/en-us/articles/6174898326683). 



**How do I revoke approvals?**
------------------------------



#### Revoke your token allowances in MetaMask Portfolio


We've added a feature to MetaMask Portfolio that allows you to view allowances and submit revocation transactions directly within the dapp. It's available on Ethereum mainnet.


To learn more, see our separate article [here](https://support.metamask.io/hc/en-us/articles/20220963022363).



The good news is there are several ways to keep track of your existing approvals and easily revoke them:


* **Head to the 'approval checker' section of the block explorer** for the network you're using. For example, [Etherscan](https://etherscan.io/tokenapprovalchecker), [BscScan](https://bscscan.com/tokenapprovalchecker) and [Polygonscan](https://polygonscan.com/tokenapprovalchecker) all have a token approval checker function.
* Use a platform such as:
	+ [Revoke](https://revoke.cash/) (Many networks)
	+ [Unrekt](https://app.unrekt.net/) (multiple networks)
	+ [approved.zone](https://approved.zone/) (Ethereum mainnet)
	+ [Cointool](https://cointool.app/approve/eth) (multiple networks)
	+ [beefy.finance](https://allowance.beefy.finance/) (BSC/BNB Smart Chain)
	+ [EverRevoke](https://everrise.com/everrevoke/) (multiple networks).
* Use MetaMask to overwrite existing token approvals by sending a new approval transaction with the same token details and nonce as the previous approval. See our [article](https://support.metamask.io/hc/en-us/articles/360015489251) for more information on how to do this.



#### Gas fees


Since token approvals are conducted on-chain, revoking the approval must also be on-chain. This means you need to pay gas fees for each revocation. 



Look, we know how it is: there's always a new dapp to try. The only problem is that this can quickly rack up a long list of token allowances, potentially making you vulnerable to hackers or scams. This is why it's a good idea to **develop a habit of regularly checking your token approvals**—e.g. monthly—and weeding out any you're unhappy with.


Unfortunately, token approvals are a common attack vector for both hackers and scammers: the former can sometimes locate and exploit vulnerabilities in a smart contract's code ([this happened to Wormhole](https://rekt.news/wormhole-rekt/), an Ethereum <-> Solana bridge, for example) and the latter can occur through rugpulls.


This is because token approvals often request **unlimited access** to your tokens. If a hacker or fraudulent smart contract owner is able to leverage this, they can theoretically drain your wallet of the tokens you've allowed access to. To this end, [MetaMask allows you to customize token permissions](https://support.metamask.io/hc/en-us/articles/6055177143579). 


For a more in-depth look at token approvals and dapp permissions, check out [our blog post](https://consensys.net/blog/metamask/the-seal-of-approval-know-what-youre-consenting-to-with-permissions-and-approvals-in-metamask/), or [this article](https://kalis.me/unlimited-erc20-allowances/) from the creator of the Revoke app mentioned above.

