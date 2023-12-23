
#### Kripto paralar ve web3 konularında yeni misiniz?


Web3'ye yeni başlayanlara yönelik özel hazırlanmış ve kolay bir eğitim deneyimi için [MetaMask Eğitim](https://learn.metamask.io/)'e gidin. Bu eğitim tamamen ücretsizdir ve birçok dilde mevcuttur; ayrıca MetaMask'a uyum sağlamanıza yardımcı olacak simülasyonlar gibi yararlı araçlar da içerir.



#### *Bu makalede, işlemler ve işlemlerin neden başarısız oldukları ile ilgili açıklamalar ve kaynak bağlantılarının yanı sıra yaygın başarısız işlem senaryoları ve bunların nasıl çözümleneceğiyle ilgili konular yer almaktadır:*


* [Bir blok zinciri işleminin anatomisi](#h_01G79J04D0EN1VD8VS7C7J7KD1)
* [Sık görülen sorunlar](#h_01G79J09NWA8CGR4VYC2PT5B6Y)
* [Başlıca çözümler](#h_01G79J0J8JTRPM9MRB76EN1GPP)
* [Ek kaynaklar ve sonraki adımlar](#h_01G79J0RP8ZMZ1V1SKQY70TXCT)
* [SSS](#h_01G79J18RBK27GZCF10CGN9GKP)


 


**Bir blok zinciri işleminin anatomisi**
----------------------------------------


Herkese açık bir blok zinciri ağı üzerindeki 'işlemler'den bahsettiğimizde, genellikle iki adres arasındaki etkileşimleri kastederiz. Başka bir deyişle bir adresten diğerine 'gönderilen', takas edilebilir veya edilemez token'lar ya da diğer kripto varlıklar. Ayrıca "dahili işlemler" olarak anılan ve akıllı sözleşmeler arasında gerçekleşen etkileşimler olarak tanımlanan, bu makalenin kapsamı dışında kalan işlemler de vardır.



#### Daha fazla bilgi mi istiyorsunuz?


Blok zinciri ağları ve genel olarak nasıl çalıştıkları hakkında daha fazla bilgi için [buradaki tanıtım makalemize](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) göz atabilir ve tanıdık gelmeyen terimlerle karşılaşırsanız [dilediğiniz zaman sözlüğümüzü kullanabilirsiniz](https://consensys.net/knowledge-base/a-blockchain-glossary-for-beginners/).



Daha net konuşmak gerekirse aslında hiçbir şey hiçbir yere *gönderilmemektedir.* Ethereum gibi akıllı sözleşmelerin kullanıldığı bir blok zinciri ağı, bir dizi farklı bileşene veya fonksiyona sahiptir. Bunlardan biri de "bilgisayar" olarak adlandırdığımız şeylerdir: programları ("akıllı sözleşmeler") çalıştırabilen Ethereum Sanal Makinesi veya EVM. Bununla birlikte sistemin "omurga"sı, *dağıtık bir hesap defteridir*: **Bir tarafta her bir Ethereum cüzdan adresini içeren ve her adresin tuttuğu her bir kripto varlık türü için bir sütun içeren bir çalışma tablosu hayal edin.** 


Görselleştirmek için bir örnek kullanalım. Guillaume'un Dolores'e bir işlem göndermek istediğini varsayalım. Guillaume'un hesabında 1,36 ETH olsun ve Dolores'e 0,5 ETH göndermeyi planlıyor diyelim. Ayı piyasasında bile Dolores için iyi bir gün gibi görünüyor. 


Guillaume MetaMask cüzdanını açar, Dolores'in adresini girer, ödemek istediği şekilde gas parametrelerini yapılandırır ve 'gönder' seçeneğine tıklar.


Bu noktada işlem, *yerel bellek havuzu* ya da *yerel mempool* olarak bilinen yerel geçici bekleme durumuna girer. İşlem daha sonra ağdaki en yakın düğüm tarafından 'seçilir'. Guillaume'un [gas ayarlarına](https://metamask.zendesk.com/hc/en-us/articles/360022895972-Using-advanced-gas-controls) bağlı olarak işlemine öncelik verilir (**Guillaume [gas birimi](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas) başına ne kadar çok ödemeye istekli olursa işlemi o kadar hızlı bir şekilde yürütülür**) ve ağdaki diğer düğümlere iletilir. Düğümler Guillaume'un harcayacak ETH'ye sahip olduğunu doğrulamak için çalışacak ve ardından 'işlemi' yürütecektir: **Hesap defteri değiştirilecek, 0,5 ETH Guillaume'un hesabından düşülecek ve Dolores'in hesabına 0,5 ETH yatırılacaktır.**


*'Yürüyen parmak yazar, verir hükmünü ve yazdıktan sonra geçip gider'*: ETH aslında bir ağ içerisinde yer değiştirmez; Guillaume'un bilgisayarından Dolores'in MetaMask gelen kutusuna e-posta benzeri bir şey gitmez. Guillaume, **[MetaMask üzerinden özel anahtarları](https://metamask.zendesk.com/hc/en-us/articles/4404722782107-User-guide-Secret-Recovery-Phrase-password-and-private-keys) ile doğrulanan** bir isteği kendi hesabını borçlandırmak ve Dolores'in hesabını alacaklandırmak için ağa göndermiştir. Ağın protokollerinin içine programlanmış doğrulama işleminden sonra bu işlem gerçekleştirilmiştir.


#### *İşte bir işlem ile ilgili her şey budur: bir varlığı bir adresten diğerine tahsis etmek için hesap defteri üzerinden yapılan bir istek.*


 


**İşler ters giderse**
----------------------


İşler bir dizi nedenden dolayı ters gidebilir. Genellikle, 'yazılımın doğası' durumu vardır: MetaMask'ta bir hata olabilir veya kullanmaya çalıştığınız ağla ilgili olarak yanlış yapılandırılmış bir şey vardır ya da bir bağlantı hatası gerçekleşmiştir.


**Sıkça rastlanan bir sorun da kullanıcının işlemi için daha az ücret ödemek üzere çok düşük bir gas limiti belirlemesi** ve ağ koşullarının bu kadar "ucuz" bir işlem için herhangi bir blok içinde, bazen çok uzun bir süreliğine yer bulamayacak kadar sıkışık olmasıdır. Sonuçta bu işlem "bayat" hale gelir ve kullanıcı tarafından iptal edilmesi gerekir.


**Bir işlem gönderdiyseniz ve sonuçlanmadıysa** durum bilgisi MetaMask üzerinde "beklemede" olarak gösterilir.


**Bir işlem gönderdiyseniz ve başarısız olduysa sebebi büyük olasılıkla eksik gas olmasıdır**: "Gas bitmiştir", yani başka bir deyişle işlemin öyle bir gas maliyeti vardır ki gas fiyatı ile çarpıldığında cüzdanınızda sahip olduğunuzdan daha büyük miktarda ağın yerel para birimi ile sonuçlanmıştır.



#### Bilgi


Gas hesaplaması hakkında daha fazla bilgi için [buradaki gas kılavuzumuza](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas) göz atın.



Bu durum bir dizi nedenden dolayı gerçekleşebilir; ancak dikkate alınması gereken bir nokta, gerçekleştirmeye çalıştığınız işlemin ne olduğudur. Yoğun ağ trafiği zamanlarında bir NFT'yi mint etmek çok fazla gas gerektirebilir; yeni veya deneysel bir işlem denemesi yapıyorsanız gerçek ağ ücretlerini ödemeden önce bir test ağı üzerinde sınama yapmanız avantajlı olabilir.


 


**Sorunu gidermek**
-------------------


### **Kilit Faktör #1: Yerel veya Ağ Üzerinde Yayın**


İşlem sorununuzu teşhis etmeye çalışırken, özellikle de bekleyen bir işlem söz konusu olduğunda işlemin halen yerel mempool'unuzda olup olmadığına ya da ağa kadar gitmiş ancak orada bir nedenle takılmış olup olmadığına bakmanız gerekir. Henüz yerel mempool'unuzda yer alıyorsa çözüm MetaMask cüzdanınızı kilitlemek ve kilidini geri açmak kadar basit olabilir (**bu işlemi gerçekleştirmeden önce parolanızı bildiğinizden ve Gizli Kurtarma İfadenizi yedeklediğinizden emin olun**). İşlem ağa kadar gidebildiyse çözüm daha karmaşık olabilir.


Bu sorunları gidermek için aşağıdaki bağlantılara göz atın.  
  



### **Kilit Faktör #2: Geçici Anahtar (Nonce)**


Bu kelime birkaç farklı anlama gelebilir. "Yalnızca bir kez kullanılan sayı" ifadesinin kısaltmasıdır ve bu bağlamda, gönderen adres tarafından yapılan ilk işlemden başlayarak kabaca "işlem numarası" anlamına gelir. Örneğin, aynı cüzdan adresi ile farklı MetaMask kurulumlarından iki farklı işlemi aynı anda başlatırsanız ciddi bir sorun yaşayabilirsiniz. **Adresinizin işlemlerinin geçici anahtarlarına göre artan sıralamada olmaları gerekir.** Bununla birlikte, geçici anahtarlar işlemin takılmasına neden olabildikleri gibi işlemi açmanın yolu da olabilirler.


Bu teknik hakkında daha fazla bilgi için [buraya göz atın](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction).


 


**Sonraki Adımlar**
-------------------


### *Başarısız veya bekleyen bir işleminiz varsa yardım için aşağıdaki kaynaklara başvurun.*


#### [MetaMask cüzdanınızdan nasıl token gönderirsiniz?](https://metamask.zendesk.com/hc/en-us/articles/360015488931)


#### [Bekleyen bir işlemi nasıl hızlandırır veya iptal edersiniz?](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction)


#### [İşlemim neden "Gas Bitti" hatası ile başarısız oldu?](https://metamask.zendesk.com/hc/en-us/articles/360038849792-Why-did-my-transaction-fail-with-an-Out-of-Gas-error-How-can-I-fix-it-)


#### [Uniswap Sorun Giderme](https://metamask.zendesk.com/hc/en-us/articles/360053394291-Uniswap-support-and-troubleshooting-tips)


#### [Kullanıcı Kılavuzu: Gas](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas)


#### [Daha önce onaylanmış bir işlemi tersine çevirebilir miyim?](https://metamask.zendesk.com/hc/en-us/articles/360059957352-Can-I-reverse-an-already-confirmed-transaction-)


 


**SSS**
-------


#### 
*S: Cüzdanımdaki bir hesapta bekleyen veya kuyrukta bir işlem var. Aynı cüzdan içinde farklı bir hesaptan başka bir işlem başlatabilir miyim?* C: Evet, yapabilirsiniz. Geçici anahtar cüzdan başına değil, hesap başına sayılır.

