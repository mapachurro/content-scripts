
#### Ești nou în spațiul crypto și web3?


Accesează [MetaMask Learn](https://learn.metamask.io/) pentru o experiență de învățare simplă, concepută special pentru nou-veniți în web3. Este complet gratuit, disponibil în mai multe limbi și include instrumente utile cum ar fi simulări, pentru a te ajuta să capeți încredere în tine în timp ce utilizezi MetaMask. 



Gas-ul este unitatea de măsură folosită pentru a determina efortul de calcul necesar procesării tranzacțiilor și a contractelor smart. În esență, o taxă de tranzacție, termenul provine de la Ethereum, se referă la calculele efectuate pe mașina virtuală Ethereum (EVM). De când s-a fondat Ethereum au apărut numeroase rețele compatibile cu EVM (și incompatibile cu EVM!) și au adoptat modele similare.


Folosind analogia combustibilului care alimentează un motor de mașină, gas-ul reprezintă costul de operare: fluctuant și, uneori, costisitor. Contractele smart mai complexe necesită mai mult gas pentru a-și alimenta efortul de calcul, la fel cum o mașină mai mare și mai puternică necesită mai mult combustibil pentru a rula.


Metoda de a calcula taxa de gas variază în funcție de rețea. De exemplu, calcularea gas-ului pe Ethereum era foarte complicată, dar a fost simplificată considerabil odată cu implementarea Protocolului de îmbunătățire Ethereum (EIP) 1559 în august 2021 (cunoscut și sub numele de London Upgrade). În esență, plătești o taxă de bază pentru fiecare unitate de gas, care este ***arsă*** (a se citi: este șters și dispare) la finalizarea cu succes a tranzacției. Pe lângă taxa de bază, adaugi o **taxă de prioritate,** per unitate de gas, a cărei valoare depinde de cât de repede dorești să se efectueze tranzacția. 


În toată gama de rețele compatibile EVM disponibile, gas-ul sau alternative care funcționează similar, au devenit practic metoda standard de calcul a costurilor de tranzacție. Taxele sunt plătite în tokenul nativ al rețelei: de exemplu, orice tranzacție pe Ethereum necesită ETH; utilizarea BSC necesită BNB; utilizarea Polygon necesită MATIC. Unele rețele au adoptat modelul EIP-1559 de la Ethereum, cum ar fi Polygon, în timp ce altele au făcut ajustări, inclusiv Avalanche pentru C-Chain-ul lor (care arde [atât taxa de bază, cât și taxa de prioritate;](https://docs.avax.network/learn/platform-overview/transaction-fees/#c-chain-fees) deci nu numai prima).  


Dacă dorești să aprofundezi modul în care funcționează gas-ul pe Ethereum, vezi [aici](https://ethereum.org/en/developers/docs/gas/). 


 


Iată câteva **detalii esențiale despre cum functionează gas-ul** **în MetaMask**:


#### **Limita de gas (unități de gas utilizate)**


*Limita de gas* este **numărul maxim de unități de gas pe care ești dispus să le plătești** pentru a efectua o tranzacție sau o operațiune EVM. Operațiuni diferite necesită cantități diferite de unități de gas. O tranzacție normală care trimite ETH sau un token costă în mod normal 21.000 de gas, în timp ce o aprobare de token ERC-20 necesită 45.000. Multe rețele, cum ar fi blockchain-ul compatibil EVM Harmony, folosesc un model identic în care tranzacțiile standard costă tot **21.000** de gas. 



#### Trebuie să editez limita de gas?


Nu! MetaMask stabilește automat limita de gas în funcție de tranzacția pe care încerci să o execuți. În marea majoritate a cazurilor, acest lucru va fi adecvat pentru a finaliza tranzacția. Dacă dorești să o verifici sau să o editezi, asigură-te că ai [controlul avansat de gas activ](https://support.metamask.io/hc/en-us/articles/360022895972) și apasă butonul din dreptul informatiilor despre gas, in ecranul de confirmare a tranzacției. Acesta este situat sub butoanele: "Market", "Minim', "Agresiv".



#### **Taxa de bază**


Fiecare bloc din rețeaua Ethereum are o taxă de bază determinată de cererea de pe rețea: taxa de bază se bazează pe dimensiunea blocului dinaintea acestuia, în comparație cu dimensiunea unui bloc țintă (unde dimensiunea se referă la cantitatea totală de gas utilizată pentru toate tranzacțiile pe care blocul le include). Dacă dimensiunea blocului anterior depășește ținta, taxa de bază pentru următorul bloc crește cu 12,5%, lăsându-te pe tine utilizatorul (sau portofelul tău) cu o certitudine absolută cu privire la taxa de bază a blocului viitor. Taxa totală de gas trebuie să respecte acest preț ca și minim, pentru a fi luată în considerare pentru includerea în bloc. 


#### **Taxa de prioritate**


*Taxa de prioritate*, denumită și „bacșișul minerului”, îl determină pe miner să prioritizeze tranzacția ta. 


Bineînțeles, dacă acest lucru ajunge într-adevăr unui miner depinde de [mecanismul de consens](https://support.metamask.io/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) rețeaua principală Ethereum a devenit o rețea Proof of Stake în urma fuziunii din Septembrie 2022, așa că taxa de prioritate revine validatorilor, nu minerilor. 


#### **Taxa maximă**


Taxa maximă este suma totală, globală, plătită pentru tranzacția ta. Se calculează în felul următor: **(taxa de bază + taxa de prioritate)** x unități de gas utilizate. MetaMask setează inițial această sumă pe baza istoricului blocului anterior. Cu toate acestea, utilizatorii pot edita această sumă prin setări personalizate (vezi mai jos). Diferența dintre taxa maximă per gas și (taxa de bază + taxa de prioritate maximă per gas) este „rambursată” utilizatorului.


 


### **Concepte Suplimentare**


#### **Gwei**


Gwei este o unitate de ether, cea mai mică denominație, care înseamnă [gigawei](https://ethgasstation.info/blog/gwei/) (sau 1,000,000,000). [Gwei](https://www.investopedia.com/terms/g/gwei-ethereum.asp) Gwei este folosit pentru taxele de gas, sau mai degrabă plățile efectuate de utilizatori pentru a compensa efortul de calcul necesar procesării și validării tranzacțiilor pe blockchain-ul Ethereum. 


Alte rețele tind, de asemenea, să calculeze costurile folosind gwei - de exemplu, Fantom, Harmony și Avalanche.


#### **Slippage**


Slippage-ul este diferența procentuală între un preț cotat și un preț executat.


#### **Taxa de gas**


*Taxa de gas* se referă la taxa de tranzacție pe blockchain-ul Ethereum. Este ceea ce plătesc utilizatorii pentru ca tranzacția lor să fie validată sau finalizată.


#### **Taxa de bază**


Generat de către protocol. Reprezintă multiplicatorul minim „gasUtilizat” necesar pentru ca o tranzacție să fie inclusă într-un bloc (adică pentru ca o tranzacție să fie finalizată). Aceasta este partea din costul tranzacției care este arsă.


 


### **Control avansat de gas**


Dacă dorești să intri mai detaliat în cotrolul de gas (acest lucru poate fi util dacă testezi un dapp, de exemplu), MetaMask poate face asta! Vezi articolul complet [aici](https://support.metamask.io/hc/en-us/articles/360022895972).


 


### **Întrebări Frecvente**


[De ce am plătit gas pentru o tranzacție eșuată?](https://support.metamask.io/hc/en-us/articles/360045439051) 


[Puteți returna taxa de gas?](https://support.metamask.io/hc/en-us/articles/360058370012)


[Cum accelerezi sau anulezi o tranzacție în așteptare?](https://support.metamask.io/hc/en-us/articles/360015489251) 


[Cum estimezi taxa de gas?](https://support.metamask.io/hc/en-us/articles/360059562111) 


[De ce sunt atât de mari taxele de gas?](https://support.metamask.io/hc/en-us/articles/360058751211-Why-my-gas-fees-are-so-high-)


[Eroarea: [ethjs-query] de tranzacție cu preț prea mic](https://support.metamask.io/hc/en-us/articles/4402538041869)


[Cum să corectezi eroarea "fonduri insuficiente"](https://support.metamask.io/hc/en-us/articles/360044703372)


 


 

