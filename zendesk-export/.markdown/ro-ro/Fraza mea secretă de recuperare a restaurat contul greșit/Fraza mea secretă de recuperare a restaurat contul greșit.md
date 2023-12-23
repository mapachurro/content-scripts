
#### Notă:


* Un mesaj important din partea echipei MetaMask cu privire la această problemă poate fi găsit [aici](https://community.metamask.io/t/restored-metamask-no-coins-are-showing/878/107?u=jacob.cantele).
* Pentru informații de bază despre fraza secretă de recuperare (SRP) din MetaMask, consultă ghidul nostru de utilizare [aici](https://support.metamask.io/hc/en-us/articles/4404722782107).



Presupunând că folosești fraza secretă de recuperare corectă (ce poate restaura conturi multiple) sau o cheie privată (ce poate restaura doar un singur cont atunci când este [importată](https://support.metamask.io/hc/en-us/articles/360015489331)), este imposibil să restaurezi contul greșit. Verifică dacă următoarele se aplică și în cazul tău. 


Dacă întâmpini această problemă, cele mai frecvente motive sunt: 


1. **Fraza secretă de recuperare pe care o ai în prezent nu e asociată contului care îți lipsește.**Cu alte cuvinte: ai SRP-ul greșit.
2. **Contul care îți lipsește a fost un cont secundar creat sub fraza secretă de recuperare pe care o ai în prezent.**


Pentru a verifica dacă acesta este cazul, utilizează <https://danfinlay.github.io/mnemonic-account-generator/> pentru a genera între 10 și 100 de conturi și verifică dacă în lista respectivă apar conturile lipsă.


(Ține minte că generatorul va returna adrese de cont *fără* 0x la început, deci, dacă ai copiat o adresă care *are* prefixul 0x, căutarea în listă nu va produce rezultate.)  



Dacă se află contul în acea listă, îl poți restaura în MetaMask urmând instrucțiunile [de aici](https://support.metamask.io/hc/en-us/articles/360015489271).
3. **Fraza secretă de recuperare pe care o ai a fost generată inițial de un alt furnizor de portofel.**


Dacă simți că acesta ar putea fi cazul, încearcă să-ți restabilești contul folosind acei furnizori de portofel pentru a verifica dacă ai acces la contul lipsă.
4. **Contul lipsă a fost importat folosind o cheie privată.** 


Acesta este un [cont importat](https://support.metamask.io/hc/en-us/articles/360015289932-What-are-imported-accounts-). În acest caz, singura modalitate de a accesa contul este re-importarea acestuia folosind cheia privată.
5. **Fraza secretă de recuperare a fost scrisă greșit sau este introdusă incorect la restaurare.**


O problemă frecventă este scrierea de mână (un scris neciteț al frazei secrete de recuperare); altă problemă este scrierea cuvintelor în *ordine greșită*. Cuvintele trebuie să fie în ordinea în care au fost prezentate inițial.
6. **Fraza secretă de recuperare restaurează de fapt contul, dar ceea ce lipsește sunt tokenii personalizați care trebuie adăugați din nou.** 


Poți urma pașii de [aici](https://support.metamask.io/hc/en-us/articles/360015489031-How-to-View-See-Your-Tokens-and-Custom-Tokens-in-Metamask) pentru a-i adăuga din nou.
