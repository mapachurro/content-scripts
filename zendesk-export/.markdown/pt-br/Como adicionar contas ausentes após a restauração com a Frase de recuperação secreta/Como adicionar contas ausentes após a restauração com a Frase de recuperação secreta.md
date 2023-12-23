
#### Observação:


Quaisquer contas **importadas** **não** serão readicionadas quando você restaurar a carteira usando sua frase de recuperação secreta. [É necessário readicioná-las](https://support.metamask.io/hc/en-us/articles/360015489331) da mesma forma que você as importou originalmente.



**NÃO compartilhe sua Frase de recuperação secreta com ninguém! Essas palavras podem ser usadas para roubar todas as suas contas. Não é possível editar ou alterar sua Frase de recuperação secreta.**


 


Quando você [restaura uma carteira](https://support.metamask.io/hc/en-us/articles/360015289612-How-to-restore-your-MetaMask-account-from-Seed-Phrase-Secret-Recovery-Phrase) usando sua frase de recuperação secreta, a MetaMask adicionará novamente todas as contas adicionais que você [criou](https://support.metamask.io/hc/en-us/articles/360015289452) anteriormente, mas apenas se determinadas condições forem atendidas.


A MetaMask tentará adicionar suas outras contas sempre que possível (presumindo que elas não tenham sido [importadas](https://support.metamask.io/hc/en-us/articles/360015289932)) confirmando suas contas anteriores em ordem crescente (ou seja, Conta 2, depois Conta 3 etc.). **As contas são readicionadas automaticamente se elas tiverem um saldo em ETH maior que zero**. No entanto, esse processo termina quando a MetaMask encontra uma conta com 0 ETH. Portanto, a primeira conta com 0 ETH e qualquer outra após esta *não* serão adicionadas.


Lembre-se de que **esse processo verifica apenas os saldos de ETH na rede principal da Ethereum**, portanto, outros tokens ou tokens em outras redes não resultarão na reimportação automática das suas contas.


**Para aquelas que não forem readicionadas de modo automático, será necessário adicioná-las novamente “[criando](https://support.metamask.io/hc/en-us/articles/360015289452)” as contas**. Por exemplo, se você tiver alguns tokens na Conta 4, mas ela não tiver sido adicionada automaticamente porque esses tokens não são ETH na rede principal, basta adicionar contas manualmente (usando as etapas abaixo) até chegar à Conta 4. A sua Conta 4 *antes* da restauração corresponderá à Conta 4 *após* a restauração, independentemente de qualquer nome que você tenha aplicado anteriormente.


Se precisar usar o botão "criar" para readicionar as contas, não há motivo para se preocupar para o caso dos endereços serem diferentes. Os endereços são derivados de forma criptográfica e *determinística* da chave privada, o que significa que sempre serão iguais. E como se trata de uma conta Ethereum, uma vez criada, a conta existe permanentemente, e você poderá continuar de onde parou. 


Siga as etapas abaixo sobre como restaurar suas outras contas na ordem em que foram criadas originalmente:




Extensão Aplicativo para dispositivos móveis


1. Clique no favicon, no canto superior direito do menu suspenso da MetaMask
2. Clique em “Create Account” (Criar contra) para restaurar suas contas da MetaMask na ordem em que foram criadas
3. Se as contas tiverem sido nomeadas anteriormente, você pode nomeá-las mais uma vez na etapa abaixo, antes de clicar em “**Create**” (Criar)


![How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase.gif](https://support.metamask.io/hc/article_attachments/9026739981083/How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase.gif)




1. Toque no ícone de hambúrguer, no canto superior esquerdo da tela para abrir o menu. Nele, toque na seta do menu suspenso, ao lado do nome da sua conta:
2. Toque em “Create New Account” (Criar conta):


![How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase_Mobile.gif](https://support.metamask.io/hc/article_attachments/9027058464027/How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase_Mobile.gif)




Se, ainda assim, os endereços que estava procurando não forem exibidos, eles provavelmente foram criados com uma Frase de recuperação secreta diferente ou você tinha uma conta importada que você ainda precisa reimportar usando chaves privadas ou JSON. Consulte [este artigo sobre como importar uma conta](https://support.metamask.io/hc/en-us/articles/360015489331-Importing-an-Account). 

