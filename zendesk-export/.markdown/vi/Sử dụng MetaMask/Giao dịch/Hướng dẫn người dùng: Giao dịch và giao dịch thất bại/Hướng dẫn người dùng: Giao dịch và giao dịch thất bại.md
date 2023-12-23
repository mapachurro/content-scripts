
#### Bạn mới làm quen với tiền mã hóa và web3?


Hãy truy cập [Kiến thức MetaMask](https://learn.metamask.io/) để khám phá kiến thức một cách dễ hiểu, được thiết kế dành riêng cho những người mới làm quen với web3. Nó hoàn toàn miễn phí, có sẵn bằng nhiều ngôn ngữ, và có bao gồm những công cụ hữu ích ví dụ như những mô phỏng để giúp bạn tự tin sử dụng MetaMask.



#### *Bài viết này giải thích và cung cấp đường dẫn liên kết đến các tài nguyên về chủ đề giao dịch và lý do giao dịch thất bại, và sau đó là đường dẫn liên kết đến các tình huống giao dịch thất bại phổ biến và cách giải quyết chúng:*


* [Phân tích một giao dịch blockchain](#h_01G79J04D0EN1VD8VS7C7J7KD1)
* [Vấn đề thường gặp](#h_01G79J09NWA8CGR4VYC2PT5B6Y)
* [Các cách sửa chữa chính](#h_01G79J0J8JTRPM9MRB76EN1GPP)
* [Tài nguyên bổ sung và các bước tiếp theo](#h_01G79J0RP8ZMZ1V1SKQY70TXCT)
* [Câu hỏi Thường gặp](#h_01G79J18RBK27GZCF10CGN9GKP)


 


**Phân tích một giao dịch blockchain**
--------------------------------------


Khi nói về 'giao dịch' trên mạng blockchain công khai, chúng ta thường nói về các tương tác giữa hai địa chỉ; nói cách khác, là các token, có thể thay thế hoặc không, hoặc các tài sản tiền điện tử khác được 'gửi' từ địa chỉ này sang địa chỉ khác. Ngoài ra còn có các giao dịch được gọi là "giao dịch nội bộ", là các tương tác xảy ra giữa các hợp đồng thông minh và phần lớn nằm ngoài phạm vi của bài viết này.



#### Bạn cần thêm thông tin?


Để biết thêm về các mạng blockchain và cách chúng hoạt động nói chung, hãy xem [bài viết giới thiệu của chúng tôi ở đây](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-), và nếu bạn gặp khúc mắc với bất kỳ từ lạ nào, chúng tôi [luôn có sẵn bảng chú giải thuật ngữ](https://consensys.net/knowledge-base/a-blockchain-glossary-for-beginners/).



Xin được làm rõ, chẳng có gì thực sự được *gửi* đi đâu cả. Một mạng lưới blockchain cho phép hợp đồng thông minh như Ethereum có nhiều thành tố hoặc tính năng khác nhau. Một trong những thành tố đó là cái gọi là "máy tính" - Máy Ảo Ethereum, hay EVM - có khả năng điều hành các chương trình ('hợp đồng thông minh'). Tuy nhiên, 'xương sống' của hệ thống này là một *sổ cái phân tán*: **hãy tưởng tượng một bảng tính một mặt chứa mọi địa chỉ ví Ethereum và mỗi địa chỉ có một cột cho từng loại tài sản tiền điện tử mà nó nắm giữ.** 


Hãy sử dụng ví dụ để minh họa. Giả sử Guillaume muốn gửi một giao dịch đến Dolores. Guillaume có 1,36 ETH trong tài khoản và anh ấy định gửi cho Dolores 0,5 ETH. Có vẻ đây sẽ là ngày đẹp trời cho Dolores, ngay cả khi thị trường giá xuống.


Guillaume mở ví MetaMask của mình lên, nhập địa chỉ của Dolores, thiết lập các thông số gas ở mức anh ấy cảm thấy thoải mái chi trả rồi nhấn 'gửi'.


Tại thời điểm này, giao dịch tiến vào trạng thái tạm giữ cục bộ, được gọi là *vùng nhớ cục bộ*hay *mempool cục bộ*. Sau đó, giao dịch sẽ được 'nhận' bởi nút gần nhất trong mạng; tùy thuộc vào [cài đặt gas](https://metamask.zendesk.com/hc/en-us/articles/360022895972-Using-advanced-gas-controls) của Guillaume mà giao dịch của anh ấy có được ưu tiên hay không (**Guillaume càng sẵn sàng chi trả cho mỗi [đơn vị gas](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas) thì giao dịch của anh ấy càng được xử lý nhanh**) và được truyền đến các nút khác trong mạng. Các nút sẽ thực hiện công việc xác minh rằng Guillaume có ETH để chi dùng và sau đó sẽ thực sự tiến hành 'giao dịch': **sổ cái sẽ được điều chỉnh; 0,5 sẽ được trừ từ số dư của Guillaume và 0,5 sẽ được ghi có vào số dư của Dolores.**


*'Bút sa gà chết':* ETH thực chất không di chuyển qua một mạng; nó không phải là một email được gửi từ máy tính của Guillaume đến hộp thư đến MetaMask của Dolores hay bất cứ thứ gì tương tự như vậy. Guillaume gửi một yêu cầu, **được xác thực bằng [các khóa riêng tư của anh ấy thông qua MetaMask](https://metamask.zendesk.com/hc/en-us/articles/4404722782107-User-guide-Secret-Recovery-Phrase-password-and-private-keys)**, đến mạng để trừ tài khoản của anh ấy và ghi có vào tài khoản của Dolores, và sau khi quá trình xác minh được lập trình vào giao thức của mạng, giao dịch hoàn thành. 


#### *Một giao dịch chỉ có thế: một yêu cầu gửi đến sổ cái để phân bổ lại thứ gì đó từ địa chỉ này sang địa chỉ khác.*


 


**Khi có vấn đề**
-----------------


Có nhiều lý do khiến một vấn đề xảy ra. Thông thường, bản chất của chúng là phần mềm: MetaMask có một lỗi hoặc thứ gì đó bị cấu hình sai liên quan đến mạng mà bạn đang cố sử dụng; có lỗi kết nối.


Một **vấn đề phổ biến là người dùng cố gắng trả ít hơn cho giao dịch của mình nên đặt giới hạn gas rất thấp** và tình trạng mạng bị đầy đến nỗi không có khoảng trống trong bất kỳ khối nào cho một giao dịch "rẻ tiền" như vậy, đôi khi trong một thời gian rất dài: cuối cùng, giao dịch này sẽ trở nên "mất hiệu lực" và người dùng buộc phải hủy.


**Nếu bạn đã gửi một giao dịch và nó chưa được hoàn thành**, trạng thái của nó sẽ được hiển thị là "đang chờ xử lý" trong MetaMask. 


**Nếu bạn đã gửi một giao dịch và giao dịch này thất bại, nguyên nhân rất có thể là do thiếu gas**: bạn đã "hết gas" hay nói cách khác, giao dịch có chi phí tính bằng gas mà khi nhân với giá gas sẽ dẫn đến tổng số tiền tệ gốc của mạng lớn hơn số tiền bạn có trong ví của mình.



#### Thông tin


Để biết thêm về cách tính gas, hãy tham khảo [hướng dẫn về gas của chúng tôi ở đây](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas).



Điều này có thể xảy ra vì nhiều lý do, nhưng một điều cần xem xét là giao dịch mà bạn đang cố gắng thực hiện là gì. Việc đúc một NFT trong thời gian lưu lượng mạng đạt đỉnh có thể rất tốn gas; nếu bạn đang thử một giao dịch mới hoặc giao dịch thử nghiệm, sẽ đáng để thử trên mạng thử nghiệm trước khi trả phí mạng thực.


 


**Khắc phục vấn đề**
--------------------


### **Yếu tố Chính #1: Cục bộ hoặc Truyền phát tới Mạng**


Khi bạn bắt đầu chẩn đoán vấn đề mà giao dịch gặp phải, nhất là với một giao dịch đang chờ xử lý, bạn cần phải xem liệu giao dịch này có còn trong vùng nhớ cục bộ của mình không, hay liệu nó đã được đưa vào mạng và bị mắc kẹt ở đó vì lý do nào đó. Nếu nó vẫn nằm trong vùng nhớ cục bộ của bạn, giải pháp có thể đơn giản là khóa và mở khóa ví MetaMask của bạn (**hãy đảm bảo bạn biết mật khẩu của mình và đã sao lưu Cụm mật khẩu Khôi phục Bí mật trước khi làm như vậy**). Nếu nó đã được đưa vào mạng, giải pháp có thể phức tạp hơn.


Để biết thêm về cách khắc phục các vấn đề này, hãy xem các liên kết bên dưới.  
  



### **Yếu tố Chính #2: Nonce**


Từ này có thể mang nhiều ý nghĩa. Nó là từ rút gọn của "số được sử dụng một lần duy nhất", và trong bối cảnh này, nó đại khái có nghĩa là 'số giao dịch', bắt đầu từ giao dịch đầu tiên được thực hiện bởi địa chị gửi đó. Ví dụ, bạn có thể gặp rắc rối lớn nếu cùng lúc gửi hai giao dịch khác nhau từ hai tài khoản khác nhau trong MetaMask với cùng địa chỉ ví.  **Các giao dịch thuộc địa chỉ của bạn cần phải theo thư tự tăng dần theo số nonce của chúng.** Tuy nhiên, giống như các nonce có khả năng khiến một giao dịch bị kẹt, chúng cũng có thể là chìa khóa để giải thế kẹt đó.


Để biết thêm về kỹ thuật đó, [hãy xem ở đây](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction).


 


**Các Bước Tiếp theo**
----------------------


### *Nếu bạn có giao dịch thất bại hoặc đang chờ xử lý thì hãy tham khảo các tài nguyên sau để được hỗ trợ.*


#### [Cách gửi token từ ví MetaMask của bạn](https://metamask.zendesk.com/hc/en-us/articles/360015488931)


#### [Cách tăng tốc hoặc hủy giao dịch đang chờ xử lý](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction)


#### [Tại sao giao dịch của tôi lại thất bại với lỗi "Hết Gas"?](https://metamask.zendesk.com/hc/en-us/articles/360038849792-Why-did-my-transaction-fail-with-an-Out-of-Gas-error-How-can-I-fix-it-)


#### [Khắc phục sự cố Uniswap](https://metamask.zendesk.com/hc/en-us/articles/360053394291-Uniswap-support-and-troubleshooting-tips)


#### [Hướng dẫn Người dùng: Gas](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas)


#### [Tôi có thể thu hồi giao dịch đã xác nhận không?](https://metamask.zendesk.com/hc/en-us/articles/360059957352-Can-I-reverse-an-already-confirmed-transaction-)


 


**Câu hỏi Thường gặp**
----------------------


#### 
*H: Một tài khoản trong ví của tôi có giao dịch đang chờ xử lý hoặc đang trong hàng đợi. Tôi có thể bắt đầu giao dịch khác từ một tài khoản khác trong cùng ví không?* Đ: Được, bạn có thể. Nonce được tính theo từng tài khoản, không phải theo ví.

