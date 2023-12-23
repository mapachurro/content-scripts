Quando um site solicita que adicione uma rede personalizada à MetaMask, você recebe as informações que a MetaMask usará para interagir com a rede. A MetaMask realiza validações básicas dessas informações e o avisa se algo parecer errado ou incomum. A MetaMask também impedirá que a mesma rede seja adicionada mais de uma vez. No entanto, **a MetaMask não verifica as redes personalizadas**, e mesmo que a validação da MetaMask pareça normal, a rede poderá ser maliciosa ou mal representada pelo site que faz a solicitação.


**Para mais informações e uma apresentação das redes personalizadas, consulte nosso Guia de usuários [aqui](https://support.metamask.io/hc/en-us/articles/4404424659995).**


Assim como é sua responsabilidade verificar os endereços Ethereum com os quais você faz transações, também é sua responsabilidade verificar as redes personalizadas que adicionar à MetaMask. Neste artigo, vamos compartilhar algumas orientações sobre como fazer isso.


Quando um site faz uma solicitação para adicionar uma rede personalizada, a MetaMask exibe esta confirmação:


![custom-network.png](https://support.metamask.io/hc/article_attachments/360087917091/custom-network.png)


 


Essa confirmação mostra **as informações de rede que o site forneceu**. *Não há garantia de que essas informações estejam corretas*. Portanto, você deve confiar nas informações na mesma medida em que confia no site.


Se você clicar em “View all details” (Exibir todos os detalhes) na confirmação, poderá visualizar todas as informações de rede fornecidas pelo site, que incluem:


* **Nome da rede**: o nome que a MetaMask associará à rede.
* **URL da rede:** a URL que a MetaMask usará para acessar a rede.
* **ID da cadeia:** o ID da cadeia que a MetaMask usará para assinar transações na rede.
* **Símbolo de moeda:** o símbolo de moeda que a MetaMask usará para a moeda nativa da rede.
	+ Por exemplo, para a rede principal da Ethereum, o símbolo de moeda é ETH e para a Gnosis Chain, o símbolo é xDAI (mantido após sua fusão).
* **URL do explorador de blocos (opcional):** o URL para o qual a MetaMask o direcionará para inspecionar contas, transações etc. O equivalente ao [etherscan.io](https://etherscan.io), mas para a rede em questão.


Se, por algum motivo, você não tiver certeza sobre a exatidão das informações da rede, recomendamos que execute estas etapas para verificá-las:


* Acesse [Chainlist](https://chainlist.wtf/) e procure o ID da cadeia fornecido e/ou o nome da rede. Se a MetaMask estiver dizendo que algumas informações não correspondem, você poderá identificar o problema na Chainlist. Se a rede personalizada não estiver listada na Chainlist, significa que ela é extremamente nova ou possivelmente de qualidade questionável.
* Pesquise o nome da rede no Google e tente responder às perguntas a seguir. Quanto mais perguntas você responder com “sim”, mais motivos terá para acreditar que a rede é legítima. Saiba que existem muitos golpes e canais falsos de mídia social, especialmente no Telegram.
+ A rede tem um site? Se sim, parece legítimo? Ele lista os detalhes da rede?
+ A rede tem uma conta oficial no Twitter ou outra rede social? Eles têm muitos seguidores? Eles parecem ser bem conceituados? O que as pessoas estão falando sobre a rede?
+ Você consegue identificar alguma das pessoas que mantêm a rede? Podem ser encontradas nas redes sociais? Eles têm muitos seguidores?
+ Existem notícias sobre a rede?


Para a maioria das redes, deve ficar bastante óbvio se elas são legítimas ou não e se o site está fornecendo informações precisas ou não. Se, após concluir essas etapas, ainda não tiver certeza deverá rejeitar a solicitação para adicionar a rede, pesquisar mais e talvez tentar novamente mais tarde.

