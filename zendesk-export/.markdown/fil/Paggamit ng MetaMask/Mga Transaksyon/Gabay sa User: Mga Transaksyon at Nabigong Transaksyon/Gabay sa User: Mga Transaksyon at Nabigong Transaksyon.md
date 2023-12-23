
#### Baguhan sa crypto at web3?


Pumunta sa [MetaMask Learn](https://learn.metamask.io/) para sa isang simpleng karanasan sa pagkatuto na partikular na dinisenyo para sa mga baguhan sa web3. Libre ito, available sa maraming wika, at may kasamang kapaki-pakinabang na tools gaya ng mga simulation para tulungan kang maging pamilyar sa MetaMask.



#### *Binubuo ang artikulong ito ng paliwanag at mga link sa mga mapagkukunang tumatalakay sa mga transaksyon at kung bakit nabibigo ang mga ito, at higit pa sa ibaba, mga link sa mga karaniwang scenario ng nabigong transaksyon at kung paano tugunan ang mga ito:*


* [Anatomy ng isang blockchain transaction](#h_01G79J04D0EN1VD8VS7C7J7KD1)
* [Mga karaniwang problema](#h_01G79J09NWA8CGR4VYC2PT5B6Y)
* [Mga pangunahing remedyo](#h_01G79J0J8JTRPM9MRB76EN1GPP)
* [Mga karagdagang mapagkukunan at mga susunod na hakbang](#h_01G79J0RP8ZMZ1V1SKQY70TXCT)
* [Mga FAQ](#h_01G79J18RBK27GZCF10CGN9GKP)


 


**Anatomy ng isang blockchain transaction**
-------------------------------------------


Kapag pinag-uusapan natin ang tungkol sa 'mga transaksyon' sa isang pampublikong network ng blockchain, kadalasang pinag-uusapan natin ang mga pakikipag-ugnayan sa pagitan ng dalawang address; sa madaling salita, mga token, ito man ay magagamit o hindi, o iba pang mga crypto-asset na 'ipinadala' mula sa isang address patungo sa isa pa. Mayroon ding mga transaksyon na tinutukoy bilang "mga panloob na transaksyon", na mga pakikipag-ugnayan na nagaganap sa pagitan ng mga matalinong kontrata, at sa karamihan ay nasa labas ng saklaw ng artikulong ito.



#### Gusto ng higit pang impormasyon?


Para sa higit pa tungkol sa mga blockchain network at kung paano gumagana ang mga ito sa pangkalahatan, tingnan ang aming [panimulang artikulo rito](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-), at kung natigil ka sa anumang hindi pamilyar na mga salita, ang aming [glossary ay palaging magagamit](https://consensys.net/knowledge-base/a-blockchain-glossary-for-beginners/).



Para sa kapakanan ng kalinawan, wala talagang *pinapadala* kahit saan. Ang isang blockchain network na pinagana ng smart contract gaya ng Ethereum ay may ilang iba't ibang bahagi, o mga function. Isa sa mga ito ang kung tawagin natin ay isang "computer": ang Ethereum Virtual Machine, o EVM, na may kakayahang magpatakbo ng mga program ('mga smart contract'). Ang backbone ng sistema, gayunpaman, ay isang *distributed ledger*: **isipin ang isang spreadsheet na naglalaman, sa isang panig, ng bawat isang Ethereum wallet address, at bawat address ay may column para sa bawat uri ng crypto-asset na hawak nito.** 


Gamitin natin ang isang halimbawa para sa ilustrasyon. Sabihin na gusto ni Guillaume na magpadala ng transaksyon kay Dolores. Si Guillaume ay may 1.36 ETH sa kanyang account, at plano niya na magpadala kay Dolores ng 0.5 ETH. Mukhang isang magandang araw para kay Dolores, kahit sa isang bear market. 


Binuksan ni Guillaume ang kanyang MetaMask wallet, ipinasok ang address ni Dolores, kino-configure ang mga parameter ng gas na komportable siyang bayaran, at pinindot ang 'ipadala'.


Sa puntong ito, papasok ang transaksyon sa isang lokal na status ng pansamantalang paghawak, na kilala bilang *lokal na memory pool,* o*lokal na mempool*. Ang transaksyon ay 'kukunin' ng pinakamalapit na node sa network; depende sa [mga gas setting](https://metamask.zendesk.com/hc/en-us/articles/360022895972-Using-advanced-gas-controls) ni Guillaume, uunahin ang transaksyon niya (**miyentras mas handang magbayad si Guillaume kada [yunit ng gas](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas), mas mabilis maproseso ang transaksyon niya**), at maipalaganap sa ibang node sa network. Gagawin ng mga node ang gawain ng pag-verify na si Guillaume ay may ETH na gagastusin, at pagkatapos ay aktwal na gagawa ng 'transaksyon': **ang ledger ay mababago; 0.5 ay ide-debit mula sa balanse ni Guillaume, at 0.5 ay i-credit kay Dolores'.**


*'Ang gumagalaw na kamay, matapos magsulat, ay lilipat na':* Ang ETH ay hindi lumipat sa isang network; hindi ito isang email na ipinadala mula sa computer ni Guillaume sa inbox ng MetaMask ni Dolores o anumang uri. Nagpadala si Guillaume ng kahilingan, **na pinatotohanan ng kanyang [mga pribadong key sa pamamagitan ng MetaMask](https://metamask.zendesk.com/hc/en-us/articles/4404722782107-User-guide-Secret-Recovery-Phrase-password-and-private-keys)**, sa network upang i-debit ang kanyang account at i-credit si Dolores', at pagkatapos ng proseso ng pag-verify na na-program sa mga protocol ng network, natapos na ito.


#### *Iyon lang ang isang transaksyon: isang kahilingan sa ledger na muling italaga ang isang bagay mula sa isang address patungo sa isa pa.*


 


**Kapag nagkamali ang mga bagay**
---------------------------------


Maaaring magkamali ang mga bagay sa maraming kadahilanan. Kadalasan, ang mga ito ay 'dahilan sa software': May bug ang MetaMask, o may mali sa pagkaka-configure tungkol sa network na sinusubukan mong gamitin; nagkaroon ng error sa pagkakakonekta.


Ang isang **karaniwang isyu ay ang user, sa pagtatangkang magbayad ng mas mura para sa kanilang transaksyon, ay nagtatakda ng napakababang gas limit**, at ang mga kondisyon ng network ay napakasikip na walang espasyo sa anumang mga block para sa ganoong "murang" transaksyon, kung minsan para sa napakahabang panahon: sa kalaunan, ang transaksyong ito ay magiging "lipas" at kailangang kanselahin ng user.


**Kung nagpadala ka ng transaksyon at hindi pa ito na-finalize**, ipapakita ang status nito bilang "nakabinbin" sa MetaMask.


**Kung nagpadala ka ng isang transaksyon, at ito ay nabigo, ang pinaka-malamang na dahilan ay ang kakulangan ng gas**: ikaw ay "naubusan ng gas", sa madaling salita, ang transaksyon ay may halaga sa gas na, kapag pinarami ng presyo ng gas, ay nagresulta sa isang kabuuang halaga ng native currency ng network na mas malaki kaysa sa mayroon ka sa iyong wallet.



#### Impormasyon


Para sa higit pa tungkol sa pagkalkula ng gas, kumunsulta sa aming [gabay sa gas na nandito](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas).



Ito ay maaaring mangyari sa maraming kadahilanan, ngunit ang isang bagay na dapat isaalang-alang ay kung ano ang transaksyon na sinusubukan mong isagawa. Ang pag-mining ng isang NFT sa panahon ng peak network traffic ay maaaring masyadong gas-intensive; kung sumusubok ka ng bago o pang-eksperimentong transaksyon, maaaring sulit na subukan ang isang pagsubok na network bago magbayad ng mga tunay na bayarin sa live na network.


 


**Pag-aayos ng problema**
-------------------------


### **Pangunahing Salik #1: Lokal o Broadcast sa Network**


Habang nagpapatuloy ka tungkol sa pag-diagnose ng iyong isyu sa transaksyon, lalo na pagdating sa isang nakabinbing transaksyon, kailangan mong tingnan kung ang transaksyon ay nasa iyong lokal na mempool, o kung nakarating ito sa network at natigil doon sa anumang dahilan. Kung ito ay nasa iyong lokal na mempool, ang solusyon ay maaaring kasing-simple ng pag-lock, at pag-unlock, ang iyong MetaMask wallet (**siguraduhing alam mo ang iyong password at i-back up ang iyong Secret Recovery Phrase bago mo gawin**). Kung ito ay ginawa sa network, ang solusyon ay maaaring maging mas kumplikado.


Para sa higit pa sa pag-aayos sa mga problemang ito, tingnan ang mga link sa ibaba.  
  



### **Pangunahing Salik #2: Nonce**


Maaaring mangahulugan ang salitang ito ng ilang magkakaibang bagay. Isa itong pagpapaikli ng "number only used once", at sa kontekstong ito, ang halos ibig sabihin nito ay 'numero ng transaksyon', simula sa unang transaksyong ginawa ng nagpapadalang address. Maaari malagay ka sa tunay na gulo kung, halimbawa, nagfa-fire ka ng dalawang magkaibang transaksyon mula sa magkakaibang instance ng MetaMask na may parehong wallet address nang magkasabay. **Ang mga transaksyon ng iyong address ay kailangang nasa tumataas na pagkakasunud-sunod ayon sa kanilang nonce.** Gayunpaman, kung paanong ang mga nonce ay may kakayahang magdulot ng natigil na transaksyon, maaari silang maging susi upang maalis ang isang transaksyon.


Para sa higit pa sa pamamaraang iyon, [tingnan dito](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction).


 


**Susunod na Mga Hakbang**
--------------------------


### *Kung mayroon kang nabigo o nakabinbing transaksyon, kumunsulta sa mga sumusunod na mapagkukunan para sa tulong.*


#### [Paano magpadala ng mga token mula sa iyong MetaMask wallet](https://metamask.zendesk.com/hc/en-us/articles/360015488931)


#### [Paano pabilisin o kanselahin ang isang nakabinbing transaksyon](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction)


#### [Bakit nabigo ang aking transaksyon na may error na "Wala nang Gas"?](https://metamask.zendesk.com/hc/en-us/articles/360038849792-Why-did-my-transaction-fail-with-an-Out-of-Gas-error-How-can-I-fix-it-)


#### [Uniswap na Pag-troubleshoot](https://metamask.zendesk.com/hc/en-us/articles/360053394291-Uniswap-support-and-troubleshooting-tips)


#### [Gabay sa User: Gas](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas)


#### [Maaari ko bang baligtarin ang isang nakumpirma nang transaksyon?](https://metamask.zendesk.com/hc/en-us/articles/360059957352-Can-I-reverse-an-already-confirmed-transaction-)


 


**Mga FAQ**
-----------


#### 
*Q: Ang isang account sa aking wallet ay may nakabinbin o nasa pila na transaksyon. Maaari ba akong magsimula ng isa pang transaksyon mula sa ibang account sa loob ng parehong wallet?* A: Oo, maaari mong gawin. Ang nonce ay binibilang sa bawat account, hindi sa bawat wallet.

