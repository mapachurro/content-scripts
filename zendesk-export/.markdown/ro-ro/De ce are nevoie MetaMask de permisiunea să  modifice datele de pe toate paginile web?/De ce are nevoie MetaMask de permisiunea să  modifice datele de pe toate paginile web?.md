Când adaugi MetaMask în browser, este posibil să vezi o alertă care indică faptul că MetaMask are nevoie de permisiunea **"să citească și să modifice toate datele tale de pe site-urile web pe care le vizitezi"**:


![MetaMask install edge notification](https://support.metamask.io/hc/article_attachments/13271397337627)


*Această imagine a fost luată dintr-un proces de instalare pe Microsoft Edge; mesajul tău poate varia în funcție de browser și de sistemul de operare pe care îl utilizezi.*


 


### De ce are nevoie MetaMask de aceste permisiuni?


#### Context:


Aceste permisiuni se referă la **browsere web și la ceea ce are nevoie MetaMask pentru a funcționa pe ele**. Explicația este puțin tehnică, dar vom încerca să o păstrăm simplă.


MetaMask este un instrument care îți permite să interacționezi cu rețele blockchain, cum ar fi Ethereum. Aceste interacțiuni constau, la un nivel de bază, în trimitere de informații către acele rețele și obținerea de răspunsuri înapoi.


Dar Ethereum nu este doar un server web tradițional, care servește pagini web în HTML. Este o rețea descentralizată de computere care sincronizează informațiile și ține evidența activelor; nu face parte cu adevărat din internetul tradițional. Nu primește solicitări și nu trimite informații la fel cum o face un server care găzduiește un site web: **MetaMask are nevoie de permisiunea ta pentru a obține acele informații, deoarece în web3, *tu ești cel care deține controlul*.**


#### Cum funcționează


Să presupunem că te aflii pe o pagină care îți permite să emiți un NFT (mint). Iată ce se întâmplă, pas cu pas:


* Te conectezi cu MetaMask la aplicația descentralizată (dapp).
	+ Acest lucru îi permite aplicației descentralizate să știe care este adresa ta publică, de exemplu.
* Introduci informații pertinente — să zicem, anumite caracteristici pe care le dorești în NFT sau câte dorești.
* **Aplicația descentralizată (dapp-ul) în sine preia informațiile pe care le introduci,** le adună într-o tranzacție propusă sau într-o cerere de semnătură și le transmite către MetaMask.
* **Execuți cererea în MetaMask**, iar MetaMask o trimite în rețea
	+ Acest lucru necesită uneori mai multe semnături - de exemplu, autorizarea aplicației descentralizate să solicite cheltuirea tokenilor tăi și apoi autorizarea efectivă a emiterii NFT-ului (minting).
* Rețeaua primește cererea ta și execută mint-ul.
* **Dapp-ul este capabil să detecteze acea tranzacție** prin propria sa conexiune la rețeaua blockchain și îți afișează NFT-ul pe care l-ai emis.



#### Concluzia


**MetaMask nu citește sau schimbă, în niciun moment, informațiile de pe pagina web.**. Dapp-ul face toată munca de actualizare a informațiilor din blockchain.


Motivul pentru care MetaMask are nevoie de aceste permisiuni ample este, pur și simplu, pentru că browserele nu oferă nicio altă modalitate de a deschide un canal de comunicare între MetaMask și pagina web.



#### Browserele web tradiționale nu au fost create pentru date blockchain; de aceea a fost creat MetaMask, pentru a construi această funcționalitate în browser.


 


### Cum funcționează acest lucru la nivel tehnic?


Pentru a permite aplicațiilor descentralizate să acceseze o rețea blockchain, MetaMask trebuie să introducă un obiect JavaScript în fiecare pagină. Acest lucru permite aplicației descentralizate să acceseze blockchain-ul și să preia informații disponibile public specifice portofelului tău, cum ar fi NFT-urile pe care le deții, istoricul tranzacțiilor sau soldurile tokenilor. Pentru mai multe informații despre cum funcționează, [consultă documentația MetaMask](https://docs.metamask.io/guide/#new-dapp-developers). 


 


### De ce să vă cred?


Ai prins ideea! **Web3 înseamnă posibilitatea de a verifica personal ceea ce îți spun alții.**


Dacă nu ești încă convins, o modalitate bună de a experimenta și de a-ți gestiona browserul este să îți izolezi [MetaMask](https://support.metamask.io/hc/en-us/articles/360015289672-Sandboxing-MetaMask) într-un mediu de testare de tip sandbox: creează  [un profil separat de browser](https://support.metamask.io/hc/en-us/articles/12174759849371) astfel încât MetaMask să fie instalat doar acolo. Acest lucru îți va permite să te obișnuiești cu MetaMask și Web3 într-un mediu care este separat de identitatea ta web existentă și îți va oferi o mai mare liniște sufletească cu privire la ce are acces MetaMask.


Acestea fiind spuse, **MetaMask este sigur pentru navigare**; suntem lideri în industrie în securitate și dezvoltare open-source; pentru mai multe informații despre auditurile care au fost efectuate, consultă [pagina noastră de securitate](https://metamask.io/security/).


###  Bine ai venit — te alături celor peste 30 de milioane de utilizatori MetaMask din întreaga lume!

