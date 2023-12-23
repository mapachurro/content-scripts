Khi bạn gửi đi một giao dịch trên Ethereum hoặc một mạng tương thích, một phần gas bạn trả là khoản trả cho mạng để xử lý giao dịch của bạn nhanh hơn – yếu tố này được coi là phí ưu tiên. Dù MetaMask sẽ hỗ trợ bạn bằng cách tính toán tổng phí gas bạn cần đặt để giao dịch của bạn được nhận, bạn vẫn có thể phải chờ lâu nếu gửi giao dịch đi với phí gas thấp. Để xem lời khuyên về việc giá gas ảnh hưởng ra sao đến tốc độ hoàn thành giao dịch trong khoảng thời gian tương ứng, hãy tham khảo các nguồn như [Trình theo dõi gas của Etherscan](https://etherscan.io/gastracker) hoặc một trình theo dõi tương tự cho bất kỳ mạng nào bạn đang sử dụng.


Thêm vào đó, đôi khi có những trường hợp có lỗi xảy ra và một giao dịch bị kẹt hoặc phải chờ xử lý rất lâu.


Dù bạn gặp tình huống này vì lý do gì, thì luôn có một số cách khác nhau để giải quyết.


 


### Trước khi bạn thực hiện thêm bất cứ hành động gì, bước đầu tiên bạn cần làm là thoát và tắt trình duyệt hoàn toàn, mở lại trình duyệt, và mở khóa MetaMask (trên di động, chỉ cần đóng ứng dụng rồi mở lại). Nếu làm vậy không giải quyết được vấn đề, hãy tiếp tục với các bước sau:


 


**Tăng tốc một giao dịch**
--------------------------


![Tăng tốc giao dịch MetaMask](https://support.metamask.io/hc/article_attachments/12927043481371)


Hãy thử một trong những tùy chọn dưới đây:


* Chờ đến khi mạng sẵn sàng xử lý giao dịch với giá này
* Nếu bạn chưa làm vậy, hãy nhấp vào nút có ghi **Tăng Tốc**. Thao tác này sẽ cho phép bạn gửi lại chính giao dịch đó, nhưng với phí gas cao hơn để giao dịch được xử lý nhanh hơn. Vì quá trình này sử dụng số Nonce như giao dịch gốc, bạn sẽ không cần trả phí gas hai lần.


Đừng quên rằng **việc tăng tốc giao dịch sẽ làm tăng lượng toekn bạn tiêu tốn cho giao dịch** đó.


 


**Hủy giao dịch - Phương pháp 1: Hủy trong ứng dụng**
-----------------------------------------------------


Để hủy giao dịch, bạn chỉ cần chọn **Hủy** như ảnh chụp màn hình trên đây, nếu bạn chưa làm vậy. Hãy lưu ý, **việc hủy chỉ có thể được *thực hiện* nếu giao dịch vẫn đang trong trạng thái chờ xử lý trên mạng.** Các giao dịch đã được xác nhận sẽ không thể thu hồi.


 


**Hủy giao dịch - Phương pháp 2: Nonce tùy chỉnh**
--------------------------------------------------


Quá trình này bao gồm việc gửi một giao dịch mới với cùng số nonce (là số định danh cho mỗi giao dịch, viết tắt của cụm từ 'số chỉ được sử dụng một lần'). Giao dịch này không thực sự phải có bất kỳ giá trị nào, ví dụ: bạn có thể gửi 0 ETH. Điều quan trọng là bạn phải trả đủ gas để mạng ưu tiên nó.


Khi sử dụng phương thức này, **bạn sẽ cần làm ngược lại tính từ giao dịch đang chờ xử lý xa nhất trong hàng chờ mà bạn muốn hủy**. Ví dụ: bạn không thể tìm cách hủy giao dịch có số nonce 10 khi chưa hủy giao dịch có số nonce 9.


*Những ảnh chụp màn hình dưới đây được chụp vào những thời điểm khác nhau, nên phí gas hiển thị có thể thay đổi, dù là qua các bước. Đừng để nó khiến bạn nản chí! Khi bạn tự làm điều này, MetaMask sẽ tự động cập nhật trong thời gian thực để hiển thị tỷ giá thị trường.*




Tiện ích mở rộng Thiết bị di động


1. Trong cài đặt nâng cao, hãy bật **Tùy chỉnh nonce giao dịch** và **Kiểm soát gas nâng cao.** Cái thứ hai sẽ cho phép bạn điều chỉnh số gas bạn trả và hãy đảm bảo giao dịch hủy của bạn được xử lý trước giao dịch ban đầu mà bạn muốn hủy.



#### Lưu ý:


Tiện ích mở rộng MetaMask hiện đang có sẵn tính năng thử nghiệm có tên [Giao diện Phí Gas Nâng Cao](https://metamask.io/1559/) (đừng nhầm với [quản lý phí gas nâng cao](https://support.metamask.io/hc/en-us/articles/360022895972)). Các bước này có thể được thực hiện dù bạn có bật tính năng này hay không, nhưng hãy nhớ rằng chúng trông sẽ khác. Các bước dưới đây không sử dụng Giao diện Phí Gas Nâng Cao. Đừng quên:



	* Nếu bạn bật Giao Diện Gas Nâng Cao, bạn vẫn sẽ cần bật "Số nounce giao dịch tùy chỉnh".
	* Nếu bạn không bật UI Phí Gas Nâng Cao, bạn cần bật cả 'Quản lý phí gas nâng cao' và 'Số nounce giao dịch tùy chỉnh'.

![Cài đặt MetaMask nâng cao](https://support.metamask.io/hc/article_attachments/12927064113947)
2. **Gửi một giao dịch mới**. Trong giao dịch mới, hãy gửi **ĐẾN** chính bạn, nghĩa là địa chỉ MetaMask công khai của bạn. **Điền vào phần 'Nonce Tùy chỉnh' số nonce giống với của giao dịch vẫn đang chờ xử lý**:


![Metamask_custom_transaction_nonce_Extension.png](https://support.metamask.io/hc/article_attachments/12927064259483)
3. Giờ hãy nhấn 'Chỉnh sửa' bên cạnh 'Phí Gas' (nếu bạn đã bật tính năng thử nghiệm [Giao diện Gas Nâng cao](https://support.metamask.io/hc/en-us/articles/360022895972-Using-advanced-gas-controls#:~:text=%C2%A0-,Enhanced%20Gas%20UI,-Since%20the%20introduction), nó sẽ xuất hiện dưới tên 'Thị trường'). Giờ bạn sẽ thấy các tùy chọn dưới đây:


![Tiện ích mở rộng quản lý phí gas nâng cao MetaMask](https://support.metamask.io/hc/article_attachments/12927065407515)


Để đảm bảo yêu cầu hủy của bạn được coi là ưu tiên và thực hiện trước giao dịch ban đầu, **bạn sẽ cần trả nhiều gas hơn**. Hãy làm theo các hướng dẫn sau:


	* Đặt **giới hạn gas** *của bạn tương đương hoặc cao hơn một chút* so với giao dịch ban đầu.
	* Đặt **phí ưu tiên tối đa** của bạn *cao hơn ít nhất 10%* (đơn vị Gwei) so với phí gas của giao dịch (đang chờ xử lý) ban đầu (ví dụ: nếu giao dịch ban đầu có phí gas là 30 Gwei, hãy đặt phí ưu tiên tối đa trong giao dịch thay thế/hủy lên 33-35 Gwei).
	* Hãy đảm bảo phí tối đa của bạn cao hơn ít nhất 30% so với phí tối đa của giao dịch mà bạn đang thay thế. Ví dụ: nếu phí trước đó của bạn là 150 Gwei, lần này hãy chọn một con số gần 200 Gwei hơn.Hãy kiểm tra trình theo dõi gas như [của Etherscan](https://etherscan.io/gastracker) hoặc [Trạm Gas ETH](https://ethgasstation.info/) để được hướng dẫn về phí tối đa được khuyến nghị.




1. **Trong Cài đặt > Nâng cao, hãy bật "Số nonce giao dịch tùy chỉnh".**
2. **Gửi một giao dịch mới.** Trong giao dịch mới, hãy gửi ĐẾN chính bạn, nghĩa là địa chỉ MetaMask công khai của bạn. **Điền vào phần 'Số Nonce Tùy chỉnh' số nonce giống với của giao dịch vẫn đang chờ xử lý**.


Để tìm cài đặt số nonce tùy chỉnh trong ứng dụng, hãy đến trang xác nhận giao dịch xuất hiện sau khi bạn đã nhập số lượng token và người nhận. Nhấn 'Chỉnh sửa' để thay đổi nó:


![Số nonce giao dịch tùy chỉnh MetaMask di động](https://support.metamask.io/hc/article_attachments/12927068442907)
3. Giờ bạn cần chắc chắn rằng cài đặt phí gas của bạn đã được thiết lập để giao dịch thay thế của bạn được xử lý. Từ màn hình xác nhận giao dịch, chạm vào giá trị phí gas được tô sáng:


![Quản lý phí gas nâng cao MetaMask di động](https://support.metamask.io/hc/article_attachments/12927041593755)


Giờ hãy truy cập vào 'Tùy chọn nâng cao' ở menu xuất hiện.
4. Từ đây, bạn có thể tinh chỉnh phí gas để đảm bảo giao dịch của bạn được nhận. Giờ màn hình bạn thấy sẽ trông như sau:


![Quản lý phí gas nâng cao MetaMask di động](https://support.metamask.io/hc/article_attachments/12927063201691)


Từ đây, hãy điều chỉnh cài đặt phí gas. Hãy làm theo những hướng dẫn này để đảm bảo giao dịch của bạn được nhận:


	* Đặt **giới hạn gas** *của bạn tương đương hoặc cao hơn một chút* so với giao dịch ban đầu.
	* Đặt **phí ưu tiên tối đa** của bạn *cao hơn ít nhất 10%* (đơn vị Gwei) so với phí gas của giao dịch (đang chờ xử lý) ban đầu (ví dụ: nếu giao dịch ban đầu có phí gas là 30 Gwei, hãy đặt phí ưu tiên tối đa trong giao dịch thay thế/hủy lên 33-35 Gwei).
	* Hãy đảm bảo **phí tối đa** của bạn *cao hơn ít nhất 30%* so với phí tối đa của giao dịch mà bạn đang thay thế. Ví dụ: nếu phí trước đó của bạn là 150 Gwei, lần này hãy chọn một con số gần 200 Gwei hơn.Hãy kiểm tra trình theo dõi phí gas như [của Etherscan](https://etherscan.io/gastracker) hoặc [ETH Gas Station](https://ethgasstation.info/) để được hướng dẫn về phí tối đa được khuyến nghị.



