Quando invii una transazione su Ethereum o su una rete compatibile, una parte del gas che paghi è un'offerta alla rete per elaborare prima la tua transazione, questo elemento è noto come tassa di priorità. Anche se MetaMask ti assiste calcolando un costo totale in gas che probabilmente farà accettare la tua transazione, puoi finire per aspettare a lungo se invii con un prezzo del gas basso. Per consigli sui prezzi del gas necessari per completare una transazione in un lasso di tempo ragionevole, usa come riferimento fonti tipo [Etherscan Gas Tracker](https://etherscan.io/gastracker) o un tracker simile a seconda della rete che stai utilizzando.


Inoltre, a volte si verificano circostanze in cui qualcosa non va a buon fine e una transazione è semplicemente bloccata o resta in corso da molto tempo.


Non importa come si arriva a questa situazione, ma esistono vari modi per affrontarla.


 


### Prima di intraprendere qualsiasi altra azione, il primo passo dovrebbe essere quello di uscire e chiudere completamente il browser, riaprirlo e sbloccare MetaMask (sul dispositivo mobile basta chiudere l'app e riaprirla). Se il problema persiste, segui le istruzioni riportate di seguito.


 


**Velocizzare una transazione**
-------------------------------


![Transazione velocizzata da MetaMask](https://support.metamask.io/hc/article_attachments/12927043481371)


Prova una delle seguenti opzioni:


* Attendi finché la rete non è disposta a elaborare le transazioni a questo prezzo
* Se non l'hai già fatto, fai clic sul pulsante che dice **Velocizza**. In questo modo potrai inviare nuovamente la stessa transazione, ma con un costo in gas superiore che dovrebbe consentire un'elaborazione più rapida della transazione. Poiché questo processo riutilizza lo stesso numero della transazione dell'originale, non dovrai pagare il gas due volte.


Tieni presente che **velocizzare la transazione aumenterà l'importo che spenderai per la transazione**.


 


**Annullamento di una transazione - Metodo 1: annullamento in app**
-------------------------------------------------------------------


Se non l'hai già fatto, per annullare la transazione, seleziona semplicemente **Annulla**, come nello screenshot precedente. Tieni presente che **l'annullamento può essere *tentato* solo se la transazione sulla rete è ancora in corso.** Le transazioni già confermate non possono essere annullate.


 


**Annullare una transazione - Metodo 2: numero di transazione personalizzato**
------------------------------------------------------------------------------


Questo processo prevede l'invio di una transazione con lo stesso numero della transazione (un numero identificativo per ogni transazione, derivato dalla frase "numero usato solo una volta"). La transazione in realtà non deve avere alcun valore, ad esempio potresti inviare 0 ETH. L'importante è pagare un costo in gas sufficiente per far sì che la rete le dia la priorità. 


Quando utilizzi questo metodo, **dovrai procedere a ritroso partendo dalla transazione in attesa meno recente nella coda che vuoi annullare**. Ad esempio, non puoi tentare di annullare una transazione con un numero di transazione 10 prima di annullarne una con numero di transazione 9. 


*Gli screenshot qui sotto sono stati realizzati in momenti diversi, quindi i costi in gas mostrati possono variare, anche da una passo dall'altro. Non lasciarti scoraggiare da questo! Quando lo fai di persona, MetaMask si aggiorna automaticamente in tempo reale per mostrare tariffe di mercato.*




Estensione App mobile


1. Nelle impostazioni avanzate, attiva **Customize transaction nonce** e **Controlli gas avanzati**. Con questi controlli puoi gestire il costo in gas che paghi e assicurarti che la transazione di annullamento venga elaborata prima di quella originale che vuoi annullare.



#### Nota:


Estensione MetaMask dispone attualmente di una funzione sperimentale chiamata [Enhanced Gas Fee UI](https://metamask.io/1559/) (da non confondere con [controlli avanzati del gas](https://support.metamask.io/hc/en-us/articles/360022895972)). Puoi eseguire questi passaggi indipendentemente dal fatto che sia attivata, ma tieni presente che avranno un aspetto diverso. I passaggi di seguito non utilizzato Enhanced Gas UI. Tieni presente:



	* Se hai attivato la funzione Enhanced Gas UI, dovrai comunque attivare anche la funzione "Customize transaction nonce".
	* Se non hai attivato Enhanced Gas UI, dovrai attivare sia "Advanced gas controls" che "Customize transaction nonce".

![Impostazioni avanzate MetaMask](https://support.metamask.io/hc/article_attachments/12927064113947)
2. **Invia una nuova transazione**. In nuova transazione, invia **A** te stesso, ossia al tuo indirizzo MetaMask pubblico. **Compila "Personalizza il numero della transazione" con lo stesso numero della transazione ancora in corso**:


![Metamask_custom_transaction_nonce_Extension.png](https://support.metamask.io/hc/article_attachments/12927064259483)
3. Ora premi "Modifica" accanto a "Costo di annullamento in gas" (se la funzionalità sperimentale [Interfaccia utente migliorata per gas](https://support.metamask.io/hc/en-us/articles/360022895972-Using-advanced-gas-controls#:~:text=%C2%A0-,Enhanced%20Gas%20UI,-Since%20the%20introduction) è attiva, verrà visualizzata come "Market"). Verranno visualizzate le seguenti opzioni:


![Estensione MetaMask per controlli avanzati del gas](https://support.metamask.io/hc/article_attachments/12927065407515)


Per assicurarti che la tua richiesta di annullamento venga presa in considerazione in via prioritaria e prima della transazione originale, **devi pagare di più come costo in gas**. Segui queste istruzioni:


	* Imposta un tuo **gas limit** *simile o leggermente superiore* rispetto alla transazione originale.
	* Imposta il **costo per priorità massimo** su *almeno il 10% in più* (in Gwei) rispetto al costo in gas della transazione originale (in corso). Ad esempio, se tale transazione prevedeva un costo in gas di 30 Gwei, imposta il costo per priorità massimo nella transazione di sostituzione/annullamento su 33-35 Gwei.
	* Assicurati che il tuo costo massimo sia almeno del 30% superiore rispetto al costo massimo della transazione che stai sostituendo. Ad esempio, se il tuo costo precedente era di 150 Gwei, questa volta scegli qualcosa di più vicino a 200 Gwei.Consulta un gas tracker tipo [Etherscan](https://etherscan.io/gastracker) o [ETH Gas Station](https://ethgasstation.info/) per indicazioni sui costi massimi consigliati.




1. **In Impostazioni > Avanzate, attiva "Customize transaction nonce".**
2. **Invia una nuova transazione.** In nuova transazione, invia A te stesso, ossia al tuo indirizzo MetaMask pubblico. **Compila "Personalizza il numero della transazione" con lo stesso numero della transazione ancora in corso**:


Per trovare l'impostazione Personalizza il numero della transazione nell'app, vai alla schermata di conferma della transazione, che verrà visualizzata dopo aver inserito la quantità di token e il destinatario. Tocca su "Modifica" per modificarla:


![Personalizza il numero della transazione MetaMask mobile](https://support.metamask.io/hc/article_attachments/12927068442907)
3. Ora devi assicurarti che le impostazione del gas siano configurate in modo che la transazione di sostituzione venga elaborata. Nella schermata di conferma della transazione, tocca il valore del gas evidenziato:


![Controlli del gas avanzati MetaMask mobile](https://support.metamask.io/hc/article_attachments/12927041593755)


Ora vai su "Opzioni avanzate" dal menu che viene visualizzato.
4. Da qui, puoi regolare con precisione il gas per assicurarti che la tua transazione venga accettata. Ora vedrai una schermata simile a questa:


![Controlli del gas avanzati MetaMask mobile](https://support.metamask.io/hc/article_attachments/12927063201691)


Da qui, modifica le impostazioni del gas. Segui queste istruzioni per assicurarti che la transazione venga accettata:


	* Imposta un tuo **gas limit** *simile o leggermente superiore* rispetto alla transazione originale.
	* Imposta il **costo per priorità massimo** su *almeno il 10% in più* (in Gwei) rispetto al costo in gas della transazione originale (in corso). Ad esempio, se tale transazione prevedeva un costo in gas di 30 Gwei, imposta il costo per priorità massimo nella transazione di sostituzione/annullamento su 33-35 Gwei.
	* Assicurati che il **tuo costo massimo** sia *almeno del 30% superiore* rispetto al costo massimo della transazione che stai sostituendo. Ad esempio, se il tuo costo precedente era di 150 Gwei, questa volta scegli qualcosa di più vicino a 200 Gwei.Consulta un gas tracker tipo [Etherscan](https://etherscan.io/gastracker) o [ETH Gas Station](https://ethgasstation.info/) per indicazioni sui costi massimi consigliati.



