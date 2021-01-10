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

> Me ha encantado<br> :date: __2021-01-09 19:13:39__

> buenísima<br> :date: __2021-01-09 16:04:22__

> Deberíamos tenerla todo el mundo<br> :date: __2021-01-08 22:07:42__

> Tengo dudas que lo instalen<br> :date: __2021-01-08 20:56:23__

> Super extraordinaria y que todos deberíamos tener mis felicitaciones a nuestro Gobierno<br> :date: __2021-01-08 19:33:04__

> No<br> :date: __2021-01-08 16:24:50__

> Interesante sistema operativo de CovD te vaya avisando de todos los síntomas y el riesgo que se puede tener<br> :date: __2021-01-08 13:25:15__

> Es una aplicación muy necesitada con el tema de comida 19<br> :date: __2021-01-08 11:55:50__

> Escelente<br> :date: __2021-01-08 11:32:35__

> Mola<br> :date: __2021-01-08 06:40:40__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="es.gob.radarcovid 4 reviews"/>
</p>

> No..tengo..de momento...!!!<br> :date: __2021-01-08 14:11:45__

> La neta esta bien pero: no ledoi 5 estrellas porque funciona el 99% porque cuando pille, el corona no supo decirme que estaba con un positivo o si,no Lu ubiera pollo la verdad a parte cuando lo tenía no paraba de decirme estAa en un positivo al lado i me arto, i gasta batería mucha adiós(◍•ᴗ•◍)❤<br> :date: __2021-01-07 22:43:33__

> Yo la tenía xro la quité, xk debería ser obligatorio en toda España, algunas personas k tienen el virus no lo dicen y tampoco te enteras xk ellos no la tienen.<br> :date: __2021-01-07 19:22:32__

> Correcta<br> :date: __2021-01-07 19:05:50__

> Espero que esto se mejore<br> :date: __2021-01-07 17:32:25__

> De momento todo bien, gracias<br> :date: __2021-01-05 16:22:05__

> Gasta demasiada batería<br> :date: __2021-01-05 01:08:41__

> Lo voy a probar<br> :date: __2021-01-04 09:54:50__

> Una pequeña ayuda más para mejorar la situación. Lástima qur no se le dé más publicidad para que la conozca mayor número de gente. A veces salta algún mensaje de que la app no se ha podido actualizar, pero entrando aparece todo en orden (un par de veces tuve que desactivar/activar para que actualizara los datos). Aunque en algunos dispositivos dé errores, mientras no sean muy molestos yo no la desinstalaría, pues la van actualizando y al fin y al cabo es para el bien nuestro y de los nuestros.<br> :date: __2021-01-04 09:22:14__

> Esta bien porque no te pide ningún dato tullo solo tienes que activar el bluetooth y ya.<br> :date: __2021-01-04 07:26:02__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="es.gob.radarcovid 3 reviews"/>
</p>

> Me he instalado la aplicación unas 2 semanas y no ha funcionado. Y no por cuestiones técnicas sino por falta de civismo. Por el mismo motivo por el que la pandemia está tan extendida. Si no eres responsable de no ir donde debes y no mezclarte con quien no tienes que hacerlo ¿vas a notificar por aquí si estás infectado o no? Esta aplicación funcionará bien si la gente es cívica y responsable, cosa que por lo que he visto hasta ahora, no lo es.<br> :date: __2021-01-09 11:19:52__

> Estaría bien aportar estadísticas actualizadas diariamente. Incluir el número de afectados cada 100.000 habitantes, datos sobre las comunidades autónomas, etc...<br> :date: __2021-01-08 22:29:12__

> Nolose cuándo losepa lodigo nose si funciona<br> :date: __2021-01-07 19:27:53__

> Parece buena, pero......quien la usa? Vivo en una zona de muchos contagios, trabajo en reparto a domicilio y nunca me dio cercanía a ningún positivo incluso estando cerca de los que conozco, muchas descarga nada de uso<br> :date: __2021-01-07 14:26:12__

> De momento no tengo datos.<br> :date: __2021-01-05 16:54:45__

> La veo una aplicación bastante útil, pero debería ser obligatorio su descarga y uso para que fuera 100% efectiva. Además, a veces da fallos. Actualmente me da el siguiente error: ASST404; aunque antes de actualizarla me iba bien. Yo añadiría también alguna función de consulta de datos de incidencia en tu comunidad, o el recuento nacional de positivos, o incluso añadiría las restricciones que tiene la comunidad autónoma en la que resides.<br> :date: __2021-01-05 11:07:52__

> Buena Efectiva<br> :date: __2021-01-05 08:35:25__

> Ninguna<br> :date: __2021-01-04 14:17:32__

> Regulera...falta informacion general y akgunas graficas.<br> :date: __2021-01-01 21:43:36__

> Instalada. Espero que valga pra algo<br> :date: __2021-01-01 14:18:04__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="es.gob.radarcovid 2 reviews"/>
</p>

> Es la primera vez que la utilizo<br> :date: __2021-01-09 16:01:27__

> La idea no está mal, pero sin que la administración pública haga publicidad para que se lo instale en su móvil la mayoría de la población no sirve para nada. Desinstalado.<br> :date: __2021-01-09 12:05:19__

> No sirve para nada<br> :date: __2021-01-08 14:22:29__

> Da error cada dos por tres de que no va el bluetooth, cuando éste está funcionando. Da poca confianza de su efectividad.<br> :date: __2021-01-08 10:32:42__

> La aplicación muy correcta. Falta pedagogía para que la gente la use, pero llega tardísimo... Aún así, sigue mereciendo la pena tenerla.<br> :date: __2021-01-07 21:44:39__

> La desinstalé ya dos veces. La finalidad es fantástica, pero seguro que existen mentes más brillantes, técnicos y científicos de verdad, para mejorarla. Lo digo porque todo lo que gestiona ESTE Gobierno de España es ineficaz y chapucero. Gracias<br> :date: __2021-01-07 20:16:30__

> Sale un mensaje de que no funciona correctamente, que desactive el modo ahorro de energía, pero no lo tengo puesto.<br> :date: __2021-01-06 11:29:32__

> Todos los dias entorno a las 21.35 me da un error. De seguir asi la borrare.<br> :date: __2021-01-05 21:40:32__

> La APP no se actualiza y no recibo mensaje alguno<br> :date: __2021-01-05 12:40:58__

> Buena iniciativa mala implementación. Lleva dos días sin actualizar si he estado en contacto o no con alguien que dio positivo. Debería tener un botón para forzar actualización por si falla alguna vez, y publicitarla más para que más gente la llevara puesta y fuera más útil, además de los médicos que detecten un paciente con Covid poder instalarla en el móvil del mismo y notificarlo ellos, por si son personas mayores o lejanas a la tecnología y no saben hacerlo, de este modo tendría sentido.<br> :date: __2021-01-05 09:15:47__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="es.gob.radarcovid 1 reviews"/>
</p>

> No funciona correctamente porque pone falló en la aplicación siempre ésto es una porquería de aplicación no sirve para nada solo para que los políticos nos roben<br> :date: __2021-01-09 18:34:45__

> La instalé el primer día que las autoridades lo pidieron. La activaba cada vez que salía a la calle o recibía alguna visita. Ayer me enteré que en Catalunya no se había activado NUNCA. Nos habían engañado. Por eso la desinstalo.<br> :date: __2021-01-09 18:16:53__

> No sirve<br> :date: __2021-01-09 18:16:16__

> No sirve si nadie notifica su PCR positiva, no me ha notificado exposición en ningún momento pese a que ya hace mucho tiempo que la tengo instalada y hay infinidad de aglomeraciones sobretodo en grandes superficies. Es matemáticamente imposible que no me haya cruzado con ningún positivo.<br> :date: __2021-01-09 17:41:48__

> No conozco a nadie a quien le halla llegado ninguna notificación, teniendo la aplicación descargada y habiendo estado con contagiados. Y no es solo mi opinion<br> :date: __2021-01-09 16:06:16__

> Acabo de instalarlo<br> :date: __2021-01-09 15:33:27__

> Desinstalo. Patético. Y nunca entenderé el que en una actualización nos metieran "de clavo" el control de la ubicación.<br> :date: __2021-01-09 14:16:30__

> Intento informar de un positivo, introduzco los datos de análisis y fecha inicio síntomas, y no me deja pulsar el botón de continuar, ni me da indicaciones de donde esta el problema. Un fiasco.<br> :date: __2021-01-09 13:51:11__

> La he tenido instalada desde el principio y aún no se ha informado de código que valga. Utilidad de app: Mandarte notificaciones todo el ratode que la app no va bien. Claro, cómo va a ir bien si aún no he podido activarla..?<br> :date: __2021-01-09 11:56:50__

> No hay nadie que proclame que tiene el covid.tendria que ser obligatorio que todo el que lo tiene se le disparara la alarma en todos los moviles.<br> :date: __2021-01-09 10:37:26__


