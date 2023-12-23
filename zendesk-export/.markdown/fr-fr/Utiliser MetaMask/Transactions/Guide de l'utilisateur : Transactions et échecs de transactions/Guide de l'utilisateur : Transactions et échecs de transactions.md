
#### Nouveau dans le domaine de la crypto et du web3 ?


Rendez-vous sur [MetaMask Learn](https://learn.metamask.io/) pour une expérience d'apprentissage simple conçue spécifiquement pour les nouveaux arrivants dans le domaine du web3. Entièrement gratuite, elle est disponible en plusieurs langues et comprend des outils utiles tels que des simulations pour vous aider à trouver vos marques avec MetaMask.



#### *Cet article se comporte une explication et des liens vers des ressources concernant les transactions et les raisons de leur échec, et plus loin, des liens vers des scénarios courants d'échec de transaction et la façon d'y remédier :*


* [Anatomie d'une transaction de blockchain](#h_01G79J04D0EN1VD8VS7C7J7KD1)
* [Problèmes fréquents](#h_01G79J09NWA8CGR4VYC2PT5B6Y)
* [Principales corrections](#h_01G79J0J8JTRPM9MRB76EN1GPP)
* [Ressources supplémentaires et prochaines étapes](#h_01G79J0RP8ZMZ1V1SKQY70TXCT)
* [FAQ](#h_01G79J18RBK27GZCF10CGN9GKP)


 


**Anatomie d'une transaction de blockchain**
--------------------------------------------


Lorsque nous parlons de « transactions » sur un réseau public de blockchain, nous parlons habituellement des interactions entre deux adresses ; en d'autres termes, des jetons, qu'ils soient fongibles ou non, ou d'autres crypto-actifs étant « envoyés » d'une adresse à une autre. Il existe également des transactions appelées « transactions internes », qui sont des interactions qui se produisent entre des contrats intelligents, et qui, pour la plupart, sortent du cadre de cet article.



#### Vous voulez plus d'informations ?


Pour plus d'informations sur les réseaux de blockchain et la façon dont ils fonctionnent en général, consultez notre [article d'introduction ici](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-), et si vous êtes bloqué sur des mots inconnus, notre [glossaire est toujours disponible](https://consensys.net/knowledge-base/a-blockchain-glossary-for-beginners/).



Par souci de clarté, rien n'est réellement *envoyé* où que ce soit. Un réseau blockchain basé sur des contrats intelligents, comme Ethereum, comporte un certain nombre de composants, ou fonctions, différents. L'un d'entre eux est ce que nous appellerions un « ordinateur » : la machine virtuelle Ethereum, ou EVM, qui est capable d'exécuter des programmes (« contrats intelligents »). Cependant, le squelette du système est un *grand livre distribué* : **imaginez une feuille de calcul qui contient, d'un côté, chaque adresse de portefeuille Ethereum unique, et chaque adresse a une colonne pour chaque type de crypto-actifs qu'elle détient.**


Utilisons un exemple pour l'illustration. Disons que Guillaume veut envoyer une transaction à Dolores. Guillaume a 1,36 ETH dans son compte, et il prévoit d'envoyer à Dolores 0,5 ETH. C'est une bonne journée pour Dolores, même dans un marché baissier.


Guillaume ouvre son portefeuille MetaMask, entre l'adresse de Dolores, configure les paramètres du gaz qu'il est prêt à payer et appuie sur « envoyer ».


À ce stade, la transaction entre dans un état d'attente temporaire local, connu comme *le pool de mémoire* local ou *le mempool local*. La transaction sera ensuite récupérée par le nœud le plus proche du réseau ; selon les [paramètres de gaz](https://metamask.zendesk.com/hc/en-us/articles/360022895972-Using-advanced-gas-controls) de Guillaume, sa transaction sera priorisée (**plus Guillaume est prêt à payer par [unité de gaz](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas), plus sa transaction sera rapidement traitée**), et propagée à d'autres nœuds dans le réseau. Les nœuds se chargeront de vérifier que Guillaume a les ETH à dépenser, puis effectueront effectivement la « transaction » : **le grand livre sera modifié, 0,5 sera débité du solde de Guillaume et 0,5 sera crédité sur le compte de Dolores.** 


*« La main qui bouge, ayant écrit, avance » :* ETH n'a pas transité par un réseau à proprement parler ; ce n'était pas un e-mail envoyé de l'ordinateur de Guillaume à la boîte de réception MetaMask de Dolorès ou quoi que ce soit de ce genre. Guillaume a envoyé une demande, **authentifiée par ses [clés privées via MetaMask](https://metamask.zendesk.com/hc/en-us/articles/4404722782107-User-guide-Secret-Recovery-Phrase-password-and-private-keys)**, au réseau pour débiter son compte et créditer celui de Dolores, et après le processus de vérification programmé dans les protocoles du réseau, cela était fait.


#### *C'est tout ce qu'il y a à faire pour une transaction : une demande au grand livre de réaffecter quelque chose d'une adresse à une autre.*


 


**Lorsque les choses vont mal**
-------------------------------


Les choses peuvent mal tourner pour un certain nombre de raisons. Souvent, il sont de « nature logicielle » : MetaMask a un bug ou quelque chose a été mal configuré concernant le réseau que vous essayez d'utiliser ; il y a une erreur de connectivité.


Un **problème commun est que l'utilisateur, dans une tentative de payer moins pour sa transaction, définit une limite de gaz très faible**, et les conditions de réseau sont si encombrées qu'il n'y a pas d'espace dans des blocs pour une telle transaction « bon marché », parfois pendant très longtemps. Finalement, cette transaction deviendra « périmée » et devra être annulée par l'utilisateur.


**Si vous avez envoyé une transaction et qu'elle n'a pas été finalisée**, son état sera affiché comme « en attente » dans MetaMask.


**Si vous avez envoyé une transaction et qu'elle a échoué, la cause la plus probable est un manque de gaz**. En d'autres termes, vous « n'avez plus de gaz » et la transaction avait un coût en essence qui, lorsqu'il était multiplié par le prix de l'essence, donnait un montant total de la monnaie native du réseau supérieur à ce que vous aviez dans votre portefeuille. 



#### Info


Pour plus d'informations sur le calcul du gaz, consultez notre [guide sur le gaz ici](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas).



Cela peut se produire pour un certain nombre de raisons, mais une chose à considérer est la nature de la transaction que vous essayez d'effectuer. Frapper un NFT pendant les heures de pointe du trafic réseau peut être très gourmand en gaz ; si vous essayez une transaction nouvelle ou expérimentale, il peut être intéressant de l'essayer sur un réseau de test avant de payer des frais de réseau réels.


 


**Corriger le problème**
------------------------


### **Facteur clé n° 1 : local ou diffusion vers le réseau**


Lorsque vous diagnostiquez votre problème de transaction, en particulier lorsqu'il s'agit d'une transaction en attente, vous devez vérifier si la transaction est toujours dans votre pool de mémoire local ou si elle a atteint le réseau et y est bloquée pour une raison quelconque. Si c'est seulement dans votre mempool local, la solution pourrait être aussi simple que le verrouillage et le déverrouillage de votre portefeuille MetaMask (**assurez-vous de connaître votre mot de passe et que votre phrase de récupération secrète est sauvegardée avant de le faire**). Si elle est parvenue jusqu'au réseau, la solution pourrait être plus compliquée.


Pour plus d'informations sur la résolution de ces problèmes, consultez les liens ci-dessous.  
  



### **Facteur clé n° 2 : nonce**


Ce mot peut avoir plusieurs significations. Il s'agit d'une contraction de « numéro utilisé une seule fois » et, dans ce contexte, il signifie approximativement « numéro de transaction », à partir de la première transaction effectuée par l'adresse d'envoi. Vous pouvez vous mettre dans une situation délicate si, par exemple, vous initiez simultanément deux transactions différentes à partir de différentes instances de MetaMask avec la même adresse de portefeuille. **Les transactions de votre adresse doivent être classées par ordre croissant en fonction de leur nonce.** Cependant, tout comme les nonces sont capables de provoquer le blocage d'une transaction, ils peuvent être la clé pour débloquer une transaction.


Pour plus d'informations sur cette technique, [rendez-vous ici](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction).


 


**Prochaines étapes**
---------------------


### *Si votre transaction a échoué ou est en attente, consultez les ressources suivantes pour obtenir de l'aide.*


#### [Comment envoyer des jetons de votre portefeuille MetaMask ?](https://metamask.zendesk.com/hc/en-us/articles/360015488931)


#### [Comment accélérer ou annuler une transaction en attente ?](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction)


#### [Pourquoi ma transaction a-t-elle échoué en raison d'une erreur « manque de gaz » ?](https://metamask.zendesk.com/hc/en-us/articles/360038849792-Why-did-my-transaction-fail-with-an-Out-of-Gas-error-How-can-I-fix-it-)


#### [Dépannage d'Uniswap](https://metamask.zendesk.com/hc/en-us/articles/360053394291-Uniswap-support-and-troubleshooting-tips)


#### [Guide de l'utilisateur : gaz](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas)


#### [Puis-je annuler une transaction déjà confirmée ?](https://metamask.zendesk.com/hc/en-us/articles/360059957352-Can-I-reverse-an-already-confirmed-transaction-)


 


**FAQ**
-------


#### 
*Q : Un compte de mon portefeuille a une transaction en attente ou en file d'attente. Puis-je commencer une autre transaction à partir d'un compte différent dans le même portefeuille ?* R : Oui, vous pouvez. Le nonce est compté par compte et non par portefeuille.

