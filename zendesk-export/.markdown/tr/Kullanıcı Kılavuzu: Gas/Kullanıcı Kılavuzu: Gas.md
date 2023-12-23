
#### Kripto paralar ve web3 konularında yeni misiniz?


Web3'ye yeni başlayanlara yönelik özel hazırlanmış ve kolay bir eğitim deneyimi için [MetaMask Eğitim](https://learn.metamask.io/)'e gidin. Bu eğitim tamamen ücretsizdir ve birçok dilde mevcuttur; ayrıca MetaMask'a uyum sağlamanıza yardımcı olacak simülasyonlar gibi yararlı araçlar da içerir.



Gas, işlemlerin ve akıllı sözleşmelerin yürütülmesi için ne kadar hesaplama işi gerektiğinin ölçü birimidir. Esasen işlem ücreti anlamına gelen bu terim Ethereum'dan gelir ve bu bağlamda Ethereum Sanal Makine (EVM) üzerinde yürütülen hesaplamaya işaret eder. Ethereum kurulduğundan bu yana, EVM ile uyumlu (ve EVM ile uyumlu olmayan!) pek çok ağ ortaya çıkmış ve benzer modelleri benimsemiştir. 


Bu terim, bir araba motoruna güç veren gas'tan (gasoline, benzin) gelmektedir; değişken ve bazen de pahalı olan operasyon maliyetidir. Nasıl ki daha büyük, daha güçlü arabalar çalışmak için daha fazla yakıta ihtiyaç duyuyorsa daha karmaşık akıllı sözleşmeler de hesaplamalarına güç vermesi için daha fazla gas ihtiyacı duyar.


Gas ücretlerini hesaplamak için kullanılan yöntem, ağa bağlı olarak değişir. Örneğin, Ethereum'da gas hesaplamak eskiden çok karmaşıktı, ancak Ağustos 2021'de Ethereum Geliştirme Protokolü **(EIP) 1559**'un uygulanmaya başlamasıyla (Londra Güncellemesi olarak da bilinir) oldukça basitleştirildi. Özünde, işlemin başarıyla tamamlanmasından sonra **yakılan** (yani silinen ve yok olan) her gas birimi için bir **temel ücret** ödersiniz. Temel ücretin üzerine, yine birim gas başına bir **öncelik ücreti** eklersiniz. Bu ücret de işlemin ne kadar hızlı gerçekleştirilmesini istediğinize bağlı olarak değişir.


EVM ile uyumlu geniş ağ yelpazesinde gas veya benzer şekilde işlev gösteren alternatifler işlem maliyetlerini hesaplamak için kullanılan standart yöntem haline gelmiştir. Ücretler ağın yerel token'ı ile ödenir: Örneğin, Ethereum'daki işlemler için ETH, BSC kullanmak içim BNB, Polygon kullanmak için MATIC gerekir. Polygon gibi bazı ağlar Ethereum'un EIP-1559 modelini tümüyle benimsemiş olsalar da, Avalanche dahil diğerleri C-Chain'leri için bazı düzenlemeler yapmışlardır (Avalanche sadece temel [ücreti değil, öncelik ücretini de yakar](https://docs.avax.network/learn/platform-overview/transaction-fees/#c-chain-fees)).


Ethereum'da gas sisteminin nasıl çalıştığına dair daha derin bir inceleme için [buraya](https://ethereum.org/en/developers/docs/gas/) göz atın. 


 


**MetaMask** **üzerinde gas ile uğraşırken gerekli bazı detayları** burada bulabilirsiniz:


#### **Gas limiti (kullanılan gas birimi sayısı)**


*Gas limiti*, bir işlemi veya EVM operasyonunu gerçekleştirmek için ödemek istediğiniz maksimum gas birimi sayısıdır. Farklı operasyonlar, farklı miktarda gas birimi gerektirir. ETH veya bir token'ın gönderildiği normal bir işlemde normalde **21.000** gas gerekirken, ERC-20 token onayında ise 45.000 gerekir.  EVM ile uyumlu blok zinciri Harmony gibi birçok ağ, benzer şekilde standart bir işlem için 21.000 gas gerektiren modeli kullanır.



#### Gas limitini düzenlemem gerekiyor mu?


Hayır! MetaMask, yapmaya çalıştığınız işleme bağlı olarak gas limitinizi otomatik olarak belirler. Çoğu durumda bu, işleminizi tamamlamak için yeterli olacaktır. Bu limiti kontrol etmek veya düzenlemek istiyorsanız, [gelişmiş gas kontrollerinin](https://metamask.zendesk.com/hc/en-us/articles/360022895972) açık olduğundan (veya deneysel Gelişmiş Gas UI kullanıldığından) emin olun ve işlem onay ekranında "Düzenle"ye tıklayın.



#### **Temel ücret**


Ethereum ağındaki her bloğun, ağ talebi tarafından belirlenen bir temel ücreti vardır: temel ücret, bir hedef blok boyutuna kıyasla, önceki bloğun boyutu temel alınarak belirlenir (burada boyut, blok içindeki tüm işlemler için kullanılan toplam gas miktarını belirtir). Önceki bloğun boyutu hedefi aşıyorsa, sonraki blok için temel ücret %12,5 artırılır; bu şekilde kullanıcı yani siz (veya cüzdanınız) gelecek bloğun temel ücretini mutlak kesinlikle bilirsiniz. Bloğa dahil edilmek için, toplam gas ücretiniz, en az bu fiyat kadar olmalıdır. 


#### **Öncelik ücreti**


*Öncelik ücreti*, diğer adıyla "madenci bahşişi", işleminizi önceliklendirmesi için madenciyi teşvik eder. 


Doğal olarak, bu ücretin gerçekten bir madenciye gidip gitmediği, kullandıkları [mutabakat mekanizmasına](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) bağlıdır: Ethereum mainnet, Eylül 2022'deki Birleşme sonrasında bir Pay İspatı (Proof of Stake) ağı haline geldi, bu nedenle öncelik ücreti madencilere değil doğrulayıcılara gider. 


#### **Maksimum ücret**


Maksimum ücret, işleminiz için ödenen toplam genel miktardır. Şöyle hesaplanır: **(****temel ücret + öncelik ücreti) x kullanılan gas birimi**. MetaMask başlangıçta bu tutarı önceki blokun geçmişine göre belirler. Bununla birlikte, kullanıcılar bu miktarı özel ayarlar üzerinden düzenleyebilir (aşağıya göz atın). Gas başına maksimum ücret ve (temel ücret + gas başına maksimum öncelik ücreti) arasındaki fark kullanıcıya “iade edilir”.


 


### **Ek Kavramlar**


#### **Gwei**


Gwei, [gigawei](https://ethgasstation.info/blog/gwei/) (veya 1.000.000.000) anlamına gelir ve en düşük değer ölçüsü olan ether birimini ifade eder. [Gwei](https://www.investopedia.com/terms/g/gwei-ethereum.asp), gas ücretleri için ya da Ethereum blok zinciri üzerinde işlemleri gerçekleştirmek ve doğrulamak için gereken hesaplama enerjisini tazmin etmek üzere kullanıcılar tarafından yapılan ödemeler için kullanılır.


Fantom, Harmony ve Avalanche gibi diğer ağlar da maliyetleri gwei kullanarak hesaplama eğilimindedir.


#### **Kayma**


Kayma, teklif edilen ve uygulanan fiyat arasında yüzde olarak beklenen farktır.


#### **Gas ücreti**


Gas *ücreti*, Ethereum blok zinciri üzerindeki işlem ücretini ifade eder. Kullanıcıların işlemlerini doğrulamak veya tamamlamak için ödedikleri tutardır.


#### **Temel ücret**


Protokol tarafından belirlenir. Bir işlemin bloka dahil edilmesi (yani işlemin tamamlanması) için gereken minimum 'gasUsed' çarpanını temsil eder. Bu, işlem ücretinin yakılan kısmıdır.


 


### **Gelişmiş Gas Kontrolleri**


Gas kontrollerinizin özüne inmek istiyorsanız (örneğin bir dapp testi yapıyorsanız bu size yardımcı olabilir) MetaMask bunu yapabilir! Makalenin tamamını [buradan](https://metamask.zendesk.com/hc/en-us/articles/360022895972) görebilirsiniz.


 


### **SSS**


[Başarısız bir işlem için neden gas ücreti ödedim?](https://metamask.zendesk.com/hc/en-us/articles/360045439051)


[Gas ücretimi iade edebilir misiniz?](https://metamask.zendesk.com/hc/en-us/articles/360058370012)


[Bekleyen bir işlemi nasıl hızlandırırım ya da iptal ederim?](https://metamask.zendesk.com/hc/en-us/articles/360015489251)


[Gas ücretini nasıl tahmin edersiniz?](https://metamask.zendesk.com/hc/en-us/articles/360059562111)


[Gas ücretim neden bu kadar yüksek?](https://metamask.zendesk.com/hc/en-us/articles/360058751211-Why-my-gas-fees-are-so-high-)


[Hata: RPC'den çıktılar biçimlendirilirken [ethjs-query] (işlem düşük fiyatlı hatası)](https://metamask.zendesk.com/hc/en-us/articles/4402538041869)


["Yetersiz bakiye" hatasını veya seçilemeyen onay butonunu nasıl düzeltirim?](https://metamask.zendesk.com/hc/en-us/articles/360044703372)


 


 

