Wenn Sie eine Transaktion auf Ethereum oder einem kompatiblen Netzwerk einreichen, ist ein Teil des von Ihnen bezahlten Gases ein Gebot an das Netzwerk, Ihre Transaktion früher zu verarbeiten - dieses Element wird als die Prioritätsgebühr bezeichnet. Obwohl MetaMask Sie bei der Berechnung eines Gesamtgaspreises unterstützt, bei dem es wahrscheinlich ist, dass Ihre Transaktion abgeholt wird, können Sie am Ende lange warten, wenn Sie einen niedrigen Gaspreis einreichen. Wenn Sie wissen möchten, welche Gaspreise zum Abschluss einer Transaktion in einem angemessenen Zeitraum, ziehen Sie bitte Quellen wie den [Gas-Tracker von Etherscan](https://etherscan.io/gastracker)oder einen ähnlichen Tracker für das von Ihnen genutzte Netz zurate.


Ferner kann es vorkommen, dass etwas nicht klappt und eine Transaktion einfach stecken bleibt oder sehr lange aussteht.


Wie auch immer Sie in diese Lage gekommen sind, es gibt mehrere Möglichkeiten, das Problem zu beheben.


 


### Bevor Sie weitere Maßnahmen ergreifen, sollten Sie Ihren Browser vollständig verlassen und schließen, ihn erneut öffnen und MetaMask entsperren (auf Mobilgeräten schließen Sie einfach die App und öffnen Sie sie erneut). Bleibt das Problem bestehen, gehen Sie wie folgt vor:


 


**Beschleunigen einer Transaktion**
-----------------------------------


![MetaMask beschleunigt die Transaktion](https://support.metamask.io/hc/article_attachments/12927043481371)


Probiere Sie Folgendes aus:


* Warten Sie, bis das Netzwerk gewillt ist, Transaktionen zu diesem Preis zu verarbeiten.
* Falls Sie das nicht schon getan haben, klicken Sie auf die Schaltfläche **Beschleunigen**. So können Sie dieselbe Transaktion erneut einreichen, allerdings mit einer höheren Gasgebühr, die eine schnellere Transaktion ermöglichen sollte. Da bei diesem Prozess dieselbe Nonce wie das Original wiederverwendet wird, müssen Sie nicht zweimal für Gas bezahlen.


Denken Sie daran, dass **die Beschleunigung der Transaktion den Betrag erhöht, den Sie für die Transaktion ausgeben**.


 


**Transaktionsabbruch – Methode 1: Stornierung in der App**
-----------------------------------------------------------


Falls Sie dies noch nicht getan haben, wählen Sie zum Stornieren der Transaktion einfach**Abbrechen**, wie im obigen Screenshot gezeigt. Beachten Sie bitte, **dass eine Stornierung nur dann *versucht werden kann*, wenn die Transaktion im Netzwerk noch immer ausstehend ist.** Bereits bestätigte Transaktionen können nicht mehr storniert werden.


 


**Transaktionsabbruch – Methode 2: Benutzerdefinierte Nonce**
-------------------------------------------------------------


Dieser Prozess beinhaltet das Senden einer neuen Transaktion mit derselben Nonce (einer Identifikationsnummer für jede Transaktion, die von der Phrase „Nummer nur einmal verwendet“ abgeleitet wird). Die Transaktion muss nicht unbedingt einen Wert haben – Sie können z. B. 0 ETH senden. Worauf es ankommt ist, dass Sie für die Priorisierung genügend Gas an das Netzwerk zahlen.


Wenn Sie diese Methode verwenden, **müssen Sie von der ältesten ausstehenden Transaktion in der Warteschlange rückwärts arbeiten, die Sie abbrechen möchten**. Beispiel: Sie können eine Transaktion mit einer Nonce von 10 erst nach dem Storno von Nonce 9 stornieren.


*Die folgenden Screenshots wurden zu verschiedenen Zeiten aufgenommen, sodass die darin angegebenen Gasgebühren auch von Schritt zu Schritt variieren können. Lassen Sie sich davon nicht abschrecken! Wenn Sie dies selbst tun, aktualisiert sich MetaMask automatisch in Echtzeit, um die Marktpreise anzuzeigen.*




Erweiterung Mobilgerät


1. Aktivieren Sie in den erweiterten Einstellungen **Transaktionsnonce einstellen** und **Erweiterte Gassteuerungen.** Dadurch können Sie die von Ihnen bezahlte Gasgebühr anpassen und sicherstellen, dass Ihr Storno vor der ursprünglichen Transaktion, die Sie stornieren möchten, bearbeitet wird.



#### Hinweis:


Die MetaMask-Erweiterung verfügt derzeit über eine experimentelle Funktion namens [Enhanced Gas Fee UI](https://metamask.io/1559/) (nicht zu verwechseln mit [erweiterten Gaskontrollen](https://support.metamask.io/hc/en-us/articles/360022895972)). Diese Schritte können auch ohne diese Funktion ausgeführt werden, aber sie sehen dann anders aus. Die folgenden Schritte verwenden keine Enhanced Gas UI. Denken Sie daran:



	* Wenn Sie die Enhanced Gas UI eingeschaltet haben, müssen Sie immer noch die Option „Customize anpassen“ aktiviert haben.
	* Wenn Sie die Enhanced Gas UI nicht eingeschaltet haben, müssen Sie sowohl die „Erweiterte Gaskontrollen“ als auch die „Transaktionsnonce anpassen“ aktiviert haben.

![MetaMask erweiterte Einstellungen](https://support.metamask.io/hc/article_attachments/12927064113947)
2. **Eine neue Transaktion senden**. Die neue Transaktion senden Sie an sich **SELBST**, also an Ihre öffentliche MetaMask-Adresse. **Füllen Sie „Benutzerdefinierte Nonce” mit der gleichen Nonce aus, die auch für die noch ausstehende Transaktion gilt:**


![Metamask_custom_transaction_nonce_Extension.png](https://support.metamask.io/hc/article_attachments/12927064259483)
3. Klicken Sie nun neben „Gasgebühr” auf „Bearbeiten” (ist die experimentelle Funktion [Enhanced Gas UI](https://support.metamask.io/hc/en-us/articles/360022895972-Using-advanced-gas-controls#:~:text=%C2%A0-,Enhanced%20Gas%20UI,-Since%20the%20introduction) aktiviert, wird dies als „Markt” angezeigt). Danach haben Sie die folgenden Möglichkeiten:


![MetaMask Erweiterung der erweiterten Gassteuerung](https://support.metamask.io/hc/article_attachments/12927065407515)


Damit Ihre Stornierungsanfrage priorisiert wird und vor dem Original bearbeitet wird, **müssen Sie eine höhere Gasgebühr bezahlen**. Folgen Sie diesen Anweisungen:


	* Stelle Sie Ihr **Gaslimit** *gleich oder etwas höher* als Ihre ursprüngliche Transaktion ein.
	* Stellen Sie Ihre **maximale Prioritätsgebühr**um *mindestens 10 % höher* (in Gwei) als die Gasgebühr der ursprünglichen (ausstehenden) Transaktion ein (wenn diese Transaktion eine Gasgebühr von 30 Gwei hatte, setzen Sie die maximale Prioritätsgebühr in der Ersatz-/Stornierungstransaktion auf 33-35 Gwei).
	* Vergewissern Sie sich, dass Ihre maximale Gebühr mindestens 30 % höher ist als die maximale Gebühr der Transaktion, die Sie ersetzen. Beispiel: wenn Ihre vorherige Gebühr. 150 Gwei betrug, wählen Sie dieses Mal einen Betrag im Bereich von 200 Gwei.Ziehen Sie den Gas-Tracker, wie [Etherscan](https://etherscan.io/gastracker) oder [ETH Gas Station](https://ethgasstation.info/) bezüglich einer Anleitung für empfohlene Höchstgebühren zurate.




1. **Aktivieren Sie unter Einstellungen > Erweitert „Transaktionsnonce anpassen“.**
2. **Eine neue Transaktion senden.** Die neue Transaktion senden Sie an sich SELBST, also an Ihre öffentliche MetaMask-Adresse. **Füllen Sie „Benutzerdefinierte Nonce” mit der gleichen Nonce aus, die auch für die noch ausstehende Transaktion gilt**.


Um die benutzerdefinierte Nonce Einstellung in der App zu finden, rufen Sie den Transaktionsbestätigungsbildschirm auf, der angezeigt wird, nachdem Sie die Tokenmenge und den Empfänger eingegeben haben. Klicken Sie auf „Bearbeiten“, um es zu ändern:


![MetaMask benutzerdefinierte Transaktionsnonce Mobile](https://support.metamask.io/hc/article_attachments/12927068442907)
3. Jetzt müssen Sie sicherstellen, dass Ihre Gaseinstellungen so konfiguriert sind, dass Ihre Ersatztransaktion verarbeitet wird. Tippen Sie auf dem Transaktionsbestätigungsbildschirm auf den hervorgehobenen Gaswert:


![MetaMask erweiterte Gassteuerung mobil](https://support.metamask.io/hc/article_attachments/12927041593755)


Greifen Sie nun über das angezeigte Menü auf „Erweiterte Optionen“ zu.
4. Von hier aus können Sie Gas genau anpassen, um sicherzustellen, dass Ihre Transaktion abgeholt wird. Sie sehen sich jetzt einen Bildschirm an, der wie folgt aussieht:


![MetaMask erweiterte Gassteuerung mobil](https://support.metamask.io/hc/article_attachments/12927063201691)


Passen Sie von hier aus die Gaseinstellungen an. Befolgen Sie diese Anweisungen, um sicherzustellen, dass Ihre Transaktion abgeholt wird:


	* Stelle Sie Ihr **Gaslimit** *gleich oder etwas höher* als Ihre ursprüngliche Transaktion ein.
	* Stellen Sie Ihre **maximale Prioritätsgebühr**um *mindestens 10 % höher* (in Gwei) als die Gasgebühr der ursprünglichen (ausstehenden) Transaktion ein (wenn diese Transaktion eine Gasgebühr von 30 Gwei hatte, setzen Sie die maximale Prioritätsgebühr in der Ersatz-/Stornierungstransaktion auf 33-35 Gwei).
	* Vergewissern Sie sich, dass Ihre maximale **Gebühr** *mindestens 30 % höher* ist als die maximale Gebühr der Transaktion, die Sie ersetzen. Beispiel: wenn Ihre vorherige Gebühr. 150 Gwei betrug, wählen Sie dieses Mal einen Betrag im Bereich von 200 Gwei.Ziehen Sie den Gas-Tracker, wie [Etherscan](https://etherscan.io/gastracker) oder [ETH Gas Station](https://ethgasstation.info/) bezüglich einer Anleitung für empfohlene Höchstgebühren zurate.



