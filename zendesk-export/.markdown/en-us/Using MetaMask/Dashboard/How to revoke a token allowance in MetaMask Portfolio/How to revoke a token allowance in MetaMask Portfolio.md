You can view and revoke any token allowances (also known as token approvals) in MetaMask Portfolio.



#### Ethereum mainnet only


Please note that this feature is only supported for Ethereum mainnet. We'll add support for further networks when possible.


To revoke approvals on networks other than Ethereum, check out our list of third-party revocation tools in this article: [How to revoke smart contract allowances/token approvals](https://support.metamask.io/hc/en-us/articles/4446106184731)



What is a token allowance?
--------------------------


Allowances are permissions that you sign to indicate consent for a dapp to access a given number of a specific token type. Usually, this is because you're interacting with a dapp that involves an operation like depositing, sending, staking, etc. — all of which require tokens to be moved *from* your account and, generally, *to*a smart contract or another [externally owned account](https://ethereum.org/en/developers/docs/accounts/#types-of-account) (just like yours). **You can read a more in-depth explainer of token allowances [here](https://support.metamask.io/hc/en-us/articles/6174898326683).** (Note that you don't need to sign allowances for ETH — only ERC-20 and ERC-777 tokens require them.)


Once an allowance is signed, its existence is recorded on the blockchain, meaning it will be valid until you sign another transaction that revokes it. Each allowance limits how many tokens of that type the dapp can access. For example, if you signed an allowance for 1,000 USDC, you could order the dapp to use up to 1,000 USDC tokens in one transaction or many — either way, the permission is valid until you've used up this allowance. 



#### Spending caps in MetaMask


When you sign a token allowance in MetaMask, you're prompted to specify how many of the tokens you want to allow access to. We call this a "spending cap", and you can [read more about the process here](https://support.metamask.io/hc/en-us/articles/6055177143579). Dapps often request a default value, which in many cases is so large it essentially permits unlimited access. Unlimited token approvals, as they are known, are dangerous — signing one to a fraudulent dapp, or a legitimate dapp that is hacked, can result in all of a certain token type being drained from your wallet without you being aware.



How to view and revoke token allowances
---------------------------------------


1. Head to [MetaMask Portfolio](https://portfolio.metamask.io/) and make sure your wallet is connected.
2. Head to 'Settings'. On a desktop browser, this is found in the drop-down menu on the top-left of the page:


![MetaMask_Portfolio_find_account_settings.png](https://support.metamask.io/hc/article_attachments/21168254912027)


On mobile, hit the hamburger icon in the top-left to access it:


![MetaMask Portfilio locate settings mobile](https://support.metamask.io/hc/article_attachments/20350882171675)
3. Select the 'Allowances' category in the settings menu.


![MetaMask Portfilio revoke allowance](https://support.metamask.io/hc/article_attachments/20376414759323)


Make sure you select the account whose allowances you want to view. You can only select one account at a time.
4. Click the revoke button next to the allowance you want to revoke.
5. Submit the transaction in MetaMask. Since revocation requires submitting a transaction to the network, **you will need pay gas fees to revoke an allowance**.
