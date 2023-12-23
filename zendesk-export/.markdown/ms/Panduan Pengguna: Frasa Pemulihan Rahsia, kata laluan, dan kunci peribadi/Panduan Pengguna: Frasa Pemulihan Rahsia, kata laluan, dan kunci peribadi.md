
#### Baru ke cypto dan web3?


Pergi ke [Belajar MetaMask](https://learn.metamask.io/) untuk pengalaman pembelajaran mudah yang direka khusus untuk pendatang baharu di web3. Ia percuma sepenuhnya, tersedia dalam pelbagai bahasa, dan termasuk alat berguna seperti simulasi untuk membantu anda mencari kaki anda dengan MetaMask.



### Dalam artikel ini:


* [Cara keselamatan MetaMask berbeza dengan akaun web tradisi](#h_01FYVAXCSH95CQ08Q0P2VJA5HV)
* [Apakah Frasa Pemulihan Rahsia?](#h_01FYVAXJQT914HCHEYFPNMEJEA)
* [Frasa Pemulihan Boleh dan Tidak Boleh Rahsia](#h_01FYVAXSE5C9E4YBCSWT2F2RBQ)
* [Frasa Pemulihan Rahisa Soalan Lazim](#h_01FYVAXZYWJENFWG9K9CJTQFK7)
* [Kata laluan dan MetaMask](#h_01FYVAY5K22PX6926537V8B4SX)
* [Kekunci Peribadi Soalan Lazim](#h_01FYVAYH3ZZ8VW8BPDDADWRC8E)




**MetaMask: satu model akaun berbeza** **keselamatan**
-------------------------------------------------------


[Teknologi rantai kunci Awam](https://metamask.zendesk.com/hc/en-us/articles/360015489611) menggunakan set alat berbeza untuk melindungi data pengguna, berbanding teknologi atas talian tradisi. Kebanyakan daripada kita terbiasa membuat akaun dengan aplikasi atau perkhidmatan dan boleh, sebagai contoh, menulis kepada sokongan untuk menetapkan semula kata laluan atau nama pengguna kami. Kami sudah biasa dengan aplikasi menyimpan data kami, mungkin pada sejenis komputer milik syarikat.


Namun... MetaMask tidak berfungsi sedemikian. MetaMask mempunyai tiga jenis **rahsia** berbeza yang digunakan dalam cara berbeza untuk menimpan dompet anda, dan akaun anda, peribadi dan selamat: Frasa Pemulihan Rahsia, kata laluan, dan kunci peribadi. Kami akan membimbing anda melalui rahsia-rahsia ini satu demi satu.


 


**Pengenalan ke Frasa Pemulihan Rahsia**
----------------------------------------


Salah satu kunci (anda akan melihat apa yang saya lakukan di sana) teknologi yang mendasari MetaMask, dan kebanyakan alat berkaitan akaun pengguna dalam ruang crypto ialah *benih frasa,*atau seperti yang dirujuk dalam MetaMask, *Frasa Pemulihan Rahsia*anda. 


#### **Semua akaun anda diperoleh secara matematik daripada Frasa Pemulihan Rahsia anda. Anda boleh menganggap SRP seperti cincin kunci, dan ia memegang seberapa banyak kunci peribadi yang anda mahukan: dan setiap satu daripada kunci tersebut mengawal sesebuah akaun.**


Sekarang, jika anda mahukan penjelasan teknikal: Frasa benih seperti yang kita ketahui hari ini dikodkan untuk penggunaan dalam Bitcoin, mengikut piawaian yang disebut sebagai Cadangan Penambahbaikan Bitcoin 39, atau [BIP-39](https://en.bitcoin.it/wiki/BIP_0039). Secara ringkasnya, satu siri perkataan dipilih dengan tahap rawak yang tinggi daripada yang tertentu [senarai perkataan](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt). Dalam MetaMask dan banyak teknologi lain yang serasi dengan Ethereum, terdapat 12 perkataan dalam frasa benih. Beberapa benih lama yang dihasilkan oleh pelayar Brave, dan beberapa dompet perkakasan, menggunakan frasa 24 perkataan.


Setiap satu daripada perkataan ini sepadan dengan satu siri nombor, dan apabila ditempatkan dalam **aturan tertentu**, mewakili cara yang lebih mesra pengguna untuk mengingati nombor yang sangat panjang. Nombor itu kemudiannya digunakan untuk *secara deterministik* menjana akaun anda, dan anda mungkin mendengar orang merujuk kepada dompet deterministik. Dalam sains komputer, deterministik digunakan untuk menerangkan proses (biasanya sejenis algoritma) yang akan *sentiasa*mengeluarkan hasil yang sama. Dalam erti kata lain, **Frasa Pemulihan Rahsia anda akan sentiasa menghasilkan set akaun yang sama yang diperolehi daripadanya**.


 


### Terdapat beberapa ciri penting yang perlu dinotakan di sini:


* **Frasa Pemulihan Rahsia ialah rahsia yang mengawal dompet**. Jika seseorang mempunyai rahsia ini, mereka mempunyai akses penuh kepada dompet. **MetaMask tidak menyimpan SRP anda:** **[anda ialah penjaga dompet anda.](https://metamask.zendesk.com/hc/en-us/articles/360059952212)** Wakil MetaMask tidak **akan** meminta Frasa Pemulihan Rahsia anda, walaupun dalam senario sokongan pelanggan. Jika seseorang memintanya, mereka mungkin cuba menipu anda atau mencuri dana anda.
* SRP anda **digunakan secara tempatan untuk mendapatkan kunci peribadi**, satu setiap akaun/alamat. Akaun disimpan di blok rantai, dan kunci peribadi ini membuka kunci akaun tersebut.
* **Jika anda menyahpasang aplikasi** atau sambungan, makan versi tempatan data akan hilang (pengecualian yang ketara adalah [peti besi](https://metamask.zendesk.com/hc/en-us/articles/360018766351)), tetapi mana-mana transaksi yang anda lakukan dengan versi tempatan MetaMask akan direkod di blok rantai. Oleh yang demikian, transaksi tersebut harus dicerminkan di kedua-dua [blok penjelajah](https://metamask.zendesk.com/hc/en-us/articles/360057536611), dan dalam contoh lain MetaMask, selagi anda [memulihkan dengan menggunakan Frasa Pemulihan Rahsia yang sama](https://metamask.zendesk.com/hc/en-us/articles/360015289612) (**dengan perkataan dalam aturan yang sama**). Ini bermakna selagi anda mempunyai Frasa Pemulihan Rahsia anda, anda sentiasa boleh menyahpasang MetaMask dan memulihkan dompet anda.
* **Dalam dompet anda, anda boleh mempunyai jumlah akaun berbeza yang besar.** Apabila MetaMask mencipta atau memulihkan dompet anda daripada Frasa Pemulihan Rahsia, ia pada mulanya hanya menghasilkan akaun pertama. Walaubagaimanapun, mana-mana[akaun tambahan yang anda cipta boleh dicipta semula](https://metamask.zendesk.com/hc/en-us/articles/360015489271) dalam satu contoh masa hadapan MetaMask. **Memandangkan dompet adalah *deterministik*, ia akan sentiasa mencipta semula akaun yang sama, dalam aturan yang sama. Untuk lebih lanjut tentang isu ini, lihat Soalan Lazim di bawah.**  Walau bagaimanapun, ambil perhatian bahawa akaun tambahan (di luar yang pertama, dilabelkan secara automatik 'Akaun 1') tidak ***akan***secara automatik ditambah semula ke akaun anda dalam semua keadaan. Sila lihat penjelasan kami [di sini](https://metamask.zendesk.com/hc/en-us/articles/360015489271-How-to-add-missing-accounts-after-restoring-with-Secret-Recovery-Phrase#:~:text=If%20you%20have,automatically%20re%2Dadded.) untuk maklumat lebih lanjut.
* **Ia adalah mungkin untuk [mengimport akaun](https://metamask.zendesk.com/hc/en-us/articles/360015489331) daripada teknologi yang serasi dengan Ethereum ke dalam dompet MetaMask.** Untuk melakukannya, *kunci peribadi* akaun tertentu tersebut digunakan. Walaubagaimanapun, **akaun ini tidak akan secara automatik dipulihkan oleh MetaMask dalam keadaan yang lain; anda perlu menambahnya semula secara manual**. Oleh itu, jika anda telah mengimport akaun secara manual, **perhatikan kunci peribadi mereka, dengan cara yang sama anda melakukan frasa benih anda**, supaya boleh mengimport mereka semula pada masa hadapan.


 


**Frasa Rahsia Pemulihan MetaMask: Apa yang boleh Buat dan Jangan Buat**
------------------------------------------------------------------------




**Buat:**

* **Tulis Frasa Pemulihan Rahsia anda di tempat selamat**. Kami tidak boleh memberitahu anda dengan tepat di mana, kerana ia bergantung pada keadaan anda.
	+ Kepentingan menulis dengan tangan Frasa Pemulihan Rahsia anda ialah ia tidak boleh dicuri atas talian. Jika anda menyimpannya dalam fail folder penyimpanan awan yang mempunyai pautan internet, sebagai contoh, ia secara teorinya boleh dicuri.
* Semak semula ejaan anda dan anda menulis setiap perkataan dalam susunan yang sama yang diberikan.
* Hubungi Sokongan MetaMask [saluran rasmi](https://metamask.zendesk.com/hc/en-us/articles/360058230211) jika anda perlukan bantuan.





**Apa yang Jangan Buat:**

* Simpan di lokasi yang mudah ditemui atau mudah digodam; cth. dalam dokumen atau e-mel yang disimpan awan bertajuk "Frasa Benih"; pada nota post-it yang melekat pada komputer anda.
* Memberikan benih frasa anda kepada sesiapa, walaupun jika mereka mengatakan mereka dari Sokongan MetaMask.
* Menukar aturan perkataan.





 


**Frasa Pemulihan Rahisa: Soalan Lazim**
----------------------------------------


### Frasa benih saya disimpan di akaun berbeza!


Sila rujuk artikel asas pengetahuan tentang topik ini [di sini](https://metamask.zendesk.com/hc/en-us/articles/360058120992). Selain itu, lihat benang Komuniti[di sini](https://community.metamask.io/t/restored-metamask-no-coins-are-showing/878/107?u=jacob.cantele) untuk maklumat latar belakang dan konteks lebih lanjut.


### Frasa Pemulihan Rahsia Lain Soalan Lazim:


[Cara mendedahkan Frasa Pemulihan Rahsia anda](https://metamask.zendesk.com/hc/en-us/articles/360015290032)


[Cara memulihkan Frasa Pemulihan Rahsia anda](https://metamask.zendesk.com/hc/en-us/articles/360018766351)


[Mengimport benih frasa dari perisian dompet lain: laluan terbitan](https://metamask.zendesk.com/hc/en-us/articles/360060331752)


[Panduan Migrasi Wallet](https://metamask.zendesk.com/hc/en-us/articles/4867408571803)


[Cara untuk mengimport satu akaun](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[Cara untuk memeriksa aktiviti dompet saya di penjelajah blok rantai](https://metamask.zendesk.com/hc/en-us/articles/360057536611)


[Apakah itu Frasa Pemulihan Rahsia dan bagaimana saya memastikan dompet saya selamat?](https://metamask.zendesk.com/hc/en-us/articles/360060826432)


 


**Kata laluan dan MetaMask**
----------------------------


MetaMask menggunakan kata laluan untuk satu tujuan: untuk melindungi aplikasi itu sendiri; dengan kata lain, untuk membuka aplikasi, sama ada aplikasi Mudah Alih atau Sambungan dalam penyemak imbas. Sebaik sahaja anda memulihkan atau mencipta dompet anda daripada Frasa Pemulihan Rahsia anda, anda tidak akan memerlukannya secara tetap (**walaupun anda harus menyimpannya disandarkan dan selamat**), dan anda akan menggunakan kata laluan anda (atau lebih biasa pada Mudah Alih, pengesahan biometrik seperti pengecaman muka atau cap jari anda) untuk membuka kunci aplikasi. Untuk maklumat lebih lanjut, lihat artikel kami [di sini](https://metamask.zendesk.com/hc/en-us/articles/4405451730331).


 


**Kunci Peribadi**
------------------


Walaupun Frasa Pemulihan Rahsia digunakan untuk mencipta dan memulihkan keseluruhan Dompet MetaMask anda, termasuk semua akaun yang dibuat dalam dompet itu, setiap akaun mempunyai *kunci peribadi*. Kunci ini boleh digunakan untuk mengimport akaun tersebut, dan hanya akaun tersebut, ke dalam dompet berbeza. Begitu juga, akaun tunggal daripada teknologi kripto lain boleh diimport ke dompet MetaMask anda.


### Kunci Peribadi Soalan lazim:


[Apakah akaun yang diimport?](https://metamask.zendesk.com/hc/en-us/articles/360015289932)


[Cara untuk mengimport satu akaun](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[Cara untuk mengimport kunci peribadi akaun](https://metamask.zendesk.com/hc/en-us/articles/360015289632)


[Bolehkah saya mengimport akaun dompet Coinbase ke dompet MetaMask saya?](https://metamask.zendesk.com/hc/en-us/articles/360058485292)

