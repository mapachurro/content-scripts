
#### Neu bei Krypto und Web3?


Besuchen Sie [MetaMask Learn](https://learn.metamask.io/) für eine einfache Lernerfahrung, die speziell für Web3-Neulinge entwickelt wurde. Es ist völlig kostenlos, in mehreren Sprachen verfügbar und enthält nützliche Tools wie Simulationen, die Ihnen helfen, sich mit MetaMask zurechtzufinden.



#### *Dieser Aufsatz erklärt und verweist auf Quellen, die sich mit Transaktionen und den Gründen für ihr Scheitern befassen. Ferner enthält er Links zu gängigen Szenarien für fehlgeschlagene Transaktionen und deren Behebung:*


* [Aufbau einer Blockchain-Transaktion](#h_01G79J04D0EN1VD8VS7C7J7KD1)
* [Häufige Probleme](#h_01G79J09NWA8CGR4VYC2PT5B6Y)
* [Wichtigste Korrekturen](#h_01G79J0J8JTRPM9MRB76EN1GPP)
* [Zusätzliche Ressourcen und nächste Schritte](#h_01G79J0RP8ZMZ1V1SKQY70TXCT)
* [FAQs](#h_01G79J18RBK27GZCF10CGN9GKP)


 


**Aufbau einer Blockchain-Transaktion**
---------------------------------------


Wenn wir in einem öffentlichen Blockchain-Netzwerk von „Transaktionen” sprechen, meinen wir in der Regel den Datenaustausch zwischen zwei Adressen, d. h. Token, ob fungibel oder nicht, oder andere Krypto-Vermögenswerte, die von einer Adresse an eine andere „geschickt” werden. Es gibt außerdem Transaktionen, die als „interne Transaktionen” bezeichnet werden. Dabei handelt es sich um Beziehungen zwischen Smart Contracts – die den Rahmen dieses Artikel jedoch sprengen würden.



#### Möchten Sie mehr Informationen?


Weitere Informationen zu Blockchain-Netzwerken und ihrer Funktionsweise im Allgemeinen finden Sie in unserem [Einführungsartikel hier](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-), und wenn Sie bei unbekannten Begriffen nicht weiter wissen, steht Ihnen unser [Glossar jederzeit zur Verfügung](https://consensys.net/knowledge-base/a-blockchain-glossary-for-beginners/).



Für ein besseres Verständnis kann jedoch festgestellt werden, dass nichts tatsächlich *versendet* wird. Ein Smart contract-enabled Blockchain-Netzwerk wie Ethereum hat eine Reihe verschiedener Komponenten oder Funktionen. Eines davon ist, was wir einen „Computer“ nennen würden: die Ethereum Virtual Machine oder EVM, die in der Lage ist, Programme („Smart Contracts“) auszuführen. Das „Rückgrat” des Systems ist jedoch ein verteiltes *Hauptbuch*: **Man kann sich darunter eine Tabelle vorstellen, die auf der einen Seite jede einzelne Ethereum-Wallet-Adresse enthält und jede Adresse besitzt eine Spalte für jede Art von Krypto-Asset, die sie verwahrt.** 


Das kann am besten an einem Beispiel erklärt werden. Nehmen wir an, dass Guillaume eine Transaktion an Dolores senden möchte. Guillaume hat 1,36 ETH auf seinem Konto und möchte Dolores 0,5 ETH schicken. Klingt nach einem guten Tag für Dolores, sogar in einem Bärenmarkt. 


Guillaume öffnet seine MetaMask-Wallet, gibt Dolores’ Adresse ein, stellt die Gasparameter ein, die er gerne zahlen möchte und betätigt mit „Senden”.


An dieser Stelle gelangt die Transaktion in einen lokalen temporären Haltestatus, der als *lokaler Speicherpool*oder *lokaler Mempool* bezeichnet wird. Die Transaktion wird dann vom nächstgelegenen Knoten im Netzwerk „abgeholt”; je nach Guillaumes [Gaseinstellungen](https://metamask.zendesk.com/hc/en-us/articles/360022895972-Using-advanced-gas-controls)wird seine Transaktion vorrangig bearbeitet (**je mehr Guillaume bereit ist, pro [Gaseinheit](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas) zu bezahlen, desto rascher wird seine Transaktion bearbeitet**) und an andere Netzwerkknoten weitergeleitet. Die Knoten überprüfen, ob Guillaume die ETH besitzt, die er ausgeben möchte und führen dann die „Transaktion” durch: **Das Hauptbuch wird aktualisiert; 0,5 werden von Guillaumes Konto abgebucht und werden Dolores gutgeschrieben.**


Die ETH haben sich nicht durch ein Netzwerk bewegt; es war keine E-Mail, die von Guillaumes Computer an Dolores’ MetaMask-Posteingang geschickt wurde o. ä. Guillaume hat eine mit seinen Private Keys über MetaMask **authentifizierte [Anfrage an das](https://metamask.zendesk.com/hc/en-us/articles/4404722782107-User-guide-Secret-Recovery-Phrase-password-and-private-keys)** Netzwerk geschickt. Sein Konto wurde belastet und der Betrag wurde dem von Dolores gutgeschrieben. Dies wurde nach den in den Netzwerkprotokollen programmierten Prüfverfahren so durchgeführt.


#### *Das ist das Wesen einer Transaktion: Eine Anfrage an das Hauptbuch, die Umverteilung eines bestimmten Betrages an eine andere Adresse durchzuführen.*


 


**Wenn etwas schiefgeht**
-------------------------


Es kann aus diversen Gründen etwas schiefgehen. Oft sind sie „softwaretechnischer Natur”: MetaMask hat ein Problem, oder das Netzwerk wurde falsch konfiguriert; es liegt ein Verbindungsfehler vor.


Ein **häufiges Problem ist, dass der Benutzer beim Versuch, weniger für seine Transaktion zu bezahlen, ein sehr niedriges Gaslimit festlegt** und die Netzwerke so überlastet sind, dass in keinem Block Platz für eine solch „preiswerte Transaktion” ist – manchmal auch für einen sehr langen Zeitraum: Irgendwann wird ist die Transaktion „veraltet” und muss vom Benutzer storniert werden.


**Wenn Sie eine Transaktion gesendet haben und diese noch nicht abgeschlossen ist**, wird ihr Status in MetaMask als „ausstehend” angezeigt.


**Wenn Sie eine Transaktion abgeschickt haben und diese fehlgeschlagen ist, ist die wahrscheinlichste Ursache ein Gasmangel:**: „Sie haben keinen Sprit mehr”, d. h. die Transaktion hatte Kosten in Form von Gas, die, multipliziert mit dem Gaspreis, zu einem Gesamtbetrag der netzwerkeigenen Währung führten, der größer war als der, den Sie in Ihrer Wallet hatten.



#### Info


Näheres zur Gasberechnung finden Sie in unserem [Gas-Leitfaden hier](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas).



Die Gründe dafür können vielfältig sein, aber eine Sache, die Sie berücksichtigen sollten, ist der Transaktionstyp. Das Mining von NFT während hoher Netzwerkbelastung kann viel Gas kosten. Wenn Sie eine neue oder experimentelle Transaktion ausprobieren wollen, kann es sich lohnen, sie in einem Testnetzwerk zu testen, bevor Sie echte Netzwerkgebühren bezahlen.


 


**Problembehebung**
-------------------


### **Hauptfaktor Nr. 1: Lokal oder Übertragung ins Netzwerk**


Bei der Diagnose Ihres Transaktionsproblems, insbesondere wenn es sich um eine ausstehende Transaktion handelt, müssen Sie prüfen, ob sich die Transaktion noch in Ihrem lokalen Mempool befindet, oder ob sie es ins Netzwerk geschafft hat und dort aus irgendeinem Grund stecken geblieben ist. Befindet sie sich nur in Ihrem lokalen Mempool, könnte die Lösung einfach das Sperren und Entsperren Ihrer MetaMask-Wallet (**vergewissern Sie sich, dass Sie Ihr Passwort kennen und Ihre geheime Wiederherstellungsphrase gesichert haben, bevor Sie das tun** ). Befindet sie sich bereits im Netzwerk ist die Lösung nicht so einfach.


Mehr über die Fehlerbehebung finden Sie in den folgenden   
Links.  



### **Hauptfaktor 2: Nonce**


Dieses Wort kann ein paar verschiedene Dinge bedeuten. Es ist eine Kontraktion von „nur einmal verwendete Zahl“, und in diesem Zusammenhang bedeutet es grob „Transaktionsnummer“, beginnend mit der ersten Transaktion, die von der Senderadresse durchgeführt wird. Sie können sich in echte Schwierigkeiten bringen, wenn Sie zum Beispiel zwei verschiedene Transaktionen von verschiedenen Instanzen von MetaMask mit derselben Wallet-Adresse zur gleichen Zeit abfeuern. **Die Transaktionen Ihrer Adresse müssen in aufsteigender Reihenfolge nach Ihrer Nonce geordnet sein.** So wie Nonces jedoch eine festgefahrene Transaktion verursachen können, können sie auch der Schlüssel sein, um eine Transaktion wieder in Gang zu bringen.


Mehr über diese Technik erfahren Sie [hier](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction).


 


**Nächste Schritte**
--------------------


### *Bei gescheiterten oder noch nicht abgeschlossenen Transaktionen können Sie die folgenden Informationsquellen zurate ziehen.*


#### [Wie versenden Sie Token aus meiner MetaMask-Wallet](https://metamask.zendesk.com/hc/en-us/articles/360015488931)


#### [So beschleunigen oder stornieren Sie eine ausstehende Transaktion.](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction)


#### [Warum ist meine Transaktion mit dem Fehler „Kein Gas” fehlgeschlagen?](https://metamask.zendesk.com/hc/en-us/articles/360038849792-Why-did-my-transaction-fail-with-an-Out-of-Gas-error-How-can-I-fix-it-)


#### [Uniswap Fehlersuche](https://metamask.zendesk.com/hc/en-us/articles/360053394291-Uniswap-support-and-troubleshooting-tips)


#### [Benutzerhandbuch: Gas](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas)


####  [Kann ich eine bereits bestätigte Transaktion rückgängig machen?](https://metamask.zendesk.com/hc/en-us/articles/360059957352-Can-I-reverse-an-already-confirmed-transaction-)


 


**FAQs**
--------


#### 
*Frage: In einem Konto in meiner Wallet gibt es eine ausstehende oder sich in der Warteschlange befindende Transaktion. Kann ich eine andere Transaktion von einem anderen Konto in derselben Wallet durchführen?* A: Ja, das können Sie. Die Nonce wird pro Konto und nicht pro Wallet gezählt.

