### Come calcolare il prezzo del gas


Se sei sulla rete Ethereum principale puoi controllare [lo strumento del gas di Etherscan](https://etherscan.io/gastracker) per una stima del prezzo del gas di oggi.  Tieni presente che il prezzo del gas oscilla. Fai sempre riferimento alla stazione di servizio per vedere i prezzi correnti del gas.


La rete Ethereum richiede gas per eseguire transazioni. Quando invii token, interagisci con un contratto, invii ETH o fai qualsiasi altra cosa sulla blockchain, devi pagare per quel calcolo. Tale pagamento viene calcolato in gas e il gas viene sempre pagato in ETH.


Paghi il calcolo, indipendentemente dal fatto che la transazione abbia esito positivo o meno. Anche se la transazione non va a buon fine, i miner o i validatori devono finalizzare ed eseguire la transazione, il che richiede potenza di calcolo. Devi pagare per quel calcolo, proprio come pagheresti per una transazione andata a buon fine.


 


### Come recuperare il gas limite


Sai quanto costa ogni unità di gas, ma quante unità di gas devi spendere? Se si tratta di una semplice transazione, ad esempio l'invio di ETH o di un token ERC-721 a un altro indirizzo, dovresti spendere 21.000 unità di gas. Se fai qualcosa di più complesso, uno strumento adatto è un block explorer, come [etherscan.io](https://etherscan.io/). Vai al contratto con cui vuoi interagire e inizia a esaminare le transazioni che sono state effettuate con il contratto. Avrai un'idea migliore della quantità di gas effettivamente utilizzata dagli altri utenti.



#### Calcolatore gas


Esistono alcuni strumenti che ti permettono di stimare quanto ti costerà il gas in valuta fiat prima di effettuare una transazione. Un esempio è il [Calcolatore del costo in gas di Cryptoneur](https://www.cryptoneur.xyz/gas-fees-calculator) che ti permette di inserire i dettagli della tua transazione e di ottenere il costo stimato del gas nella tua valuta locale e in base alla domanda corrente di una determinata rete (puoi scegliere tra le principali reti compatibili con il sistema EVM).



### 
Struttura complessiva del costo in gas


A partire da [EIP-1559](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1559.md), il costo complessivo pagato dal creatore di una transazione viene calcolata nel seguente modo: **((costo base + costo per priorità) x unità di gas consumato)**. 


Per ulteriori informazioni, leggi [qui](https://support.metamask.io/hc/en-us/articles/4404600179227).


 


**Tieni presente che non si tratta di un costo che MetaMask riceve, quindi non possiamo rimborsarlo.** Questa costo viene pagata ai miner o ai validatori per finalizzare la transazione, convalidarla in un blocco e proteggere la blockchain.

