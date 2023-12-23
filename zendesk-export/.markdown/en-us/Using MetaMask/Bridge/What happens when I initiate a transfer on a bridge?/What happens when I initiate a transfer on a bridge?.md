1. If you’re transferring an ERC-20 token, you’ll need to sign a [token approval](https://support.metamask.io/hc/en-us/articles/6174898326683-What-is-a-token-approval-) from your wallet, enabling the bridge to access the tokens on the source network.
2. **Source network transaction**: You sign a transaction to deposit your tokens into the bridge on the source network. The cost of the transaction—which is the only one you’ll need to sign in the bridging process—is: transfer amount + bridge provider fees + gas fees + the MetaMask fee (for more on fees, see [here](https://support.metamask.io/hc/en-us/articles/10056707767963)).
3. **Destination network transaction**: The bridge provider will initiate the transaction on the destination network once the transaction in step 2 has been validated. You don’t need to pay for this step, as its costs are usually covered by the fees you’ve paid in step 2.


You’ll be able to track the status of each bridge within our platform.

