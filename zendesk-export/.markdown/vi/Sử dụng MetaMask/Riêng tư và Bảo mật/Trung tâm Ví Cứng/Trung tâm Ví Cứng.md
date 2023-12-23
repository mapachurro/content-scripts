### MetaMask hiện hỗ trợ năm dòng ví cứng: AirGap Vault, Keystone, Lattice, Ledger và Trezor. Những ví này được hỗ trợ trên Tiện ích mở rộng, và sẽ có thể được thêm vào Di động trong các cập nhật sau này.



#### Tôi có đang ở đúng chỗ không?


Nếu bạn đang muốn tìm hiểu ví cứng là gì và vì sao bạn nên sở hữu một cái, hãy tiếp tục đọc.


Nếu bạn muốn tìm hỗ trợ liên quan đến loại ví cứng của bạn, hãy kéo xuống dưới để tìm mục tương ứng.


Nếu bạn đang thiết lập ví cứng lần đầu tiên, **hãy xem [Hướng dẫn Người dùng](https://support.metamask.io/hc/en-us/articles/5450173968283) của chúng tôi để biết những thông số được khuyến nghị.**



#### 


Ví cứng là gì? Và vì sao tôi nên sở hữu một cái?
------------------------------------------------


Để hiểu được ví cứng là gì, bạn cần đi sâu về Ethereum một cchuts. Trước tiên hãy xem định nghĩa "ví" của chúng tôi. Thoạt nhìn, đây là một khái niệm mang tính trực giác: ví cứng là nơi chứa đựng kỹ thuật số để cất giữ tiền điện tử và những thứ khác. Giống như khi sử dụng một chiếc ví thật, bạn có thể để vài loại tiền giấy và vài bức ảnh chú mèo hay gia đình của bạn; trong ví MetaMask, bạn cũng để vài loại tiền và vài chú mèo ảo CryptoKitty và một bức ảnh động về xác sống. Tính đến đoạn này thì chúng vẫn khá giống nhau.


Nhưng hóa ra việc gọi nó là "ví" còn chứa đựng nhiều ý nghĩa hơn. "Ví" là từ tốt để miêu tả cách ta trải nghiệm nó, nhưng lại không thể hiện chính xác những gì đang diễn ra về mặt công nghệ. Những thứ chứa trong "ví" của bạn thật ra gồm có *các tài sản được gán cho địa chỉ của bạn trên chuỗi khối*. Khi ta gửi ETH "cho" ai đó, nó không *đi* đâu cả, nó chỉ đơn giản là bị khấu trừ từ số dư ETH được gán cho địa chỉ của bạn, và được gán lại cho số dư trong địa chỉ nơi bạn đang gửi tiền đến. Hãy nhớ, chuỗi khối công khai cũng được gọi là *công nghệ sổ cái chia sẻ*, và tất cả ví của chúng ta là những đường ở trong sổ cái đó; số dư, số nắm giữ của ta là các cột, và Máy ảo Ethereum (EVM) là người ghi sổ tự động của chúng ta.


Theo nghĩa đó, MetaMask "đơn giản" là một ứng dụng mạng gửi yêu cầu đến chuỗi khối Ethereum: để biết thêm thông tin những tài sản gì được gán cho địa chỉ của bạn; để "gửi" token từ địa chỉ này đến địa chỉ khác, và hơn thế nữa. Nó làm vậy cách sử dụng Cụm Mật khẩu Bí mật của bạn.


Địa chỉ Ethereum công khai của bạn là một nửa của một cặp, và chính xác thì đó là một *cặp khóa mật mã học*. Nửa công khai, hay chính là địa chỉ của bạn, có thể được chia sẻ với bất cứ ai mà không sợ họ có thể tấn công hay cướp tiền của bạn. Nửa không công khai, hay chính là Cụm Mật khẩu Khôi phục Bí mật (còn gọi là "cụm từ hạt giống"), để xác minh bất cứ ai nắm giữ nó có quyền truy cập đầy đủ và toàn diện đối với địa chỉ đó và mọi tài khoản liên quan đến nó. **Đừng quên rằng: "Không giữ khóa thì không phải coin của bạn".**


MetaMask cực kỳ an toàn, và miễn là không ai truy cập được Cụm mật khẩu Khôi phục Bí mật ([bạn đã ghi nó lại ở một nơi ngoại tuyến an toàn rồi, đúng không?](https://support.metamask.io/hc/en-us/articles/4404722782107)), tài khoản của bạn sẽ được an toàn. Có rất nhiều yếu tố khác nằm ngoài tầm kiểm soát của MetaMask và các kỹ sư bảo mật của chúng tôi, ví dụ như độ an toàn của trình duyệt của bạn, liệu người khác có thể sử dụng máy tính của bạn không, hoặc có thể dùng virus để chiếm quyền máy tính của bạn.


Vì lý do này, chúng tôi khuyến nghị nếu bạn đang lưu trữ một lượng tiền giá trị không ngỏ trong ví MetaMask của bạn, hoặc chỉ đơn giản là những tài sản quan trọng với bạn, hãy sử dụng ví cứng để làm hàng rào bảo vệ thứ hai.


Sau khi đã giải thích chi tiết:



Tóm gọn lại
------------


### **Ví cứng là một thiết bị vật lý nằm ngoài máy tính của bạn để giữ an toàn cho các khóa của ví, và đóng vai trò như tường lửa ngăn chặn người khác tấn công những nội dung trong ví của bạn.**


Để giao dịch bằng tiền được đảm bảo trong ví cứng, bạn sẽ cần phải thao tác với ví cứng để chấp thuận giao dịch đó. Bằng cách này, cho dù có người khác chiếm được quyền truy cập ví MetaMask của bạn, họ cũng sẽ không thể chuyển được nội dung trong ví ra ngoài.


 


 AirGap Vault
-------------


* [Kết nối AirGap Vault với MetaMask](https://support.airgap.it/guides/metamask/)
* [AirGap Vault - CH Play trên Android](https://play.google.com/store/apps/details?id=it.airgap.vault&hl=en_US&gl=US)
* [AirGap Vault - App Store trên iOS](https://apps.apple.com/us/app/airgap-vault-secure-secrets/id1417126841)


 Keystone
---------


* [Kết nối Keystone với ví MetaMask của bạn](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/bind-metamask-with-keystone)
* [Cách kết nối Keystone với MetaMask trên Di động và gửi ETH](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile)
* [Cách dùng Keystone với MetaMask trên Di động cho dApp thông qua Wallet Connect](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile/defi-with-metamask-mobile)
* [Cách cấu hình chuỗi EVM trên MetaMask cho Di động](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile/configuring-evm-chains-on-metamask-mobile)
* [Cách tận dụng tính bảo mật của ví cứng bằng cách sử dụng mã QR không có nền](https://consensys.net/blog/news/metamask-x-keystone-how-to-benefit-from-hardware-wallet-security-using-transparent-qr-code/)
* Để hiểu thêm về tuyên bố giá trị bảo mật tăng cường của Keystone, [hãy xem tại đây](https://blog.keyst.one/blind-signing-a-security-black-hole-for-the-ethereum-community-13f909b848b6).
* Để xem những chủ đề chuyên sâu về các tính năng bảo mật của Keystone, bao gồm giới thiệu về entropy tùy chỉnh, [hãy xem tại đây](https://support.keyst.one/general-navigation-guide#advanced-users).


 Lattice
--------


* Với những người mới dùng Lattice, hãy chắc chắn bạn đã được thiết lập đầy đủ: <https://gridplus.io/setup>
* Xem tài liệu của GridPlus giới thiệu về cách sử dụng MetaMask với ví Lattice [tại đây](https://docs.gridplus.io/setup/metamask).


 Ledger
-------


 Ledger có bộ tài liệu mở rộng cho người dùng MetaMask. Sau đây là một số tài liệu giúp bạn bắt đầu:  



* [Thiết lập và sử dụng MetaMask để truy cập tài khoản Ledger Ethereum (ETH) của bạn](https://support.ledger.com/hc/en-us/articles/4404366864657-Set-up-and-use-MetaMask-to-access-your-Ledger-Ethereum-ETH-account?docs=true)
* [Tôi không thấy các token BEP-20 của tôi trong tài khoản Ledger Binance Smart Chain (BSC), tôi có thể làm gì?](https://support.ledger.com/hc/en-us/articles/4406111561617-I-don-t-see-my-BEP-20-tokens-in-my-Ledger-Binance-Smart-Chain-BSC-account-what-can-I-do-?support=true)
* [Cách truy cập tài khoản Ledger Polygon của bạn thông qua MetaMask](https://support.ledger.com/hc/en-us/articles/4418394184209-How-to-access-your-Ledger-Polygon-MATIC-account-via-Metamask?docs=true)


 Trezor
-------


* Xem tài liệu của Trezor về tính khả dụng với MetaMask [tại đây](https://wiki.trezor.io/Apps:MetaMask).
