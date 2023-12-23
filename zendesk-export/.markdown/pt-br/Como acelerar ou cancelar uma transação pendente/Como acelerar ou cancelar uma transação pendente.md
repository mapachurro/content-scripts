Ao enviar uma transação em Ethereum ou em uma rede compatível, parte do gas pago é como uma oferta para a rede processar sua transação mais cedo. Esse elemento é conhecido como a taxa de prioridade. Embora a MetaMask ajude você a calcular uma taxa de gas total que fará sua transação ser coletada, você pode acabar esperando muito tempo se enviar um preço de gas baixo. Para obter orientações sobre quais preços de “gas” resultarão na finalização de uma transação em um período razoável, consulte fontes como o rastreado[r de “gas” da Etherscan ou um ra](https://etherscan.io/gastracker)streador semelhante para qualquer rede que você esteja usando.


Além disso, às vezes há circunstâncias em que algo dá errado e uma transação fica travada ou pendente por muito tempo.


Independentemente de como chegou a essa situação, há diferentes maneiras de se lidar com isso.


 


### Antes de qualquer ação adicional, o primeiro passo deve ser sair e fechar seu navegador, reabri-lo e então desbloquear a MetaMask (no celular, basta fechar e reabrir o aplicativo). Se isso não resolver o problema, continue com o seguinte:


 


**Aceleração de uma transação**
-------------------------------


![A MetaMask acelera a transação](https://support.metamask.io/hc/article_attachments/12927043481371)


Tente uma das opções abaixo:


* Aguarde até que a rede esteja disponível para processar transações a esse preço
* Se não tiver feito isso ainda, clique no botão **Speed Up** (Acelerar). Isso permitirá que você reenvie a mesma transação, mas com uma taxa de gas mais alta que deve permitir que a transação seja processada mais rapidamente. Como esse processo reutiliza o mesmo nonce da transação original, você não precisará pelo gas duas vezes.


Tenha em mente que **acelerar a transação aumentará o valor gasto na transação**.


 


**Cancelamento de uma transação — Método 1: cancelamento no aplicativo**
------------------------------------------------------------------------


Se você ainda não tiver feito isso, para cancelar a transação, basta selecionar **Cancel** (Cancelar), como se vê na captura de tela acima. Atenção: **só é possível *tentar* o cancelamento se a transação ainda estiver pendente na rede.** As transações que já tiverem sido confirmadas não poderão ser revertidas.


 


**Cancelamento de uma transação — Método 2: nonce personalizado**
-----------------------------------------------------------------


Esse processo envolve o envio de uma nova transação com o mesmo nonce, um número de identificação para cada transação, derivado da frase "number only used one" (número usado apenas uma vez). Na verdade, a transação não precisa ter valor; por exemplo, você pode enviar 0 ETH. O que importa é pagar por “gas” suficiente para que a rede priorize a transação. 


Ao usar este método, **será preciso conferir a transação pendente que deseja cancelar entre as mais antigas na fila**. Por exemplo, você não pode tentar cancelar uma transação com um nonce de 10, antes de cancelar o nonce de 9. 


*As capturas de tela abaixo mostram diferentes momentos, então as taxas de gas mostradas podem variar, mesmo em pequenas variações. Não deixe isso desanimar você. Quando fizer isso sozinho, a MetaMask atualizará as taxas de mercado em tempo real automaticamente.*




Extensão Aplicativo para dispositivos móveis


1. Em “Advanced settings” (Configurações avançadas), ative a opção **Customize transaction nonce** (Personalizar nonce da transação) e **Advanced gas controls (Controles de gas avançados)** (Controles de “gas” avançados). Este último permitirá que você manipule a taxa de “gas” que paga e garantirá que sua transação de cancelamento seja processada, antes da transação original que deseja cancelar.



#### Observação:


Atualmente, a extensão da MetaMask tem um recurso experimental chamado [IU de taxa gas aprimorada](https://metamask.io/1559/) (não confundir com [controles de gas avançados](https://support.metamask.io/hc/en-us/articles/360022895972)). Essas etapas podem ser realizadas independentemente, tenha você ativado ou não essa funcionalidade. No entanto, elas terão uma aparência diferente. As etapas abaixo não usam IU de gas aprimorada. Lembre-se:



	* Se tiver a IU de gas aprimorada ativa, também precisará da opção "Personalizar nonce da transação".
	* Se não tiver habilitado a IU de gas aprimorada, será necessário ativar "Controles de gas avançados" e "Personalizar nonce da transação".

![Configurações avançadas da MetaMask](https://support.metamask.io/hc/article_attachments/12927064113947)
2. **Envie uma nova transação**. Na nova transação, envie **PARA** si mesmo, ou seja, seu endereço público da MetaMask. **Preencha o “Custom Nonce” (Nonce personalizado) com o mesmo nonce da transação que ainda está pendente**:


![Metamask_custom_transaction_nonce_Extension.png](https://support.metamask.io/hc/article_attachments/12927064259483)
3. Agora, clique em “Editar” ao lado de “Taxa de gas” (se a [IU de gas aprimorada](https://support.metamask.io/hc/en-us/articles/360022895972-Using-advanced-gas-controls#:~:text=%C2%A0-,Enhanced%20Gas%20UI,-Since%20the%20introduction) experimental estiver ativa, isso aparecerá como "Mercado"). Agora, as opções abaixo serão exibidas:


![Controles de gas avançados na extensão da MetaMask](https://support.metamask.io/hc/article_attachments/12927065407515)


Para garantir que seu pedido de cancelamento seja atendido com prioridade e antes da original, **você precisará pagar mais pela taxa de “gas”**. Siga estas instruções:


	* Defina o seu **gas limit** (limite de cobrança da taxa de “gas”), que seja *comparável ou ligeiramente superior* ao da transação original.
	* Defina sua **max priority fee** (taxa de prioridade máxima) *pelo menos 10% mais alta* (em Gwei) do que a taxa de “gas” da transação original (pendente). Por exemplo, se essa transação tinha uma taxa de “gas” de 30 Gwei, defina a taxa de prioridade máxima na transação de substituição/cancelamento em 33 a 35 Gwei.
	* Certifique-se de que sua taxa máxima seja pelo menos 30% maior do que a taxa máxima da transação que você está substituindo. Por exemplo, se sua taxa anterior era de 150 Gwei, escolha algo mais próximo de 200 Gwei desta vez.Confira um rastreador de taxa de “gas” como o [Etherscan](https://etherscan.io/gastracker) ou o [ETH Gas Station](https://ethgasstation.info/) para obter orientações sobre as taxas máximas recomendadas.




1. **Em Configurações > Avançado, ative "Personalizar nonce da transação".**
2. **Envie uma nova transação.** Na nova transação, envie PARA si mesmo, ou seja, seu endereço público da MetaMask. **Preencha o “(Nonce personalizado)” com o mesmo nonce da transação que ainda está pendente**:


Para encontrar a configuração de nonce personalizada no app, acesse a tela de confirmação da transação, que aparece depois de inserir a quantidade de tokens e o destinatário. Clique em "Editar" para alterar:


![Nonce de transação personalizado da MetaMask Mobile](https://support.metamask.io/hc/article_attachments/12927068442907)
3. Agora é preciso certificar-se de que as configurações de gas estão corretas para que sua transação substituta seja processada. Na tela de confirmação da transação, toque no de gas destacado:


![Controles de gas avançados na extensão da MetaMask](https://support.metamask.io/hc/article_attachments/12927041593755)


Agora acesse "Opções avançadas" no menu que aparecerá.
4. A partir daqui, será possível ajustar precisamente o gas a fim de garantir que sua transação seja coletada. Confira o que você verá na tela:


![Controles de gas avançados na extensão da MetaMask](https://support.metamask.io/hc/article_attachments/12927063201691)


A partir daqui, ajuste as configurações de gas. Siga as instruções para garantir que sua transação seja coletada:


	* Defina o seu **gas limit** (limite de cobrança da taxa de “gas”), que seja *comparável ou ligeiramente superior* ao da transação original.
	* Defina sua **max priority fee** (taxa de prioridade máxima) *pelo menos 10% mais alta* (em Gwei) do que a taxa de “gas” da transação original (pendente). Por exemplo, se essa transação tinha uma taxa de “gas” de 30 Gwei, defina a taxa de prioridade máxima na transação de substituição/cancelamento em 33 a 35 Gwei.
	* Certifique-se de que sua **taxa máxima** seja *pelo menos 30% maior* do que a taxa máxima da transação que você está substituindo. Por exemplo, se sua taxa anterior era de 150 Gwei, escolha algo próximo de 200 Gwei desta vez.Confira um rastreador de taxas de gas como [o Etherscan](https://etherscan.io/gastracker) ou o [ETH Gas Station](https://ethgasstation.info/) para obter orientações sobre as taxas máximas recomendadas.



