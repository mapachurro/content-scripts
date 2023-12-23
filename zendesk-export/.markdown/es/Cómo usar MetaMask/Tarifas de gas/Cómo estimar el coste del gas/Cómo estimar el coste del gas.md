### Averiguar el precio de gas


Si se conecta a la red principal de Ethereum, podrá consultar la [herramienta de gas de Etherscan](https://etherscan.io/gastracker) para estimar el precio de gas al día de hoy. Tenga en cuenta que el precio de gas fluctúa; consulte siempre a la estación de gas para ver los precios de gas actuales.


Para llevar a cabo una transacción en la red de Ethereum, habrá que gastar gas. Cuando uno envía tokens, interactúa con un contrato, envía ETH o hace cualquier otra cosa en la cadena de bloques, hay que pagar por aquella computación. Aquel pago se calcula en unidades de gas, y el gas siempre se paga en ETH.


Debe pagar por el cálculo, independientemente de si su transacción tiene éxito o no. Incluso si falla, los mineros o validadores deben finalizar y ejecutar su transacción, lo cual requiere poder computacional. Tiene que pagar para esa computación, al igual que pagaría para una transacción exitosa.


 


### Conseguir el límite de gas


Entonces, ya sabe cuánto cuesta cada unidad de gas, pero ¿cuántas unidades de gas necesitará gastar? Bueno, si se trata de una transacción simple (digamos, enviar ETH o un token tipo ERC-721 a otra dirección), debería gastar 21 000 unidades de gas. Si hace algo más complejo, una buena herramienta es un explorador de bloques, como [etherscan.io](https://etherscan.io/). Navegar al contrato con el cual desea interactuar, y comenzar a examinar las transacciones que se han hecho a través del contrato. Esto le dará una mejor idea de cuánto gas, de hecho, usaron al final otros usuarios.



#### Calculadora de gas


Existen algunas herramientas que te permiten calcular cuánto te va a costar la gasolina en dinero fiat antes de realizar una transacción. Un ejemplo es la [calculadora de tarifas de gas de Cryptoneur](https://www.cryptoneur.xyz/gas-fees-calculator), la cual le permite ingresar los detalles de su transacción y mostrar una estimación del costo del gas en su moneda local, tomando en cuenta la demanda actual de esa red (puede seleccionar entre la mayoría de las principales redes compatibles con EVM).



### 
Estructura general de tarifas de gas


A partir del [EIP-1559](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1559.md), la tarifa general que paga aquel que crea una transacción se calcula como: **( (tarifa base + tarifa de prioridad) x unidades de gas utilizadas)**.


Para más información, consulte [aquí](https://support.metamask.io/hc/en-us/articles/4404600179227).


 


**Tenga en cuenta que esto no es una tarifa que se recibe en MetaMask, así que no podemos reembolsarla.** Esta tarifa se paga a mineros o validadores para finalizar la transacción, validarla en un bloque y asegurar la cadena de bloques.

