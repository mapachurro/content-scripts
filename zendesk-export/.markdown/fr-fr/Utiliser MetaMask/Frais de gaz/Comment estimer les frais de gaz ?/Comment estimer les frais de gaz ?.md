### Obtenir le prix du gaz


Si vous êtes sur le réseau Ethereum, vous pouvez vérifier l'[outil de gaz d'Etherscan](https://etherscan.io/gastracker) pour estimer le prix du gaz actuel. Veuillez noter que le prix du gaz fluctue ; il faut toujours se référer à la station-service pour connaître les prix actuels du gaz.


Le réseau Ethereum a besoin de gaz pour exécuter les transactions. Lorsque vous envoyez des jetons, interagissez avec un contrat, envoyez des ETH ou faites quelque chose d'autre sur la blockchain, vous devez payer ce calcul. Ce paiement est calculé en gaz et celui-ci est toujours payé en ETH.


Vous payez pour le calcul, que votre transaction réussisse ou non. Même si elle échoue, les mineurs ou les validateurs doivent finaliser et exécuter votre transaction, ce qui nécessite de la puissance de calcul. Vous devez payer pour ce calcul, tout comme vous le feriez pour une transaction réussie.


 


### Obtenir la limite de gaz


Vous savez donc combien coûte chaque unité de gaz, mais combien d'unités de gaz devez-vous dépenser ? S'il s'agit d'une transaction simple, par exemple l'envoi d'ETH ou d'un jeton ERC-721 à une autre adresse, vous devriez dépenser 21 000 unités de gaz. Si vous faites quelque chose de plus complexe, un bon outil est un explorateur de bloc, tel qu’[Etherscan.io](https://etherscan.io/). Accédez au contrat avec lequel vous souhaitez interagir et commencez à examiner les transactions qui ont été effectuées avec le contrat. Cela vous donnera une meilleure idée de la quantité de gaz que les autres utilisateurs finissent par utiliser.



#### Calculateur de gaz


Il existe quelques outils qui vous permettent d'estimer le coût de l'essence en monnaie fiduciaire avant d'effectuer une transaction. Un exemple est le [calculateur de frais d'essence Cryptoneur](https://www.cryptoneur.xyz/gas-fees-calculator), qui vous permet de saisir les détails de votre transaction et produit une estimation du coût de l'essence dans votre monnaie locale, en fonction de la demande actuelle sur ce réseau (vous pouvez choisir parmi la plupart des grands réseaux compatibles avec l'EVM).



### 
Structure globale des frais de gaz


Conformément à la norme [EIP-1559](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1559.md), les frais globaux que paient un créateur de transaction sont calculés comme suit : **( (frais de base + frais de priorité) x unités de gaz utilisées)**. 


Pour plus d'informations, rendez-vous [ici](https://support.metamask.io/hc/en-us/articles/4404600179227).


 


**Veuillez noter qu'il ne s'agit pas de frais que MetaMask reçoit et que nous ne pouvons donc pas les rembourser.** Ces frais sont payés aux mineurs ou aux validateurs pour finaliser la transaction, la valider dans un bloc et sécuriser la blockchain.

