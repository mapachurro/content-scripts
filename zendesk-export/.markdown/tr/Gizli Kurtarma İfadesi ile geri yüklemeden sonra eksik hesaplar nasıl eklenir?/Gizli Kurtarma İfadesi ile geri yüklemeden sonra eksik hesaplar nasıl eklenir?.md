
#### Not:


Gizli Kurtarma Kodunuzu kullanarak cüzdanınızı geri yüklediğinizde, **içe aktarılmış** hesaplar, yeniden **eklenmeyecektir**. Başlangıçta bunları içe aktardığınız şekilde [manuel olarak yeniden eklenmeleri gerekir](https://support.metamask.io/hc/en-us/articles/360015489331).



**Gizli Kurtarma İfadenizi kimseyle PAYLAŞMAYIN! Bu kelimeler tüm hesaplarınızı ele geçirmek için kullanılabilir. Gizli Kurtarma İfadenizi düzenleyemez veya değiştiremezsiniz.**


 


Gizli Kurtarma Kodunuzu kullanarak [bir cüzdanı geri yüklediğinizde](https://support.metamask.io/hc/en-us/articles/360015289612-How-to-restore-your-MetaMask-account-from-Seed-Phrase-Secret-Recovery-Phrase), MetaMask daha önce [oluşturduğunuz](https://support.metamask.io/hc/en-us/articles/360015289452) tüm ilave hesapları otomatik olarak yeniden ekleyecektir; ancak bu yalnızca belirli koşullar altında geçerlidir.


MetaMask, önceki hesaplarınızı artan sırayla (yani önce Hesap 2, sonra Hesap 3 vb. şeklinde) kontrol ederek mümkün olan durumlarda ([içe aktarılmadıkları](https://support.metamask.io/hc/en-us/articles/360015289932) varsayılarak) ek hesaplarınızı eklemeye çalışacaktır. **Sıfırdan farklı ETH bakiyesine sahip hesaplar, otomatik olarak yeniden eklenir**. Bununla birlikte bu işlem, MetaMask 0 ETH bakiyeye sahip bir hesapla karşılaştığında sona erer; yani 0 ETH bakiyeli ilk hesap (ve ondan sonrakiler) *eklenmeyecektir*.


**Bu işlemin yalnızca Ethereum mainnet üzerindeki ETH bakiyeleri için geçerli olduğunu** unutmayın. Yani diğer token'lar veya diğer ağlardaki token'lar hesabınızın otomatik olarak yeniden eklenmesini sağlamaz.


**Otomatik olarak tekrar eklenmeyen hesapları, bir hesap "[oluşturarak](https://support.metamask.io/hc/en-us/articles/360015289452)" geri eklemeniz gerekecektir**. Örneğin, Hesap 4'te bazı token'lara sahipseniz ancak bu token'lar mainnet üzerinde ETH olmadıkları için Hesap 4 otomatik olarak eklenmediyse yapmanız gereken tek şey Hesap 4'e ulaşana kadar (aşağıdaki adımları kullanarak) manuel olarak hesap eklemektir. Geri yüklemeden *önceki* Hesap 4'ünüz, daha önce uyguladığınız adlandırmadan bağımsız olarak geri yüklemeden *sonraki* Hesap 4'e karşılık gelir.


Hesapları yeniden eklemek için "oluştur" düğmesini kullanmanız gerektiğinde, hesap adresinin farklı olmasından endişelenmeyin. Adresler, özel anahtar'ınızdan *deterministik halde* kriptografik olarak türetilir; bu da onların her zaman aynı olacakları anlamına gelir. Bir Ethereum hesabı bir kez oluşturulduktan sonra süresiz olarak kalıcı olduğundan, kaldığınız yerden devam edebilirsiniz. 


Diğer hesaplarınızı orijinalde oluşturuldukları sırayla geri yüklemek için lütfen aşağıdaki adımları izleyin:




Uzantı Mobil


1. MetaMask aşağı açılır menüsünün sağ üst köşesindeki kısayol simgesine tıklayın
2. MetaMask hesaplarınızı oluşturuldukları sırayla geri yüklemek için "Hesap Oluştur" seçeneğine tıklayın
3. Hesaplar daha önce adlandırılmış ise "**Oluştur**" seçeneğine tıklamadan önce aşağıdaki adımda onları yeniden adlandırabilirsiniz


![How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase.gif](https://support.metamask.io/hc/article_attachments/9026739981083/How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase.gif)




1. Menüyü getirmek için ekranın sol üst kısmındaki hamburger simgesine dokunun. Buradan hesap adınızın yanındaki aşağı açılır ok simgesine dokunun:
2. 'Yeni Hesap Oluştur' seçeneğine dokunun:


![How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase_Mobile.gif](https://support.metamask.io/hc/article_attachments/9027058464027/How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase_Mobile.gif)




Aradığınız adresleri halen göremiyorsanız muhtemelen farklı bir Gizli Kurtarma İfadesi ile oluşturulmuşlardır ya da özel anahtarlar veya JSON kullanarak yeniden içe aktarmanız gereken bir içe aktarılmış hesabınız var demektir. Lütfen [bir hesabın nasıl içe aktarılacağı ile ilgili bu makaleye](https://support.metamask.io/hc/en-us/articles/360015489331-Importing-an-Account) göz atın.

