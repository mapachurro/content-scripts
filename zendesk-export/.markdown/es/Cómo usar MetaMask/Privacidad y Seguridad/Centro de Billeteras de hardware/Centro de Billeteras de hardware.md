### MetaMask es compatible actualmente con cinco líneas de billeteras hardware: AirGap Vault, Keystone, Lattice, Ledger y Trezor. Estas billeteras son compatibles con Extensión, y podrán ser añadidas a Mobile en próximas actualizaciones.



#### ¿Estoy en el sitio correcto?


Si está buscando una explicación sobre qué es una billetera hardware y por qué debería tener una, siga leyendo.


Si está buscando asistencia para su billetera hardware en particular, desplácese hacia abajo hasta la sección correspondiente.


Si es la primera vez que configura su billetera hardware, **consulte nuestra [Guía del usuario](https://support.metamask.io/hc/en-us/articles/5450173968283) para ver la configuración recomendada.**



#### 


¿Qué es una billetera hardware? ¿Y por qué debería tener una?
-------------------------------------------------------------


Para conocer las billeteras hardware, hay que meterse un poco "debajo del capó" de Ethereum. Veamos primero a qué nos referimos cuando hablamos de "billetera". A simple vista, se trata de un concepto intuitivo: una especie de contenedor digital para almacenar dinero y otros activos digitales. Al igual que en una cartera física, puede tener algo de dinero y algunas fotos de su familia o su gato, en su billetera MetaMask puede guardar algo de dinero, algunos CryptoKitties y un GIF animado de un zombi. Bastante parecido hasta ahora.


Bueno, resulta que llamarlo "billetera" es un término un poco metafórico. Desde el punto de vista de nuestra experiencia, es una buena metáfora, pero tecnológicamente no representa con exactitud lo que está ocurriendo. El contenido de su "billetera" en realidad consiste *en los activos asignados a su dirección en la cadena de bloques*. Cuando enviamos ETH "a" alguien, en realidad no *se mueve* a ninguna parte; simplemente se resta del saldo de ETH asignado a su dirección y se agrega al saldo de la dirección a la que está enviando. Recuerde, una cadena de bloques pública también se denomina *tecnología de libro mayor distribuido*, y todas nuestras billeteras son líneas en ese libro mayor; nuestros saldos, nuestras tenencias, son las columnas, y la Máquina Virtual Ethereum es nuestro contador automatizado.


En este sentido, MetaMask es "simplemente" una aplicación web que envía solicitudes a la cadena de bloques de Ethereum: para obtener información sobre los activos asignados a su dirección, para "enviar" tokens de una dirección a otra, y realizar otras operaciones similares. Para ello, se utiliza la Frase de Recuperación Secreta.


Tu dirección pública de Ethereum es la mitad de un par: un *par de claves criptográficas*, para ser más precisos. La parte pública, su dirección, se puede dar a cualquiera sin temor a que pueda piratear y robar sus fondos. La parte privada, la Frase de Recuperación Secreta (también conocida como "frase semilla"), permite autentificar a quien la posea para que tenga acceso total y completo a la dirección y a todas las cuentas asociadas a ella. **Recuerda: "ni tus claves, ni tus monedas".**


Ahora, MetaMask es extremadamente seguro, y mientras nadie tenga acceso a su Frase de Recuperación Secreta ([¿La ha guardado en un lugar seguro y sin conexión a internet? ¿Verdad?](https://support.metamask.io/hc/en-us/articles/4404722782107)), su cuenta debe estar protegida. Hay muchos otros factores que están fuera del control de MetaMask y sus ingenieros de seguridad: cómo de seguro es tu navegador, si alguien toma el control físico de su ordenador o infecta su ordenador con un virus, entre otros.


Por esta razón, recomendamos que si estás almacenando alguna cantidad significativa de valor en su billetera MetaMask, o simplemente activos que son importantes para usted, utilice una billetera hardware como una segunda línea de defensa.


Una vez que se han abordado todos estos antecedentes:



TL;DR
------


### **Una billetera hardware es un dispositivo físico fuera de tu ordenador que protege las claves de tu billetera y actúa como un firewall entre posibles atacantes y el contenido de tu billetera.**


Para realizar transacciones con fondos asegurados por una billetera hardware, usted tendrá que interactuar con la billetera hardware para aprobar la transacción. De esta manera, incluso si alguien de alguna manera obtiene acceso a tu billetera MetaMask, se le impedirá mover cosas fuera de ella.


 


Bóveda AirGap
-------------


* [Conectar la Bóveda AirGap a MetaMask](https://support.airgap.it/guides/metamask/)
* [Bóveda AirGap - Android Play Store](https://play.google.com/store/apps/details?id=it.airgap.vault&hl=en_US&gl=US)
* [Bóveda AirGap - iOS App Store](https://apps.apple.com/us/app/airgap-vault-secure-secrets/id1417126841)


Keystone
--------


* [Vincular su Keystone a su MetaMask Wallet](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/bind-metamask-with-keystone)
* [Cómo conectar Keystone a MetaMask Mobile y enviar ETH](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile)
* [Cómo usar Keystone con MetaMask Mobile para dApps a través de Wallet Connect](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile/defi-with-metamask-mobile)
* [Cómo configurar cadenas EVM en MetaMask Mobile](https://support.keyst.one/3rd-party-wallets/eth-and-web3-wallets-keystone/metamask-mobile/configuring-evm-chains-on-metamask-mobile)
* [Cómo beneficiarse de la seguridad de la billetera de hardware utilizando códigos QR transparentes](https://consensys.net/blog/news/metamask-x-keystone-how-to-benefit-from-hardware-wallet-security-using-transparent-qr-code/)
* Para comprender la propuesta de valor añadido de seguridad de Keystone, [consulte aquí](https://blog.keyst.one/blind-signing-a-security-black-hole-for-the-ethereum-community-13f909b848b6)
* Para temas avanzados sobre las características de seguridad de Keystone, incluida la incorporación de entropía personalizada, [leer aquí](https://support.keyst.one/general-navigation-guide#advanced-users).


Lattice
-------


* Para los usuarios de Lattice por primera vez, asegúrese de que está configurado correctamente: <https://gridplus.io/setup>
* Consulte la documentación de "GridPlus" sobre cómo empezar a utilizar MetaMask y un Lattice [aquí](https://docs.gridplus.io/setup/metamask)


Ledger
------


Ledger tiene una amplia documentación para los usuarios de MetaMask. Aquí hay algunos que le ayudarán a empezar:  



* [Configurar y utilizar MetaMask para acceder a su cuenta Ledger Ethereum (ETH)](https://support.ledger.com/hc/en-us/articles/4404366864657-Set-up-and-use-MetaMask-to-access-your-Ledger-Ethereum-ETH-account?docs=true)
* [No veo mis tokens BEP-20 en mi cuenta Ledger Binance Smart Chain (BSC), ¿qué puedo hacer?](https://support.ledger.com/hc/en-us/articles/4406111561617-I-don-t-see-my-BEP-20-tokens-in-my-Ledger-Binance-Smart-Chain-BSC-account-what-can-I-do-?support=true)
* [Cómo acceder a su cuenta Ledger Polygon a través de MetaMask](https://support.ledger.com/hc/en-us/articles/4418394184209-How-to-access-your-Ledger-Polygon-MATIC-account-via-Metamask?docs=true)


Trezor
------


* Consulte la documentación de Trezor relativa a la operabilidad con MetaMask [aquí](https://wiki.trezor.io/Apps:MetaMask).
