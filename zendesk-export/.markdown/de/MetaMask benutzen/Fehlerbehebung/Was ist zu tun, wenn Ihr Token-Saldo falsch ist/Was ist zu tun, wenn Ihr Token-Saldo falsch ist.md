
#### Token erscheinen überhaupt nicht?


Lesen Sie unseren Leitfaden zur Behebung dieses Problems [hier](https://support.metamask.io/hc/en-us/articles/360059232852).



Überprüfen Sie zunächst die Token-Salden, die im Block-Explorer angezeigt werden, und vergleichen Sie mit MetaMask. Sie tun dies, indem Sie Ihre Wallet-Adresse kopieren und sie in den Block Explorer einfügen, der dem Netzwerk entspricht, auf dem Sie sich befinden — Etherscan für Ethereum Mainnet, Arbiscan für Arbitrum usw. Für detaillierte Anweisungen siehe [hier](https://support.metamask.io/hc/en-us/articles/360057536611).




Erweiterung Mobilgerät


Wenn Ihre MetaMask-Erweiterung den falschen oder ungenauen Saldo für ETH oder andere Token anzeigt, versuchen Sie die folgenden Schritte nacheinander, bis Sie Ihren Saldo korrekt sehen.


**Bevor Sie fortfahren, stellen Sie sicher, dass Sie Ihre [geheime Wiederherstellungsphrase](https://support.metamask.io/hc/en-us/articles/4404722782107-User-Guide-Secret-Recovery-Phrase-password-and-private-keys) an einem sicheren Ort gesichert haben.**


1. Überprüfen Sie, ob Ihre Internetverbindung stark und stabil ist. Wenn nicht, kann MetaMask möglicherweise nicht die richtigen Salden laden.
2. Schließen Sie Ihren Browser, in dem Sie die MetaMask-Erweiterung installiert haben, und öffnen Sie ihn erneut.
3. Versuchen Sie, alle von Ihnen installierten Werbeblocker auszuschalten, oder, wenn Sie ein VPN verwenden, versuchen Sie, MetaMask mit deaktiviertem Gerät zu verwenden.
4. Wechseln Sie zu einem anderen Netzwerk und wieder zurück. Klicken Sie dazu oben in der App auf Ihr aktuelles Netzwerk. Wählen Sie ein anderes Netzwerk aus und wechseln Sie dann wieder zu Ihrem ursprünglichen Netzwerk.
5. Stellen Sie sicher, dass kein Problem mit [den Browserberechtigungen](https://support.metamask.io/hc/en-us/articles/360038139452-MetaMask-states-Balance-may-be-outdated-displays-in-orange-or-ETH-not-added-to-balance) besteht.
6. Versuchen Sie eine andere RPC URL, wenn für das von Ihnen verwendete Netzwerk mehr als eine verfügbar ist. Sie können die RPC bearbeiten, indem Sie zu Einstellungen > Netzwerk gehen und dann auf das betreffende Netzwerk klicken. Weitere Informationen finden Sie in unserem [Artikel zum Hinzufügen von Netzwerken](https://support.metamask.io/hc/en-us/articles/360043227612).
7. Installieren Sie MetaMask mit einem anderen unterstützten Browser (Firefox, Chrome, Brave, Edge) von unserer offiziellen Website [https://metamask.io](https://metamask.io/) , und versuchen Sie dann, Ihre Brieftasche mit der 12-Wort-Secret Recovery Phrase wiederherzustellen, falls das Problem nur in dem Browser vorhanden ist, den Sie derzeit verwenden.




Nachdem Sie auf Etherscan überprüft haben, dass die Anzahl der Token, die in MetaMask Mobile angezeigt werden, falsch ist, gehen Sie wie folgt vor:


1. Stellen Sie sicher, dass Ihre Internetverbindung stark und stabil ist. Wenn nicht, sind Token Werte möglicherweise nicht auf dem neuesten Stand.
2. Wechseln Sie zu einem anderen Netzwerk und wechseln Sie dann wieder zurück.
3. Ändern Sie die RPC des Netzwerks, in dem Sie sich befinden, nach Möglichkeit in eine Alternative. Weitere Informationen finden Sie in unserem [Artikel zum Hinzufügen von Netzwerken](https://support.metamask.io/hc/en-us/articles/360043227612).
4. Verstecken Sie das Token nach den Anweisungen [hier](https://support.metamask.io/hc/en-us/articles/360015489031-How-to-add-unlisted-tokens-custom-tokens-in-MetaMask#h_01FWH499MRDT5QC4R3KNPQNRWB), und fügen Sie das Token nach den Anweisungen [hier](https://support.metamask.io/hc/en-us/articles/360015489031-How-to-add-unlisted-tokens-custom-tokens-in-MetaMask) erneut hinzu.


**Wenn es sich bei dem betreffenden Token um einen netzwerkeigenen Token für ein anderes Netzwerk als Ethereum** (BNB, AVAX, MATIC usw.) handelt, versuchen Sie, [das Netzwerk zu löschen](https://support.metamask.io/hc/en-us/articles/4502810252059-How-to-remove-networks) und es dann [erneut hinzuzufügen](https://support.metamask.io/hc/en-us/articles/360043227612-How-to-add-a-custom-network-RPC).   
  
**Wenn es sich bei dem betreffenden Token um ETH handelt, stellen Sie sicher, dass Ihre [geheime Wiederherstellungsphrase](https://support.metamask.io/hc/en-us/articles/4404722782107-User-Guide-Secret-Recovery-Phrase-password-and-private-keys) an einem sicheren Ort gesichert wird**, und installieren Sie die App neu.

Wenn Sie nach dem Ausführen dieser Schritte immer noch Probleme haben, kontaktieren Sie uns bitte über die Schaltfläche "Eine Unterhaltung starten" auf unserer [Support](https://support.metamask.io/hc/en-us)-Seite.



#### Hat der Token integrierte Mechanismen, die Angebot oder Wert beeinflussen?


Ethereum- und EVM-kompatible Ketten beherbergen eine enorme Vielfalt an Token mit verschiedenen Dienstprogrammen. Einige Token sind so konzipiert, dass sie Angebot oder Wert dynamisch gemäß verschiedenen Bedingungen ändern:


* [Rebase Token](https://support.metamask.io/hc/en-us/articles/4405497827355-User-Guide-Tokens#:~:text=Elastic%20supply%20/%20Rebase%20/%20Algorithmic%20tokens), wo das Tokenangebot angepasst wird
* Token mit „Steuern“ für Transaktionen verschiedener Art (z. B. einfache Übertragung, Swap, Verkauf usw.). Diese werden manchmal als „Gebühr auf Übertragungen“ Token bezeichnet.


Bevor Sie zu dem Schluss kommen, dass Ihr Guthaben falsch ist, überprüfen Sie, ob ähnliche Bedingungen für Ihren Token gelten. Sie können diese Informationen normalerweise finden, indem Sie das Whitepaper oder die Dokumentation des Projekts überprüfen.


