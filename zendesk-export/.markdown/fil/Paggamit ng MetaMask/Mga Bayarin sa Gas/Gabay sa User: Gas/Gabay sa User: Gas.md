
#### Baguhan sa crypto at web3?


Magpunta sa [MetaMask Learn](https://learn.metamask.io/) para sa hindi kumplikadong karanasan sa pagkatuto na partikular na dinisenyo para sa mga baguhan sa web3. Libreng-libre ito, available sa maraming wika, at may kasamang kapaki-pakinabang na tools gaya ng mga simulation upang matulungan kang maging pamilyar sa MetaMask.



Ang gas ay ang yunit ng panukat para sa kung gaano karaming computational work ang kinakailangan upang maproseso ang mga transaksyon at matalinong kontrata. Mahalagang bayad sa transaksyon, ang termino ay nagmula sa Ethereum, kung saan ang konteksto ay tumutukoy sa pagtutuos na isinagawa sa Ethereum Virtual Machine (EVM). Mula noong maitatag ang Ethereum, napakarami nang compatible sa EVM (at hindi compatible sa EVM!) na mga network ang nagsilabasan at nagpatibay ng mga katulad na modelo. 


Ang termino ay may pagkakahalintulad sa gas na nagpapaandar sa makina ng isang kotse: ito ang pagbagu-bago, paminsan-minsan ay mahal na gastos ng pagpapatakbo. Ang mas kumplikadong mga smart contract ay nangangailangan ng mas maraming gas para mapagana ang kanilang pag-compute, tulad ng isang mas malaki, mas makapangyarihang kotse na nangangailangan ng mas maraming gas upang tumakbo.


Ang paraan para sa pagkalkula ng mga bayarin sa gas ay nag-iiba depende sa network. Halimbawa, ang pagkalkula ng gas sa Ethereum ay dating napakakumplikado, ngunit lubhang pinasimple ng pagpapatupad ng Ethereum Improvement Protocol **(EIP) 1559** noong Agosto 2021 (kilala rin bilang London Upgrade). Kung tutuusin, nagbabayad ka ng **base fee** para sa bawat yunit ng gas, na ***binu-burn*** (basahin: dine-delete ito, at nawawala) sa matagumpay na pagkumpleto ng transaksyon. Karagdagan pa sa base fee, magdadagdag ka ng **priority fee**, muli sa bawat yunit ng gas, ang halaga nito ay depende sa kung gaano kabilis mo gustong maganap ang transaksyon.


Sa malawak na hanay ng mga available na network na katugma sa EVM, ang gas, o mga alternatibong gumaganang katulad nito, ay naging karaniwang paraan ng pagkalkula ng mga gastos sa transaksyon. Ang mga fee ay binabayaran sa native token ng network: halimbawa, ang anumang transaksyon sa Ethereum ay nangangailangan ng ETH; ang paggamit ng BSC ay nangangailangan ng BNB; ang paggamit ng Polygon ay nangangailangan ng MATIC. Ang ilang mga network ay ginamit ang EIP-1559 na modelong wholesale ng Ethereum, tulad ng Polygon, habang ang iba ay gumawa ng mga pagsasaayos, kabilang ang Avalanche, para sa kanilang C-Chain (na [sumusunog sa parehong base fee at priority fee](https://docs.avax.network/learn/platform-overview/transaction-fees/#c-chain-fees), sa halip na ang una lamang).


Kung gusto mong magbasa ng mas malalimang pagtingin sa kung paano gumagana ang gas sa Ethereum, tingnan [dito](https://ethereum.org/en/developers/docs/gas/). 


 


Narito ang ilang **mahahalagang detalye para sa pag-deal sa gas** **sa MetaMask**:


#### **Ang limitasyon ng gas (mga yunit ng gas na nagamit)**


Ang *limitasyon ng gas* ay ang **maximum na bilang ng mga yunit ng gas na handa mong bayaran para** makapagsagawa ng transaksyon o operasyon ng EVM. Nangangailangan ang iba't ibang operasyon ng iba't ibang dami ng yunit ng gas. Ang isang normal na transaksyong nagpapadala ng ETH o isang token ay karaniwang nagkakahalaga ng **21,000** gas, samantalang nangangailagan naman ng 45,000 ang pag-apruba ng ERC-20 token.  Maraming mga network, tulad ng EVM-compatible blockchain na Harmony, ay gumagamit ng magkaparehong modelo kung saan ang mga karaniwang transaksyon ay nagkakahalaga rin ng 21,000 gas.



#### Kailangan ko bang i-edit ang limitasyon ng gas?


Hindi! Awtomatikong itinatakda ng MetaMask ang iyong limitasyon ng gas depende sa transaksyong sinusubukan mong isagawa. Sa karamihan ng mga kaso, magiging sapat ito para makumpleto ang iyong transaksyon. Kung gusto mong tingnan ito o i-edit ito, siguraduhing mayroon kang [mga advanced gas control](https://metamask.zendesk.com/hc/en-us/articles/360022895972) na naka-on (o ginagamit mo ang Enhanced Gas UI) at pindutin ang 'I-edit' sa screen ng kumpirmasyon ng transaksyon.



#### **Ang base fee**


Bawat block sa Ethereum network ay may base fee na dinedetermina ng network demand: ang base fee ay batay sa laki ng block ng block bago nito, kumpara sa isang target na laki ng block (kung saan tumutukoy ang laki sa kabuuang halaga ng gas na nagamit para sa lahat ng transaksyon na kasama sa block). Kung lagpas sa target ang laki ng nakaraang block, tumataas nang 12.5% ang base fee para sa susunod na block, na nag-iiwan sa iyo, ang user (o ang iyong wallet), ng ganap na katiyakan tungkol sa base fee ng susunod na block. Dapat matugunan ng iyong kabuuang gas fee ang presyong ito bilang minimum upang maisaalang-alang na maisama sa block. 


#### **Ang priority fee**


Ang*priority fee*, na tinutukoy din bilang "miner tip", ay nagbibigay-insentibo sa miner para unahin ang iyong transaksyon. 


Natural, kung talagang napupunta man ito sa isang miner ay nakadepende sa [mekanismo ng consensus](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) na ginagamit nila: naging Proof of Stake network ang Ethereum mainnet kasunod ng Merge noong Setyembre 2022, kaya ang priority fee ay napupunta sa mga validator sa halip na sa mga miner. 


#### **Ang max fee**


Ang pinakamataas na fee ay ang kabuuang, pandaigdigang halaga na binayaran para sa iyong transaksyon. Ito ay kinakalkula bilang: **(****base fee + priority fee) x mga yunit ng gas na ginamit.** Una nang itinatakda ng MetaMask ang halagang ito batay sa kasaysayan ng nakaraang block. Gayunpaman, maaaring i-edit ng mga user ang halagang ito sa pamamagitan ng mga custom na setting (tingnan sa ibaba). Ang diperensya sa pagitan ng max fee kada gas at (base fee + max priority fee kada gas) ay “nire-refund” sa user.


 


### **Karagdagang Mga Konsepto**


#### **Gwei**


Ang Gwei ay isang yunit ng ether, ang pinakamaliit na denominasyon, na kumakatawan sa [gigawei](https://ethgasstation.info/blog/gwei/) (o 1,000,000,000). Ginagamit ang [Gwei](https://www.investopedia.com/terms/g/gwei-ethereum.asp) para sa mga gas fee, o sa halip ay mga pagbabayad na ginawa ng mga user upang mabayaran ang enerhiya sa pag-compute na kinakailangan upang maproseso at ma-validate ang mga transaksyon sa Ethereum blockchain.


May posibilidad din na kalkulahin ng ibang mga network ang mga gastos gamit ang gwei -- halimbawa, Fantom, Harmony, at Avalanche.


#### **Slippage**


Ang slippage ay ang inaasahang pagkakaiba sa porsyento sa pagitan ng isang na-quote at isang naisagawang presyo.


#### **Gas fee**


Ang gas *fee* ay tumutukoy sa transaction fee sa Ethereum blockchain. Ito ang binabayaran ng mga user para mapatunayan, o makumpleto ang kanilang transaksyon.


#### **Base fee**


Binuo ng protocol. Kinakatawan ang minimum na 'gasUsed' multiplier na kinakailangan para sa isang transaksyon na maisama sa isang block (i.e. para sa isang transaksyon na makumpleto). Ito ang bahagi ng bayad sa transaksyon na nawala.


 


### **Mga Advanced na Kontrol sa Gas**


Kung gusto mong mapunta sa nitty-gritty ng iyong mga kontrol sa gas (maaaring makatulong ito kung sinusubukan mo ang isang dapp, halimbawa), magagawa iyon ng MetaMask! Tingnan ang buong artikulo [rito](https://metamask.zendesk.com/hc/en-us/articles/360022895972).


 


### **FAQ**


[Bakit ako nagbayad ng gas fee para sa isang nabigong transaksyon?](https://metamask.zendesk.com/hc/en-us/articles/360045439051)


[Maaari mo bang ibalik ang aking mga gas fee?](https://metamask.zendesk.com/hc/en-us/articles/360058370012)


[Paano ko pabibilisin o kakanselahin ang isang nakabinbing transaksyon?](https://metamask.zendesk.com/hc/en-us/articles/360015489251)


[Paano matantya ang gas fee](https://metamask.zendesk.com/hc/en-us/articles/360059562111)


[Bakit napakataas ng aking mga gas fee?](https://metamask.zendesk.com/hc/en-us/articles/360058751211-Why-my-gas-fees-are-so-high-)


[Error: [ethjs-query] habang pino-format ang mga output mula sa RPC (transaction underpriced error)](https://metamask.zendesk.com/hc/en-us/articles/4402538041869)


[Paano ayusin ang error na "hindi sapat na pondo" o na-grey na button na kumpirmahin](https://metamask.zendesk.com/hc/en-us/articles/360044703372)


 


 

