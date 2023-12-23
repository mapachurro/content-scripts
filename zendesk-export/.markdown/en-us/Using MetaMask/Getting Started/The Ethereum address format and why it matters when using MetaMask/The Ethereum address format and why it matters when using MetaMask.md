When you create a MetaMask account, or [add a new account](https://support.metamask.io/hc/en-us/articles/360015289452-How-to-create-an-additional-account-in-your-wallet) to your wallet, you're given a unique **public address**. 


On Ethereum and other networks compatible with the Ethereum Virtual Machine (EVM), **public addresses all share the same format: they begin with *0x*, and are followed by 40 alphanumeric characters** (numerals and letters), adding up to 42 characters in total. They're also *not*case sensitive.


This address is a number, even though it also includes alphabetical characters. This is because the hexadecimal (base 16) system used to generate the address doesn't just use numerals, like our ten-digit decimal system. Instead, the hexadecimal system uses the numerals 0-9 *and* the letters A-F. This means it has 16 characters at its disposal, hence the name base *16*. In computer science and many programming languages, the 0x prefix is used at the start of all hex numbers, as they are known, to differentiate them from decimal values. 


**How does this affect your daily use of MetaMask?**
----------------------------------------------------


### Interoperability: use the same address on different networks


As mentioned above, EVM-compatible networks all share the Ethereum address format. This is because they're generally 'hard forks', based heavily on Ethereum's design, or share key fundamentals. Not all are derived directly from Ethereum, though — many were developed separately and designed for compatibility. Reflecting much of the same architecture naturally lends itself to sharing address formats too. 


Due to these shared characteristics, you can use MetaMask to [interact with any other EVM-compatible network](https://support.metamask.io/hc/en-us/articles/4404424659995-User-Guide-Custom-networks-and-sidechains) **using the same address**. This includes networks such as:


* [Polygon](https://support.metamask.io/hc/en-us/articles/4415758346267)
* [BSC (BNB Chain)](https://support.metamask.io/hc/en-us/articles/4415758120219)
* [Fantom](https://support.metamask.io/hc/en-us/articles/4415758161435)
* [Avalanche (C-Chain)](https://support.metamask.io/hc/en-us/articles/4415758179355).


Try it out: [add a network](https://support.metamask.io/hc/en-us/articles/360043227612) to MetaMask, or switch over from one you've already added. Notice how your account and its address stay the same. This means your MetaMask address on both Ethereum mainnet and BSC, for example, is exactly the same. 


However, the interplay of networks and tokens (particularly the question of [ERC-20 variants](https://support.metamask.io/hc/en-us/articles/4405497827355-User-Guide-Tokens#:~:text=ERC%2D20%20Tokens,add%20it%20manually.) of native tokens) can be complex and is not without risk, so please always do your research before sending a transaction. A network's native tokens are unlikely to be interchangeable with the (ERC-20) version that you can send and receive on MetaMask, for example. 


For information on some of the most prominent EVM-compatible networks you can use with MetaMask, head to our [network profiles page](https://support.metamask.io/hc/en-us/articles/4415750833691). Follow the link to the network you're investigating to read more about bridging, tokens, and the nuances of its use. 


### Interacting with networks that have different address formats: be careful!



#### tl;dr


**Don't use MetaMask with any addresses that don't use the Ethereum format**, either when sending or receiving. This is in addition to the fact **you should never send tokens straight from one network to another without bridging**. (There are some cases where you won't lose them, but in most scenarios, you will.) You could, for instance, send tokens on Polygon to your MetaMask address, and be able to view them in MetaMask — presuming you have the Polygon network and the tokens themselves added. However, you would not be able to use these tokens on Ethereum, despite the ease with which you can switch over to mainnet in MetaMask. You'd need to bridge the tokens over separately.


Check out our [Field Guide to Bridges](https://support.metamask.io/hc/en-us/articles/4836913606683) for more information.



Whilst MetaMask is a flexible passport to accessing Ethereum and EVM-compatible chains, there are **some cases where you need to exercise caution** when it comes to address formats:


* **EVM-compatible networks with different formats**. Just because a network is EVM-compatible does not necessarily mean it uses an *0x*address in all circumstances. The Harmony network, for example, is fully EVM-compatible, but [allows users to switch between an *0x*and *one1*version of their address](https://support.metamask.io/hc/en-us/articles/4415758143387-Network-profile-Harmony-ONE-#:~:text=Are%20my%20MetaMask,information%2C%20see%20here.%C2%A0) (although the number which follows this prefix is the same). Others, like Avalanche, have multiple chains with varying levels of EVM support ([you should only interact with Avalanche C-Chain on MetaMask](https://support.metamask.io/hc/en-us/articles/4415758179355-Network-profile-Avalanche-AVAX-#:~:text=Is%20my%20Avalanche,bridge%20them%20over.%C2%A0)).
* **Non-EVM-compatible networks: stay away**. As flexible as MetaMask is, you cannot interact with non-EVM-compatible networks on completely different blockchains. The most obvious example would be Bitcoin, whose address format is completely different. If the blockchain has nothing or little to do with Ethereum, it is unlikely to be usable with MetaMask.
