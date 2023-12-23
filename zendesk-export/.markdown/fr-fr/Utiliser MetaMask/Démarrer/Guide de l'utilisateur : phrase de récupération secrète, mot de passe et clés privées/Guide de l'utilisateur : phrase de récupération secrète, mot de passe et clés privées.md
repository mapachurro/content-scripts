
#### Nouveau dans le domaine de la crypto et du web3 ?


Rendez-vous sur [MetaMask Learn](https://learn.metamask.io/) pour une expérience d'apprentissage simple conçue spécifiquement pour les nouveaux arrivants dans le domaine du web3. Entièrement gratuite, elle est disponible en plusieurs langues et comprend des outils utiles tels que des simulations pour vous aider à trouver vos marques avec MetaMask.



### Dans cet article :


* [Comment la sécurité de MetaMask diffère des comptes Web traditionnels](#h_01FYVAXCSH95CQ08Q0P2VJA5HV)
* [Qu'est-ce qu'une phrase de récupération secrète ?](#h_01FYVAXJQT914HCHEYFPNMEJEA)
* [Les choses à faire et à ne pas faire concernant la phrase de récupération secrète](#h_01FYVAXSE5C9E4YBCSWT2F2RBQ)
* [FAQ sur la phrase de récupération secrète](#h_01FYVAXZYWJENFWG9K9CJTQFK7)
* [Mots de passe et MetaMask](#h_01FYVAY5K22PX6926537V8B4SX)
* [FAQ sur les clés privées](#h_01FYVAYH3ZZ8VW8BPDDADWRC8E)




**MetaMask : un modèle différent de sécurité des** **comptes**
---------------------------------------------------------------


[La technologie de blockchain publique](https://metamask.zendesk.com/hc/en-us/articles/360015489611) utilise un ensemble d'outils très différents pour sécuriser les données des utilisateurs, par rapport aux technologies en ligne traditionnelles. La plupart d'entre nous ont l'habitude de créer un compte avec une application ou un service et de pouvoir, par exemple, écrire au service d'assistance pour réinitialiser leur mot de passe ou leur nom d'utilisateur. Nous sommes habitués à ce que l'application conserve nos données, probablement sur un ordinateur appartenant à l'entreprise.


Eh bien... MetaMask ne fonctionne pas comme ça. MetaMask dispose de trois types de **secrets** différents qui sont utilisés de différentes manières pour garder votre portefeuille et vos comptes privés et sûrs : la phrase de récupération secrète, le mot de passe et les clés privées. Nous allons vous présenter ces secrets un par un.


 


**Introduction aux phrases de récupération secrètes**
-----------------------------------------------------


L'une des technologies clés (vous comprendrez ce que j'ai voulu dire) qui sous-tend MetaMask et la plupart des outils liés aux comptes d'utilisateurs dans l'espace cryptographique est la *phrase mnémonique*, ou comme on l'appelle dans MetaMask, votre *phrase de récupération secrète*. 


#### **Tous vos comptes sont mathématiquement dérivés de votre phrase de récupération secrète. Vous pouvez considérer le SRP comme un trousseau de clés, qui contient autant de clés privées que vous le souhaitez : chacune de ces clés contrôle un compte.**


Maintenant, si vous voulez une explication technique : Les phrases mnémoniques telles que nous les connaissons aujourd'hui ont été codifiées pour une utilisation dans le Bitcoin, conformément à une norme appelée Bitcoin Improvement Proposal 39, ou [BIP-39](https://en.bitcoin.it/wiki/BIP_0039). En termes simples, une série de mots est sélectionnée de manière très aléatoire à partir d'une [liste de mots](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt) spécifique. Dans MetaMask et bien d'autres technologies compatibles avec l'Ethereum, il y a 12 mots dans une phrase mnémonique. Certaines anciennes phrases mnémoniques générées par le navigateur Brave et certains portefeuilles matériels utilisent des phrases de 24 mots.


Chacun de ces mots correspond à une série de chiffres et, lorsqu'ils sont placés dans **un ordre précis**, représentent un moyen beaucoup plus pratique de se souvenir d'un nombre très, très long. Ce numéro est ensuite utilisé pour générer vos comptes *de manière déterministe*, et vous entendrez peut-être parler de portefeuilles déterministes. En informatique, le terme « déterministe » est utilisé pour décrire un processus (généralement un algorithme) qui produira *toujours* le même résultat. En d'autres termes, **votre phrase de récupération secrète générera toujours le même ensemble de comptes dérivés**. 


 


### Il y a un certain nombre de caractéristiques importantes à noter ici :


* La **phrase de récupération secrète est le secret qui contrôle le portefeuille**. Si quelqu'un possède ce secret, il a un accès complet au portefeuille. **MetaMask ne conserve pas votre SRP :** **[vous êtes le dépositaire de votre portefeuille.](https://metamask.zendesk.com/hc/en-us/articles/360059952212)** Les représentants de MetaMask ne vous demanderont **jamais** votre phrase de récupération secrète, même dans le cadre d'une assistance à la clientèle. Si quelqu'un vous la demande, il est probable qu'il essaie de vous escroquer ou de voler vos fonds.
* Votre SRP est **utilisé localement pour obtenir des clés privées**, une par compte/adresse. Les comptes sont stockés sur la blockchain, et ces clés privées déverrouillent ces comptes.
* **Si vous désinstallez l'application** ou l'extension, la version locale des données disparaît (à l'exception notable du [coffre-fort](https://metamask.zendesk.com/hc/en-us/articles/360018766351)), mais toutes les transactions que vous avez effectuées avec cette version locale de MetaMask ont été enregistrées sur la blockchain. Par conséquent, les transactions devraient être reflétées à la fois dans un [explorateur de blocs](https://metamask.zendesk.com/hc/en-us/articles/360057536611) et dans une autre instance de MetaMask, tant que vous [restaurez en utilisant la même phrase de récupération secrète](https://metamask.zendesk.com/hc/en-us/articles/360015289612) (**avec les mots dans le même ordre**). Cela signifie que tant que vous avez votre phrase de récupération secrète, vous serez toujours en mesure de désinstaller MetaMask et de restaurer votre portefeuille.
* **Il est possible d'avoir un très grand nombre de comptes distincts au sein de votre portefeuille.** Lorsque MetaMask crée ou restaure votre portefeuille à partir de la phrase de récupération secrète, il ne produit initialement que le premier compte. Cependant, tous [les comptes supplémentaires que vous créez peuvent être récréés](https://metamask.zendesk.com/hc/en-us/articles/360015489271) dans une instance future de MetaMask. **Le portefeuille étant *déterministe*, il recréera toujours les mêmes comptes, dans le même ordre. Pour plus d'informations à ce sujet, consultez les FAQ ci-dessous.** Notez toutefois que les comptes supplémentaires (au-delà du premier, automatiquement étiqueté « Compte 1 ») ne seront ***pas***automatiquement ré-ajoutés à votre compte en toutes circonstances. Consultez notre explication [ici](https://metamask.zendesk.com/hc/en-us/articles/360015489271-How-to-add-missing-accounts-after-restoring-with-Secret-Recovery-Phrase#:~:text=If%20you%20have,automatically%20re%2Dadded.) pour plus d'informations.
* **Il est possible d'[importer des comptes](https://metamask.zendesk.com/hc/en-us/articles/360015489331) à partir d'autres technologies compatibles avec l'Ethereum dans un portefeuille MetaMask.** Pour ce faire, la *clé privée* de ce compte spécifique est utilisée. Cependant, **ce compte ne sera pas automatiquement restauré par MetaMask dans une autre instance ; vous devrez le ré-ajouter manuellement**. Par conséquent, si vous avez importé manuellement des comptes, **notez leurs clés privées, de la même manière que vous l'avez fait pour votre phrase mnémonique**, afin de pouvoir les réimporter à l'avenir.


 


**Phrase de récupération secrète MetaMask : À faire et à ne pas faire**
-----------------------------------------------------------------------




**À faire :**

* **Notez votre phrase de récupération secrète dans un endroit sûr**. Nous ne pouvons pas vous dire précisément où, car cela dépend de votre situation.
	+ Il est important d'écrire votre phrase de récupération secrète à la main, car elle ne peut pas être volée en ligne. Si vous la stockez dans un fichier dans un dossier de stockage en Cloud lié à Internet, par exemple, elle peut théoriquement être volée.
* Vérifiez votre orthographe et que vous avez écrit tous les mots dans l'ordre où ils ont été donnés.
* Contactez les [canaux officiels](https://metamask.zendesk.com/hc/en-us/articles/360058230211) d'assistance de MetaMask si vous avez besoin d'aide.





**À ne pas faire :**

* La conserver dans un endroit facile à découvrir ou à pirater, par exemple dans un document ou un e-mail enregistré dans le Cloud et intitulé « Phrase mnémonique », ou sur un post-it collé sur votre ordinateur.
* Fournir votre phrase mnémonique à n'importe qui, même s'il dit qu'il vient du service d'assistance de MetaMask.
* Modifier l'ordre des mots.





 


**Phrase de récupération secrète : FAQ**
----------------------------------------


### Ma phrase mnémonique a restauré un compte différent !


Veuillez consulter l'article de base de connaissances sur ce sujet [ici](https://metamask.zendesk.com/hc/en-us/articles/360058120992). En outre, consultez le fil de discussion de la Communauté [ici](https://community.metamask.io/t/restored-metamask-no-coins-are-showing/878/107?u=jacob.cantele) pour plus de contexte et d'informations générales.


### Autre FAQ sur la phrase de récupération secrète :


[Comment révéler votre phrase de récupération secrète](https://metamask.zendesk.com/hc/en-us/articles/360015290032)


[Comment récupérer votre phrase de récupération secrète](https://metamask.zendesk.com/hc/en-us/articles/360018766351)


[Importer une phrase mnémonique à partir d'un autre logiciel de portefeuille : chemin de dérivation](https://metamask.zendesk.com/hc/en-us/articles/360060331752)


[Guide de migration de portefeuille](https://metamask.zendesk.com/hc/en-us/articles/4867408571803)


[Comment importer un compte](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[Comment vérifier mon activité de portefeuille sur l'explorateur de la blockchain](https://metamask.zendesk.com/hc/en-us/articles/360057536611)


[Qu'est-ce qu'une phrase de récupération secrète et comment puis-je protéger mon portefeuille ?](https://metamask.zendesk.com/hc/en-us/articles/360060826432)


 


**Mots de passe et MetaMask**
-----------------------------


MetaMask utilise des mots de passe dans un seul but : sécuriser l'application elle-même ; en d'autres termes, ouvrir l'application, q'il s'agisse de l'application mobile ou de l'extension dans le navigateur. Une fois que vous avez restauré ou créé votre portefeuille à partir de votre phrase de récupération secrète, vous n'en aurez plus besoin régulièrement (**bien que vous devrez la sauvegarder et la mettre en sécurité**), et vous utiliserez votre mot de passe (ou plus couramment sur mobile, une authentification biométrique telle que la reconnaissance faciale ou votre empreinte digitale) pour déverrouiller l'application. Pour plus de détails, consultez notre article [ici](https://metamask.zendesk.com/hc/en-us/articles/4405451730331).


 


**Clés privées**
----------------


Bien qu'une phrase de récupération secrète est utilisée pour créer et restaurer l'ensemble de votre portefeuille MetaMask, y compris tous les comptes créés dans ce portefeuille, chaque compte possède sa propre *clé privée*. Cette clé peut être utilisée pour importer ce compte, et ce compte uniquement, dans un portefeuille différent. De même, des comptes uniques provenant d'autres technologies de crypto peuvent être importés dans votre portefeuille MetaMask. 


### FAQ sur les clés privées :


[Que sont les comptes importés ?](https://metamask.zendesk.com/hc/en-us/articles/360015289932)


[Comment importer un compte](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[Comment exporter la clé privée d'un compte](https://metamask.zendesk.com/hc/en-us/articles/360015289632)


[Puis-je importer un compte de portefeuille Coinbase dans mon portefeuille MetaMask ?](https://metamask.zendesk.com/hc/en-us/articles/360058485292)

