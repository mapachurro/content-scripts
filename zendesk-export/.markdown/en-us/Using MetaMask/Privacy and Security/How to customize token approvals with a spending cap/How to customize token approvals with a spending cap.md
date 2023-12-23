*tl;dr: MetaMask allows you to manually edit the number of tokens dapps can access. [Click here](#h_01G3E1JE4CPVP1VH8PFS4FH25P) to jump straight to how.*


 


What is the point of token allowances?
--------------------------------------


When you interact with any dapp that involves your ERC-20 token holdings in some way or another, you're likely to have to approve its access to that token's smart contract (the same applies for ERC-20 equivalents on other chains, such as BEP-20 on BNB Chain). Then, when you decide, for example, to add 1,000 of token A and 1,000 of token B to a liquidity pool, the dapp *already*has your permission to take the necessary quantity of tokens straight out of your wallet, and all you have to do is confirm the transaction. 


Token allowances are specific to one token. That means that if you've granted an allowance for a dapp to access your USDT, for example, it is only USDT that it can access. 


In most cases, token allowances that exceed what you need for any single transaction are very convenient; it would be time-consuming to have to grant permission anew for every transaction you wish to make on the dapp. Pre-approving access to a number of tokens at once is, therefore, something of a quality-of-life feature that makes your web3 activities smoother.


Customizing token allowances in MetaMask
----------------------------------------


To preserve your control and agency, as well as giving you the tools to protect yourself from [one of the most common scam attack vectors](https://consensys.net/blog/metamask/the-seal-of-approval-know-what-youre-consenting-to-with-permissions-and-approvals-in-metamask/#:~:text=Token%20approvals%20are,intention%20of%20stealing.) around, MetaMask enables you to customize how many tokens you allow dapps to access. 


How? Well, when you come across a request to grant access to your tokens, a MetaMask approval window will appear. Check out the tabs below to see how this looks on Mobile and Extension:




Extension Mobile


When you're prompted to sign a token allowance, MetaMask will show you the below screen, asking you to set a spending cap for the token:


![Custom spending cap extension](https://support.metamask.io/hc/article_attachments/13635781517467)


We designed this interface to give you more control and visibility over your token allowances, since you'll *always* be prompted to input a preferred limit, rather than default to the amount proposed by the dapp (though you can still select this default allowance if you choose).


All you need to do is **input an amount you're comfortable with**. If you're not sure, see our [main article on token allowances](https://support.metamask.io/hc/en-us/articles/6174898326683) (a.k.a. approvals) for some more context.


You can choose between:


* A custom value that you choose
* 'Max', which inserts your account's balance of the relevant token
* 'Use default', which inserts the amount the dapp is suggesting.


Click 'Next' to move to the second of two screens in the process, where you review your limit:


![Custom spending cap extension](https://support.metamask.io/hc/article_attachments/13635781542939)


When you're ready, click 'Approve' to complete the process.




Any interaction with a dapp that requires a token approval will call up a screen that reads "Spending cap request for your [token]": 


![Customize spending cap mobile](https://support.metamask.io/hc/article_attachments/17635641166235)


We designed this interface to give you more control and visibility over your token allowances, since you'll *always* be prompted to input a preferred limit, rather than default to the amount proposed by the dapp (though you can still select this default allowance if you choose).


All you need to do is **input an amount you're comfortable with** in the 'Spending cap' field. If you're not sure, see our [main article on token allowances](https://support.metamask.io/hc/en-us/articles/6174898326683) (a.k.a. approvals) for some more context.


You can choose between:


* A custom value that you choose
* 'Max', which inserts your account's balance of the relevant token
* 'Use site suggestion', which inserts the amount the dapp suggests.


Hit 'Next' to move to the second of two screens in the process, where you review your limit:


![Customize spending cap mobile](https://support.metamask.io/hc/article_attachments/17635641167259)


Once you're satisfied with the conditions of the transaction, tap 'Approve' to complete the process.




 


Staying safe
------------


Token allowances are an essential part of web3, and issuing virtually unlimited approvals is also not problematic in itself: most of the time, it makes your life easier and reduces how much gas you're paying (since you need to pay for each separate approval). However, dapps are rarely ever completely secure from exploits and hack attempts, and having an unlimited token allowance in place may put you at risk of theft. If the dapp has a vulnerability in its code, it may be possible that bad actors can exploit it and order the dapp to withdraw your funds without you requesting it.


Equally, it's also possible that the site from which the token approval request originates is malicious. This is the more common form of attack: you visit a site designed to look like another, more trustworthy site or brand, and it's this trust that gets exploited. In these cases, your tokens can be stolen as soon as you send the approval transaction.


To prevent yourself becoming a victim of this, there are **two potential methods** you could adopt:


1. Never grant unlimited (astronomically high) allowances.
2. Grant unlimited allowances to trusted sites from time to time, but frequently [check in and revoke them](https://support.metamask.io/hc/en-us/articles/4446106184731) to keep on top of who and what has access to your tokens.


Both are viable, but **option 1 is the safest**. 


Additionally, you should **always do your [due diligence](https://consensys.net/blog/metamask/the-seal-of-approval-know-what-youre-consenting-to-with-permissions-and-approvals-in-metamask/#:~:text=You%E2%80%99ll%20often%20see,short%20time%20periods.)** on any site to which you grant token allowances. Sometimes, if the dapp itself was deployed by a bad actor out to steal your funds, it doesn't even have to be exploited for you to become a victim: as soon as you click 'approve' on the token, they can drain your wallet of that token. See our [Twitter thread](https://twitter.com/MetaMask/status/1499848729615949824) on this subject for additional context.


For more information on token approvals, here are some more resources:


* [Our deep dive blog post](https://consensys.net/blog/metamask/the-seal-of-approval-know-what-youre-consenting-to-with-permissions-and-approvals-in-metamask/)
* [How to revoke smart contract allowances/token approvals](https://support.metamask.io/hc/en-us/articles/4446106184731)
* [What is a token approval?](https://support.metamask.io/hc/en-us/articles/6174898326683)
