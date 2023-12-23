
#### Aviso:


Ninguna cuenta **importada** **se** volverá a agregar cuando restaure su billetera usando su Frase de Recuperación Secreta. [Necesitan ser agregadas de nuevo de forma manual](https://support.metamask.io/hc/en-us/articles/360015489331) de la misma manera que los importaste en un principio.



**¡NO COMPARTA su Frase de Recuperación Secreta con nadie! Estas palabras se pueden usar para robarle todas sus cuentas. No se puede editar ni cambiar su Frase de Recuperación Secreta.**


 


Cuando restaure [una billetera](https://support.metamask.io/hc/en-us/articles/360015289612-How-to-restore-your-MetaMask-account-from-Seed-Phrase-Secret-Recovery-Phrase) usando tu Frase de Recuperación Secreta, MetaMask reincorporará de forma automática cualquier cuenta adicional que haya [creado](https://support.metamask.io/hc/en-us/articles/360015289452) anteriormente, pero solo bajo ciertas condiciones.


MetaMask intentará agregar sus cuentas adicionales siempre que sea posible (asumiendo que no estaban [importadas](https://support.metamask.io/hc/en-us/articles/360015289932)) comprobando sus cuentas anteriores en orden ascendente (es decir, Cuenta 2, luego Cuenta 3, etc.). **Las cuentas se agregarán de forma automática si tienen un saldo de ETH distinto de cero**. Sin embargo, este proceso se detiene cuando MetaMask encuentra una cuenta con 0 ETH, por lo que la primera cuenta con 0 ETH (y cualquiera posterior a esta) *no* se agregará.


Tenga en cuenta que **este proceso solo verifica los saldos de ETH en la red principal de Ethereum**, por lo que otros tokens o tokens en otras redes no harán que su cuenta se vuelva a agregar automáticamente.


**Si no se vuelven agregar automáticamente, tendrá que volver a hacerlo "[creando](https://support.metamask.io/hc/en-us/articles/360015289452)" una cuenta**. Por ejemplo, si tiene algunos tokens en la Cuenta 4, pero la Cuenta 4 no se añade automáticamente porque aquellos tokens no sean ETH en la red principal, lo únicio que tendrá que hacer es agregar sus cuentas manualmente (utilizando los siguientes pasos) hasta que llegue a la Cuenta 4. Su Cuenta 4 *antes* de la recuperación corresponde a la Cuenta 4 *después* de la restauración, independientemente de si le hubiera aplicado un nombre personalizado previamente.


Si necesita utilizar el botón "crear" para volver a agregar cuentas, no se preocupe porque la dirección de la cuenta sea diferente. Las direcciones se derivan criptográficamente de *forma determinista* a partir de su clave privada, lo que significa que siempre serán las mismas. Y como una cuenta de Ethereum, una vez creada, tiene vigencia permanente, puedes retomarla donde la dejaste.


Siga los pasos a continuación sobre cómo recuperar sus otras cuentas en el orden en que se crearon originalmente:




Extensión Móvil


1. Haga clic en el icono personalizado en la esquina superior derecha del menú desplegable en MetaMask.
2. Haga clic en "Crear una cuenta" para recuperar sus cuentas de MetaMask en el orden en que se crearon.
3. Si previamente se les puso un nombre personalizado a las cuentas, se les puede nombrar nuevamente en el siguiente paso, antes de hacer clic en "**Crear**"


![How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase.gif](https://support.metamask.io/hc/article_attachments/9026739981083/How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase.gif)




1. Pulse el icono de tres barras laterales en la parte superior izquierda de la pantalla para que salte el menú. A partir de aquí, pulse en la flecha desplegable junto al nombre de su cuenta:
2. Pulse 'Crear una cuenta nueva':


![How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase_Mobile.gif](https://support.metamask.io/hc/article_attachments/9027058464027/How_to_add_missing_accounts_after_restoring_with_Secret_Recovery_Phrase_Mobile.gif)




Si aún no se ven las direcciones que buscaba, probablemente se crearon a partir de una Frase de Recuperación Secreta diferente, o tenía una cuenta importada a través de una clave privada o un archivo JSON que aún le hace falta importar. Consulte [este artículo sobre cómo importar una cuenta](https://support.metamask.io/hc/en-us/articles/360015489331-Importing-an-Account).

