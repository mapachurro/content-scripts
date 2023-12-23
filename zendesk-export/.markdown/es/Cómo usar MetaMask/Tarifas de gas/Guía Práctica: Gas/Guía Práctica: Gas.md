
#### ¿Eres nuevo en criptomonedas y web3?


Visite [MetaMask Learn](https://learn.metamask.io/) para obtener una experiencia de aprendizaje directa diseñada específicamente para los recién llegados a web3. Es totalmente gratis y está disponible en varios idiomas e incluye herramientas útiles, como simulaciones, que le ayudarán a familiarizarte con MetaMask.



El gas es la unidad de medida para la cantidad de trabajo computacional que se requiere para procesar transacciones y contratos inteligentes. Lo que es esencialmente una tarifa de transacción, el término se origina en Ethereum, en cuyo contexto se refiere a la computación realizada en la Máquina Virtual de Ethereum (EVM). Desde que se fundó Ethereum, han surgido numerosas empresas compatibles con EVM (¡y no compatibles con EVM!) y han adoptado modelos similares. 


El término se asemeja al gas que alimenta el motor de un vehículo: representa un gasto de funcionamiento fluctuante y, en ocasiones, caro. Los contratos inteligentes más complejos requieren más gas para alimentar su cálculo, al igual que un coche más grande y poderoso usa más gas para funcionar.


El método para calcular las tarifas de gas varía en función de la red. Por ejemplo, calcular el gas en Ethereum solía ser muy complicado, pero se simplificó considerablemente con la implementación del Protocolo de Mejora de Ethereum **(EIP) 1559** en agosto de 2021 (también conocido como la Actualización de Londres). Básicamente, pagas una **tarifa base** por cada unidad de gas, que se ***quema*** (leer: se elimina y desaparece) al completar con éxito la transacción. Además de la tarifa base, se agrega una **tarifa de prioridad**, de nuevo por cada unidad de gas, cuyo valor depende de la rapidez con que se desee que la transacción se lleve a cabo.


A lo largo de la amplia gama de redes compatibles con EVM disponibles, gas, o alternativas de funcionamiento similar, se han convertido esencialmente en el método estándar para calcular los costos de una transacción. Las tarifas se pagan en el token nativo de la red: por ejemplo, toda transacción en Ethereum requiere ETH; usar la red BSC requiere BNB; usar Polygon requiere MATIC. Algunas redes han adoptado el modelo de Ethereum EIP-1559 globalmente, como Polygon, mientras que otras han hecho ajustes, como Avalanche, para su cadena C (que [quema tanto la tarifa base como la tarifa de prioridad](https://docs.avax.network/learn/platform-overview/transaction-fees/#c-chain-fees), en lugar de solo la primera).


Si desea leer un análisis más profundo de cómo funciona el gas en Ethereum, consulta [aquí](https://ethereum.org/en/developers/docs/gas/).


 


A continuación se presentan algunos **detalles esenciales para saber tratar con el gas** **en MetaMask**:


#### **El límite de gas (unidades de gas utilizadas)**


El *límite de gas* es el **número máximo de unidades de gas para las cuales está dispuesto a pagar** para llevar a cabo una transacción o una operación de EVM. Diferentes operaciones exigen diferentes cantidades de unidades de gas. Una transacción normal enviando ETH o un token normalmente cuesta **21 000** gas, mientras que la aprobación de un token ERC-20 requiere 45 000. Muchas redes, como Harmony, la cual es una cadena de bloques compatible con la EVM, utilizan un modelo idéntico en el que las transacciones estándar también cuestan 21 000 gas.



#### ¿Necesito corregir el límite de gas?


¡No! MetaMask ajusta automáticamente su límite de gas dependiendo de la transacción que esté intentando ejecutar. En la gran mayoría de los casos, esto será suficiente para completar tu transacción. Si desea comprobarlo o editarlo, compruebe que tiene activados [los controles de gas avanzados](https://metamask.zendesk.com/hc/en-us/articles/360022895972) (o que está utilizando la interfaz de usuario de gas mejorada experimental) y pulse "Editar" en la pantalla de confirmación de la transacción.



#### **La tarifa base**


Cada cadena de la red Ethereum tiene una tarifa base determinada por la demanda de la red: la tarifa base depende del tamaño de la cadena anterior en comparación con un tamaño de la cadena objetivo (donde el tamaño se refiere a la cantidad total de gas utilizado para todas las transacciones que incluye la cadena). Si el tamaño de la cadena anterior supera el objetivo, la comisión base de la siguiente cadena aumenta un 12,5 %, lo que le deja a usted, el usuario (o a su billetera), con la absoluta certeza de cuál será la comisión base de la siguiente cadena. La tarifa total por gas debe cumplir este precio como mínimo para que se considere la posibilidad de incluirlo en la cadena. 


#### **La tarifa prioritaria**


La *tarifa prioritaria*, también llamada "propina del minero", incentiva al minero a dar prioridad a tu transacción.


Por supuesto, el hecho de que esto vaya realmente a un minero depende del [mecanismo de consenso](https://metamask.zendesk.com/hc/en-us/articles/360015489611-Learn-the-basics-of-blockchains-and-Ethereum-miners-and-validators-gas-cryptocurrencies-and-NFTs-block-explorer-networks-etc-) que utilice: La red principal de Ethereum se convirtió en la red Prueba de participación tras la fusión de septiembre de 2022, por lo que la tarifa prioritaria va a los validadores en lugar de a los mineros.


#### **La tarifa máxima**


La tarifa máxima es la cantidad total y entera pagada por su transacción. Se calcula según: **(****tarifa base + tarifa de prioridad) x unidades gas utilizadas.** En MetaMask inicialmente se establece esta cantidad en función de la historia del bloque anterior. Sin embargo, los usuarios pueden editar esta cantidad a través de ajustes personalizados (consulte a continuación). La diferencia entre la tarifa máxima por gas y la diferencia entre (tarifa base + tarifa prioritaria máxima por gas) se "reembolsa" al usuario.


 


### **Conceptos adicionales**


#### **Gwei**


Gwei es una unidad de Ether, la denominación más pequeña, que significa [gigawei](https://ethgasstation.info/blog/gwei/) (o 1 000 000 000). [Gwei](https://www.investopedia.com/terms/g/gwei-ethereum.asp) se usa para las tarifas de gas, o más bien para pagos realizados por los usuarios para compensar la energía de computación necesaria para procesar y validar transacciones en la cadena de bloques de Ethereum.


Otras redes también tienden a calcular los precios utilizando gwei, por ejemplo, Fantom, Harmony y Avalanche.


#### **Recotización**


La recotización es la diferencia esperada, como porcentaje, entre un precio cotizado y un precio ejecutado.


#### **Tarifa de gas**


*La tarifa* de gas se refiere a la tarifa de la transacción en la cadena de bloques de Ethereum. Es lo que los usuarios pagan para que su transacción se valide, o se complete.


#### **Tarifa base**


Generado por el protocolo. Representa el multiplicador mínimo de "gasUsed" que se requiere para que una transacción se incluya en la cadena (es decir, para que se complete una transacción). Esta es la parte de la tarifa de la transacción que se quema.


 


### **Controles de gas avanzados**


Si desea entrar en los detalles más finos del control de gas (esto puede ser útil si se está probando una dapp, por ejemplo), ¡en MetaMask se puede hacer eso! Consulte el artículo completo [aquí](https://metamask.zendesk.com/hc/en-us/articles/360022895972).


 


### **Preguntas frecuentes**


[¿Por qué pagué tarifas de gas por una transacción fallida?](https://metamask.zendesk.com/hc/en-us/articles/360045439051)


[¿Es posible reembolsar mis tarifas de gas?](https://metamask.zendesk.com/hc/en-us/articles/360058370012)


[¿Cómo se acelera o cancela una transacción pendiente?](https://metamask.zendesk.com/hc/en-us/articles/360015489251)


[Cómo estimar la tarifa de gas](https://metamask.zendesk.com/hc/en-us/articles/360059562111)


[¿Por qué son tan altas las tarifas de gas?](https://metamask.zendesk.com/hc/en-us/articles/360058751211-Why-my-gas-fees-are-so-high-)


[Error: [ethjs-query] while formatting outputs from RPC (error por transacción tasada por debajo de su precio)](https://metamask.zendesk.com/hc/en-us/articles/4402538041869)


[Cómo arreglar el error de "fondos insuficientes" o el botón de confirmación se queda en gris](https://metamask.zendesk.com/hc/en-us/articles/360044703372)


 


 

