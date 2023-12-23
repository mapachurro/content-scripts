
#### ¿Eres nuevo en criptomonedas y web3?


Visite [MetaMask Learn](https://learn.metamask.io/) para obtener una experiencia de aprendizaje directa diseñada específicamente para los recién llegados a web3. Es totalmente gratis y está disponible en varios idiomas e incluye herramientas útiles, como simulaciones, que le ayudarán a familiarizarte con MetaMask.



#### *Este artículo contiene una explicación y enlaces a recursos sobre las transacciones y por qué fallan, además de, más adelante, enlaces a escenarios comunes de transacciones fallidas y cómo solucionarlo:*


* [Anatomía de una transacción en una cadena de bloques](#h_01G79J04D0EN1VD8VS7C7J7KD1)
* [Problemas comunes](#h_01G79J09NWA8CGR4VYC2PT5B6Y)
* [Soluciones principales](#h_01G79J0J8JTRPM9MRB76EN1GPP)
* [Recursos adicionales y pasos a seguir](#h_01G79J0RP8ZMZ1V1SKQY70TXCT)
* [Preguntas frecuentes](#h_01G79J18RBK27GZCF10CGN9GKP)


 


**Anatomía de una transacción en una cadena de bloques**
--------------------------------------------------------


Cuando hablamos de 'transacciones' en una cadena de bloques pública, por lo general estamos hablando de interacciones entre dos direcciones; en otras palabras, tokens, ya sean fungibles o no, u otros activos criptográficos que se "mandan" desde una dirección a otra. También hay transacciones llamadas "transacciones internas", que son interacciones que se producen entre contratos inteligentes, y en su mayor parte quedan fuera del alcance de este artículo.



#### ¿Quiere más información?


Para obtener más información sobre las redes de cadenas de bloques y su funcionamiento en general, consulte nuestra [publicación artículo introductorio aquí](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-), y si se queda atascado en alguna palabra desconocida, nuestro [glosario está siempre disponible](https://consensys.net/knowledge-base/a-blockchain-glossary-for-beginners/)



Para que quede claro, nada se está *enviando* en realidad a ningún lado. Las redes de cadenas de bloques con contratos inteligentes como Ethereum tienen varios componentes o funciones. Uno de ellos es lo que llamaríamos un "computadora": la máquina virtual de Ethereum, o EVM, capaz de ejecutar programas ("contratos inteligentes"). Sin embargo, la columna vertebral del sistema es un *libro de contabilidad distribuido*: **imagínese una hoja de cálculo que contiene, por un lado, todas las direcciones de las billeteras de Ethereum, y cada dirección tiene una columna para cada tipo de criptoactivo que posee.**


Usemos un ejemplo para entenderlo. Digamos que Guillaume quiere enviar una transacción a Dolores. Guillaume tiene 1,36 ETH en su cuenta, y piensa enviar a Dolores 0,5 ETH. Es un buen día para Dolores, incluso en un mercado bajista.


Guillaume abre su billetera de MetaMask e introduce la dirección de Dolores, configura los parámetros de gas que está dispuesto a pagar, y le da al botón 'Enviar'.


En este momento, la transacción entra en un estado temporal de espera en el disco local, conocido como *el grupo de memoria*, que en inglés se conoce como memory pool, o *local mempool*. Luego, el nodo de la red más cercano le 'recogerá' a la transacción, y en función de la [configuración de gas](https://metamask.zendesk.com/hc/en-us/articles/360022895972-Using-advanced-gas-controls) de Guillaume, a su transacción se le priorizará (**cuanto más Guillaume está dispuesto a pagar por [cada unidad de gas,](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas) tanto más rápido se procesará su transacción**), y se propagará a otros nodos en la red. Los nodos harán el trabajo de verificar que Guillaume tenga el ETH para gastar, y luego en realidad realizarán la 'transacción': **el libro de contabilidad se modificará; 0,5 se cargará al saldo de Guillaume, y 0,5 se le abonará a Dolores.**


*'Escribe y pasa el móvil dedo del infinito':* ETH no se movió a través de una red tal cual; no era un correo electrónico enviado desde la computadora de Guillaume a la bandeja de entrada de MetaMask de Dolores, ni nada por el estilo. Guillaume envió una solicitud, **autenticada por sus [claves privadas a través de MetaMask](https://metamask.zendesk.com/hc/en-us/articles/4404722782107-User-guide-Secret-Recovery-Phrase-password-and-private-keys)**, a la red para que le hiciera un cargo en su cuenta y lo abonara en la de Dolores, y después de hacerse el proceso de verificación programado en los protocolos de la red, esto se hizo.


#### *Eso es todo lo que tiene una transacción: una solicitud al libro de contabilidad para que reasigne algo de una dirección a otra.*


 


**Cuando las cosas salen mal**
------------------------------


Las cosas pueden salir mal por varias razones. A menudo, son 'debido al software': en MetaMask se da un error o algo se ha configurado mal en cuanto a la red que está tratando de usar; hubo un error de conectividad.


Un **problema común es que el usuario, en un intento de pagar menos por su transacción, establece un límite de gas muy bajo**, y las condiciones de la red están tan congestionadas que no hay espacio en ningún bloque para una transacción tan "barata", a veces por un tiempo muy largo: al cabo del tiempo, esta transacción se convertirá en "inerte" y el usuario tendrá que cancelarla.


**Si ha enviado una transacción y no se ha finalizado**, su estado se mostrará como "pendiente" en MetaMask.


**Si envió una transacción, y falló, la causa más probable es la falta de gas**: "se le acabó el gas", para decirlo así; la transacción tenía un costo en gas que, al multiplicarse por el precio de gas, dio como resultado una cantidad total en la moneda nativa de la red que era mayor que lo que tenía en su billetera.



#### Información


Para más información sobre el cálculo del gas, consulte nuestra guía sobre [el gas aquí](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas).



Esto puede suceder por varias razones, pero una cosa a tener en cuenta es qué es la transacción que desea realizar. Acuñar a un NFT durante los tiempos de tráfico más alto en la red puede ser muy costoso en concepto de gas; si está probando una transacción nueva o experimental, puede que valga la pena probar una red de pruebas antes de pagar tarifas reales de la red en vivo.


 


**Solucionar el problema**
--------------------------


### **Factor clave #1: Local o difundida a la red**


En el transcurso del diagnóstico de su problema de transacción, especialmente cuando se trata de una transacción pendiente, tendrá que ver si la transacción sigue en su grupo de memoria local, o si ya llegó a la red y se encuentra allí atascada por cualquier razón. Si se encuentra solo en su grupo de memoria local, la solución podría ser tan simple como bloquear y desbloquear su billetera MetaMask (**asegúrese de conocer su contraseña y de que su Frase de Recuperación Secreta se haya respaldado antes de hacerlo**). Si ha llegado a la red, la solución podría ser más complicada.


Para más información sobre cómo solucionar estos problemas, consulte los enlaces a continuación.  
  



### **Factor clave #2: El nonce**


Esta palabra puede significar varias cosas diferentes. En este contexto, significa en términos generales "número de transacción", a partir de la primera transacción realizada por la dirección remitente. Por ejemplo, se pueden tener verdaderos problemas si se realizan dos transacciones diferentes desde diferentes instancias de MetaMask con la misma dirección de la billetera al mismo tiempo. **Las transacciones de su dirección deben estar en orden ascendente de acuerdo a su nonce.** Sin embargo, al igual que los nonces son capaces de causar una transacción atascada, pueden ser la clave para desatascar una transacción.


Para más información sobre esa técnica, [consulte aquí.](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction)


 


**Próximos Pasos**
------------------


### *Si tiene una transacción fallida o pendiente, consulte los siguientes recursos para ayuda.*


#### [Cómo enviar tokens desde su billetera MetaMask](https://metamask.zendesk.com/hc/en-us/articles/360015488931)


#### [Cómo acelerar o cancelar una transacción pendiente](https://metamask.zendesk.com/hc/en-us/articles/360015489251-How-to-Speed-Up-or-Cancel-a-Pending-Transaction)


#### [¿Por qué falló mi transacción con un error de "Gas insuficiente"?](https://metamask.zendesk.com/hc/en-us/articles/360038849792-Why-did-my-transaction-fail-with-an-Out-of-Gas-error-How-can-I-fix-it-)


#### [Soluciones para problemas de Uniswap](https://metamask.zendesk.com/hc/en-us/articles/360053394291-Uniswap-support-and-troubleshooting-tips)


#### [Guía Práctica: Gas](https://metamask.zendesk.com/hc/en-us/articles/4404600179227-User-Guide-Gas)


#### [¿Puedo revertir una transacción ya confirmada?](https://metamask.zendesk.com/hc/en-us/articles/360059957352-Can-I-reverse-an-already-confirmed-transaction-)


 


**Preguntas frecuentes**
------------------------


#### 
*P: Una cuenta en mi billetera tiene una transacción pendiente o en cola. ¿Puedo iniciar otra transacción desde una cuenta diferente dentro de la misma billetera?* R: Sí, se puede. El nonce se cuenta por cuenta, no por billetera.

