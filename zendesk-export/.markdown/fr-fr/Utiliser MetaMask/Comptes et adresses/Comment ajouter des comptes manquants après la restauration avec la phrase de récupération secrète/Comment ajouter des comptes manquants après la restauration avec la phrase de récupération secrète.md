
#### Remarque :


Tous les comptes **importés** ne seront **pas** rajoutés lorsque vous restaurerez votre portefeuille en utilisant votre phrase secrète de récupération. [Ils doivent être réajoutés manuellement](https://support.metamask.io/hc/en-us/articles/360015489331) de la même manière que vous les avez importés à l'origine.



**NE PARTAGEZ votre phrase de récupération secrète avec personne ! Ces mots peuvent être utilisés pour voler tous vos comptes. Vous ne pouvez pas modifier ou changer votre phrase de récupération secrète.**


 


Lorsque vous [restaurez un portefeuille](https://support.metamask.io/hc/en-us/articles/360015289612-How-to-restore-your-MetaMask-account-from-Seed-Phrase-Secret-Recovery-Phrase) à l'aide de votre phrase secrète de récupération, MetaMask réintègre automatiquement tous les comptes supplémentaires que vous aviez précédemment [créés](https://support.metamask.io/hc/en-us/articles/360015289452), mais uniquement sous certaines conditions.


MetaMask essaiera d'ajouter vos comptes supplémentaires lorsque cela est possible (en supposant qu'ils n'ont pas été [importés](https://support.metamask.io/hc/en-us/articles/360015289932)) en vérifiant vos comptes précédents dans l'ordre croissant (c'est-à-dire le compte 2, puis le compte 3, etc.). **Les comptes sont automatiquement rajoutés s'ils ont un solde d'ETH non nul**. Cependant, ce processus se termine lorsque MetaMask rencontre un compte avec 0 ETH, donc le premier compte avec 0 ETH (et tous ceux qui suivent) ne sera *pas* ajouté.


Gardez à l'esprit que **ce processus ne vérifie que les soldes d'ETH sur le réseau Ethereum** afin que d'autres jetons ou jetons sur d'autres réseaux ne provoquent pas le nouvel ajout automatique de votre compte.


**Pour tous ceux qui ne sont pas rajoutés automatiquement, vous devrez les ajouter en « [créant](https://support.metamask.io/hc/en-us/articles/360015289452) » un compte**. Par exemple, si vous avez quelques jetons dans le Compte 4, mais que le Compte 4 n'est pas automatiquement ajouté parce que ces jetons ne sont pas des ETH sur le réseau, tout ce que vous devez faire est d'ajouter manuellement des comptes (en utilisant les étapes ci-dessous) jusqu'à ce que vous arriviez au Compte 4. Votre compte 4 *avant* la restauration correspond au Compte 4 *après* la restauration, peu importe le nom que vous avez précédemment appliqué.


Si vous devez utiliser le bouton « créer » pour ajouter de nouveaux comptes, ne vous inquiétez pas si l'adresse du compte est différente. Les adresses sont dérivées de manière cryptographique et *déterministe* de votre clé privée, ce qui signifie qu'elles seront toujours les mêmes. Et comme un compte Ethereum, une fois créé, existe en permanence, vous pouvez reprendre là où vous vous êtes arrêté.


Veuillez suivre les étapes ci-dessous concernant la façon de restaurer vos autres comptes dans l'ordre dans lequel ils ont été initialement créés :




Extension Mobile


1. Cliquez sur le favicon dans le coin supérieur droit du menu déroulant MetaMask
2. Cliquez sur « Créer un compte » pour restaurer vos comptes MetaMask dans l'ordre dans lequel ils ont été créés
3. Si les comptes ont été précédemment nommés, vous pouvez les nommer à nouveau dans l'étape ci-dessous avant de cliquer sur « **Créer** »


![How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase.gif](https://support.metamask.io/hc/article_attachments/9026739981083/How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase.gif)




1. Appuyez sur l'icône hamburger dans le coin supérieur gauche de l'écran pour faire apparaître le menu. À partir d'ici, appuyez sur la flèche déroulante à côté de votre nom de compte :
2. Appuyez sur « Créer un nouveau compte » :


![How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase_Mobile.gif](https://support.metamask.io/hc/article_attachments/9027058464027/How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase_Mobile.gif)




Si vous ne voyez toujours pas les adresses que vous recherchez, elles ont probablement été créées avec une autre phrase de récupération secrète ou vous avez un compte importé que vous devez encore réimporter à l'aide de clés privées ou de JSON. Veuillez consulter [cet article sur la façon d'importer un compte](https://support.metamask.io/hc/en-us/articles/360015489331-Importing-an-Account).

