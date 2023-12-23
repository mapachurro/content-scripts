Lorsque vous soumettez une transaction sur Ethereum ou un réseau compatible, une partie du gaz que vous payez est une offre au réseau de traiter votre transaction plus rapidement cet élément est connu sous le nom de frais de priorité. Bien que MetaMask vous aide à calculer le tarif total du gaz pour que votre transaction soit prise en compte, vous risquez d'attendre longtemps si vous soumettez votre demande avec un tarif de gaz peu élevé. Pour obtenir des conseils sur les prix du gaz qui permettront de finaliser une transaction dans un délai raisonnable, veuillez vous référer à des sources telles que [le suivi de gaz d'Etherscan](https://etherscan.io/gastracker), ou un suivi similaire pour le réseau que vous utilisez.


En outre, il arrive parfois que quelque chose se passe mal et qu'une transaction reste bloquée ou en attente pendant très longtemps.


Quelle que soit la façon dont vous en êtes arrivé là, il existe plusieurs façons d'y remédier.


 


### Avant de prendre toute autre mesure, la première étape consiste à quitter et à fermer complètement votre navigateur, à le rouvrir et à déverrouiller MetaMask (sur mobile, il suffit de fermer l'application et de la rouvrir). Si cela ne résout pas le problème, continuez avec les éléments suivants :


 


**Accélérer une transaction**
-----------------------------


![MetaMask accélère la transaction](https://support.metamask.io/hc/article_attachments/12927043481371)


Essayez l'une des options ci-dessous :


* Attendez que le réseau soit prêt à traiter des transactions à ce prix
* Si vous ne l'avez pas encore fait, cliquez sur ce bouton « **Accélérer** ». Vous pourrez ainsi soumettre à nouveau la même transaction, mais avec des frais de gaz plus élevés qui devraient permettre un traitement plus rapide de la transaction. Comme ce processus réutilise le même nonce que l'original, vous ne devez pas payer le gaz deux fois.


N'oubliez pas **qu'en accélérant la transaction, vous augmentez le montant que vous dépensez pour la transaction**.


 


**Annuler une transaction – Méthode 1 : annulation dans l'application**
-----------------------------------------------------------------------


Si vous ne l'avez pas encore fait pour annuler la transaction, sélectionnez simplement « **Annuler** » comme dans la capture d'écran ci-dessus. Veuillez noter **qu'une annulation ne peut être *tentée* que si la transaction est toujours en attente sur le réseau.** Les transactions qui ont déjà été confirmées ne peuvent pas être annulées.


 


**Annuler une transaction – Méthode 2 : nonce personnalisé**
------------------------------------------------------------


Ce processus implique l'envoi d'une nouvelle transaction avec le même nonce (un numéro d'identification pour chaque transaction, dérivé de l'expression « numéro utilisé une seule fois »). La transaction ne doit pas nécessairement avoir une valeur (par exemple, vous pouvez envoyer 0 ETH). Ce qui importe est que vous payiez suffisamment de gaz pour que le réseau puisse la prioriser.


Lorsque vous utilisez cette méthode, **vous devez remonter à partir de la plus ancienne transaction en attente dans la file d'attente que vous souhaitez annuler**. Par exemple, vous ne pouvez pas tenter d'annuler une transaction avec un nonce de 10 avant d'annuler le nonce 9.


*Les captures d'écran ci-dessous ont été réalisées à des moments différents, de sorte que les tarifs du gaz qui y figurent peuvent varier, même d'une étape à l'autre. Ne vous laissez pas décourager ! Lorsque vous le faites vous-même, MetaMask se met automatiquement à jour en temps réel pour afficher les taux du marché.*




Extension Mobile


1. Dans les paramètres avancés, activez « **Personnaliser le nonce de la transaction** » et « **Contrôles de gaz avancés** ». Cette dernière vous permettra de manipuler le gaz que vous payez et de vous assurer que votre transaction d'annulation est traitée avant la transaction initiale que vous voulez annuler.



#### Remarque :


MetaMask Extension dispose actuellement d'une fonctionnalité expérimentale disponible appelée [Enhanced Gas Fee UI](https://metamask.io/1559/) (à ne pas confondre avec [les contrôles avancés du gaz](https://support.metamask.io/hc/en-us/articles/360022895972)). Ces étapes peuvent être exécutées, que cette option soit activée ou non, mais n'oubliez pas qu'elles auront un aspect différent. Les étapes ci-dessous n'utilisent pas l'interface utilisateur améliorée pour le gaz. N'oubliez pas :



	* Si vous avez activé l'interface utilisateur améliorée pour le gaz, vous devez également activer l'option « Personnaliser le nonce de la transaction ».
	* Si vous n'avez pas activé l'interface utilisateur améliorée pour le gaz, vous devez activer les options « Contrôles avancés du gaz » et « Personnaliser le nonce de transaction ».

![Paramètres avancés MetaMask](https://support.metamask.io/hc/article_attachments/12927064113947)
2. **Envoyez une nouvelle transaction**. Dans cette nouvelle transaction, envoyez **À** vous-même, c'est-à-dire votre adresse publique MetaMask. **Remplissez « Nonce personnalisé » avec le même nonce que la transaction qui est toujours en attente** :


![Metamask_custom_transaction_nonce_Extension.png](https://support.metamask.io/hc/article_attachments/12927064259483)
3. Cliquez ensuite sur « Modifier » à côté de « Tarif du gaz » (si vous avez activé [l'interface utilisateur expérimentale améliorée pour le gaz](https://support.metamask.io/hc/en-us/articles/360022895972-Using-advanced-gas-controls#:~:text=%C2%A0-,Enhanced%20Gas%20UI,-Since%20the%20introduction), celle-ci apparaîtra en tant que « Marché »). Vous verrez maintenant les options ci-dessous :


![Extension des contrôles de gaz avancés MetaMask](https://support.metamask.io/hc/article_attachments/12927065407515)


Pour vous assurer que votre demande d'annulation est saisie avec le statut prioritaire, et avant la transaction initiale, **vous devrez payer plus pour le gaz**. Suivez ces instructions :


	* Définissez votre **limite de gaz** comparable à votre transaction initiale *ou légèrement plus élevée*.
	* Définissez vos **frais de priorité maximum** à *au moins 10 % plus élevés* (en Gwei) que les frais de gaz de la transaction initiale (en attente) (par exemple, si cette transaction avait des frais de gaz de 30 Gwei, définissez les frais de priorité maximum dans la transaction de remplacement/annulation à 33-35 Gwei).
	* Assurez-vous que vos frais maximum sont au moins 30 % plus élevés que les frais maximum de la transaction que vous remplacez. Par exemple, si vos frais précédents étaient de 150 Gwei, choisissez quelque chose de plus proche de 200 Gwei cette fois.Consultez un suivi de gaz comme la [station de gaz ETH](https://etherscan.io/gastracker) ou [Etherscan](https://ethgasstation.info/) pour obtenir des conseils sur les frais maximum recommandés.




1. **Dans Paramètres > Avancés, activez l'option « Personnaliser le nonce de la transaction ».**
2. **Envoyez une nouvelle transaction.** Dans cette nouvelle transaction, envoyez À vous-même, c'est-à-dire votre adresse publique MetaMask. **Remplir le champ « Nonce personnalisé » avec le même nonce que celui de la transaction encore en cours**.


Pour trouver le paramètre de nonce personnalisé dans l'application, accédez à l'écran de confirmation de la transaction, qui s'affiche une fois que vous avez saisi la quantité de jetons et le destinataire. Cliquez sur « Modifier » pour le changer :


![Nonce de transaction personnalisé MetaMask Mobile](https://support.metamask.io/hc/article_attachments/12927068442907)
3. Vous devez maintenant vous assurer que vos paramètres de gaz sont configurés de telle sorte que votre transaction de remplacement soit traitée. Dans l'écran de confirmation de la transaction, appuyez sur la valeur de gaz en surbrillance :


![Contrôle avancé des gaz MetaMask mobile](https://support.metamask.io/hc/article_attachments/12927041593755)


Accédez ensuite aux « Options avancées » dans le menu qui s'affiche.
4. À partir de là, vous pouvez ajuster précisément le gaz pour vous assurer que votre transaction est prise en charge. Vous verrez alors apparaître un écran qui ressemble à celui-ci :


![Contrôle avancé des gaz MetaMask mobile](https://support.metamask.io/hc/article_attachments/12927063201691)


À partir de là, ajustez les paramètres de gaz. Suivez ces instructions pour vous assurer que votre transaction est bien prise en charge :


	* Définissez votre **limite de gaz** comparable à votre transaction initiale *ou légèrement plus élevée*.
	* Définissez vos **frais de priorité maximum** à *au moins 10 % plus élevés* (en Gwei) que les frais de gaz de la transaction initiale (en attente) (par exemple, si cette transaction avait des frais de gaz de 30 Gwei, définissez les frais de priorité maximum dans la transaction de remplacement/annulation à 33-35 Gwei).
	* Assurez-vous que vos **frais maximum** sont *au moins 30 % plus élevés* que les frais maximum de la transaction que vous remplacez. Par exemple, si vos frais précédents étaient de 150 Gwei, choisissez quelque chose de plus proche de 200 Gwei cette fois.Consultez un suivi de gaz comme la [station de gaz](https://ethgasstation.info/) ETH ou [Etherscan](https://etherscan.io/gastracker) pour obtenir des conseils sur les frais maximum recommandés.



