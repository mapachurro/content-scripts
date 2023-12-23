
#### Bạn mới làm quen với tiền mã hóa và web3?


Hãy truy cập [Kiến thức MetaMask](https://learn.metamask.io/) để khám phá kiến thức một cách dễ hiểu, được thiết kế dành riêng cho những người mới làm quen với web3. Nó hoàn toàn miễn phí, có sẵn bằng nhiều ngôn ngữ, và có bao gồm những công cụ hữu ích ví dụ như những mô phỏng để giúp bạn tự tin sử dụng MetaMask.



### Trong bài viết này:


* [Bảo mật của MetaMask khác với các tài khoản web truyền thống ra sao](#h_01FYVAXCSH95CQ08Q0P2VJA5HV)
* [Cụm từ Khôi phục Bí mật là gì?](#h_01FYVAXJQT914HCHEYFPNMEJEA)
* [Nên và không nên với Cụm Mật khẩu Khôi phục Bí mật](#h_01FYVAXSE5C9E4YBCSWT2F2RBQ)
* [Câu hỏi thường gặp về Cụm Mật khẩu Khôi phục Bí mật](#h_01FYVAXZYWJENFWG9K9CJTQFK7)
* [Mật khẩu và MetaMask](#h_01FYVAY5K22PX6926537V8B4SX)
* [Câu hỏi thường gặp về khóa riêng tư](#h_01FYVAYH3ZZ8VW8BPDDADWRC8E)




**MetaMask: một mô hình bảo mật tài khoản** **hoàn toàn khác**
---------------------------------------------------------------


[Công nghệ blockchain công khai](https://metamask.zendesk.com/hc/en-us/articles/360015489611) sử dụng bộ công cụ rất khác biệt để bảo mật dữ liệu người dùng so với các công nghệ trực tuyến truyền thống. Phần lớn chúng ta đã quen với việc tạo tài khoản ứng dụng hoặc dịch vụ, và có thể làm được nhiều việc ví dụ như liên lạc với đội ngũ hỗ trợ để đặt lại mật khẩu hoặc tên người dùng. Chúng ta đã quen với việc ứng dụng lưu trữ dữ liệu của chúng ta, có lẽ là trên một máy tính nào đó thuộc về công ty đó.


Nhưng... MetaMask thì không làm việc như vậy. MetaMask có ba loại **bí mật** khác nhau được sử dụng theo các cách khác nhau để đảm bảo an toàn và riêng tư cho ví và các tài khoản của bạn: Cụm từ Khôi phục Bí mật, mật khẩu, và khóa riêng tư. Chúng ta sẽ lần lượt tìm hiểu về từng bí mật.


 


**Giới thiệu về Cụm từ Khôi phục Bí mật**
-----------------------------------------


Một trong những công nghệ khóa chính (chơi chữ đó) đứng đằng sau MetaMask và phần lớn các công cụ liên quan đến tài khoản người dùng trong giới tiền mã hóa là *cụm từ hạt giống,* hay còn gọi là Cụm Mật khẩu *Khôi phục Bí mật* trong MetaMask.


#### **Tất cả tài khoản của bạn đều được lập trình dẫn xuất từ Cụm Mật khẩu Khôi phục Bí mật của bạn. Bạn có thể coi SRP giống như cái móc chìa khóa, và bạn muốn móc bao nhiêu chiếc khóa riêng tư vào đó cũng được: và mỗi chiếc khóa đó sẽ mở một tài khoản.**


Nếu bạn muốn nghe giải thích kiểu kỹ thuật, thì cụm từ hạt giống ngày nay được hệ thống hóa để sử dụng trong Bitcoin, dựa theo một tiêu chuẩn gọi là Đề xuất Cải tiến Bitcoin 39, hay [BIP-39](https://en.bitcoin.it/wiki/BIP_0039). Nói một cách đơn giản, một chuỗi từ được lựa chọn với tính ngẫu nhiên cao từ một [danh sách từ](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt) cụ thể. Trong MetaMask và rất nhiều công nghệ tương thích với Ethereum, cụm từ hạt giống có 12 từ. Một số cụm từ hạt giống cũ hơn do trình duyệt Brave và một số ví cứng tạo ra sử dụng 24 từ.


Mỗi từ này tương ứng với một dãy số, và khi được đặt theo **một thứ tự nhất định** sẽ giúp người dùng dễ dàng nhớ một dãy số rất, rất dài. Số đó sau đó được sử dụng để tạo các tài khoản của bạn theo *thuyết* tất định, và có lẽ bạn đã từng nghe người ta nhắc đến ví tất định. Trong khoa học máy tính, tất định được dùng để mô tả một quá trình (thường là một kiểu thuật toán) sẽ *luôn* cho kết quả giống nhau. Nói cách khác, **Cụm từ Khôi phục Bí mật của bạn sẽ luôn tạo ra đúng những tài khoản được dẫn xuất từ nó**.


 


### Có một số tính năng quan trọng cần chú ý ở đây:


* **Cụm Mật khẩu Khôi phục Bí mật là bí mật kiểm soát ví của bạn**. Nếu có người biết được bí mật này, họ sẽ có toàn quyền truy cập vào ví của bạn. **MetaMask không giữ SRP của bạn:** **[bạn là người lưu ký ví của bạn.](https://metamask.zendesk.com/hc/en-us/articles/360059952212)** Đại diện của MetaMask sẽ **không bao giờ** hỏi Cụm Mật khẩu Khôi phục Bí mật của bạn, ngay cả trong trường hợp hỗ trợ khách hàng. Nếu có người hỏi nó, rất có khả năng họ đang định lừa hoặc ăn cắp tiền của bạn.
* SRP của bạn được **sử dụng cục bộ để dẫn xuất khóa riêng tư**, mỗi khóa cho một tài khoản/địa chỉ. Các tài khoản được lưu trữ trên blockchain, và những khóa riêng tư này giúp mở khóa những tài khoản đó.
* **Nếu bạn gỡ cài đặt ứng dụng** hoặc tiện ích mở rộng, thì phiên bản dữ liệu trên máy sẽ biến mất (trừ ngoại lệ đáng chú ý là [két](https://metamask.zendesk.com/hc/en-us/articles/360018766351)), nhưng bất cứ giao dịch nào bạn đã thực hiện với phiên bản MetaMask trên máy đó sẽ được ghi lại trên blockchain. Vì vậy, các giao dịch sẽ hiển thị cả trên trình [khám phá khối](https://metamask.zendesk.com/hc/en-us/articles/360057536611) và trong tài khoản khác của MetaMask, miễn là bạn [sử dụng đúng Cụm Mật khẩu Khôi phục Bí mật đó để khôi phục](https://metamask.zendesk.com/hc/en-us/articles/360015289612) (**với các từ có thứ tự giống hệt**). Điều này có nghĩa miễn là bạn có Cụm từ Khôi phục Bí mật, bạn sẽ luôn có thể gỡ cài đặt MetaMask và khôi phục lại ví của bạn.
* **Bên trong ví của bạn, bạn có thể có rất nhiều tài khoản riêng biệt.** Khi MetaMask tạo hoặc khôi phục ví của bạn từ Cụm từ Khôi phục Bí mật, ban đầu nó chỉ tạo tài khoản đầu tiên. Tuy nhiên, bất cứ [tài khoản bổ sung nào bạn tạo có thể được tạo lại](https://metamask.zendesk.com/hc/en-us/articles/360015489271) trong một tài khoản MetaMask trong tương lai. **Vì đây là ví *tất định*, nó sẽ luôn tạo lại đúng những tài khoản đó, theo đúng thứ tự đó. Để tìm hiểu thêm về vấn đề này, hãy xem các câu hỏi thường gặp bên dưới.** Tuy nhiên, xin lưu ý rằng những tài khoản bổ sung (ngoài tài khoản đầu tiên, được gán tên tự động là "Tài khoản 1") sẽ ***không*** được tự động thêm lại vào tài khoản của bạn trong mọi trường hợp. Hãy xem giải thích của chúng tôi [tại đây](https://metamask.zendesk.com/hc/en-us/articles/360015489271-How-to-add-missing-accounts-after-restoring-with-Secret-Recovery-Phrase#:~:text=If%20you%20have,automatically%20re%2Dadded.) để biết thêm thông tin.
* **Bạn có thể [nhập tài khoản](https://metamask.zendesk.com/hc/en-us/articles/360015489331) từ các công nghệ tương thích Ethereum khác vào ví MetaMask.** Để làm vậy, *khóa riêng tư* của tài khoản cụ thể đó được sử dụng. Tuy nhiên, **tài khoản này sẽ không được MetaMask tự động khôi phục trong tài khoản mới; bạn sẽ phải thêm lại nó thủ công**. Vì vậy, nếu bạn có những tài khoản được nhập vào thủ công, **hãy ghi lại khóa riêng tư của chúng, giống như cách bạn đã ghi lại cụm từ hạt giống**, để có thể nhập chúng vào lần nữa trong tương lai.


 


**Nên và không nên với Cụm Mật khẩu Khôi phục Bí mật MetaMask**
---------------------------------------------------------------




**Nên:**

* **Ghi lại Cụm Mật khẩu Khôi phục Bí mật ở một nơi an toàn**. Chúng tôi không thể chỉ chính xác cho bạn là ở đâu, vì nó phụ thuộc vào hoàn cảnh của bạn.
	+ Việc viết tay lại Cụm Mật khẩu Khôi phục Bí mật của bạn là rất quan trọng vì như vậy nó sẽ không bị đánh cắp trực tuyến. Ví dụ, nếu bạn ghi lại nó trong một tập tin trong một thư mục đám mây kết nối bằng mạng internet, về lý thuyết nó có khả năng bị đánh cắp.
* Hãy kiểm tra lại chính tả và xem bạn có viết từng từ theo đúng thứ tự chúng hiển thị không.
* Hãy liên hệ [các kênh chính thức](https://metamask.zendesk.com/hc/en-us/articles/360058230211) của đội ngũ Hỗ trợ MetaMask nếu bạn cần giúp đỡ.





**Không nên:**

* Lưu cụm mật khẩu ở một nơi dễ bị phát hiện hoặc bị tin tặc tấn công, ví dụ như một văn bản được lưu trên đám mây hoặc một email có tiêu đề "cụm từ hạt giống" hoặc một tờ giấy nhớ dán trên máy tính của bạn.
* Cung cấp cụm từ hạt giống cho bất cứ ai, cho dù họ nói mình là người ở đội Hỗ trợ của MetaMask.
* Thay đổi thứ tự của các từ.





 


**Câu hỏi thường gặp về Cụm Mật khẩu Khôi phục Bí mật**
-------------------------------------------------------


### Cụm từ hạt giống của tôi khôi phục lại một tài khoản hoàn toàn khác!


Xin tham khảo bài viết cung cấp kiến thức về chủ đề này [tại đây](https://metamask.zendesk.com/hc/en-us/articles/360058120992). Bên cạnh đó, hãy xem chuỗi bài Cộng đồng [tại đây](https://community.metamask.io/t/restored-metamask-no-coins-are-showing/878/107?u=jacob.cantele) để biết thêm thông tin về bối cảnh.


### Các câu hỏi thường gặp khác về Cụm từ Khôi phục Bí mật:


[Cách tiết lộ Cụm Mật khẩu Khôi phục Bí mật](https://metamask.zendesk.com/hc/en-us/articles/360015290032)


[Cách khôi phục Cụm từ Khôi phục Bí mật](https://metamask.zendesk.com/hc/en-us/articles/360018766351)


[Nhập cụm từ hạt giống từ một phần mềm ví khác: đường dẫn xuất](https://metamask.zendesk.com/hc/en-us/articles/360060331752)


[Hướng dẫn chuyển đổi ví](https://metamask.zendesk.com/hc/en-us/articles/4867408571803)


[Cách nhập một tài khoản](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[Cách kiểm tra hoạt động ví của tôi trên trình khám phá blockchain](https://metamask.zendesk.com/hc/en-us/articles/360057536611)


[Cụm từ Khôi phục Bí mật là gì và làm sao để tôi đảm bảo an toàn cho ví của mình?](https://metamask.zendesk.com/hc/en-us/articles/360060826432)


 


**Mật khẩu và MetaMask**
------------------------


MetaMask sử dụng mật khẩu cho một mục đích duy nhất: để bảo mật cho chính ứng dụng; nói cách khác, là để mở ứng dụng, dù đó là ứng dụng trên Di động hay Tiện ích mở rộng trong trình duyệt. Một khi bạn đã khôi phục hoặc tạo ví của bạn từ Cụm từ Khôi phục Bí mật, bạn sẽ không thường xuyên cần đến nó (**mặc dù bạn nên sao lưu và giữ nó an toàn**), và bạn sẽ dùng mật khẩu của bạn (hay thường xuyên hơn là xác thực sinh trắc học như nhận dạng khuôn mặt hoặc vân tay trên Di động) để mở khóa ứng dụng. Để biết thêm chi tiết, hãy xem bài viết của chúng tôi [ở đây](https://metamask.zendesk.com/hc/en-us/articles/4405451730331).


 


**Khóa riêng tư**
-----------------


Dù Cụm từ Khôi phục Bí mật được dùng để tạo và khôi phục toàn bộ Ví MetaMask của bạn, bao gồm tất cả những tài khoản được tạo bên trong ví đó, mỗi tài khoản vẫn có *khóa riêng tư* của riêng nó. Khóa này có thể sử dụng để nhập tài khoản đó và chỉ mình tài khoản đó sang một ví khác. Tương tự, các tài khoản đơn lẻ từ các công nghệ tiền mã hóa khác có thể được nhập vào ví MetaMask của bạn.


### Câu hỏi thường gặp về khóa riêng tư:


[Tài khoản đã nhập là gì?](https://metamask.zendesk.com/hc/en-us/articles/360015289932)


[Cách nhập một tài khoản](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[Cách xuất khóa riêng tư của một tài khoản](https://metamask.zendesk.com/hc/en-us/articles/360015289632)


[Tôi có thể nhập tài khoản ví Coinbase vào ví MetaMask của mình không?](https://metamask.zendesk.com/hc/en-us/articles/360058485292)

