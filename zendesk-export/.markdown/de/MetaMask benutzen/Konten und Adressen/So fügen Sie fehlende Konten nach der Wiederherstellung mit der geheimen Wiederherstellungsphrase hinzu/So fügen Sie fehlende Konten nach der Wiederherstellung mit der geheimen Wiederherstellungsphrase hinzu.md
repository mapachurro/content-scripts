
#### Hinweis:


**Importierte** Konten werden **nicht** erneut hinzugefügt, wenn Sie Ihr Wallet mit Ihrer geheimen Wiederherstellungsphrase wiederherstellen. [Sie müssen manuell](https://support.metamask.io/hc/en-us/articles/360015489331) auf die gleiche Weise hinzugefügt werden, wie Sie sie ursprünglich importiert haben.



**Geben Sie Ihre Wiederherstellungsphrase NICHT an andere weiter! Diese Wörter können zum Diebstahl Ihrer sämtlichen Konten benutzt werden. Sie können Ihre geheime Wiederherstellungsphrase weder bearbeiten noch ändern.**


 


Wenn Sie [ein Wallet](https://support.metamask.io/hc/en-us/articles/360015289612-How-to-restore-your-MetaMask-account-from-Seed-Phrase-Secret-Recovery-Phrase) mit Ihrer geheimen Wiederherstellungsphrase wiederherstellen, fügt MetaMask alle zusätzlichen Konten automatisch erneut hinzu, die Sie zuvor [erstellt](https://support.metamask.io/hc/en-us/articles/360015289452) hatten - jedoch nur unter bestimmten Bedingungen.


MetaMask versucht nach Möglichkeit, Ihre zusätzlichen Konten hinzuzufügen (vorausgesetzt, sie wurden nicht [importiert](https://support.metamask.io/hc/en-us/articles/360015289932)), indem es Ihre bisherigen Konten in aufsteigender Reihenfolge abfragt (d. h. Konto 2, dann Konto 3 usw.). **Konten werden automatisch neu hinzugefügt, wenn sie einen ETH-Saldo ungleich Null haben**. Dieser Prozess endet jedoch, wenn MetaMask auf ein Konto mit 0 ETH stößt - so dass das erste Konto mit 0 ETH (und ein darüber hinausgehendes Konto) *nicht* hinzugefügt wird.


Beachten Sie, dass **bei diesem Vorgang nur das Guthaben von ETH im Ethereum-Mainnet überprüft** wird. Sollten Sie andere Token oder Token in anderen Netzwerken besitzen oder halten, heißt das nicht, dass Ihr Konto automatisch erneut hinzugefügt wird.


**Sie müssen ein Konto „[anlegen](https://support.metamask.io/hc/en-us/articles/360015289452)”, wenn Sie alle, die nicht automatisch aufgenommen wurden, hinzufügen möchten**. Sollten Sie beispielsweise einige Token auf Konto 4 haben, dieses aber nicht automatisch hinzugefügt wurde, weil diese Token nicht zum ETH im Mainnet gehören, müssen Sie nur manuell Konten hinzufügen (anhand der unten aufgeführten Schritte), bis Sie zu Konto 4 gelangen. Ihr Konto 4 *vor* der Wiederherstellung entspricht, unabhängig von der vorherigen Kontobezeichnung, Konto 4 *nach* der Wiederherstellung.


Wenn Sie die Schaltfläche „Erstellen“ zum erneuten Hinzufügen von Konten verwenden müssen, machen Sie sich keine Sorgen, dass die Kontenadresse abweicht. Die Adressen werden kryptographisch *deterministisch* von Ihrem privaten Schlüssel abgeleitet, was bedeutet, dass sie immer gleich sind. Und da ein Ethereum Konto, sobald es erstellt wurde, dauerhaft existiert, können Sie einfach dort weitermachen, wo Sie aufgehört haben.


Bitte befolgen Sie die nachstehenden Schritte, um Ihre anderen Konten in der ursprünglichen Reihenfolge wiederherzustellen:




Erweiterung Mobilgerät


1. Klicken Sie auf das Favicon in der oberen rechten Ecke des MetaMask-Dropdown-Menüs
2. Möchten Sie Ihre MetaMask-Konten in der ursprünglichen Reihenfolge wiederherstellen, klicken Sie auf „Konto erstellen”.
3. Sofern die Konten bereits benannt wurden, können Sie sie im folgenden Schritt erneut benennen, bevor Sie auf „**Erstellen**” klicken.


![How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase.gif](https://support.metamask.io/hc/article_attachments/9026739981083/How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase.gif)




1. Das Menü wird durch Tippen auf das Hamburger-Symbol oben links auf dem Bildschirm aufgerufen. Tippen Sie auf den Dropdown-Pfeil neben Ihrem Kontonamen:
2. Tippen Sie auf „Neues Konto erstellen”:


![How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase_Mobile.gif](https://support.metamask.io/hc/article_attachments/9027058464027/How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase_Mobile.gif)




Können Sie die gesuchten Adressen immer noch nicht sehen, wurden sie wahrscheinlich mit einer anderen geheimen Wiederherstellungsphrase erstellt, oder Sie hatten ein importiertes Konto, das Sie noch mit Private Keys oder JSON erneut importieren müssen. Wie Sie ein [Konto importieren, entnehmen Sie bitte diesem Artikel](https://support.metamask.io/hc/en-us/articles/360015489331-Importing-an-Account).

