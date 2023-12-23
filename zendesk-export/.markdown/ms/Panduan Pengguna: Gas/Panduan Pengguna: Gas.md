
#### Baru ke cypto dan web3?


Pergi ke [MetaMask Learn](https://learn.metamask.io/) untuk pengalaman pembelajaran mudah yang direka khusus untuk pendatang baharu di web3. Ia percuma sepenuhnya, tersedia dalam pelbagai bahasa, dan termasuk alat berguna seperti simulasi untuk membantu anda mencari kaki anda dengan MetaMask.



Gas merupakan unit ukuran untuk jumlah kerja pengiraan yang diperlukan untuk memproses transaksi dan kontrak pintar. Pada dasarnya sejenis yuran transaksi, istilah ini berasal daripada Ethereum, yang dalam konteksnya merujuk kepada pengiraan yang dilakukan pada Mesin Maya Ethereum (EVM). Sejak Ethereum diasaskan, banyak EVM-serasi (dan tidak-EVM-serasi!) rangkaian telah muncul dan menerima pakai model yang serupa. 


Istilah ini serupa dengan gas yang menggerakkan enjin kereta: ia adalah kos operasi yang turun naik, kadangkala mahal. Kontrak pintar yang lebih kompleks memerlukan lebih banyak gas untuk menggerakkan pengiraannya, sama seperti kereta yang lebih besar dan berkuasa memerlukan lebih banyak gas untuk bergerak.


Kaedah untuk mengira fi gas berbeza bergantung pada rangkaian. Sebagai contoh, pengiraan gas di Ethereum dahulunya sangat rumit, tetapi telah dipermudahkan dengan ketara, dengan pelaksanaan Protokol Penambahbaikan Ethereum **(EIP) 155**9 pada Ogos 2021. (juga dikenali sebagai Baik Taraf London). Pada asasnya, anda membayar **yuran asas**untuk setiap unit gas yang ***terbakar*** (baca: ia dipadam, dan hilang)setelah transaksi selesai dengan jaya. Selain daripada yuran asas ini, anda akan menambah **yuran keutamaan**, sekali lagi bagi setiap unit gas, di mana nilainya bergantung pada seberapa cepat anda ingin transaksi tersebut diselesaikan. 


Merentasi berbagai-bagai rangkaian serasi EVM yang tersedia, gas atau alternatifnya dengan fungsi yang serupa, pada dasarnya telah menjadi kaedah standard untuk mengira kos transaksi. Yuran dibayar dalam token asal rangkaian: sebagai contoh, sebarang transaksi di Ethereum memerlukan ETH; penggunaan BSC memerlukan BNB; penggunaan Polygon memerlukan MATIC. Sesetengah rangkaian telah menggunakan model borong EIP-1559 Ethereum, seperti Polygon, manakala yang lain telah membuat pelarasan, termasuk Avalanche, untuk C-Chain mereka (yang [membakar kedua-dua yuran asas dan yuran keutamaan](https://docs.avax.network/learn/platform-overview/transaction-fees/#c-chain-fees), bukan hanya yuran yang pertama). 


Jika anda ingin membaca pandangan yang lebih mendalam tentang cara gas berfungsi pada Ethereum, lihat[di sini](https://ethereum.org/en/developers/docs/gas/). 


 


Berikut ialah beberapa **butiran penting tentang cara menangani gas** **di MetaMask**:


#### **Had gas (unit gas yang digunakan)**


Had *gas* merupakan **bilangan maksimum unit gas yang anda sanggup bayar** untuk menjalankan transaksi atau operasi EVM. Operasi yang berbeza memerlukan kuantiti unit gas yang berbeza. Kos transaksi biasa menghantar ETH atau token biasanya mencecah **21,000** gas, manakala kelulusan token ERC-20 memerlukan 45,000.  Banyak rangkaian, seperti blok rantai Harmony yang serasi dengan EVM, menggunakan model yang serupa di mana transaksi standard juga berharga 21,000 gas. 



#### Adakah saya perlu mengedit had gas?


Tidak! MetaMask secara automatik menetapkan had gas anda bergantung pada transaksi yang anda cuba laksanakan. Dalam kebanyakan kes, ini sudah memadai untuk melengkapkan transaksi anda. Jika anda ingin menyemaknya atau mengeditnya, pastikan anda mempunyai [kawalan gas lanjutan](https://metamask.zendesk.com/hc/en-us/articles/360022895972) dihidupkan (atau sedang menggunakan UI Gas percubaan Dipertingkat) dan tekan 'Edit' pada skrin pengesahan transaksi.



#### **Yuran asas**


Setiap blok pada rangkaian Ethereum mempunyai yuran asas yang ditentukan oleh permintaan rangkaian: yuran asas adalah berdasarkan saiz blok bagi blok sebelum itu, berbanding dengan saiz blok sasaran (di mana saiz merujuk kepada jumlah jumlah gas yang digunakan untuk semua urus niaga blok yang dimasukkan). Jika saiz blok sebelumnya melebihi sasaran, yuran asas untuk blok seterusnya meningkat sebanyak 12.5%, menjadikan anda, pengguna (atau dompet anda), dengan kepastian mutlak tentang yuran asas blok yang akan datang. Jumlah yuran gas anda mesti memenuhi harga ini sebagai minimum untuk dipertimbangkan untuk dimasukkan ke dalam blok. 


#### **Yuran utama**


*Yuran utama*, juga dirujuk sebagai "tip pelombong", memberi insentif kepada mereka untuk mengutamakan transaksi anda.. 


Sememangnya, sama ada ini benar-benar pergi ke pelombong bergantung kepada [mekanisme konsensus](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) mereka gunakan: Rangkaian utama Ethereum menjadi rangkaian Bukti Pertaruhan berikutan Gabungan pada September 2022, jadi yuran utaman diberikan kepada pengesah dan bukannya pelombong. 


#### **Yuran maksimum**


Yuran maksimum ialah jumlah global keseluruhan yang dibayar untuk transaksi anda. Ia dikira sebagai: **(****yuran asas + yuran keutamaan) x unit gas yang digunakan.** MetaMask pada mulanya menetapkan jumlah ini berdasarkan sejarah blok sebelumnya. Walau bagaimanapun, pengguna boleh mengedit jumlah ini melalui tetapan tersuai (lihat di bawah). Perbezaan antara yuran maksimum bagi setiap gas dan (yuran asas + yuran keutamaan maksimum bagi setiap gas) "dibayar balik" kepada pengguna.


 


### **Konsep Tambahan**


#### **Gwei**


Gwei merupakan unit eter, denominasi terkecil, yang bermaksud [gigawei](https://ethgasstation.info/blog/gwei/) (atau 1,000,000,000). [Gwei](https://www.investopedia.com/terms/g/gwei-ethereum.asp) digunakan untuk fi gas, atau sebaliknya pembayaran yang dibuat oleh pengguna untuk membayar tenaga pengkomputeran yang diperlukan untuk memproses dan mengesahkan transaksi pada blok rantai Ethereum. 


Rangkaian lain juga cenderung mengira kos menggunakan gwei -- sebagai contoh, Fantom, Harmony dan Avalanche.


#### **Gelinciran**


Gelinciran merupakan jangkaan perbezaan peratusan antara harga yang disebut dan harga yang dilaksanakan.


#### **Fi gas**


Fi *gas* merujuk kepada yuran transaksi pada blok rantai Ethereum. Ia apa yang dibayar oleh pengguna untuk mengesahkan atau menyelesaikan transaksi mereka. 


#### **Yuran asas**


Dihasilkan oleh protokol. Mewakili pengganda 'gasUsed' minimum yang diperlukan untuk menyertakan transaksi ke dalam blok (iaitu untuk menyelesaikan transaksi). Ini adalah sebahagian daripada yuran transaksi yang dibakar.


 


### **Kawalan Gas Lanjutan**


Jika anda ingin memahami perkara penting tentang kawalan gas anda (ini boleh membantu jika anda sedang menguji dapp, sebagai contoh), MetaMask boleh melakukannya! Lihat artikel penuh [di sini](https://metamask.zendesk.com/hc/en-us/articles/360022895972).


 


### **FAQ**


[Mengapa saya membayar fi gas untuk transaksi yang gagal?](https://metamask.zendesk.com/hc/en-us/articles/360045439051)


[Bolehkah anda membayar balik fi gas saya?](https://metamask.zendesk.com/hc/en-us/articles/360058370012)


[Bagaimanakah saya mempercepatkan atau membatal transaksi yang belum selesai?](https://metamask.zendesk.com/hc/en-us/articles/360015489251)


[Bagaimana menganggarkan fi gas](https://metamask.zendesk.com/hc/en-us/articles/360059562111)


[Mengapakah fi gas saya begitu tinggi?](https://metamask.zendesk.com/hc/en-us/articles/360058751211-Why-my-gas-fees-are-so-high-)


[Ralat: [ethjs-pertanyaan] semasa memformat output daripada RPC (ralat transaksi terkurang harga)](https://metamask.zendesk.com/hc/en-us/articles/4402538041869)


[Cara membetulkan ralat "dana tidak mencukupi" atau butang pengesahan yang dikelabukan](https://metamask.zendesk.com/hc/en-us/articles/360044703372)


 


 

