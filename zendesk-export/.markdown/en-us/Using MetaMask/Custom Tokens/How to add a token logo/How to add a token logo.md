**This article is intended for token developers; if you simply want to see tokens in your wallet that you think you own but aren't appearing, consult [this article](https://support.metamask.io/hc/en-us/articles/360015489031).**


The token search box and the auto-detect functions are a part of a centralized solution. We encourage developers to use the EIP-747 method, which you can find in MetaMask's technical documentation:<https://docs.metamask.io/guide/registering-your-token.html#registering-tokens-with-users>


In the above link, you can find instructions on how to integrate the *wallet\_watchAsset* API as defined in EIP-747 without having to create code, and also a more advanced code example that includes the option to set a logo or icon for your token. This will let your users add your token to their MetaMask wallet, and see it, easily.

