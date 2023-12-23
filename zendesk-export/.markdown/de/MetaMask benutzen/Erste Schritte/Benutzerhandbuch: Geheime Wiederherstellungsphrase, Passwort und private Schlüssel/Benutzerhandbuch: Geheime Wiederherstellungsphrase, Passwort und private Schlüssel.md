
#### Neu bei Krypto und Web3?


Besuchen Sie [MetaMask Learn](https://learn.metamask.io/) für eine einfache Lernerfahrung, die speziell für Web3-Neulinge entwickelt wurde. Es ist völlig kostenlos, in mehreren Sprachen verfügbar und enthält nützliche Tools wie Simulationen, die Ihnen helfen, sich mit MetaMask zurechtzufinden.



### In diesem Artikel:


* [Wie sich die Sicherheit von MetaMask von herkömmlichen Webkonten unterscheidet](#h_01FYVAXCSH95CQ08Q0P2VJA5HV)
* [Was ist eine geheime Wiederherstellungsphrase?](#h_01FYVAXJQT914HCHEYFPNMEJEA)
* [Geheime Wiederherstellungsphrase Dos und Don'ts](#h_01FYVAXSE5C9E4YBCSWT2F2RBQ)
* [Geheime Wiederherstellungsphrase FAQs](#h_01FYVAXZYWJENFWG9K9CJTQFK7)
* [Passwörter und MetaMask](#h_01FYVAY5K22PX6926537V8B4SX)
* [Private Schlüssel FAQs](#h_01FYVAYH3ZZ8VW8BPDDADWRC8E)




**MetaMask: ein anderes Modell der Kontosicherheit**
-----------------------------------------------------


[Die öffentliche Blockchain-Technologie](https://metamask.zendesk.com/hc/en-us/articles/360015489611) verwendet im Vergleich zu herkömmlichen Online-Technologien eine sehr andere Reihe von Tools, um Benutzerdaten zu schützen. Die meisten von uns sind es gewohnt, ein Konto mit einer App oder einem Dienst zu erstellen und beispielsweise an den Support zu schreiben, um unser Passwort oder unseren Benutzernamen zurückzusetzen. Wir sind es gewohnt, dass die App unsere Daten speichert, vermutlich auf einer Art Computer, der zum Unternehmen gehört.


Nun... MetaMask funktioniert nicht so. MetaMask hat drei verschiedene Arten von **Geheimnissen**, die auf verschiedene Weise verwendet werden, um Ihr Wallet und Ihre Konten privat und sicher zu halten: Die geheime Wiederherstellungsphrase, das Passwort und private Schlüssel. Wir werden Sie durch diese Geheimnisse führen, eines nach dem anderen.


 


**Einführung in geheime Wiederherstellungsphasen**
--------------------------------------------------


Eine der wichtigsten (Sie werden sehen, was ich dort getan habe) Technologien, die MetaMask zugrunde liegen, und die meisten nutzerbezogenen Tools im Crypto Space ist die *Seed Phrase* oder wie sie in MetaMask genannt wird, Ihre *geheime Wiederherstellungsphrase*.


#### **Alle Ihre Konten werden mathematisch von Ihrer geheimen Wiederherstellungsphrase abgeleitet. Sie können sich das SRP wie einen Schlüsselring vorstellen, und es enthält so viele private Schlüssel, wie Sie möchten: und jeder dieser Schlüssel steuert ein Konto.**


Wenn Sie nun eine technische Erklärung wünschen: Seed-Phrasen, wie wir sie heute kennen, wurden gemäß einem Standard, der als Bitcoin Improvement Proposal 39 oder [BIP-39](https://en.bitcoin.it/wiki/BIP_0039) bezeichnet wird, für die Verwendung in Bitcoin kodifiziert. Vereinfacht ausgedrückt, wird eine Reihe von Wörtern mit einem hohen Maß an Zufälligkeit aus einer bestimmten [Liste von Wörtern](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt) ausgewählt. In MetaMask und vielen anderen Ethereum-kompatiblen Technologien gibt es 12 Wörter in einer Seed-Phrase. Einige ältere Seeds, die vom Brave generiert wurden, und einige Hardware-Wallets verwenden 24-Wörter-Phrasen.


Jedes dieser Wörter entspricht einer Reihe von Zahlen, und wenn sie in **einer bestimmten Reihenfolge** platziert werden, stellen sie eine viel benutzerfreundlichere Weise dar, sich eine sehr, sehr lange Zahl zu merken. Diese Nummer wird dann verwendet, um Ihre Konten *deterministisch* zu generieren, und Sie können hören, dass Menschen auf deterministische Brieftaschen verweisen. In der Informatik wird Deterministik verwendet, um einen Prozess (normalerweise einen Algorithmus einer Art) zu beschreiben, der *immer* dasselbe Ergebnis erzeugt. Mit anderen Worten, **Ihre geheime Wiederherstellungsphrase wird immer die gleiche Gruppe von Konten generieren, die davon abgeleitet** werden.


 


### Es gibt eine Reihe wichtiger Funktionen, die hier zu beachten sind:


* Die **geheime Wiederherstellungsphrase ist das Geheimnis, das die Brieftasche steuert**. Wenn jemand dieses Geheimnis hat, hat er vollständigen Zugriff auf das Wallet. **MetaMask behält Ihr SRP nicht:** **[Sie sind der Verwahrer Ihres Wallets.](https://metamask.zendesk.com/hc/en-us/articles/360059952212)** MetaMask werden **niemals** nach Ihrer geheimen Wiederherstellungsphrase fragen, selbst in einem Szenario für den Kundensupport. Wenn jemand danach fragt, versucht er wahrscheinlich, Sie zu betrügen oder Ihr Geld zu stehlen.
* Ihr SRP wird **lokal verwendet, um private Schlüssel abzuleiten**, einen pro Konto/Adresse. Konten werden in der Blockchain gespeichert, und diese privaten Schlüssel entsperren diese Konten.
* **Wenn Sie die App** oder die Erweiterung deinstallieren, ist die lokale Version der Daten verloren (die bemerkenswerte Ausnahme ist der [Tresor](https://metamask.zendesk.com/hc/en-us/articles/360018766351)), aber alle Transaktionen, die Sie mit dieser lokalen Version von MetaMask durchgeführt haben, wurden in der Blockchain aufgezeichnet. Daher sollten die Transaktionen sowohl in einem [Block Explorer](https://metamask.zendesk.com/hc/en-us/articles/360057536611) als auch in einer anderen Instanz von MetaMask reflektiert werden, solange Sie [die Wiederherstellung mit derselben geheimen Wiederherstellungsphrase](https://metamask.zendesk.com/hc/en-us/articles/360015289612) (**mit den Wörtern in derselben Reihenfolge**) durchführen. Dies bedeutet, dass Sie, solange Sie Ihre geheime Wiederherstellungsphrase haben, MetaMask immer deinstallieren und Ihre Brieftasche wiederherstellen können.
* **Innerhalb Ihres Wallets können Sie eine sehr große Anzahl separater Konten haben.** Wenn MetaMask Ihre Brieftasche aus der geheimen Wiederherstellungsphrase erstellt oder wiederherstellt, erstellt es zunächst nur das erste Konto. Alle [zusätzlichen Konten, die Sie erstellen](https://metamask.zendesk.com/hc/en-us/articles/360015489271), können jedoch in einer zukünftigen Instanz von MetaMask neu erstellt werden. **Da das Wallet *deterministisch* ist, wird es immer die gleichen Konten in der gleichen Reihenfolge neu erstellen. Weitere Informationen zu diesem Problem finden Sie in den folgenden FAQs.** Beachten Sie jedoch, dass die zusätzlichen Konten (über das erste hinaus, automatisch als „Konto 1“ bezeichnet) ***nicht*** unter allen Umständen automatisch zu Ihrem Konto hinzugefügt werden. Weitere Informationen finden Sie [in](https://metamask.zendesk.com/hc/en-us/articles/360015489271-How-to-add-missing-accounts-after-restoring-with-Secret-Recovery-Phrase#:~:text=If%20you%20have,automatically%20re%2Dadded.) unserer Erklärung hier.
* **Es ist möglich, [Konten](https://metamask.zendesk.com/hc/en-us/articles/360015489331) von anderen Ethereum-kompatiblen Technologien in ein MetaMask-Wallet zu importieren.** Dazu wird der *private Schlüssel* dieses spezifischen Kontos verwendet. Dieses **Konto wird jedoch nicht automatisch von MetaMask in einer anderen Instanz wiederhergestellt; Sie müssen es manuell erneut hinzufügen**. Wenn Sie also Konten manuell importiert haben, **notieren Sie sich ihre privaten Schlüssel auf die gleiche Weise wie Sie es mit Ihrer Seed-Phrase gemacht** haben, um sie in Zukunft erneut importieren zu können.


 


**MetaMask Geheime Wiederherstellungsphrase: Dos und Don'ts**
-------------------------------------------------------------




**Do:**

* **Notieren Sie Ihre geheime Wiederherstellungsphrase an einem sicheren Ort**. Wir können Ihnen nicht genau sagen, wo, da das von Ihren Umständen abhängt.
	+ Die Bedeutung der Handschrift Ihrer geheimen Wiederherstellungsphrase ist, dass sie nicht online gestohlen werden kann. Wenn Sie es beispielsweise in einer Datei in einem mit dem Internet verbundenen Cloud-Speicherordner speichern, könnte es theoretisch gestohlen werden.
* Überprüfen Sie Ihre Rechtschreibung und dass Sie jedes Wort in der gleichen Reihenfolge aufgeschrieben haben, in der sie gegeben wurden.
* Wenden Sie sich an [die offiziellen Kanäle](https://metamask.zendesk.com/hc/en-us/articles/360058230211) des MetaMask Support, wenn Sie Hilfe benötigen.





**Nicht:**

* Bewahren Sie es an einem leicht zu erkennenden oder leicht gehackten Ort auf; z. B. in einem in der Cloud gespeicherten Dokument oder einer E-Mail mit dem Titel „Seed Phrase“; auf einer Post-it-Notiz, die an Ihrem Computer geklebt ist.
* Stellen Sie Ihre Seed-Phrase jedem zur Verfügung, auch wenn er sagt, dass er vom MetaMask-Support stammt.
* Ändern Sie die Reihenfolge der Wörter.





 


**Geheime Wiederherstellungsphrase: FAQs**
------------------------------------------


### Meine Seed-Phrase hat ein anderes Konto wiederhergestellt!


Bitte lesen Sie den Knowledge Base-Artikel zu diesem Thema [hier](https://metamask.zendesk.com/hc/en-us/articles/360058120992). Weitere Informationen zum Kontext und Hintergrundinformationen finden Sie [hier](https://community.metamask.io/t/restored-metamask-no-coins-are-showing/878/107?u=jacob.cantele) im Community Thread.


### Andere geheime Wiederherstellungsphrase FAQs:


[Anzeige Ihrer geheimen Wiederherstellungsphrase](https://metamask.zendesk.com/hc/en-us/articles/360015290032)


[Wiederherstellung Ihrer geheimen Wiederherstellungsphrase](https://metamask.zendesk.com/hc/en-us/articles/360018766351)


[Importieren einer Seed-Phrase aus einer anderen Wallet-Software: Ableitungspfad](https://metamask.zendesk.com/hc/en-us/articles/360060331752)


[Wallet Migrationshandbuch](https://metamask.zendesk.com/hc/en-us/articles/4867408571803)


[Wie importiere ich ein Konto](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[Wie überprüfe ich meine Wallet-Aktivität im Blockchain-Explorer](https://metamask.zendesk.com/hc/en-us/articles/360057536611)


[Was ist eine geheime Wiederherstellungsphrase und wie bewahre ich mein Wallet sicher auf?](https://metamask.zendesk.com/hc/en-us/articles/360060826432)


 


**Passwörter und MetaMask**
---------------------------


MetaMask verwendet Passwörter für einen einzigen Zweck: um die App selbst zu schützen; mit anderen Worten, um die App zu öffnen, sei es die mobile App oder die In-Browser-Erweiterung. Sobald Sie Ihr Wallet aus Ihrer geheimen Wiederherstellungsphrase wiederhergestellt oder erstellt haben, benötigen Sie es nicht regelmäßig (**obwohl Sie es gesichert und sicher aufbewahren** sollten), und Sie verwenden Ihr Passwort (oder häufiger auf Mobilgeräten, biometrische Authentifizierung wie Gesichtserkennung oder Ihren Fingerabdruck), um die App zu entsperren. Weitere Informationen finden Sie in unserem Artikel [hier](https://metamask.zendesk.com/hc/en-us/articles/4405451730331).


 


**Private Keys**
----------------


Während eine geheime Wiederherstellungsphrase zum Erstellen und Wiederherstellen Ihres gesamten MetaMask Wallet, einschließlich aller in diesem Wallet erstellten Konten, verwendet wird, verfügt jedes Konto über seinen eigenen *Private Key*. Mit diesem Schlüssel können Sie dieses Konto und nur dieses Konto in ein anderes Wallet importieren. Ebenso können einzelne Konten aus anderen Kryptotechnologien in Ihr MetaMask-Wallet importiert werden.


### Private Keys FAQs:


[Was sind importierte Konten?](https://metamask.zendesk.com/hc/en-us/articles/360015289932)


[Wie importiere ich ein Konto](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[So exportieren Sie den privaten Schlüssel eines Kontos](https://metamask.zendesk.com/hc/en-us/articles/360015289632)


[Kann ich das Coinbase Wallet-Konto in mein MetaMask-Wallet importieren?](https://metamask.zendesk.com/hc/en-us/articles/360058485292)

