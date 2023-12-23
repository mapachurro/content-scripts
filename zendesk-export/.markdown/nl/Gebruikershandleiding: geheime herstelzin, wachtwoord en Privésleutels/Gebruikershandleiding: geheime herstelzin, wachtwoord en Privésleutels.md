
#### Nieuw bij crypto en web3?


Ga naar [MetaMask Learn](https://learn.metamask.io/) voor een eenvoudige leerervaring, speciaal ontworpen voor nieuwkomers in web3. Het is volkomen gratis, beschikbaar in meerdere talen, en bevat nuttige hulpmiddelen zoals simulaties om je te helpen je weg te vinden met MetaMask.



### In dit artikel:


* [Hoe de beveiliging van MetaMask verschilt van traditionele webaccounts](#h_01FYVAXCSH95CQ08Q0P2VJA5HV)
* [Wat is een geheime herstelzin?](#h_01FYVAXJQT914HCHEYFPNMEJEA)
* [Geheime herstelzin do's en don'ts](#h_01FYVAXSE5C9E4YBCSWT2F2RBQ)
* [Geheime herstelzin veelgestelde vragen](#h_01FYVAXZYWJENFWG9K9CJTQFK7)
* [Wachtwoorden en MetaMask](#h_01FYVAY5K22PX6926537V8B4SX)
* [Privésleutels veelgestelde vragen](#h_01FYVAYH3ZZ8VW8BPDDADWRC8E)




**MetaMask: een ander model van accountbeveiliging**
-----------------------------------------------------


[Openbare blockchaintechnologie](https://metamask.zendesk.com/hc/en-us/articles/360015489611) gebruikt heel andere tools om gebruikersgegevens te beveiligen dan traditionele online technologieën. De meesten van ons zijn gewend om een account aan te maken bij een app, of service en bijvoorbeeld naar de ondersteuning te kunnen schrijven om ons wachtwoord of gebruikersnaam opnieuw in te stellen. We zijn gewend dat de app onze gegevens bewaart, vermoedelijk op een soort computer van het bedrijf.


Nou ... MetaMask werkt zo niet. MetaMask heeft drie verschillende soorten **geheim** die op verschillende manieren worden gebruikt om je wallet, en je accounts, privé en veilig te houden: de geheime herstelzin, het wachtwoord en de privésleutels. We zullen je één voor één door deze geheimen leiden.


 


**Inleiding tot geheime herstelzinnen**
---------------------------------------


Een van de sleutel (je zult zien wat ik daar deed) -technologieën die ten grondslag liggen aan MetaMask, en de meeste gebruikersaccount-gerelateerde tools in de cryptoruimte is de *seed phrase,* of zoals het wordt genoemd in MetaMask, je *geheime herstelzin*.


#### **Al je accounts zijn wiskundig afgeleid van je geheime herstelzin. Je kunt de SRP zien als een sleutelhanger, die zoveel privésleutels bevat als je maar wilt: en elk van die sleutels beheert een account.**


Als je een technische uitleg wilt: seed-phrases zoals we die nu kennen zijn gecodificeerd voor gebruik in Bitcoin, volgens een standaard die Bitcoin Improvement Proposal 39 heet, oftewel [BIP-39](https://en.bitcoin.it/wiki/BIP_0039). Eenvoudig gezegd wordt een reeks woorden met een hoge mate van willekeur geselecteerd uit een specifieke [lijst van woorden](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt). In MetaMask en vele andere Ethereum-compatibele technologieën zijn er 12 woorden in een seed phrase. Sommige oudere seeds die door de Brave-browser worden gegenereerd, en sommige hardware wallets, gebruiken 24-woorden zinnen.


Elk van deze woorden komt overeen met een reeks getallen, en wanneer ze geplaatst worden in **een specifieke volgorde**, vertegenwoordigen ze een veel gebruiksvriendelijkere manier om een heel, heel lang nummer te onthouden. Dat getal wordt dan gebruikt om *deterministisch* je accounts te genereren, en je hoort mensen misschien verwijzen naar deterministische wallets. In de computerwetenschap wordt deterministisch gebruikt om een proces te beschrijven (meestal een of ander algoritme) dat *altijd* hetzelfde resultaat oplevert. Met andere woorden, **je geheime herstelzin zal altijd dezelfde set accounts genereren die ervan zijn afgeleid**.


 


### Er zijn hier een aantal belangrijke functies aan te wijzen:


* De **geheime herstelzin is het geheim dat de wallet beheert**. Als iemand dit geheim heeft, hebben ze volledige toegang tot de wallet. **MetaMask bewaart je SRP niet:** **[jij bent de beheerder van je wallet.](https://metamask.zendesk.com/hc/en-us/articles/360059952212)** MetaMask-vertegenwoordigers zullen **nooit** om je geheime herstelzin vragen, zelfs niet in een klantenservice scenario. Als iemand er wel om vraagt, proberen ze je waarschijnlijk op te lichten of je geld te stelen.
* Je SRP wordt **lokaal gebruikt om privésleutels af te leiden**, één per account/adres. Accounts worden opgeslagen op de blockchain, en deze privésleutels ontgrendelen die accounts.
* **Als je de app** of de extensie verwijdert, dan is de lokale versie van de gegevens verdwenen (met uitzondering van de [vault](https://metamask.zendesk.com/hc/en-us/articles/360018766351)), maar alle transacties die je hebt uitgevoerd met die lokale versie van MetaMask zijn vastgelegd op de blockchain. Daarom moeten de transacties zowel op een [block explorer](https://metamask.zendesk.com/hc/en-us/articles/360057536611) en in een andere instantie van MetaMask, zolang je [herstelt met dezelfde geheime herstelzin](https://metamask.zendesk.com/hc/en-us/articles/360015289612) (**met de woorden in dezelfde volgorde**). Dit betekent dat zolang je je geheime herstelzin hebt, je MetaMask altijd kunt verwijderen en je wallet kunt herstellen.
* **Binnen je wallet kun je een heel groot aantal afzonderlijke accounts hebben.** Wanneer MetaMask je wallet creëert of herstelt vanuit de geheime herstelzin, produceert het in eerste instantie alleen de eerste account. Echter, elke [extra accounts die je aanmaakt kunnen opnieuw worden aangemaakt](https://metamask.zendesk.com/hc/en-us/articles/360015489271) in een toekomstige versie van MetaMask. **Omdat de wallet *deterministisch* is, zal het altijd dezelfde accounts opnieuw aanmaken, in dezelfde volgorde. Zie de onderstaande veelgestelde vragen voor meer informatie over deze kwestie.** Hou er echter rekening mee dat de extra accounts (naast de eerste, automatisch gelabeld als 'account 1') ***niet*** onder alle omstandigheden automatisch opnieuw aan je account worden toegevoegd. Zie onze uitleg [hier](https://metamask.zendesk.com/hc/en-us/articles/360015489271-How-to-add-missing-accounts-after-restoring-with-Secret-Recovery-Phrase#:~:text=If%20you%20have,automatically%20re%2Dadded.) voor meer informatie.
* **Het is mogelijk om [accounts](https://metamask.zendesk.com/hc/en-us/articles/360015489331) van andere Ethereum-compatibele technologieën te importeren in een MetaMask-wallet.** Om dit te doen, wordt de *privésleutel* van die specifieke account gebruikt. **Deze account wordt echter niet automatisch hersteld door MetaMask in een andere versie; je moet het handmatig opnieuw toevoegen**. Daarom, als je handmatig accounts hebt geïmporteerd, **noteer dan hun privésleutels, op dezelfde manier als je seed phrase**, om ze in de toekomst opnieuw te kunnen importeren.


 


**MetaMask geheime herstelzin: Do's en don'ts**
-----------------------------------------------




**Do:**

* **Noteer je geheime herstelzin ergens veilig**. We kunnen je niet precies vertellen waar, dat hangt af van je omstandigheden.
	+ Het belang van het met de hand schrijven van je geheime herstelzin is dat deze niet online kan worden gestolen. Als je het bijvoorbeeld opslaat in een bestand in een aan internet gekoppelde map voor cloud-opslag, kan het in theorie worden gestolen.
* Controleer je spelling en of je elk woord in dezelfde volgorde hebt opgeschreven.
* Neem contact op met de [officiële kanalen](https://metamask.zendesk.com/hc/en-us/articles/360058230211) van MetaMask Support als je hulp nodig hebt.





**Don't:**

* Het op een gemakkelijk te ontdekken of gemakkelijk te hacken plaats bewaren; bijvoorbeeld in een in de cloud opgeslagen document of e-mail met de titel 'Seed Phrase'; op een post-it briefje dat op je computer is geplakt.
* Je geheime herstelzin aan iemand geven, zelfs als ze zeggen dat ze van MetaMask Support zijn.
* De volgorde van de woorden wijzigen.





 


**Geheime herstelzinnen: veelgestelde vragen**
----------------------------------------------


### Mijn seed phrase heeft een ander account hersteld!


Raadpleeg [hier](https://metamask.zendesk.com/hc/en-us/articles/360058120992) een artikel in de kennisbank over dit onderwerp. Zie ook de community-conversatie [hier](https://community.metamask.io/t/restored-metamask-no-coins-are-showing/878/107?u=jacob.cantele) voor meer context en achtergrondinformatie.


### Andere veelgestelde vragen over de geheime herstelzin:


[Je geheime herstelzin onthullen](https://metamask.zendesk.com/hc/en-us/articles/360015290032)


[Je geheime herstelzin herstellen](https://metamask.zendesk.com/hc/en-us/articles/360018766351)


[Importeren van een seed phrase uit een andere wallet software: afleidingspad](https://metamask.zendesk.com/hc/en-us/articles/360060331752)


[Wallet migratiehandleiding](https://metamask.zendesk.com/hc/en-us/articles/4867408571803)


[Een account importeren](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[Hoe bekijk ik mijn wallet-activiteit op de blockchain explorer](https://metamask.zendesk.com/hc/en-us/articles/360057536611)


[Wat is een geheime herstelzin en hoe houd ik mijn wallet veilig?](https://metamask.zendesk.com/hc/en-us/articles/360060826432)


 


**Wachtwoorden en MetaMask**
----------------------------


MetaMask gebruikt wachtwoorden voor één enkel doel: om de app zelf te beveiligen; met andere woorden, om de app te openen, of het nu de mobiele app is of de in-browser extensie. Als je eenmaal je wallet hebt hersteld of aangemaakt met je geheime herstelzin, heb je die niet meer regelmatig nodig (**hoewel je er wel een back-up van moet maken**), en gebruik je je wachtwoord (of vaker op Mobile, biometrische verificatie zoals gezichtsherkenning of je vingerafdruk) om de app te ontgrendelen. Zie ons artikel [hier](https://metamask.zendesk.com/hc/en-us/articles/4405451730331) voor meer details.


 


**Privésleutels**
-----------------


Terwijl een geheime herstelzin wordt gebruikt om je gehele MetaMask-wallet aan te maken en te herstellen, inclusief alle accounts die in die wallet zijn aangemaakt, heeft elke account een eigen *privésleutel*. Deze sleutel kan worden gebruikt om die account, en alleen die account, te importeren in een andere wallet. Op dezelfde manier kunnen afzonderlijke rekeningen van andere cryptotechnologieën worden geïmporteerd naar je MetaMask-wallet.


### Veelgestelde vragen over privésleutels:


[Wat zijn geïmporteerde accounts?](https://metamask.zendesk.com/hc/en-us/articles/360015289932)


[Een account importeren](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[De privésleutel van een account exporteren](https://metamask.zendesk.com/hc/en-us/articles/360015289632)


[Kan ik een Coinbase-wallet account importeren naar mijn MetaMask-wallet?](https://metamask.zendesk.com/hc/en-us/articles/360058485292)

