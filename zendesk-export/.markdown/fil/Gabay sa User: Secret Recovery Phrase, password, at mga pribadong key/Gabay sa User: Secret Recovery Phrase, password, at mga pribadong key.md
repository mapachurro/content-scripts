
#### Baguhan sa crypto at web3?


Pumunta sa [MetaMask Learn](https://learn.metamask.io/) para sa isang simpleng karanasan sa pagkatuto na partikular na idinisenyo para sa mga baguhan sa web3. Libre ito, available sa maraming wika, at may kasamang kapaki-pakinabang na tools gaya ng mga simulation para tulungan kang maging pamilyar sa MetaMask.



### Sa artikulong ito:


* [Paano naiiba ang seguridad ng MetaMask mula sa mga tradisyonal na web account](#h_01FYVAXCSH95CQ08Q0P2VJA5HV)
* [Ano ang Secret Recovery Phrase?](#h_01FYVAXJQT914HCHEYFPNMEJEA)
* [Mga Dapat at Hindi Dapat Gawin sa Secret Recovery Phrase](#h_01FYVAXSE5C9E4YBCSWT2F2RBQ)
* [Mga Madalas Itanong sa Secret Recovery Phrase](#h_01FYVAXZYWJENFWG9K9CJTQFK7)
* [Mga Password at MetaMask](#h_01FYVAY5K22PX6926537V8B4SX)
* [Mga Madalas Itanong tungkol sa mga pribadong key](#h_01FYVAYH3ZZ8VW8BPDDADWRC8E)




**MetaMask: isang naiibang modelo ng seguridad ng account**
------------------------------------------------------------


Gumagamit ang [teknolohiya ng pampublikong blockchain](https://metamask.zendesk.com/hc/en-us/articles/360015489611) ng lubhang kakaibang set ng mga tool para ma-secure ang data ng user, kumpara sa mga tradisyonal na online na teknolohiya. Karamihan sa atin ay sanay nang gumawa ng account sa isang app, o service at pagkakaroon ng kakayahan, halimbawa, na sumulat sa support para i-reset ang ating password o username. Sanay tayong pinapanatili ng app ang ating data, na marahil ay sa isang uri ng computer na pag-aari ng kumpanya.


Pero... Hindi ganyan gumagana ang MetaMask. Ang MetaMask ay may tatlong magkakaibang uri ng **sikreto** na ginagamit sa iba't ibang paraan para panatilihing pribado at ligtas ang iyong wallet, at iyong mga account. Ang Secret Recovery Phrase, ang password, at mga pribadong key. Maingat ka naming gagabayan sa mga sikretong ito nang paisa-isa.


 


**Panimula sa mga Secret Recovery Phrase**
------------------------------------------


Isa sa mahahalagang (makikita mo ang ibig sabihin ko rito) teknolohiya sa likod ng MetaMask, at mga tool na pinakanauugnay sa account ng user sa crypto space ang *seed phrase,*o ang tinatawag sa MetaMask na *Secret Recovery Phrase* mo. 


#### **Lahat ng account mo ay matematikal na kinuha sa Secret Recovery Phrase mo. Puwede mong isipan ang SRP bilang isang keyring, at nagtatago ito ng maraming pribadong key hanggang gusto mo: at kinokontrol ng bawat isa sa mga key na iyon ang isang account.**


Ngayon, kung gusto mo ng teknikal na paliwanag: Ang mga seed phrase gaya ng alam natin ngayon ay nilagyan ng code para magamit sa Bitcoin, batay sa isang pamantayang tinatawag na Bitcoin Improvement Proposal 39, o [BIP-39](https://en.bitcoin.it/wiki/BIP_0039). Sa mga simpleng salita, isang series ng mga salita ang pinili nang may mataas na antas ng pagiging random mula sa isang partikular na [listahan ng mga salita](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt). Sa MetaMask at sa marami pang ibang teknolohiya na compatible sa Ethereum, may 12 salita sa isang seed phrase. Gumagamit ng mga phrase na may 24 na salita ang ilang mas lumang seed na na-generate ng Brave browser, at ng ilang hardware wallet.


Bawat isa sa mga salitang ito ay katumbas ng isang series ng mga numero, at kapag inilagay sa **isang partikular na pagkakasunod-sunod**, ay kumakatawan sa isang higit na mas user-friendly na paraan para tandaan ang isang napakahabang numero. Ginagamit naman ang numerong iyon para *deterministic* na mag-generate ng mga account mo, at puwede mong marinig na tinatawag ng mga tao na mga deterministic wallet. Sa computer science, ginagamit ang salitang deterministic para ilarawan ang isang proseso (na karaniwang parang isang algorithm) na *palaging*nagbibigay ng parehong resulta. Sa madaling salita, **ang iyong Secret Recovery Phrase ay palaging ige-generate ang parehong hanay ng mga account na nanggaling dito**. 


 


### May ilang mahahalagang feature na dapat tandaan dito:


* Ang **Secret Recovery Phrase ay ang sikretong kumokontrol sa wallet**. Kung nasa ibang tao ang sikretong ito, mayroon silang kumpletong access sa wallet. **Hindi itinatago ng MetaMask ang SRP mo:** **[ikaw ang custodian ng wallet mo.](https://metamask.zendesk.com/hc/en-us/articles/360059952212)** **Hindi kailanman** hihingin ng mga kinatawan ng MetaMask ang Secret Recovery Phrase mo, kahit na nasa isang sitwasyon kung saan kailangan ng suporta sa customer. Kung may taong humingi nito sa iyo, malamang na sinusubukan nilang i-scam ka o nakawin ang mga pondo mo.
* **Lokal na ginagamit para makakuha ng mga pribadong key** ang SRP mo, isa kada account/address. Naka-store ang mga account sa blockchain, at ina-unlock ng mga pribadong key na ito ang mga account na iyon.
* **Kapag nag-uninstall ka ng app** o ng extension, mawawala ang lokal na bersyon ng data (ang [vault](https://metamask.zendesk.com/hc/en-us/articles/360018766351) ang kapansin-pansing exception), pero na-record na sa blockchain ang anumang transaksyon na ginawa mo gamit ang lokal na bersyon na iyon ng MetaMask. Kung gayon, dapat na lumabas ang mga transaksyon sa [block explorer](https://metamask.zendesk.com/hc/en-us/articles/360057536611), at sa isa pang instance ng MetaMask, hangga't [nag-restore ka gamit ang parehong Secret Recovery Phrase](https://metamask.zendesk.com/hc/en-us/articles/360015289612) (**na may mga salita sa parehong pagkakasunod-sunod**). Ibig sabihin nito, hangga't nasa iyo ang Secret Recovery Phrase mo, palagi kang makakapag-uninstall ng Metamask at makakapag-restore ng wallet mo.
* **Sa loob ng wallet mo, puwede kang magkaroon ng napakalaking bilang ng magkakahiwalay na account.** Kapag gumagawa o nagre-restore ang MetaMask ng wallet mo mula sa Secret Recovery Phrase, ginagawa lang muna nito ang unang account. Gayunpaman, [puwedeng gawin ulit ang mga karagdagang account na ginawa mo](https://metamask.zendesk.com/hc/en-us/articles/360015489271) sa instance ng MetaMask sa hinaharap. **Dahil *deterministic* ang. wallet, palagi nitong gagawin ulit ang parehong mga acoount, sa parehong pagkakasunod-sunod. Para sa iba pa tungkol sa isyung ito, tingnan ang mga Madalas Itanong sa ibaba.** Tandaan, na ang mga karagdagang account (pagkatapos ng una, na awtomatikong ni-label bilang 'Account 1') ay ***hindi***awtomatikong idadagdag ulit sa account mo sa lahat ng pagkakataon. Tingnan ang aming paliwanag [dito](https://metamask.zendesk.com/hc/en-us/articles/360015489271-How-to-add-missing-accounts-after-restoring-with-Secret-Recovery-Phrase#:~:text=If%20you%20have,automatically%20re%2Dadded.) para sa karagdagang impormasyon.
* **Posibleng [mag-import ng mga account](https://metamask.zendesk.com/hc/en-us/articles/360015489331) mula sa ibang teknolohiya na compatible sa Ethereum papunta sa isang MetaMask wallet.** Para gawin ito, ginagamit ang *pribadong key* ng partikular na account na iyon. Gayunpaman, **hindi awtomatikong ire-restore ng MetaMask ang account na ito sa isa pang instance; kakailanganin mong mano-manong idagdag ito ulit**. Kung gayon, kung mano-mano mong na-import ang mga account, **tandaan ang mga pribadong key ng mga ito, sa parehong paraan nang ginawa mo sa seed phrase mo**, upang ma-import mo ulit ang mga ito sa hinaharap.


 


**MetaMask Secret Recovery Phrase: Mga Dapat at Hindi Dapat Gawin**
-------------------------------------------------------------------




**Dapat:**

* **Isulat ang iyong Secret Recovery Phrase sa isang ligtas na lugar**. Hindi namin masasabi sa iyo nang tiyak kung saan, dahil nakadepende ito sa iyong mga sitwasyon.
	+ Ang kahalagahan ng pagsulat ng Secret Recovery Phrase mo ay hindi ito mananakaw online. Kapag na-store mo ito sa isang file sa isang folder sa cloud storage na naka-link sa internet, halimbawa, puwede itong teoretikal na manakaw.
* I-double check ang spelling mo at na isinulat mo ang bawat salita sa parehong pagkakasunod-sunod nang ibinigay ang mga ito sa iyo.
* Makipag-ugnayan sa [mga opisyal na channel](https://metamask.zendesk.com/hc/en-us/articles/360058230211) ng Suporta ng MetaMask kung kailangan mo ng tulong.





**Hindi Dapat:**

* Itago ito sa isang lugar na madaling makita o lokasyon na madaling ma-hack; hal. sa isang document na naka-save sa cloud o email na may title na "Seed Phrase"; sa isang post-it na nakadikit sa computer mo.
* Ibigay ang seed phrase mo sa kahit sino, kahit pa sabihin nilang galing sila sa Suporta ng MetaMask.
* Baguhin ang pagkakasunud-sunod ng mga salita.





 


**Mga Secret Recovery Phrases: Mga Madalas Itanong**
----------------------------------------------------


### Na-restore ang seed phrase ko sa ibang account!


Kumonsulta sa artikulo sa knowledge base tungkol sa paksang ito [rito](https://metamask.zendesk.com/hc/en-us/articles/360058120992). Dagdag pa, tingnan ang thread ng Komunidad [dito](https://community.metamask.io/t/restored-metamask-no-coins-are-showing/878/107?u=jacob.cantele) para sa higit pang context at background na impormasyon.


### Iba pang Madalas Itanong sa Secret Recovery Phrase:


[Paano ipapakita ang Secret Recovery Phrase mo](https://metamask.zendesk.com/hc/en-us/articles/360015290032)


[Paano i-recover ang Secret Recovery Phrase mo](https://metamask.zendesk.com/hc/en-us/articles/360018766351)


[Pag-import ng isang seed phrase mula sa isa pang wallet software: derivation path](https://metamask.zendesk.com/hc/en-us/articles/360060331752)


[Gabay sa Pag-migrate ng Wallet](https://metamask.zendesk.com/hc/en-us/articles/4867408571803)


[Paano mag-import ng account](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[Paano i-check ang aktibidad ng aking wallet sa blockchain explorer](https://metamask.zendesk.com/hc/en-us/articles/360057536611)


[Ano ang Secret Recovery Phrase at paano ko papanatilihing ligtas ang wallet ko?](https://metamask.zendesk.com/hc/en-us/articles/360060826432)


 


**Mga Password at MetaMask**
----------------------------


Gumagamit ang MetaMask ng mga password para sa iiisang layunin: para i-secure ang mismong app; sa madaling salita, para buksan ang app, ito man ay Mobile app o in-browser Extension. Kapag nag-restore o gumawa ka ng wallet mo mula sa Secret Recovery Phrase, hindi mo na ito regular na kakailanganin (**bagama't dapat na panatilihin mo itong naka-back up at ligtas**), at gagamitin mo ang password mo (o mas madalas sa Mobile, biometric authentication gaya ng facial recognition o fingerprint mo) para i-unlock ang app. Para sa higit pang detalye, tingnan ang aming artikulo [rito](https://metamask.zendesk.com/hc/en-us/articles/4405451730331).


 


**Mga pribadong key**
---------------------


Bagama't ginagamit ang Secret Recovery Phrase para gawin at i-restore ang buong MetaMask wallet mo, kasama ang lahat ng account na ginawa sa wallet na iyon, bawat account ay may sariling *private key*. Puwedeng gamitin ang key na ito para i-import ang account na iyon, at ang account lang na iyon, sa ibang wallet. Gayundin, puwedeng i-import sa MetaMask wallet mo ang mga single account mula sa iba pang crypto technology. 


### Mga Madalas Itanong tungkol sa mga pribadong key:


[Ano ang mga na-import na account?](https://metamask.zendesk.com/hc/en-us/articles/360015289932)


[Paano mag-import ng account](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[Paano i-export ang pribadong key ng isang account](https://metamask.zendesk.com/hc/en-us/articles/360015289632)


[Pwede ba akong mag-import ng Coinbase wallet account papunta sa aking MetaMask account?](https://metamask.zendesk.com/hc/en-us/articles/360058485292)

