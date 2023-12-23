
#### Ainda descobrindo criptos e a web3?


Acesse a [MetaMask Learn](https://learn.metamask.io/) para uma experiência de aprendizado simples criada especificamente para novatos na web3. É totalmente gratuito, está disponível em vários idiomas e inclui ferramentas úteis, como simulações para ajudar você a entender a MetaMask.



#### *Este artigo traz uma explicação e links para recursos que abordam transações e o porque elas falham. Mais adiante, incluímos links para cenários comuns de transações com falha e como resolvê-los:*


* [Anatomia de uma transação em blockchain](#h_01G79J04D0EN1VD8VS7C7J7KD1)
* [Problemas comuns](#h_01G79J09NWA8CGR4VYC2PT5B6Y)
* [Principais correções](#h_01G79J0J8JTRPM9MRB76EN1GPP)
* [Recursos adicionais e próximas etapas](#h_01G79J0RP8ZMZ1V1SKQY70TXCT)
* [Perguntas frequentes](#h_01G79J18RBK27GZCF10CGN9GKP)


 


**Anatomia de uma transação em blockchain**
-------------------------------------------


Quando falamos de “transações” em uma rede pública de blockchain, normalmente estamos falando de interações entre dois endereços; em outras palavras, tokens, sejam fungíveis ou não, ou outros criptoativos sendo “enviados” de um endereço para outro. Também existem transações chamadas de “transações internas”, que são interações que ocorrem entre contratos inteligentes e, na maioria dos casos, não se enquadram no escopo deste artigo.



#### Deseja mais informações?


Para saber mais sobre redes de blockchain e como elas funcionam, em geral, confira nosso [artigo de introdução aqui](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-). Caso não conheça algum termo, nosso [glossário está sempre disponível](https://consensys.net/knowledge-base/a-blockchain-glossary-for-beginners/).



A título de esclarecimento, na verdade, nada está sendo *enviado* para lugar algum. Uma rede blockchain que usa contratos inteligentes como a Ethereum tem componentes diferentes ou funções. Uma delas é o que chamamos de "computador": Ethereum Virtual Machine, ou EVM, que é capaz de executar programas ("contratos inteligentes"). No entanto, o suporte principal (backbone) do sistema é um *livro razão distribuído*: **imagine uma planilha que contém, de um lado, cada endereço de carteira na Ethereum e cada endereço tem uma coluna para cada tipo de criptoativo que possui.** 


Vamos usar um exemplo para ilustração. Digamos que Guillaume queira enviar uma transação para Dolores. Guillaume tem 1,36 ETH em sua conta e planeja enviar a Dolores 0,5 ETH. Parece ser um bom dia para a Dolores, mesmo em um mercado de ursos.


Guillaume abre sua carteira da MetaMask, digita o endereço de Dolores, configura os parâmetros da tarifa de gás — cujo valor fica tranquilo em pagar — e clica em “enviar”.


Nesse momento, a transação entra em um status de retenção temporária local, conhecido como *pool de memória local,*ou *mempool local*. A transação será então “coletada” pelo nó mais próximo na rede; dependendo das [configurações da tarifa de gás](https://metamask.zendesk.com/hc/en-us/articles/360022895972-Using-advanced-gas-controls) de Guillaume, sua transação será priorizada (**quanto mais Guillaume estiver disposto a pagar por [unidade de gás](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas), mais rápido sua transação será processada**) e propagada para outros nós na rede. Os nós vão confirmar se Guillaume tem o valor em ETH para gastar e, em seguida, realizarão a “transação”: **o razão será modificado; 0,5 será debitado do saldo de Guillaume e 0,5 será creditado ao de Dolores.**


*“Qualquer que seja sua decisão, a responsabilidade será sua e não poderá ser desfeita”:* o ETH não é propriamente movido através de uma rede; não houve um e-mail enviado do computador do Guillaume para a caixa de entrada da MetaMask da Dolores, nem nado do tipo. Guillaume enviou uma solicitação, **autenticada por suas [chaves privadas por meio da MetaMask](https://metamask.zendesk.com/hc/en-us/articles/4404722782107-User-guide-Secret-Recovery-Phrase-password-and-private-keys)** à rede para debitar sua conta e creditar a de Dolores. Depois do processo de confirmação programado nos protocolos da rede, a solicitação foi realizada. 


#### *Isso é tudo em que consiste uma transação: uma solicitação para o razão realocar algo (um valor) de um endereço para outro.*


 


**Quando algo dá errado**
-------------------------


Algo pode dar errado por vários motivos. Muitas vezes, são “software por natureza”: a MetaMask tem um bug, ou algo foi configurado incorretamente em relação à rede que você está tentando usar; houve um erro de conectividade.


Um **problema comum é que o usuário, na tentativa de pagar menos pela transação, define um limite de gás muito baixo** e as condições da rede ficam tão congestionadas que não há espaço em nenhum bloco para uma transação tão “barata”, às vezes por muito tempo: eventualmente, essa transação se tornará “obsoleta” e terá que ser cancelada pelo usuário. 


**Se você enviou uma transação e ela não foi finalizada**, seu status será mostrado como “pendente” na MetaMask. 


**Se você enviou uma transação e ela falhou, a causa provável é a falta de gás: voc**ê “ficou sem gás”, ou seja, a transação teve um custo em gás que, multiplicado pelo preço do gás, resultou em um valor total — na moeda nativa da rede — que era maior que o que tinha em sua carteira. 



#### Informações


Para obter mais informações sobre como calcular a taxa de gás, consulte nosso [guia de gás aqui](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas).



Isso pode acontecer por vários motivos. Algo a se considerar, porém, é o tipo de transação que você está tentando realizar. A criação de um token não fungível (NFT) nos horários de pico de tráfego de rede pode implicar em intensa incidência da tarifa de “gas”; se você estiver testando uma transação nova ou experimental, pode valer a pena tentar em uma rede de teste antes de pagar as taxas efetivas da rede em tempo real.


 


**Correção do problema**
------------------------


### **Fator-chave n.º 1: local ou transmissão para rede**


Conforme identifica o problema de sua transação, especialmente quando se trata de uma transação pendente, você precisa verificar se ela ainda está em seu mempool local ou se chegou à rede e está parada ali por algum motivo. Se estiver apenas em seu mempool local, a solução pode ser tão simples quanto bloquear e desbloquear sua carteira MetaMask (**certifique-se de ter a senha e o back-up de sua Frase de recuperação secreta, antes de fazer isso**). Se chegou à rede, a solução pode ser mais complicada.


Para obter mais informações sobre como corrigir esses problemas, consulte os links abaixo.  
  



### **Fator-chave n.º 2: nonce**


Essa palavra pode significar algumas coisas diferentes. É uma contração de "número apenas usado uma vez" (em inglês), e nesse contexto, significa "número de transação", começando pela primeira transação feita pelo endereço. Você pode ter problemas de verdade se, por exemplo, estiver disparando duas transações diferentes de instâncias diferentes da MetaMask com a mesma carteira ao mesmo tempo. **As transações do seu endereço precisam estar em ordem crescente, de acordo com seu nonce.** No entanto, assim como os nonces são capazes de travar uma transação, eles podem ser a chave para destravar uma transação.


[Confira aqui](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction) mais informações sobre essa técnica.


 


**Próximos passos**
-------------------


### *Se você tiver uma transação com falha ou pendente, consulte os seguintes recursos para obter ajuda.*


#### [Como enviar tokens da sua carteira da MetaMask](https://metamask.zendesk.com/hc/en-us/articles/360015488931)


#### [Como acelerar ou cancelar uma transação pendente](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction)


#### [Por que minha transação falhou com um erro “Out of Gas (Sem gas)”?](https://metamask.zendesk.com/hc/en-us/articles/360038849792-Why-did-my-transaction-fail-with-an-Out-of-Gas-error-How-can-I-fix-it-)


#### [Solução de problemas da Uniswap](https://metamask.zendesk.com/hc/en-us/articles/360053394291-Uniswap-support-and-troubleshooting-tips)


#### [Guia do usuário: gas](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas)


#### [Posso reverter uma transação já confirmada?](https://metamask.zendesk.com/hc/en-us/articles/360059957352-Can-I-reverse-an-already-confirmed-transaction-)


 


**Perguntas frequentes**
------------------------


#### 
*P: Uma conta na minha carteira tem uma transação pendente ou na fila. Posso iniciar outra transação de uma conta diferente na mesma carteira?* A: sim, pode. O nonce é contado por conta, não por carteira.

