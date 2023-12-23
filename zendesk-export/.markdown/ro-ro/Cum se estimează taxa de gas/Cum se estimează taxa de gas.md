### Obținerea taxei de gas


Dacă ești pe rețeaua Ethereum, poți verifica [instrumentul de calcul al taxei de gas](https://etherscan.io/gastracker), pentru a estima corect taxa de gas în orice moment. Este foarte important să reții că taxa de gas este într-o continuă fluctuație, și este indicat să verifici instrumentul de calcul al taxei de gas ori de câte ori dorești să inițiezi o tranzacție nouă.


Rețeaua Ethereum necesită gas pentru a executa orice tranzacție. Când trimiți tokeni, interacționezi cu un contract sau orice altă acțiune pe blockchain, trebuie să plătești taxa de gas. Această taxă este calculată în gas, iar gas-ul se plătește întotdeauna în ETH.


Indiferent dacă tranzacția ta este reușită sau eșuată, tot trebuie sa plătești taxa de gas. Minerii sau validatorii trebuie să finalizeze și să execute tranzacția ta, chiar dacă tranzacția eșuează. Acest lucru necesită putere de calcul. Trebuie să plătești pentru acest calcul, la fel cum ai plăti pentru o tranzacție reușită.


### Obținerea limitei de gas


Deci știi cât costă fiecare unitate de gas, dar câte unități de gas trebuie să cheltui? Ei bine, dacă este o tranzacție simplă - să zicem, trimiterea tokenului ETH sau a unui token ERC-721 la o altă adresă, ar trebui să cheltui 21.000 de unități de gas. Dacă faci ceva mai complex, un instrument bun este un explorer blockchain (explorator de blocuri), cum ar fi [etherscan.io](https://etherscan.io/). Navighează la contractul cu care vrei să interacționezi și uită-te la  tranzacțiile care s-au efectuat cu contractul respectiv. Îți poți face astfel o idee mai amplă despre cât de mult gas utilizează ceilalți.


#### 
Calculatorul de gas


Există câteva instrumente disponibile pentru a estima cât te va costa gas-ul în monedă fiat, înainte de a efectua o tranzacție. Un exemplu este calculatorul de taxe de gas[Cryptoneur gas fee calculator](https://www.cryptoneur.xyz/gas-fees-calculator), care-ți permite să introduci detaliile tranzacției tale și să generezi costul estimat al gas-ului în moneda locală, conform cu cererea curentă de pe acea rețea (poți alege din majoritatea rețelelor compatibile EVM).


### Structura generală a taxei de gas


Începând cu EIP-1559, taxa totală pe care o plătește un utilizator se calculează astfel:**(taxă de bază + taxă de prioritate) x unități de gas utilizate**.


Pentru mai multe informații, vezi [aici](https://support.metamask.io/hc/en-us/articles/4404600179227).


Te rugăm să reții că aceasta nu este o taxă pe care o primește MetaMask, așa că nu o putem rambursa. Această taxă este plătită minerilor sau validatorilor pentru finalizarea tranzacției, validarea acesteia într-un bloc și securizarea blockchain-ului.


 


 

