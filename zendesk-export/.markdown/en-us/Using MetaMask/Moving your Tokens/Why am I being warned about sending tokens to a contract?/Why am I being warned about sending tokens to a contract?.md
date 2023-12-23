MetaMask tries to make sending and receiving ERC-20 tokens simple & safe.


When sending tokens, you should always double-check that you're sending to the proper address, controlled by either another user, an account you own, or a dapp with which you're interacting. 


**MetaMask will warn you when sending tokens to the address of a token contract.** Many users accidentally "burn" (**lose forever**) their tokens by sending to the address of the token contract, so if you're sending to a token contract, we want to make sure you're doing it intentionally. 


If you're seeing a warning that looks like this on your send screen, we've detected that the recipient address you've entered is the address of a token contract: 


![Known_contact_address_warning_MetaMask.png](https://support.metamask.io/hc/article_attachments/10057363978395)


ERC-20 tokens are controlled by a smart contract that tracks the balance of the token. For example, the GNO token is tracked by a contract at address *0x6810e776880c02933d47db1b9fc05908e5386b96*. If you visit that address on [Etherscan](https://etherscan.io/address/0x6810e776880c02933d47db1b9fc05908e5386b96), you'll see plenty of calls to the contract.


Most of them are function calls that originate from a token holder (like you!), and supply a destination address and token amount. This tells the GNO contract to transfer a certain amount of tokens from the sender's balance to the recipient's balance. 


Unlike your ETH balance, which is tracked in actual blocks on the Ethereum blockchain, token balances are tracked on a contract that runs on the blockchain — basically a mini-ledger of which address owns how many tokens. 


When you send tokens through MetaMask, we already know which token contract should receive the transaction. The 'to' field is specifically for the address of the **recipient** — who you want to receive the tokens. When you click "Send," you're submitting a transaction to the appropriate token contract, telling it to transfer the specified number of tokens from your balance to the recipient's balance. **If the recipient is the token contract itself, those tokens may be lost forever!**


 

