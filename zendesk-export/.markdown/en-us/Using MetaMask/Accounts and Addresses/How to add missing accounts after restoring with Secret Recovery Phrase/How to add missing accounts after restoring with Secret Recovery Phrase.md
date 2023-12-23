
#### Note:


Any **imported** accounts will **not** be re-added when you restore your wallet using your Secret Recovery Phrase. [They need to be manually re-added](https://support.metamask.io/hc/en-us/articles/360015489331) in the same way you imported them originally.



**DO NOT share your Secret Recovery Phrase with anyone! These words can be used to steal all your accounts. You cannot edit or change your Secret Recovery Phrase.**


 


When you [restore a wallet](https://support.metamask.io/hc/en-us/articles/360015289612-How-to-restore-your-MetaMask-account-from-Seed-Phrase-Secret-Recovery-Phrase) using your Secret Recovery Phrase, MetaMask will automatically re-add any additional accounts you had previously [added](https://support.metamask.io/hc/en-us/articles/360015289452) — but only under certain conditions.


MetaMask will attempt to add your additional accounts where possible (assuming they were not [imported](https://support.metamask.io/hc/en-us/articles/360015289932)) by checking your previous accounts in ascending order (i.e. Account 2, then Account 3, etc.). **Accounts are automatically re-added if they have a non-zero ETH balance**. However, this process ends when MetaMask encounters an account with 0 ETH — so the first account with 0 ETH (and any beyond it) will *not* be added.


Bear in mind that **this process only checks for balances of ETH on Ethereum mainnet**, so other tokens or tokens on other networks will not result in your account being automatically re-added.


**For any that are not re-added automatically, you have to [add the account in the standard way](https://support.metamask.io/hc/en-us/articles/360015289452)**. For example, if you have some tokens in Account 4, but Account 4 isn't automatically added because those tokens are not ETH on mainnet, all you need to do is manually add accounts (using the below steps) until you get to Account 4. Your Account 4 *before* the restore corresponds to Account 4 *after* the restore, regardless of any name you previously applied.


If you do need to re-add accounts this way, don't worry about the account address being different. The addresses are cryptographically derived *deterministically* from your private key, which means they will always be the same. And since an Ethereum account, once created, exists permanently, you can just pick up where you left off. 


Please follow the steps below on how to restore your other accounts in the order they were originally created:




Extension Mobile


1. Click on the account selector at the top of the wallet, and select 'Add account or hardware wallet':  

![MetaMask find add account button extension](https://support.metamask.io/hc/article_attachments/19818138241307)
2. On the next screen, click 'Add a new account' to restore your MetaMask accounts in the order they were created
3. If the accounts were previously named, you can name them again in the step below, before clicking "**Create**"


![MetaMask create new account extension](https://support.metamask.io/hc/article_attachments/19818138261019)




1. Tap the name of the currently selected account, and then tap 'Add account or hardware wallet'.
2. Tap 'Add new account':


![MetaMask create additional account mobile](https://support.metamask.io/hc/article_attachments/17277626158619)




If you still do not see the addresses you were looking for, they were probably created with a different Secret Recovery Phrase, or you had an imported account that you still need to reimport using private keys or JSON. Please see [this article on how to import an account](https://support.metamask.io/hc/en-us/articles/360015489331-Importing-an-Account). 

