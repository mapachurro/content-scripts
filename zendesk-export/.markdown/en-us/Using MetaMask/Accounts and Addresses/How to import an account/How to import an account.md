*This article covers the process of adding accounts to your wallet which are not associated with your MetaMask wallet's Secret Recovery Phrase. If you're starting from a fresh install and want to access an existing MetaMask account, you should head to our article on [restoring your wallet using your Secret Recovery Phrase](https://support.metamask.io/hc/en-us/articles/360015289612). Please note that you can't import a second MetaMask Secret Recovery Phrase into your existing MetaMask wallet. It will overwrite the original and all associated data.*


**Quick links:**
----------------


* [Import using a private key](#h_01G01W07NV7Q94M7P1EBD5BYM4)
* [Import using a JSON](#h_01G01W0D3TGE72A7ZBV0FMSZX1)



#### Note:


**Imported accounts are not associated with/derived from your Secret Recovery Phrase**. This means you need to **back them up separately.** Even though they will appear in your MetaMask wallet, you need to save the private keys used to import them the same way you save your Secret Recovery Phrase. **If you delete your wallet from your device, your imported accounts will be removed with it.** When/if you then [restore your wallet using your Secret Recovery Phrase](https://support.metamask.io/hc/en-us/articles/360015289612), you will need to re-add imported accounts with their private keys. 


Read more about imported accounts [here](https://support.metamask.io/hc/en-us/articles/360015289932).



For this process, you'll need the private key string or JSON file of the account you're looking to import. Refer to the documentation of that wallet provider to learn how to find it. 


**Importing using a private key**
---------------------------------




Extension Mobile


1. Click the account selector at the top of your wallet.
2. Select 'Add account or hardware wallet' at the bottom of the list.


![MetaMask find add account button extension](https://support.metamask.io/hc/article_attachments/19727572102171)
3. On the next menu, select 'Import account'.
4. You will be directed to the Import page. Paste your private key and click 'Import**'**.


![MetaMask import account from private key extension](https://support.metamask.io/hc/article_attachments/19727588316187)


You should be able to see the newly imported account in the account selector dropdown with an 'Imported' tag next to it.


![MetaMask import account badge extension](https://support.metamask.io/hc/article_attachments/19727572109979)




1. From the wallet view, tap the currently selected account to bring up the account selector.
2. Tap 'Add account or hardware wallet' at the bottom of the menu.
3. Hit 'Import account'.
4. On this screen, paste in the private key of the account you want to import, or scan a QR code if supported by the other wallet. Tap 'Import' to complete the process.


![MetaMask import account from private key mobile](https://support.metamask.io/hc/article_attachments/17096511485851)




**Importing using a JSON file**
-------------------------------


JSON (JavaScript Object Notation) is a file format commonly used to store and share data. For our purposes, it's used to encrypt the private key. 


You can use a JSON to import a wallet into MetaMask, but **only on Extension**. To do so, get the JSON file from your external wallet and follow the steps for Extension above until you get to the import page in step 3. From there:


1. On the Import page, expand the dropdown from 'Select Type**'**.
2. Select 'JSON File**'**.
3. Click 'Choose File**'** and locate the file from your computer.
4. Enter the password that protects your JSON file (**not** your MetaMask password).
5. Click 'Import**'**.


![MetaMask import account from json file extension](https://support.metamask.io/hc/article_attachments/19727588324507)


 

