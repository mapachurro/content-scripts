
#### New security alerts system


Partnering with Blockaid, we recently launched a new privacy-preserving alternative to the API-based security alerts system described here. Find out more [here](https://support.metamask.io/hc/en-us/articles/19878220833947).


Please note that you can only have one of these security alerts systems turned on at any time.




#### Using security providers does not guarantee safety


The services of third-party security providers can better inform you about transactions you're signing, and issue additional warning messages in MetaMask when you might be interacting with an unsafe dapp.


However, **this feature cannot prevent you from signing a transaction that might result in loss of funds**. You should still exercise good web3 safety habits like researching dapps and contracts before you interact with them. MetaMask is a [self-custodial wallet](https://support.metamask.io/hc/en-us/articles/360059952212), meaning only *you* are able to sign transactions, but also that we—or anyone else—cannot intervene, stop you, or reverse transactions. 



The most common way that scammers attempt to steal assets is by manipulating you into signing transactions or signature requests that carry out actions you don't actually want. 


Usually, this surfaces in the form of malicious [token approval](https://support.metamask.io/hc/en-us/articles/6174898326683) requests that aim to get control of all of your wallet's assets of a certain type, such as an ERC-20 token or an NFT collection. Bad actors rely on a range of tactics to be successful, but a significant element of the playbook is to make it as difficult as possible for the user to properly understand what they're signing.


**This is where transaction security checks come in**. This service is offered by third-party providers that analyze transactions or signature requests and advise, based on their records, whether it is potentially unsafe.


To start with, we've partnered with OpenSea and Blockaid, and may add other security providers in future.


Learn more below:




**How do I turn on the security provider feature?**

Head to 'Settings' > 'Experimental' and toggle 'Enable security alerts'. 


![MetaMask enable transaction security providers settings](https://support.metamask.io/hc/article_attachments/17272353279899)


 


At the moment, this option is only available on Extension. Once we're ready, we'll add it to Mobile too.





**Who actually are the security providers? Which ones are available?**

Security providers are third-party, web3 organizations that maintain a database, so to speak, of fraudulent dapps.


The first security providers available in MetaMask are OpenSea and Blockaid.





**How do security providers' checks work?**

Security providers are third-party organizations that interpret transaction data on your behalf. Here's how it works:


1. When the dapp, network, and transaction type you're about to use are all supported by the security providers you have turned on, MetaMask will first send the transaction data to the security provider, rather than straight to the dapp itself. This is done by requesting a response from the security provider's API.
2. The security provider processes the transaction data and returns information on whether the transaction is safe or not.
3. The received information is displayed in MetaMask.
4. Having reviewed the security information provided, you can choose whether or not to proceed with the transaction.


When you use this feature, **MetaMask does not prevent you from doing anything**. It's important to note that **you can still get scammed with this feature turned on**; instead, our objective is to provide you with as much of the best, clear information we can about the transaction. Armed with this, you can then make a more informed choice about whether or not to proceed.


Remember: MetaMask is a [self-custodial wallet](https://support.metamask.io/hc/en-us/articles/360059952212), and*you alone have control over your wallet and assets*. We cannot and will not restrict your agency.





**If I turn this on, what data am I sharing with security providers?**

For this feature to work, MetaMask must share certain data points with the security provider. This is data that you'd normally be sharing with the dapp you're interacting with anyway — data that you need to send as part of your signed transaction. This includes:


* The **web address** of the dapp (here referred to as the 'host') you're using.
* The ***JSON-RPC*** ***method***the dapp/host is using. JSON-RPC methods are essentially defined ways to request information from the network — see [here](https://docs.infura.io/infura/networks/ethereum/json-rpc-methods) for more information.
* The **chain ID** of the network.
* The **data** the dapp is sending with its request. This varies depending on the dapp and the context.


 





**What kind of information will the security provider give me?**

To assess whether the transaction you're about to make is secure, your transaction data is checked against the records of the security provider. MetaMask will then receive and display the results of these records, with the message variable depending on the security provider's data. If, for example, the data matches a URL marked as potentially dangerous, you'll see a message flagging this.


Every entry in the security provider's database flagged as 'Unsafe' (or similar wording) will have a 'reason' attributed to it, which explains the designation. The exact message depends on the *reason* that the security provider has recorded.




