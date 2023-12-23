
#### Neu bei Krypto und Web3?


Besuchen Sie [MetaMask Learn](https://learn.metamask.io/) für eine einfache Lernerfahrung, die speziell für Web3-Neulinge entwickelt wurde. Es ist völlig kostenlos, in mehreren Sprachen verfügbar und enthält nützliche Tools wie Simulationen, die Ihnen helfen, sich mit MetaMask zurechtzufinden.



Gas ist die Maßeinheit dafür, wie viel Rechenarbeit für die Transaktionsabwicklung und Smart Contracts erforderlich ist. Der Begriff stammt im Wesentliche von Ethereum, wo er sich auf Berechnungen auf der Ethereum Virtual Machine (EVM) bezieht. Seit der Gründung von Ethereum zahlreiche EVM-kompatible (und nicht-EVM-kompatible!) Netzwerke sind entstanden und übernahmen ähnliche Modelle. .


Der Begriff ist analog zum Gas, das einen Automotor antreibt: Es sind die schwankenden, gelegentlich teuren Betriebskosten. Komplexere Smart Contracts benötigen mehr Treibstoff für ihre Berechnungen, so wie ein größeres, leistungsstärkeres Auto mehr Benzin benötigt, um zu fahren.


Die Methode zur Berechnung der Gasgebühren ist je nach Netzwerk verschieden. Beispiel:die Berechnung der Gasgebühren auf Ethereum war ziemlich kompliziert, wurde aber mit der Einführung des Ethereum Improvement Protocol **(EIP) 1559** im August 2021 erheblich vereinfacht (auch als London Upgrade bekannt). Im Wesentlichen zahlen Sie eine **Grundgebühr** für jede Gaseinheit, die nach erfolgreichem Abschluss der Transaktion verbrannt wird (sprich: es wird gelöscht und verschwindet). Zur Grundgebühr wird eine **Prioritätsgebühr**gerechnet, ebenfalls pro Gaseinheit, deren Höhe davon abhängt, wie schnell die Transaktion abgewickelt werden soll. 


Bei der Vielzahl der verfügbaren EVM-kompatiblen Netzwerken sind Gas oder ähnlich funktionierende Varianten im Wesentlichen die Standardmethode zur Berechnung der Transaktionskosten geworden. Die Gebühren werden im netzwerkeigenen Token bezahlt: Jede Transaktion auf Ethereum setzt ETH voraus; wer BSC nutzt, braucht BNB; Polygon wird mit MATIC bezahlt. Einige Netzwerke haben das EIP-1559-Modell von Ethereum vollständig übernommen, wie z. B. Polygon, während andere, z. B. Avalanche, Anpassungen für ihre C-Chain vorgenommen haben (die sowohl [die Grundgebühr als auch die Prioritätsgebühr verbrennt,](https://docs.avax.network/learn/platform-overview/transaction-fees/#c-chain-fees) anstatt nur die Grundgebühr). 


Wenn Sie einen genaueren Blick darauf lesen möchten, wie Gas auf Ethereum funktioniert, lesen Sie [hier](https://ethereum.org/en/developers/docs/gas/). 


 


Hier finden Sie einige **grundlegende Informationen für den Umgang mit Gas** **in MetaMask**:


#### **Die Gasgrenze (Einheiten des verwendeten Gases)**


Das *Gaslimit* bezeichnet **die Höchstgrenze an Gaseinheiten, die Sie für die** Transaktionsausführung oder die EVM-Abwicklung bezahlen möchten. Verschiedene Operationen erfordern unterschiedliche Mengen an Gaseinheiten. Eine normale Transaktion, die ETH oder einen Token sendet, kostet normalerweise **21.000** Gas, während eine ERC-20-Token-Genehmigung 45.000 erfordert. Viele Netzwerke, wie die EVM-kompatible Blockchain Harmony, verwenden das selbe Modell, bei dem Standardtransaktionen ebenfalls 21.000 Gas kosten. 



#### Muss ich das Gaslimit bearbeiten?


Nein! MetaMask legt Ihr Gaslimit automatisch fest, je nach der Transaktion, die Sie auszuführen versuchen. In den allermeisten Fällen ist dies ausreichend, um Ihre Transaktion abzuschließen. Wenn Sie es überprüfen oder bearbeiten möchten, stellen Sie sicher, dass Sie [die erweiterten Gassteuerungen](https://metamask.zendesk.com/hc/en-us/articles/360022895972) aktiviert haben (oder die experimentelle Enhanced Gas-Benutzeroberfläche verwenden), und klicken Sie auf dem Transaktionsbestätigungsbildschirm auf „Bearbeiten“.



#### **Die Grundgebühr**


Jeder Block im Ethereum-Netzwerk hat eine Grundgebühr, die von der Netznachfrage bestimmt wird: Die Grundgebühr basiert auf der Blockgröße des davor liegenden Blocks im Vergleich zu einer Zielblockgröße (wobei sich die Größe auf die Gesamtmenge an Gas bezieht, die für alle Transaktionen verwendet wird, die der Block umfasst). Wenn die Größe des vorherigen Blocks das Ziel überschreitet, erhöht sich die Grundgebühr für den nächsten Block um 12,5%, sodass Sie, der Benutzer (oder Ihr Wallet), mit absoluter Sicherheit über die Grundgebühr des kommenden Blocks bleiben. Ihre Gesamtgasgebühr muss diesen Preis als Minimum erfüllen, um für die Aufnahme in den Block berücksichtigt zu werden. 


#### **Die Prioritätsgebühr**


Die *Prioritätsgebühr*, auch als „Miner-Tip” bezeichnet, ist als Anreiz für die Priorisierung der Transaktion des Miners zu verstehen.


Ob dies tatsächlich an einen Miner geht, hängt natürlich von dem [Konsensmechanismus](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) ab, den sie verwenden: Das Ethereum-Mainnet wurde nach der Fusion im September 2022 zu einem Proof of Stake-Netzwerk, sodass die Prioritätsgebühr an Validatoren anstatt an Miner geht. 


#### **Die Höchstgebühr**


Die Höchstgebühr ist der Gesamtbetrag, den Sie für Ihre Transaktion bezahlen. Berechnungsmodell: **(****Grundgebühr + Prioritätsgebühr) x der Anzahl an verbrauchten Gaseinheiten.** MetaMask setzt diesen Betrag zunächst auf der Grundlage der Historie des vorherigen Blocks fest. Die Nutzer können diesen Betrag jedoch über benutzerdefinierte Einstellungen bearbeiten (siehe unten). Die Differenz zwischen der maximalen Gebühr pro Gas und (Grundgebühr + maximale Prioritätsgebühr pro Gas) wird dem Benutzer „erstattet“.


 


### **Ergänzende Konzepte**


#### **Gwei**


Gwei ist eine Einheit von Ether: Es ist die kleinste Einheit und steht für [Gigawei](https://ethgasstation.info/blog/gwei/) (oder 1.000.000.000). [Gwei](https://www.investopedia.com/terms/g/gwei-ethereum.asp) wird für Gasgebühren verwendet, d. h. für Zahlungen, die von den Nutzern als Kompensation für den zur Verarbeitung und Validierung von Transaktionen auf der Ethereum-Blockchain erforderlichen Rechenaufwand geleistet werden. 


Auch in anderen Netzen werden die Kosten in der Regel mit Gwei berechnet, z. B. bei Fantom, Harmony und Avalanche.


#### **Slippage**


Slippage bezeichnet die voraussichtliche prozentuale Differenz zwischen einem notierten und einem ausgeführten Kurs.


#### **Gasgebühr**


Die *Gasgebühr* bezeichnet die Transaktionsgebühr auf der Ethereum-Blockchain. Es ist der Preis, den die Nutzer zahlen, um ihre Transaktion zu validieren oder abzuschließen. 


#### **Grundgebühr**


Protokollerzeugung. Stellt den Mindestmultiplikator „Gasverbrauch” dar, der erforderlich ist, damit eine Transaktion in einen Block aufgenommen werden kann (d. h. damit eine Transaktion abgeschlossen wird). Dieser Teil der Transaktionsgebühr wird verbrannt.


 


### **Erweiterte Gassteuerungen**


Wenn Sie Ihre Gassteuerungen auf Herz und Nieren prüfen wollen (was z. B. beim Testen einer Dapp hilfreich sein kann), kann MetaMask das für Sie tun! Den ganzen Artikel finden Sie [hier](https://metamask.zendesk.com/hc/en-us/articles/360022895972).


 


### **FAQ**


[Warumzahle ich Gasgebühr für eine fehlgeschlagene Transaktion?](https://metamask.zendesk.com/hc/en-us/articles/360045439051)


[Können Sie meine Gasgebühren erstatten?](https://metamask.zendesk.com/hc/en-us/articles/360058370012)


[Wie beschleunige oder storniere ich eine ausstehende Transaktion?](https://metamask.zendesk.com/hc/en-us/articles/360015489251)


[Wie wird die Gasgebühr geschätzt?](https://metamask.zendesk.com/hc/en-us/articles/360059562111)


[Warum sind meine Gasgebühren so hoch?](https://metamask.zendesk.com/hc/en-us/articles/360058751211-Why-my-gas-fees-are-so-high-)


[Fehler: [ethjs-query] bei der Formatierung der Ausgaben von RPC (Fehler bei der Unterbewertung der Transaktion)](https://metamask.zendesk.com/hc/en-us/articles/4402538041869)


[So beheben Sie die Fehlermeldung „Unzureichende Deckung” oder die ausgegraute Bestätigungsschaltfläche](https://metamask.zendesk.com/hc/en-us/articles/360044703372)


 


 

