Wanneer je een transactie indient op Ethereum of een compatibel netwerk, is een deel van het gas dat je betaalt een verzoek aan het netwerk om je transactie eerder te verwerken - dit element staat bekend als de prioriteitskosten. Hoewel MetaMask je zal helpen door de totale gaskosten te berekenen die waarschijnlijk je transactie zal laten oppakken, kun je lang wachten als je met een lage gasprijs indient. Advies over welk tarief voor gas je moet instellen om een transactie binnen een redelijke tijd te voltooien, kun je vinden via de [Gas Tracker van Etherscan](https://etherscan.io/gastracker), of via een soortgelijke tracker van de andere netwerken die je gebruikt.


Toch kan het gebeuren dat er soms iets mis gaat, en dat er een transactie vast komt te zitten, of heel lang in behandeling is.


Het maakt niet uit hoe je hier terecht bent gekomen, dit kun je op een paar verschillende manieren oplossen.


 


### Voordat je verdere actie onderneemt, moet je als eerste je browser volledig afsluiten, deze opnieuw openen en MetaMask ontgrendelen (op mobiel sluit je gewoon de app en open je deze opnieuw). Als dit het probleem hierdoor niet is opgelost, ga dan verder met het volgende:


 


**Een transactie versnellen**
-----------------------------


![MetaMask transacties versnellen](https://support.metamask.io/hc/article_attachments/12927043481371)


Probeer een van de onderstaande opties:


* Wacht tot het netwerk bereid is om de transacties voor deze prijs te verwerken.
* Als je dit nog niet hebt gedaan, klik je op de knop **Versnellen**. Hiermee kun je dezelfde transactie opnieuw indienen, maar met een hoger tarief voor gas waardoor de transactie sneller kan worden verwerkt. Omdat dit proces dezelfde nonce hergebruikt als het origineel, hoef je niet twee keer voor gas te betalen.


Houd er rekening mee dat **het versnellen van de transactie het bedrag dat je voor de transactie uitgeeft, zal verhogen**.


 


**Een transactie annuleren — Methode 1: Annuleren in de app**
-------------------------------------------------------------


Als je dit nog niet hebt gedaan, moet je op **Annuleren** klikken (zie hierboven in de screenshot) om de transactie te annuleren. Houd er rekening mee dat **een annulering alleen kan worden *uitgevoerd* als de transactie op het netwerk nog steeds in behandeling is.** Transacties die zijn bevestigd, kunnen niet worden teruggedraaid.


 


**Een transactie annuleren — Methode 2: Custom nonce**
------------------------------------------------------


Hierbij wordt een nieuwe transactie verzonden met dezelfde nonce (een identificatienummer voor elke transactie, afgeleid van de uitdrukking "nummer dat slechts eenmaal wordt gebruikt"). De transactie hoeft eigenlijk geen waarde te hebben, je kunt bijv. 0 ETH sturen. Het gaat erom dat je voldoende gas betaalt, zodat het netwerk er prioriteit aan kan geven.


Als je deze methode gebruikt, **moet je terugwerken vanaf de oudste lopende transactie in de wachtrij die je wilt annuleren**. Je kunt bijv. niet een transactie met als nonce 10 annuleren, voordat je nonce 9 annuleert.


*De onderstaande screenshots zijn op verschillende tijdstippen gemaakt, dus de gaskosten die erin worden getoond kunnen variëren, zelfs van stap tot stap. Laat dit je niet afschrikken! Wanneer je dit zelf doet, wordt MetaMask automatisch in realtime bijgewerkt om marktkoersen te tonen.*




Extensie Mobiel


1. Schakel, in de geavanceerde instellingen,**Nonce transactie aanpassen** en **Geavanceerde instellingen voor gas** in. Met de laatstgenoemde kun je de gasprijs manipuleren, en kun je ervoor zorgen dat de annuleringstransactie wordt verwerkt, voordat de originele transactie die je wilt annuleren, wordt verwerkt.



#### Opmerking:


MetaMask Extension heeft momenteel een experimentele functie beschikbaar genaamd [Enhanced Gas Fee UI](https://metamask.io/1559/) (niet te verwarren met [geavanceerde instellingen voor gas](https://support.metamask.io/hc/en-us/articles/360022895972)). Deze stappen kun je volgen, ongeacht of dit al dan niet is ingeschakeld, maar houd er wel rekening mee dat ze verschillend zijn. De onderstaande stappen gebruiken geen Enhanced Gas UI. Houd in gedachten:



	* Als je Enhanced Gas UI hebt ingeschakeld, moet je nog steeds 'Nonce transactie aanpassen' hebben ingeschakeld.
	* Als je Enhanced Gas UI niet hebt ingeschakeld, moet je zowel 'Geavanceerde instellingen voor gas' als 'Nonce transactie aanpassen' hebben ingeschakeld.

![MetaMask geavanceerde instellingen](https://support.metamask.io/hc/article_attachments/12927064113947)
2. **Een nieuwe transactie versturen**. In de nieuwe transactie stuur je **NAAR JEZELF**, dus naar je openbare MetaMask-adres. **Voer in het veld 'Custom Nonce' dezelfde nonce in als van de transactie die nog in behandeling is**:


![Metamask_custom_transaction_nonce_Extension.png](https://support.metamask.io/hc/article_attachments/12927064259483)
3. Klik nu naast 'Kosten voor Gas' op 'Bewerken' (als je de experimentele [Enhanced Gas-UI](https://support.metamask.io/hc/en-us/articles/360022895972-Using-advanced-gas-controls#:~:text=%C2%A0-,Enhanced%20Gas%20UI,-Since%20the%20introduction) hebt ingeschakeld, wordt dit als 'Markt' weergegeven). Je ziet nu de onderstaande opties:


![MetaMask geavanceerde instellingen voor gas extensie](https://support.metamask.io/hc/article_attachments/12927065407515)


Om ervoor te zorgen dat je annuleringsverzoek met prioriteit wordt behandeld, en voordat de originele transactie wordt verwerkt, **moet je meer gas betalen**. Volg deze instructies:


	* Stel een **limiet voor gas** in die *vergelijkbaar is met, of iets hoger is dan* je originele transactie.
	* Stel je **maximale prioriteitskosten** *minstens 10% hoger* in (in gwei) dan de kosten voor gas van de originele (in behandeling zijnde) transactie. Als die transactie bijv. een gasprijs van 30 gwei had, dan stel je de maximale prioriteitskosten van de annuleringstransactie in op 33-35 gwei.
	* Zorg ervoor dat je maximale kosten minstens 30% hoger zijn, dan de maximale kosten van de transactie die je wilt vervangen. Als je vorige kosten bijv. 150 gwei waren, dan kies je deze keer voor kosten van rond de 200 gwei.Gebruik een gas-tracker zoals die van [Etherscan](https://etherscan.io/gastracker) of [ETH Gas Station,](https://ethgasstation.info/) voor meer informatie over de aanbevolen maximale kosten.




1. **Schakel in Instellingen > Geavanceerd 'Nonce transacties aanpassen' in.**
2. **Een nieuwe transactie versturen.** In de nieuwe transactie stuur je NAAR JEZELF, dus naar je openbare MetaMask-adres. **Voer in het veld 'Custom Nonce' dezelfde nonce in als van de transactie die nog in behandeling is**.


Om de aangepaste nonce in de app te vinden, ga je naar het transactiebevestigingsscherm, dat verschijnt nadat je de token en de ontvanger hebt ingevoerd. Druk op 'Bewerken' om het te wijzigen:


![MetaMask aangepaste transactie nonce Mobiel](https://support.metamask.io/hc/article_attachments/12927068442907)
3. Nu moet je ervoor zorgen dat je gasinstellingen zo zijn geconfigureerd dat je vervangingstransactie wordt verwerkt. Tik in het bevestigingsscherm van de transactie op de gemarkeerde gaswaarde:


![MetaMask geavanceerde instellingen voor gas mobiel](https://support.metamask.io/hc/article_attachments/12927041593755)


Ga nu naar 'Geavanceerde opties' vanuit het menu dat verschijnt.
4. Vanaf hier kun je het gas precies aanpassen om ervoor te zorgen dat je transactie wordt opgehaald. Je zult nu naar een scherm kijken dat er zo uitziet:


![MetaMask geavanceerde instellingen voor gas mobiel](https://support.metamask.io/hc/article_attachments/12927063201691)


Vanaf hier pas je de gasinstellingen aan. Volg deze instructies om ervoor te zorgen dat je transactie wordt opgehaald:


	* Stel een **limiet voor gas** in die *vergelijkbaar is met, of iets hoger is dan* je originele transactie.
	* Stel je **maximale prioriteitskosten** *minstens 10% hoger* in (in gwei) dan de kosten voor gas van de originele (in behandeling zijnde) transactie. Als die transactie bijv. een gasprijs van 30 gwei had, dan stel je de maximale prioriteitskosten van de annuleringstransactie in op 33-35 gwei.
	* Zorg ervoor dat je **maximale kosten** *minstens 30% hoger* zijn, dan de maximale kosten van de transactie die je wilt vervangen. Als je vorige kosten bijv. 150 gwei waren, dan kies je deze keer voor kosten van rond de 200 gwei.Gebruik een gas-tracker zoals [die van Etherscan](https://etherscan.io/gastracker) of [ETH Gas Station](https://ethgasstation.info/), voor meer informatie over de aanbevolen maximale kosten.



