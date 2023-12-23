
#### ¿Eres nuevo en criptomonedas y web3?


Visita [MetaMask Learn](https://learn.metamask.io/) para obtener una experiencia de aprendizaje directa diseñada específicamente para los recién llegados a web3. Es totalmente gratis y está disponible en varios idiomas e incluye herramientas útiles, como simulaciones, que te ayudarán a familiarizarte con MetaMask.



### En este artículo:


* [¿Qué diferencia hay entre la seguridad de MetaMask y la de las cuentas web tradicionales?](#h_01FYVAXCSH95CQ08Q0P2VJA5HV)
* [¿Qué es una frase de Recuperación Secreta?](#h_01FYVAXJQT914HCHEYFPNMEJEA)
* [Qué hacer y qué no hacer con una frase de Recuperación Secreta](#h_01FYVAXSE5C9E4YBCSWT2F2RBQ)
* [Preguntas frecuentes sobre Frase de Recuperación Secreta](#h_01FYVAXZYWJENFWG9K9CJTQFK7)
* [Contraseñas y MetaMask](#h_01FYVAY5K22PX6926537V8B4SX)
* [Preguntas frecuentes sobre claves privadas](#h_01FYVAYH3ZZ8VW8BPDDADWRC8E)




**MetaMask: un modelo diferente de seguridad**de**cuentas**
------------------------------------------------------------


[La tecnología de cadena de bloques pública](https://metamask.zendesk.com/hc/en-us/articles/360015489611) utiliza herramientas muy diferentes para proteger los datos de los usuarios, en comparación con las tecnologías en línea tradicionales. La mayoría de nosotros estamos acostumbrados a crear una cuenta en una aplicación o un servicio y poder, por ejemplo, escribir al servicio de asistencia para restablecer nuestra contraseña o el nombre de usuario. Estamos acostumbrados a que la aplicación guarde nuestros datos, suponemos que en algún tipo de computadora que pertenece a la empresa.


Pues bien... MetaMask no funciona así. MetaMask tiene tres tipos diferentes de **secretos** que se utilizan de diferentes maneras para mantener tu billetera y tus cuentas de forma privada y segura: la Frase de Recuperación Secreta, la contraseña, y las claves privadas. Te guiaremos a través de estos secretos de uno en uno.


 


**Frases de Recuperación Secreta**
----------------------------------


Una de las tecnologías clave (verás lo que hice allí) que sustenta a MetaMask, y a la mayoría de las herramientas relacionadas con las cuentas de los usuarios en el ámbito de las criptomonedas, es la *frase semilla*, o como se la denomina en MetaMask, la *Frase de Recuperación Secreta*.


#### **Todas las cuentas se derivan matemáticamente de la Frase de Recuperación Secreta. Puedes visualizar la Frase de Recuperación Secreta como un llavero que alberga todas las claves privadas que necesitas: y cada una de esas claves controla una cuenta.**


Ahora, si buscas una explicación más técnica Las frases semilla, tal y como las conocemos hoy en día, fueron codificadas para su uso en Bitcoin, de acuerdo con un estándar conocido como Propuesta de Mejora de Bitcoin 39, o [BIP-39](https://en.bitcoin.it/wiki/BIP_0039) En términos sencillos, se seleccionan una serie de palabras con un alto nivel de aleatoriedad a partir de una lista específica [de palabras](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt) En MetaMask y en otras muchas tecnologías compatibles con Ethereum, hay 12 palabras en una frase semilla. Algunas semillas antiguas generadas por el navegador Brave, y algunas carteras de hardware, utilizan frases de 24 palabras.


Estas palabras corresponden cada una a una serie de números y, colocadas en **un orden determinado**, representan una forma mucho más fácil de recordar un número muy, muy largo. Ese número se emplea entonces para generar *de forma determinista* tus cuentas, y es posible que escuches a personas hablar de billeteras deterministas. En informática, se utiliza el término determinista para describir un proceso (normalmente un algoritmo de algún tipo) que *siempre* generará el mismo resultado. En otras palabras, **la Frase de Recuperación Secreta siempre generará la misma serie de cuentas que están asociadas a ella**.


 


### Hay que tener en cuenta una serie de características importantes:


* La **Frase de Recuperación Secreta es el secreto que controla la billetera** Si alguien tiene este secreto, tiene acceso completo a la billetera. **MetaMask no guarda tu frase de recuperación secreta:** **[tú eres el guardián de tu billetera.](https://metamask.zendesk.com/hc/en-us/articles/360059952212)** Los representantes de MetaMask **nunca** te pedirán tu Frase de Recuperación Secreta, ni siquiera en una situación de atención al cliente. Si alguien te la pide, probablemente esté intentando estafarte o robarte tus fondos.
* Tu FRS se **utiliza en el lugar para obtener claves privadas**, una para cada cuenta o dirección. Las cuentas se guardan en la cadena de bloques y las claves privadas las desbloquean.
* **Si desinstalas la aplicación** o la extensión, la versión local de los datos desaparece (con la excepción de la [bóveda](https://metamask.zendesk.com/hc/en-us/articles/360018766351)), sin embargo, cualquier transacción que hayas realizado con esa versión local de MetaMask quedará registrada en la cadena de bloques. Por lo tanto, las transacciones deberían reflejarse tanto en una cadena de [bloques](https://metamask.zendesk.com/hc/en-us/articles/360057536611), como también en otra instancia de MetaMask, siempre y cuando restaures [la cuenta utilizando la misma Frase de Recuperación Secreta](https://metamask.zendesk.com/hc/en-us/articles/360015289612) (**con las palabras en el mismo orden**). Esto significa que mientras tengas tu Frase de Recuperación Secreta, siempre podrás desinstalar MetaMask y restaurar tu billetera.
* **Dentro de tu billetera, puedes tener un gran número de cuentas separadas.** Si MetaMask crea o restaura tu billetera a partir de la Frase Secreta de Recuperación, generará solo la primera cuenta. Sin embargo, cualquier [cuenta adicional que hayas creado puede volver a crearse](https://metamask.zendesk.com/hc/en-us/articles/360015489271) en una instancia futura de MetaMask. **Como la billetera es *determinista*, siempre volverá a crear las mismas cuentas, en el mismo orden. Para más información sobre este tema, vea las preguntas frecuentes más abajo.** Ten en cuenta, sin embargo, que las cuentas adicionales (más allá de la primera, denominada automáticamente "Cuenta 1") ***no*** se volverán a añadir a tu cuenta automáticamente en cualquier circunstancia. Si desea más información, vea nuestra explicación [aquí](https://metamask.zendesk.com/hc/en-us/articles/360015489271-How-to-add-missing-accounts-after-restoring-with-Secret-Recovery-Phrase#:~:text=If%20you%20have,automatically%20re%2Dadded.).
* **Es posible [importar cuentas](https://metamask.zendesk.com/hc/en-us/articles/360015489331) de otras tecnologías compatibles con Ethereum a una billetera MetaMask.** Para esto, se utiliza la *clave privada* de esa cuenta específica. Sin embargo, **MetaMask no restaurará automáticamente esta cuenta en otra instancia; tendrás que volver a añadirla de forma manual**. Si has importado cuentas de forma manual, **toma nota de las claves privadas, de la misma forma que hiciste con la frase semilla**, para volver a importarlas en el futuro.


 


**Frase de Recuperación Secreta de MetaMask: Qué hacer y qué no hacer**
-----------------------------------------------------------------------




**Que hacer:**

* **Anota tu Frase de Recuperación Secreta en algún lugar seguro**. No podemos decirte con exactitud dónde, ya que eso depende de tus circunstancias.
	+ La importancia de escribir a mano tu Frase de Recuperación Secreta es que no puede ser robada en línea. Por ejemplo, si la guardas en un archivo de una carpeta de almacenamiento en la nube conectada a Internet, es posible que te la roben.
* Revisa la ortografía y comprueba que has escrito todas las palabras en el mismo orden.
* Si necesitas ayuda, contacta con los [canales oficiales](https://metamask.zendesk.com/hc/en-us/articles/360058230211) de soporte de MetaMask.





**Que no hacer:**

* Guardarla en un lugar fácil de descubrir o hackear; por ejemplo, en un documento guardado en la nube o en un correo electrónico titulado "Frase semilla"; o en un post-it pegado en tu computadora.
* Facilitar tu frase semilla a cualquier persona, incluso si dicen que son del Soporte de MetaMask.
* Cambia el orden de las palabras.





 


**Frases de Recuperación Secretas: preguntas y respuestas frecuentes**
----------------------------------------------------------------------


### ¡Mi frase semilla restauró una cuenta diferente!


Consulta el artículo de la base de conocimientos sobre este tema [aquí](https://metamask.zendesk.com/hc/en-us/articles/360058120992) Además, consulta el hilo de la Comunidad [aquí](https://community.metamask.io/t/restored-metamask-no-coins-are-showing/878/107?u=jacob.cantele) para obtener más contexto e información sobre el tema.


### Otras preguntas frecuentes sobre frases de recuperación secretas:


[¿Cómo descubrir su frase de recuperación secreta?](https://metamask.zendesk.com/hc/en-us/articles/360015290032)


[¿Cómo recuperar tu Frase de Recuperación Secreta?](https://metamask.zendesk.com/hc/en-us/articles/360018766351)


[Importar una frase semilla de otro software de billetera: ruta de derivación](https://metamask.zendesk.com/hc/en-us/articles/360060331752)


[Guía de migración de billeteras](https://metamask.zendesk.com/hc/en-us/articles/4867408571803)


[¿Cómo importar una cuenta?](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[¿Cómo comprobar la actividad de mi billetera en el explorador de cadena de bloques?](https://metamask.zendesk.com/hc/en-us/articles/360057536611)


[¿Qué es una Frase de Recuperación Secreta y cómo puedo mantener segura mi billetera?](https://metamask.zendesk.com/hc/en-us/articles/360060826432)


 


**Contraseñas y MetaMask**
--------------------------


MetaMask utiliza contraseñas con un único propósito: proteger la propia aplicación; en otras palabras, abrir la aplicación, bien sea la aplicación móvil o la extensión del navegador. Una vez que hayas restaurado o creado la billetera a partir de la Frase de Recuperación Secreta, no la necesitarás regularmente (**aunque deberás mantener una copia de respaldo y en un lugar seguro**), y deberás usar tu contraseña (o más comúnmente en móviles, mediante autenticación biométrica como el reconocimiento facial o la huella dactilar) para desbloquear la aplicación. Para más detalles, vea nuestro artículo [aquí](https://metamask.zendesk.com/hc/en-us/articles/4405451730331).


 


**Claves privadas**
-------------------


Aunque una Frase de Recuperación Secreta se utiliza para crear y restaurar toda la billetera MetaMask, incluyendo todas las cuentas en esa billetera, cada cuenta tiene su propia *clave privada*. Esta clave se puede utilizar para importar esa cuenta, y solo esa cuenta, a una billetera diferente. De igual manera, es posible importar cuentas individuales de otras tecnologías de criptomonedas a la billetera de MetaMask.


### Preguntas frecuentes sobre claves privadas:


[¿Qué son las cuentas importadas?](https://metamask.zendesk.com/hc/en-us/articles/360015289932)


[¿Cómo importar una cuenta?](https://metamask.zendesk.com/hc/en-us/articles/360015489331)


[¿Cómo exportar la clave privada de una cuenta?](https://metamask.zendesk.com/hc/en-us/articles/360015289632)


[¿Puedo importar una cuenta de Coinbase a mi billetera MetaMask?](https://metamask.zendesk.com/hc/en-us/articles/360058485292)

