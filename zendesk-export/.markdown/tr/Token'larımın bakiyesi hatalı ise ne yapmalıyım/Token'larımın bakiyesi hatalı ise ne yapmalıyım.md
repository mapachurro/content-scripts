
#### Tokenlar hiç görünmüyorsa ne yapacağım?


Bu sorunu gidermek için [buradaki](https://support.metamask.io/hc/en-us/articles/360059232852) kılavuzumuza bakın.



Öncelikle, blok gezgininde gösterilen token bakiyelerini doğrulayın ve MetaMask ile karşılaştırın. Bunu yapmak için cüzdan adresinizi kopyalayıp bulunduğunuz ağa karşılık gelen blok gezginine (Ethereum mainnet için Etherscan, Arbitrum için Arbiscan vb) yapıştırmanız gerekecektir. Ayrıntılı talimatlar için [buraya](https://support.metamask.io/hc/en-us/articles/360057536611) bakın.




Uzantı Mobil


MetaMask Uzantınız, ETH veya diğer token'lar için hatalı veya eksik bakiye gösteriyorsa, bakiyenizi doğru görene kadar aşağıdaki adımları tek tek deneyin.


**Devam etmeden önce, [Gizli Kurtarma Kodunuzu](https://support.metamask.io/hc/en-us/articles/4404722782107-User-Guide-Secret-Recovery-Phrase-password-and-private-keys) güvenli bir yere kaydettiğinizden emin olun.**


1. İnternet bağlantınızın güçlü ve stabil olup olmadığını kontrol edin. Değilse, MetaMask doğru bakiyeleri yükleyemeyebilir.
2. MetaMask uzantısının yüklü olduğu tarayıcınızı kapatın ve tekrar açın.
3. Yüklediğiniz reklam engelleyicileri kapatmayı deneyin veya bir VPN kullanıyorsanız, VPN kapalıyken MetaMask'ı kullanmayı deneyin.
4. Farklı bir ağa geçiş yapın ve tekrar geri dönün. Bunu yapmak için uygulamanın en üstündeki mevcut ağınıza tıklayın. Farklı bir ağ seçin ve ardından ilk ağınıza geri dönün.
5. [Tarayıcı izinleri sorunu](https://support.metamask.io/hc/en-us/articles/360038139452-MetaMask-states-Balance-may-be-outdated-displays-in-orange-or-ETH-not-added-to-balance) yaşamadığınızdan emin olun.
6. Kullandığınız ağ için birden fazla kullanılabilir RPC URL'si varsa, farklı bir RPC URL'si deneyin. RPC URL'sini düzenlemek için Ayarlar > Ağ'a gidin ve ardından söz konusu ağa tıklayın. Daha fazla bilgi için [ağ ekleme hakkındaki makalemize](https://support.metamask.io/hc/en-us/articles/360043227612) bakın.
7. Yaşadığınız sorunun sadece şu anda kullandığınız tarayıcı kaynaklı olması ihtimaline karşı, resmi web sitemizden ([https://metamask.io](https://metamask.io/)) başka bir desteklenen tarayıcı (Firefox, Chrome, Brave, Edge) kullanarak MetaMask'i kurun ve ardından 12 kelimelik Gizli Kurtarma Kodunu kullanarak cüzdanı geri yüklemeyi deneyin.




MetaMask Mobile'da görüntülenen token'ların sayısının hatalı olduğunu Etherscan üzerinde doğruladıktan sonra, şu adımları izleyin:


1. İnternet bağlantınızın güçlü ve stabil olduğundan emin olun. Değilse, token değerleri güncel olmayabilir.
2. Farklı bir ağa geçiş yapın ve ardından tekrar geri dönün.
3. Mümkünse bağlı olduğunuz ağın RPC URL'sini bir alternatifiyle değiştirin.  Daha fazla bilgi için [ağ ekleme hakkındaki makalemize](https://support.metamask.io/hc/en-us/articles/360043227612) bakın.
4. [Buradaki](https://support.metamask.io/hc/en-us/articles/360015489031-How-to-add-unlisted-tokens-custom-tokens-in-MetaMask#h_01FWH499MRDT5QC4R3KNPQNRWB) talimatları izleyerek token'ı gizleyin ve ardından [buradaki](https://support.metamask.io/hc/en-us/articles/360015489031-How-to-add-unlisted-tokens-custom-tokens-in-MetaMask) talimatları izleyerek token'ı tekrar ekleyin.


**Söz konusu token, Ethereum dışındaki bir ağ için ağ yerel token'ı ise** (BNB, AVAX, MATIC vb) [ağı silip](https://support.metamask.io/hc/en-us/articles/4502810252059-How-to-remove-networks) [tekrar eklemeyi](https://support.metamask.io/hc/en-us/articles/360043227612-How-to-add-a-custom-network-RPC) deneyin.  
  
**Söz konusu token ETH ise, [Gizli Kurtarma Kodunuzu](https://support.metamask.io/hc/en-us/articles/4404722782107-User-Guide-Secret-Recovery-Phrase-password-and-private-keys) güvenli bir yere kaydettiğinizden (yedeklediğinizden) emin olun** ve uygulamayı yeniden kurun.

Bu adımları denedikten sonra hala sorun yaşıyorsanız, lütfen [destek sayfamızdaki](https://support.metamask.io/hc/en-us) "Bir Konuşma Başlat" düğmesi aracılığıyla bizimle iletişime geçin.



#### Bu token, arzı veya değeri etkileyen yerleşik mekanizmalara sahip mi?


Ethereum ve EVM uyumlu zincirlerde, farklı faydalara (utility) sahip çok çeşitli token'lar bulunur. Bazı token'lar, çeşitli koşullara göre arz veya değeri dinamik olarak değiştirmek için tasarlanmıştır:


* Token arzının ayarlandığı [elastik arz (rebase) token](https://support.metamask.io/hc/en-us/articles/4405497827355-User-Guide-Tokens#:~:text=Elastic%20supply%20/%20Rebase%20/%20Algorithmic%20tokens)'ları
* Farklı türde işlemlere (ör. basit transfer, takas, satma vb) uygulanan "vergili" tokenlar. Bunlara "transferi ücretli" token'lar da denir.


Bakiyenizin hatalı olduğu sonucuna varmadan önce, token'larınız için buna benzer durumların geçerli olup olmadığını kontrol edin. Bu bilgileri genellikle projenin teknik dokümanında (white paper) veya dokümantasyonda bulabilirsiniz.


