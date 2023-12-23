### MetaMaskは現在、AirGap Vault、Keystone、Lattice、Ledger、Trezorの5種類のハードウェアウォレットをサポートしています。これらのウォレットはExtensionでサポートされ、将来の更新でMobileに追加することができるようになります。



#### 私は適切な場所にいますか？


ハードウェアウォレットとは、また、なぜ持つべきなのかについて、説明をお求めであれば、そのまま読み進めてください。


特定のハードウェアウォレットに関するサポートをお求めの場合は、該当するセクションまでスクロールしてください。


ハードウェアウォレットを初めて設定する場合は、**推奨される構成に関する[ユーザーガイド](https://support.metamask.io/hc/en-us/articles/5450173968283)をご覧ください。**



#### 


ハードウェアウォレットとは？ なぜ持つ必要があるのでしょうか？
-------------------------------


ハードウェアウォレットを理解することは、Ethereumの「内部」を少し知るということになります。まず、「ウォレット」とは何を意味するのかを見てみましょう。一見、それは直感的な概念であり、デジタル通貨やその他のものを保有するためのデジタルコンテナです。実際のウォレットと同じように、いくらかの通貨、猫や家族の写真を持っているかもしれません。それで、MetaMaskウォレットには、いくらかの通貨と、いくつかのCryptoKittiesとゾンビのアニメーションGIFがあります。これまでのところ、かなり似ています。


さて、「ウォレット」と呼ばれているのは、ちょっとした比喩であることが分かりました。それは、私たちがどのような体験を体験するかという点で納得できるものですが、技術的に起こっていることを正確に表現しているわけではありません。「ウォレット」の中身は、実際に*ブロックチェーン上のあなたのアドレスに割り当てられた資産で*構成されています。ETHを誰か「に」送信する際、ETHはどこにも*行*かず、単にあなたのアドレスに割り当てられたETHの残高から差し引かれ、送信先アドレスの残高に再度割り当てられます。また、パブリックブロックチェーンは、*分散型台帳技術*とも呼ばれ、すべてのウォレットはその台帳内の行で、残高、保有資産は列であり、Ethereum Virtual Machineは自動化された台帳管理者であることを覚えておいてください。


この意味では、MetaMaskはEthereumブロックチェーンにリクエストを送信する「単純な」ウェブアプリケーションであり、アドレスに割り当てられた資産に関する情報を取得したり、あるアドレスから別のアドレスにトークンを「送信」したりすることができます。Secret Recovery Phraseを使用して、これを行います。


あなたの公開Ethereumアドレスは、ペアの片方、正確には*暗号鍵ペア*です。公開鍵、つまりあなたのアドレスは、あなたの資金が他人にハッキングされたり、盗まれたりすることを心配せずに、誰にでも与えることができます。秘密鍵であるシークレットリカバリーフレーズ（「シードフレーズ」とも呼ばれます）は、それを保有する人が誰であれ、そのアドレスとそれに関連するすべてのアカウントへの完全なアクセスを認証します。**「not your keys, not your coins」（鍵の所有者こそが、コインの所有者である）ことを忘れないでください。**


現在、MetaMaskは非常に安全であり、シークレットリカバリーフレーズに誰もアクセスできない限り（[安全なオフラインの場所に書き留めていますよね？](https://support.metamask.io/hc/en-us/articles/4404722782107)）、アカウントは安全であるべきです。MetaMaskとそのセキュリティエンジニアのコントロールできない要因は他にもたくさんあります。例えば、ブラウザがどれほど安全であるか、誰かがコンピュータを物理的に制御しているか、あるいはウイルスを使いコンピューターを乗っ取っているかなどです。


このため、MetaMaskウォレット、または単に重要な資産に大量の価値を保存する場合は、ハードウェアウォレットを副次的な防衛手段として使用することをお勧めします。


そのような背景を踏まえた上で、以下をご確認ください：



TL;DR
------


### **ハードウェアウォレットは、コンピュータの外部にある物理的なデバイスで、ウォレットの鍵を保護し、攻撃者とウォレットの内容の間のファイアウォールとして機能します。**


ハードウェアウォレットによって保護された資金でトランザクションを行うには、トランザクションを承認するために、ハードウェアウォレットと対話する必要があります。この方法では、誰かがMetaMaskウォレットに何らかの形でアクセスしたとしても、MetaMaskウォレットから資産を移動することを阻止します。


 


AirGap Vault
------------


* [AirGap VaultをMetaMaskに接続する](https://support.airgap.it/guides/metamask/)
* [AirGap Vault - Android Play ストア](https://play.google.com/store/apps/details?id=it.airgap.vault&hl=en_US&gl=US)
* [AirGap Vault - iOS App Store](https://apps.apple.com/us/app/airgap-vault-secure-secrets/id1417126841)


 Keystone
---------


* [MetaMaskウォレットにKeystoneをバインドする](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/bind-metamask-with-keystone)
* [KeystoneをMetaMask Mobileに接続し、ETHを送信する方法](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile)
* [Wallet Connectを介してKeystoneをMetaMask Mobile for dAppsで使用する方法](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile/defi-with-metamask-mobile)
* [MetaMask MobileでEVMチェーンを設定する方法](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile/configuring-evm-chains-on-metamask-mobile)
* [透明QRコードを利用したハードウェアウォレットのセキュリティを活用する方法](https://consensys.net/blog/news/metamask-x-keystone-how-to-benefit-from-hardware-wallet-security-using-transparent-qr-code/)
* Keystoneのセキュリティ付加価値の提案に関する詳細は、[こちらをご覧ください](https://blog.keyst.one/blind-signing-a-security-black-hole-for-the-ethereum-community-13f909b848b6)。
* Keystoneのカスタムエントロピーの導入を含む、Keystoneのセキュリティ機能に関する詳細なトピックについては、[こちらをご覧ください](https://support.keyst.one/general-navigation-guide#advanced-users)。


 Lattice
--------


* Latticeを初めて使用する場合は、適切に設定されていることを確認してください。<https://gridplus.io/setup>
* ﻿MetaMaskやLatticeの使用開始に関する﻿GridPlusの﻿ドキュメントは、﻿﻿ [こちら﻿](https://docs.gridplus.io/setup/metamask) をご覧ください。


 Ledger
-------


LedgerにはMetaMaskのユーザーのための幅広いドキュメントがあります。こちらでは、あなたが始めるのに役立ついくつかのものをご紹介します。  



* [MetaMaskを設定、使用してLedger Ethereum（ETH）アカウントにアクセスする](https://support.ledger.com/hc/en-us/articles/4404366864657-Set-up-and-use-MetaMask-to-access-your-Ledger-Ethereum-ETH-account?docs=true)
* [Ledger Binance Smart Chain（BSC）のアカウントにBEP-20トークンが表示されないのですが、どうすればいいですか？](https://support.ledger.com/hc/en-us/articles/4406111561617-I-don-t-see-my-BEP-20-tokens-in-my-Ledger-Binance-Smart-Chain-BSC-account-what-can-I-do-?support=true)
* [MetaMaskを介してLedger Polygonアカウントにアクセスする方法](https://support.ledger.com/hc/en-us/articles/4418394184209-How-to-access-your-Ledger-Polygon-MATIC-account-via-Metamask?docs=true)


 Trezor
-------


* MetaMaskとの操作性については、[こちら](https://wiki.trezor.io/Apps:MetaMask)のTrezorのドキュメントをご覧ください。
