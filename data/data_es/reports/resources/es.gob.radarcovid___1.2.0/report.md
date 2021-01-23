# Radar COVID
App version ``1.2.0``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="Radar COVID icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Radar COVID |
| **Unique identifier** | es.gob.radarcovid |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=es.gob.radarcovid](https://play.google.com/store/apps/details?id=es.gob.radarcovid) |
| **Summary**  | Radar COVID, app oficial de prevención del COVID-19 del Gobierno de España |
| **Privacy policy** | [https://radarcovid.covid19.gob.es/terms-of-service/privacy-policy.html](https://radarcovid.covid19.gob.es/terms-of-service/privacy-policy.html) |
| **Latest version** | 1.2.0 |
| **Last update** | 2020-12-17 18:27:09 |
| **Recent changes** | - Actualización versión DP-3T.<br>- Vista de Estadísticas Radar COVID.<br>- Vista de información del estado de la aplicación.<br>- Recordatorio de apertura de la aplicación.<br>- Contador confinamiento.<br>- Compartir enlace para facilitar descarga.<br>- Añadido idioma Francés.<br>- Introducción de código desde SMS.<br>- Mejoras de accesibilidad:<br>   Aumento de tamaño de texto y contraste.<br>   Cambio en el estilo de los enlaces.<br>   Etiquetado de elementos en pantalla.<br>   Incorporación de encabezados. |
| **Installs**  | 1.000.000+ |
| **Category** | Medicina |
| **First release** | 7 ago 2020 |
| **Size**  | 22M |
| **Supported Android version**  | 6.0 y versiones posteriores |

### Description
> Radar COVID es la aplicación diseñada y dirigida por la Secretaría de Estado de Digitalización e Inteligencia Artificial del Gobierno de España para ayudar a evitar la propagación del coronavirus (COVID-19). 
<br>Radar COVID te avisa de manera anónima del posible contacto que has podido tener en los últimos 14 días con una persona que haya resultado infectada utilizando la tecnología Bluetooth de bajo consumo.
<br>Radar COVID además permite:
<br>-	Comunicar de forma anónima tu diagnóstico positivo.
<br>-	Comunicar la exposición de forma anónima a las personas con las que has estado en contacto 
<br>Radar COVID garantiza la seguridad y privacidad y es 100% anónimo. Por ello no solicitamos ni tu nombre, ni tu teléfono, ni tu correo electrónico. 
<br>Esta aplicación usa ilustraciones de licencia gratuita y que pertenecen a www.freepik.es


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Ministerio de Asuntos Económicos y Transf. Digital |
| **Website**  | - |
| **Email** | soporte.radarcovid@economia.gob.es |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Ministerio+de+Asuntos+Econ%C3%B3micos+y+Transf.+Digital](https://play.google.com/store/apps/developer?id=Ministerio+de+Asuntos+Econ%C3%B3micos+y+Transf.+Digital) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Android10, version 10 (API level 29) |
| **Effective target Android version**  | Android10, version 10 (API level 29) |
| **Minimum supported Android version**  | Marshmallow, version 6.0 (API level 23) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>REQUEST_IGNORE_BATTERY_OPTIMIZATIONS** | Normal | Permission an application must hold in order to use Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | ietf.org | IETF Trust | :us: US | 1995-03-11 05:00:00 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Telephony services abuse**
> - This application makes phone calls<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Lcom/android/tools/r8/GeneratedOutlineSupport;->outline15(Ljava/lang/String;)Ljava/lang/StringBuilder;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The Radar COVID app has been installed by more than **1000000** times. At this time, **13257** rated the app and its average score is **3.0216258**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 5171

:star::star::star::star:: 1156

:star::star::star:: 1038

:star::star:: 573

:star:: 5319

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="es.gob.radarcovid 5 reviews"/>
</p>

> Buena<br> :date: __2021-01-23 11:58:44__

> Por favor que todo el mundo se descargue esta app, ayudaría mucho<br> :date: __2021-01-23 00:07:02__

> oculto<br> :date: __2021-01-22 23:39:40__

> Que pena que no se use casi nada....<br> :date: __2021-01-22 21:41:17__

> Bien<br> :date: __2021-01-22 19:39:26__

> Muy buena henora buena<br> :date: __2021-01-22 12:22:04__

> Way<br> :date: __2021-01-21 17:56:23__

> Los datos personales no están bien protegidos si usas esta aplicación.<br> :date: __2021-01-21 15:09:39__

> Estudie medicina en general comohe sije el colegio de medicos<br> :date: __2021-01-21 12:02:37__

> Fácil acceso e información muy clara, tanto de su utilidad como seguridad del anonimato en redes sociales<br> :date: __2021-01-21 11:17:32__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="es.gob.radarcovid 4 reviews"/>
</p>

> L Ññuiuuuuuyuuuuuuuu<br> :date: __2021-01-23 13:19:02__

> Rectificar es de sabios ....<br> :date: __2021-01-22 23:27:46__

> Funciona de verdad<br> :date: __2021-01-21 18:53:22__

> Acabo de instalarlo<br> :date: __2021-01-21 18:03:24__

> Magnífica<br> :date: __2021-01-21 12:45:04__

> Muy buena ap pero me gustaría que fuese anónimo para todos menos a los médicos por eso le doy 4 estrellas<br> :date: __2021-01-21 07:48:24__

> De momento estoy inactivos<br> :date: __2021-01-20 13:02:59__

> Ahora acabo de descargar esta aplicacion , supongo que funcciona , pero es muy temprano para dar una valoracion completa,!<br> :date: __2021-01-18 15:39:18__

> Supongo que funciona bien de momento no me ha alertado de ningún contacto pero tiene un pequeño fallo. Me dice que en modo ahorro no puede funcionar cada 2 por 3 y he comprobado lo del modo ahorro ya más de 10 veces viendo que no estaba puesto pero me sigue saltando la alerta<br> :date: __2021-01-17 01:20:34__

> Gracioso que haya países conectados a la aplicación pero ni uno fronterizo que tendrían que ser la prioridad a mi parecer. Marruecos no creo que fuera muy útil pero Portugal, Gibraltar, Andorra y Francia tendrían que estar si o si.<br> :date: __2021-01-15 09:42:06__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="es.gob.radarcovid 3 reviews"/>
</p>

> Me gasta la batería del teléfono<br> :date: __2021-01-22 22:03:22__

> Valor, ayuda, experiencia, Gente interés + ó -- juego por Poder Extra\*\*\*\*<br> :date: __2021-01-21 18:38:33__

> Esta bien pero si nosotros tenemos el covid 19 se pone alerta<br> :date: __2021-01-21 16:34:40__

> seria una APP si todo era l mundo fueta honesto 100%, o puenso q la administracion lo informase anonimamente , es decir, marcar en todo momento la ubicacion,(excepcionalmente con tema covid), ademad si no se hacen PCR masivas tampoco tiene utiludad, si yo lo tengo el covid y no lo se... es inutil sin saberlo ..<br> :date: __2021-01-20 23:22:44__

> Buena versión de plague.inc<br> :date: __2021-01-18 21:32:23__

> Acabo d descargarla<br> :date: __2021-01-17 14:00:47__

> Para impulsar su uso y sacar provecho a la app, estaría bien que añadieran la opción de indicar si el usuario se ha vacunado o no, distinguiendo entre primera y segunda dosis. Creo que es de gran utilidad para conocer la efectividad de la misma.<br> :date: __2021-01-16 18:51:02__

> nadie hace caso a las recomendaciones,hay transformar enOBLIGACIONES.<br> :date: __2021-01-16 13:49:58__

> Esta muy bien GRACIAS<br> :date: __2021-01-15 21:13:36__

> Nada mas que hay tres ventanas la de ajustes, la de info y la de informar casos del covid. No es completa.<br> :date: __2021-01-12 16:02:59__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="es.gob.radarcovid 2 reviews"/>
</p>

> No cumple su función. Las opiniones positivas son de gente que se ha equivocado de app y opinan sobre un juego. No avisa nunca. Te rodeas de positivos y a la app se la pela aún funcionando correctamente después de pelear con el Bluetooth y las opciones de energía. Porque es el SISTEMA el que no funciona. Cuánto ha costado esto y qué publicidad masiva se le ha dado para hacer el seguimiento eficaz? Porque lo he pagado yo entre otros... Entre esta castaña y las apps de Educación vamos mal, eh?<br> :date: __2021-01-23 00:32:56__

> Desde hace dos semanas da mensajes de no funcionar bien y consume más batería.<br> :date: __2021-01-21 19:30:02__

> 6 millones de descargas en 10 países? 350000 positivos? En serio? Esto es imposible que cumpla su función...y menos sabiendo,que lo sabéis,que muchos aunque tengan la aplicación y sean positivos no lo iban a notificar en la app,además como podéis leer en otros comentarios ni siquiera ha funcionado...la aguantaré un tiempo pero por favor que alguien me explique si esto realmente sirve de algo.<br> :date: __2021-01-21 10:09:19__

> En cuanto el teléfono está bajo de batería dice que la aplicación no funciona correctamente, debería funcionar incluso con la batería baja, espero no necesitarla<br> :date: __2021-01-18 11:19:36__

> La aplicación muy bien, pero si no dan el código que tienen que dar cuando das positivo, no sirve para nada. Tengo tres familiares con positivo y a ninguno les dieron el código.<br> :date: __2021-01-15 13:08:21__

> No sé actualiza a tiempo ...no merece la pena tenerla recibes información mejor por otros medios.<br> :date: __2021-01-14 15:52:42__

> Yo di positivo pero nadie me dio tal código por lo q no pude ingresarlo en la app. Siempre pone baja exposición supongo q ese será un motivo. Poco éxito me parece a mí<br> :date: __2021-01-14 09:55:19__

> Tendria que mejorar. Poner noticias de donde estes. Pero esta aplicación no te da mucha información. Tiene que entrar mas gente para que en teoria fuera eficaz.<br> :date: __2021-01-13 21:18:39__

> No se puede actualizar, y no cumple con las respectivas de una plicación de el gobierno de España. Se podría poner un nombre con un aviso de que todas las personas con las que has estado más de 15 minutos podrán verte. He puesto 2 estrellas porque no está a la altura.<br> :date: __2021-01-13 16:41:37__

> La desinstalé ya dos veces. La finalidad es fantástica, pero seguro que existen mentes más brillantes, técnicos y científicos de verdad, para mejorarla. Lo digo porque todo lo que gestiona ESTE Gobierno de España es ineficaz y chapucero. Gracias.<br> :date: __2021-01-13 09:19:55__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="es.gob.radarcovid 1 reviews"/>
</p>

> De qué sirve la aplicación, si cuando salud pública te comunica que eres positivo no te dan ningún código para comunicar tu positivo a la app??<br> :date: __2021-01-23 11:44:16__

> Otra estafa del gobierno para hacer rico a algún amiguete. Al dar positivo por una prueba realizada por la sanidad privada, el código que te Dan de la prueba no se puede poner, no sirve para nada y por tanto no puedo notificar que soy positivo. Lo siento por mis conciudadanos que aún se creen que el gobierno está a nuestro servicio. Deberíamos de hacerlo público en todos los medios.<br> :date: __2021-01-23 10:40:23__

> Se ha demostrado su ineficacia<br> :date: __2021-01-23 08:38:54__

> Caca<br> :date: __2021-01-23 08:19:45__

> Sería útil si la gente se implicase más, llevo tiempo usándola y no ha notificado ni una sola alerta, cuando personas del entorno han dado positivo. Si no eres responsable, este sistema no sirve de nada.<br> :date: __2021-01-23 07:42:15__

> De que sirve la aplicación si en el hospital junto al positivo no te dan el código entero que debes introducir a los positivos que he conocido incluso yo hemos intentado meter el código que pide pero le faltan números y no te deja introducirlo.. si los centro médicos donde se hacen las pruebas no colaboran para usar este tipo de medida de que sirve.. una vergüenza todo.. nadie hace nada bien que país..<br> :date: __2021-01-22 23:51:45__

> No me sirve ni para ver a la gente con covid porque mi abuelo lo tiene y no me dice na q estoy a lado suyaaa!!!<br> :date: __2021-01-22 23:25:38__

> Esta es la peor aplicación del mundo, lo mejor que puedes hacer es quedarte en tu casa y no fiarte de toda esta patraña de mentiras del gobierno. No comunica nada y eso que he estado con una persona contagiada, la cual tenía la aplicación y lo ha comunicado, pero al parecer esto solo sirve para que te controlen. GRACIAS PEDRO SANCHEZ Y PABLO IGLESIAS, por llevar este pais a la RUINA, y sobre todo gracias por tener que pagar durante toda mi vida un IRPF de más del 20% cuando tengo 25 años.<br> :date: __2021-01-22 22:55:12__

> Buena app para acondicionarnos de un control masivo a la población no muy lejano, hijos de la grandisima.<br> :date: __2021-01-22 22:28:20__

> Para decir que eres positivo tienes que introducir un Código, el cual cuando te llaman para decirte que eres positivo, no te lo facilitan sino lo preguntas (imagino). Por lo que he tenido contacto con positivos y por no poder poner el Código (mis contactos), no me ha valido para nada la aplicación<br> :date: __2021-01-22 20:50:40__


