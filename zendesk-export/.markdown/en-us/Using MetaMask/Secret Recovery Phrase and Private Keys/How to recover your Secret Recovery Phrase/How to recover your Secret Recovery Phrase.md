*MetaMask provides you with a unique 12-word Secret Recovery Phrase on the very first launch. If you did not write it down, or you lost it, you can unlock MetaMask and [reveal your Secret Recovery Phrase](https://support.metamask.io/hc/en-us/articles/360015290032).*


### Are you in a situation where you don't have access to your Secret Recovery Phrase?


This can happen, for example, if your computer broke and you didn't back up your SRP. Because the SRP is the tool that creates and controls all your accounts, it might be that you've lost access to them forever. Or maybe not.


If you can [plug that old hard drive into your computer and access it](https://www.lifewire.com/access-data-from-an-old-hard-drive-5201989), or if you have a cloud backup of your system, or some other method of accessing the system data, you may be able to recover the SRP.


If, for whatever reason, you cannot unlock MetaMask using your password, there may still be a *possibility* of recovering your Secret Recovery Phrase.


Follow these instructions, and if you get stuck, start a conversation with our Support agents. 


**This article is to be used under the following circumstances**:


1. You **do not** know your Secret Recovery Phrase
2. You **do** know your password
3. For some reason you are **unable to unlock MetaMask** with your password
4. You are using MetaMask Extension in a desktop browser.



#### Note:


* Vault recovery on Android and iOS mobile devices is not currently possible.
* If you have uninstalled the MetaMask extension, your data has likely been deleted. However, you may attempt the method below, under the heading "What if you no longer have access to the browser...?," especially if you have a backup of your computer's data.



If you're not sure if this situation applies to you, [consult the various scenarios here](https://support.metamask.io/hc/en-us/articles/13112366068251) to help you determine which is right for you. 


 



#### A few things before we begin...


* We know that potentially losing access to MetaMask and your assets is stressful — that's why we've put this content together, so that you might be able to resolve that stress. We wish we could do more, but [MetaMask is self-custodial](https://support.metamask.io/hc/en-us/articles/360059952212) by design. We're rooting for you though!
* We do our best to keep these instructions up to date, but since they depend in part on the back end of third-party platforms (the browsers), sometimes things may have changed relative to what we describe below. If so, please let us know by [getting in touch with Support](https://support.metamask.io/hc/en-us/articles/360058969391).
* This is not a simple process, so make sure you set aside roughly 30 minutes and that you're in a location where you can focus. If you get stuck, get in touch.
* The final step of the process, once you've recovered your SRP, will be to [restore your wallet](https://support.metamask.io/hc/en-us/articles/360015289612). Keep in mind that **MetaMask stores only one SRP per browser profile at a time**, and **importing an SRP into an existing MetaMask installation wipes any SRP data** already present in that profile's vault.
	+ If you're only managing one SRP, then this isn't really an issue; **if you're managing multiple SRPs**, however, we strongly recommend you [follow our best practices outlined here](https://support.metamask.io/hc/en-us/articles/12174759849371).





Extension iOS Android


**Vault extraction and decryption instructions**
------------------------------------------------


If you’re here, you probably want to get straight to solving the issue. However, if you get stuck, it might help to understand what’s going on. We’ve provided an in-depth explanation of how this all works further down, in case you need it now, or want to read it another time.





**Chrome-based browsers**
#### (includes Chrome, Brave, Edge, and Opera)




Step One: Load the Vault Decryptor Tool
---------------------------------------


This tool was written by MetaMask co-founder Dan Finlay, and has recently been updated to be much more user-friendly. The decryptor can be accessed in a web page here:


<https://metamask.github.io/vault-decryptor/>


**If you’re concerned about someone having access to your computer over the Internet, you can load this page, and then disconnect your internet connection; it will work offline.**You can even download the code and run it on your machine, if you want to. The repository is [here.](https://github.com/MetaMask/vault-decryptor)


Step Two: Locate your Vault
---------------------------


When you load the tool, the easiest method by far of using it will be to click on "Database backup", then "Choose File":


  
![](https://support.metamask.io/hc/article_attachments/13473929359643)


At this point, a file explorer window will open, and you'll need to find the vault. 


**In Windows 10 or 11**, you should be able to find the location of the vault by going to this folder location (you need to be able to see the hidden files):


*C:\Users\USER\_NAME\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nkbihfbeogaeaoehlefnkodbefgpgknn*


**On a Mac,** the location of the folder should be:   
*Library>Application Support>Google>Chrome>Default>Local Extension Settings>nkbihfbeogaeaoehlefnkodbefgpgknn*


* If you're having trouble finding this location, try the following:
	+ Open a Finder window.
	+ Select Go -> Go to Folder... in the menu bar.
	+ Type ~/Library in the input field and click Go.


In that folder you'll see a file called 000003.ldb or something similar--**the specific number may differ, but it should be a low numerical value, like 000005 or 000004. If it is a larger number, it is not the vault:**


**![](https://support.metamask.io/hc/article_attachments/13474146474139)**


If you do try to decrypt a file that's not a vault, this will be the result:


![vault-notavault.png](https://support.metamask.io/hc/article_attachments/13474335273243)


 


 



#### Handling multiple vault files


If you have imported multiple SRPs into MetaMask on this system--and many of us have--you may have multiple vault files. You can decrypt each one, so long as you know its corresponding password.


**If you imported an SRP into MetaMask, and "lost" the SRP you had in MetaMask previously, that old SRP's vault file may still be on your system. You may be able to recover it using this process, so long as you know the password.**


If you have an idea of what your password was, but can't *quite*remember, you might want to try using [btcrecover,](https://btcrecover.readthedocs.io/en/latest/) a tool designed to help people manage and recover cryptographic keys. Specifically, it has functionality that automates the process of trying lots of different variations of a password. For an idea of what this process involves, check out [this chapter](https://youtu.be/TzZDcN6SnCU?t=266) of a btcrecover video tutorial.



When handling multiple vault files, keep in mind that they will likely have different numbers, although again, they should be low-value numbers, as stated above. Another important consideration is whether you used MetaMask in different browser profiles. If this is the case, or you think it may be, then it's worth looking. On Windows, this is a few levels up in the folder structure:


*C:\Users\<your-user-name-here>\AppData\Local\Google\Chrome\User Data*


In that directory, you should see a set of folders, one for each profile created: 


  
![](https://support.metamask.io/hc/article_attachments/13607345314843)


Within each of those directories, navigate to *Extensions*, and you'll see the familiar MetaMask extension ID. Follow the same instructions as above with each one of your profiles until you find the vault you're looking for. 


**Tip: If you're handling a lot of different vaults, you should probably make a list of which one is where, and which password goes to which!**


![](https://support.metamask.io/hc/article_attachments/13607383091995)


Step Three: Decrypt the vault
-----------------------------


This part is easy, so long as you know your password. Simply put in your password, hit "Decrypt", and your Secret Recovery Phrase should appear below the box:


  
![vault-ldbupload.png](https://support.metamask.io/hc/article_attachments/13474291339803)


 


**Now: back up your SRP, *in the order in which the words appear on the screen*, somewhere safe.**


We recommend multiple copies in physical locations, or encrypted, non-Internet connected locations that you trust to be safe.


If you want to know more about a common form of key storage, hardware wallets, follow [our guide here](https://support.metamask.io/hc/en-us/articles/5450173968283-User-Guide-How-to-use-a-Hardware-Wallet).


Now that you have your SRP, you can proceed to [import your SRP into MetaMask and restore access to your accounts.](https://support.metamask.io/hc/en-us/articles/360015289612-How-to-restore-your-MetaMask-wallet-from-Secret-Recovery-Phrase)





**Firefox**


#### Current Limitations of these instructions


Firefox has implemented changes to its data encoding that have made these instructions of limited use. If you have MetaMask installed in Firefox and know your password, the below instuctions may help solve your problem. If, however, you no longer have access to the browser or are attempting to recover an SRP from an old file system or backup, these instructions may not help, unless you are able to somehow access an instance of Firefox on that file system. As soon as we have a better solution, these documents will be updated.



In Firefox you may need to have the MetaMask extension opened in 'Expanded view' to be able to open the 'Inspect Element' or Web Inspector. Check out this video and follow the instructions below:


   
  
Open a new tab in Firefox and enter the following in order to find the extension's *UUID* (Universally Unique Identifier): 


**about:debugging#addons**


**![UUID_Firefox.png](https://support.metamask.io/hc/article_attachments/11188660768027)**


 


You should be able to see the UUID of the MetaMask extension. Copy it to add it to the following URL (without the spaces):


**moz-extension://<your-UUID-here>****/home.html**


![Extension_view_Firefox.png](https://support.metamask.io/hc/article_attachments/11188660817435)


This will open the MetaMask wallet in a browser tab in Firefox. 


* Right-click on the MetaMask wallet that's opened in the full-view tab to see the options
* Click the 'Inspect Element' option
* In the opened window, go to the Console tab
* Enter this command in the Console and click enter or return (you can copy+paste the following command):



```
chrome.storage.local.get('data', result => {  
 var vault = result.data.KeyringController.vault  
 console.log(vault)  
})
```

* This should return a result that begins " *{"data":* ". This is the vault data (which is in JSON format).
* Copy it to your clipboard.
* Proceed to the Vault Decryptor that you can find in the link below and also see the open-source code at [GitHub](https://github.com/MetaMask/vault-decryptor):


<https://metamask.github.io/vault-decryptor/> 


*This Vault Decryptor tool can also be used offline, you just need to use your browser's tool bar > File > Save page as... > MetaMask Decryptor.htm. Then open the **MetaMask Decryptor.htm** file in your browser with your computer disconnected from the Internet.*


 



* On the Vault Decryptor page, paste the *{"data":}* part of the vault data and use the password you set for your wallet in the MetaMask Extension and click the "Decrypt" button.
* If successful, you'll see the result below the Decrypt button showing the *"mnemonic"* 12 Word English Secret Recovery Phrase, along with any other imported *"Simple Key Pair"* (private key).  
  
You can now use the Secret Recovery Phrase (and private keys) to restore your MetaMask wallet.


* +


### **We urge you strongly to make sure that you always backup your Secret Recovery Phrase, and any manually imported private keys, so this never happens again.**





**Recovering an old SRP after importing another one (Chrome-based)**

### Did you import an SRP into MetaMask and lose your old one?


MetaMask can't detect multiple vault files, or switch between them--but if you imported an SRP to MetaMask, the vault might still be there, or in a backup of your system made at the time.


Currently, we only have a process for this on Chrome-based browsers, but we're working on it for Firefox, and we'll update this documentation when we have one. Follow the instructions above, under "Chrome-based browsers", and pay special attention to the note at the end of Step 2, regarding 'Multiple vault files'.





**Manual extraction method**

What if I can't upload my vault file? (Chrome-based browsers **only**)  
  

The Vault Decryptor tool's vault upload feature has built in order to avoid users having to step through a fair amount of manual work involved in finding, formatting, and extracting their vault data. However, if you're in a situation where, for whatever reason, you can't use that feature, the steps below may help.


Keep in mind that this process changes from time to time, without MetaMask being aware; this is due to the fact that Chrome can change the way it saves data to disk, for example; or [how it encodes data](https://blog.hubspot.com/website/what-is-utf-8), which affects this process. **If you notice such a change, please let us know--keeping these instructions up to date is a group effort! ❤️🦊**


#### Note: it is due to exactly these issues, encoding, that we currently **do not have documentation for this process in Firefox**. The team is actively working on resolving this, and as soon as we have a process, these documents will be updated.


**In Windows 10 and 11**, you should be able to find the location of the Vault by going to this folder location (you need to be able to see the hidden files):


*C:\Users\USER\_NAME\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nkbihfbeogaeaoehlefnkodbefgpgknn*


**On a Mac,** the location of the folder should be:   
*Library>Application Support>Google>Chrome>Default>Local Extension Settings>nkbihfbeogaeaoehlefnkodbefgpgknn*


* If you're having trouble finding this location, try the following:
	+ Open a Finder window.
	+ Select Go -> Go to Folder... in the menu bar.
	+ Type ~/Library in the input field and click Go.


In that folder you'll see a file called 000003.ldb or something similar--**the number doesn't matter, you're looking for .ldb files**. Open that file with a text editor or code editor software like Atom (https://atom.io/) or [sublimetext](https://www.sublimetext.com/). *Note: The screenshot below says file type 'text document' because it was already opened with a text editor.*


![screenshot_vault_location.PNG](https://support.metamask.io/hc/article_attachments/360017332831/screenshot_vault_location.PNG)


Once you've opened the file, search for the word "keyring". There will be a dense block of text following it (if using SublimeText, it might be easier to view it by clicking on "View" and "Enter Distraction-Free Mode"), which looks like this:


  
![mceclip0.png](https://support.metamask.io/hc/article_attachments/10204253413659)


**This is your vault data; however, we will need to re-format certain parts of it in order to be able to decrypt it: We'll need to make sure you have the "data", "iv", and "salt" sections properly labelled.**


In order to do this, we'll need to copy-paste your vault data to a new text editor file. Look at the section following "Keyring" in the text. There's a section that reads **{\"???'<0x04>\"**. That's the beginning of your vault data. Now look for the word "salt". Following "salt" there's a long string of alphanumeric characters in quotation marks, and that section ends with **=\"}***. That's the end of your vault data,*so **copy from the opening curly bracket following "Keyring" to the closing curly bracket following the alphanumeric characters after "salt", and paste into a new text editor document.**


 


Whew! Now's the easy part. I promise.


**"data":**


You already saw this part of the text: **{\"???'<0x04>\"** Keep in mind that yours might look a little different; it might be a different code between the triangle brackets, for example. In any case, make this part of the text look like: **{"data"**


**"iv":**


This isn't always changed; in the screenshot above, for example, they're functional as-is. If your code looks like that, you're good to go!


**"salt":**


Like with "iv", look to make sure "salt" looks like it does in the screenshot above. Additionally, make sure that the entire text block ends like this: ="} **not like this:** =\"}"}


**remove slashes:**


Use the Search and Replace feature of the editor to change all the **\"** to **"**(removing them):


 


![mceclip2.png](https://support.metamask.io/hc/article_attachments/10206783991451)


 


You would now have something like this:


*{"data":"wwpXXtFCqZkYsWfeEwItZjJ0Cc7mRVjG47Dqh+ztL1PiCG6Izhg+zG0mM+H2ykyjz3X0RNhAE6IVsWFZamcZ47B4sVi4SvUxrMhARm5L3yHPxr3UsyGrOXmthyVMgEGmjwlmnFCNd2nMZ2o8/sRMra8FupurqevnBv57FiYpEEs7gPpFHv6587aL44MmKD8Snv4JLFqiqmlK82Waq5F+Iv9mw2sFVAL9mgZBSgFgbWdB3TsKVB2k","iv":"rkUQlNcGTxBE0My7a/bCXw==","salt":"HcKyNfGzaRALRQ0DlKgcIe5Uk30iI/M//oG6w8vX8Nk="}*


* **Note: upon opening the .ldb file in sublimetext,** you may get thousands of lines of something that looks like the following:  
  
![mceclip0.png](https://support.metamask.io/hc/article_attachments/4405814045723/mceclip0.png)  
  
If this is the case, click on **File>Reopen with Encoding>UTF-8**. At this point, you can search for "vault" and find the data you need.


#### **OK! That's it! You're ready to decrypt!**


 


You can now go to the Vault Decryptor (<https://metamask.github.io/vault-decryptor/>) and paste the vault data there, then enter the password you set for the extension when you created your MetaMask wallet. You should be able to see your secret Seed Phrase / Secret Recovery Phrase and any manually imported private key below if you click the Decrypt button.


 








#### iOS method currently unavailable


We've recently become aware that the iOS recovery method is no longer working. We're investigating the cause and will update this page when we have updated instructions.


However, and like Android, iOS devices now have an automated vault recovery method built-in. With v6.3.0 or later, if MetaMask detects any kind of problem with the vault files required to load MetaMask, the app will initiate an automatic recovery sequence.


Note that this is *not* like the vault extraction method described above for Chrome-based browsers, and cannot be initiated manually.



### **In order to recover your vault data, you will need:**


* You **must have had** iCloud backup enabled in your iCloud settings while the app was being used.
* The password that was used on MetaMask Mobile when the vault was created (or restored on that device)
* MacOS running on a separate computer or laptop, other than the mobile device in question
* An app capable of displaying JSON data in a readable fashion. You may need to download one, for example: <https://imazing.com/download/macos>
* A WiFi connection or the appropriate cable to sync your phone and your computer


### **Procedure**


* Connect the mobile device to the computer, either via wifi or a physical cable, so that the mobile device appears in your Finder.  
	+ Search for the word "KeyringController"
	+ Copy and paste that JSON object into a new document. It will look something like this:
	
		- {\\\\\\\\\\\\"cipher\\\\\\\\\\\\":\\\\\\\\\\\\"JaX8Z80QMzzqA4XMgPsUuleNLIuxvchXZ5q1SO9GO1kuNUmokUke06op9EF0ZU4WXsILfUZ0yKI5kjzYY9H12t5aGb43BOAWJwlKuC8neXWeL5enoD/L05eDC9tzZEBupLwF7cGG6JdPHHQKdRDWWbQM+TUo6EvZv7LClPZQVJ17uowGvPMPB0UwfPea7DP/dE5DYleHmX1rhxAJr1YN4HUPAYpCCReU4W4/2QsaM+E=\\\\\\\\\\\\",\\\\\\\\\\\\"iv\\\\\\\\\\\\":\\\\\\\\\\\\"dcabe6ed590ae3ee8e056c7844c58047\\\\\\\\\\\\",\\\\\\\\\\\\"salt\\\\\\\\\\\\":\\\\\\\\\\\\"h6IkHlWjloB9c9+KiGgYvQ==\\\\\\\\\\\\",\\\\\\\\\\\\"lib\\\\\\\\\\\\":\\\\\\\\\\\\"original\\\\\\\\\\\\"}
+ Back up the mobile device as per the instructions [here](https://support.apple.com/guide/iphone/back-up-iphone-iph3ecf67d29/ios) under 'Backup your iPhone using your Mac'. We recommend using the *encrypted option*, and **making a note of the password for later.**
+ Select Manage Backups
+ Show in Finder
+ Drag the backup folder into the iMazing app, or whichever app you're using to read the backup. **This is the point at which you'll need your password if you encrypted the backup.**
+ In the backup tool, navigate to Apps->MetaMask->Documents->persistStore->persist-root
+ Open the persist-root file. It will be a lengthy file in JSON format.
+ Modify the object to reflect the example below (manually remove all \\\ and ensure there are no white spaces):
+ {"cipher":"JaX8Z80QMzzqA4XMgPsUuleNLIuxvchXZ5q1SO9GO1kuNUmokUke06op9EF0ZU4WssILfUZ0yKI5kjzYY9H12t5aGb43BOAWJwlKuC8neXWeL5enoD/L05eDC9tzZEBupLwF7cGG6JdPHHQKdRDWWbQM+TUo6EvZv7LClPZQVJ17uowGvPMPB0UwXPea7DP/dE5DYleHmX1rhxAJr1YN4HUPAYpCCReU4W4/2QsaM+E=","iv":"dcabe6ed590ae3ee8e056c7844c583d7","salt":"h6IkHlWjloBgc9+KiGTYvQ==","lib":"original"}
+ Now you can copy the vault payload into the mobile app.
+ Start up the MetaMask app on your iPhone and go to the Wallet Setup screen select “Import using Secret Recovery Phrase”


* In the Import using Secret Recovery Phrase screen, you can paste the vault into the seed phrase text box and then the password you want to try to unlock the vault in the password text boxes (passwords have to be the same). This is the password that was used when this vault was created or restored on this device. If the vault can be decrypted by the password, your wallet will be successfully set up.
+ Import using Secret Recovery Phrase (example image):   
![c2fc390b-7415-4b83-b89c-5533d8653b70.png](https://support.metamask.io/hc/article_attachments/4411049951131/c2fc390b-7415-4b83-b89c-5533d8653b70.png)


+ On successful setup of your wallet you should **REMEMBER to back up your seed phrase after your wallet is set up.**


 




We are currently working on a solution for Android; as soon as it is available, we will post it here.


However, and like iOS, MetaMask for Android now has an automated vault recovery method built-in. With v6.3.0 or later, if MetaMask detects any kind of problem with the vault files required to load MetaMask, the app will initiate an automatic recovery sequence.


Note that this is *not* like the vault extraction method described above for Chrome-based browsers, and cannot be initiated manually.




 


### **We urge you strongly to make sure that you always backup your Secret Recovery Phrase, and any manually imported private keys, so this never happens again.**

