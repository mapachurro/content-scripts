Backing up your Secret Recovery Phrase in several secure locations is a must-do when using MetaMask. That's because you're the [custodian of your accounts](https://support.metamask.io/hc/en-us/articles/360059952212): **no one can ever stop you from accessing those accounts or using your web3 identity, so long as you know those secret words**.


This also means that if you don't know those secret words, or have them recorded somewhere safe, they will be impossible to guess, and **no one will be able to help you get them back**: not MetaMask, and definitely not someone offering to help you in a DM on Discord.


But no one is perfect, and mistakes happen. If you find yourself in a situation where you realize you don't have your Secret Recovery Phrase and need it, **don't panic: just follow the prompts below to try and get your SRP back.**


*...and then back it up!*


 


### How to find your Secret Recovery Phrase


You'll be able to find your SRP in several different places, depending on your situation:




**I imported another SRP into MetaMask Extension, and now I can't access my old SRP**

*Please note: this process applies currently to MetaMask Extension only; this information will be updated if and when it becomes available in Mobile.*


**Good news: You might be able to get your old SRP back.** To jump straight in, follow the link below; if you want to understand what's going on here, read on:


MetaMask can only hold and manage one SRP at a time, due to technical issues relating to how MetaMask and the browser work together.


Therefore, if you already have an SRP in MetaMask, and then you import another, MetaMask simply "forgets" about the first one--you can't switch back and forth. However, **the vault data is still on your system's storage**, unless you have uninstalled the extension entirely since importing the second (or third, or fourth) SRP.


In order to find your old SRP and decrypt it, follow the instructions below, keeping in mind that **you'll be dealing with multiple vaults in the same directory**, so you might have to cycle through several vault files before you find the one you're missing:


[How to recover your Secret Recovery Phrase](https://support.metamask.io/hc/en-us/articles/360018766351)


And remember, make sure **no one can see your screen** while you go through this process!


**Note: If you have an idea of what your password was, but can't *quite*remember,** you might want to try using [btcrecover,](https://btcrecover.readthedocs.io/en/latest/) a tool designed to help people manage and recover cryptographic keys. Specifically, it has functionality that automates the process of trying lots of different variations of a password. For an idea of what this process involves, check out [this chapter](https://youtu.be/TzZDcN6SnCU?t=266) of a btcrecover video tutorial.


*This project is not affiliated with or endorsed by MetaMask or Consensys, and you should make your own decision about whether or not to use it.*
 





**I have MetaMask installed, I know my password, and can log in**

**Good news: MetaMask has a function built in for you to reveal your SRP so that you can back it up.** 


Make sure that no one is able to see your screen when you reveal it!


Instructions here: [How to reveal your Secret Recovery Phrase](https://support.metamask.io/hc/en-us/articles/360015290032)





**I have MetaMask installed, I know my password, but I can't log in**

**Good news: You might be able to get your SRP back.**


Sometimes things break; sometimes no matter how many times you type your password correctly, you type it wrong. Sometimes, we mistyped the password when we set it!


Whatever the reason, if you can't get into MetaMask, but you know the password--or have a good idea about what your password was--there are some processes you can follow to recover your SRP.


If you're sure you know your password, start with these instructions:


[How to recover your Secret Recovery Phrase](https://support.metamask.io/hc/en-us/articles/360018766351)


If your password seems to be the issue, but you have an idea of what it might be, there's a tool that can help you try lots of different options, called [btcrecover](https://btcrecover.readthedocs.io/en/latest/). For an idea of what this process involves, check out [this chapter](https://youtu.be/TzZDcN6SnCU?t=266) of a btcrecover video tutorial.


*This project is not affiliated with or endorsed by MetaMask or Consensys, and you should make your own decision about whether or not to use it.*


If you manage to figure out your password using btcrecover, the tool should decrypt the vault for you, and display your SRP--so make sure no one can see your screen while you use that tool! If btcrecover doesn't show you your SRP, or you figure out your password through some other method, then follow the steps above to recover your SRP.





**I have MetaMask installed and don’t know my password, and can’t log in**

This is a tough situation. The SRP is the cryptographic key that creates and restores all your accounts, but within MetaMask, your password is the thing that encrypts that SRP on your system's storage, and that encryption is *very* secure. Without your password, you won't be able to recover it.


So, if you have an *idea* of what your password might have been, you might want to try using [btcrecover,](https://btcrecover.readthedocs.io/en/latest/) a tool designed to help people manage and recover cryptographic keys. Specifically, it has functionality that automates the process of trying lots of different variations of a password. For an idea of what this process involves, check out [this chapter](https://youtu.be/TzZDcN6SnCU?t=266) of a btcrecover video tutorial.


*This project is not affiliated with or endorsed by MetaMask or Consensys, and you should make your own decision about whether or not to use it.*


If you manage to figure out your password using btcrecover, the tool should decrypt the vault for you, and display your SRP--**so make sure no one is able to see your screen while you use that tool!** If btcrecover doesn't show you your SRP, or you figure out your password through some other method, then follow the steps here to recover your SRP:


[How to recover your Secret Recovery Phrase](https://support.metamask.io/hc/en-us/articles/360018766351)





**I have MetaMask Mobile installed, don’t know my password, but I can log in using biometrics**

**The current solution to this situation may be simply to migrate your assets to a new SRP.**




Android iOS


Various efforts are currently underway to document the process for vault recovery on Android.


If you find yourself in this situation, it might be best to move your assets to a new SRP, as we don't currently have a timeline for when vault recovery on Android will be available and documented. For instructions on how to do so, see our [guide on wallet migration](https://support.metamask.io/hc/en-us/articles/4867408571803).




While we have a process documented for iOS, there can be changes on Apple's side that break the process.


Start by following the instructions in the article below, and if they don't work, go to support.metamask.io, and start a conversation with a Support agent for more help:


[How to recover your Secret Recovery Phrase](https://support.metamask.io/hc/en-us/articles/360018766351)







**MetaMask was installed on a system that I can't access directly, but I have access to the system files (a backup, the computer's hard drive, etc) and know the password**

**Good news: You might be able to get your SRP back.**


The particulars of this situation can vary wildly, and can affect the success of the operation. Some people have an old hard drive hooked up to a USB adapter, or have a system backup image mounted as a virtual drive. Still others are accessing a system backup in the cloud.


Providing guidance on how to get access to your system backup is well outside the scope of this article. However, if you can access the file system and the MetaMask installation is there, we can guide you.


If you're sure you know your password, start with these instructions:


[How to recover your Secret Recovery Phrase](https://support.metamask.io/hc/en-us/articles/360018766351)


If your password seems to be the issue, but you have an idea of what it might be, there's a tool that can help you try lots of different options, called [btcrecover](https://btcrecover.readthedocs.io/en/latest/). For an idea of what this process involves, check out [this chapter](https://youtu.be/TzZDcN6SnCU?t=266) of a btcrecover video tutorial.


*This project is not affiliated with or endorsed by MetaMask or Consensys, and you should make your own decision about whether or not to use it.*


If you manage to figure out your password using btcrecover, the tool should decrypt the vault for you, and display your SRP--so make sure no one is able to see your screen while you use that tool! If btcrecover doesn't show you your SRP, or you figure out your password through some other method, then follow the steps above to recover your SRP.





**I uninstalled the MetaMask extension entirely**

**Depending on your situation, it might be possible to recover your SRP.**


If you need to do this, follow [our guide on Account Migration here](https://support.metamask.io/hc/en-us/articles/4867408571803).


This is a tough situation; browser extension data is deleted when the extension is uninstalled. Generally, this means that your vault data is gone. However, it may have been preserved somewhere, especially if you have automated full operating system backups. If you manage to find a backup of your vault data, then follow the instructions above, under the heading "MetaMask was installed on a system that I can't access directly, but I have access to the system files (a backup, the computer's hard drive, etc) and know the password".


We are continuing to investigate this situation to determine how we can better protect users from SRP loss due to an extension uninstall.




