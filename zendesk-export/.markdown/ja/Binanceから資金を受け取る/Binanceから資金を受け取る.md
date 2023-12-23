Binance取引所のアカウントからMetaMaskに資金を送り、ウォレットに表示されない場合、以下の手順に従うことを推奨します。


**ステップ1：ブロックチェーンエクスプローラーでトランザクションを確認する**
----------------------------------------


まず、Binanceがトランザクションを完了するために使用したネットワークを確認する必要があります。Binanceで出金の詳細を確認することで、それが可能です。  
![mceclip0.png](https://support.metamask.io/hc/article_attachments/4416068979483/mceclip0.png)


そのうえで、ネットワークのエクスプローラーに移動します。以下にいくつか例を示します。


* Ethereum Mainnet用の[Etherscan](https://etherscan.io/)
* BSC（Binance Smart Chain）用の[Bscscan](https://bscscan.com/)
* Polygon用の[Polygonscan](https://polygonscan.com/)
* Avalanche用の[Snowtrace](https://snowtrace.io/)


ブロックチェーンエクスプローラーで、MetaMaskのアドレスを検索するか、[トランザクションID](https://support.metamask.io/hc/en-us/articles/4413442094235)を検索して、トランザクションの詳細を呼び出し、完了したことを確認します。


![mceclip1.png](https://support.metamask.io/hc/article_attachments/4416075037595/mceclip1.png)


ブロックエクスプローラーでアカウントのページの概要セクションで、トークンの残高を確認することができます。トークンがネイティブトークン（BNB、ETH、MATIC、AVAX）である場合は、残高セクションに表示されます（上のスクリーンショットを参照）。


ネイティブトークンでない場合、「Token」（トークン）セクションのドロップダウンメニューに表示されます。


 


**ステップ2：MetaMaskにネットワークを追加し、必要に応じてトークンを表示します。**
-----------------------------------------------


ネットワークを追加するには、[Chainlist](https://support.metamask.io/hc/en-us/articles/360058992772-Add-a-network-using-Chainlist-Extension-or-Mobile-)を使用して追加する際についてのガイド、あるいは[カスタムネットワークを追加する際についての記事](https://support.metamask.io/hc/en-us/articles/360043227612-How-to-add-a-custom-network-RPC)を確認してください。


ネットワークを追加後、あなたのトークンがそのネットワークのネイティブトークンでない場合、[カスタムトークンとして表示](https://support.metamask.io/hc/en-us/articles/360015489031-How-to-add-unlisted-tokens-custom-tokens-in-MetaMask)する必要があります。


ブロックチェーンエクスプローラーで、「Token」（トークン）セクションに進み、受け取ったトークンをクリックしてください。


![mceclip2.png](https://support.metamask.io/hc/article_attachments/4416075047451/mceclip2.png)


 


MetaMaskにカスタムトークンを追加するには、以下の手順が必要です。


1. トークンのコントラクトアドレスをコピーします。より詳細なガイダンスについては[こちら](https://support.metamask.io/hc/en-us/articles/360015488811-What-is-a-Token-Contract-Address-)をご覧ください。基本的に、ブロックエクスプローラーでトークンを確認し、そこからそのアドレスを取得する必要があります。
2. MetaMaskに移動し、「Assets」（資産）タブの「import tokens」（トークンをインポート）を確認します。追加済みのトークン数によっては、確認するのに少しスクロールする必要があるかもしれません。これをクリックしてトークンを追加し、アドレスを入力します。


間違ったネットワーク上でトークンを送信してしまった場合、いつでもブリッジを使用して目的のネットワーク上にそのトークンを取得することができます。


[Multichain](https://multichain.org/)（以前のAnySwap）を使用して最も一般的なネットワーク間でトークンをブリッジすることができます。


**トークンをブリッジするには、ガス手数料を払うためにネットワークのネイティブトークンで資金を保有しておく必要があります。**これらはあらゆるトランザクションで必要です。例えば、BSCではBNBが、PolygonではMATICが、AvalancheではAVAXが必要です。

