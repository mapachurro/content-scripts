eth\_sign is a transaction signing method that is now disabled by default in MetaMask. Interacting with dapps that use this method may put your funds at risk, so you should only turn it on (in Settings > Advanced) when you are absolutely sure that you want to use it.


![MetaMask_eth_sign_settings.png](https://support.metamask.io/hc/article_attachments/17358130003995)


What is eth\_sign?
------------------


`eth_sign` is one of several transaction signing methods built into MetaMask. 


Signing transactions is a fundamental function of your wallet: you use your public and private key pair to generate cryptographic signatures that immutably verify that you are the originator of the transaction. To request your signature, developers add methods to their code that are triggered at specific times. eth\_sign is one example.


You can read more about transaction signing in the [MetaMask docs](https://docs.metamask.io/guide/signing-data.html).


 


Why is it disabled by default?
------------------------------


eth\_sign is one of the oldest signing methods that MetaMask still supports. Back in the early days of MetaMask when it was originally designed, web3 was quite different from the present day. There were fewer standards for signatures, so eth\_sign was developed with a fairly simple, open-ended structure. 


The main thing to note about eth\_sign is that it allows the website you're on to request that you sign an *arbitrary hash*. In this mathematical context, 'arbitrary' means unspecified; your signature could be applied by the requesting dapp to pretty much anything. eth\_sign is therefore unsuitable to use with sources that you don't trust.


Additionally, the way eth\_sign is designed means that the contents of the message you're signing are not human-readable. It's impossible to check up on *what you're actually signing*, making it particularly dangerous. 


 


Should I turn it on?
--------------------


Firstly: **if you're in contact with someone asking you to enable eth\_sign, you should be very, very wary**. There are several much-improved signing methods available in MetaMask for dapps, and the vast majority of pages should be using these more secure alternatives. 


If you're not being asked to turn on eth\_sign for a specific purpose, but you're still considering it anyway, please be careful. **Do your due diligence on the dapp** that requires it, and consider your actions fully before taking them:


* Does the dapp/protocol have a named, contactable team?
* Do other verifiably independent users vouch for its trustworthiness?
* Is the transaction in question worth the risk?
* Are you being confronted with something that, on reflection, is probably too good to be true?


This is not a decision you should take lightly if you value your assets. Even if you're confident, your wallet could still be compromised or funds stolen. This is why we disable eth\_sign by default.


These are just example considerations; we have other resources to help you assess the trustworthiness of web3 third parties [here](https://support.metamask.io/hc/en-us/articles/10143114273563) and [here](https://support.metamask.io/hc/en-us/articles/4403988839451). If you want to read more about various phishing and scam methods you could encounter—which could feasibly be using eth\_sign—check out our [Staying Safe in Web3 database](https://support.metamask.io/hc/sections/11294597751963). 


 


Why not just remove it altogether?
----------------------------------


eth\_sign is still available to use in MetaMask because **removing it would make some dapps and websites unusable**. It's also in use in many well-intentioned ways, particularly by developers or users of internal-facing dapps that *can*completely trust the transactions they're signing because they know who they're working with. 


Most protocols should have upgraded to newer, improved signing methods, so it's unlikely that disabling eth\_sign will impact your day-to-day activities in web3. 

