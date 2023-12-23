Have assets suddenly moved out of your account, without your permission or knowledge? Have you noticed that every time you transfer something into your account, it gets automatically forwarded somewhere else?


If so, you might be dealing with a *sweeper*. This article will give some explanation as to what sweepers are, how they happen, and further guidance as to how to deal with having one attached to your account.


### 
If you don’t have a sweeper on your account, but want to know more about how to avoid ending up in this situation, consult our [preventative guide](https://support.metamask.io/hc/en-us/articles/12091923128347).


#### What is a sweeper?


Also known as a *sweeper bot*, a sweeper is an automated bit of code (also called a *script*) that can be assigned to a blockchain address, to perform actions relating to that account automatically, such as automatically *sweeping* assets deposited into the account to another address.


Like all computer programs, whether a script is malicious or not depends on who programmed it, what it’s designed to do, and where it is deployed. After all, being able to move assets programmatically from one address to another could be very convenient functionality. However, sweeper bots are often deployed maliciously. 


### Most times, a user gives away their Secret Recovery Phrase; a malicious actor uses that access to deploy a script to this account, automatically sending all the wallet’s valuable resources somewhere else.


#### How does a sweeper work?


In order to understand how sweepers, and other bots that act on public blockchain networks, operate, a little bit of technical understanding as to how these networks work is necessary. At a high level, then: A public blockchain network is composed of any number of *nodes*, each of which is communicating with the rest of the network’s nodes, continually maintaining *consensus* regarding the state of a common *ledger*. That ledger keeps track of any number of different assets, depending on how the blockchain was designed.


Users on the network send *transactions* from their addresses to other addresses. These transactions are *broadcast* to the closest node(s), which then forward the proposed transaction on to the rest of the network. The user’s transaction remains pending for a time, with other recent transactions, in what’s known as the *transaction pool* (txpool) or *memory pool* (mempool). Meanwhile, the nodes do the work of checking that the address requesting the transfer, in fact, has the funds available for transfer, and reach consensus with the rest of the network that the transaction is thus valid. At this point, a group of validated transactions is grouped together and encrypted, and proposed to the network as a *block* of transactions; when it is accepted, it is included in the *chain*.


### 
If blockchain terminology or concepts trip you up, don’t worry. Check out [Consensys’ Blockchain Glossary](https://consensys.net/knowledge-base/a-blockchain-glossary-for-beginners/) and our [Learn the Basics article](https://support.metamask.io/hc/en-us/articles/360015489611).


Sweeper bots, most often, are scanning that pool of transactions for transfers of tokens to the compromised address; as soon as a bot sees an incoming transfer of value or tokens that would be of interest, it initiates a second transaction, transferring those assets to another, third-party address.


Because this is all automated via code and actions are taken almost simultaneously with the funds being transferred to the account, it might happen faster than the time it takes to refresh the block explorer. You certainly won’t be able to manually transfer assets out of your account faster than a bot.


Consider some of these details observed about sweeper behavior:


* A sweeper might favor the asset that is highest in USD value, even if that means spending more in transaction fees to sweep it.
* The sweeper may use all available ETH to maximize the value swept out of the account, while also having a high likelihood of being the “winning” transaction, in cases where there is a battle between two parties to remove assets from an account
* Even if there is no ETH in the account, an attacker may fund an account temporarily in order to cover the gas fees to extract other desirable assets from the account (NFTs, Liquidity Pool tokens, etc.)
* If the USD value of assets in the account is below a certain level, the bot may not sweep out the assets, meaning **you may not realize that you have a sweeper on your account**.


#### Bringing a bot to a bot fight


In this context–fighting against an automated opponent who takes your ETH from you before you can use it–things can look pretty hopeless. Enter [Flashbots](https://docs.flashbots.net/), who have developed a project called [Flashbots/searcher-sponsored-tx](https://github.com/flashbots/searcher-sponsored-tx). This allows you, essentially, to pay for the transaction on the compromised address from another account. Or, as they put it: *“This is accomplished by submitting a Flashbots transaction bundle, with the first "sponsor" transaction paying the "executor" wallet in ETH, followed by a series of executor transactions that spend this newly received ETH on gas fees.”*


This strategy requires two accounts — the compromised account (the *executor*) and another to pay for the transaction (the *sponsor*). **Success using Flashbots will require significant technical know-how and research. The following instructions are provided as a general guide only.**


* Make sure the compromised account has no ETH in it; we highly recommend you use a [burner bot](https://twitter.com/smpalladino/status/1373049027365904389?s=20&t=PE8rsffOnw8PxiKzpl7OdQ) first.
+ We generally advise running this burner bot on more than one machine, using a different endpoint on each. For example, run a burner locally using [Infura](https://infura.io/), and a burner on a remote server with another provider such as [Quiknode](https://www.quicknode.com/). This is so that you have a redundancy plan in case we have high network latency or node issues (rate limits, syncing issues).

* The code in [Flashbots/searcher-sponsored-tx](https://github.com/flashbots/searcher-sponsored-tx) will need to be altered for your specific needs, but the engine is there for you to rescue your tokens from a compromised address. The Flashbots engine is flexible enough to support a single [transfer()](https://eips.ethereum.org/EIPS/eip-20) call, or [unstake()](https://eips.ethereum.org/EIPS/eip-900#unstake) and [transfer()](https://eips.ethereum.org/EIPS/eip-20)*.*


#### Using a self-destructing smart contract


Another method of getting ETH into the account without it being publicly broadcast in the transaction pool is by sending it through an [internal transaction](https://support.metamask.io/hc/en-us/articles/360058568312-Internal-transactions), using a smart contract deployed by a new, clean, safe address.



```
pragma solidity >=0.7.0 <0.9.0;  
  
contract MoveETH {  
    constructor(address sendToAddress) payable {  
        address payable addr = payable(address(sendToAddress));  
        selfdestruct(addr);  
    }  
}
```

By deploying this contract, we can send ETH and the compromised address string in the constructor argument. This contract works by creating the contract and self-destructing in the same transaction. The use of selfdestruct() means we clear the blockchain state (since it's a one time use contract) and forward the ETH to the compromised address in 1 transaction.


Example: <https://goerli.etherscan.io/tx/0x82ccb222eae55aaea73dd0efee1ea6ed7320f880889f280d4a343b8823f86692>


While effective, this method uses a notably higher amount of gas (about 70,000), as it is much more complex than a simple transfer from one account to another (normally 22,000).


From here, we would broadcast pre-signed transactions ensuring we are using all the ETH in the account so that a sweeper cannot frontrun us - or at least make it unlikely to be frontrun, as a sweeper would need to send more ETH to the account to pay a higher gas price.


### 
Remember, the best way to beat a sweeper is… to not have to in the first place! Follow our recommendations [here](https://support.metamask.io/hc/en-us/articles/12091923128347), and stay safe out there.


 


This is an updated version of [an article](https://blog.mycrypto.com/how-to-beat-an-ethereum-based-sweeper-and-recover-your-assets) originally published on MyCrypto's blog.

