### Pagkuha ng presyo ng gas


Kung ikaw ay nasa Ethereum mainnet maaari mong tingnan ang [gas tool ng Etherscan](https://etherscan.io/gastracker) upang matantya ang presyo ng gas ngayon. Mangyaring tandaan na ang presyo ng gas ay nagbabago; palaging sumangguni sa gasolinahan para makita ang kasalukuyang presyo ng gas.


Ang Ethereum network ay nangangailangan ng gas upang magsagawa ng mga transaksyon. Kapag nagpadala ka ng mga token, nakipag-ugnayan sa isang kontrata, nagpadala ng ETH, o gumawa ng anumang bagay sa blockchain, dapat kang magbayad para sa pag-compute na iyon. Ang pagbabayad na iyon ay kinakalkula sa gas, at ang gas ay palaging binabayaran ng ETH.


Nagbabayad ka para sa pagkalkula, magtagumpay man o mabigo ang iyong transaksyon. Kahit mabigo ito, ang mga minero o validator ay dapat i-finalize at isagawa ang iyong transaksyon, na nangangailangan ng computational power. Dapat kang magbayad para sa pag-compute na iyon, tulad ng babayaran mo para sa isang matagumpay na transaksyon.


 


### Pagkuha ng limitasyon ng gas


Kaya, alam mo kung magkano ang halaga ng bawat yunit ng gas, pero gaano karaming yunit ng gas ang kailangan mong gastusin? Kung ito ay isang simpleng transaksyon--halimbawa, ang pagpapadala ng ETH o isang ERC-721 token sa isa pang address, dapat kang gumastos ng 21,000 yunit ng gas. Kung gumagawa ka ng isang bagay na mas kumplikado, mahusay na tool ang isang block explorer, gaya ng [etherscan.io](https://etherscan.io/). Mag-navigate sa kontrata na gusto mong makaugnayan, at simulang suriin ang mga transaksyon na ginawa sa kontrata. Bibigyan ka nito ng mas magandang ideya kung gaano karaming gas ang aktwal na ginagamit ng ibang user.



#### Gas calculator


Mayroong ilang mga tool na magagamit mo upang matantya kung gaano karaming gas ang kailangan mong bayaran ng fiat currency bago ka magsumite ng transaksyon. Ang isang halimbawa ay ang [Cryptoneur gas fee calculator](https://www.cryptoneur.xyz/gas-fees-calculator), na nagbibigay-daan sa iyo sa pag-input ng mga detalye ng iyong transaksyon at gumagawa ng tinatayang halaga ng gas sa iyong local na currency, at nakapartikular sa kasalukuyang demand sa network na iyon (maaari kang pumili mula sa karamihan ng mga pangunahing mga network na compatible sa EVM).



### 
Pangkalahatang istraktura ng gas fee


Batay sa [EIP-1559](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1559.md), ang kabuuang bayad na binabayaran ng isang gumawa ng transaksyon ay kinakalkula bilang: **((base fee + priority fee) x unit ng gas na ginamit).**


Para sa karagdagang impormasyon, tingnan [dito](https://support.metamask.io/hc/en-us/articles/4404600179227).


 


**Pakitandaan na hindi ito bayad na natatanggap ng MetaMask kaya hindi namin ito maire-refund.** Ang bayad na ito ay binabayaran sa mga minero o validator para sa pag-finalize ng transaksyon, pagpapatunay nito sa isang block, at pag-secure ng blockchain.

