*Rezumat: MetaMask îți permite să editezi manual numărul de tokeni pe care aplicațiile descentralizate (dapp-uri) îl pot accesa. [Apasă aici](#h_01G3E1JE4CPVP1VH8PFS4FH25P) pentru a vedea pașii.*


 


Care este scopul permisiunilor tokenilor?
-----------------------------------------


Atunci când interacționezi cu o aplicație descentralizată (dapp) care implică deținerea tokenilor tăi ERC-20, într-un fel sau altul este posibil să trebuiască să aprobi accesul la contractul smart al acelui token (același lucru este valabil pentru echivalenții ERC-20 din alte rețele, cum ar fi BEP-20 în rețeaua BNB). Apoi, când decizi, spre exemplu, să adaugi 1.000 de tokeni A și 1.000 de tokeni B într-un fond de lichiditate,  dapp-ul *deja* are permisiunea ta pentru a lua cantitatea necesară de tokeni direct din portofelul tău și tot ce trebuie să faci este să confirmi tranzacția.


Permisiunile tokenilor sunt specifice unui singur token. Asta înseamnă că dacă ai acordat permisiunea unui dapp să-ți acceseze tokenul USDT, de exemplu, acesta poate accesa *doar* USDT.


În cele mai multe cazuri, permisiunile tokenilor depășesc ce ai nevoie pentru orice tranzacție unică și sunt foarte convenabile; ar fi o pierdere de timp să oferi permisiune pentru fiecare tranzacție nouă pe care dorești să o faci într-un dapp. Preaprobarea simultană a accesului la un număr de tokeni este așadar, caracteristică esențială, care face ca activitățile în web3 să fie mai ușoare.


Personalizarea aprobărilor tokenilor în MetaMask
------------------------------------------------


Pentru a păstra controlul și autoritatea, pe lângă faptul că îți oferă instrumentele pentru a te proteja de  [una dintre cele mai comune înșelătorii](https://consensys.net/blog/metamask/the-seal-of-approval-know-what-youre-consenting-to-with-permissions-and-approvals-in-metamask/#:~:text=Token%20approvals%20are,intention%20of%20stealing.)  din acest spațiu, MetaMask îți permite să personalizezi accesul aplicațiilor descentralizate la numărul de tokeni. 


Cum? Atunci când întâlnești o cerere pentru a permite accesul la tokenii tăi, va apărea o fereastră de aprobare în MetaMask. Verifică secțiunile de mai jos pentru a vedea cum arată pe mobil și extensie.




Extensie Mobil


Când ți se solicită să semnezi o permisiune pentru un token, MetaMask va afișa fereastra de mai jos și îți va cere să setezi un plafon de cheltuieli pentru token:


![Custom spending cap extension](https://support.metamask.io/hc/article_attachments/13635781517467)


Am proiectat această interfață pentru a-ți oferi control și vizibilitate asupra permisiunilor tokenilor, din moment ce ți se va solicita să introduci *întotdeauna* o limită, mai degrabă decât suma implicită propusă de aplicația descentralizată (deși, dacă vrei, poți selecta aprobarea prestabilită).


Tot ce trebuie să faci este să introduci cantitatea necesară cu care ești confortabil. Dacă nu ești sigur accesează [articolul despre aprobările tokenilor](https://support.metamask.io/hc/en-us/articles/6174898326683) pentru mai mult context. Accesează "următorul" pentru a te muta pe ecranul secundar, unde îți vezi din nou limita:


![Custom spending cap extension](https://support.metamask.io/hc/article_attachments/13635781542939)


Când ești pregătit, apasă pe "aprobare" pentru a finaliza.




La orice interacțiune cu un dapp care necesită persimisune pentru un token, va apărea un ecran pe care este afișat: "Oferi permisiunea să acceseze [tokenul]?" ("Give permission to access your [token]?"). Sunt multe informații în acesta fereastră, dar butonul care ne interesează este cel de sus, "Editează permisiunea" ("Edit permission")


![Custom spending cap mobile](https://support.metamask.io/hc/article_attachments/13636146897691)


Dacă apeși "Editează permisiunea"("Edit permission"), vei vedea:


* Limita propusă: Acesta este numarul de tokeni pe care dapp-ul ți-l cere să-l aprobi. Uneori poate fi astronomic.
* Limita personalizată: Aici vei introduce numarul de tokeni la care vrei sa dai acces dapp-ului.


![Custom spending cap mobile](https://support.metamask.io/hc/article_attachments/13636173265179)


Introdu limita dorită în acest câmp și apoi urmeaza pașii pentru a finaliza procesul.




 


Fii în siguranță
----------------


Permisiunile tokenilor sunt parte esențială a web3, iar emiterea virtuală nelimitată a aprobărilor nici nu este problematică în sine: de cele mai multe ori, îți va face viața mai ușoară și reduce cantitatea de gas pe care o plătești (pentru că trebuie să plătești pentru fiecare aprobare separat). Cu toate acestea, dapp-urile sunt rareori complet ferite de exploatare și încercări de atac cibernetic, iar având aprobări ale tokenilor nelimitate te expune riscului de atac. Dacă dapp-ul are o vulnerabilitate în codul lui, poate fi posibil ca răufăcătorii să exploateze și să comande ca dapp-ul să sustragă fondurile fără ca tu să soliciți.


De asemeneal, este posibil ca site-ul de la care se solicită aprobarea tokenului să aparțină unui site malițios. This is the more common form of attack: you visit a site designed to look like another, more trustworthy site or brand, and it's this trust that gets exploited. In these cases, your tokens can be stolen as soon as you send the approval transaction.


Pentru a preveni să devii o victimă, există **două metode posibile** pe care le poți adopta:


1. Niciodată să nu permiți aprobări nelimitate (sau foarte mari).
2. Să oferi aprobări nelimitate site-urilor de încredere doar câteodată, dar [să verifici frecvent](https://support.metamask.io/hc/en-us/articles/4446106184731) cine are acces la tokenii tăi.


Ambele sunt viabile, dar **opțiunea 1 este cea mai sigură**.


Adițional, ar trebui să **realizezi mereu [o analiză detaliată](https://consensys.net/blog/metamask/the-seal-of-approval-know-what-youre-consenting-to-with-permissions-and-approvals-in-metamask/#:~:text=You%E2%80%99ll%20often%20see,short%20time%20periods.)** pentru fiecare site căruia îi oferi aprobare. Câteodată, dacă dapp-ul în sine a fost emis de către un răufăcător pentru a-ți sustrage fondurile, nici nu trebuie să te exploateze ca să te transforme în victimă: de îndată ce apeși "aprobare" pe token, ei îți pot goli portofelul de acel token. Pentru mai multe informații despre acest subiect, accesează topicul nostru [Twitter](https://twitter.com/MetaMask/status/1499848729615949824).


Pentru mai multe informații despre aprobările tokenilor, vezi mai multe resurse:


* [Vezi postarea din blogul nostru](https://consensys.net/blog/metamask/the-seal-of-approval-know-what-youre-consenting-to-with-permissions-and-approvals-in-metamask/)
* [Cum să revoci aprobările contractelor smart/ tokenilor](https://support.metamask.io/hc/en-us/articles/4446106184731)
* [Ce este o aprobare de token?](https://support.metamask.io/hc/en-us/articles/6174898326683)
