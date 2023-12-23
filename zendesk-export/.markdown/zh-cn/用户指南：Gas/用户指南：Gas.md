
#### 加密货币和 web3 的新手？


前往 [MetaMask Learn](https://learn.metamask.io/) 获得专为 web3 新手设计的直接学习体验。完全免费，提供多种语言版本，并包含有用的工具，例如模拟，帮助您熟悉 MetaMask。



Gas 是处理交易和智能合约所需计算工作量的计量单位。该术语来源于以太坊，本质上是一种交易费，是指在以太坊虚拟机 (EVM) 上承担的计算。 自以太坊成立以来，许多兼容 EVM（和不兼容 EVM）的 网络应运而生，并且采用类似的模式。


该术语类似于为汽车发动机提供动力的汽油：不停波动，有时是昂贵的运营成本。 智能合约越复杂，计算就需要越多的 Gas，如同汽车越大、动力越强，所需汽油就越多。


Gas 费的计算方法因网络而异。例如，以太坊上 Gas 的计算曾经非常复杂，2021 年 8 月实施《以太坊改善协议》**(EIP) 1559**（也称为“伦敦升级”）后，计算大大简化。基本上，您为每单位 gas 支付一笔**基本费用**，该 gas 在***成功完成交易之后***，便会销毁（即删除并消失）。在基本费的基础上，您还要为每单位 Gas 支付一笔**优先费**，其价值取决于您希望交易完成的速度。


在现有各类兼容 EVM 的网络中，Gas 或类似功能的替代品基本上已经成为计算交易成本的标准方法。费用以相关网络的原生代币支付：例如，以太坊的交易需要以太币；币安智能链需要币安币；Polygon 需要 MATIC。一些网络已经全盘采用了以太坊的 EIP-1559 模式，如 Polygon，而其他网络（包括 Avalanche）则对其 C 链做出调整（这会同时[销毁基本费和优先费](https://docs.avax.network/learn/platform-overview/transaction-fees/#c-chain-fees)，而非仅仅是前者）。


如果您想更深入了解以太坊上 gas 运作方式，请参阅[此处](https://ethereum.org/en/developers/docs/gas/)。 


 


以下是**在 MetaMask 中处理 Gas****的一些基本详情**：


#### **gas 限额（所用 gas 单位）**


*Gas 限额*是指**为了执行交易或 EVM 操作，您愿意支付的**最大 Gas 单位数。不同的操作需要不同单位数量的 gas。 发送 ETH 或代币的普通交易一般耗费 **21,000** gas，而 ERC-20 代币批准则需要 45,000 gas。 许多网络，比如兼容 EVM 的区块链 Harmony，都在使用相同的模式，标准交易也需要花费 21,000 Gas。



#### 是否需要编辑 gas 限额？


否！MetaMask 会根据您尝试执行的交易，自动设置您的 gas 限额。在绝大多数情况下，这足以完成您的交易。如果您想检查或编辑 gas 限额，请确保您已开启[高级 gas 控制](https://metamask.zendesk.com/hc/en-us/articles/360022895972)（或者正在使用实验性增强型 Gas UI）)，然后在交易确认屏幕上点击“编辑”。



#### **基本费**


以太坊网络上的每个区块都有一个由网络需求决定的基本费：基本费取决于与目标区块大小相比，前一个区块的大小（其中大小是指区块包含的所有交易所使用的 gas 总额）。 如果前一个区块的大小超过目标，下一个区块的基本费将增加 12.5%，让您、用户（或您的钱包）对下一个区块的基本费心中有数。 您的总 gas 费必须至少达到此价格，才会考虑包含在区块中。


#### **优先费**


*优先费*，也称为“矿工小费”，用于激励矿工优先处理您的交易。


一般而言，此费用实际是否归于矿工取决于他们所用的[共识机制](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-)：以太坊主网在 2022 年 9 月合并后成为权益证明网络，因此优先费用将支付给验证者而非矿工。 


#### **最高费用**


最高费用是为您的交易支付的全局总金额。计算公式：**（****基本费+优先费）x 所用 Gas 单位。**MetaMask 最初根据前一个区块的历史记录来设置此金额。然而，用户可以在自定义设置中编辑此金额（见下文）。每笔 gas 的最大费用与（基本费 + 每笔 gas 的最大优先费）之间的差额“退还”给用户。


 


### **附加概念**


#### **Gwei**


Gwei 是以太币的单位，即最小面额，代表 [gigawei](https://ethgasstation.info/blog/gwei/)（或 10 亿）。[Gwei](https://www.investopedia.com/terms/g/gwei-ethereum.asp) 用于支付 Gas 费，或者更确切地说是用户支付的费用，以补偿在以太坊区块链上处理和验证交易所需的算力。


其他网络也倾向于使用 gwei 来计算成本，例如，Fantom、Harmony 和 Avalanche。


#### **滑点**


滑点是指报价和执行价格之间的预期百分比差异。


#### **Gas 费**


Gas *费*是指以太坊区块链上的交易费。这是用户为验证或完成交易而支付的费用。


#### **基本费**


由协议生成。代表将交易纳入一个区块（即要完成的交易）所需的最小“所用 gas”乘数。这是交易费中销毁的那部分。


 


### **高级 Gas 控制**


如果您想深入了解 Gas 控制的本质（例如，如果您正在测试 dapp，这可能会很有帮助），MetaMask 可以做到这一点！在[此处](https://metamask.zendesk.com/hc/en-us/articles/360022895972)查看全文。


 


### **常见问题解答**


[为何交易失败也要支付 Gas 费?](https://metamask.zendesk.com/hc/en-us/articles/360045439051)


[能否退还 Gas 费？](https://metamask.zendesk.com/hc/en-us/articles/360058370012)


[如何加快或取消待处理的交易？](https://metamask.zendesk.com/hc/en-us/articles/360015489251)


[如何估算 Gas 费](https://metamask.zendesk.com/hc/en-us/articles/360059562111)


[为什么 Gas 费如此之高？](https://metamask.zendesk.com/hc/en-us/articles/360058751211-Why-my-gas-fees-are-so-high-)


[错误：[ethjs-query]格式化 RPC 输出时（交易定价过低错误）](https://metamask.zendesk.com/hc/en-us/articles/4402538041869)


[如何修复“资金不足”错误或确认按钮灰化](https://metamask.zendesk.com/hc/en-us/articles/360044703372)


 


 

