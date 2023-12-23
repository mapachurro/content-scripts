
#### Nota:


Gli account **importati** **non** verranno riaggiunti quando ripristinerai il tuo portafoglio utilizzando la frase di backup segreta. [Dovranno essere aggiungi manualmente](https://support.metamask.io/hc/en-us/articles/360015489331) nello stesso modo in cui li hai importati originariamente.



**NON condividere la tua frase di backup segreta con nessuno. Queste parole possono essere usate per rubare tutti i tuoi account. Non puoi modificare o cambiare la tua frase di backup segreta.**


 


Quando [ripristini un portafoglio](https://support.metamask.io/hc/en-us/articles/360015289612-How-to-restore-your-MetaMask-account-from-Seed-Phrase-Secret-Recovery-Phrase) utilizzando la tua frase di backup segreta, MetaMask riaggiunge automaticamente tutti gli account aggiuntivi che avevi [creato](https://support.metamask.io/hc/en-us/articles/360015289452) in precedenza, ma solo in determinate condizioni.


Se possibile, MetaMask cercherà di aggiungere i tuoi altri account aggiuntivi (supponendo che non siano stati [importati](https://support.metamask.io/hc/en-us/articles/360015289932)), verificando i tuoi account precedenti in ordine crescente (ad es. Account 2, poi Account 3, ecc.). **Gli account vengono riaggiunti automaticamente nel caso in cui abbiano un saldo di ETH diverso da zero.**. Tuttavia, questo processo termina quando MetaMask trova un account con 0 ETH, quindi il primo account con 0 ETH (e tutti quelli successivi) *non* verrà aggiunto.


Tieni presente che **questa procedura verifica la presenza dei saldi ETH solo sulla rete Ethereum principale**, quindi il tuo account non potrà essere nuovamente aggiunto automaticamente con gli altri token o con token presenti su altre reti.


**Per aggiungere nuovamente tutti gli account che non sono stati aggiunti automaticamente, dovrai "[creare](https://support.metamask.io/hc/en-us/articles/360015289452)" un account**. Ad esempio, se hai alcuni token nell'Account 4, ma l'Account 4 non viene aggiunto automaticamente perché quei token non sono ETH sulla rete principale, devi semplicemente aggiungere manualmente gli account usando i seguenti passaggi fino ad arrivare all'Account 4. Il tuo Account 4 *prima* del ripristino corrisponde all'Account 4 *dopo* il ripristino, indipendentemente dal nome che hai applicato in precedenza.


Se devi utilizzare il pulsante "crea" per aggiungere nuovamente gli account, non preoccuparti che l'indirizzo dell'account sia diverso. Gli indirizzi sono derivati in maniera crittografica e *deterministica* dalla tua chiave privata, il che significa che saranno sempre gli stessi. E visto che un account Ethereum, una volta creato, è permanente, puoi semplicemente riprendere da dove hai lasciato. 


Per ripristinare gli altri account nell'ordine in cui sono stati creati originariamente, segui questa procedura:




Estensione App mobile


1. Fare clic sulla favicon nell'angolo in alto a destra del menu a discesa di MetaMask
2. Fai clic su "Crea Account" per ripristinare i tuoi account MetaMask nell'ordine in cui sono stati creati
3. Se era già stato assegnato un nome agli account, puoi rinominarli nel passaggio seguente, prima di fare clic su "**Crea**"


![How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase.gif](https://support.metamask.io/hc/article_attachments/9026739981083/How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase.gif)




1. Tocca l'icona dell'hamburger in alto a sinistra dello schermo per visualizzare il menu. Da qui, tocca la freccia a discesa accanto al nome del tuo account:
2. Tocca "Create New Account":


![How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase_Mobile.gif](https://support.metamask.io/hc/article_attachments/9027058464027/How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase_Mobile.gif)




Se ancora non vedi gli indirizzi che cercavi, probabilmente sono stati creati con una frase di backup segreta diversa oppure avevi un account importato che devi ancora reimportare utilizzando chiavi private o JSON. Consulta [questo articolo su come importare un account](https://support.metamask.io/hc/en-us/articles/360015489331-Importing-an-Account). 

