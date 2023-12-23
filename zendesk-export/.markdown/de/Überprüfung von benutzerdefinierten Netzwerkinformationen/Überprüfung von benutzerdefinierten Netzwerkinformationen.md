Wenn eine Website verlangt, dass Sie ein benutzerdefiniertes Netzwerk zu MetaMask hinzufügen, erhalten Sie die Informationen, die MetaMask für die Datenkommunikation mit dem Netzwerk verwenden wird. MetaMask führt einige grundlegende Datenüberprüfungen durch und warnt Sie, wenn etwas fehlerhaft oder ungewöhnlich erscheint. MetaMask sorgt dafür, dass ein und dasselbe Netzwerk nur einmal hinzugefügt wird. MetaMask überprüft jedoch keine benutzerdefinierten Netzwerke, und selbst wenn die Validierung von MetaMask auscheckt, könnte das Netzwerk bösartig sein oder von der Website, die es angefordert hat, falsch dargestellt werden.


**Weitere Informationen und eine Einführung in benutzerdefinierte Netzwerke finden Sie in unserem Benutzerhandbuch [hier](https://support.metamask.io/hc/en-us/articles/4404424659995).**


Sie sind für die Prüfung der Ethereum-Adressen, mit denen Sie Transaktionen abwickeln, verantwortlich. Das gilt ebenso für alle benutzerdefinierten Netzwerke, die Sie zu MetaMask hinzufügen. In diesem Artikel erfahren Sie, wie Sie das umsetzen können.


Wenn eine Website eine Anfrage zum Hinzufügen eines benutzerdefinierten Netzwerks stellt, zeigt MetaMask die folgende Bestätigung an: 


![custom-network.png](https://support.metamask.io/hc/article_attachments/360087917091/custom-network.png)


 


Diese Bestätigung zeigt **die von der Website abgegebenen Netzwerkdaten**. *Es gibt keine Garantie für die Richtigkeit dieser Daten*. Folglich sollten Sie den Daten nur so sehr vertrauen, wie Sie auch der Website vertrauen.


Wenn Sie in der Bestätigung auf „Alle Details anzeigen” klicken, können Sie alle von der Website angegebenen Netzwerkdaten sehen, darunter auch die Folgenden:


* **Netzwerkname**: Der Name, den MetaMask mit dem Netz verknüpft.
* **Netzwerk-URL:** Die URL, die MetaMask für den Netzwerkzugriff verwenden wird.
* **Chain ID:** Die Chain-ID, die MetaMask für die Transaktionssignatur im Netzwerk verwenden wird.
* **Währungssymbol:** Das Währungssymbol, das MetaMask für die native Netzwerkwährung verwenden wird.
	+ Für das Ethereum-Mainnet lautet das Währungssymbol beispielsweise ETH und für die Gnosis Chain xDAI (das nach der Fusion beibehalten wurde).
* **Block Explorer URL (optional):** Die URL, an die MetaMask Sie zur Konten- und Transaktionsprüfung usw. weiterleitet. Das Gegenstück zu [etherscan.io](https://etherscan.io), jedoch für das betreffende benutzerdefinierte Netzwerk.


Sollten Sie aus irgendeinem Grund Zweifel an der Richtigkeit der Netzwerkdaten haben, empfehlen wir Ihnen für die Überprüfung Folgendes:


* Gehen Sie zu [Chainlist](https://chainlist.wtf/) und suchen nach der angegebenen Chain-ID und/oder dem Netzwerknamen. Wenn MetaMask meldet, dass einige Daten nicht zutreffen, sollten Sie das Problem auf Chainlist feststellen können. Falls das benutzerdefinierte Netzwerk überhaupt nicht auf Chainlist aufgeführt ist, ist es entweder extrem neu oder möglicherweise von zweifelhafter Qualität.
* Googeln Sie den Netzwerknamen und versuchen Sie, die folgenden Fragen zu beantworten. Je öfter die Antwort „Ja” lautet, desto eher handelt es sich um ein seriöses Netzwerk. Beachten Sie, dass es viele Betrugsversuche und gefälschte Social-Media-Kanäle gibt, insbesondere auf Telegram.
+ Verfügt das Netzwerk über eine Website? Wenn ja, macht sie einen seriösen Eindruck? Werden die Netzwerkdetails angeführt?
+ Unterhält das Netzwerk ein offizielles Twitter-Konto oder ein anderes Konto auf sozialen Medien? Hat es viele Follower? Macht es einen glaubwürdigen Eindruck? Was sagen die Leute über das Netzwerk?
+ Können Sie eine der Personen bestimmen, die das Netzwerk betreiben? Ist es in den sozialen Medien sichtbar? Hat es viele Follower?
+ Gibt es Presseartikel über das Netzwerk?


Bei den meisten Netzwerken sollte es ziemlich offensichtlich sein, ob sie seriös sind oder nicht und ob die Website genaue Daten anzeigt oder nicht. Wenn Sie trotz dieser Schritte noch unsicher sind, sollten Sie die Anfrage zum Hinzufügen des Netzwerks ablehnen, weitere Nachforschungen anstellen und es vielleicht später noch einmal versuchen.

