What is Infura?
---------------


[Infura](https://infura.io/) is the service provider that MetaMask uses to get information on and off blockchains.  
  



![Infura homepage](https://support.metamask.io/hc/article_attachments/15958160219547)


### How does it work?


Ethereum and other blockchains use a different combination of protocols and technology than your traditional Internet network. Yes, it still uses the same physical conduits as traditional Internet, but in terms of the software, it's a separate network; there's no URL you can go to that "gets you onto Ethereum" in the way we're used to. 


To access these networks natively and see the data being passed across them, you would have to install what's known as a *client*. This is generally a fairly small program that runs as a command-line interface. In other words: no graphics, just text.


That's not very useful for a lot of people, and it's certainly not as fun as a rich Web-like experience. And besides that, sometimes for development purposes, it's much more useful to be able to build a program in a different environment that then communicates with the blockchain "remotely", without running a client at the same time.


So most public blockchain networks, Ethereum included, build what's called an API. If you're not familiar with the technology, think of it as a kind of menu: programmers can ask the blockchain for certain data or record data to the blockchain, using specifically-formulated requests. And if the information they're looking to request or record isn't on the menu, well, they can [make a proposal to the community to change the menu](https://eips.ethereum.org/). 


 


### OK, but what's Infura's part in all that?


Infura provides what are called *endpoints* to Ethereum's API. If we're thinking in terms of a menu at a restaurant, then Infura is like a server, or a cashier: the person who takes your order and rings you up. Infura provides an endpoint that your code can 'point to', so that your requests to receive or record information can always get to the network. And, of course, they return to you the information you've requested.


Like a restaurant, Infura does charge for this service, but only after you've made a *lot*of requests in one month. For developers who are just testing something out, it's free to start and easy to set up an account.


 


### Why does MetaMask use Infura?


MetaMask has always used Infura as an endpoint provider due to their second-to-none reliability and availability.


As blockchain traffic scales, MetaMask users need to be able to submit requests to the blockchain, no matter where they are, what they're asking to do on-chain, and how many people are doing it at once. There are, of course, limiting factors to this: the more on-chain activity there is, the more congested the network is, and gas fees will be affected, and at the end of the day, only so many transactions can go into each block. But at no point should your endpoint provider be the bottleneck in that scenario. That's when Infura's capacity for traffic shines, no matter which NFT is dropping.


More recently, Infura and MetaMask have both become part of Consensys Software, which is enabling the teams to work together more tightly and ensure this kind of quality experience continues.


Additionally, Infura offers endpoints for more blockchains than just Ethereum, and as we move into a world of many blockchains, this kind of reliable support for multiple chains will be essential.


 


### Do I have to use Infura?


No! MetaMask always has been and always will be a tool that empowers its users, and users can change the RPC (the protocol that most blockchain APIs use) endpoint.


If you had an alternative Ethereum endpoint—for example, if you're running a local node—you could add that provider to your MetaMask wallet under the name "Private Ethereum endpoint" by following [these steps](https://support.metamask.io/hc/en-us/articles/360043227612-How-to-add-a-custom-network-RPC).

