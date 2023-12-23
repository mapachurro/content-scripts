### Contents


* [What is a token approval?](#h_01G6WZRAE8A9Z3G3J07M14J923)
* [What they look like](#h_01G6WZRG3D3HY3J4W1DR9238KF)
* [What they mean](#h_01G6WZRNT2BS61XJHV0S9CXD2P)
* [Revoking approvals](#h_01G6WZRV65M72W3J1518B5T6ZC)
* [Unlimited token approvals](#h_01G6X0J818RMX8E35CCPE0KQEH)
* [setApprovalForAll](#h_01GA1DZF6GH7EAJV86X6D839H6)
* [Additional resources](#h_01GA1DZN3YZQX2MCZ7A3H45ZSW)


 


Across web3, you'll encounter a range of transaction types, each of which is identifiable in MetaMask at the point of confirming the transaction. 


Understanding what they are and how to interpret their meaning is an important part of staying safe in web3. The challenge is that much of the information displayed on these screens is either not designed to be human-readable—such as the long hexadecimal numbers we recognize as account or contract addresses—or, at best, is difficult to decipher.


**Token approvals**are among the most common of the transaction types you'll encounter, and learning about them is therefore essential. In web3, and especially with a [self-custodial](https://support.metamask.io/hc/en-us/articles/360059952212) wallet like MetaMask, you're firmly in control and hold ultimate responsibility for everything you do. That's why it's critical you know exactly what you're signing up for when you confirm token approvals.


What is a token approval?
-------------------------


In short: **permission for a dapp to access and move a specific type of token from your wallet**. 


These prompts will often appear in MetaMask if you're a frequent user of decentralized exchanges (DEXs) and DeFi in general. Most platforms rely on you depositing or transferring your tokens to them for one reason or another. However, clicking buttons such as 'Transfer', 'Deposit', or 'Move' won't do anything unless their dapp has your permission—as the wallet owner—to do so.


This is why token approvals are necessary: they enable the dapp to access and move your tokens on your behalf. 


What they look like
-------------------


The token approval prompt that appears in MetaMask will look something like this:


![Custom spending cap extension](https://support.metamask.io/hc/article_attachments/13644257662235)


 


Let's dissect this. Notice how:


* **The dapp's name and web URL are displayed at the top.** This helps you make sure that the dapp you *expect to be* interacting with is actually the one requesting the approval.
* You **can click 'verify contract details' to see the address of the smart contract requesting access**. If you're interacting with a dapp/contract you're not 100% sure about, you could take this address and look it up on a block explorer such as [Etherscan](https://etherscan.io/) to look for any strange activity, or to see if it is flagged as a potential scam.
* **You can** **edit the permission under the 'custom spending cap' field**. In this context, the cap refers to how much of that token (in this case, USDC) the dapp can access. Note that this is not limited by how much of the token you actually have in your account; [it can and often does drastically exceed this](#h_01G6X0J818RMX8E35CCPE0KQEH). For more on editing token approvals, see our [article on setting a custom spending cap](https://support.metamask.io/hc/en-us/articles/6055177143579).
* **You have to pay gas fees**. The only way for the approval to be secure is for everyone to be 100% sure it came from you, the wallet owner. Thankfully, we just so happen to be using a decentralized, immutable ledger (i.e. blockchain) that can record your permission as historical fact. But for this permission to be recorded, it must be on chain; and for any transaction to be processed on chain, you must pay the costs of operating the network: gas.


What they mean
--------------


If you grant permission for a dapp to access 1,000 USDT, it can do so whenever you ask it to, without requiring a similar token approval transaction again. This applies until the dapp has had access to 1,000 tokens, at which point you'll need to sign another transaction. 


But what's going on behind the scenes? Well, when you approve access to a token, in many cases you're consenting to the dapp calling the [transferFrom](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20-Transfer-address-address-uint256-:~:text=an%20Approval%20event.-,transferFrom(address%20sender%2C%20address%20recipient%2C%20uint256%20amount)%20%E2%86%92%20bool,-external) function, one of the functions defined in the ERC-20 standard. (In programming, to 'call' a function is to use it.) It enables the dapp to transfer a given amount of the token from your wallet into theirs. The amount is determined by a corresponding [approve](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20-Approval-address-address-uint256-:~:text=transferFrom%20are%20called.-,approve(address%20spender%2C%20uint256%20amount)%20%E2%86%92%20bool,-external) function, for which—you guessed it—you provide inputs for when you sign your token *approval*.


You can see this process in action when you're presented with the approval confirmation in MetaMask. If you scroll down to 'View full transaction details' and click it, you can see the 'Approve' function listed:


![Token approval data](https://support.metamask.io/hc/article_attachments/13644467046811) 


 


The 'Granted to' field gives you another opportunity to copy the contract address that's asking for approval and verify its legitimacy on a block explorer. 



#### EIP-3009: the *permit* function and minimizing gas fees


Not every token you come across works as we've described above, which relates to ERC-20 tokens. This mechanism of *approve* + *transferFrom* is not relevant for tokens that have implemented the [EIP-3009](https://eips.ethereum.org/EIPS/eip-3009) model, with the stablecoin USDC the most prominent example.


With EIP-3009, rather than an *approve*transaction, you sign a *permit*transaction. These bundle up the approval and transfer into one transaction, meaning that you effectively pay zero gas for the approval, and just pay the gas for transferring the tokens.



Want more information on approvals? See our [blog post](https://consensys.net/blog/metamask/the-seal-of-approval-know-what-youre-consenting-to-with-permissions-and-approvals-in-metamask/) on the subject for a deep dive. 


Revoking token approvals
------------------------


It never hurts to be in control of your assets, and to be aware of which dapps have access to them. There are a few ways to revoke existing token approvals: see our [article](https://support.metamask.io/hc/en-us/articles/4446106184731) for more detail. 


Unlimited token approvals: how to stay safe
-------------------------------------------


Often, token approval requests will ask for access to so many tokens that it's essentially unlimited — just see the screenshot above, which shows Uniswap requesting access to 1.1559 tokens. Many legitimate dapps do this to minimize the need—and associated transaction costs—for you to re-approve access to the token every time you want to use it on a dapp. Think of DEXs, for example: if you're conducting a lot of token swaps, you don't want the additional clicks and gas fees every single time. 


However, requesting essentially unlimited amounts of tokens is also how many malicious sites steal from unsuspecting web3 users. This can be particularly demoralizing as a user if you've adhered to all our recommended [security tips](https://support.metamask.io/hc/en-us/articles/360015489591), including keeping your Secret Recovery Phrase offline-only, and never sharing it: despite all your efforts, you could be exploited anyway. 


To make sure you're not granting bad actors access to all of your tokens, we recommend you follow these key principles (which we've borrowed from our [blog post](https://consensys.net/blog/metamask/fake-mining-scams-a-familiar-foe-in-a-new-disguise/)):


* **Always check what a dapp is actually requesting before clicking ‘approve’**. In MetaMask, you can also [adjust the amount](https://twitter.com/MetaMask/status/1245769574131400709) that the dapp has access to. Even if you only provide access to 10% of your tokens, and the dapp turns out to be a scam, that’s still a considerably better outcome than if you’d granted unlimited access.
* DYOR. The best time to get in the habit of performing **due diligence** on any dapp before interacting with it was six months ago; the second best time is today. Look out for misspellings, low-quality images/logos, and other giveaways.
* Remember that **if something seems too good to be true, it probably is**. If you’re being offered 498,563% APY, you’re probably on thin ice.



*setApprovalForAll*: Making it easier to know what you're approving in MetaMask
--------------------------------------------------------------------------------


If you're not familiar with Ethereum smart contract code, *setApprovalForAll* may look mildly bewildering, but it's worth knowing about if you interact with dapps. 


This is a function in the [ERC-721 and ERC-1155 standards](https://docs.openzeppelin.com/contracts/2.x/api/token/erc721#IERC721-setApprovalForAll-address-bool-:~:text=setApprovalForAll(address%20operator%2C%20bool%20_approved)) (which relate specifically to NFTs) that enables you to grant or revoke other addresses the ability to manage **all of your NFTs associated with a specific smart contract**. 


One of the most common applications for this function is NFT marketplaces. When you sell an NFT on a platform such as OpenSea, you need to allow the dapp to access and transfer that NFT to the buyer when it sells. Such platforms often request access to *all*the NFTs of that type (i.e. originating from the same smart contract). For you, the user, this is generally inconsequential — we trust large platforms such as OpenSea not to overstep the boundary and remove NFTs that they shouldn't. 


And, like we said, *generally*it ends there. However—like many areas of web3—this is a potential opening for scammers; either by exploiting an existing dapp to which many wallets have already granted access to *all*tokens of a certain type, or by luring you into granting approval to a malicious dapp. 


This is why **MetaMask Extension makes it as clear as possible what you're consenting to when you sign a *setApprovalForAll*transaction**. This is how it'll look:


![ApproveAll Notifcation](https://support.metamask.io/hc/article_attachments/14627842608795)


 


Notice also how you have the option to '**Verify contract details**'. If you click this, you'll be able to access a page showing the name, if any, of:


* The contract requesting access
* The NFT contract.


MetaMask retrieves this information from publicly available data, and you can also copy each contract's address to your clipboard if you want to investigate further. See our [article on verifying the safety of smart contracts](https://support.metamask.io/hc/en-us/articles/10143114273563) for what kinds of things to look out for at this point. 


Given that this function allows access to all tokens associated with the contract, two things should cross your mind when you're presented with it:


* Does the dapp I'm interacting with actually need access to all of my tokens?
* Is this a legitimate, non-malicious site that isn't trying to scam me?


One common *non-*legitimate application of this function is when malicious dapps ask you to *setApprovalForAll*to claim an NFT drop: **you shouldn't have to sign this kind of approval to receive anything**. Don't be fooled!


We can't protect you from the risks inherent in using web3: as the owner of a [self-custodial wallet](https://support.metamask.io/hc/en-us/articles/360059952212), that responsibility lies with you. However, with changes such as this, we're working to equip you with the information you need to stay vigilant and aware of exactly what you're doing. 


Further reading
---------------


For more reading on token approvals, and the unlimited approvals *gotcha*specifically, see here:


* [Fake “Mining” Scams: a Familiar Foe in a New Disguise](https://consensys.net/blog/metamask/fake-mining-scams-a-familiar-foe-in-a-new-disguise/)
* [The Seal of Approval: Know What You’re Consenting To With Permissions and Approvals in MetaMask](https://consensys.net/blog/metamask/the-seal-of-approval-know-what-youre-consenting-to-with-permissions-and-approvals-in-metamask/)
* [How to revoke smart contract allowances/token approvals](https://support.metamask.io/hc/en-us/articles/4446106184731-How-to-revoke-smart-contract-allowances-token-approvals)
* [How to customize token approvals/allowances with custom spend limit](https://support.metamask.io/hc/en-us/articles/6055177143579-How-to-customize-token-approvals-allowances-with-custom-spend-limit)
