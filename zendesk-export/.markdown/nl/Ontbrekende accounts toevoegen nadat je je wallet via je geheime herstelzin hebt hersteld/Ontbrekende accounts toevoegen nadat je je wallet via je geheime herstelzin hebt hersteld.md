
#### Opmerking:


**Geïmporteerde** accounts worden **niet** opnieuw toegevoegd wanneer je je wallet herstelt met gebruik van je geheime herstelzin. [Ze moeten handmatig worden toegevoegd](https://support.metamask.io/hc/en-us/articles/360015489331) op dezelfde manier als waarop ze oorspronkelijk zijn geïmporteerd.



**Deel je geheime herstelzin met NIEMAND! Met deze woorden kunnen al je accounts worden gestolen. Je kunt je geheime herstelzin niet bewerken of wijzigen.**


 


Wanneer je [een wallet herstelt](https://support.metamask.io/hc/en-us/articles/360015289612-How-to-restore-your-MetaMask-account-from-Seed-Phrase-Secret-Recovery-Phrase) met je geheime herstelzin, voegt MetaMask automatisch alle extra accounts toe die je eerder had [aangemaakt](https://support.metamask.io/hc/en-us/articles/360015289452), maar alleen onder bepaalde voorwaarden.


MetaMask probeert, als het kan, je extra accounts toe te voegen (ervan uitgaande dat ze niet zijn [geïmporteerd](https://support.metamask.io/hc/en-us/articles/360015289932)) door je vorige accounts in oplopende volgorde te controleren (eerst Account 2, dan Account 3, etc.). **Accounts worden automatisch opnieuw toegevoegd als ze een ETH-saldo hebben dat niet nul is**. Dit proces eindigt echter wanneer MetaMask een account met 0 ETH tegenkomt, dus de eerste account met 0 ETH (en elke andere daarachter) zal *niet* worden toegevoegd.


Houd er rekening mee dat **dit proces de saldi alleen controleert op ETH op het Ethereum-mainnet**. Andere tokens, of tokens op andere netwerken, worden niet automatisch opnieuw toegevoegd.


**De accounts die niet automatisch opnieuw worden toegevoegd, kun je opnieuw toevoegen [door](https://support.metamask.io/hc/en-us/articles/360015289452) een account "aan te maken"**. Als je bijvoorbeeld tokens in account 4 hebt, maar die tokens zijn geen mainnet-ETH, dan wordt account 4 niet automatisch toegevoegd. Je kunt echter wel, via de onderstaande stappen, handmatig accounts toevoegen totdat je aan account 4 komt. Je account 4 van *voor* het herstel is gelijk aan account 4 van *na* het herstel, of je er nu wel of niet een naam aan had gegeven.


Als je de knop 'aanmaken' moet gebruiken om opnieuw accounts toe te voegen, hoef je niet te piekeren dat het adres van de account anders is. De adressen worden cryptografisch *deterministisch* afgeleid van je privésleutel, wat betekent dat ze altijd hetzelfde zijn. En omdat een Ethereum-account, wanneer eenmaal gemaakt, permanent bestaat, kun je gewoon verder gaan waar je gebleven was.


Volg de onderstaande stappen om je andere accounts te herstellen, in de volgorde waarin ze oorspronkelijk zijn aangemaakt:




Extensie Mobiel


1. Klik in de rechterbovenhoek op de favicon van het MetaMask-vervolgkeuzemenu
2. Klik op “Account aanmaken”, om je MetaMask-accounts te herstellen in de volgorde waarin ze zijn aangemaakt
3. Als je eerder de accounts een naam hebt gegeven, kun je ze via de onderstaande stap opnieuw een naam geven, voordat je op "**Aanmaken**" klikt


![How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase.gif](https://support.metamask.io/hc/article_attachments/9026739981083/How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase.gif)




1. Tik, in de linkerbovenhoek van het scherm, op het hamburger-icoontje om het menu te openen. Tik hier, naast de accountnaam, op het vervolgkeuzepijltje:
2. Tik op 'Nieuw account aanmaken':


![How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase_Mobile.gif](https://support.metamask.io/hc/article_attachments/9027058464027/How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase_Mobile.gif)




Als je de gezochte adressen nog steeds niet ziet, zijn ze waarschijnlijk met een andere geheime herstelzin aangemaakt, of ze staan op een geïmporteerd account dat je, via je privésleutel of JSON, opnieuw moet importeren. Meer informatie [over het importeren van een account vind je in dit artikel](https://support.metamask.io/hc/en-us/articles/360015489331-Importing-an-Account).

