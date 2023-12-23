
#### Nieuw bij crypto en web3?


Ga naar [MetaMask Learn](https://learn.metamask.io/) voor een eenvoudige leerervaring, speciaal ontworpen voor nieuwkomers in web3. Het is volkomen gratis, beschikbaar in meerdere talen, en bevat nuttige hulpmiddelen zoals simulaties om je te helpen je weg te vinden met MetaMask.



Gas is de meeteenheid die weergeeft hoeveel rekenwerk vereist is voor het verwerken van transacties en smart contracts. Gas is in feite de term voor de transactiekosten die worden betaald voor het rekenwerk dat wordt uitgevoerd op de Ethereum Virtual Machine (EVM). Sinds Ethereum werd opgericht, zijn tal van EVM-compatibele (en non-EVM-compatible!) netwerken ontstaan en hebben ze vergelijkbare systemen aangenomen.


De term is vergelijkbaar met het gas dat een automotor aandrijft: het zijn de fluctuerende, soms dure bedrijfskosten. Meer complexe smart contracts vereisen meer gas om hun berekeningen uit te voeren, net zoals een grotere, krachtigere auto meer brandstof nodig heeft.


De methode voor het berekenen van de kosten voor gas is afhankelijk van het netwerk. Het berekenen van gas op Ethereum was vroeger heel ingewikkeld, maar werd aanzienlijk vereenvoudigd door de invoering van het Ethereum Improvement Protocol **(EIP) 1559** in augustus 2021 (ook bekend als de London Upgrade.) In wezen betaal je **basiskosten** voor elke eenheid gas die wordt ***verbrand*** (lees: het wordt verwijderd en verdwijnt) na succesvolle afronding van de transactie. Naast deze basiskosten worden ook **prioriteitskosten** toegevoegd. Deze betaal je ook in gas en hoe hoger het bedrag, hoe sneller de transactie zal worden afgerond.


In het brede bereik van beschikbare EVM-compatibele netwerken is gas, of een vergelijkbaar functionerend alternatief, de standaardmethode voor het berekenen van transactiekosten. De kosten worden betaald in de originele netwerk-token. Een transactie op Ethereum bijv. vereist ETH, voor het gebruik van BSC is BNB nodig en Polygon vereist MATIC. Sommige netwerken, zoals Polygon, hebben het EIP-1559-model van Ethereum compleet overgenomen, maar andere netwerken hebben aanpassingen gedaan. De C-Chain van Avalanche bv. [verbrandt zowel de basiskosten als de prioriteitskosten](https://docs.avax.network/learn/platform-overview/transaction-fees/#c-chain-fees), in plaats van alleen de basiskosten. 


Als je een meer diepgaand verhaal wilt lezen over hoe gas werkt op Ethereum, zie [hier](https://ethereum.org/en/developers/docs/gas/).


 


Hieronder vind je **nodige informatie over hoe je gas kunt gebruiken in Meta****Mask:**


#### **De gaslimiet (gebruikte eenheden gas)**


De *gaslimiet* is het **maximale aantal gaseenheden dat je wilt betalen voor** een transactie of EVM-berekening. Verschillende activiteiten vereisen verschillende hoeveelheden gas. Een normale transactie waarbij ETH of een token wordt verstuurd, kost normaal **21.000** gas, terwijl een ERC-20 token goedkeuring 45.000 vereist. Veel netwerken, zoals de EVM-compatibele blockchain Harmony, gebruiken een identiek model waarbij standaard transacties ook 21.000 gas kosten. 



#### Moet ik de gaslimiet aanpassen?


Nee! MetaMask stelt automatisch je gaslimiet in, afhankelijk van de transactie die je probeert uit te voeren. In de overgrote meerderheid van de gevallen is dit voldoende om je transactie te voltooien. Als je het wilt controleren of bewerken, zorg er dan voor dat je [geavanceerde instellingen voor gas](https://metamask.zendesk.com/hc/en-us/articles/360022895972) aan hebt staan (of de experimentele Enhanced Gas UI gebruikt) en op 'Bewerken' drukt in het transactiebevestigingsscherm.



#### **De basiskosten**


Elk block op het Ethereum-netwerk heeft basiskosten die worden bepaald door de netwerkvraag: de basiskosten zijn gebaseerd op de blockgrootte van het block ervoor, vergeleken met een doelblockgrootte (waarbij de grootte verwijst naar de totale hoeveelheid gas die wordt gebruikt voor alle transacties die het block bevat). Als de omvang van het vorige block de doelstelling overschrijdt, stijgende basiskosten voor het volgende block met 12,5%, zodat jij, de gebruiker (of je wallet), absolute zekerheid hebt over de basiskosten van het komende block. Je totale gaskosten moeten minimaal aan deze prijs voldoen om in aanmerking te komen voor opname in het block.


#### **De prioriteitskosten**


De *prioriteitskosten*, ook wel de 'miner tip' genoemd, stimuleert de miner om voorrang te geven aan jouw transactie.


Of dit daadwerkelijk naar een miner gaat, hangt natuurlijk af van het [consensusmechanisme](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) dat zij gebruiken: Ethereum-mainnet werd een Proof of Stake-netwerk na de Merge in september 2022, dus de prioriteitskosten gaan naar validators in plaats van miners.


#### **De maximale kosten**


De maximale kosten is het totale bedrag dat voor je transactie wordt betaald. Het wordt als volgt berekend: **(****basiskosten + prioriteitskosten) × aantal gaseenheden.** MetaMask stelt dit bedrag eerst in op basis van de geschiedenis van het vorige blok. Gebruikers kunnen dit bedrag echter wijzigen via de aangepaste instellingen (zie hieronder). Het verschil tussen maximale kosten voor gas en (basiskosten + maximale prioriteitskosten voor gas) wordt "terugbetaald" aan de gebruiker.


 


### **Aanvullende ideeën**


#### **Gwei**


Gwei staat voor [gigawei](https://ethgasstation.info/blog/gwei/). Eén Ethereum bestaat uit 1.000.000.000 gwei. [Gwei](https://www.investopedia.com/terms/g/gwei-ethereum.asp) wordt gebruikt voor de kosten van gas die gebruikers betalen voor het rekenwerk dat is vereist, om transacties op de Ethereum-blockchain te verwerken en goed te keuren. 


Ook andere netwerken berekenen de kosten via gwei, zoals Fantom, Harmony en Avalanche.


#### **Slippage**


Slippage is het verwachte procentuele verschil tussen een prijsvoorstel en de uitgevoerde prijs.


#### **Kosten voor gas**


De k*osten voor gas* verwijst naar de transactiekosten op de Ethereum-blockchain. Het is het bedrag dat gebruikers betalen om hun transactie te laten goedkeuren en afronden. 


#### **Basiskosten**


Worden gegenereerd door het protocol. Staat voor de minimale Gebruiktegas-multiplicator die vereist is om een transactie in een blok op te nemen (dus om een transactie af te ronden). Dit is het deel van de transactiekosten dat wordt verbrand.


 


### **Geavanceerde instellingen voor gas**


In MetaMask kun je instellingen voor gas tot in de puntjes te beheren. Dit kan van pas komen als je bijv. een dapp aan het testen bent. Het volledige artikel vind je h[ier.](https://metamask.zendesk.com/hc/en-us/articles/360022895972)


 


### **Veelgestelde vragen**


[Waarom heb ik kosten voor gas betaald voor een mislukte transactie?](https://metamask.zendesk.com/hc/en-us/articles/360045439051)


[Kunnen mijn kosten voor gas worden terugbetaald?](https://metamask.zendesk.com/hc/en-us/articles/360058370012)


[Hoe kan ik een transactie die in behandeling is versnellen of annuleren?](https://metamask.zendesk.com/hc/en-us/articles/360015489251)


[Hoe kan ik de kosten voor gas inschatten?](https://metamask.zendesk.com/hc/en-us/articles/360059562111)


[Waarom zijn mijn kosten voor gas zo hoog?](https://metamask.zendesk.com/hc/en-us/articles/360058751211-Why-my-gas-fees-are-so-high-)


[Foutmelding: [ethjs-query] while formatting outputs from RPC (foutmelding voor een transactie met een te lage prijs)](https://metamask.zendesk.com/hc/en-us/articles/4402538041869)


[Hoe kan ik de foutmelding 'niet genoeg fondsen', of de grijs weergegeven bevestigingsknop oplossen?](https://metamask.zendesk.com/hc/en-us/articles/360044703372)


 


 

