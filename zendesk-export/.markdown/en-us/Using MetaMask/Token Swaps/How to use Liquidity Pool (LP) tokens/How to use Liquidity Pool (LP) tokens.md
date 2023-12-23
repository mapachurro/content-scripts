### Several of the most powerful decentralized finance (DeFi) tools involve depositing tokens into *liquidity pools*. In exchange, the depositor is given *Liquidity Pool Tokens*. These can be put to use — **but if you misuse them, you can lose all your value.**


Liquidity Pool tokens are an interesting token type, as they can be minted in a variety of ways. Uniswap currently mints them as ERC-721 tokens, whereas SushiSwap mints them as (often fractions of) ERC-20 tokens. What's really crucial to understand is not just what they're made of, but ***what they represent*, and what this means about what you can do with them.**


Let's say you deposit $2000 USD in stablecoins and 0.5 ETH into a liquidity pool. You've put (at today's prices) about $4K USD into that pool. Let's say that, in exchange, you're given 200 liquidity pool tokens. Each one of those tokens represents a proportional part of your deposit, in this case $10 USD and 0.0025 ETH (at the time of deposit; price fluctuations can and will change this, this is another topic, known as '[impermanent loss](https://consensys.net/blog/metamask/impermanent-loss-defi-markets-gotcha-number-two/)'). ***Within the liquidity platform*, you will be able to add and remove liquidity in this proportional manner, converting LP tokens to the underlying tokens and vice versa.**


**If you try to swap these LP tokens directly for another currency (ETH, BNB, etc) via MetaMask Swaps tool or a third-party swap platform, the following is likely to happen:**


* You may be given a **very low quote** for your tokens
* If swapping on MetaMask Swaps, **you may be presented with a warning that a price is not available**, due to the fact that not many people are trading these tokens
* If you go through with the trade, **you are likely to end up with a very, very small fraction of the value** you initially put into the liquidity pool
* **This will be irreversible**; the blockchain cannot reverse any transactions, including these
* **You can't go back and remove your liquidity**; you've traded away your proof of ownership


Let's look at another scenario, where, like on Uniswap, the platform gives you an ERC-721 in exchange for your liquidity pool deposit. Let's suppose, as above, that you've put in $2000 USD in stablecoins and 0.5 ETH. Then, instead of withdrawing the liquidity through the same platform as you started with, you decide to swap your LP token for ETH. What happens?


* All the above possibilities apply
* Additionally, the recipient of the LP token has the ability to go back to the platform and withdraw the liquidity the way it's meant to be withdrawn; you've effectively transferred your holdings to someone else. If you're trading on a platform where someone has access to the traded assets, they could do that; if it's a DEX, however, those funds might simply be lost forever.
* You will, most likely, not be able to recover those funds.


### So what do I do to make sure this doesn't happen to me?


DeFi platforms can be a confusing experience; they're often very exciting websites with minimalist UI and little context for users.


* So first of all, try to find some support or guides as to how to use the product. If you can't find anything like that, maybe reconsider using the product.
* If you deposit tokens into a liquidity pool, **only handle them the way the LP platform says you should, and never try to swap LP tokens directly for a single token.**
* If you've got multiple layers of pooling or staking going on, and you wish to withdraw, again follow the platform's instructions, but think in terms of undoing every step you did to set up your 'stack' in the first place
