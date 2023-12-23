
#### Baru ke cypto dan web3?


Pergi ke [MetaMask Learn](https://learn.metamask.io/) untuk pengalaman pembelajaran mudah yang direka khusus untuk pendatang baharu di web3. Ia percuma sepenuhnya, tersedia dalam pelbagai bahasa, dan termasuk alat berguna seperti simulasi untuk membantu anda mencari kaki anda dengan MetaMask.



#### *Artikel ini mengandungi penerangan dan pautan kepada sumber yang berpusatkan transaksi dan sebab ia gagal, dan lebih ke bawah, pautan kepada senario biasa transaksi yang gagal serta cara menanganinya:*


* [Anatomi transaksi blok rantai](#h_01G79J04D0EN1VD8VS7C7J7KD1)
* [Masalah biasa](#h_01G79J09NWA8CGR4VYC2PT5B6Y)
* [Pembaikan utama](#h_01G79J0J8JTRPM9MRB76EN1GPP)
* [Sumber tambahan dan langkah seterusnya](#h_01G79J0RP8ZMZ1V1SKQY70TXCT)
* [FAQ](#h_01G79J18RBK27GZCF10CGN9GKP)


 


**Anatomi transaksi blok rantai**
---------------------------------


Semasa kami membincangkan 'transaksi' di rangkaian blok rantai awam, kami biasanya sedang bercakap tentang interaksi antara dua alamat; dalam erti kata lain, token, sama ada ia boleh digunakan atau tidak, atau aset kripto lain yang 'dihantar' dari satu alamat ke alamat yang lain. Terdapat juga transaksi yang dirujuk sebagai "transaksi dalaman", yang merupakan interaksi yang berlaku antara kontrak pintar, dan sebahagian besarnya berada di luar skop artikel ini.



#### Mahu lebih info?


Untuk maklumat lanjut tentang rangkaian blok rantai dan cara ia berfungsi secara umum, lihat [artikel pengenalan kami di sini](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-), dan jika anda tersekat pada sebarang perkataan yang tidak dikenali, glosari [kami sentiasa tersedia.](https://consensys.net/knowledge-base/a-blockchain-glossary-for-beginners/)



Demi kejelasan, tiada apa yang sebenarnya *dihantar* ke mana-mana. Rangkaian blok rantai yang didayakan kontrak pintar seperti Ethereum mempunyai beberapa komponen atau fungsi yang berbeza. Salah satu daripadanya ialah apa yang kita panggil "komputer": Mesin Maya Ethereum, atau EVM, yang mampu menjalankan program ('kontrak pintar'). Tulang belakang sistem, walaubagaimanapun, adalah *lejar teragih*: **bayangkan lembaran yang mengandungi, pada satu sisi, setiap alamat dompet Ethereum, dan setiap alamat mempunyai kolum untuk setiap jenis aset-kripto yang dipegang.** 


Mari kita menggunakan contoh untuk ilustrasi. Katakan Guillaume ingin menghantar transaksi kepada Dolores. Guillaume mempunyai 1.36 ETH dalam akaunnya dan dia merancang untuk menghantar 0.5 ETH kepada Dolores. Kedengaran seperti hari yang baik untuk Dolores, walaupun dalam pasaran beruang.


Guillaume membuka dompet MetaMasknya, memasukkan alamat Dolores, mengkonfigurasi parameter gas yang dia berasa selesa untuk membayar, dan menekan 'hantar'.


Pada ketika ini, transaksi memasuki status pegangan sementara setempat, yang dikenali sebagai *kumpulan memori setempat,*atau *mempool tempatan*. Transaksi kemudiannya akan 'diambil' oleh nod terdekat dalam rangkaian; bergantung pada [tetapan gas](https://metamask.zendesk.com/hc/en-us/articles/360022895972-Using-advanced-gas-controls) Guillaume, transaksinya akan diutamakan (**lebih banyak yang Guillaume sanggup membayar untuk [setiap unit gas](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas), lebih cepat transaksinya akan diproses**), dan disebarkan ke nod lain dalam rangkaian. Nod akan menjalankan tugasnya untuk mengesahkan bahawa Guillaume mempunyai ETH untuk dibelanjakan, dan kemudian akan betul-betul melakukan 'transaksi' tersebut: **lejar akan diubah suai; 0.5 akan didebitkan daripada baki Guillaume, dan 0.5 akan dikreditkan kepada baki Dolores.**


*'Apa-apa sahaja yang dilakukan dalam kehidupan merupakan tanggungjawab sendiri dan tidak boleh diubah':* ETH tidak bergerak melalui rangkaian per se; ia bukan e-mel yang dihantar dari komputer Guillaume ke peti masuk MetaMask Dolores, atau apa-apa seumpamanya. Guillaume menghantar permintaan, **yang telah disahkan oleh [kunci peribadinya melalui MetaMask](https://metamask.zendesk.com/hc/en-us/articles/4404722782107-User-guide-Secret-Recovery-Phrase-password-and-private-keys)**, kepada rangkaian untuk mendebitkan akaunnya dan mengkreditkan akaun Dolores, dan selepas proses pengesahan diprogramkan ke dalam protokol rangkaian, ia selesai. 


#### *Itu sahaja yang berlaku dalam sebuah trasaksi: permintaan kepada lejar untuk mengagihkan semula sesuatu dari satu alamat ke sebuah alamat yang lain.*


 


**Apabila kesilapan berlaku**
-----------------------------


Kesilapan boleh berlaku atas beberapa sebab. Lazimnya, ia 'bersifat perisian': MetaMask mempunyai pepijat, atau sesuatu telah dikonfigurasi dengan salah berkenaan rangkaian yang anda cuba gunakan; terdapat ralat sambungan.


Satu **isu biasa adalah pengguna, dalam percubaan untuk membayar harga yang lebih kurang untuk transaksi mereka, menetapkan had gas yang sangat rendah**, dan keadaan rangkaian sangat sesak sehingga tiada ruang dalam sebarang blok untuk transaksi yang begitu "murah", kadangkala untuk masa yang sangat lama: akhirnya, transaksi ini akan menjadi "lapuk" dan perlu dibatalkan oleh pengguna. 


**Jika anda telah menghantar transaksi dan ia belum dimuktamadkan**, statusnya akan ditunjukkan sebagai "belum selesai" di MetaMask. 


**Jika anda telah menghantar transaksi, dan ia gagal, kemungkinan besar puncanya adalah kekurangan gas**: anda telah "kehabisan gas", dalam erti kata lain, transaksi tersebut mempunyai kos dalam gas yang, apabila didarabkan dengan harga gas, menghasilkan jumlah keseluruhan mata wang asli rangkaian yang lebih besar daripada jumlah yang anda miliki dalam dompet anda. 



#### Maklumat


Untuk maklumat lanjut tentang pengiraan gas, rujuk kepada [panduan gas kami di sini](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas).



Perkara ini boleh berlaku atas beberapa sebab, tetapi satu perkara yang perlu dipertimbangkan adalah transaksi apa yang sedang anda cuba melaksanakan. Menempa NFT pada masa yang paling sibuk boleh mengakibatkan kos gas yang sangat tinggi; jika anda sedang mencuba transaksi baharu atau transaksi percubaan, ia mungkin berbaloi untuk mencubanya di rangkaian ujian sebelum membayar yuran rangkaian yang sebenar.


 


**Menyelesaikan masalah**
-------------------------


### **Faktor Utama #1: Setempat atau Siarkan ke Rangkaian**


Semasa anda mendiagnosis isu transaksi anda, terutamanya apabila ia berkaitan dengan transaksi yang belum selesai, anda perlu melihat sama ada transaksi tersebut masih dalam mempool tempatan anda atau sama ada ia telah sampai ke rangkaian dan tersekat di sana atas apa jua sebab. Jika ia hanya berada di mempool tempatan anda, penyelesaiannya mungkin semudah mengunci dan membuka kunci dompet MetaMask anda (**pastikan anda tahu kata laluan anda dan telah menyandarkan Frasa Pemulihan Rahsia anda sebelum anda berbuat demikian**). Jika ia telah tiba ke rangkaian, penyelesaiannya mungkin lebih rumit.


Untuk maklumat lanjut tentang penyelesaian masalah ini, lihat pautan di bawah.  
  



### **Faktor Utama #2: Nonce**


Perkataan ini boleh membawa maksud beberapa perkara yang berbeza. Ia adalah penguncupan "nombor hanya digunakan sekali", dan dalam konteks ini, ia secara kasarnya bermaksud 'nombor transaksi', bermula dari transaksi pertama yang dibuat oleh alamat penghantaran. Anda boleh menghadapi masalah sebenar jika, sebagai contoh, anda melancarkan dua transaksi berbeza daripada kejadian MetaMask yang berbeza dengan alamat dompet yang sama pada masa yang sama. **Transaksi alamat anda perlu berada dalam susunan tertib menaik mengikut nonce.** Walau bagaimanapun, sama seperti nonces mampu menyebabkan transaksi tersekat, ia juga boleh menjadi kunci untuk melepaskan transaksi.


Untuk maklumat lanjut tentang teknik tersebut, [lihat di sini](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction).


 


**Langkah-langkah Seterusnya**
------------------------------


### *Jika anda mempunyai transaksi yang gagal atau belum selesai, rujuk kepada sumber berikut untuk mendapatkan bantuan.*


#### [Cara menghantar token dari dompet MetaMask anda](https://metamask.zendesk.com/hc/en-us/articles/360015488931)


#### [Cara mempercepatkan atau membatalkan transaksi yang belum selesai](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction)


#### [Mengapakah transaksi saya gagal dengan ralat "Kehabisan Gas"?](https://metamask.zendesk.com/hc/en-us/articles/360038849792-Why-did-my-transaction-fail-with-an-Out-of-Gas-error-How-can-I-fix-it-)


#### [Penyelesaian Masalah Uniswap](https://metamask.zendesk.com/hc/en-us/articles/360053394291-Uniswap-support-and-troubleshooting-tips)


#### [Panduan Pengguna: Gas](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas)


#### [Bolehkah saya menterbalikkan transaksi yang telah disahkan?](https://metamask.zendesk.com/hc/en-us/articles/360059957352-Can-I-reverse-an-already-confirmed-transaction-)


 


**FAQ**
-------


#### 
*S: Sebuah akaun dalam dompet saya mengandungi transaksi yang belum selesai atau masih dalam barisan. Bolehkah saya memulakan transaksi yang lain dari akaun yang berbeza dalam dompet yang sama?*J: Ya, anda boleh. Nonce dikira berdasarkan setiap akaun, bukan setiap dompet.

