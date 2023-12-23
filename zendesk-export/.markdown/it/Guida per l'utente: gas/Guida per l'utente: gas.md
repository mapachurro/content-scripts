
#### Ti stai avvicinando per la prima volta alle criptovalute e al web3?


Vai su [MetaMask Learn](https://learn.metamask.io/) per accedere a un'esperienza di apprendimento intuitiva, concepita appositamente per coloro che si avvicinano per la prima volta al web3. È completamente gratuito, disponibile in più lingue e offre strumenti utili come le simulazioni per aiutarti a orientarti con MetaMask.



Gas è l'unità di misura usata per determinare la quantità di lavoro computazionale necessario per elaborare transazioni e contratti smart. In sostanza è un costo della transazione. Il termine ha origine da Ethereum, nel cui contesto si riferisce al calcolo effettuato sulla macchina virtuale di Ethereum (EVM). Dalla nascita di Ethereum, sono nate numerose reti compatibili con EVM (e non) che hanno adottato modelli simili. 


Il termine è analogo al gas che alimenta il motore di un'auto: è il costo fluttuante e occasionalmente costoso del funzionamento. I contratti smart più complessi richiedono più gas per alimentare i loro calcoli, proprio come un'auto più grande e più potente richiede più carburante per funzionare.


La modalità di calcolo del costo in gas varia a seconda della rete. Ad esempio, calcolare il gas su Ethereum era molto complicato, ma è stato notevolmente semplificato con l'implementazione della Proposta di miglioramento di Ethereum**(EIP) 1559** in agosto 2021 (noto anche come Upgrade di Londra). In sostanza, paghi una **tariffa di base** per ogni unità di gas che viene***bruciata*** (leggi: viene cancellata e scompare) al completamento della transazione. Oltre al costo base, devi aggiungere un **costo per priorità**, sempre per unità di gas, il cui valore dipende dalla rapidità con cui vuoi che venga espletata la transazione. 


Nell'ampia gamma di reti compatibili con EVM disponibili, il costo in gas o alternative con funzionamento simile sono diventati essenzialmente il metodo standard per calcolare i costi delle transazioni. I costi vengono pagati nel token nativo della rete: ad esempio, qualsiasi transazione su Ethereum richiede ETH; l'utilizzo di BSC richiede BNB; l'utilizzo di Polygon richiede MATIC. Alcune reti hanno adottato il modello all'ingrosso EIP-1559 di Ethereum, ad esempio Polygon, mentre altre hanno apportato modifiche, tra cui Avalanche, per la loro C-Chain (che [brucia sia il costo base che il costo per priorità](https://docs.avax.network/learn/platform-overview/transaction-fees/#c-chain-fees), anziché solo la prima).


Se vuoi leggere un approfondimento su come funziona il gas su Ethereum, vedi [qui](https://ethereum.org/en/developers/docs/gas/). 


 


Ecco alcune **informazioni essenziali per la gestione del gas** **su MetaMask**:


#### **Il limite di gas (unità di gas utilizzate)**


Il *gas limite* è il **numero massimo di unità di gas che sei disposto a pagare** per effettuare una transazione o un'operazione EVM. Operazioni diverse richiedono quantità diverse di unità di gas. Una normale transazione di invio di ETH o di un token costa normalmente **21.000** gas, mentre l'approvazione di un token ERC-20 ne richiede 45.000.  Molte reti, come la blockchain Harmony compatibile con EVM, utilizzano un modello identico in cui anche le transazioni standard costano 21.000 gas.



#### Devo modificare il limite del gas?


No. MetaMask imposta automaticamente il limite di gas in base alla transazione che stai cercando di eseguire. Nella maggior parte dei casi, questo sarà sufficiente per completare la transazione. Se vuoi controllarlo o modificarlo, assicurati di avere attivato [controlli avanzati del gas](https://metamask.zendesk.com/hc/en-us/articles/360022895972) (o di utilizzare l'interfaccia utente sperimentale Enhanced Gas) e premi "Modifica" nella schermata di conferma della transazione.



#### **La tariffa di base**


Ogni blocco sulla rete Ethereum ha un costo di base determinato dalla domanda della rete: il costo di base si basa sulla dimensione del blocco precedente, confrontato con una dimensione target del blocco (dove la dimensione si riferisce alla quantità totale di gas utilizzata per tutte le transazioni che il blocco include). Se la dimensione del blocco precedente supera l'obiettivo, la tariffa di base del blocco successivo aumenta del 12,5%, lasciando a te, utente (o al tuo portafoglio), la certezza assoluta della tariffa di base del blocco successivo. Il costo totale in gas deve corrispondere almeno a questo prezzo per poter essere incluso nel blocco. 


#### **La tariffa prioritaria**


La*tariffa prioritaria*, detta anche "mancia del miner", incentiva il miner a dare priorità alla tua transazione. 


Ovviamente, il fatto che questo vada effettivamente a un miner dipende dal [meccanismo di consenso](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) che utilizzano: la rete principale di Ethereum è diventata una rete Proof of Stake (PoS) in seguito alla fusione di settembre 2022, quindi la quota di priorità va ai validatori invece che ai miner. 


#### **Il costo massimo**


Il costo massimo è l'importo totale e globale pagato per la transazione. Viene calcolato come: **(****costo base + costo per priorità) x unità di gas consumato.** MetaMask inizialmente imposta questo importo in base alla cronologia del blocco precedente. Tuttavia, gli utenti possono modificare questo importo tramite le impostazioni personalizzate (vedi di seguito). La differenza tra il costo massimo in gas e (costo base + costo massimo prioritario in gas) viene "rimborsata" all'utente.


 


### **Altri concetti**


#### **Gwei**


Gwei è la forma abbreviata per gigawei. Un Ethereum è composto da 1.000.000.000 [gwei](https://ethgasstation.info/blog/gwei/). [Gwei](https://www.investopedia.com/terms/g/gwei-ethereum.asp) viene utilizzato per i costi in gas, ovvero i pagamenti effettuati dagli utenti per compensare l'energia di calcolo necessaria per elaborare e validare le transazioni sulla blockchain di Ethereum.


Anche altre reti tendono a calcolare i costi utilizzando gwei, ad esempio Fantom, Harmony e Avalanche.


#### **Slippage**


Lo slippage è la differenza percentuale prevista tra un prezzo quotato e un prezzo eseguito.


#### **Costo in gas**


Il *costo in gas* si riferisce al costo della transazione sulla blockchain di Ethereum. È ciò che gli utenti pagano per far convalidare o completare la loro transazione. 


#### **Costo base**


Generato dal protocollo. Rappresenta il moltiplicatore minimo del "Gas Utilizzato" necessario per includere una transazione in un blocco (cioè per completare una transazione). Questa è la parte del costo della transazione che viene consumata.


 


### **Controlli gas avanzati**


Se vuoi analizzare nel dettaglio i tuoi controlli del gas (può essere utile se stai testando una dapp, ad esempio), MetaMask può farlo. Leggi l'articolo completo [qui](https://metamask.zendesk.com/hc/en-us/articles/360022895972).


 


### **Domande frequenti**


[Perché ho pagato il costo in gas per una transazione non riuscita?](https://metamask.zendesk.com/hc/en-us/articles/360045439051)


[Posso avere un rimborso del costo in gas?](https://metamask.zendesk.com/hc/en-us/articles/360058370012)


[Come faccio a velocizzare o annullare una transazione in corso?](https://metamask.zendesk.com/hc/en-us/articles/360015489251)


[Come stimare il costo in gas](https://metamask.zendesk.com/hc/en-us/articles/360059562111)


[Perché i miei costi in gas sono così elevati?](https://metamask.zendesk.com/hc/en-us/articles/360058751211-Why-my-gas-fees-are-so-high-)


[Errore: [ethjs-query] durante la formattazione degli output da RPC (errore sottoprezzo della transazione)](https://metamask.zendesk.com/hc/en-us/articles/4402538041869)


[Come correggere l'errore "Fondi insufficienti" o il pulsante di conferma disattivato](https://metamask.zendesk.com/hc/en-us/articles/360044703372)


 


 

