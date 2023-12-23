Ethereum is a network of "nodes" — that is, a network of computers running similar software that connects them to the blockchain, and which, collectively, comprise the network. 


For greater security, privacy, and read speeds, you might want to run your own node, instead of using [Infura](https://support.metamask.io/hc/en-us/articles/4417315392795) as the default provider. Running nodes also increases Ethereum's decentralization, improving the health of the network.


Once you have your own node up and running, you can connect MetaMask to it and use it to send requests to the blockchain and receive information back. 


To run a node, you need Ethereum clients. Since Ethereum transitioned to Proof of Stake, you can no longer run a "full" node using one client. Instead, you need two: one for the execution layer, and one for the consensus layer. 


**Consensus layer** clients include:


* [Prysm](https://prysmaticlabs.com/)
* [Lighthouse](https://lighthouse.sigmaprime.io/)
* [Nimbus](https://nimbus.team/)
* [Teku](https://consensys.net/knowledge-base/ethereum-2/teku/)
* [Lodestar](https://lodestar.chainsafe.io/)


**Execution layer** clients include:


* [Geth](https://geth.ethereum.org/)
* [Besu](https://www.hyperledger.org/use/besu)
* [Erigon](https://github.com/ledgerwatch/erigon#erigon)
* [Nethermind](https://nethermind.io/)


Each client is designed with a slightly different set of priorities or target audience, and they also use different code languages. Make sure to look through to find the one that best suits your needs.


Once you've chosen one, the best place to start is the official Ethereum guide to running a node: <https://ethereum.org/en/developers/docs/nodes-and-clients/run-a-node/>


Once you have your local clients set up, you can connect to your node with the network menu in the top left corner of MetaMask:


![Using a local node in MetaMask](https://support.metamask.io/hc/article_attachments/17122875767067)


 


### See also:


* <https://clientdiversity.org/>. 'Client diversity' describes the mix of Ethereum clients currently in use. Concentrating Ethereum nodes into a handful of dominant clients creates a centralization risk for the network, and a potentially problematic point of failure. Whilst the diversity of consensus layer clients is relatively healthy, it's recommended you consider steering away from Geth as you execution layer client, if possible.
