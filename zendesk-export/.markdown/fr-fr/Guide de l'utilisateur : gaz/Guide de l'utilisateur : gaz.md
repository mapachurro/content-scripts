
#### Nouveau dans le domaine de la crypto et du web3 ?


Rendez-vous sur [MetaMask Learn](https://learn.metamask.io/) pour une expérience d'apprentissage simple conçue spécifiquement pour les nouveaux arrivants dans le domaine du web3. Entièrement gratuite, elle est disponible en plusieurs langues et comprend des outils utiles tels que des simulations pour vous aider à trouver vos marques avec MetaMask.



Le gaz est l'unité de mesure pour la quantité de travail de calcul nécessaire pour traiter les transactions et les contrats intelligents. Désignant essentiellement des frais de transaction, le terme provient d'Ethereum. Dans ce contexte, il fait référence au calcul effectué sur la machine virtuelle Ethereum (EVM). Depuis la création d'Ethereum, de nombreux produits compatibles avec EVM (et non compatibles avec EVM !) des réseaux ont vu le jour et ont adopté des modèles similaires. 


Le terme est analogue à l'essence qui alimente le moteur d'une voiture : il s'agit du coût fluctuant et parfois onéreux de l'opération. Les contrats intelligents plus complexes nécessitent plus de gaz pour alimenter leur calcul, tout comme une voiture plus grande et plus puissante nécessite plus de carburant pour fonctionner.


La méthode de calcul des frais de gaz varie en fonction du réseau. Par exemple, le calcul de gaz sur Ethereum était très compliqué, mais a été considérablement simplifié avec la mise en œuvre du protocole d'amélioration d'Ethereum **(EIP) 1559** en août 2021 (aussi connu sous le nom de London Upgrade). En résumé, vous payez une **redevance** de base pour chaque unité de gaz, qui est ***brûlée*** (c'est-à-dire qu'elle est supprimée et disparaît) une fois la transaction effectuée avec succès. En plus des frais de base, vous ajoutez des **frais de priorité**, à nouveau mesurés par unité de gaz, dont la valeur dépend de la rapidité avec laquelle vous souhaitez que la transaction soit traitée. 


Dans le large éventail de réseaux compatibles EVM disponibles, le gaz, ou des alternatives fonctionnant de manière similaire, sont essentiellement devenus la méthode standard de calcul des coûts de transaction. Les frais sont payés dans le jeton natif du réseau : par exemple, toute transaction sur Ethereum nécessite ETH, l'utilisation de BSC nécessite BNB et celle de Polygon a besoin de MATIC. Certains réseaux ont adopté le modèle de gros EIP-1559 d'Ethereum, comme Polygon, tandis que d'autres ont fait des ajustements, y compris Avalanche, pour leur C-Chain (qui [brûle à la fois les frais de base et les frais de priorité](https://docs.avax.network/learn/platform-overview/transaction-fees/#c-chain-fees), et non pas seulement le premier). 


Si vous souhaitez lire un article plus approfondi sur le fonctionnement du gaz sur Ethereum, cliquez [ici](https://ethereum.org/en/developers/docs/gas/). 


 


Voici quelques **détails essentiels pour gérer le gaz** **dans MetaMask** :


#### **La limite de gaz (unités de gaz utilisées)**


La *limite de gaz* est le **nombre maximum d'unités de gaz que vous êtes prêt à payer** pour effectuer une transaction ou une opération EVM. Différentes opérations exigent différentes quantités d'unités à gaz. Une transaction normale envoyant ETH ou un jeton coûte normalement **21 000** unités de gaz, alors qu'une homologation de jeton ERC-20 nécessite 45 000. Beaucoup de réseaux, comme la blockchain Harmony compatible EVM, utilisent un modèle identique dans lequel les transactions standard coûtent également 21 000 gaz. 



#### Dois-je modifier la limite de gaz ?


Non ! MetaMask définit automatiquement votre limite de gaz en fonction de la transaction que vous essayez d'exécuter. Dans la grande majorité des cas, cela suffira pour effectuer votre transaction. Si vous souhaitez la vérifier ou la modifier, assurez-vous que les [contrôles avancés du gaz](https://metamask.zendesk.com/hc/en-us/articles/360022895972) sont activés (ou que vous utilisez l'interface utilisateur expérimentale pour le gaz) et cliquez sur « Modifier » dans l'écran de confirmation de la transaction.



#### **La taxe de base**


Chaque bloc du réseau Ethereum a une taxe de base déterminée par la demande du réseau : la taxe de base est basée sur la taille du bloc précédent, par rapport à une taille de bloc cible (où la taille fait référence à la quantité totale de gaz utilisée pour toutes les transactions incluses dans le bloc). Si la taille du bloc précédent dépasse l'objectif, la taxe de base pour le bloc suivant augmente de 12,5 %, vous laissant, en tant qu'utilisateur (ou votre portefeuille), avec une certitude absolue quant à la commission de base du bloc à venir. Votre taxe totale sur le gaz doit correspondre au minimum à ce prix pour être pris en compte dans le bloc. 


#### **La taxe de priorité**


La *commission de priorité*, également appelée « conseil de mineur », incite le mineur à donner la priorité à votre transaction. 


Naturellement, la question de savoir si ces frais reviennent effectivement à un mineur dépend du [mécanisme de consensus](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) qu'il utilise : le réseau principal d'Ethereum est devenu un réseau de preuve d'enjeu à la suite de la fusion en septembre 2022, de sorte que les frais de priorité sont versés aux validateurs plutôt qu'aux mineurs. 


#### **Les frais maximum**


Les frais maximum sont le total du montant global payé pour votre transaction. Il est calculé comme : **(****frais de base + frais de priorité) x unités de gaz utilisés.** MetaMask définit initialement ce montant sur la base de l'historique du bloc précédent. Cependant, les utilisateurs peuvent modifier ce montant par le biais de paramètres personnalisés (voir ci-dessous). La différence entre la taxe maximale par gaz et (redevance de base + redevance de priorité maximale par gaz) est « remboursée » à l'utilisateur.


 


### **Concepts supplémentaires**


#### **Gwei**


Gwei est une unité d'ether, la plus petite dénomination, qui représente [gigawei](https://ethgasstation.info/blog/gwei/) (ou 1 000 000 000). [Gwei](https://www.investopedia.com/terms/g/gwei-ethereum.asp) est utilisé pour les frais de gaz, ou plutôt les paiements effectués par les utilisateurs pour compenser l'énergie de calcul nécessaire pour traiter et valider les transactions sur la blockchain Ethereum. 


D'autres réseaux ont également tendance à calculer les coûts à l'aide de gwei, par exemple, Fantom, Harmony et Avalanche.


#### **Slippage**


Le slippage (ou effet de glissement) est la différence de pourcentage attendue entre un prix coté et un prix exécuté.


#### **Frais de gaz**


Les *frais* de gaz se réfèrent aux frais de transaction sur la blockchain Ethereum. C'est ce que les utilisateurs payent pour obtenir leur transaction validée ou complétée. 


#### **Frais de base**


Générés par le protocole. Ils représentent le multiplicateur minimum « gasUsed » requis pour qu'une transaction soit incluse dans un bloc (c'est-à-dire qu'une transaction soit complétée). Ceci est la partie des frais de transaction qui sont brûlés.


 


### **Contrôles de gaz avancés**


Si vous souhaitez entrer dans les détails de vos commandes de gaz (cela peut être utile si vous testez un dapp, par exemple), MetaMask peut le faire ! Consultez l'article complet i[ci.](https://metamask.zendesk.com/hc/en-us/articles/360022895972)


 


### **FAQ**


[Pourquoi ai-je payé des frais de gaz pour une transaction qui a échoué ?](https://metamask.zendesk.com/hc/en-us/articles/360045439051)


[Pouvez-vous rembourser mes frais de gaz ?](https://metamask.zendesk.com/hc/en-us/articles/360058370012)


[Comment puis-je accélérer ou annuler une transaction en attente ?](https://metamask.zendesk.com/hc/en-us/articles/360015489251)


[Comment estimer les frais de gaz](https://metamask.zendesk.com/hc/en-us/articles/360059562111)


[Pourquoi mes frais de gaz sont-ils si élevés ?](https://metamask.zendesk.com/hc/en-us/articles/360058751211-Why-my-gas-fees-are-so-high-)


[Erreur : [ethjs-query] lors du formatage des sorties de RPC (erreur de transaction sous-évaluée)](https://metamask.zendesk.com/hc/en-us/articles/4402538041869)


[Comment corriger l'erreur de « fonds insuffisants » ou le bouton de confirmation grisé](https://metamask.zendesk.com/hc/en-us/articles/360044703372)


 


 

