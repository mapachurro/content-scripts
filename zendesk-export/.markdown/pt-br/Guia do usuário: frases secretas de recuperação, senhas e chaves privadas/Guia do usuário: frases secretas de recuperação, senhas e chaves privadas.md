
#### Ainda descobrindo criptos e a web3?


Acesse a [MetaMask Learn](https://learn.metamask.io/) para uma experiência de aprendizado simples criada especificamente para novatos na web3. É totalmente gratuito, está disponível em vários idiomas e inclui ferramentas úteis, como simulações para ajudar você a entender a MetaMask.



### Neste artigo:


* [Como a segurança da MetaMask é diferente das contas da web tradicional](#h_01FYVAXCSH95CQ08Q0P2VJA5HV)
* [O que é uma frase de recuperação secreta?](#h_01FYVAXJQT914HCHEYFPNMEJEA)
* [O que fazer ou não a respeito da frase de recuperação secreta](#h_01FYVAXSE5C9E4YBCSWT2F2RBQ)
* [Perguntas frequentes sobre a frase de recuperação secreta](#h_01FYVAXZYWJENFWG9K9CJTQFK7)
* [Senhas e a MetaMask](#h_01FYVAY5K22PX6926537V8B4SX)
* [Perguntas frequentes sobre chaves privadas](#h_01FYVAYH3ZZ8VW8BPDDADWRC8E)




**MetaMask: um modelo diferente de** **segurança** de contas
-------------------------------------------------------------


[A tecnologia do blockchain público](https://metamask.zendesk.com/hc/en-us/articles/360015489611) usa um conjunto muito diferente de ferramentas para proteger os dados dos usuários, quando comparada às tecnologias online tradicionais. Estamos acostumados a criar uma conta com um aplicativo ou serviço e, quando precisamos, podemos pedir ajuda para redefinir nossa senha ou nome de usuário a uma equipe de suporte. Estamos acostumados com um aplicativo que mantém nossos dados, presumivelmente em algum tipo de computador que pertence à empresa.


Bem... A MetaMask não funciona assim. A MetaMask tem três tipos diferentes de **segredo** que são usados de maneiras diferentes para manter sua carteira e suas contas privadas e seguras: a frase de recuperação secreta, a senha e as chaves privadas. Vamos falar sobre cada um desses segredos.


 


**Introdução às frases de recuperação secretas**
------------------------------------------------


Uma das tecnologias essenciais da MetaMask e da maioria das ferramentas de conta de usuário no espaço cripto é a *frase semente,*chamada também de *frase de recuperação secreta* na MetaMask.


#### **Todas as suas contas são matematicamente derivadas da sua frase de recuperação secreta. Imagine como se a FRS fosse um chaveiro que tem quantas chaves privadas quiser: cada uma dessas chaves controla uma conta.**


Agora, se quiser uma explicação técnica, as frases sementes como as conhecemos hoje foram codificadas para o uso no Bitcoin, conforme um padrão chamado Proposta de Melhoria do Bitcoin 39 ou [BIP-39](https://en.bitcoin.it/wiki/BIP_0039). Em termos simples, são uma série de palavras selecionadas com um alto nível de aleatoriedade de uma [lista específica de palavras](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt). Na MetaMask e muitas outras tecnologias compatíveis com o Ethereum, há 12 palavras em uma frase semente. Algumas frases mais antigas geradas pelo navegador Brave e algumas carteiras de hardware usam frases de 24 palavras.


Cada uma dessas palavras corresponde a uma série de números e, quando colocadas em **uma ordem específica**, representam uma maneira muito mais fácil de se lembrar de um número muito, muito longo. Esse número é então usado para gerar *deterministicamente* suas contas. Talvez você ouça falar sobre carteiras determinísticas. Na ciência da computação, determinístico é usado para descrever um *processo* (geralmente um algoritmo de algum tipo) que sempre gerará o mesmo resultado. Em outras palavras, **sua frase de recuperação secreta sempre gerará o mesmo conjunto de contas derivadas dela** 


 


### Há uma série de recursos importantes a se observar aqui:


* A **frase de recuperação secreta é o segredo que controla a carteira**. Se alguém tiver esse segredo, essa pessoa terá acesso total à sua carteira. **A MetaMask não mantém sua FRS:** **[você é quem faz a custódia da sua carteira.](https://metamask.zendesk.com/hc/en-us/articles/360059952212)** Os representantes da MetaMask **nunca** pedirão sua frase de recuperação secreta, mesmo em um cenário de suporte ao cliente. Se alguém a pedir, provavelmente está tentando enganar você ou roubar seus fundos.
* Sua FRS é **usada localmente para derivar as chaves privadas**, uma por conta/endereço. As contas são armazenadas na blockchain, e essas chaves privadas desbloqueiam essas contas.
* **Se você desinstalar o aplicativo** ou a extensão, a versão local dos dados sumirá (com exceção do [cofre](https://metamask.zendesk.com/hc/en-us/articles/360018766351)), mas todas as transações realizadas com a versão local da MetaMask terão sido gravadas na blockchain. Portanto, as transações devem se refletir tanto no [explorador de blocos](https://metamask.zendesk.com/hc/en-us/articles/360057536611) quanto em outra instância da MetaMask, desde que você [a restaurar usando a mesma frase de recuperação secreta](https://metamask.zendesk.com/hc/en-us/articles/360015289612) (**com as palavras na mesma ordem**). Isso significa que, enquanto você tiver sua frase de recuperação secreta, sempre conseguirá desinstalar a MetaMask e restaurar sua carteira.
* **Dentro da carteira, é possível ter um número muito grande de contas separadas.** Quando a MetaMask cria ou restaura a carteira da frase de recuperação secreta, ela inicialmente produz apenas a primeira conta. No entanto, todas [as contas adicionais que você criar podem ser recriadas](https://metamask.zendesk.com/hc/en-us/articles/360015489271) em uma instância futura da MetaMask. **Como a carteira é *determinística*, ela sempre recria as mesmas contas, na mesma ordem. Para mais sobre essa questão, consulte as perguntas frequentes abaixo.** No entanto, note que as contas adicionais (além da primeira, automaticamente chamada "Conta 1") ***não*** serão automaticamente adicionadas à sua conta em todas as circunstâncias. Veja nossa explicação [aqui](https://metamask.zendesk.com/hc/en-us/articles/360015489271-How-to-add-missing-accounts-after-restoring-with-Secret-Recovery-Phrase#:~:text=If%20you%20have,automatically%20re%2Dadded.) para mais informações.
* **É possível [importar contas](https://metamask.zendesk.com/hc/en-us/articles/360015489331) de outras tecnologias compatíveis com o Ethereum para uma carteira da MetaMask.** Para isso, a *chave privada* dessa conta específica é usada. No entanto, **essa conta não será restaurada automaticamente pela MetaMask em outra instância; você terá que readicioná-la manualmente**. Portanto, se tiver importado as contas, **anote suas chaves privadas da mesma maneira que fez com a frase semente** para poder reimportá-la no futuro.


 


**Frase de recuperação secreta da MetaMask: recomendações**
-----------------------------------------------------------




**O que fazer:**

* **Anote sua frase de recuperação secreta em algum lugar seguro**. Não podemos dizer exatamente onde, pois isso depende das suas circunstâncias.
	+ A importância de escrever sua frase de recuperação secreta é o fato de ela não poder ser roubada online. Se armazená-la em um arquivo em uma pasta de armazenamento na nuvem conectada à internet, por exemplo, ela poderia teoricamente ser roubada.
* Verifique a ortografia e se você escreveu todas as palavras na mesma ordem que elas foram mostradas.
* Entre em contato com [os canais oficiais](https://metamask.zendesk.com/hc/en-us/articles/360058230211) de suporte da MetaMask se precisar de ajuda.





**O que não fazer:**

* Manter a frase em um local facilmente encontrável ou fácil de hackear; por exemplo, em um documento ou e-mail salvo na nuvem intitulado "Frase semente"; em um post-it no seu computador.
* Fornecer sua frase semente a qualquer pessoa, mesmo que ela diga ser do suporte da MetaMask.
* Mudar a ordem das palavras.





 


**Perguntas frequentes sobre a frase de recuperação secreta**
-------------------------------------------------------------


### Minha frase semente restaurou uma conta diferente!


Consulte o artigo da base de conhecimento sobre esse assunto [aqui](https://metamask.zendesk.com/hc/en-us/articles/360058120992). Além disso, consulte o tópico da comunidade [aqui](https://community.metamask.io/t/restored-metamask-no-coins-are-showing/878/107?u=jacob.cantele) para mais informações de contexto.


### Outras perguntas frequentes sobre a frase de recuperação secreta:


[Como revelar sua frase de recuperação secreta](https://metamask.zendesk.com/hc/en-us/articles/360015290032)


[Como recuperar sua frase de recuperação secreta](https://metamask.zendesk.com/hc/en-us/articles/360018766351)


[Importando uma frase semente de outro software de carteira: caminho de derivação](https://metamask.zendesk.com/hc/en-us/articles/360060331752)


[Guia de migração de carteira](https://metamask.zendesk.com/hc/en-us/articles/4867408571803)


[Como importar uma conta](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[Como verificar a atividade da minha carteira no explorador da blockchain](https://metamask.zendesk.com/hc/en-us/articles/360057536611)


[O que é uma frase de recuperação secreta e como manter minha carteira segura?](https://metamask.zendesk.com/hc/en-us/articles/360060826432)


 


**Senhas e a MetaMask**
-----------------------


A MetaMask usa senhas para um único propósito: proteger o próprio aplicativo; em outras palavras, abrir o aplicativo, seja o aplicativo móvel ou a extensão do navegador. Depois de restaurar ou criar sua carteira a partir da sua frase de recuperação secreta, não será necessário usá-la regularmente (**embora deva mantê-la em backup e segura**). Você usará sua senha (ou mais comumente a autenticação biométrica do dispositivo móvel, como o reconhecimento facial ou a impressão digital) para desbloquear o aplicativo. Para mais detalhes, consulte nosso artigo [aqui](https://metamask.zendesk.com/hc/en-us/articles/4405451730331).


 


**Chaves privadas**
-------------------


Embora uma frase de recuperação secreta seja usada para criar e restaurar a carteira da MetaMask, incluindo todas as contas criadas nessa carteira, cada conta tem sua *chave privada*. Essa chave pode ser usada para importar essa conta (e apenas ela) em uma carteira diferente. Da mesma forma, contas individuais de outras tecnologias cripto podem ser importadas para a carteira da MetaMask.


### Perguntas frequentes sobre chaves privadas:


[O que são contas importadas?](https://metamask.zendesk.com/hc/en-us/articles/360015289932)


[Como importar uma conta](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[Como exportar a chave privada de uma conta](https://metamask.zendesk.com/hc/en-us/articles/360015289632)


[Posso importar a conta da carteira da Coinbase para a MetaMask?](https://metamask.zendesk.com/hc/en-us/articles/360058485292)

