
#### Ești nou în spațiul crypto și web3?


Accesează [MetaMask Learn](https://learn.metamask.io/) pentru o experiență de învățare simplă, concepută special pentru nou-veniți în web3. Este complet gratuit, disponibil în mai multe limbi și include instrumente utile cum ar fi simulări, pentru a te ajuta să capeți încredere în tine în timp ce utilizezi MetaMask. 



#### *Acest articol cuprinde explicații și linkuri către resurse despre tranzacții și de ce acestea eșuează; mai jos includem linkuri către scenarii comune de tranzacții nereușite și cum să le abordăm:*


* [Anatomia tranzacțiilor pe blockchain](#h_01G79J04D0EN1VD8VS7C7J7KD1)
* [Probleme comune](#h_01G79J09NWA8CGR4VYC2PT5B6Y)
* [Remedieri principale](#h_01G79J0J8JTRPM9MRB76EN1GPP)
* [Resurse adiționale și următorii pași](#h_01G79J0RP8ZMZ1V1SKQY70TXCT)
* [Întrebări frecvente](#h_01G79J18RBK27GZCF10CGN9GKP)


 


**Anatomia tranzacțiilor pe blockchain**
----------------------------------------


Când vorbim despre "tranzacțiile" dintr-o rețea publică blockchain, de obicei vorbim despre interacțiunile dintre două adrese; cu alte cuvinte, despre tokeni (fungibili sau non-fungibil) sau despre alte fonduri crypto care sunt "trimise" de la o adresă la alta. De asemena, există și "tranzacții interne", care reprezintă interacțiunile ce au loc între contractele smart și, în cea mai mare parte, nu intră în scopul acestui articol.



#### Vrei mai multe informații?


Pentru mai multe informații despre rețele blockchain și despre modul în care acestea funcționează în general, consultă [articolul introductiv de aici](https://support.metamask.io/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) și dacă identifici cuvinte necunoscute [glosarul nostru este mereu disponibil](https://consensys.net/knowledge-base/a-blockchain-glossary-for-beginners/).



Să clarificăm: de fapt nimic nu este *trimis* nicăieri. O rețea blockchain compatibilă cu contractele smart, precum Ethereum, are o serie de componente sau funcții. Una dintre acestea este ceea ce am numi un "computer": mașina virtuală Ethereum sau EVM, care este capabilă să ruleze programe ("contracte smart"). Cu toate acestea, pilonul sistemului este un *registru distribuit*: **imaginează-ți o foaie de calcul care conține fiecare adresă a portofelului Ethereum, unde fiecare adresă are o coloană pentru fiecare tip de fond crypto pe care îl deține.** 


Să ilustram printr-un exemplu: să zicem că Guillaume dorește să trimită o tranzacție către Dolores. Guillaume are 1.36 ETH în cont și plănuiește să îi trimită lui Dolores 0.5 ETH. Este o zi bună pentru Dolores, chiar și într-o piață în scădere. 


Guillaume deschide portofelul MetaMask, introduce adresa lui Dolores, configurează parametrii cu care este confortabil pentru plata gas-ului, și apasă pe "trimite".


În acest punct, tranzacția intră într-o stare temporară locală de așteptare, cunoscută sub numele de *local memory pool*sau *local mempool*. Tranzacția va fi apoi "preluată" de cel mai apropiat nod din rețea; în funcție de [setările de gas](https://support.metamask.io/hc/en-us/articles/360022895972-Using-advanced-gas-controls), ale lui Guillaume, tranzacția sa va fi prioritară (**cu cât Guillaume este mai dispus să plătească pe [unitatea de gas](https://support.metamask.io/hc/en-us/articles/4404600179227-User-Guide-Gas), cu atât tranzacția sa va fi procesată mai repede)** ), și propagată la alte noduri din rețea. Nodurile vor face munca de a verifica dacă Guillaume are ETH de cheltuit, iar apoi vor efectua efectiv "tranzacția": **registrul va fi modificat; va fi debitat 0,5 din soldul lui Guillaume și creditat lui Dolores.**


Tokenii ETH nu trec în sine prin rețea; nu există un email trimis de la computerul lui Guillaume către inboxul MetaMask al lui Dolores sau nimic de acest gen. Guillaume a trimis o cerere către rețea, **autentificat cu [cheile lui private, prin MetaMask](https://support.metamask.io/hc/en-us/articles/4404722782107-User-guide-Secret-Recovery-Phrase-password-and-private-keys)**, pentru a se debita din contul lui și a-l credita pe cel al lui Dolores; acest lucru s-a întamplat după ce procesul de verificare programat în protocoalele rețelei s-a încheiat. 


#### *Asta reprezintă o tranzacție: o cerere către registru pentru a realoca ceva de la o adresă la alta.*


 


**Când lucrurile dau greș**
---------------------------


Lucrurile dau greș din mai multe motive. De multe ori, ele sunt probleme "software": MetaMask are un bug, sau ceva a fost configurat greșit la rețeaua pe care încerci să o utilizezi; a existat o eroare de conectivitate.


O **problemă comună este că utilizatorul, în încercarea de a plăti mai puțin pentru tranzacție, stabilește o limită de gas foarte scăzută**, iar starea rețelei este atât de aglomerată încât nu există spațiu în nici un bloc pentru o astfel de tranzacție "ieftină", uneori pentru o perioadă foarte lungă de timp: în cele din urmă, această tranzacție va deveni "învechită" și va trebui să fie anulată de utilizator. 


**Dacă ai efectuat o tranzacție și nu a fost finalizată**, starea ei va fi afișată în MetaMask ca "în așteptarare” (pending). 


**Dacă ai efectuat o tranzacție și a eșuat, cauza cea mai probabilă este lipsa de gas**: "ai rămas fără gas"; cu alte cuvinte, tranzacția a avut un cost de gas care, multiplicat cu prețul gas-ului, a rezultat o cantitate totală de monedă nativă mai mare decât ce ai avut tu în portofel. 



#### Info


Pentru mai multe informații despre calcul de gas, consultă  [aici ghidul nostru despre gas](https://support.metamask.io/hc/en-us/articles/4404600179227-User-Guide-Gas).



Acest lucru se poate întâmpla din mai multe motive, dar un lucru de luat în considerare este ce fel de tranzacție încerci să efectuezi. Emiterea unui NFT în timpul orelor de vârf cu trafic în rețea pot fi foarte consumatoare de gas; dacă încerci o tranzacție nouă sau experimentală, poate merită să încerci pe o rețea de testare înainte de a plăti taxele dintr-o rețea în timp real.


 


**Remedierea problemei**
------------------------


### **Factorul cheie #1: Local sau apare pe rețea**


Pe măsură ce diagnostichezi problema tranzacției, mai ales când vine vorba de o tranzacție în așteptare, trebuie să verifici dacă tranzacția este încă în mempool-ul local sau dacă a ajuns în rețea și este blocată acolo din orice motiv. Dacă este doar în mempool local, soluția ar putea fi simpla blocare și deblocare a portofelului MetaMask (**înainte de a face ceva asigură-te că îți cunoști parola și că ai salvat fraza secretă de recuperare**). Dacă este blocată pe rețea, soluția ar putea fi mai complicată.


Pentru mai multe informații despre remedierea acestor probleme, consultă linkurile de mai jos.  
  



### **Factorul cheie #2: Nonce**


Acest cuvânt are diferite înțelesuri. Este o prescurtare pentru "număr folosit o singură dată" ("number only used once"), iar în acest context, înseamnă aproximativ "numărul tranzacției", începând de la prima tranzacție efectuată de adresa de trimitere. Poți să întâmpini o problemă serioasă dacă, spre exemplu, trimiți de la aceeași adresă din portofelul MetaMask două tranzacții diferite din instanțe MetaMask diferite, în același timp. **Tranzacțiile adresei tale trebuie să fie în ordine crescătoare în funcție de nonce-ul lor.**Cu toate acestea, așa cum nonce-urile sunt capabile să cauzeze blocarea unei tranzacții, pot fi și cheia care o deblochează.


Pentru mai multe informații despre această tehnică [vezi aici](https://support.metamask.io/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction).


 


**Următorii pași**
------------------


### *Dacă ai tranzacții eșuate sau tranzacții în așteptare, consultă următoarele resurse pentru asistență.*


#### [Cum să trimiți tokeni din portofelul MetaMask](https://support.metamask.io/hc/en-us/articles/360015488931)


#### [Cum să accelerezi sau să anulezi o tranzacție în așteptare](https://support.metamask.io/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction)


#### [De ce a eșuat tranzacția mea cu eroarea "fără gas" ("out of gas")?](https://support.metamask.io/hc/en-us/articles/360038849792-Why-did-my-transaction-fail-with-an-Out-of-Gas-error-How-can-I-fix-it-)


#### [Troubleshooting Uniswap](https://support.metamask.io/hc/en-us/articles/360053394291-Uniswap-support-and-troubleshooting-tips)


#### [Ghidul utilizatorului: Gas](https://support.metamask.io/hc/en-us/articles/4404600179227-User-Guide-Gas)


#### [Pot anula o tranzacție deja confirmată?](https://support.metamask.io/hc/en-us/articles/360059957352-Can-I-reverse-an-already-confirmed-transaction-)


 


**Întrebări frecvente**
-----------------------


#### 
*Î: Un cont din portofelul meu are o tranzacție în așteptare. Pot iniția o altă tranzacție dintr-un cont diferit în același portofel?*R: Da, poți. Nonce-ul se calculează per cont, nu per portofel.

