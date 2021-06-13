# Radar COVID
App version ``1.3.0``

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
| **Latest version** | 1.3.0 |
| **Last update** | 2021-02-17 13:20:51 |
| **Recent changes** | - Modificaciones en política de privacidad.<br>- Reporte de métrica anónima para medir eficiencia de la aplicación.<br>- Se añade idioma rumano.<br>- Corrección de errores.<br>- Mejoras de accesibilidad:<br>	--  Corregido encabezado de “Cambio de estado” en el pop up de 14 días que el lector de pantalla no leía.<br>	-- Incorporación de iconos de cierre en los ventanas emergentes. |
| **Installs**  | 5.000.000+ |
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

The Radar COVID app has been installed by more than **5000000** times. At this time, **17370** rated the app and its average score is **2.716753**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 5520

:star::star::star::star:: 1620

:star::star::star:: 1050

:star::star:: 780

:star:: 8400

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="es.gob.radarcovid 5 reviews"/>
</p>

> Está bien de pende pero aceptable<br> :date: __2021-06-11 09:55:04__

> No me gusta el covid<br> :date: __2021-06-10 19:18:28__

> Muy buena<br> :date: __2021-06-09 12:58:07__

> X m.c u 900i £ mj<br> :date: __2021-06-08 22:00:15__

> Maximo<br> :date: __2021-06-07 08:14:32__

> Es una aplicación muy buena (te informa de todo y es eficaz en la lucha contra el virus)q…La información que viene en la aplicación es excelente y da todo tipo de consejos avalados por la Comunidad Científica (es como si te acompañará un médico o enfermera las 24h del día). Si te surge cualquier pregunta siempre tienes los teléfonos del SERGAS a tú disposición. A pesar de que digan que puede no ser adecuada para mí dispositivo yo me quedé con una impresión tan buena que la he vuelto a instalar.<br> :date: __2021-06-03 23:41:09__

> HTC TRABAJO de recibidogracias tt<br> :date: __2021-06-03 19:03:49__

> Excelente App para avisarte cuando el Bluetooth de tu celular está apagado, le doy 5 estrellas porque no hay más y además soy fun de la Mahou 5 estrellas. Desde que la instalé no puedo vivir sin ella.<br> :date: __2021-06-03 11:32:29__

> El coronavirus<br> :date: __2021-05-29 00:09:41__

> ¡¡¡¡Muy buena la app!!!!<br> :date: __2021-05-26 13:34:54__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="es.gob.radarcovid 4 reviews"/>
</p>

> En resumen: Estaria bien que se pudiese jugar con amigos en batallas multijador así más competividad. El modo historia de lo mejor bastante entretenido y con muchos momentos épicos que le dan el toque. Y molaria que metiesen eventos como el sida, ébola, covid1234 nueva plaga, etc<br> :date: __2021-06-04 22:57:48__

> Pocaexpefiencia<br> :date: __2021-05-25 22:55:36__

> Es un adelanto estar adelantado k sin solicitarlo ya hay app k detecte problemas d x igual indole pal resto d la humanidad k da tiempo a ponerce a salvo, gracias...<br> :date: __2021-05-25 08:23:11__

> Bamos.amirar.sida.resultado.. Esperemos.que.trabaje.vien. Nosenada.de.la.aplicacion.<br> :date: __2021-05-20 17:02:26__

> Estaría bien que incorporaseis una función para que el usuario pudiese marcar que ya está vacunado, cuántas dosis y de qué laboratorio.<br> :date: __2021-05-17 17:13:34__

> Muy poco práctica<br> :date: __2021-05-10 14:37:25__

> Menudos sustos mete la "notificación semanal" de la última versión. Francamente ¿es necesario que avisen cada semana de que tienes las notificaciones de exposición activadadas? Eso ya lo sé, de hecho ¿para qué iba a quererlas desactivar si la finalidad de esta aplicación es que te notifique si has estado expuesto o notificar tú si has dado positivo? Francamente o el mensaje está equivocado o que te notifique de que la app funciona es no solamente innecesario sino alarmante. Por favor, revisenlo.<br> :date: __2021-04-15 12:58:24__

> Super<br> :date: __2021-04-13 15:10:01__

> Lo veo muy bien me gusta mucho estar informada<br> :date: __2021-04-11 16:24:14__

> Buena Si<br> :date: __2021-04-09 21:55:34__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="es.gob.radarcovid 3 reviews"/>
</p>

> En su tiempo fue echa con muy buena intención pero no creo que halla servido de mucho para frenar la pandemia<br> :date: __2021-06-03 15:50:25__

> Muy buenas<br> :date: __2021-06-02 21:12:28__

> Nunca me dijo nada o me.mostro algo.<br> :date: __2021-05-28 13:22:06__

> Desde que me la descargué en septiembre no me ha avisado de ningún contacto estrecho. Es más, de lo único que me avisa es del error del ahorro de batería, pero aun cambiándolo me sigue dando ese fallo. Una de dos, o he tenido mucha suerte todos estos meses o no funciona.<br> :date: __2021-05-15 17:00:54__

> Los niveles son muy sencillo pero ahora se van a complicar<br> :date: __2021-05-11 23:21:27__

> Muy buena app, pero No sirve de nada si nadie la descarga.<br> :date: __2021-05-10 20:46:55__

> Quiero ponerme la vacuna en Rey Juan Carlos soy dependiente 2 grado casi 3 no puedo ir hasta Madrid garacias No veo bien y no puedo respirar bien<br> :date: __2021-05-09 20:13:43__

> No se pero si me gustaría saber si estoy al lado de un cobi9<br> :date: __2021-05-09 15:37:14__

> Me resulta chocante que en Euskadi que tengo alardeamos de muchas cosa estemos con respecto a otras comunidades n la cola d espera para vacunarnos tengo yo tengo 69 años y ni una sola notificacion para vacunarme<br> :date: __2021-05-07 01:32:52__

> Si se supone que usa el Bluetooth y no la localización, así que no debería de estar constantemente dando señales de alerta para activar localización. Si no quieres hacerlo. Incluso con modo avión, o de noche, molesta. Si no quiero activar localización, no debería de estar todo el tiempo avisando.<br> :date: __2021-05-06 09:05:40__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="es.gob.radarcovid 2 reviews"/>
</p>

> Gavilan<br> :date: __2021-06-07 10:30:33__

> Consume toda mi batería. La idea era muy buena, pero teniendo que usar GPS y bluetooth de esa manera no me dura nada. Demasiado esfuerzo para llevarla activa.<br> :date: __2021-06-04 16:45:38__

> La aplicación está bien, pero la veo algo limitada para la situación actual, sería conveniente añadir una opción para declarar si tienes síntomas, ya que la aplicación solo sirve si oficialmente has dado positivo (cosa que está perfecto) pero hay muchas personas que aún no se han hecho una pcr y padecen síntomas de covid, pues opino que por prevención, sería útil añadir esta opción<br> :date: __2021-06-02 15:12:57__

> Antes me funcionaba bien. Pero hace unos 10 días me dice que no funciona correctamente, la llevo usando desde el principio y nunca me había pasado. La desistalé y volví a instalar. Pero me sigue pasando.<br> :date: __2021-05-21 21:38:41__

> No ha sido útil al estar basada en ser utilizada por mucha gente y no haberse cumplido esta premisa<br> :date: __2021-05-18 18:39:49__

> Un tirar el dinero de los ciudadanos. Inútil total. Al final la borré.<br> :date: __2021-05-16 09:24:04__

> Cuando tuve covid no había forma de ponerlo en la aplicación, te pide un código que nunca tuve<br> :date: __2021-05-16 09:22:07__

> Gracias. Por esta gran aplicación así puedo contagiar a la gente<br> :date: __2021-05-11 14:33:40__

> Excelente iniciativa para ayudar a combatir la pandemia. Lastima que no haya funcionado como debiera. No me refiero al molesto aviso de ahorro de batería que salía cada dos por tres. Sino al conjunto de factores que hacen que no funcione como proyecto. Por un lado la app no la usaba casi nadie porque muchos no sabían que existía o se creían que era intrusiva en cuanto a privacidad. Y por otro lado resulta que para indicara la app que tienes covid han de darte un código especial en el médico.<br> :date: __2021-05-06 07:56:05__

> Nunca he tenido nadie cerca desde que lo instalé, me parece muy raro<br> :date: __2021-05-05 17:52:53__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="es.gob.radarcovid 1 reviews"/>
</p>

> Una patata de aplicación, no ha funcionado nunca.<br> :date: __2021-06-11 07:04:12__

> He dado positivo quiero ponerlo pero no me deja. No tengo ningún código de positivo ni nada. Debería de haber una función para enviar los papeles para que los verifiquen si falla la otro<br> :date: __2021-06-10 16:30:04__

> El bajo nivel en la IA de los npcs de este juego me desespera. queremos mejores actualizaciones, con giros argumentales de calidad.<br> :date: __2021-06-10 04:05:56__

> Gasta batería en exceso, esta App es horrible. Buena idea pero muy mal llevada a la práctica. Un fracaso, y según vi en una noticia ha costado un pastón crearla y mantenerla, lamentable.<br> :date: __2021-06-09 23:52:30__

> La app de pena, mi mujer positiva y dio la alerta en la app. Yo con su móvil y en mi app no detecta que estoy cerca de alguien con covid. De vergüenza<br> :date: __2021-06-09 11:33:52__

> No sé porque hay que ir todo el tiempo con la ubicación activa, me fUnde la batería por eso la desistalo<br> :date: __2021-06-09 09:11:47__

> La vida molaba mas cuando cazabamos pokemons y no infectados<br> :date: __2021-06-09 03:31:24__

> Una auténtica basura que ha costado casi 2 millones de euros a todos los españoles, que vergüenza<br> :date: __2021-06-09 01:33:10__

> No sirve de nada<br> :date: __2021-06-08 22:05:44__

> Pene de plàstico<br> :date: __2021-06-08 16:02:47__


