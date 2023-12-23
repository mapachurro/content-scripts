
#### Kripto paralar ve web3 konularında yeni misiniz?


Web3'ye yeni başlayanlara yönelik özel hazırlanmış ve kolay bir eğitim deneyimi için [MetaMask Eğitim](https://learn.metamask.io/)'e gidin. Bu eğitim tamamen ücretsizdir ve birçok dilde mevcuttur; ayrıca MetaMask'a uyum sağlamanıza yardımcı olacak simülasyonlar gibi yararlı araçlar da içerir.



### Bu makalede yer alan bilgiler:


* [MetaMask güvenliğinin klasik web hesaplarından farkı nedir](#h_01FYVAXCSH95CQ08Q0P2VJA5HV)
* [Gizli Kurtarma Kodu nedir?](#h_01FYVAXJQT914HCHEYFPNMEJEA)
* [Gizli Kurtarma Kodu'nda Yapılacaklar ve Yapılmayacaklar](#h_01FYVAXSE5C9E4YBCSWT2F2RBQ)
* [Gizli Kurtarma Kodu SSS](#h_01FYVAXZYWJENFWG9K9CJTQFK7)
* [Parolalar ve MetaMask](#h_01FYVAY5K22PX6926537V8B4SX)
* [Özel anahtarlar SSS](#h_01FYVAYH3ZZ8VW8BPDDADWRC8E)




**MetaMask: farklı bir hesap** **güvenliği** modeli
----------------------------------------------------


[Açık blok zinciri teknolojisi](https://metamask.zendesk.com/hc/en-us/articles/360015489611), kullanıcı verilerini korumak için geleneksel çevrimiçi teknolojilere kıyasla çok farklı bir araç seti kullanır. Çoğumuz bir uygulama veya hizmet ile bir hesap oluşturmaya ve örneğin parolamızı veya kullanıcı adımızı sıfırlamak için destek ile mesajlaşmaya alışkınız. Uygulamanın verilerimizi, muhtemelen şirkete ait bir tür bilgisayarda saklamasına alışkınız.


Fakat... MetaMask bu şekilde çalışmıyor. MetaMask'te, cüzdan ve hesaplarınızı, kişiye özel ve güvenli tutmak için farklı şekillerde kullanılan üç farklı **gizli bilgi** bulunur: Gizli Kurtarma Kodu, parola ve özel anahtarlar. Bu gizli bilgilerden sırasıyla bahsedeceğiz.


 


**Gizli Kurtarma Kodlarına Giriş**
----------------------------------


MetaMask'in ve kripto evrenindeki kullanıcı hesabıyla ilgili araçların çoğunun temelinde yatan anahtar teknolojilerden biri, *tohum ifade*dir (seed phrase); buna MetaMask'te *Gizli Kurtarma Kodu* diyoruz. 


#### **Tüm hesaplarınız, Gizli Kurtarma Kodunuzdan matematiksel olarak türetilir. GKK'yi bir anahtarlık gibi düşünebilirsiniz; bu anahtarlığa dilediğiniz sayıda özel anahtar takabilirsiniz ve bu anahtarların her biri bir hesabı kontrol eder.**


Teknik bir açıklamasını yapmak gerekirse; bugün bildiğimiz haliyle tohum ifadeler, Bitcoin Geliştirme Teklifi 39 veya [BIP-39](https://en.bitcoin.it/wiki/BIP_0039) olarak adlandırılan bir standarda göre, Bitcoin'de kullanım için kodlanmıştır. Basit bir anlatımla, belirli bir [kelime listesinden](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt) yüksek düzeyde rastgelelik içeren bir dizi kelime seçilir. MetaMask'te ve diğer birçok Ethereum uyumlu teknolojide, bir tohum ifadede 12 kelime bulunur. Brave tarayıcısı ve bazı donanım cüzdanları tarafından üretilmiş bazı daha eski tohumlarda, 24 kelimelik ifadeler kullanılmaktadır.


Bu kelimelerin her biri, bir sayı dizisine karşılık gelir ve **belirli bir sırayla** dizildiğinde, çok ama çok uzun bir sayıyı hatırlamak için çok daha kullanıcı-dostu bir yol sağlar. Bu sayı daha sonra hesaplarınızı *deterministik olarak* oluşturmak için kullanılır; deterministik cüzdanlardan bahsedildiğini duymuş olabilirsiniz. Bilgisayar biliminde, deterministik, *her zaman* aynı sonucu üreten bir süreci (genellikle bir tür algoritmayı) tanımlamak için kullanılır. Başka bir deyişle, **Gizli Kurtarma Kodunuz her zaman, kendisinden türetilmiş aynı hesap kümesini oluşturur**. 


 


### Burada dikkat edilmesi gereken bazı önemli özellikler var:


* **Gizli Kurtarma Kodu, cüzdanı kontrol eden gizli bilgidir**. Bu bilgiye sahip olan biri, cüzdana tam erişim hakkına sahiptir. **MetaMask sizin GKK'nızı saklamaz:** **[cüzdanınızın sorumlusu sizsiniz.](https://metamask.zendesk.com/hc/en-us/articles/360059952212)** MetaMask temsilcileri, bir müşteri destek durumunda bile, **asla** Gizli Kurtarma Kodunuzu sormaz. Birisi sizden bu kodu istiyorsa, muhtemelen sizi dolandırmaya veya varlıklarınızı çalmaya çalışıyordur.
* GKK'nız, hesap/adres başına bir tane olmak üzere **özel anahtarları yerel olarak türetmek için kullanılır**. Hesaplar blok zinciri üzerinde saklanır ve bu özel anahtarlar bu hesapların kilidini açar.
* **Uygulamayı veya uzantıyı kaldırırsanız**, verilerin yerel versiyonu ortadan kaybolur (buna kayda değer tek istisna [kasadır (vault)](https://metamask.zendesk.com/hc/en-us/articles/360018766351)); ancak MetaMask'in bu yerel sürümü ile yaptığınız tüm işlemler, blok zincirinde kaydedilmiş haldedir. Bu nedenle, aynı [Gizli Kurtarma Kodunu](https://metamask.zendesk.com/hc/en-us/articles/360015289612) (**kelimeler aynı sırada olacak şekilde**) kullanarak geri yükleme yaparsanız, bu işlemler hem bir [blok gezginine](https://metamask.zendesk.com/hc/en-us/articles/360057536611) hem de Metamask'in başka bir kurulumuna yansıtılır. Bu, Gizli Kurtarma Kodunuza sahip olduğunuz sürece, her zaman MetaMask'i kaldırabileceğiniz ve cüzdanınızı geri yükleyebileceğiniz anlamına gelir.
* **Cüzdanınızın içinde, çok sayıda ayrı hesap bulunabilir.** MetaMask, Gizli Kurtarma Kodundan cüzdanınızı oluşturduğunda veya geri yüklediğinde, başlangıçta yalnızca ilk hesabı üretir. Bununla birlikte, [oluşturacağınız tüm diğer hesaplar, MetaMask'in gelecekteki bir kurulumunda yeniden oluşturulabilir](https://metamask.zendesk.com/hc/en-us/articles/360015489271). **Cüzdan *deterministik* olduğu için, her zaman aynı hesapları, aynı sırayla yeniden oluşturur. Bu konuda daha fazla bilgi için aşağıdaki SSS'lere bakın.** Bununla birlikte, (otomatik olarak "Hesap 1" olarak etiketlenmiş ilk hesaptan sonraki) ilave hesapların her koşulda hesabınıza otomatik olarak tekrar ***eklenmeyeceğini*** unutmayın. Daha fazla bilgi için [buradaki](https://metamask.zendesk.com/hc/en-us/articles/360015489271-How-to-add-missing-accounts-after-restoring-with-Secret-Recovery-Phrase#:~:text=If%20you%20have,automatically%20re%2Dadded.) açıklamamıza göz atın.
* **Diğer Ethereum uyumlu teknolojilerden bir MetaMask cüzdanına [hesapları aktarmak](https://metamask.zendesk.com/hc/en-us/articles/360015489331) mümkündür.** Bunu yapmak için, bu belirtilen hesabın *özel anahtarı* kullanılır. Ancak **bu hesap, başka bir kurulumda MetaMask tarafından otomatik olarak geri yüklenmeyecek; bunu manuel olarak yeniden eklemeniz gerekecektir**. Bu nedenle, manuel olarak içe aktarılmış hesaplarınız varsa, **tohum ifadenizi bir yere kaydettiğiniz gibi bu hesapların özel anahtarlarını da bir yere kaydedin**. Bu şekilde bu hesapları, gelecekte tekrar içe aktarabilirsiniz.


 


**MetaMask Gizli Kurtarma Kodu: Yapılacaklar ve Yapılmayacaklar**
-----------------------------------------------------------------




**Yapılacak:**

* **Gizli Kurtarma Kodunuzu güvenli bir yere yazın**. Nereye yazmanız gerektiğini söyleyemeyiz, çünkü bu sizin koşullarınıza bağlıdır.
	+ Gizli Kurtarma Kodunuzu bir yere elle yazarak kaydetmenin avantajı, çevrimiçi olarak çalınamayacak olmasıdır. Örneğin GKK'yı internete bağlı bir bulut depolama klasöründe saklarsanız, teorik olarak çalınması mümkündür.
* Kelimeleri verilen sırayla yazdığınızdan ve yazım hatası yapmadığınızdan emin olun.
* Yardıma ihtiyacınız varsa MetaMask Desteği'nin [resmi kanallarına](https://metamask.zendesk.com/hc/en-us/articles/360058230211) ulaşın.





**Yapılmayacak:**

* Kolayca bulunabilecek veya kolayca ele geçirilebilecek bir yerde saklamayın; ör: buluta kaydedilmiş bir belgede veya "Tohum İfade" başlıklı bir e-postanın içinde veya bilgisayarınıza yapıştırılmış bir post-it notunun üzerinde.
* MetaMask Desteği'nde çalıştıklarını söyleseler bile, tohum ifadeyi (GKK) kimseye vermeyin.
* Kelimelerin sırasını değiştirmeyin.





 


**Gizli Kurtarma Kodları: Sık Sorulan Sorular**
-----------------------------------------------


### Tohum ifadem (GKK), farklı bir hesabı geri yükledi!


Lütfen bu konuyla ilgili [buradaki](https://metamask.zendesk.com/hc/en-us/articles/360058120992) bilgi tabanı makalesine bakın. Ek olarak, daha fazla kaynak ve ilave bilgi için [buradaki](https://community.metamask.io/t/restored-metamask-no-coins-are-showing/878/107?u=jacob.cantele) Topluluk mesaj akışına bakın.


### Diğer Gizli Kurtarma Kodu Sık Sorulan Soruları:


[Gizli Kurtarma Kodumu nasıl görebilirim](https://metamask.zendesk.com/hc/en-us/articles/360015290032)


[Gizli Kurtarma Kodumu nasıl kurtarabilirim](https://metamask.zendesk.com/hc/en-us/articles/360018766351)


[Başka bir cüzdan yazılımından bir tohum ifadenin içe aktarılması: türetme yolu](https://metamask.zendesk.com/hc/en-us/articles/360060331752)


[Cüzdan Yer Değiştirme Kılavuzu](https://metamask.zendesk.com/hc/en-us/articles/4867408571803)


[Bir hesap nasıl içe aktarılır](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[Blok zinciri gezgininde cüzdan aktivitemi nasıl kontrol edebilirim](https://metamask.zendesk.com/hc/en-us/articles/360057536611)


[Gizli Kurtarma Kodu nedir ve cüzdanımı nasıl güvende tutabilirim?](https://metamask.zendesk.com/hc/en-us/articles/360060826432)


 


**Parolalar ve MetaMask**
-------------------------


MetaMask'ın parolalar kullanmasının tek bir amacı vardır: uygulamanın kendisini güvende tutmak için; başka bir deyişle, ister Mobil uygulama ister tarayıcı içi Uzantı olsun, uygulamayı açmak için. Gizli Kurtarma Kodunuzdan cüzdanınızı geri yükledikten veya oluşturduktan sonra, GKK'ya artık sürekli ihtiyacınız olmayacaktır (**ancak GKK'yı güvenli bir yere kaydetmeniz gerekir**); uygulamayı açmak için parolanızı (veya Mobilde daha yaygın olarak, yüz tanıma veya parmak iziniz gibi biyometrik kimlik doğrulama yöntemlerini) kullanabilirisiniz. Daha fazla bilgi için [buradaki](https://metamask.zendesk.com/hc/en-us/articles/4405451730331) makalemize göz atın.


 


**Özel anahtarlar**
-------------------


MetaMask Cüzdanınızın tamamını, bu cüzdanda oluşturulan tüm hesaplar dahil olmak üzere, oluşturmak ve geri yüklemek için bir Gizli Kurtarma Kodu kullanılsa da, her hesabın kendi *özel anahtarı* vardır. Bu anahtar, bu hesabı ve yalnızca bu hesabı farklı bir cüzdana aktarmak için kullanılabilir. Benzer şekilde, diğer kripto teknolojilerinden hesaplarınız da ayrı ayrı MetaMask cüzdanınıza aktarılabilir. 


### Özel Anahtarlar Sık Sorulan Sorular:


[İçeri aktarılan hesaplar nelerdir?](https://metamask.zendesk.com/hc/en-us/articles/360015289932)


[Bir hesap nasıl içe aktarılır](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[Bir hesabın özel anahtarı nasıl dışa aktarılır](https://metamask.zendesk.com/hc/en-us/articles/360015289632)


[Coinbase cüzdan hesabını MetaMask cüzdanıma aktarabilir miyim?](https://metamask.zendesk.com/hc/en-us/articles/360058485292)

