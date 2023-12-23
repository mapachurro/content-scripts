MetaMask makes dapp adoption quick and easy because we host a blockchain connection by default, and our trusty friends at Infura do an amazing job making this experience feel totally seamless, [almost all of the time](https://status.infura.io/)!


Sometimes, some dapp usage has grown much faster than we've been able to anticipate, and so MetaMask's default provider connection can become intermittent. Sometimes we have to limit abusive sites.


At times like that, there are three options:


1. Wait and be patient.
2. Connect to another blockchain provider in place of Infura (like [your own local node](https://support.metamask.io/hc/en-us/articles/360015290012-Using-a-Local-Node))
3. Use another client.


Connecting to another blockchain provider
-----------------------------------------


To connect, you'll need to run a local RPC server, and then connect to it in MetaMask as if you were selecting a network. On both Extension and Mobile, the network selector is at the top of the screen, in the middle.


When you have successfully [spun up your own node](https://support.metamask.io/hc/en-us/articles/360015290012), it will run on 'Localhost 8545', which you'll find in your networks list by default (you may need to go to Settings > Advanced > Show test networks to make sure this is displayed):


![Using a local node in MetaMask](https://support.metamask.io/hc/article_attachments/17122923408539)


Select it to start using your node to send requests to the blockchain. 

