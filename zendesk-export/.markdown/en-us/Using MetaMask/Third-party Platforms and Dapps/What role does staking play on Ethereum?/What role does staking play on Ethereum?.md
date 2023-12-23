
#### Am I in the right place?


This article describes the role that staking plays in web3 and on Ethereum. If you're looking for documentation about [MetaMask Staking](https://portfolio.metamask.io/stake), head to [this section](https://support.metamask.io/hc/sections/10505259606555).



#### One of the most common actions that you will come across as a user of Web3 technologies is an action referred to as *staking*.


It's helpful to think of staking as similar to putting your tokens in a savings account, or as depositing them with a third party. On a technical level, when you stake a cryptoasset you are generally committing that asset to be controlled by a smart contract, in exchange for something, usually an alternative token of some kind. 


Staking is used in a very wide variety of contexts. Let's take a look at some of the most common.


### Staking and Liquidity Pools (DeFi, gaming)


One of the great innovations of Decentralized Finance, or DeFi, has been the [liquidity pool](https://consensys.net/blog/metamask/impermanent-loss-defi-markets-gotcha-number-two/). In order to exchange one token for another without relying on a trusted intermediary such as a centralized exchange, users *deposit*matching amounts of two different tokens—say, ETH and DAI—into a pool controlled by a smart contract; other users can then use that pool of tokens (hence, a *liquidity pool*) to trade ETH for DAI, or vice versa. Those who deposited tokens into the pool earn a percentage of a transaction fee for the use of their tokens.


In a way, this is a kind of staking, but it's not usually called that; it's usually called depositing. Staking often occurs at the next level:


Once a user deposits tokens into the liquidity pool, they usually receive something in return, like a receipt of their deposit. Many times it's an NFT, representing their specific token amounts and the value of the same; it can also be what's called [*liquidity pool tokens*](https://support.metamask.io/hc/en-us/articles/4409347883675-How-to-use-Liquidity-Pool-LP-tokens), or LPTs. 


On many DeFi platforms, these LPTs can be *staked*, or again deposited, into a contract that then gives the users rewards in the "native token" of the platform. **This model is often referred to as "farming", as you are 'reaping' the benefits of your staked token****.**


Another model of staking used on such platforms is that, once you have those "platform-native" tokens, you can stake *those*, and earn *governance* tokens, allowing you to participate in votes regarding the direction of the platform.


### Staking ETH in a validator node


In order to effectuate the switch from Proof of Work to Proof of Stake on Ethereum, the Ethereum network has devised a structure that uses staking to help ensure the security of the network. Maintaining consensus regarding the state of a blockchain network is a complex technical topic that is [described more elsewhere](https://support.metamask.io/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-). For the present purposes, think of it like this:


The network is made up of lots of *validators*, which are programs that sync data about what transactions are coming in, and validate them, or refuse them if they're not acceptable. In order to have a validator live on the network, a user has to initiate the validator with a wallet address that corresponds to an address that has [staked 32 ETH into a smart contract run by the Ethereum network](https://ethereum.org/en/staking/).


If that user's validator functions as intended, in other words, is on and is connected to the network, validates blocks correctly, then they are rewarded with fractions of ETH. This follows the pattern we saw in the DeFi examples above.


If, on the other hand, the user's validator does not function as intended, some or all of the ETH that is staked can be *slashed —* i.e. taken from them. This can happen if, for example, the validator tries to validate transactions it shouldn't and maliciously move funds, or, more innocently, if it doesn't meet minimum uptime requirements.


Given the value of ETH, running a validator node is no small investment. It is this financial incentive, along with the multifaceted additional security measures, which help ensure the security of the Ethereum network under Proof of Stake.


Until an upgrade in 2023 when withdrawals will be enabled, all ETH staked in validator nodes continues to earn rewards as designed, but is 'locked'; the users who have deposited that ETH cannot remove it.

