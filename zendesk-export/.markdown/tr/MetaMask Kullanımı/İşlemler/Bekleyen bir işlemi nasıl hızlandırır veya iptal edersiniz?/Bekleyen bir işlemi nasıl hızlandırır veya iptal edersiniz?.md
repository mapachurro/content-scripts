Ethereum veya uyumlu bir ağda bir işlem gönderdiğinizde, ödediğiniz gas miktarının bir kısmı, işleminizi daha erken işleme koymak için ağa yaptığınız bir tekliftir; buna öncelik ücreti denir. Her ne kadar MetaMask, işleminizin muhtemelen kabul edilmesini sağlayacak toplam gas ücretini hesaplayarak size yardımcı olsa da, düşük bir gas ücreti ile göndermeniz durumunda uzun süre bekleyebilirsiniz. Hangi gas fiyatlarının işlemin daha makul bir süre içinde sonuçlanmasını sağlayacağı ile ilgili tavsiyeler için [Etherscan'in gas izleyicisi](https://etherscan.io/gastracker) veya kullandığınız ağ için benzer bir izleyici gibi kaynaklara başvurun.


Ek olarak, bazen işlerin ters gittiği ve işlemin takıldığı ya da uzun süre beklemede kaldığı durumlar da meydana gelebilir.


Bu noktaya nasıl geldiğinizden bağımsız olarak, bu sorunu farklı şekillerde çözebilirsiniz.


 


### Başka bir işlem yapmadan önce ilk yapmanız gereken, çıkmak ve tarayıcınızı tamamen kapatmak, tekrar açmak ve MetaMask'in kilidini açmak olmalıdır (mobil'de uygulamayı kapatıp açmanız yeterlidir). Bu işlem sorunu çözmezse aşağıdakilerle devam edin:


 


**İşlemi hızlandırma**
----------------------


![MetaMask işlemi hızlandırma](https://support.metamask.io/hc/article_attachments/12927043481371)


Aşağıdaki seçeneklerden birini deneyin:


* Ağın bu fiyatla işlemleri işleme koymaya hazır olmasını bekleyin
* Henüz yapmadıysanız **Hızlandır** yazan düğmeye tıklayın. Bu düğme, aynı işlemi yeniden göndermenize izin verir, ancak daha yüksek bir gas ücreti alarak işlemin daha hızlı yürütülmesini sağlar. Bu işlem, orijinal işlemle aynı geçici anahtarı (nonce) tekrar kullandığı için, iki kez gas ücreti ödemeniz gerekmeyecektir.


**İşlemi hızlandırmanın, işlem için harcadığınız tutarı artıracağını** unutmayın.


 


**İşlemi iptal etme - Yöntem 1: Uygulama içi iptal**
----------------------------------------------------


Henüz yapmadıysanız işlemi iptal etmek için yukarıdaki ekran görüntüsünde olduğu gibi **İptal Et** tercihini seçmeniz yeterlidir. Lütfen **iptal işleminin yalnızca işlem halen ağ üzerinde beklemede ise *denenebileceğini* unutmayın.** Daha önce onaylanmış işlemler tersine çevrilemez.


 


**İşlemi iptal etme - Yöntem 2: Özel geçici anahtar**
-----------------------------------------------------


Bu süreçte, aynı geçici anahtar/nonce (her işlem için tanımlayıcı bir sayıdır, İngilizce "sadece bir kez kullanılan sayı" ifadesinin harflerinden türetilmiştir) ile yeni bir işlem gönderme yer alır. İşlemin herhangi bir değer içermesi gerekmez; örneğin 0 ETH gönderebilirsiniz. Önemli olan, ağın işlemi önceliklendirmesi için gerekli gas miktarını ödemenizdir.


Bu yöntemi kullanırken, **iptal etmek istediğiniz sıradaki en eski bekleyen işlemden geriye doğru gelmeniz gerekecektir**. Örneğin, özel geçici anahtar 10 ile yapılan bir işlemin iptal girişimini, anahtar 9 ile yapılanı iptal etmeden önce yapamazsınız.


*Aşağıdaki ekran görüntüleri farklı zamanlarda alınmıştır, bu nedenle bu görüntülerde gösterilen gas ücretleri, bir adımdan diğerine geçilirken bile değişebilir. Bunun sizi şaşırtmasına izin vermeyin! Bunu kendiniz yaptığınızda, MetaMask, piyasa fiyatlarını göstermek için gerçek zamanlı ve otomatik olarak güncellenecektir.*




Uzantı Mobil


1. Gelişmiş ayarlarda **İşlem geçici anahtarını özelleştir** ve **Gelişmiş gas kontrolleri** tercihlerini etkinleştirin. İkinci tercih, ödediğiniz gas miktarını değiştirmenize ve iptal işleminizin iptal etmek istediğiniz orijinal işlemden önce yürütülmesine olanak tanıyacaktır.



#### Not:


MetaMask Eklentisinde şu anda [Gelişmiş Gas Ücreti UI](https://metamask.io/1559/) ([gelişmiş gas kontrolleri](https://support.metamask.io/hc/en-us/articles/360022895972) ile karıştırılmamalıdır) denilen deneysel bir özellik bulunmaktadır. Bu adımlar bu özelliğin açık olup olmadığından bağımsız olarak gerçekleştirilebilir, ancak farklı görüneceklerini unutmayın. Aşağıdaki adımlarda Gelişmiş Gas UI kullanılmamaktadır. Aklınızda bulundurun:



	* Gelişmiş Gas UI özelliğini açmışsanız, "İşlem geçici anahtarını (nonce) özelleştir" seçeneğini de etkinleştirmeniz gerekir.
	* Gelişmiş Gas UI açık değilse, hem "Gelişmiş gas kontrolleri" hem de "İşlem geçici anahtarını (nonce) etkinleştir" seçeneğini açmanız gerekir.

![MetaMask gelişmiş ayarlar](https://support.metamask.io/hc/article_attachments/12927064113947)
2. **Yeni bir işlem gönderin**. Yeni işlemi **KENDİNİZE** gönderin, yani herkese açık MetaMask adresinize. **'Özel Geçici Anahtar' alanını halen bekleyen işleminizin geçici anahtarı ile doldurun**:


![Metamask_custom_transaction_nonce_Extension.png](https://support.metamask.io/hc/article_attachments/12927064259483)
3. Şimdi "Gas Ücreti"nin yanındaki "Düzenle" seçeneğine basın (Deneysel [Gelişmiş Gas UI](https://support.metamask.io/hc/en-us/articles/360022895972-Using-advanced-gas-controls#:~:text=%C2%A0-,Enhanced%20Gas%20UI,-Since%20the%20introduction) özelliği açıksa bu seçenek "Pazar" olarak görüntülenir). Artık aşağıdaki seçenekleri görebilirsiniz:


![MetaMask gelişmis gas kontrolleri eklentisi](https://support.metamask.io/hc/article_attachments/12927065407515)


İptal talebinizin öncelikli olarak ve orijinal işlemden önce alındığına emin olmak için **daha fazla gas ödemeniz gerekecektir**. Şu talimatları izleyin:


	* **Gas limitinizi** orijinal işleminiz ile *aynı veya biraz daha yüksek olarak* ayarlayın.
	* **Maksimum öncelik ücretinizi** orijinal (bekleyen) işleminizin gas ücretinden *en az %10 daha yüksek* (Gwei cinsinden) olacak şekilde ayarlayın (örneğin, bir işlem 30 Gwei gas ücretine sahipse değişim/iptal işleminde maksimum öncelik ücretini 33-35 Gwei olarak ayarlayın).
	* Maksimum ücretinizin, yenisiyle değiştireceğiniz işlemin maksimum ücretinden en az %30 daha fazla olduğundan emin olun. Örneğin, önceki ücretiniz 150 Gwei ise bu sefer 200 Gwei'ye yakın bir değer seçin.Önerilen maksimum ücretler hakkında rehberlik için [Etherscan](https://etherscan.io/gastracker) veya [ETH Gas İstasyonu](https://ethgasstation.info/) gibi bir gas izleyicisine göz atın.




1. **Ayarlar > Gelişmiş sayfasında, "İşlem geçici anahtarını özelleştir" seçeneğini açın.**
2. **Yeni bir işlem gönderin.** Yeni işlemi KENDİNİZE gönderin, yani herkese açık MetaMask adresinize. **"Özel Geçici Anahtar" alanına halen bekleyen işleminizin geçici anahtarını yazın**.


Uygulamada özel geçici anahtar ayarını bulmak için, token miktarını ve alıcıyı girdikten sonra beliren işlem onay ekranına gidin. Değiştirmek için "Düzenle"ye tıklayın:


![MetaMask özel işlem geçici anahtarı Mobil](https://support.metamask.io/hc/article_attachments/12927068442907)
3. Şimdi, eskisinin yerine geçen işlemin işlenebilmesi için, gas ayarlarınızın yapılandırılmış olduğundan emin olmanız gerekir. İşlem onay ekranından vurgulanmış gas değerine tıklayın:


![MetaMask gelişmiş gas kontrolleri mobil](https://support.metamask.io/hc/article_attachments/12927041593755)


Şimdi açılan menüden "Gelişmiş seçenekler" bölümüne gidin.
4. İşleminizin alındığından emin olmak için burada gas ayarlarınızı hassas bir şekilde yapabilirsiniz. Şimdi şu şekilde bir ekran göreceksiniz:


![MetaMask gelişmiş gas kontrolleri mobil](https://support.metamask.io/hc/article_attachments/12927063201691)


Burada gas ayarlarını değiştirin. İşleminizin alındığından emin olmak için aşağıdaki talimatları izleyin:


	* **Gas limitinizi** orijinal işleminiz ile *aynı veya biraz daha yüksek olarak* ayarlayın.
	* **Maksimum öncelik ücretinizi** orijinal (bekleyen) işleminizin gas ücretinden *en az %10 daha yüksek* (Gwei cinsinden) olacak şekilde ayarlayın (örneğin, bir işlem 30 Gwei gas ücretine sahipse değişim/iptal işleminde maksimum öncelik ücretini 33-35 Gwei olarak ayarlayın).
	* **Maksimum ücretinizin**, yenisiyle değiştireceğiniz işlemin maksimum ücretinden *en az %30 daha fazla* olduğundan emin olun. Örneğin, önceki ücretiniz 150 Gwei ise bu sefer 200 Gwei'ye yakın bir değer seçin.Önerilen maksimum ücretler hakkında yardım için [Etherscan](https://etherscan.io/gastracker) veya [ETH Gas İstasyonu](https://ethgasstation.info/) gibi bir gas izleyicisine göz atın.



