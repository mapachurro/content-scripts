Contractele smart sunt programe pe computer ce rulează în mașina virtuală Ethereum (EVM) și în blockchain-uri similare. Numele lor te poate induce în eroare: când interacționezi cu ele, tu nu semnezi un contract, ci doar anunți (comanzi) un program să ruleze. 


[Posibilitățile infinite](https://www.geeksforgeeks.org/what-is-meant-by-turing-complete-in-ethereum/) pentru funcțiile contractelor smart sunt ceea ce face Ethereum și web3 atât de puternic. Accesibilitatea lor este de asemenea, o caracteristică importantă: deoarece web3 este menit să fie descentralizat și accesibil tuturor, contractele smart pot fi create și implementate de oricine dorește. Inevitabil, unii încearcă să exploateze această libertate pentru a profita de alți utilizatori. 


De aceea trebuie să înveți cum să identifici un contract fraudulos și să te protejezi pentru a nu deveni o victimă a lui. 


Pentru clarificare, contractele smart pot reprezenta:


* Un token (ERC-20), ce este definit și controlat de un contract smart, sau o colecție de NFT-uri.
* O funcție în cadrul unei aplicații web3 (dapp), cum ar fi un program ce verifică schimburile de tokeni (swaps) sau chiar un mecanism DAO.


 


Conectare versus aprobare
-------------------------


Când folosești MetaMask în web3, vei fi atenționat adeseori să îți **conectezi** portofelul. Totodată, vei fi solicitat să **aprobi** anume operații. În acest context, aprobările sunt cele care te interesează: diferența este importantă!


* **Conectarea portofelului** la un site nu îi permite acestuia să facă nimic cu fondurile tale decât dacă ești de acord în mod expres. Deci, deși această conexiune va permite unei aplicații descentralizate (dapp) să îți propună anumite tranzacții sau acțiuni, nimic nu se va întâmpla cu fondurile tale decât dacă aprobi tranzacțiile care sunt sugerate. Citește mai multe despre conectarea portofelului [aici](https://support.metamask.io/hc/en-us/articles/360059535551).
* Spre deosebire, **aprobările**, implică acordarea unui contract smart capacitatea de a interacționa cu un anumit token, într-o anumită cantitate, (așa cum și atunci când o solicită.) Ar trebui să te oprești mereu și să te gândești atunci când ți se cere să aprobi ceva, deoarece, în general, implică oferirea controlului asupra tokenilor tăi unui contract smart care ar fi putut fi scris de oricine. Citește mai multe [aici](https://support.metamask.io/hc/en-us/articles/6174898326683).



Cum verific dacă un contract smart este de încredere
----------------------------------------------------


Să trecem în listă câteva lucruri ce trebuie luate în considerare când verifici un contract smart:


1. **Îți cere să aprobi accesul la tokenii tăi?**?
	* În afară de ingineria socială pentru a obține expresia secretă de recuperare ([învață cum să fii în siguranță](https://support.metamask.io/hc/en-us/articles/360060826432)), escrocheriile de aprobare a tokenilor sunt unul dintre cei mai frecvenți vectori de atac din web3. Acesta este motivul pentru care le-am explicat pe scurt mai sus. Dacă ești de acord ca aprobarea unui token să fie folosit de un dapp, îi oferi controlul asupra oricărui token (și *cantității* din acel token) pe care îl aprobi. **Numai asta ar trebui să te facă să te gândești de două ori.**
	* Are sens ca dapp-ul să solicite acces la acel token? Este relevant pentru funcționalitatea aplicației pe care intenționezi să o utilizezi?
	* Cantitatea de tokeni solicitată este corectă? Reține că multe aplicații populare solicită acces la o cantitate practic infinită de tokeni pentru a preveni nevoia de a semna (și plăti pentru) numeroase tranzacții în viitor. Citește mai multe [aici](https://support.metamask.io/hc/en-us/articles/6174898326683).
2. **Caută adresa în blockchain explorer-ul relevant**. Toate contractele smart au o adresă. Orice dapp de renume, colecție NFT sau altă parte ar trebui să facă această adresă disponibilă ușor; fie direct pe site-ul lor principal, fie în documente. MetaMask îți va arăta, de asemenea, adresa contractului smart înainte de a semna orice tranzacție care îl implică.


Introdu adresa în bara de căutare a [blockchain explorer-ului](https://support.metamask.io/hc/en-us/articles/360057536611). Multe dintre acestea, inclusiv Etherscan, îți vor spune când codul este verificat sau nu, așa cum este evidențiat mai jos. De asemenea, poți verifica și numele contractului, dacă există — dacă nu există, ar putea fi ori foarte nou, ori nedemn de încredere. 


![Smart contract verification Etherscan](https://support.metamask.io/hc/article_attachments/13306514521371)


De asemenea, poți verifica secțiunea de comentarii din blockchain explorer pentru o indicație a sentimentului utilizatorului. Nu te baza 100% pe asta deoarece ar putea fi influențat de factorii frauduloși înșiși.
3. **Utilizează site-uri de listare a monedelor/tokenilor pentru a verifica un token**. Accesează [Coingecko](https://www.coingecko.com/), de exemplu, și introdu numele sau adresa tokenului. Ar trebui să poți vedea detalii relevante despre token, cum ar fi site-ul web al proiectului și rețelele sociale ale acestora. Aici poți verifica dacă dapp/tokenul/proiectul are o comunitate autentică, activă, care nu este doar plină de roboți, sau poți căuta un “whitepaper” (carte albă) pe site-ul lor care să demonstreze că nu este doar un [rugpull](https://support.metamask.io/hc/en-us/articles/4407169552667) în așteptare. Ghidul nostru pentru [practici de siguranță pentru tokeni](https://support.metamask.io/hc/en-us/articles/4403988839451) este, de asemenea, foarte util în acest context.
4. **Verifică activitatea recentă a contractului**. Uită-te la tranzacțiile recente enumerate pe pagina contractului smart din blockchain explorer. Deși informația de aici poate fi copleșitoare, încearcă să te concentrezi pe **identificarea tiparelor** și apoi întreabă de ce ar putea exista acel model. O practică frauduloasă obișnuită, de exemplu, este de a împiedica deținătorii și cumpărătorii de tokeni să vândă un token — așa că, dacă nu vezi nicio tranzacție de *vânzare*, este posibil să te uiți la o înșelătorie honeypot sau similară.


Din păcate, nu există nicio modalitate de a fi 100% sigur de legitimitatea unui contract smart, fără a petrece multe ore familiarizându-te cu Solidity și limbajele de codare aferente, astfel încât să le poți verifica singur. 


**Așa că merită repetat: acționează întotdeauna cu prudență în web3**. Dacă nu ești sigur de un anumit site sau ai întrebări suplimentare, contactează-ne prin intermediul butonului "Începe o conversație" de pe pagina de pornire a acestui site. 

