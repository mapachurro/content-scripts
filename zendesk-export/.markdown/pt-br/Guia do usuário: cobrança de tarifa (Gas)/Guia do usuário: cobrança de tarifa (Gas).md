
#### Ainda descobrindo criptos e a web3?


Acesse a [MetaMask Learn](https://learn.metamask.io/) para uma experiência de aprendizado simples criada especificamente para novatos na web3. É totalmente gratuito, está disponível em vários idiomas e inclui ferramentas úteis, como simulações para ajudar você a entender a MetaMask.



Gas é a unidade de medida de quanto trabalho computacional é necessário para processar transações e contratos inteligentes. Basicamente, uma taxa de transação, o termo se origina da Ethereum, em cujo contexto se refere à computação realizada na Ethereum Virtual Machine (EVM). Desde que a Ethereum foi criada, existem inúmeras redes compatíveis com EVM (e não compatíveis) que surgiram e modelos semelhantes adotados. 


O termo é análogo à gasolina que alimenta o motor dos automóveis: é o custo flutuante ocasionalmente caro de operação. Ou seja, contratos inteligentes mais complexos exigem mais energia para alimentar sua computação, assim como um carro maior e mais potente consome mais combustível para funcionar.


O método para calcular as taxas de “gas” varia de acordo com a rede. Por exemplo, calcular a taxa de gas na Ethereum costumava ser muito complicado, mas foi consideravelmente simplificado com a implementação do Ethereum Improvement Protocol **(EIP) 1559** em agosto de 2021 (também conhecido como London Upgrade). Essencialmente, você paga uma **taxa base** para cada unidade de gas ***queimada*** (leia-se: ela é consumida e desaparece) após a conclusão bem-sucedida da transação. Sobre a taxa-base, você adiciona uma **taxa de prioridade**, novamente por unidade de “gas”, cujo valor depende da rapidez com que você deseja que a transação seja concluída. 


Por toda a ampla gama de redes compatíveis com a EVM disponível, a taxa de “gas” ou alternativas que funcionam de modo parecido tornaram-se essencialmente o método padrão para calcular os custos da transação. As taxas são pagas no token nativo da rede: por exemplo, qualquer transação na Ethereum requer ETH; usar BSC requer BNB; usar Polygon requer MATIC. Algumas redes adotaram o modelo por atacado EIP-1559 da Ethereum, como a Polygon, enquanto outras fizeram ajustes, incluindo a Avalanche, para sua C-Chain (que [queima tanto a taxa-base quanto a taxa de prioridade](https://docs.avax.network/learn/platform-overview/transaction-fees/#c-chain-fees), em vez de apenas a primeira).  


Se quiser ler mais sobre como o gas funciona na rede Ethereum, confira [aqui](https://ethereum.org/en/developers/docs/gas/). 


 


Aqui estão alguns **detalhes essenciais para lidar com a cobrança da taxa de “gas”** **na MetaMask**:


#### **O limite de gas (unidades de gas usadas)**


O *limite para cobrança da taxa de “gas”* é a **quantidade máxima de unidades de “gas” que você está disposto a pagar** para realizar uma transação ou operação em EVM. Diferentes operações exigem diferentes quantidades de unidades de gas. Uma transação normal que envie ETH ou um token custa, normalmente, **21 mil** unidades de gas, enquanto uma aprovação de tokens ERC-20 requer 45 mil.  Muitas redes, como a Harmony, uma blockchain compatível com EVM, usam um modelo idêntico no qual as transações padrão também custam 21.000 unidades de “gas”.  



#### Preciso editar o limite gas?


Não! A MetaMask define o gas automaticamente de acordo com a transação que você está tentando executar. Na grande maioria dos casos, isso será adequado para completar sua transação. Se você quiser verificar ou editá-lo, confira se possui [os controles de gas avançados](https://metamask.zendesk.com/hc/en-us/articles/360022895972) ativos (ou se estiver usando a IU de gas aprimorada experimental) e clique em "Editar" na tela de confirmação da transação.



#### **A taxa base**


Cada bloco da rede Ethereum tem uma taxa base determinada pela demanda da rede: a taxa base se baseia no tamanho do bloco anterior, comparado ao tamanho do bloco alvo (onde o tamanho é a quantidade total de gas usado para todas as transações que o bloco inclui). Se o tamanho do bloco anterior exceder o tamanho do alvo, a taxa base para o seguinte aumenta em 12,5%, deixando o usuário com certeza absoluta sobre a taxa base do próximo bloco. O total da sua taxa de gas deve atender a esse preço como um valor mínimo considerado para a inclusão no bloco. 


#### **A taxa de prioridade**


A *taxa de prioridade* máxima, também referida como “gorjeta para o minerador”, incentiva o minerador a priorizar sua transação. 


Naturalmente, se a transação vai para o minerador de fato depende do [mecanismo de consenso](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) que usam: a rede principal da Ethereum usa agora a prova de participação após o The Merge em setembro de 2022, então a taxa de prioridade é para validadores e não para os mineradores. 


#### **Taxa máxima**


A taxa máxima é o valor total global pago pela sua transação. Ela é calculada como: **(****taxa-base + taxa de prioridade) x unidades de “gas” usadas.** Inicialmente, a MetaMask define esse valor com base no histórico do bloco anterior. No entanto, os usuários podem editar esse valor por meio de configurações personalizadas (confira abaixo). A diferença entre a taxa máxima de gas e a taxa base + a taxa máxima de prioridade por gas é "reembolsada" ao usuário.


 


### **Conceitos adicionais**


#### **Gwei**


O gwei é uma unidade de Ether, a menor denominação que corresponde a [gigawei](https://ethgasstation.info/blog/gwei/) (ou 1.000.000.000). [Gwei](https://www.investopedia.com/terms/g/gwei-ethereum.asp) é usado para taxas de “gas”, ou melhor, para os pagamentos feitos por usuários para compensar pela energia de computação necessária para processar e validar transações na blockchain da Ethereum. 


Outras redes também tendem a calcular os custos usando o gwei como, por exemplo, a Fantom, a Harmony e a Avalanche.


#### **Slippage**


A slippage é a diferença percentual esperada entre um preço cotado e um preço executado.


#### **Taxa de “gas”**


A *taxa de gas* se refere à taxa por transação na blockchain da Ethereum. É o que os usuários pagam para validar ou concluir uma transação. 


#### **Taxa-base**


Gerada pelo protocolo. Representa o multiplicador mínimo “gasUsed” (gasUsado), necessário para que uma transação seja incluída em um bloco (ou seja, para que uma transação seja concluída). Esta é a parte da taxa de transação que é queimada.


 


### **Controles de “gas” avançados**


Se você quiser conhecer o âmago da questão sobre seus controles da taxa de “gas” (isso pode ser útil se estiver testando um dapp, por exemplo), a MetaMask pode fazer isso! Consulte o artigo completo [aqui](https://metamask.zendesk.com/hc/en-us/articles/360022895972).


 


### **Perguntas frequentes**


[Por que paguei taxas de “gas” por uma transação com falha?](https://metamask.zendesk.com/hc/en-us/articles/360045439051)


[É possível obter reembolso das taxas de “gas” cobradas?](https://metamask.zendesk.com/hc/en-us/articles/360058370012)


[Como faço para acelerar ou cancelar uma transação pendente?](https://metamask.zendesk.com/hc/en-us/articles/360015489251)


[Como faço para estimar a taxa de “gas”?](https://metamask.zendesk.com/hc/en-us/articles/360059562111)


[Por que minhas taxas de “gas” são tão altas?](https://metamask.zendesk.com/hc/en-us/articles/360058751211-Why-my-gas-fees-are-so-high-)


[Erro: [ethjs-query] ao formatar as saídas da RPC (erro de transação subprecificada)](https://metamask.zendesk.com/hc/en-us/articles/4402538041869)


[Como faço para corrigir o erro “fundos insuficientes” ou o botão de confirmação desabilitado?](https://metamask.zendesk.com/hc/en-us/articles/360044703372)


 


 

