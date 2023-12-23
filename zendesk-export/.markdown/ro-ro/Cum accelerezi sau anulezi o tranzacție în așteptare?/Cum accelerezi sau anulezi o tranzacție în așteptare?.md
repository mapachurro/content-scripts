
#### Ai încercat MetaMask Activity?


MetaMask Activity este un instrument nou care îți poate analiza tranzacțiile și îți poate sugera automat posibile rezolvări. Are și o funcție încorporată dedicată tranzacțiilor în așteptare. De ce să nu-l încerci? Apasă [aici](https://support.metamask.io/hc/en-us/articles/13460965279003) pentru mai multe informații.



Când trimiți o tranzacție pe Ethereum sau o altă rețea compatibilă, o parte din gas-ul pe care îl plătești este o ofertă către rețea pentru a-ți procesa tranzacția mai devreme - acest element este cunoscut sub numele de taxă de prioritate. Deși MetaMask te va asista prin calcularea unei taxe totale de gas care, cel mai probabil, va permite ca tranzacția să fie preluată, poți ajunge să aștepți mult dacă lansezi tranzacția cu un preț scăzut al gas-ului. Pentru sfaturi cu privire la ce preț de gas va duce la finalizarea unei tranzacții într-un interval de timp rezonabil, te rugăm să consulți surse precum [gas tracker-ul Etherscan](https://etherscan.io/gastracker), sau gas tracker-ul aferent rețelei pe care o utilizezi.


În plus, există uneori circumstanțe în care ceva nu merge bine și o tranzacție este pur și simplu blocată sau în așteptare pentru o perioadă foarte lungă de timp.


Indiferent cum ai ajuns în acest punct, există câteva moduri diferite de a aborda această situație.


 


### Înainte de orice altă acțiune, primul pas ar fi să ieși și să închizi complet browser-ul, să-l redeschizi și să deblochezi MetaMask (pe mobil, trebuie doar să închizi aplicația și să o redeschizi). Dacă acest lucru nu rezolvă problema, continuă cu următoarele:


 


**Accelerarea unei tranzacții**
-------------------------------


![MetaMask speed up transaction](https://support.metamask.io/hc/article_attachments/12927043481371)


Încearcă una dintre opțiunile de mai jos:


* Așteaptă până când rețeaua este dispusă să proceseze tranzacțiile la acest preț.
* Dacă nu ai făcut asta deja, apasă pe butonul pe care scrie **“Accelerează” (Speed Up)**. Acest lucru îți va permite să reefectuezi aceeași tranzacție, dar cu o taxă de gas mai mare, care ar trebui să permită procesarea mai rapidă a tranzacției. Deoarece acest proces va reutiliza același nonce ca și tranzacția originală, nu trebuie să plătești gas de două ori.


Reține că **accelerarea tranzacției va crește suma pe care o cheltui pentru tranzacție**.


 


**Anularea unei tranzacții - Metoda 1: anulare în aplicație**
-------------------------------------------------------------


Dacă nu ai făcut acest lucru deja, pentru a anula tranzacția, pur și simplu apasă butonul **“Anulare”**, ca în captura de ecran de mai sus. Te rugăm să reții că **poți încerca să *anulezi* o tranzacție numai dacă aceasta este încă în așteptare în rețea.**Tranzacțiile care au fost deja confirmate nu pot fi anulate.


 


**Anularea unei tranzacții - Metoda 2: Nonce personalizat**
-----------------------------------------------------------


Acest proces implică efectuarea unei noi tranzacții cu același nonce (un număr de identificare al fiecărei tranzacții, derivat din sintagma „number only used once” adică „număr folosit o singură dată”). Tranzacția nu trebuie să aibă nicio valoare -- de ex. ai putea trimite 0 ETH. Ceea ce contează este să plătești suficient gas pentru ca rețeaua să-i acorde prioritate. 


Când utilizezi această metodă **va trebui să începi de jos în sus, de la cea mai veche tranzacție în așteptare din coada pe care dorești să o anulezi**. De exemplu, nu poți anula o tranzacție care are nonce 10 înainte de a anula nonce 9. 


 *Capturile de ecran de mai jos au fost făcute în momente diferite, așa că taxele de gas afișate pot varia, chiar și de la un pas la altul. Nu te îngrijora! Când faci tu însuți acest lucru, MetaMask se va actualiza automat în timp real pentru a afișa cursul pieței.*




Extensie Mobil


1. În setări avansate, activează **Personalizează nonce-ul tranzacției****.** Trebuie activat pentru a putea trimite o tranzacție înlocuitoare (folosind același nonce).   


![MetaMask advanced settings](https://support.metamask.io/hc/article_attachments/14929539257883)
2. **Efectuază o tranzacție nouă**. Tranzacția nouă trimite-o **CĂTRE** tine, adică la adresa ta publică MetaMask. **Completează „Nonce Personalizat” cu același nonce ca tranzacția care este încă în așteptare**:


![Metamask custom transaction nonce Extension](https://support.metamask.io/hc/article_attachments/14731609986843)
3. Lângă taxa de gas afișată pe ecranul de confirmare a tranzacției, vei vedea un buton pe care scrie „Piață” (poate fi activat și „Scăzut” sau „Agresiv”, în funcție de ultima ta setare utilizată). Apasă pe acesta, apoi pe „Avansat” în partea de jos: 


![MetaMask advanced gas controls find](https://support.metamask.io/hc/article_attachments/14731706474011)


Pentru a te asigura că solicitarea ta de anulare este preluată cu prioritate și înainte de tranzacția originală, **va trebui să plătești mai mult pentru gas**. Urmează aceste instrucțiuni:


	* Setează **limita de gas** *comparabilă sau ușor mai mare* decât cea din tranzacția inițială.
	* Setează**taxa de prioritate (priority fee)** cu *cel puțin 10% mai mare* (în Gwei) decât taxa de gas a tranzacției inițiale (cea aflată în așteptare) (de exemplu, dacă tranzacția a avut o taxă de gas de 30 Gwei, setează taxa maximă de prioritate în tranzacția de înlocuire/anulare la 33-35 Gwei).
	* Asigură-te că **taxa ta maximă (max fee)** este cu cel puțin 30% mai mare decât taxa maximă a tranzacției pe care o înlocuiești. De exemplu, dacă taxa anterioară a fost de 150 Gwei, seteaz-o undeva la 200 Gwei, de data aceasta.Consultă un gas tracker, cum ar fi cel de la [Etherscan](https://etherscan.io/gastracker) sau [ETH Gas Station](https://ethgasstation.info/) pentru îndrumări cu privire la taxele maxime recomandate.




1. **În Setări > Avansat, activează „Personalizează nonce-ul tranzacției”.**
2. **Efectuează o tranzacție nouă.** În tranzacția nouă, trimite CĂTRE tine, adică la adresa ta publică MetaMask. **Completează „Nonce Personalizat” cu același nonce ca tranzacția care este încă în așteptare**.


Pentru a găsi setarea de nonce personalizat în aplicație, accesează ecranul de confirmare a tranzacției, care apare după ce ai introdus cantitatea de tokeni și destinatarul. Apasă „Editează” pentru a face modificări:


![MetaMask custom transaction nonce Mobile](https://support.metamask.io/hc/article_attachments/12927068442907)
3. Acum trebuie să te asigurați că setările tale de gas sunt configurate astfel încât tranzacția de înlocuire să fie procesată. În ecranul de confirmare a tranzacției, apasă pe valoarea evidențiată de gas:


![MetaMask advanced gas controls mobile](https://support.metamask.io/hc/article_attachments/12927041593755)


Acum accesează „Opțiuni avansate” din meniul care apare.
4. De aici, poți ajusta gas-ul cu precizie pentru a te asigura că tranzacția ta este preluată. Acum vei vedea un ecran care arată astfel:


![MetaMask advanced gas controls mobile](https://support.metamask.io/hc/article_attachments/12927063201691)


De aici, reglează setările de gas. Urmează aceste instrucțiuni pentru a te asigura că tranzacția ta este preluată:


	* Setează **limita de gas** *comparabilă sau ușor mai mare*  decât cea din tranzacția inițială.
	* Setează **taxa maximă de prioritate (max priority fee)** cu *cel puțin 10% mai mare* (în Gwei) decât taxa de gas a tranzacției inițiale (cea aflată în așteptare) (de exemplu, dacă tranzacția a avut o taxă de gas de 30 Gwei, setează taxa maximă de prioritate în tranzacția de înlocuire/anulare la 33-35 Gwei).
	* Asigură-te că **taxa ta maximă (max fee)** este *cu cel puțin 30% mai mare* than the max fee of the transaction you're replacing. decât taxa maximă a tranzacției pe care o înlocuiești. De exemplu, dacă taxa anterioară a fost de 150 Gwei, setează-o undeva la 200 Gwei, de data aceasta.Consultă un gas tracker, cum ar fi cel de la [Etherscan](https://etherscan.io/gastracker) or [ETH Gas Station](https://ethgasstation.info/) pentru îndrumări cu privire la taxele maxime recomandate.



