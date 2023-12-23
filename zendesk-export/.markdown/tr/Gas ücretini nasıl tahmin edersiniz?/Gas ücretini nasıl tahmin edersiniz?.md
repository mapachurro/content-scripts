### Gas fiyatı alma


Ethereum mainnet üzerindeyseniz bugünün gas fiyatını tahmin etmek için [Etherscan'in gas aracını](https://etherscan.io/gastracker) kullanabilirsiniz. Lütfen gas fiyatının dalgalandığını unutmayın; güncel gas fiyatlarını görmek için daima gas istasyonuna başvurun.


Ethereum ağı, işlemleri yürütmek için gas gerektirir. Token gönderdiğinizde, bir sözleşme ile etkileşime girdiğinizde, ETH gönderdiğinizde veya blok zinciri üzerinde başka herhangi bir şey yaptığınızda söz konusu hesaplama için bir ödeme yapmanız gerekir. Bu ödeme gas olarak hesaplanır ve gas her zaman ETH cinsinden ödenir.


İşleminizin başarılı olup olmadığından bağımsız olarak, bu hesaplama için ödeme yaparsınız. İşleminiz başarısız olsa bile, madenciler veya doğrulayıcılar işleminizi tamamlamalı ve yürütmelidirlerler ve bu da işlem gücü gerektirir. Aynen başarılı bir işlemde olduğu gibi bu hesaplama için de ödeme yapmanız gerekir.


 


### Gas limiti alma


Her bir gas biriminin ne kadar tuttuğunu biliyor, ancak kaç birim gas harcamanız gerektiğini mi merak ediyorsunuz? Pekala, basit bir işlemden söz ediyorsak, yani başka bir adrese ETH veya bir ERC-721 token gönderiyorsanız 21.000 birim gas ödemeniz gerekir. Daha karmaşık bir şey yapıyorsanız [etherscan.io](https://etherscan.io/) gibi bir blok gezgini sizin için iyi bir araçtır. Etkileşim kurmak istediğiniz sözleşmeye gidin ve sözleşmeyle yapılmış işlemleri incelemeye başlayın. Bunu yapmak size diğer kullanıcıların gerçekte ne kadar gas kullandıkları ile ilgili daha iyi bir fikir verecektir.



#### Gas hesaplayıcı


Bir işlem göndermeden önce itibari (fiat) para cinsinden gas maliyetinin ne kadar olacağını tahmin etmekte kullanabileceğiniz birkaç araç mevcuttur. Bunlardan biri [Cryptoneur gas ücreti hesaplayıcıdır](https://www.cryptoneur.xyz/gas-fees-calculator); bu araca işleminizin ayrıntılarını girdiğinizde yerel para biriminizde ve o ağdaki (başlıca EVM uyumlu ağlardan birini seçebilirsiniz) mevcut talebe özgü tahmini gas maliyetini verir.



### 
Genel gas ücret yapısı


[EIP-1559](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1559.md) itibarıyla, bir işlem sahibinin ödediği toplam ücret şu şekilde hesaplanır: **((baz ücret + öncelik ücreti) x kullanılan gas birimi)**.


Daha fazla bilgi için [buraya](https://support.metamask.io/hc/en-us/articles/4404600179227) göz atın.


 


**Lütfen bu ücretin MetaMask tarafından alınmadığını, dolayısıyla bizim ücret iadesi yapamayacağımızı unutmayın.** Bu ücret, işlemin sonuçlandırılması, bir blok içinde doğrulanması ve blok zincirinin güvenceye alınması için madencilere veya doğrulayıcılara ödenir.

