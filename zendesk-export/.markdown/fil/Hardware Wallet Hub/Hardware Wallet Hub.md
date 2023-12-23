### Kasalukuyang sinusuportahan ng MetaMask ang limang linya ng hardware wallet: AirGap Vault, Keystone, Lattice, Ledger, at Trezor. Suportado ang mga wallet na ito sa Extension, at maidaragdag ang mga ito sa Mobile sa mga update sa hinaharap.



#### Nasa tamang lugar ba ako?


Kung naghahanap ka ng paliwanag tungkol sa kung ano ang isang hardware wallet at kung bakit kailangan mong magkaroon nito, magpatuloy sa pagbabasa.


Kung naghahanap ka ng suporta tungkol sa iyong partikular na hardware wallet, mag-scroll pababa sa kaukulang seksyon.


Kung nagse-set up ka ng hardware wallet sa unang pagkakataon, **tingnan ang aming [Gabay sa User](https://support.metamask.io/hc/en-us/articles/5450173968283) para sa aming inirerekomendang configuration.** 



#### 


Ano ang hardware wallet? At bakit kailangan kong magkaroon nito?
----------------------------------------------------------------


Kung nauunawaan mo ang mga hardware wallet, medyo natututunan mo na ang tungkol sa Ethereum. Tingnan muna natin kung ano ang ibig sabihin namin kapag pinag-uusapan ang isang 'wallet'. Sa unang tingin, isa itong intuitive concept: isa itong digital na lalagyan para maghawak ng digital money at iba pang bagay. Tulad ng sa isang totoong wallet, maaaring mayroon kang ilang currency at ilang larawan ng iyong pusa o ng iyong pamilya. Sa iyong MetaMask wallet naman, mayroon kang ilang currency at ilang CryptoKitties at isang animated GIF ng isang zombie. Medyo magkapareho kung tutuusin.


Lumalabas na medyo isang metaphor ang pagtawag dito bilang isang 'wallet'. Maganda ito pagdating sa kung paano natin nararanasan ito, pero hindi ito tumpak na kumakatawan sa kung ano ang nangyayari sa teknolohikal na paraan. Ang 'wallet' mo ay aktuwal na naglalaman ng *mga asset na nakatalaga sa iyong address sa blockchain*. Kapag nagpapadala tayo ng ETH 'papunta' sa isang tao, hindi ito *napupunta*sa kahit saan; ibinabawas lang ito sa balanse ng ETH na nakatalaga sa iyong address, at itinatalaga naman sa balanse ng address ng tao kung kanino mo ito ipinapadala. Tandaan, tinatawag ding *distributed ledger technology* ang isang pampublikong blockchain, at lahat ng wallet natin ay mga linya sa ledger na iyon; ang mga balanse natin, ang mga holding natin, ay ang mga column, at ang Ethereum Virtual Machine ay ang automated bookkeeper.


Sa ganitong pagpapakahulugan, ang MetaMask ay isa lang web application na nagpapadala ng mga kahilingan sa Ethereum blockchain: mula sa mga impormasyon tungkol sa kung anong mga asset ang nakatalaga sa address mo, hanggang sa 'magpadala' ng mga token mula sa isang address papunta sa isa pa, at iba pa. Ginagawa nito ito sa pamamagitan ng paggamit ng Secret Recovery Phrase mo.


Ang iyong pampublikong Ethereum address ay kalahati ng isang pares: isang *cryptographic key pair*, para maging tumpak. Puwedeng ibigay ang pampublikong kalahati, ang address mo, sa kahit sino nang walang pangamba na maha-hack at mananakaw nila ang iyong mga pondo. Ino-authenticate naman ng pribadong kalahati, ang Secret Recovery Phrase (kilala rin bilang 'seed phrase'), ang taong nagmamay-ari nito na siyang may ganap at kumpletong access sa address at lahat ng account na nauugnay rito. **Tandaan: "hindi mo keys, hindi mo coins".**


Ngayon, napaka-secure na ng MetaMask at hangga't walang may access sa Secret Recovery Phrase mo ([isinulat mo naman ito sa isang ligtas na offline na lokasyon, 'di ba?](https://support.metamask.io/hc/en-us/articles/4404722782107)), dapat na maging secure ang account mo. Maraming pang salik ang wala sa kontrol ng MetaMask at ng mga security engineer nito: gaano kaligtas ang browser mo magkakaroon ba ng pisikal na kontrol ang isang tao sa computer mo, o makokontrol ang mo computer gamit ang isang virus, bilang halimbawa.


Dahil dito, inirerekomenda namin na kung nagso-store ka ng anumang malaking halaga sa MetaMask wallet mo—o mga asset na mahalaga sa iyo—na gumamit ka ng hardware wallet bilang pangalawang linya ng depensa. 


Ngayong tapos nang talakayin ang lahat ng 'yan:



TL;DR
------


### **Ang hardware wallet ay isang pisikal na device sa labas ng computer mo na ginagawang ligtas ang mga key ng wallet mo, at nagsisilbing firewall sa pagitan ng mga attacker at ng mga nilalaman ng iyong wallet.**


Upang makapagtransaksyon gamit ang mga pondong sine-secure ng isang hardware wallet, kakailanganin mong makipag-ugnayan sa hardware wallet upang aprubahan ang transaksyon. Sa ganitong paraan, kahit na magkaroon ng access ang isang tao sa MetaMask wallet mo sa anumang paraan, mapipigilan sila sa paglilipat ng mga bagay palabas nito.


 


 AirGap Vault
-------------


* [Ikonekta ang AirGap Vault sa MetaMask](https://support.airgap.it/guides/metamask/)
* [AirGap Vault - Android Play Store](https://play.google.com/store/apps/details?id=it.airgap.vault&hl=en_US&gl=US)
* [AirGap Vault - iOS App Store](https://apps.apple.com/us/app/airgap-vault-secure-secrets/id1417126841)


 Keystone
---------


* [Pagba-bind ng Keystone mo sa iyong MetaMask Wallet](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/bind-metamask-with-keystone)
* [Paano ikonekta ang Keystone sa MetaMask Mobile at magpadala ng ETH](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile)
* [Paano gamitin ang Keystone sa MetaMask Mobile para sa mga dApp sa pamamagitan ng Wallet Connect](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile/defi-with-metamask-mobile)
* [Paano mag-configure ng mga EVM chain sa MetaMask Mobile](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile/configuring-evm-chains-on-metamask-mobile)
* [Paano Makinabang sa Seguridad ng Hardware Wallet Gamit ang mga Transparent QR Code](https://consensys.net/blog/news/metamask-x-keystone-how-to-benefit-from-hardware-wallet-security-using-transparent-qr-code/)
* Para maunawaan ang value-added na panukala sa seguridad ng Keystone, [tingnan dito](https://blog.keyst.one/blind-signing-a-security-black-hole-for-the-ethereum-community-13f909b848b6).
* Para sa mga advanced na paksa tungkol sa mga pangseguridad na feature ng Keystone, kasama na ang custom entropy, [magbasa rito](https://support.keyst.one/general-navigation-guide#advanced-users).


 Lattice
--------


* Para sa mga baguhang user ng Lattice, siguraduhing naka-set up ka nang maayos: <https://gridplus.io/setup>
* Tingnan ang dokumentasyon ng GridPlus tungkol sa pagsisimula gamit ang MetaMask at Lattice [dito](https://docs.gridplus.io/setup/metamask).


 Ledger
-------


 Maraming dokumentasyon ang Ledger para sa mga user ng MetaMask. Narito ang ilan na makakatulong sa iyong makapagsimula:  



* [I-set up at gamitin ang MetaMask para i-access ang iyong Ledger Ethereum (ETH) account](https://support.ledger.com/hc/en-us/articles/4404366864657-Set-up-and-use-MetaMask-to-access-your-Ledger-Ethereum-ETH-account?docs=true)
* [Hindi ko nakikita ang mga BEP-20 token ko sa aking Ledger Binance Smart Chain (BSC) account, ano ang puwede kong gawin?](https://support.ledger.com/hc/en-us/articles/4406111561617-I-don-t-see-my-BEP-20-tokens-in-my-Ledger-Binance-Smart-Chain-BSC-account-what-can-I-do-?support=true)
* [Paano i-access ang Ledger Polygon account mo sa pamamagitan ng MetaMask](https://support.ledger.com/hc/en-us/articles/4418394184209-How-to-access-your-Ledger-Polygon-MATIC-account-via-Metamask?docs=true)


 Trezor
-------


* Tingnan [dito](https://wiki.trezor.io/Apps:MetaMask) ang dokumentasyon ng Trezor tungkol sa operability sa MetaMask.
