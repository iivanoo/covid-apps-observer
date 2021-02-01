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

> No está mal!!!!<br> :date: __2021-01-29 22:32:30__

> Muy buena<br> :date: __2021-01-29 17:27:16__

> Ve la descripcion 😷😷<br> :date: __2021-01-28 15:19:17__

> Muy importante de tenerlo<br> :date: __2021-01-28 13:51:51__

> Nom<br> :date: __2021-01-28 09:19:56__

> Expectante<br> :date: __2021-01-28 08:16:34__

> De momento ninguna<br> :date: __2021-01-28 07:07:30__

> Buena<br> :date: __2021-01-28 00:13:23__

> La aplicación está bien<br> :date: __2021-01-27 22:44:55__

> Escelente<br> :date: __2021-01-27 20:29:34__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="es.gob.radarcovid 4 reviews"/>
</p>

> Cuando ya se han seguido las instrucciones del centro sanitario por positivo covid y ya se ha pasado el covid, ¿como se cambia para que no estés registrado como positivo?<br> :date: __2021-01-29 12:54:33__

> nadie hace caso a las recomendaciones,hay que transformar "recomendación" en OBLIGACION.. (no cumplir obligación..SANCION).<br> :date: __2021-01-27 14:10:35__

> Me siento un poco más segura.😘😘<br> :date: __2021-01-27 11:35:14__

> No puedo opinar por suerte no me hizo falta hasta ahora<br> :date: __2021-01-26 13:32:01__

> Es una aplicación que no molesta. Solo pide que tengas el bluetooth activo.... Es una pena que no tenga mayor difusión para que se pueda hacer un mejor seguimiento de los contactos que a veces hacemos sin darnos cuenta con personas que no conocemos en algunos lugares que luego no recordamos.<br> :date: __2021-01-25 14:21:21__

> Hecho en falta informacion sobre el código de diagnostico: donde localizarlo en el informe o si, en caso de positivo, lo facilitan de forma exclusiva para la aplicación.<br> :date: __2021-01-25 09:13:45__

> No tengo comparativa para opina<br> :date: __2021-01-24 01:07:32__

> L Ññuiuuuuuyuuuuuuuu<br> :date: __2021-01-23 13:19:02__

> Rectificar es de sabios ....<br> :date: __2021-01-22 23:27:46__

> Funciona de verdad<br> :date: __2021-01-21 18:53:22__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="es.gob.radarcovid 3 reviews"/>
</p>

> No he sabido cuando había terminado, lo último me preguntan si mi resultado es positivo, No me hecho ninguna prueba pues estoy bien y salgo muy poco, espero q se haya quedado instalado y me sea útil, gracias<br> :date: __2021-01-29 10:55:38__

> Me iba a bajar la aplicación, pero leyendo las reseñas no es que anime mucho, la verdad... De todas formas, habría que ver si los problemas que describe la gente en las reseñas de no notificación se deben a que no llevan activo el bluetooth o a que no meten el código. Si, por el contrario, es por error de la aplicación o porque no dan el código en el hospital, arregladlo, por favor. Me parece una app muy útil, pero para eso, tanto usuarios como administradores, debemos estar atentos.<br> :date: __2021-01-26 21:20:52__

> El concepto de la aplicación es muy bueno, pero la puesta en marcha sin la coordinación necesaria, ni voluntad, ni medios dedicados de las administraciones públicas de este país han hecho que la desinstale por ineficaz. He tenido un caso de Covid cercano con la aplicación instalada y nadie le ha facilitado el código necesario para activar la utilidad de esta aplicación.<br> :date: __2021-01-24 12:28:22__

> Me gasta la batería del teléfono<br> :date: __2021-01-22 22:03:22__

> Valor, ayuda, experiencia, Gente interés + ó -- juego por Poder Extra\*\*\*\*<br> :date: __2021-01-21 18:38:33__

> Esta bien pero si nosotros tenemos el covid 19 se pone alerta<br> :date: __2021-01-21 16:34:40__

> seria una APP si todo era l mundo fueta honesto 100%, o puenso q la administracion lo informase anonimamente , es decir, marcar en todo momento la ubicacion,(excepcionalmente con tema covid), ademad si no se hacen PCR masivas tampoco tiene utiludad, si yo lo tengo el covid y no lo se... es inutil sin saberlo ..<br> :date: __2021-01-20 23:22:44__

> Buena versión de plague.inc<br> :date: __2021-01-18 21:32:23__

> Acabo d descargarla<br> :date: __2021-01-17 14:00:47__

> Para impulsar su uso y sacar provecho a la app, estaría bien que añadieran la opción de indicar si el usuario se ha vacunado o no, distinguiendo entre primera y segunda dosis. Creo que es de gran utilidad para conocer la efectividad de la misma.<br> :date: __2021-01-16 18:51:02__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="es.gob.radarcovid 2 reviews"/>
</p>

> Esta app no sirve si no se la instala un porcentaje elevado de la población. Para ello hay que darle valor al usuario. Si esta app nos diese diariamente las estadísticas COVID o nos dijese las restricciones de movilidad que nos aplican en función de nuestra ubicación, seguro que se la bajaría muchisima más gente<br> :date: __2021-01-29 17:04:37__

> No está bien planteada,,, no es muy útil, una lástima.<br> :date: __2021-01-29 07:50:41__

> Déjalo, igual vas a morir<br> :date: __2021-01-29 05:10:01__

> DEDICARLE MAS TIEMPO A LA APP PORQUE TIENE MUCHOS ERRORES<br> :date: __2021-01-27 21:10:50__

> El concepto está bien, pero no sirve de nada si la gente no se la descarga. Una buena forma de captar gente es introduciendo a la app un apartado de información del virus, casos en tu localidad o ciudad, etc.<br> :date: __2021-01-27 11:44:11__

> Tendría que tener la opción de que arranque la app automáticamente, para asegurar que siempre está activa<br> :date: __2021-01-27 10:04:15__

> Hola, alguien me puede decir si el radar covid funciona en la provincia de Alicante? Gracias de antemano<br> :date: __2021-01-26 18:16:53__

> personalmente,creo que tenerla activada me resta mucha batería. Ya que hay que tenerla activada me gustaría que optimizarán ese inconveniente.Por eso le pongo dos estrellas<br> :date: __2021-01-26 16:45:20__

> Creo que no sirve de muvho.<br> :date: __2021-01-25 22:47:19__

> La tuve descargada más por solidaridad que otra cosa. Pero funciona mal, da errores. Tendrían que haberle dado más publicidad. Pero ya no digo nada hoy un negacionista covid positivo en Murcia, que quiere ver en persona a su medico.... Pero la gente sabe lo que es una pandemia? Antes y más serios, no ahora todo tarde y mal. La app no funciona porque no está bien hecha y tampoco te explican nada<br> :date: __2021-01-25 18:26:30__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="es.gob.radarcovid 1 reviews"/>
</p>

> Para que funcione la app se necesita que la persona que sea positivo en covid introduzca una clave la cual no te dan en los hospitales, sin eso la app es inútil que solo consume batería por tener el bluetooth todo el día encendido<br> :date: __2021-01-29 21:45:47__

> Le doy una estrella porque si no le doy ninguna no me deja calificarlo pero esto sirve para los que ya se sabe que son positivos pero esos total están confinados y los que van por la calle no te los detecta, no sirve para nada<br> :date: __2021-01-29 16:36:17__

> La aplicacion es una auténtica basura.relantiza el móvil e inhabilita a Google Maps .eso sí, rastrea todo el sistema operativo Android.<br> :date: __2021-01-29 16:32:09__

> No funciona lo pruevas lo he provado estando ingresada no salian positivos , estaba lleno urgencias 😨😡<br> :date: __2021-01-29 14:09:25__

> No funciona<br> :date: __2021-01-29 13:49:26__

> No vale para<br> :date: __2021-01-29 13:30:08__

> Pésima inutil<br> :date: __2021-01-29 11:23:00__

> basura del gobierno como todo<br> :date: __2021-01-29 10:57:59__

> No al NWO<br> :date: __2021-01-29 10:48:10__

> Es un desastre.cuando no funcionna hay que actualizarlo<br> :date: __2021-01-29 10:45:36__


