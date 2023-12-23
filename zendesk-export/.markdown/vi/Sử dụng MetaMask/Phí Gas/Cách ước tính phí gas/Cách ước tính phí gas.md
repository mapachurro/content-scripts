### Tính giá gas


Nếu bạn đang trên mạng chính Ethereum, bạn có thể kiểm tra [công cụ phí gas của Etherscan](https://etherscan.io/gastracker) để ước tính giá gas hôm nay.  Hãy lưu ý rằng giá gas luôn biến động; hãy luôn tham khảo trạm gas để xem giá gas hiện tại.


Mạng Ethereum yêu cầu gas để thực hiện giao dịch. Khi bạn gửi token, tương tác với hợp đồng, gửi ETH hoặc làm bất kỳ điều gì khác trên blockchain, bạn phải trả tiền cho công việc tính toán đó. Khoản tiền phải trả này được tính bằng gas và gas luôn được trả bằng ETH.


Bạn cần thanh toán cho công việc tính toán, bất kể giao dịch của bạn thành công hay thất bại. Dù thất bại, các thợ đào hoặc người kiểm định vẫn phải hoàn thành và thực hiện giao dịch của bạn, điều này cần công suất tính toán. Bạn phải trả tiền cho công việc tính toán đó, giống như bạn sẽ trả cho một giao dịch thành công.


 


### Tính giới hạn gas


Vậy, bạn biết mỗi đơn vị gas giá bao nhiêu, nhưng bạn cần bao nhiêu đơn vị gas để chi trả? Chà, nếu đó là một giao dịch đơn giản--như gửi ETH hoặc token ERC-721 đến một địa chỉ khác chẳng hạn, bạn cần trả 21.000 đơn vị gas. Nếu bạn làm điều gì đó phức tạp hơn thì trình khám phá khối, như [etherscan.io](https://etherscan.io/), là công cụ hữu ích. Di chuyển đến hợp đồng bạn muốn tương tác và bắt đầu kiểm tra giao dịch đã được thực hiện với hợp đồng. Điều này sẽ cho bạn một cái nhìn rõ hơn về việc những người dùng khác thực sự đã sử dụng bao nhiêu gas.



#### Bộ tính phí gas


Có một số công cụ giúp bạn ước tính phí gas sẽ tương đương với bao nhiêu tiền pháp định trước khi bạn gửi giao dịch đi. Một trong số những công cụ này là Bộ [tính phí gas Cryptoneur](https://www.cryptoneur.xyz/gas-fees-calculator), cho phép bạn nhập thông tin chi tiết giao dịch của bạn và ước tính phí gas theo đơn vị tiền tệ địa phương của bạn, và tương thích với nguồn cầu hiện tại của mạng lưới đó (bạn có thể chọn trong số những mạng tương thích EVM phổ biến nhất).



### 
Cấu trúc tổng phí gas


Đối với [EIP-1559](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1559.md), tổng chi phí mà người tạo giao dịch phải trả được tính là: **( (phí cơ sở + phí ưu tiên) x đơn vị gas đã sử dụng)**. 


Để biết thêm thông tin, hãy xem [ở đây](https://support.metamask.io/hc/en-us/articles/4404600179227).


 


**Hãy lưu ý rằng đây không phải là khoản phí mà MetaMask nhận được, vì vậy chúng tôi không thể hoàn lại.** Phí này được trả cho các thợ đào hoặc người kiểm định để hoàn thành giao dịch, xác thực nó vào một khối và bảo mật blockchain.

