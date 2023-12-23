Cuando un sitio web solicita que agregue una red personalizada a MetaMask, se le presenta la información que MetaMask utilizará para interactuar con aquella red. En MetaMask se realizará una validación básica de esta información, y le avisará si algo parece mal o fuera de lo normal. En MetaMask también se evitará que la misma red se agregue más de una vez. Aunque **MetaMask no verifica las redes personalizadas**, incluso si la validación de MetaMask es correcta, la red podría ser maliciosa o tergiversada por el sitio web que la solicitó.


**Si desea obtener más información y una introducción sobre las redes personalizadas, consulte nuestra Guía del Usuario [aquí](https://support.metamask.io/hc/en-us/articles/4404424659995).**


Al igual que es su responsabilidad verificar las direcciones de Ethereum con las que transacciona, también es su responsabilidad verificar toda red personalizada que agregue a MetaMask. En este artículo, compartiremos algunos consejos sobre cómo hacerlo.


Cuando un sitio web hace una solicitud de agregar una red personalizada, en MetaMask se muestra la siguiente confirmación:


![custom-network.png](https://support.metamask.io/hc/article_attachments/360087917091/custom-network.png)


 


Esta confirmación muestra **la información de la red que el sitio web proporcionó**. *No hay garantía de que esta información sea correcta*. Por lo tanto, debe fiarse de la información en el mismo grado en que confía en el sitio web.


Si hace clic en "Ver todos los detalles" en la confirmación, se puede ver toda la información de la red proporcionada por el sitio web, lo cual incluye:


* **Nombre de la red**: El nombre que en MetaMask se asociará con la red.
* **URL de la red:** La URL que en MetaMask se utilizará para acceder a la red.
* **ID de cadena:** La ID de cadena que en MetaMask se utilizará para firmar transacciones para la red.
* **Símbolo de divisas:** El símbolo de la moneda que en MetaMask se utilizará para la moneda nativa de la red.
	+ Por ejemplo, para la red principal de Ethereum, el símbolo de la moneda es de ETH, y para la cadena de Gnosis, el símbolo es de xDAI (se mantiene aún después de su fusión).
* **Bloquear la URL del Explorador (opcional):** La URL a la que MetaMask lo dirigirá para inspeccionar sus cuentas, transacciones, etc. Similar a [etherscan.io](https://etherscan.io) pero para esa red específica.


Si por alguna razón no está seguro de la exactitud de la información de la red, le recomendamos que tome los siguientes pasos para verificarla:


* Visite [Chainlist](https://chainlist.wtf/) y busque el ID de la cadena proporcionada y/o el nombre de la red. Si MetaMask le indica que determinada información no coincide, debería poder identificar el problema en Chainlist. Si la red personalizada no figura en ninguna lista de Chainlist, o bien se creó hace muy poco tiempo, o posiblemente es de calidad cuestionable.
* Busque el nombre de la red por Google, y trate de responder a las siguientes preguntas. Cuanto más pueda responder con un "sí", más razones tendrá para creer que la red es legítima. Tenga en cuenta que hay muchas estafas y canales de redes sociales falsos, especialmente en Telegram.
+ ¿Se tiene para la red un sitio web? Si es así, ¿parece legítimo? ¿Ahí se indican los detalles de la red?
+ ¿Se tiene para la red una cuenta de Twitter oficial o de otras redes sociales? ¿Tienen muchos seguidores? ¿Se parecen de confianza? ¿Qué dicen las personas sobre la red?
+ ¿Se puede identificar a cualquiera de las personas que mantienen la red? ¿Tienen visibilidad en las redes sociales? ¿Tienen muchos seguidores?
+ ¿Hay artículos de prensa sobre la red?


Para la mayoría de las redes, debería ser bastante obvio si son legítimos o no, y si en el sitio web se está proporcionando información precisa o no. Si aún no está seguro después de completar estos pasos, debe rechazar la solicitud de agregar la red, hacer más investigaciones y quizás vuelva a intentarlo más tarde.

