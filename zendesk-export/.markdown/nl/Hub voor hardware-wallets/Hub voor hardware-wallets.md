### MetaMask ondersteunt momenteel vijf lijnen van hardware-wallets: AirGap Vault, Keystone, Lattice, Ledger en Trezor. Deze wallets worden ondersteund op Extensie en kunnen in toekomstige updates aan Mobiel worden toegevoegd.



#### Ben ik op de juiste plek?


Als je uitleg zoekt over wat een hardware-wallet is en waarom je er een zou moeten hebben, lees dan verder.


Als je ondersteuning zoekt voor je specifieke hardware-wallet, scrol naar beneden voor de betreffende sectie.


Als je voor de eerste keer een hardware-wallet instelt, **bekijk dan onze [gebruikershandleiding](https://support.metamask.io/hc/en-us/articles/5450173968283) voor onze aanbevolen configuratie.**



#### 


Wat is een hardware-wallet? En waarom zou ik er een nodig hebben?
-----------------------------------------------------------------


Het begrijpen van hardware-wallets betekent een beetje 'onder de motorkap' van Ethereum kruipen. Laten we eerst eens kijken wat we bedoelen als we het over een "wallet" hebben. Op het eerste gezicht is het een intuïtief concept: het is een digitale container om digitaal geld en andere dingen in te bewaren. Net zoals je in een echte wallet wat geld hebt en wat foto's van je kat of je familie; welnu, in je MetaMask-wallet heb je wat geld en wat CryptoKitties en een geanimeerde GIF van een zombie. Dat is vrijwel identiek, toch?


Nou, om het een 'wallet' te noemen, dat is eigenlijk een metafoor. Het klopt in termen van hoe we het ervaren, maar het geeft niet goed weer wat er technologisch gebeurt. De inhoud van je 'wallet bestaat eigenlijk uit *de activa die aan je adres op de blockchain zijn toegewezen*. Als we ETH "naar" iemand sturen, gaat het niet echt ergens *heen*; het wordt gewoon afgetrokken van het saldo van ETH dat aan jouw adres is toegewezen, en opnieuw toegewezen aan het saldo van het adres waarnaar je het stuurt. Vergeet niet dat een publieke blockchain ook wel *een gedistribueerde grootboek* heet en al onze wallets lijnen zijn in dat grootboek; onze saldi, onze holdings, zijn de kolommen, en de Ethereum Virtual Machine is onze geautomatiseerde boekhouder.


In die zin is MetaMask "gewoon" een webapplicatie die verzoeken stuurt naar de Ethereum-blockchain: voor informatie over welke activa zijn toegewezen aan je adres; om tokens te "verzenden" van het ene adres naar het andere, enzovoort. Het doet dit door je geheime herstelzin te gebruiken.


Je openbare Ethereum-adres is de ene helft van een paar: een *cryptografisch sleutelpaar* om precies te zijn. De openbare helft, jouw adres, kan aan iedereen worden gegeven zonder angst dat ze kunnen inbreken om je fondsen te stelen. De privéhelft, de geheime herstelzin (ook bekend als een "seed phrase"), verifieert wie deze in zijn bezit heeft als hebbende volledige toegang tot het adres en alle daaraan gekoppelde accounts. **Denk eraan: "niet jouw sleutels, niet jouw coins".**


Nu is MetaMask extreem veilig, en zolang niemand toegang heeft tot je geheime herstelzin ([je bewaart het op een veilige offline locatie, toch?](https://support.metamask.io/hc/en-us/articles/4404722782107)), moet je account veilig zijn. Er zijn veel andere factoren die buiten de controle van MetaMask en zijn beveiligingsingenieurs vallen: hoe veilig je browser is, of iemand fysieke controle over je computer krijgt, of je computer overneemt met een virus, bijvoorbeeld.


Om deze reden raden we aan dat als je een aanzienlijke hoeveelheid waarde opslaat in je MetaMask-wallet (of gewoon activa die belangrijk voor je zijn), dat je een hardware-wallet gebruikt als tweede verdedigingslinie.


Met al die achtergrond uit de weg:



TL;DR
------


### **Een hardware-wallet is een fysiek apparaat buiten je computer dat de sleutels van je wallet beveiligt, en fungeert als een firewall tussen aanvallers en de inhoud van je wallet.**


Om transacties te verrichten met fondsen die door een hardware-wallet zijn beveiligd, moet er interactie zijn met de hardware-wallet om de transactie goed te keuren. Op deze manier, zelfs als iemand op een of andere manier toegang krijgt tot je MetaMask-wallet, zullen ze worden tegengehouden om er dingen uit te halen.


 


 AirGap Vault
-------------


* [AirGap Vault met MetaMask verbinden](https://support.airgap.it/guides/metamask/)
* [AirGap Vault - Android Play Store](https://play.google.com/store/apps/details?id=it.airgap.vault&hl=en_US&gl=US)
* [AirGap Vault - iOS App Store](https://apps.apple.com/us/app/airgap-vault-secure-secrets/id1417126841)


 Keystone
---------


* [Je Keystone aan je MetaMask-wallet binden](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/bind-metamask-with-keystone)
* [Keystone verbinden met MetaMask Mobiel en ETH versturen](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile)
* [Keystone gebruiken met MetaMask Mobiel voor dApps via Wallet Connect](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile/defi-with-metamask-mobile)
* [EVM-chains op MetaMask Mobiel configureren](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile/configuring-evm-chains-on-metamask-mobile)
* [Hoe haal je voordeel uit hardware-walletbeveiliging met transparante QR-codes?](https://consensys.net/blog/news/metamask-x-keystone-how-to-benefit-from-hardware-wallet-security-using-transparent-qr-code/)
* Voor inzicht in het aanbod van Keystone met toegevoegde waarde voor beveiliging, [zie hier](https://blog.keyst.one/blind-signing-a-security-black-hole-for-the-ethereum-community-13f909b848b6).
* Voor geavanceerde onderwerpen met betrekking tot de beveiligingsfuncties van Keystone, waaronder het invoeren van aangepaste entropie, [lees hier](https://support.keyst.one/general-navigation-guide#advanced-users).


 Lattice
--------


* Voor beginnende Lattice-gebruikers, zorg dat je alles goed hebt ingesteld: <https://gridplus.io/setup>
* GridPlus' documentatie over aan de slag gaan met MetaMask en een Lattice [vind je hier](https://docs.gridplus.io/setup/metamask).


Ledger
------


Ledger heeft een brede documentatie voor gebruikers van MetaMask. Hier volgt wat informatie die je op weg zal helpen:  



* [MetaMask instellen en gebruiken om toegang te krijgen tot je Ledger Ethereum (ETH)-account](https://support.ledger.com/hc/en-us/articles/4404366864657-Set-up-and-use-MetaMask-to-access-your-Ledger-Ethereum-ETH-account?docs=true)
* [Ik zie mijn BEP-20-tokens niet in mijn Ledger Binance Smart Chain (BSC). Wat kan ik doen?](https://support.ledger.com/hc/en-us/articles/4406111561617-I-don-t-see-my-BEP-20-tokens-in-my-Ledger-Binance-Smart-Chain-BSC-account-what-can-I-do-?support=true)
* [Hoe krijg je toegang tot je Ledger Polygon-account via MetaMask?](https://support.ledger.com/hc/en-us/articles/4418394184209-How-to-access-your-Ledger-Polygon-MATIC-account-via-Metamask?docs=true)


Trezor
------


* Zie Trezor's documentatie over de werking met MetaMask [hier](https://wiki.trezor.io/Apps:MetaMask).
