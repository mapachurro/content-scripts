### Obtendo o preço de Gas


Se você estiver na mainnet Ethereum, você pode conferir [a ferramenta da taxa de Gas da Etherscan](https://etherscan.io/gastracker) para estimar o preço de Gas do dia.  Note que o preço da taxa de Gas é flutuante. Consulte sempre a estação de Gas para ver os preços atuais.


A rede Ethereum exige o pagamento da taxa de Gas para executar transações. Quando você envia tokens, interage com um contrato, envia ETH, ou faz qualquer outra coisa na blockchain, deve pagar por essa computação. Esse pagamento é calculado em Gas, o qual sempre é pago em ETH.


Você estará pagando pela computação, seja a transação bem-sucedida ou não. Mesmo que ela falhe, os mineradores ou validadores devem finalizar e executar a transação, o que utiliza recursos de computação. Você deve pagar por essa computação, assim como pagaria por uma transação bem-sucedida.


 


### Obtendo o limite de Gas


Então, você sabe quanto custa cada unidade de Gas, mas quantas unidades de Gas precisará gastar? Bem, se for uma transação simples — digamos, enviar ETH ou um token ERC-721 para outro endereço, deve gastar 21.000 unidades de Gas. Se estiver fazendo algo mais complexo, uma boa ferramenta é um explorador de blocos, como o [etherscan.io](https://etherscan.io/). Navegue até o contrato com o qual deseja interagir e comece a examinar as transações que foram feitas com ele. Isso lhe dará uma ideia melhor de quanto Gas outros usuários efetivamente usaram.



#### Calculadora de gas


Existem algumas ferramentas disponíveis para você estimar o custo de gas em moeda fiduciária antes de enviar uma transação. Um exemplo é a [calculadora da taxa de Gas da Cryptoneur](https://www.cryptoneur.xyz/gas-fees-calculator), que permite inserir os detalhes da transação para refletir o custo de gas em moeda local específico para a demanda atual na rede (você pode escolher entre as principais redes compatíveis com EVMs).



### 
Estrutura da taxa de Gas


A partir da [EIP-1559](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1559.md), a taxa global que um criador de transação paga é calculada como: **((taxa base + taxa de prioridade) x unidades de Gas usadas).** 


Para obter mais informações, consulte [aqui](https://support.metamask.io/hc/en-us/articles/4404600179227).


 


**Observe que não se trata de uma taxa recebida pela MetaMask e, por isso, não é possível reembolsá-la.** Essa taxa é paga aos mineradores ou validadores para finalizar a transação, validá-la em um bloco, e proteger a blockchain.

