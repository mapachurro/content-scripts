#### Please note, this article is for MetaMask swaps performed with the Swap button within our app or extension (as shown below). ***For all other swap inquiries, please contact the third-party swap system you used, as they will have a better understanding of their system's intricacies, nuances, and issues.****For general information regarding transactions, [see here](https://support.metamask.io/hc/en-us/articles/4410741657499-User-Guide-Transactions).*


![MetaMask Swaps icon locate](https://support.metamask.io/hc/article_attachments/17036969444763)


MetaMask Swaps fetches multiple quotes from various DeFi protocols. When you execute a swap through MetaMask, you interact directly with the liquidity source that offered the best price for your requested trade. MetaMask does its best to optimize each transaction before the swap is submitted. However, just like any on-chain transaction, transaction success is not guaranteed.


The main reason why your swap might have failed is likely to be **slippage**. When you perform a swap, you are agreeing to a price quote.  I**f the price of the swap goes outside of the allowed slippage set (typically 2-3%), it will fail**, in order to prevent you from seeing a huge variance in value when completed. There is a higher risk of slippage if you're trading a pair that includes a volatile asset, as its price is more likely to change whilst the transaction is processing.


If your swap fails, you can retry the swap, but this time, input a higher slippage percentage. Here's how to do so:




Extension Portfolio Mobile


When you're inputting the details of your swap, hit the 'Settings' icon and adjust slippage tolerance. If you want to increase it above 3%, you'll need to click 'Custom' and input your preferred tolerance.


![MetaMask adjust slippage settings extension](https://support.metamask.io/hc/article_attachments/17036969444891)




When you're inputting the details of your swap, hit the 'Advanced Options' button and adjust slippage tolerance. If you want to increase it above 3%, you'll need to click 'Custom' and input your preferred tolerance.


![MetaMask adjust slippage settings portfolio](https://support.metamask.io/hc/article_attachments/17036956340379)




When you navigate to the Swaps screen, look to the bottom-left corner, where it says 'Max slippage 2%' (with 2% being the default). Tap this text to adjust it.


![MetaMask adjust slippage settings mobile](https://support.metamask.io/hc/article_attachments/17036969445275)




Please be aware that this means the swap will still complete even if the price of the token changes more drastically during the pending/confirmation time.


If the swap still won't execute, you can [contact our support team](https://support.metamask.io/hc/en-us/articles/360058969391) so we can investigate the underlying DEXs and assets to ensure it is due to slippage each time. 


When a swap fails, **some gas (ETH) will still be spent**. This ETH goes to the network validators and not to MetaMask. This is unavoidable and part of the nature of blockchain.

