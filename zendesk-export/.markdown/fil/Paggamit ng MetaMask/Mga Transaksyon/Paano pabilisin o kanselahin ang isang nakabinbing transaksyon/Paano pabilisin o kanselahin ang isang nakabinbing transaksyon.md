Kapag nagsumite ka ng transaksyon sa Ethereum o isang compatible na network, bahagi ng gas na binabayaran mo ay isang bid sa network para iproseso ang iyong transaksyon nang mas maaga — kilala ang elementong ito bilang priority fee. Bagama't tutulungan ka ng MetaMask sa pamamagitan ng pagkalkula ng kabuuang gas fee na malamang na magtulak na ma-pick up ang iyong transaksyon, maaaring maghintay ka nang matagal sa huli kung magsusumite ka nang may mababang presyo ng gas. Bilang payo sa kung anong mga presyo ng gas ang magreresulta sa isang transaksyon na matatapos sa isang makatwirang tagal ng oras, mangyaring sumangguni sa mga mapagkukunan tulad ng [gas tracker ng Etherscan](https://etherscan.io/gastracker), o isang katulad na tracker para sa alinmang network na iyong ginagamit.


Bukod pa rito, minsan may mga pagkakataon kung saan may nangyayaring mali, at ang isang transaksyon ay natigil lang, o nakabinbin nang napakahabang panahon.


Umabot ka man sa puntong ito, may ilang iba't ibang paraan para matugunan ito.


 


### Bago ka gumawa ng anumang karagdagang aksyon, ang una mong hakbang ay dapat na ganap na i-exit at isara ang iyong browser, buksan itong muli, at i-unlock ang MetaMask (sa mobile, isara lang ang app at buksan itong muli). Kung hindi nito malulutas ang problema, magpatuloy sa sumusunod:


 


**Pagpapabilis ng isang transaksyon**
-------------------------------------


![MetaMask speed up transaction](https://support.metamask.io/hc/article_attachments/12927043481371)


Subukan ang isa sa mga pagpipilian sa ibaba:


* Maghintay hanggang ang network ay handa na magproseso ng mga transaksyon sa presyong ito
* Kung hindi mo pa nagagawa, i-click ang button na iyon na nagsasabing **Pabilisin**. Hahayaan ka nitong muling isumite ang parehong transaksyon, ngunit may mas mataas na gas fee na dapat magpahintulot sa transaksyon na maproseso nang mas mabilis. Dahil ginagamit muli ng prosesong ito ang parehong nonce tulad ng orihinal, hindi mo kailangang magbayad para sa gas nang dalawang beses.


Tandaan na ang **pagpapabilis sa transaksyon ay magpapataas sa halagang ginagastos mo para sa transaksyon**.


 


**Pagkansela ng transaksyon - Paraan 1: Pagkansela ng in-app**
--------------------------------------------------------------


Kung hindi mo pa ito nagagawa, upang kanselahin ang transaksyon, piliin lamang ang **Kanselahin**, tulad ng sa screenshot sa itaas. Pakitandaan, **ang pagkansela ay maaari lamang *subukan* kung ang transaksyon ay nakabinbin pa rin sa network.** Ang mga transaksyong nakumpirma na ay hindi na mababago.


 


**Pagkansela ng transaksyon - Paraan 2: Pasadyang nonce**
---------------------------------------------------------


Kasangkot sa prosesong ito ang pagpapadala ng bagong transaksyon na may parehong nonce (isang numerong pantukoy para sa bawat transaksyon, na hinango sa pariralang 'number only used once'). Ang transaksyon ay hindi talaga kailangang magkaroon ng anumang halaga -- hal. maaari kang magpadala ng 0 ETH. Ang mahalaga ay nagbabayad ka ng sapat na gas para sa network na unahin ito.


Kapag ginagamit ang paraang ito, **kakailanganin mong magtrabaho nang paurong mula sa pinakalumang nakabinbing transaksyon sa queue na gusto mong kanselahin**. Halimbawa, hindi mo maaaring subukang kanselahin ang isang transaksyon na may nonce na 10 bago kanselahin ang nonce 9.


*Kinuha ang mga screenshot sa ibaba sa magkakaibang oras, kaya maaaring mag-iba-iba ang mga gas fee na ipinapakita sa mga ito, maging sa bawat hakbang. Huwag hayaang panghinaan ka ng loob dahil dito! Kapag ikaw mismo ang gagawa nito, awtomatikong mag-a-update ang MetaMask nang real time para ipakita ang mga rate sa merkado.*




Extension Mobile


1. Sa mga advanced na setting, i-on ang **Customize transaction nonce** at **Advanced na mga kontrol sa gas.** Ang huli ay magbibigay-daan sa iyo na manipulahin ang gas na babayaran mo at tiyaking naproseso ang iyong transaksyon sa pagkansela bago ang orihinal na gusto mong kanselahin.



#### Tandaan:


Ang MetaMask Extension ay kasalukuyang may experimental feature na available na tinatawag na [Enhanced Gas Fee UI](https://metamask.io/1559/) (hindi dapat mapagkamalang [mga advanced na kontrol sa gas](https://support.metamask.io/hc/en-us/articles/360022895972)). Maaaring isagawa ang mga hakbang na ito kung na-on mo man ito o hindi, ngunit tandaan na iba ang magiging hitsura ng mga ito. Hindi gumagamit ng Enhanced Gas UI ang mga hakbang sa ibaba. Tandaan:



	* Kung naka-on sa iyo ang Enhanced Gas UI, kailangan mo pa ring i-on ang 'I-customize ang transaction nonce'.
	* Kung hindi naka-on sa iyo ang Enhanced Gas UI, kailangan mong i-on ang parehong 'Mga advance na kontrol sa gas' at 'I-customize ang transaction nonce'.

![Mga advance na setting ng MetaMask](https://support.metamask.io/hc/article_attachments/12927064113947)
2. **Magpadala ng bagong transaksyon**. Sa bagong transaksyon, ipadala **SA** iyong sarili, ibig sabihin ang iyong pampublikong address sa MetaMask. **Punan ang 'Custom Nonce' ng kaparehong nonce sa transaksyon na nakabinbin pa rin**:


![Metamask_custom_transaction_nonce_Extension.png](https://support.metamask.io/hc/article_attachments/12927064259483)
3. Ngayon, pindutin ang 'I-edit' sa tabi ng 'Gas Fee' (kung naka-on sa iyo ang experimental [Advanced Gas UI](https://support.metamask.io/hc/en-us/articles/360022895972-Using-advanced-gas-controls#:~:text=%C2%A0-,Enhanced%20Gas%20UI,-Since%20the%20introduction), lalabas ito bilang 'Market'). Makikita mo na ngayon ang mga pagpipilian sa ibaba:


![MetaMask advanced gas controls extension](https://support.metamask.io/hc/article_attachments/12927065407515)


Upang matiyak na ang iyong kahilingan sa pagkansela ay kukunin bilang isang prayoridad, at bago ang orihinal, **kailangan mong magbayad ng higit pa para sa gas**. Sundin ang mga tagubilin na ito:


	* Itakda ang iyong **limitasyon sa gas** *na maihahambing sa o bahagyang mas mataas* kaysa sa iyong orihinal na transaksyon.
	* Itakda ang iyong **max priority fee** sa *hindi bababa sa 10% na mas mataas* (sa Gwei) kaysa sa gas fee ng orihinal na (nakabinbing) transaksyon (hal. kung ang transaksyong iyon ay may gas fee na 30 Gwei, itakda ang max na priyoridad na bayarin sa transaksyon sa pagpapalit/pagkansela hanggang 33-35 Gwei).
	* Siguraduhin na ang iyong max fee ay hindi bababa sa 30% na mas mataas kaysa sa max na bayarin ng transaksyon na iyong papalitan. Halimbawa, kung ang iyong dating bayad ay 150 Gwei, pumili ng mas malapit sa 200 Gwei sa pagkakataong ito.Suriin ang gas tracker tulad ng [Etherscan](https://etherscan.io/gastracker) o [ETH Gas Station](https://ethgasstation.info/) para sa gabay sa mga inirerekumendang max fee.




1. **Sa Settings > Advanced, i-on ang 'I-customize ang transaction nonce'.**
2. **Magpadala ng bagong transaksyon.** Sa bagong transaksyon, ipadala SA iyong sarili, ibig sabihin ang iyong pampublikong address sa MetaMask. **Ilagay sa 'Custom Nonce' ang kaparehong nonce ng sa transaksyon na nakabinbin pa rin**.


Para mahanap ang custom nonce setting sa app, pumunta sa screen ng kumpirmasyon ng transaksyon, na lumalabas pagkatapos mong ilagay ang dami ng token at tatanggap. Pindutin ang 'I-edit' para baguhin ito:


![MetaMask custom transaction nonce Mobile](https://support.metamask.io/hc/article_attachments/12927068442907)
3. Ngayon kailangan mong siguraduhin na naka-configure ang iyong mga setting ng gas nang sa gayon ay maproseso ang iyong kapalit na transaksyon. Mula sa screen ng kumpirmasyon ng transaksyon, i-tap ang naka-highlight na gas value:


![MetaMask advanced gas controls mobile](https://support.metamask.io/hc/article_attachments/12927041593755)


Ngayon, i-access ang 'Mga advanced na opsyon' mula sa menu na lalabas.
4. Mula rito, maaari mong isaayos nang husto ang gas para masiguradong mapi-pick up ang iyong transaksyon. Titingin ka naman ngayon sa isang screen na ganito ang hitsura:


![MetaMask advanced gas controls mobile](https://support.metamask.io/hc/article_attachments/12927063201691)


Mula rito, isaayos ang mga setting ng gas. Sundin ang mga tagubiling ito para masiguradong mapi-pick up ang iyong transaksyon:


	* Itakda ang iyong **limitasyon sa gas** *na maihahambing sa o bahagyang mas mataas* kaysa sa iyong orihinal na transaksyon.
	* Itakda ang iyong **max priority fee** sa *hindi bababa sa 10% na mas mataas* (sa Gwei) kaysa sa gas fee ng orihinal na (nakabinbing) transaksyon (hal. kung ang transaksyong iyon ay may gas fee na 30 Gwei, itakda ang max na priyoridad na bayarin sa transaksyon sa pagpapalit/pagkansela hanggang 33-35 Gwei).
	* Siguraduhin na ang iyong **max fee** ay *hindi bababa sa 30% na mas mataas* kaysa sa max fee ng transaksyon na pinapalitan mo. Halimbawa, kung ang iyong dating bayad ay 150 Gwei, pumili ng mas malapit sa 200 Gwei sa pagkakataong ito.Suriin ang isang gas tracker tulad ng [Etherscan](https://etherscan.io/gastracker) o [ETH Gas Station](https://ethgasstation.info/) para sa patnubay sa mga inirerekomendang max fee.



