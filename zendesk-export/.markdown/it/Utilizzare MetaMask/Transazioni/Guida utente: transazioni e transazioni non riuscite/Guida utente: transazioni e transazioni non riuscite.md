
#### Ti stai avvicinando per la prima volta alle criptovalute e al web3?


Vai su [MetaMask Learn](https://learn.metamask.io/) per accedere a un'esperienza di apprendimento intuitiva, concepita appositamente per coloro che si avvicinano per la prima volta al web3. È completamente gratuito, disponibile in più lingue e offre strumenti utili come le simulazioni per aiutarti a orientarti con MetaMask.



#### *Questo articolo contiene spiegazione e collegamenti a risorse relative alle transazioni e al motivo per cui non sempre vanno a buon fine e, più in basso, sono disponibili collegamenti a scenari comuni di transazioni non riuscite e indicazioni su come affrontarli:*


* [Anatomia di una transazione della blockchain](#h_01G79J04D0EN1VD8VS7C7J7KD1)
* [Problemi comuni](#h_01G79J09NWA8CGR4VYC2PT5B6Y)
* [Correzioni principali](#h_01G79J0J8JTRPM9MRB76EN1GPP)
* [Risorse aggiuntive e passaggi successivi](#h_01G79J0RP8ZMZ1V1SKQY70TXCT)
* [Domande frequenti](#h_01G79J18RBK27GZCF10CGN9GKP)


 


**Anatomia di una transazione della blockchain**
------------------------------------------------


Quando si parla di "transazioni" su una rete blockchain pubblica, di solito ci si riferisce a interazioni tra due indirizzi, in altre parole, token, siano essi fungibili o meno, o altri criptoasset "inviati" da un indirizzo all'altro. Esistono anche transazioni denominate "transazioni interne", che sono interazioni che si verificano tra contratti smart e per la maggior parte non rientrano nell'ambito di questo articolo.



#### Hai bisogno di ulteriori informazioni?


Per ulteriori informazioni sulle reti blockchain e su come funzionano in generale, leggi qui il nostro [articolo introduttivo](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) e se rimani bloccato su parole sconosciute, il nostro [glossario è sempre disponibile](https://consensys.net/knowledge-base/a-blockchain-glossary-for-beginners/).



Per maggiore chiarezza, nulla viene effettivamente *inviato* da nessuna parte. Una rete blockchain abilitata ai contratti intelligenti come Ethereum ha diversi componenti, o funzioni. Uno di questi è quello che chiamiamo "computer": la macchina virtuale di Ethereum, o EVM, che è in grado di eseguire programmi ("contratti intelligenti"). La "spina dorsale" del sistema, tuttavia, è un *registro distribuito*: **immagina un foglio di calcolo che contenga, su un lato, ogni singolo indirizzo del portafoglio Ethereum e ogni indirizzo ha una colonna per ogni tipo di criptoasset che contiene.** 


Usiamo un esempio per l'illustrare questo sistema. Supponiamo che Guglielmo voglia inviare una transazione a Giovanna. Guglielmo ha 1,36 ETH nel suo account e vuole inviare 0,5 ETH a Giovanna. Sembra una buona giornata per Dolores, anche in un mercato ribassista. 


Guglielmo apre il suo portafoglio MetaMask, inserisce l'indirizzo di Giovanna, configura i parametri del costo in gas che ritiene di poter pagare e preme 'invia'.


A questo punto, la transazione entra in uno stato di possesso temporaneo locale, nota come *pool di memoria locale,*o *mempool locale*. La transazione verrà quindi "rilevata" dal nodo più vicino della rete; a seconda delle [impostazioni gas](https://metamask.zendesk.com/hc/en-us/articles/360022895972-Using-advanced-gas-controls) di Guglielmo, la sua transazione avrà la priorità (**più Guglielmo è disposto a pagare per [unità di gas](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas), più rapidamente verrà elaborata la sua transazione**) e propagata ad altri nodi della rete. I nodi faranno il lavoro di verificare che Guglielmo abbia ETH da spendere, quindi eseguiranno effettivamente la "transazione": **il registro verrà modificato; 0,5 saranno addebitati sul saldo di Guglielmo e 0,5 saranno accreditati a Giovanna'.**


*"Movendosi la mano scrive e avendo scritto va avanti":* l'ETH non si è mosso attraverso una rete di per sé; non era un'e-mail inviata dal computer di Guglielmo alla posta in arrivo del MetaMask di Giovanna o qualcosa del genere. Guglielmo ha inviato una richiesta, **autenticata dalle sue [chiavi private tramite MetaMask](https://metamask.zendesk.com/hc/en-us/articles/4404722782107-User-guide-Secret-Recovery-Phrase-password-and-private-keys)**, alla rete per fare un accredito a Giovanna da addebitare sul suo account. Dopo il processo di verifica programmato nei protocolli della rete, questa è l'operazione che viene eseguita. 


#### *Questo è tutto quello che c'è da sapere su una transazione: è una richiesta al registro di riallocare qualcosa da un indirizzo all'altro.*


 


**Se qualcosa va storto**
-------------------------


Le cose possono andare storte per tutta una serie di motivi. Spesso i motivi sono "di natura software": MetaMask ha un bug o qualcosa è stato configurato in modo errato per quanto riguarda la rete che stai cercando di utilizzare oppure si è verificato un errore di connettività.


Un **problema comune è che l'utente, nel tentativo di pagare meno per la propria transazione, abbia impostato un gas limite molto basso** e le condizioni della rete sono così congestionate che non c'è spazio in nessun blocco per una transazione così "economica", a volte per molto tempo. Alla fine, la transazione diventerà "obsoleta" e dovrà essere annullata dall'utente. 


**Se hai inviato una transazione e non è stata finalizzata**, il suo stato su MetaMask verrà mostrato come "in corso". 


**Se hai inviato una transazione e non è riuscita, la causa più probabile è la mancanza di gas**: hai "finito il gas", in altre parole, la transazione ha avuto un costo in gas che, moltiplicato per il prezzo del gas, ha portato a un importo totale della valuta nativa della rete superiore a quello che avevi nel tuo portafoglio. 



#### Info


Per ulteriori informazioni sul calcolo del gas, consulta la nostra [guida al costo in gas qui](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas).



Ci sono vari motivi per cui ciò può accadere, ma la prima cosa da prendere in considerazione è la transazione che stai cercando di eseguire. Il minting di un NFT durante i periodi di picco del traffico di rete può essere molto dispendioso in termini di costo in gas; se stai provando una transazione nuova o sperimentale, provare su una rete di prova prima di pagare vere tasse di rete in tempo reale è un'idea che vale la pena valutare.


 


**Risolvere il problema**
-------------------------


### **Fattore chiave n. 1: locale o trasmesso in rete**


Mentre procedi alla diagnosi del problema relativo alla transazione, specialmente quando si tratta di una transazione in corso, devi verificare se la transazione è ancora nel tuo mempool locale o se è arrivata alla rete ed è bloccata lì per qualsiasi motivo. Se si trova solo nel tuo mempool locale, la soluzione potrebbe essere semplice come bloccare e sbloccare il tuo portafoglio MetaMask (**assicurati di avere la tua password e di aver eseguito il backup della tua frase di backup segreta prima di farlo**). Se è arrivata alla rete, la soluzione potrebbe essere più complicata.


Per ulteriori informazioni sulla risoluzione di questi problemi, vedi i seguenti link.  
  



### **Fattore chiave n. 2: numero della transazione**


Questa parola può significare cose diverse. È una contrazione di "numero usato solo una volta" e, in questo contesto, significa grossomodo "numero di transazione", a partire dalla prima transazione effettuata dall'indirizzo di invio. Puoi metterti in guai seri se, ad esempio, effettui due transazioni diverse da istanze diverse di MetaMask con lo stesso indirizzo di portafoglio nello stesso momento. **Le transazioni del tuo indirizzo devono essere in ordine crescente in base al loro numero di transazione** Tuttavia, proprio come i numeri di transazione possono causare il blocco di una transazione, possono essere la chiave per sbloccare una transazione.


Per saperne di più su questa tecnica, [leggi qui](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction).


 


**Passaggi successivi**
-----------------------


### *Se hai una transazione non riuscita o in corso, consulta le seguenti risorse per assistenza.*


#### [Come inviare token dal portafoglio MetaMask](https://metamask.zendesk.com/hc/en-us/articles/360015488931)


#### [Come velocizzare o annullare una transazione in corso](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction)


#### [Perché la mia transazione non è riuscita con un errore "Gas esaurito"?](https://metamask.zendesk.com/hc/en-us/articles/360038849792-Why-did-my-transaction-fail-with-an-Out-of-Gas-error-How-can-I-fix-it-)


#### [Risoluzione dei problemi di Uniswap](https://metamask.zendesk.com/hc/en-us/articles/360053394291-Uniswap-support-and-troubleshooting-tips)


#### [Guida per l'utente: gas](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas)


#### [Posso annullare una transazione già confermata?](https://metamask.zendesk.com/hc/en-us/articles/360059957352-Can-I-reverse-an-already-confirmed-transaction-)


 


**Domande frequenti**
---------------------


#### 
*D: Un account nel mio portafoglio ha una transazione in corso o in coda. Posso avviare un'altra transazione da un account diverso all'interno dello stesso portafoglio?*R: Sì, puoi farlo. Il numero di transazione viene conteggiato per account, non per portafoglio.

