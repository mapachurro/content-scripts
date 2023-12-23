### Ermittlung des Gaspreises


Im Ethereum-Mainnet können Sie das [Gas-Tool von Etherscan](https://etherscan.io/gastracker) zur Schätzung des heutigen Gaspreises nutzen.  Bitte beachten Sie, dass der Gaspreis schwankt; erkundigen Sie sich immer an der entsprechenden Stelle nach den aktuellen Gaspreisen.


Das Ethereum-Netzwerk benötigt Gas, um Transaktionen durchzuführen. Wenn Sie einen Token senden, einen Vertrag abschließen, ETH übermitteln oder eine andere Aktion auf der Blockchain ausführen, müssen Sie für die Rechenleistung bezahlen. Diese Zahlung wird in Gas berechnet. Gas wird immer in ETH abgerechnet.


Sie zahlen für die Rechenleistung, unabhängig davon, ob Ihre Transaktion erfolgreich ist oder nicht. Denn auch wenn sie scheitert, müssen die Miner oder Validierer Ihre Transaktion abschließen und ausführen und das kostet Rechenleistung. Sie müssen diese Rechenleistung bezahlen, so wie Sie auch für eine erfolgreiche Transaktion bezahlen würden.


 


### Erreichen des Gasgrenzwerts


Sie kennen also die Kosten pro Gaseinheit, aber wie viele Gaseinheiten müssen Sie ausgeben? Handelt es sich um eine einfache Transaktion, z. B. um das Senden von ETH oder eines ERC-721-Tokens an eine andere Adresse, sollten Sie 21.000 Gaseinheiten verbrauchen. Für komplexere Aktionen ist ein Block-Explorer wie [etherscan.io](https://etherscan.io/) ein gutes Instrument. Wechseln Sie zum Vertrag, den Sie bearbeiten möchten und beginnen Sie mit der Prüfung der Transaktionen, die mit diesem Vertrag durchgeführt wurden. So können Sie sich ein besseres Bild davon machen, wie viel Gas andere Nutzer tatsächlich verbrauchen.



#### Gasrechner


Es gibt ein paar Tools da draußen, mit denen Sie schätzen können, wie viel Gas Sie in Fiatwährung kosten wird, bevor Sie eine Transaktion einreichen. Ein Beispiel ist der [Cryptoneur-Gasgebührenrechner](https://www.cryptoneur.xyz/gas-fees-calculator), mit dem Sie die Details Ihrer Transaktion eingeben und die geschätzten Gaskosten in Ihrer lokalen Währung und speziell für die aktuelle Nachfrage in diesem Netzwerk produzieren können (Sie können aus den meisten großen EVM-kompatiblen Netzwerken wählen).



### 
Gesamtstruktur der Gasgebühren


Ab [EIP-1559](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1559.md) wird die Gesamtgebühr, die ein Auftraggeber für eine Transaktion zahlt, wie folgt berechnet: **((Grundgebühr + Prioritätsgebühr) x verbrauchte Gaseinheiten).** 


Weiterführende Informationen finden Sie [hier](https://support.metamask.io/hc/en-us/articles/4404600179227).


 


**Bitte beachten Sie, dass dies keine Gebühr ist, die an MetaMask entrichtet wird, daher können wir diese nicht erstatten.** Diese Gebühr wird an die Miner oder Validierer abgeführt, die die Transaktion abschließen, sie zu einem Block validieren und die Blockchain sichern.

