
#### Os tokens sequer estão aparecendo?


Veja nosso guia para solucionar esse problema [aqui](https://support.metamask.io/hc/en-us/articles/360059232852).



Primeiramente, verifique os saldos de token exibidos no explorador de blocos e compare com a MetaMask. Faça isso copiando o endereço da sua carteira e colando-a no explorador de blocos corresponde à rede que está usando: Etherscan para mainnet do Ethereum, Arbiscan para Arbitrum etc. Para instruções detalhadas, clique [aqui](https://support.metamask.io/hc/en-us/articles/360057536611).




Extensão Aplicativo para dispositivos móveis


Se a extensão da MetaMask estiver exibindo o saldo incorreto ou impreciso para ETH ou outros tokens, tente os procedimentos abaixo até vir o saldo corretamente.


**Antes de continuar, verifique se fez backup da sua [frase de recuperação secreta](https://support.metamask.io/hc/en-us/articles/4404722782107-User-Guide-Secret-Recovery-Phrase-password-and-private-keys) em um local seguro.**


1. Verifique se sua conexão com a internet é forte e estável. Caso contrário, a MetaMask pode não conseguir carregar os saldos corretos.
2. Feche o navegador que tem a extensão da MetaMask instalada e abra-o novamente.
3. Tente desativar quaisquer bloqueadores de anúncios instalados ou, se estiver usando uma VPN, tente usar a MetaMask com ela desativada.
4. Troque para uma rede diferente e volte novamente. Para fazer isso, clique na rede atual na parte superior do aplicativo. Escolha uma rede diferente e depois volte para sua rede original.
5. Verifique se não há nenhum [problema de permissões no navegador](https://support.metamask.io/hc/en-us/articles/360038139452-MetaMask-states-Balance-may-be-outdated-displays-in-orange-or-ETH-not-added-to-balance).
6. Tente usar um URL de RPC diferente, se houver mais de um disponível para a rede em uso. É possível editar o URL do RPC acessando Configurações > Rede e então clicando na rede em questão. Para mais informações, veja nosso [artigo sobre como adicionar redes](https://support.metamask.io/hc/en-us/articles/360043227612).
7. Instale a MetaMask usando outro navegador suportado (Firefox, Chrome, Brave, Edge) em nosso site oficial [https://metamask.io](https://metamask.io/) e tente restaurar a carteira usando a frase de recuperação secreta de 12 palavras, caso o problema persista apenas no navegador que está usando.




Após verificar no Etherscan que a quantidade de tokens exibidos na MetaMask Mobile está incorreta, siga estas etapas:


1. Verifique se sua conexão com a internet está forte e estável. Caso contrário, os valores de tokens podem não estar atualizados.
2. Mude para uma rede diferente e troque de volta novamente.
3. Mude o URL do RPC da rede para um endereço alternativo, sempre que possível.  Para mais informações, veja nosso [artigo sobre como adicionar redes](https://support.metamask.io/hc/en-us/articles/360043227612).
4. Oculte o token, seguindo as instruções [aqui](https://support.metamask.io/hc/en-us/articles/360015489031-How-to-add-unlisted-tokens-custom-tokens-in-MetaMask#h_01FWH499MRDT5QC4R3KNPQNRWB), e adicione novamente o token seguindo [estas instruções](https://support.metamask.io/hc/en-us/articles/360015489031-How-to-add-unlisted-tokens-custom-tokens-in-MetaMask).


**Se o token em questão for um token nativo da rede que não seja o da rede Ethereum** (BNB, AVAX, MATIC, etc), tente [excluir a rede](https://support.metamask.io/hc/en-us/articles/4502810252059-How-to-remove-networks) e depois [readicioná-la](https://support.metamask.io/hc/en-us/articles/360043227612-How-to-add-a-custom-network-RPC).   
  
**Se o token em questão for o ETH, verifique se fez o backup da sua [frase de recuperação secreta](https://support.metamask.io/hc/en-us/articles/4404722782107-User-Guide-Secret-Recovery-Phrase-password-and-private-keys) em um local seguro**, então reinstale o aplicativo.

Se ainda estiver tendo problemas após seguir tais passos, entre em contato conosco por meio do botão "Iniciar uma conversa" na nossa [página de suporte](https://support.metamask.io/hc/en-us).



#### O token possui mecanismos internos que afetam seu fornecimento ou valor?


As redes Ethereum e compatíveis com EVMs abrigam uma grande variedade de tokens com diferentes utilidades. Alguns tokens são projetados para alterar dinamicamente o fornecimento ou o valor de acordo com várias condições:


* [Tokens de rebase](https://support.metamask.io/hc/en-us/articles/4405497827355-User-Guide-Tokens#:~:text=Elastic%20supply%20/%20Rebase%20/%20Algorithmic%20tokens) ajustam o fornecimento de tokens
* Tokens com "taxas" aplicadas a diferentes tipos de transação (por exemplo, transferência simples, swap, venda, etc). Tais tokens são por vezes chamados de tokens com "taxa de transferência".


Antes de concluir que seu saldo está incorreto, verifique se quaisquer condições semelhantes se aplicam ao token. Normalmente, você pode encontrar essas informações verificando o white paper ou a documentação do projeto.


