Apabila anda menghantar transaksi ke Ethereum atau rangkaian yang sepadan, sebahagian daripada gas yang anda bayar adalah tawaran ke rangkaian untuk memproses transaksi anda lebih awal — elemen ini dikenali sebagai yuran utama. Walaupun MetaMask akan membantu anda dengan mengira jumlah bayaran gas yang berkemungkinan besar transaksi anda diambil, anda boleh menunggu lama jika anda menyerahkan dengan harga gas yang rendah. Untuk mendapat nasihat tentang harga gas yang akan mengakibatkan transaksi dimuktamadkan dalam jangka masa yang munasabah, sila rujuk kepada sumber seperti [penjejak gas Etherscan](https://etherscan.io/gastracker), atau penjejak yang serupa untuk sebarang rangkaian yang anda gunakan.


Selain itu, kadang kala akan terdapat keadaan di mana kesilapan berlaku, dan transaksi tersekat, atau tidak diselesaikan untuk masa yang sangat lama.


Tanpa mengira bagaimana anda sampai ke tahap ini, terdapat beberapa cara yang berlainan untuk menanganinya.


 


### Sebelum anda mengambil tindakan selanjutnya, langkah pertama anda adalah untuk keluar dari pelayar anda sepenuhnya, buka semula, dan buka kunci MetaMask (di mudah alih, hanya tutup aplikasi dan buka semula). Jika langkah ini tidak menyelesaikan masalah tersebut, teruskan dengan yang berikut:


 


**Mempercepatkan transaksi**
----------------------------


![MetaMask mempercepatkan transaksi](https://support.metamask.io/hc/article_attachments/12927043481371)


Cuba salah satu pilihan di bawah:


* Tunggu sehingga rangkaian sanggup memproses transaksi pada harga ini
* Jika anda belum berbuat demikian, ketik pada butang yang menyatakan **Mempercepatkan**. Ini akan membolehkan anda menyerahkan semula transaksi yang sama, namun dengan yuran gas yang lebih tinggi, yang sepatutnya membolehkan transaksi diproses dengan lebih cepat. Memandangkan proses ini menggunakan semula nonce yang sama seperti yang asal, anda tidak perlu membayar untuk gas dua kali.


Ingat bahawa **mempercepatkan transaksi akan menambah amaun yang anda belanjakan untuk transaksi tersebut**.


 


**Membatalkan transaksi - Kaedah 1: Pembatalan dalam aplikasi**
---------------------------------------------------------------


Jika anda belum melakukannya, untuk membatalkan transaksi, hanya pilih **Batal**, seperti yang ditunjukkan dalam tangkapan skrin di atas. Sila ambil perhatian, **pembatalan hanya boleh *dicuba* jika transaksi masih belum diselesaikan di rangkaian.** Transaksi yang telah disahkan tidak boleh dibatalkan.


 


**Batalkan transaksi - Kaedah 2: Nonce tersuai**
------------------------------------------------


Proses ini melibatkan penghantaran urus niaga baharu dengan nonce yang sama (nombor pengenalan untuk setiap urus niaga, berasal daripada frasa 'nombor hanya digunakan sekali'). Transaksi sebenarnya tidak perlu mengandungi sebarang nilai -- cth. anda boleh menghantar 0 ETH. Apa yang penting adalah anda membayar gas yang mencukupi untuk rangkaian mengutamakannya. 


Apabila menggunakan kaedah ini, **anda akan perlu untuk bekerja ke belakang daripada transaksi tertunda tertua dalam baris gilir yang ingin anda batalkan.** Sebagai contoh, anda tidak boleh cuba untuk membatalkan transaksi dengan nonce 10 sebelum membatalkan nonce 9. 


*Tangkapan skrin di bawah diambil pada masa yang berbeza, jadi bayaran gas yang ditunjukkan di dalamnya boleh berbeza-beza, walaupun dari langkah ke langkah. Jangan biarkan ini menghalang anda! Apabila anda melakukan ini sendiri, MetaMask akan mengemas kini secara automatik dalam masa nyata untuk menunjukkan kadar pasaran.*




Sambungan Mudah Alih


1. Dalam tetapan lanjut, hidupkan **Sesuaikan transaksi nonce** dan **Kawalan gas lanjutan.** Kawalan gas lanjutan akan membolehkan anda memanipulasi gas yang dibayar dan memastikan transaksi pembatalan anda diproses sebelum transaksi asal yang ingin anda batalkan.



#### Nota:


Sambungan MetaMask buat masa kini mempunyai ciri eksperimen tersedia dipanggil [Yuran Gas Dipertingkatkan UI](https://metamask.io/1559/) (bukan untuk dikelirukan dengan [kawalan gas lanjutan](https://support.metamask.io/hc/en-us/articles/360022895972)). Langkah-langkah ini boleh dilakukan sama ada anda telah menghidupkannya atau tidak, tetapi ingat bahawa ia akan kelihatan berbeza. Langkah-langkah di bawah tidak menggunakan Gas UI Dipertingkatkan. Ingatlah:



	* Jika anda telah menghidupkan UI Gas Dipertingkat, anda masih perlu menghidupkan 'Sesuaikan transaksi sekali-kali' juga.
	* Jika anda tidak menghidupkan UI Gas Dipertingkat, anda perlu menghidupkan kedua-dua 'Kawalan gas lanjutan' dan 'Sesuaikan transaksi sekali-kali'.

![MetaMask tetapan lanjutan](https://support.metamask.io/hc/article_attachments/12927064113947)
2. **Hantar transaksi baharu**. Dalam transaksi baharu, hantar **KEPADA** anda sendiri, maksudnya, alamat awam MetaMask anda. **Isikan 'Nonce Tersuai' dengan nonce yang sama dengan transaksi yang masih belum diselesaikan**:


![Metamask_tersuai_transaksi_nonce_Sambungan.png](https://support.metamask.io/hc/article_attachments/12927064259483)
3. Sekarang, tekan 'Edit' di sebelah 'Fi Gas' (jika anda telah menghidupkan [UI Gas Lanjutan uji kajiI](https://support.metamask.io/hc/en-us/articles/360022895972-Using-advanced-gas-controls#:~:text=%C2%A0-,Enhanced%20Gas%20UI,-Since%20the%20introduction), ia akan muncul sebagai 'Pasaran'). Anda kini akan melihat pilihan di bawah:


![Sambungan kawalan gas termaju MetaMask](https://support.metamask.io/hc/article_attachments/12927065407515)


Untuk memastikan permintaan pembatalan anda diterima sebagai keutamaan, dan sebelum permintaan yang asal, **anda akan perlu membayar lebih banyak untuk gas**. Ikut arahan ini:


	* Tetapkan **had gas** *anda setanding dengan atau lebih tinggi sedikit* daripada transaksi asal anda.
	* Tetapkan **fi keutamaan maksimum** anda kepada *sekurang-kurangnya 10% lebih tinggi* (dalam Gwei) daripada fi gas transaksi asal (belum selesai) (cth. jika transaksi tersebut mempunyai fi gas sebanyak 30 Gwei, tetapkan fi keutamaan maksimum pada transaksi penggantian/pembatalan kepada 33-35 Gwei).
	* Pastikan fi maksimum anda sekurang-kurangnya 30% lebih tinggi daripada fi maksimum transaksi yang anda gantikan. Sebagai contoh, jika fi anda yang sebelumnya ialah 150 Gwei, pilih jumlah yang lebih hampir dengan 200 Gwei kali ini.Semak penjejak gas seperti [Stesen Gas Etherscan](https://etherscan.io/gastracker) atau [ETH](https://ethgasstation.info/) untuk mendapatkan panduan tentang fi maksimum yang dicadangkan.




1. **Dalam Tetapan > Lanjutan, hidupkan 'Transaksi tersuai nonce'.**
2. **Hantar transaksi baharu.** Dalam transaksi baharu, hantar KEPADA anda sendiri, maksudnya, alamat awam MetaMask anda. **Isikan 'Nonce Tersuai' dengan nonce yang sama dengan transaksi yang masih belum diselesaikan**.


Untuk mencari tetapan nonce tersuai dalam aplikasi, pergi ke skrin pengesahan transaksi, yang muncul selepas anda memasukkan kuantiti token dan penerima. Tekan 'Edit' untuk mengubahnya:


![MetaMask transaksi tersuai nonce Mudah alih](https://support.metamask.io/hc/article_attachments/12927068442907)
3. Kini anda perlu memastikan tetapan gas anda dikonfigurasikan supaya transaksi penggantian anda diproses. Daripada skrin pengesahan transaksi, ketik nilai gas yang ditandakan:


![Gas termaju MetaMask mengawal mudah alih](https://support.metamask.io/hc/article_attachments/12927041593755)


Sekarang akses 'Pilihan lanjutan' daripada menu yang muncul.
4. Dari sini, anda boleh melaraskan gas dengan tepat untuk memastikan transaksi anda diambil. Anda kini akan melihat skrin yang kelihatan seperti ini:


![Gas termaju MetaMask mengawal mudah alih](https://support.metamask.io/hc/article_attachments/12927063201691)


Dari sini, selaraskan tetapan gas. Ikut arahan ini untuk memastikan transaksi anda di pilih:


	* Tetapkan **had gas** *anda setanding dengan atau lebih tinggi sedikit* daripada transaksi asal anda.
	* Tetapkan **fi keutamaan maksimum** anda kepada *sekurang-kurangnya 10% lebih tinggi* (dalam Gwei) daripada fi gas transaksi asal (belum selesai) (cth. jika transaksi tersebut mempunyai fi gas sebanyak 30 Gwei, tetapkan fi keutamaan maksimum pada transaksi penggantian/pembatalan kepada 33-35 Gwei).
	* Pastikan **yuran maksimum** anda adalah *sekurang-kurangnya 30% lebih tinggi* daripada yuran maksimum transaksi yang anda gantikan. Sebagai contoh, jika yuran anda yang sebelumnya ialah 150 Gwei, pilih jumlah yang lebih hampir dengan 200 Gwei kali ini.Semak penjejak gas seperti [Stesen Gas ETH](https://etherscan.io/gastracker) atau [Etherscan](https://ethgasstation.info/) untuk panduan tentang yuran maksimum yang dicadangkan.



