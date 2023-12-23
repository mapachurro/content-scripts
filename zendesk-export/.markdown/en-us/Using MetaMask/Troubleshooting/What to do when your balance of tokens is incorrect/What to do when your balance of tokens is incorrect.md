
#### Tokens not showing up at all?


See our guide to troubleshooting this issue [here](https://support.metamask.io/hc/en-us/articles/360059232852).



First of all, verify the token balances shown on the block explorer and compare with MetaMask. You do this by copying your wallet address and pasting it into the block explorer corresponding to the network you're on — Etherscan for Ethereum mainnet, Arbiscan for Arbitrum, etc. For detailed instructions, see [here](https://support.metamask.io/hc/en-us/articles/360057536611).




Extension Mobile


If your MetaMask Extension is displaying the incorrect or inaccurate balance for ETH or other tokens, try the steps below one by one until you see your balance correctly.


**Before proceeding, make sure that you have your [Secret Recovery Phrase](https://support.metamask.io/hc/en-us/articles/4404722782107-User-Guide-Secret-Recovery-Phrase-password-and-private-keys) backed up in a safe place.**


1. Check that your internet connection is strong and stable. If not, MetaMask may be unable to load the correct balances.
2. Close down your browser where you have the MetaMask extension installed and open it again.
3. Try switching off any ad blockers you have installed, or, if you're using a VPN, try using MetaMask with it turned off.
4. Switch to a different network and back again. To do this, click on your current network at the top of the app. Select a different network, and then switch back to your original network again.
5. Make sure you're not experiencing a [browser permissions issue](https://support.metamask.io/hc/en-us/articles/360038139452-MetaMask-states-Balance-may-be-outdated-displays-in-orange-or-ETH-not-added-to-balance).
6. Try a different RPC URL, if there is more than one available for the network you're using. You can edit the RPC URL by going to Settings > Network, and then clicking the network in question. See our [article on adding networks](https://support.metamask.io/hc/en-us/articles/360043227612) for more information.
7. Install MetaMask using another supported browser (Firefox, Chrome, Brave, Edge) from our official website [https://metamask.io](https://metamask.io/) , and then try restoring your wallet using the 12-word Secret Recovery Phrase in case the issue is only present in the browser you are currently using.




Once you've verified on Etherscan that the amount of tokens being displayed in MetaMask Mobile is incorrect, follow these steps:


1. Make sure your internet connection is strong and stable. If it isn't, token values may not be up to date.
2. Change to a different network and then switch back again.
3. Change the RPC URL of the network you're on to an alternative, where possible. See our [article on adding networks](https://support.metamask.io/hc/en-us/articles/360043227612) for more information.
4. Hide the token, following instructions [here](https://support.metamask.io/hc/en-us/articles/360015489031-How-to-add-unlisted-tokens-custom-tokens-in-MetaMask#h_01FWH499MRDT5QC4R3KNPQNRWB), and then re-add the token, following instructions [here](https://support.metamask.io/hc/en-us/articles/360015489031-How-to-add-unlisted-tokens-custom-tokens-in-MetaMask).


**If the token in question is a network native token for a network other than Ethereum** (BNB, AVAX, MATIC, etc), try [deleting the network](https://support.metamask.io/hc/en-us/articles/4502810252059-How-to-remove-networks) and then [re-adding it](https://support.metamask.io/hc/en-us/articles/360043227612-How-to-add-a-custom-network-RPC).  
  
**If the token in question is ETH, then make sure that your [Secret Recovery Phrase](https://support.metamask.io/hc/en-us/articles/4404722782107-User-Guide-Secret-Recovery-Phrase-password-and-private-keys) is backed up in a safe place**, and reinstall the app.

If you're still encountering issues after trying these steps, please get in touch with us via the 'Start a Conversation' button on our [support page](https://support.metamask.io/hc/en-us).



#### Does the token have built-in mechanisms that affect supply or value?


Ethereum and EVM-compatible chains are home to an enormous variety of tokens with different utilities. Some tokens are designed to dynamically change supply or value according to various conditions:


* [Rebase tokens](https://support.metamask.io/hc/en-us/articles/4405497827355-User-Guide-Tokens#:~:text=Elastic%20supply%20/%20Rebase%20/%20Algorithmic%20tokens), where token supply is adjusted
* Tokens with 'taxes' applied to transactions of different kinds (e.g. simple transfer, swap, sell, etc.). These are sometimes referred to as 'fee on transfer' tokens.


Before you conclude that your balance is incorrect, check whether any similar conditions apply to your token. You can usually find this information by checking the project's white paper or documentation.


