*Notă: permisiunile contractelor smart sunt diferite față de simpla conectare a portofelului la un dapp (aplicații descentralizate). Pentru informații despre cum să-ți deconectezi portofelul de la dapp-uri [vezi acest articol](https://support.metamask.io/hc/en-us/articles/360059535551).*


Aprobările pentru tokeni și contractele smart **permit dapp-urilor să acceseze și să trimită tokeni din portofelul tău**. Când folosești un DEX (exchange descentralizat), de exemplu, ai nevoie să semnezi o aprobare ce permite unui contract smart să ia din tokenii tăi pentru a finaliza cererea ta de schimb. Chiar dacă sună riscant, ia aminte că este necesar sa oferi *anumite* permisiuni dapp-urilor. Dacă vrei să fii utilizator în web3, nu ai cum să eviți această operațiune. 



#### Revocarea permisiunii versus deconectarea aplicațiilor: care este diferența?


Este ușor să confundăm aceste două procese, dar ele sunt fundamental diferite:


* **Deconectarea portofelului** de la un dapp implică anularea permisiunii acestui dapp de a-ți vedea adresa publică și tokenii din portofel și oprește inițierea tranzacțiilor de către acea aplicație. Vezi  [acest aricol](https://support.metamask.io/hc/en-us/articles/360059535551) pentru mai multe informații.
* **Revocarea aprobărilor** se referă la anularea accesului unei aplicații la fondurile din portofelul tău (tokeni), aceștia nemaiputând fi trimiși de acea aplicație.


Vezi și: [postarea noastră pe Twitter](https://twitter.com/MetaMask/status/1499848000549515265) ce explică diferențele dintre aceste două acțiuni și [articolul despre aprobările tokenilor](https://support.metamask.io/hc/en-us/articles/6174898326683). 



**Cum revoci (elimini) aprobările tokenilor?**
----------------------------------------------


Vestea bună este că sunt mai multe metode de a verifica și anula aceste aprobări asupra tokenilor tăi.


* **Mergi la secțiunea "approval checker"**  pe blockchain explorer-ul rețelei folosite de tine. De exemplu, [Etherscan](https://etherscan.io/tokenapprovalchecker), [BscScan](https://bscscan.com/tokenapprovalchecker) și [Polygonscan](https://polygonscan.com/tokenapprovalchecker) toate au această funcție.
* Folosește platforme precum:
	+ [Revoke](https://revoke.cash/) (mai multe rețele)
	+ [Unrekt](https://app.unrekt.net/) (mai multe rețele)
	+ [approved.zone](https://approved.zone/) (rețeaua principală Ethereum)
	+ [Cointool](https://cointool.app/approve/eth) (mai multe rețele)
	+ [beefy.finance](https://allowance.beefy.finance/) (rețeaua BSC/BNB Smart Chain)
	+ [EverRevoke](https://everrise.com/everrevoke/) (mai multe rețele).



#### Taxa de gas


Deoarece aprobările tokenilor sunt operații "on-chain" (pe rețea), anularea lor se întâmplă tot "on-chain". Asta înseamnă că trebuie să plătești gas pentru fiecare operațiune de eliminare a aprobărilor. 



Știm cum e, mereu vrei să încerci o aplicație nouă. Problema este că aceste aplicații (dapps) pot trece repede printr-o listă de operațiuni de acceptat, ce te pot pune într-o poziție vulnerabilă față de hackeri sau scammeri. De aceea e o idee bună **să dezvolți un obicei în a-ți verifica aprobările tokenilor periodic** și să le elimini pe cele care nu ți se par la locul lor.


Din păcate, aprobările tokenilor sunt o metodă de atac comună a hackerilor și scammerilor: hackerii pot câteodată să localizeze și să exploateze o vulnerabilitate a codului unui contract smart ([ce s-a întâmplat cu Wormhole](https://rekt.news/wormhole-rekt/), un bridge Ethereum <-> Solana, de exemplu) și scammerii pot interveni prin rugpulluri.


Asta se întâmplă deoarece, de obicei, aprobările de tokeni cer **acces nelimitat** la tokenii tăi. Dacă un hacker sau un proprietar de contract smart fraudulos este capabil să folosească această metodă, ei pot, teoretic, să-ți golească portofelul de fondurile (tokenii) la care tu i-ai dat access (prin token allowance). Pentru a combate asta [MetaMask îți permite să personalizezi aprobările tokenilor](https://support.metamask.io/hc/en-us/articles/6055177143579). 


Pentru o analiză mai detaliată despre cele menționate mai sus (aprobări de tokeni/permisiuni dapp-uri) vezi [articolul de pe blog](https://consensys.net/blog/metamask/the-seal-of-approval-know-what-youre-consenting-to-with-permissions-and-approvals-in-metamask/) sau [acest articole](https://kalis.me/unlimited-erc20-allowances/) scris de creatorul aplicației Revoke, menționată mai sus.

