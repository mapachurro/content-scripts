
#### Nieuw bij crypto en web3?


Ga naar [MetaMask Learn](https://learn.metamask.io/) voor een eenvoudige leerervaring, speciaal ontworpen voor nieuwkomers in web3. Het is volkomen gratis, beschikbaar in meerdere talen, en bevat nuttige hulpmiddelen zoals simulaties om je te helpen je weg te vinden met MetaMask.



#### *In dit artikel vind je uitleg en links naar bronnen over transacties, en waarom deze mislukken. Verder naar beneden vind je ook links naar vaak voorkomende scenario's van mislukte transacties, en hoe je deze kunt aanpakken:*


* [Anatomie van een blockchain-transactie](#h_01G79J04D0EN1VD8VS7C7J7KD1)
* [Veelvoorkomende problemen](#h_01G79J09NWA8CGR4VYC2PT5B6Y)
* [Belangrijkste fixes](#h_01G79J0J8JTRPM9MRB76EN1GPP)
* [Extra bronnen en volgende stappen](#h_01G79J0RP8ZMZ1V1SKQY70TXCT)
* [Veelgestelde vragen](#h_01G79J18RBK27GZCF10CGN9GKP)


 


**Anatomie van een blockchain-transactie**
------------------------------------------


Als we over transacties op een blockchain-netwerk spreken, hebben we het meestal over interacties tussen twee adressen. Met andere woorden, het gaat over tokens, of ze nu fungible zijn of niet, of andere crypto-activa die van het ene adres naar het andere worden verzonden. Er bestaat ook zoiets als 'interne transacties'. Deze transacties zijn interacties die plaatsvinden tussen smart contracts, maar ze komen verder niet ter sprake in dit artikel.



#### Meer informatie?


Meer informatie over blockchain-netwerken en hoe ze in het algemeen werken, vind je in onze [introductie.](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) Als je op onbekende termen stuit, kun je altijd onze [woordenlijst](https://consensys.net/knowledge-base/a-blockchain-glossary-for-beginners/) raadplegen.



Voor alle duidelijkheid, er wordt eigenlijk niets *verstuur*d. Een blockchain netwerk dat met smart contracts zoals Ethereum werkt, bevat een aantal verschillende componenten, of functies. Een daarvan is wat wij een "computer" zouden noemen: de Ethereum Virtual Machine, of EVM, die programma's ("smart contracts") kan uitvoeren. De ruggengraat van het systeem is echter een *verspreid grootboek*: **stel je een spreadsheet voor met alle wallet-adressen van Ethereum en waarbij elk adres een kolom bevat met de crypto-activa die het bevat.**


Laten we dit met een voorbeeld verduidelijken. Stel dat Geert een transactie naar Lotte wil sturen. Geert heeft 1,36 ETH in zijn account en hij is van plan om Lotte 0,5 ETH te sturen. Klinkt als een goede dag voor Lotte, zelfs in een berenmarkt.


Geert opent zijn MetaMask-wallet, voert het adres van Lotte in, stelt de parameters voor gas in die voor hem oké zijn, en klikt op 'Versturen'.


Op dit moment komt de transactie in een lokale, tijdelijke bewaarstatus, die bekend staat als de *lokale geheugenpool,* of *lokale mempool*. De transactie wordt dan opgepikt door de dichtstbijzijnde node in het netwerk. Afhankelijk van Geerts [instellingen voor gas,](https://metamask.zendesk.com/hc/en-us/articles/360022895972-Using-advanced-gas-controls) zal zijn transactie worden geprioriteerd (h**oe meer g[aseenheden](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas) Geert heeft besteed, hoe sneller zijn transactie wordt verwerkt)**, en naar andere nodes in het netwerk wordt doorgestuurd. De nodes controleren of Geert genoeg ETH heeft voor de transactie en gaan hierna de transactie echt uitvoeren: **het grootboek wordt gewijzigd en er wordt 0,5 ETH afgetrokken van het saldo van Geert en aan de wallet van Lotte toegevoegd.**


*Blockchain-transacties zijn onomkeerbaar.* Er is echter niet echt ETH doorheen een netwerk verplaatst. Het is niet zoals een e-mail die van Geert zijn computer naar de MetaMask-inbox van Lotte is verstuurd. Geert heeft een verzoek d**at in MetaMask geverifieerd is m[et zijn privésleutels,](https://metamask.zendesk.com/hc/en-us/articles/4404722782107-User-guide-Secret-Recovery-Phrase-password-and-private-keys)** naar het netwerk verstuurd om zijn account te debiteren en dat van Lotte te crediteren. Nadat het verificatieproces in de protocollen van het netwerk is geprogrammeerd, is de transactie afgerond.


#### 
*Transacties houden verder niets extra in. Ze zijn alleen een verzoek aan het grootboek om de fondsen van verschillende adressen te herverdele*n.


 


**Als er iets mis gaat**
------------------------


Er kan van alles fout gaan, om veel redenen. Vaak is de reden softwaregerelateerd: MetaMask heeft een bug of er is iets verkeerd geconfigureerd wat betreft het netwerk dat je probeert te gebruiken, waardoor er een verbindingsfout is opgetreden.


Een **vaak voorkomend probleem is dat de gebruiker, in een poging om minder te betalen voor zijn transactie, een zeer lage gaslimiet instelt** en dat, omdat het netwerk overbelast is, er gedurende lange tijd in geen enkel blok ruimte is voor zo'n 'goedkope' transactie. Na verloop van tijd wordt een dergelijke transactie 'stale' (volledig geblokkeerd), en moet deze door de gebruiker worden geannuleerd.


**Als je een transactie hebt verstuurd en deze is nog niet afgerond**, wordt de status ervan in MetaMask weergegeven als 'in behandeling'.


**Als je een transactie hebt verstuurd en deze is mislukt, is de meest waarschijnlijke oorzaak een gebrek aan gas**. Met andere woorden, de kosten van gas voor de transactie waren hoger dan wat er in je wallet, in de originele valuta van het netwerk, beschikbaar was.



#### Info


Meer informatie over het berekenen van de kosten voor gas vind je in onze [handleiding over gas](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas).



Er kunnen verschillende redenen voor zijn. Houd ook steeds rekening met het type transactie dat je wilt uitvoeren. Als je een NFT wilt minten tijdens het spitsuur van het netwerk, heb je heel veel gas nodig. Als je een nieuwe of experimentele transactie uitprobeert, kan het de moeite waard zijn om dit op een testnetwerk te proberen voordat je echte netwerkkosten betaalt.


 


**Het probleem oplossen**
-------------------------


### **Sleutelfactor #1: Lokaal of uitgezonden naar netwerk**


Wanneer je het probleem van je transactie gaat analyseren, vooral als het gaat om een transactie die in behandeling is, moet je kijken of de transactie nog steeds in je lokale mempool zit, of dat ze in het netwerk terecht is gekomen en daar om welke reden dan ook vastzit. Als de transactie in je lokale mempool zit, kan het probleem misschien worden opgelost door je MetaMask-wallet te vergrendelen en ontgrendelen (**zorg ervoor dat je je wachtwoord kent en je geheime herstelzin hebt opgeslagen**). Als ze het netwerk heeft bereikt, is de oplossing wat ingewikkelder.


Meer informatie over het oplossen van deze problemen vind je in de onderstaande links.  
  



### **Sleutelfactor #2: Nonce**


Dit woord kan een aantal verschillende betekenissen hebben. Het is een samentrekking van "slechts eenmaal gebruikt nummer", en in deze context betekent het ruwweg "transactienummer", vanaf de eerste transactie van het verzendende adres. Je kunt jezelf in de problemen werken als je bijv. tegelijkertijd twee verschillende transacties vanuit verschillende MetaMask-instanties met hetzelfde wallet-adres verstuurt. **De transacties van je adres moeten in oplopende volgorde gebeuren, volgens hun nonce.** Maar net zoals nonces een vastgelopen transactie kunnen veroorzaken, worden ze ook gebruikt om een transactie te deblokkeren.


Meer informatie over deze techniek [vind](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction) je hier.


 


**Volgende stappen**
--------------------


### *Als je een mislukte transactie hebt, of een transactie die in behandeling is, kun je voor meer hulp de volgende bronnen raadplegen.*


#### [Tokens vanuit je MetaMask-wallet versturen](https://metamask.zendesk.com/hc/en-us/articles/360015488931)


#### [Een transactie die in behandeling is versnellen of annuleren](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction)


#### [Waarom is mijn transactie mislukt met de foutmelding 'Niet genoeg gas'?](https://metamask.zendesk.com/hc/en-us/articles/360038849792-Why-did-my-transaction-fail-with-an-Out-of-Gas-error-How-can-I-fix-it-)


#### [Probleemoplossing voor Uniswap](https://metamask.zendesk.com/hc/en-us/articles/360053394291-Uniswap-support-and-troubleshooting-tips)


#### [Gebruikersgids: Gas](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas)


#### [Kan ik een al bevestigde transactie terugdraaien?](https://metamask.zendesk.com/hc/en-us/articles/360059957352-Can-I-reverse-an-already-confirmed-transaction-)


 


**Veelgestelde vragen**
-----------------------


#### 
*V: Een account in mijn wallet heeft een transactie die in behandeling is (nog steeds in de wachtrij). Kan ik een andere transactie starten vanuit een ander account binnen dezelfde wallet?* A: Ja, dat kan. De nonce wordt niet per wallet, maar per account geteld.

