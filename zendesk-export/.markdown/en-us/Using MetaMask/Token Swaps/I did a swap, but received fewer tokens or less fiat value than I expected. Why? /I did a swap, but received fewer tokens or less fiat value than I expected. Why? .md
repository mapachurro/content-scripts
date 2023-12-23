
#### Check here first!


See the troubleshooting steps [here](https://support.metamask.io/hc/en-us/articles/360028059272). This advice applies to normal transactions *and*Swaps transactions, so make sure you've taken a look at them before you attribute the issue to the possibilities listed below. 



Please note: this article is for MetaMask Swaps performed with the swap button within our app or extension.**For all other swap inquiries, please contact the third-party swap system you used, as they will have a better understanding of their system's intricacies, nuances, and issues.**


There are two main reasons why a swap might end up with less "value" in terms of dollar (fiat) amount.


1. **Price slippage:** Every swap has a preset price slippage limit. This limit prevents the swap from completing at an unfavorable price if the price changes after your order is submitted. Let's say the slippage is set to 5%, and you bought 100 tokens. The price could change, but you will not receive fewer than 95 tokens. If you want to change your slippage tolerance, head to Advanced Options whilst you're configuring the swap.


![MetaMask user guide_swaps slippage](https://support.metamask.io/hc/article_attachments/10023496271131)


2. **Price difference (or price impact):** Before approving a swap quote, check to see if there is a price difference warning. This warning generally appears if there is low liquidity for a given token, and/or if your order size is large. For more detail on how this phenomenon works, see our [blog post](https://consensys.net/blog/metamask/price-impact-the-first-gotcha-of-defi-markets/). It is important to review this warning to see the difference in the value of the token you currently hold and the value of the token you are swapping to. Our warning for this will look something like this:


![MetaMask price difference warning](https://support.metamask.io/hc/article_attachments/10023529748507)


MetaMask Swaps fetches multiple quotes from various DeFi protocols. When you execute a swap through MetaMask, you interact directly with the liquidity source that offered the best price for your requested trade. MetaMask does its best to optimize each transaction before the swap is submitted.


However, MetaMask cannot guarantee that every transaction will be successful because the market and network conditions can vary dramatically, especially when highly volatile assets are traded.

