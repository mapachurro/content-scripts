
#### Ti stai avvicinando per la prima volta alle criptovalute e al web3?


Vai su [MetaMask Learn](https://learn.metamask.io/) per accedere a un'esperienza di apprendimento intuitiva, concepita appositamente per coloro che si avvicinano per la prima volta al web3. È completamente gratuito, disponibile in più lingue e offre strumenti utili come le simulazioni per aiutarti a orientarti con MetaMask.



### Contenuti di questo articolo:


* [Che cosa distingue la sicurezza di MetaMask da quella degli account web tradizionali](#h_01FYVAXCSH95CQ08Q0P2VJA5HV)
* [Che cos'è la frase di recupero segreta?](#h_01FYVAXJQT914HCHEYFPNMEJEA)
* [Frase di recupero segreta: cosa fare e cosa evitare](#h_01FYVAXSE5C9E4YBCSWT2F2RBQ)
* [Domande frequenti sulla frase di recupero segreta](#h_01FYVAXZYWJENFWG9K9CJTQFK7)
* [MetaMask e le password](#h_01FYVAY5K22PX6926537V8B4SX)
* [Domande frequenti sulle chiavi private](#h_01FYVAYH3ZZ8VW8BPDDADWRC8E)




**MetaMask: un nuovo modello** **di sicurezza dell'account**
-------------------------------------------------------------


A confronto delle tradizionali tecnologie online, [la tecnologia blockchain pubblica](https://metamask.zendesk.com/hc/en-us/articles/360015489611) si avvale di strumenti molto diversi per garantire la sicurezza dei dati degli utenti. Nella maggior parte dei casi, siamo abituati a creare un account su un'app o un servizio web e a contattare l'assistenza per reimpostare la password o il nome utente. Siamo abituati al fatto che l'app conservi i nostri dati, presumibilmente su un computer di proprietà della nostra azienda.


MetaMask non funziona esattamente così. MetaMask si avvale di tre tipi di **segreti** diversi che, in modi diversi, servono a garantire la privacy e la sicurezza del tuo portafoglio e dei tuoi account: la frase di recupero segreta, la password e le chiavi private. In questo articolo descriveremo nel dettaglio tutti i segreti.


 


**Introduzione alle frasi di recupero segrete**
-----------------------------------------------


Una delle tecnologie chiave su cui si basano MetaMask e la maggior parte degli strumenti relativi agli account utente nell'ambito delle criptovalute è la *frase seme*o, come viene chiamata in MetaMask, la *frase di recupero segreta* (FRS). 


#### **Tutti i tuoi account sono derivati matematicamente dalla frase di recupero segreta. Puoi immaginare la FRS come un portachiavi in grado di contenere tutte le chiavi private che vuoi, ognuna delle quali controlla un account.**


Ora, la spiegazione più accurata dal punto di vista tecnico è la seguente: le frasi seme come le conosciamo oggi erano state programmate per essere utilizzate in Bitcoin, in base a uno standard chiamato Bitcoin Improvement Proposal 39 o [BIP-39](https://en.bitcoin.it/wiki/BIP_0039). In soldoni, una serie di parole selezionate con un alto livello di casualità da uno specifico [elenco di parole](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt). In MetaMask e in molte altre tecnologie compatibili con Ethereum, una frase seme contiene 12 parole. Alcuni semi meno recenti generati dal browser Brave e dal alcuni portafogli hardware, contengono frasi di 24 parole.


Ciascuna di queste parole corrisponde a una serie numerica e quando sono posizionate in **un ordine specifico** possono essere ricordate molto più facilmente rispetto a un numero lunghissimo. Quel numero viene quindi utilizzato in modo *deterministico* per generare i tuoi account e spesso potresti sentire anche l'espressone portafogli deterministici. In informatica, il termine "deterministico" descrive un processo, generalmente un algoritmo, che restituisce *sempre*lo stesso risultato. In altre parole, **la tua frase di recupero segreta genererà sempre lo stesso gruppo di account derivati da essa**. 


 


### A questo punto, è necessario aggiungere alcune note importanti:


* La **frase di recupero segreta è il segreto che controlla il portafoglio**. Se qualcuno è in possesso di questo segreto avrà accesso completo al portafoglio. **MetaMask non conserva la tua FRS:** **[sei tu a custodire il tuo portafoglio.](https://metamask.zendesk.com/hc/en-us/articles/360059952212)** I rappresentanti di MetaMask non ti chiederanno **mai** la frase di recupero segreta, neanche nel caso in cui tu ti sia rivolto all'assistenza clienti. Se qualcuno te la chiede, probabilmente cercano di truffarti o di rubarti il tuo patrimonio.
* La tua FRS viene **utilizzata in locale per generare le chiavi private**, una per ciascun account/indirizzo. Gli account sono memorizzati nella blockchain e le chiavi private servono per sbloccarli.
* **Se disinstalli l'app** o l'estensione, perderai la copia locale dei dati (con l'unica eccezione del [vault](https://metamask.zendesk.com/hc/en-us/articles/360018766351)), tuttavia tutte le transazioni eseguite con quella versione locale di MetaMask sono state registrate nella blockchain. Le transazioni dunque dovrebbero essere visibili sia su [block explorer](https://metamask.zendesk.com/hc/en-us/articles/360057536611), che in un'altra istanza di MetaMask, se [ripristini l'app utilizzando la stessa frase di recupero segreta](https://metamask.zendesk.com/hc/en-us/articles/360015289612), **con le parole nello stesso ordine**. In conclusione, fintanto che potrai utilizzare la frase di recupero segreta, potrai sempre disinstallare MetaMask e ripristinare il tuo portafoglio.
* **Questo può contenere un numero molto elevato di account diversi.** Quando MetaMask crea o ripristina il tuo portafoglio tramite la frase di recupero segreta, inizialmente viene generato soltanto il primo account. Tuttavia, tutti [gli altri account che hai creato possono essere creati nuovamente](https://metamask.zendesk.com/hc/en-us/articles/360015489271) in un'istanza futura di MetaMask. **Poiché il portafoglio è *deterministico*, verranno ricreati sempre gli stessi account nello stesso ordine. Per ulteriori informazioni, consulta le domande frequenti di seguito.** Tieni presente che gli account aggiuntivi oltre al primo, che viene chiamato automaticamente "Account 1", ***non***verranno aggiunti automaticamente al tuo account in tutti i casi. Per ulteriori informazioni, consulta la nostra spiegazione [qui](https://metamask.zendesk.com/hc/en-us/articles/360015489271-How-to-add-missing-accounts-after-restoring-with-Secret-Recovery-Phrase#:~:text=If%20you%20have,automatically%20re%2Dadded.).
* **È possibile [importare account](https://metamask.zendesk.com/hc/en-us/articles/360015489331) da altre tecnologie compatibili con Ethereum in un portafoglio MetaMask.** Per farlo, viene utilizzata la *chiave privata* corrispondente all'account che si vuole importare. Tuttavia, **questo account non verrà ripristinato automaticamente da un'altra istanza di MetaMask, ma dovrai aggiungerlo di nuovo manualmente**. Di conseguenza, se hai importato manualmente gli account, **annota le chiavi private corrispondenti, proprio come hai fatto per la frase seme**, per poterli importare nuovamente in futuro.


 


**La frase di recupero segreta di MetaMask: cosa fare e cosa evitare**
----------------------------------------------------------------------




**Da fare:**

* **Scrivi la frase di recupero segreta e conservala in un luogo sicuro**. Non possiamo dirti precisamente dove, poiché dipende dalle circostanze in cui ti trovi.
	+ È importante scriverla su carta perché in questo modo non può essere sottratta online. Ad esempio, se tu la salvassi in una cartella di archiviazione sul cloud collegata a internet, in linea di principio, potrebbe venire rubata.
* Verifica lo spelling, la completezza della frase e che l'ordine originario delle parole sia stato rispettato.
* Se hai bisogno di assistenza, contatta i [canali ufficiali](https://metamask.zendesk.com/hc/en-us/articles/360058230211) del Supporto di MetaMask.





**Da evitare:**

* Salvare la frase di recupero segreta in un luogo che può essere facilmente scoperto o violato, come in un documento salvato sul cloud o in un'email con oggetto "Frase seme", oppure in un post-it sul tuo computer.
* Condividere la frase con chiunque, anche se la persona dice di essere del Supporto di MetaMask.
* Modificare l'ordine delle parole.





 


**Domande frequenti sulla frase di recupero segreta**
-----------------------------------------------------


### La mia frase seme ha ripristinato un account diverso.


Consulta [qui](https://metamask.zendesk.com/hc/en-us/articles/360058120992) l'articolo della knowledge base su questo argomento. Inoltre, puoi consultare il thread della Community [qui](https://community.metamask.io/t/restored-metamask-no-coins-are-showing/878/107?u=jacob.cantele) per ottenere maggiore contesto e ulteriori informazioni.


### Altre domande frequenti sulla frase di recupero segreta:


[Come rivelare la frase di recupero segreta](https://metamask.zendesk.com/hc/en-us/articles/360015290032)


[Come recuperare la frase di recupero segreta](https://metamask.zendesk.com/hc/en-us/articles/360018766351)


[Importazione di una frase seme da un altro software: percorso di derivazione](https://metamask.zendesk.com/hc/en-us/articles/360060331752)


[Guida alla migrazione del portafoglio](https://metamask.zendesk.com/hc/en-us/articles/4867408571803)


[Come importare un account](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[Come verificare l'attività del mio portafoglio in un blockchain explorer](https://metamask.zendesk.com/hc/en-us/articles/360057536611)


[Che cos'è una frase di recupero segreta e come faccio a tenere al sicuro il mio portafoglio?](https://metamask.zendesk.com/hc/en-us/articles/360060826432)


 


**MetaMask e le password**
--------------------------


MetaMask utilizza le password per un unico scopo, ossia per garantire la sicurezza dell'app. In altre parole, affinché gli utenti possano aprire l'app sia nell'app per mobile che nell'estensione per il browser. Dopo che avrai ripristinato o creato il tuo portafoglio dalla frase di recupero segreta non dovrai utilizzarla regolarmente, **sebbene sia sempre consigliabile fare un backup e conservarlo in un luogo sicuro**. Quindi per sbloccare l'app sul tuo dispositivo, utilizzerai la password oppure, più probabilmente, l'autenticazione biometrica, come il riconoscimento del volto o l'impronta digitale. Per maggiori dettagli, consulta il nostro articolo [qui](https://metamask.zendesk.com/hc/en-us/articles/4405451730331).


 


**Chiavi private**
------------------


Se da un lato, la frase di recupero segreta viene utilizzata per creare e ripristinare l'intero portafoglio di MetaMask, compresi tutti gli account creati in quel portafoglio, dall'altro, a ciascun account corrisponde una *chiave privata*, che può essere utilizzata per importare soltanto quell'account in un altro portafoglio. Analogamente, singoli account da altre tecnologie crypto possono essere importanti nel tuo portafoglio MetaMask. 


### Domande frequenti sulle chiavi private


[Che cosa sono gli account importati?](https://metamask.zendesk.com/hc/en-us/articles/360015289932)


[Come importare un account](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[Come esportare la chiave privata di un account](https://metamask.zendesk.com/hc/en-us/articles/360015289632)


[Posso importare un account di un portafoglio Coinbase nel portafoglio MetaMask?](https://metamask.zendesk.com/hc/en-us/articles/360058485292)

