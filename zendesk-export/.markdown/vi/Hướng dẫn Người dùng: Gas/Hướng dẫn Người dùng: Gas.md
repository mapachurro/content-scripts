
#### Bạn mới làm quen với tiền mã hóa và web3?


Hãy truy cập [Kiến thức MetaMask](https://learn.metamask.io/) để khám phá kiến thức một cách dễ hiểu, được thiết kế dành riêng cho những người mới làm quen với web3. Nó hoàn toàn miễn phí, có sẵn bằng nhiều ngôn ngữ, vào có bao gồm những công cụ hữu ích ví dụ như những mô phỏng để giúp bạn tự tin sử dụng MetaMask.



Gas  là đơn vị đo lường lượng công việc tính toán cần thiết để xử lý các giao dịch và hợp đồng thông minh. Về cơ bản đây là phí giao dịch, và thuật ngữ này bắt nguồn từ Ethereum, trong ngữ cảnh này, nó đề cập đến công việc tính toán được thực hiện trên Máy Ảo Ethereum (EVM). Kể từ khi Ethereum được thành lập, rất nhiều mạng lưới tương thích với EVM (và không tương thích với EVM!) đã xuất hiện và áp dụng những mô hình tương tự.


Thuật ngữ này tương tự với xăng để khởi động động cơ ô tô: nó chính là chi phí hoạt động không ngừng thay đổi, và đôi khi còn đắt đỏ. Các hợp đồng thông minh phức tạp hơn đòi hỏi nhiều gas hơn để cung cấp năng lượng cho công việc tính toán, cũng giống như một chiếc xe to hơn, mạnh mẽ hơn cần nhiều xăng hơn để chạy.


Phương pháp tính phí gas khác nhau tùy thuộc vào từng mạng. Ví dụ: việc tính gas trên Ethereum từng rất phức tạp, nhưng đã được đơn giản hóa đáng kể nhờ việc triển khai Giao thức Cải tiến Ethereum **(EIP) 1559** vào tháng 8/2021 (còn được biết đến với cái tên London Upgrade). Tóm lại, bạn cần trả **phí cơ sở** cho mỗi đơn vị gas, được ***tiêu thụ*** (tức là nó được xóa rồi biến mất) khi hoàn thành giao dịch đó. Bên cạnh phí cơ sở, bạn thêm một khoản **phí ưu tiên**, vẫn là với mỗi đơn vị gas, giá trị của khoản phí này phụ thuộc vào tốc độ bạn muốn giao dịch được thực hiện. 


Trên phạm vi rộng lớn của các mạng tương thích với EVM sẵn có, gas, hoặc các đơn vị thay thế có cách vận hành tương tự, về cơ bản đã trở thành phương thức tiêu chuẩn để tính chi phí giao dịch. Phí được trả bằng token gốc của mạng: ví dụ: bất kỳ giao dịch nào trên Ethereum đều yêu cầu có ETH; sử dụng BSC yêu cầu có BNB; sử dụng Polygon yêu cầu có MATIC. Một số mạng đã áp dụng bán buôn mô hình EIP-1559 của Ethereum, chẳng hạn như Polygon, trong khi những mạng khác đã thực hiện điều chỉnh như Avalanche đối với C-Chain của họ (nó [tiêu thụ cả phí cơ sở và phí ưu tiên](https://docs.avax.network/learn/platform-overview/transaction-fees/#c-chain-fees), thay vì chỉ tiêu thụ phí ưu tiên). 


Nếu bạn muốn tìm hiểu sâu thêm về cách hoạt động của gas trên Ethereum, hãy xem [tại đây](https://ethereum.org/en/developers/docs/gas/).


 


Sau đây là một số **thông tin quan trọng khi làm việc với gas** **trong Meta Mask**:


#### **Hạn mức gas (số đơn vị gas sử dụng)**


 *Giới hạn gas*  là **số lượng đơn vị gas tối đa bạn sẵn sàng trả** để thực hiện một giao dịch hoặc một hoạt động EVM. Các hoạt động khác nhau cần có lượng đơn vị gas khác nhau. Thông thường, một giao dịch gửi ETH hoặc token bình thường tốn **21.000** gas, trong khi đó chấp thuận token ERC-20 cần đến 45.000 gas. Rất nhiều mạng, chẳng hạn như blockchain Harmony tương thích với EVM, sử dụng mô hình tương tự, trong đó các giao dịch tiêu chuẩn cũng có phí 21.000 gas. 



#### Tôi có cần chỉnh sửa hạn mức gas không?


Không! MetaMask tự động đặt hạn mức gas của bạn tùy thuộc vào kiểu giao dịch bạn đang thực hiện. Trong đa số trường hợp, số lượng này đủ để hoàn thành giao dịch của bạn. Nếu bạn muốn kiểm tra hoặc chỉnh sửa nó, hãy chắc chắn bạn đã bật [quản lý gas nâng cao](https://metamask.zendesk.com/hc/en-us/articles/360022895972) (hoặc đang sử dụng Giao diện Gas Nâng cao thử nghiệm) và chạm vào 'Sửa' ở màn hình xác nhận giao dịch.



#### **Phí cơ sở**


Mỗi khối trên mạng Ethereum có phí cơ sở được xác định bởi nguồn cầu của mạng lưới: phí cơ sở dựa trên kích thước của khối phía trước nó, được so sánh với kích thước một khối mục tiêu (kích thước chỉ tổng số gas sử dụng cho mọi giao dịch bao gồm trong khối đó). Nếu kích thước của khối trước vượt quá kích thước khối mục tiêu, phí cơ sở cho khối tiếp theo tăng thêm 12,5%, giúp bạn - người dùng (ví của bạn) biết chắc chắn phí cơ sở cho khối tiếp theo. Tổng phí gas của bạn tối thiểu phải bằng mức giá này để được cân nhắc bao gồm trong khối đó. 


#### **Phí ưu tiên**


Phí ưu tiên còn được gọi là "tiền thưởng cho thợ đào" và khuyến khích họ ưu tiên giao dịch của bạn.


Do đó, liệu số tiền này có đến tay thợ đào hay không thùy thuộc vào [cơ chế đồng thuận](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) họ sử dụng: Mạng chính Ethereum trở thành mạng lưới Bằng chứng cổ phần sau khi sát nhập vào tháng 9/2022, tức là phí ưu tiên sẽ về tay người kiểm định chứ không phải thợ đào. 


#### **Phí tối đa**


Phí tối đa là tổng số tiền toàn cầu được trả cho giao dịch của bạn. Nó được tính như sau: **(****phí cơ sở + phí ưu tiên) x đơn vị gas được sử dụng.** Ban đầu, MetaMask thiết lập số tiền này dựa trên lịch sử của khối trước đó. Tuy nhiên, người dùng có thể điều chỉnh số tiền này thông qua cài đặt tùy chỉnh (xem bên dưới). Chênh lệch giữa phí tối đa cho mỗi gas và (phí cơ sở + phí ưu tiên tối đa mỗi gas) được "trả lại" cho người dùng.


 


### **Các Khái niệm Bổ sung**


#### **Gwei**


Gwei là đơn vị nhỏ nhất của ether, viết tắt của [gigawei](https://ethgasstation.info/blog/gwei/) (hay 1.000.000.000). [Gwei](https://www.investopedia.com/terms/g/gwei-ethereum.asp) được sử dụng cho phí gas, hay đúng hơn là các khoản thanh toán được người dùng chi trả để bù đắp cho năng lượng tính toán cần có để xử lý và xác thực các giao dịch trên blockchain Ethereum. 


Các mạng khác cũng có xu hướng tính chi phí bằng gwei – ví dụ: Fantom, Harmony và Avalanche.


#### **Trượt giá**


Trượt giá là phần trăm chênh lệch dự kiến giữa giá được báo và giá thực thi.


#### **Phí gas**


Phí *gas* chỉ phí giao dịch trên blockchain Ethereum. Đây là phí người dùng phải trả để giao dịch của họ được xác thực hoặc hoàn thành. 


#### **Phí cơ sở**


Được tạo bởi giao thức. Đại diện cho bội số của 'lượng gas sử dụng' tối thiểu cần có để một giao dịch được đưa vào một khối (tức để cho giao dịch được hoàn tất). Đây là phần phí giao dịch được tiêu thụ.


 


### **Kiểm soát Gas Nâng cao**


Nếu bạn muốn đi sâu vào cốt lõi của việc kiểm soát gas (có thể hữu ích nếu bạn đang thử nghiệm một dapp chẳng hạn), MetaMask có thể làm điều đó! Xem bài viết đầy đủ [ở đây](https://metamask.zendesk.com/hc/en-us/articles/360022895972).


 


### **Câu hỏi Thường gặp**


[Tại sao tôi phải trả phí gas cho một giao dịch thất bại?](https://metamask.zendesk.com/hc/en-us/articles/360045439051)


[Có thể hoàn lại phí gas của tôi không?](https://metamask.zendesk.com/hc/en-us/articles/360058370012)


[Làm thế nào để tăng tốc hoặc hủy giao dịch đang chờ xử lý?](https://metamask.zendesk.com/hc/en-us/articles/360015489251)


[Cách ước tính phí gas](https://metamask.zendesk.com/hc/en-us/articles/360059562111)


[Tại sao phí gas của tôi cao vậy?](https://metamask.zendesk.com/hc/en-us/articles/360058751211-Why-my-gas-fees-are-so-high-)


[Lỗi: [ethjs-query] trong khi định dạng kết quả đầu ra từ RPC (lỗi giao dịch định giá thấp)](https://metamask.zendesk.com/hc/en-us/articles/4402538041869)


[Cách khắc phục lỗi "không đủ tiền" hoặc nút xác nhận bị tô xám](https://metamask.zendesk.com/hc/en-us/articles/360044703372)


 


 

