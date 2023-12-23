Cuando envía una transacción en Ethereum o en una red compatible, parte del gas que paga es una oferta a la red para que procese antes tu transacción: esta oferta se conoce como tarifa de prioridad. Aunque MetaMask le ayudará calculando una tarifa de gas total que probablemente haga que tu transacción sea recogida, es posible que tenga que esperar mucho tiempo si envía la transacción con un precio de gas bajo. Para consejos sobre qué precios de gas resultarán en que una transacción se finalice dentro de un tiempo razonable, consulte a fuentes como el [rastreador de gas de Etherscan](https://etherscan.io/gastracker), o un rastreador similar para la red que esté utilizando.


Además, a veces hay circunstancias en las que algo sale mal, y una transacción simplemente está atascada o pendiente por un tiempo muy largo.


No importa cómo llegue a este punto, hay varias maneras para abordarlo.


 


### Antes de realizar cualquier otra acción, el primer paso debe ser salir y cerrar el navegador por completo, volver a abrirlo y desbloquear MetaMask (en el móvil, basta con cerrar la aplicación y volverla a abrir). Si eso no resuelve el problema, continúe con lo siguiente:


 


**Agilizar una transacción**
----------------------------


![MetaMask agiliza la transacción](https://support.metamask.io/hc/article_attachments/12927043481371)


Pruebe una de las opciones a continuación:


* Espere hasta que la red esté dispuesta a procesar transacciones a este precio
* Si aún no lo ha hecho, haga clic en ese botón que dice **Acelerar**. Esto te permitirá volver a enviar la misma transacción pero con una tarifa de gas más elevada, lo que debería agilizar el procesamiento. Dado que este proceso reutiliza el mismo nonce que el original, no es necesario pagar dos veces por el gas.


Hay que tener en cuenta que **acelerar la transacción aumentará la cantidad que se gasta por la misma**.


 


**Cancelación de una transacción - Método 1: Cancelación dentro de la aplicación**
----------------------------------------------------------------------------------


Si aún no ha hecho esto, para cancelar la transacción, simplemente seleccione **Cancelar**, como en la captura de pantalla anterior. Tenga en cuenta, **una cancelación solo se puede *intentar* si la transacción aún está pendiente en la red.** Las transacciones que ya se han confirmado no se pueden revertir.


 


**Cancelación de una transacción - Método 2: Nonce personalizado**
------------------------------------------------------------------


Este proceso consiste en enviar una nueva transacción con el mismo nonce (un número de identificación para cada transacción, derivado de la expresión "número que solo se utiliza una vez"). La transacción no tiene que tener ningún valor; por ejemplo, se podría enviar 0 ETH. Lo que importa es que pague gas suficiente para que la red la priorice.


Cuando utilice este método, **deberá retroceder desde la transacción pendiente más antigua de la cola que desee cancelar**. Por ejemplo, no se puede intentar cancelar una transacción con un nonce de 10 antes de cancelar una de nonce 9.


*Las capturas de pantalla que aparecen a continuación se tomaron en momentos diferentes, por lo que las tarifas de gas que se muestran en ellas pueden variar, incluso de un paso a otro. ¡No deje que esto te desanime! Cuando hagas esto tú mismo, MetaMask se actualizará automáticamente en tiempo real, mostrando las tarifas del mercado.*




Extensión Móvil


1. En configuraciones avanzadas, active **Personalizar nonce de la transacción** y **Controles avanzados de gas.** Este último le permitirá manipular el gas que paga y asegurarse de que su transacción de cancelación se procese antes de la original que desea cancelar.



#### Aviso:


MetaMask Extension tiene actualmente una función experimental disponible llamada [Enhanced Gas Fee UI](https://metamask.io/1559/) (no confundir con [los controles avanzados de gas](https://support.metamask.io/hc/en-us/articles/360022895972)) Estos pasos se pueden realizar tanto si está activada esta opción como si no, pero tenga en cuenta que tendrán un aspecto diferente. Los siguientes pasos no utilizan Enhanced Gas UI. Ten en cuenta:



	* Si tiene activado Enhanced Gas UI, también deberá tener activado "Personalizar el nonce de transacción".
	* Si no tiene activada la interfaz Enhanced Gas UI, deberá tener activadas las opciones "Controles avanzados de gas" y "Personalizar el nonce de transacción".

![Configuración avanzada de MetaMask](https://support.metamask.io/hc/article_attachments/12927064113947)
2. **Envíe una transacción nueva**. En la transacción nueva, envíela **A** sí mismo, o sea a su dirección pública de MetaMask. **Llene el blanco de 'Nonce personalizado' con el mismo nonce que la transacción que aún está pendiente**:


![Metamask_custom_transaction_nonce_Extension.png](https://support.metamask.io/hc/article_attachments/12927064259483)
3. Ahora pulsa "Editar" junto a "Tarifa de gas" (si tienes activada la interfaz experimental [IU de gas avanzada](https://support.metamask.io/hc/en-us/articles/360022895972-Using-advanced-gas-controls#:~:text=%C2%A0-,Enhanced%20Gas%20UI,-Since%20the%20introduction), aparecerá como "Mercado"). Ahora verá las opciones a continuación:


![Extensión de los controles de gas avanzados de MetaMask](https://support.metamask.io/hc/article_attachments/12927065407515)


Para asegurarse de que su solicitud de cancelación se recoja como prioridad, y antes de la original, **tendrá que pagar a por más gas**. Siga estas instrucciones:


	* Configure el **límite de gas** a una cantidad *comparable o un poco más alto* que la transacción original.
	* Fije su **tarifa de prioridad máxima** a *al menos un 10% más* (en Gwei) que la tarifa de gas de la transacción original (pendiente) (por ejemplo, si esa transacción tuvo una tarifa de gas de 30 Gwei, fije la tarifa de prioridad máxima en la transacción de reemplazo o de cancelación a 33-35 Gwei).
	* Asegúrese de que su tarifa máxima sea al menos un 30% más alta que la tarifa máxima de la transacción que está reemplazando. Por ejemplo, si su tarifa anterior era de 150 Gwei, elija algo más cerca de 200 Gwei esta vez.Consulte un rastreador de gas como [el de Etherscan,](https://etherscan.io/gastracker) o [la estación de gas de ETH](https://ethgasstation.info/) para obtener orientación sobre las tarifas máximas recomendadas.




1. **En Configuración > Avanzada, activa "Personalizar el nonce de transacción".**
2. **Envía una nueva transacción.** En la transacción nueva, envíela A sí mismo, o sea a su dirección pública de MetaMask. **Rellene "Personalizar el nonce" con el mismo nonce que la transacción que aún está pendiente**.


Para encontrar la configuración personalizada de nonce en la aplicación, vaya a la pantalla de confirmación de la transacción que aparece después de haber ingresado la cantidad de tokens y el destinatario. Pulse "Editar" para cambiarlo:


![MetaMask personalizar nonce de transacción Móvil](https://support.metamask.io/hc/article_attachments/12927068442907)
3. Ahora tiene que asegurarse de que los ajustes de su gas están configurados para que se procese la transacción de reemplazo. En la pantalla de confirmación de la transacción, pulse el valor de gas que aparece resaltado:


![MetaMask controles de gas avanzados móvil](https://support.metamask.io/hc/article_attachments/12927041593755)


Ahora acceda a "Opciones avanzadas" desde el menú que se despliega.
4. Desde aquí, se puede ajustar con precisión el gas para asegurarse de que su transacción es recogida. Ahora verá una pantalla parecida a esta:


![MetaMask controles de gas avanzados móvil](https://support.metamask.io/hc/article_attachments/12927063201691)


Desde aquí, ajuste la configuración del gas. Siga estas instrucciones para garantizar que su transacción sea procesada:


	* Configure el **límite de gas** a una cantidad *comparable o un poco más alto* que la transacción original.
	* Fije su **tarifa de prioridad máxima** a *al menos un 10% más* (en Gwei) que la tarifa de gas de la transacción original (pendiente) (por ejemplo, si esa transacción tuvo una tarifa de gas de 30 Gwei, fije la tarifa de prioridad máxima en la transacción de reemplazo o de cancelación a 33-35 Gwei).
	* Asegúrese de que su **tarifa máxima** es *al menos un 30 % superior* a la tarifa máxima de la transacción que está reemplazando. Por ejemplo, si su tarifa anterior era de 150 Gwei, elija algo cercano a 200 Gwei en esta ocasión.Consulte un rastreador de gas como [Etherscan](https://etherscan.io/gastracker) o [ETH Gas Station](https://ethgasstation.info/) para obtener orientación sobre las tarifas máximas recomendadas.



