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

> Muy buen juego, deberían mejorar los niveles yo estoy en la cuarta fase y no subo de nivel, llevo un año jugando y no di positivo ninguna vez, a alguien más le pasa?<br> :date: __2021-03-14 14:14:04__

> Aplicación profesional<br> :date: __2021-03-14 07:44:22__

> YO HICE LA PRUEVA DE COVID NO ME LLAMARON ALOMEJOR HE ESTADO CON GENTE QUE LO TIENE Y NO TE LO DICE NI DA ALERTA<br> :date: __2021-03-13 19:00:41__

> Muy bien<br> :date: __2021-03-12 13:53:28__

> Hola Yo vivo en el campo solo,<br> :date: __2021-03-12 12:48:15__

> A mi me funciona genial. Por suerte, nunca me ha saltado ninguna alerta.<br> :date: __2021-03-12 11:00:48__

> M parece muche bien este aplicación todo tiene k tenerlo para mejorar<br> :date: __2021-03-09 20:48:11__

> Buena privacidad, funciona de fondo sin consumir mucho ni molestar. No he podido probar si es efectiva, ya que no he contactado con nadie positivo.<br> :date: __2021-03-09 16:32:19__

> Me gusta mucho la aplicación<br> :date: __2021-03-08 18:21:40__

> 1omuy bien<br> :date: __2021-03-08 00:52:15__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="es.gob.radarcovid 4 reviews"/>
</p>

> Viajo en transporte público y trabajo en un centro administrativo. La duración del transporte es de más de una hora. Tengo 64 años.<br> :date: __2021-03-13 07:48:05__

> Falla mucho<br> :date: __2021-03-09 19:08:42__

> Acabo de descargármela. Me parece estupendo la iniciativa, así podremos detectar más casos y de forma más rápida.<br> :date: __2021-03-06 04:58:49__

> Me gustaría que también pusieran desde donde se reporta cada caso de COVID-19<br> :date: __2021-03-05 20:15:51__

> Seria muy util si todo enfermo de COVID comunicara su estado de contagiado. De no ser asi, su eficacia se reduce y deja de cumplir su mision al 100x100. Mas colaboracion del ciudadano.<br> :date: __2021-03-04 19:19:30__

> Cuando el código sea abierto le podré dar una puntuación objetiva. Mientras tanto, dinero público, código público.<br> :date: __2021-03-04 08:39:23__

> Un poco decepcionada. No recibo mucha información. Esperaba más la verdad<br> :date: __2021-03-02 12:35:01__

> es buena en su orientación muy ambigua pero correcta<br> :date: __2021-02-28 17:42:24__

> Muy buena<br> :date: __2021-02-27 14:47:19__

> Chachy<br> :date: __2021-02-25 16:49:34__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="es.gob.radarcovid 3 reviews"/>
</p>

> muy sitifactoria.<br> :date: __2021-03-11 15:42:58__

> No se por que la gente no lo usa. Media poblacion contagiada y nunca ha saltado. Funciona realmente????<br> :date: __2021-03-09 13:58:43__

> Creo que es una buena idea veremos como es de efectiva<br> :date: __2021-03-08 22:04:51__

> LA APP TIENE UN VIRUS NO LA DESCARGUES Y SI LA TIENES DESINSTALALA YA ES MUY PELIGROSO PUEDEN RASTREARTE ATENCIÓN TIENE UN VIRUS<br> :date: __2021-03-04 04:33:13__

> No tengo experiencia<br> :date: __2021-03-03 23:53:27__

> Eso de que no te pide ubicacion... A mi si me pide activarla, por lo visto porque el bluetooh se lo exige, creo que en iphones no. Seguramente no use datos de ubicacion ni otroas datoa, pero es que son ya entonces dos funciones que hay que tener activas, y funde la bateria que no veas<br> :date: __2021-03-03 11:41:32__

> Al final es un problema si no se notifican los positivos y todo eso...yo creo que con el código que te dan cuando te hacen los pcr... Ellos deberían notificar el positivo y hasta que no se obtenga un negativo no se cambiaría en la app pero bueno<br> :date: __2021-03-03 01:03:15__

> bien<br> :date: __2021-03-02 22:58:39__

> Los gráficos del juego pueden mejorar. En el nivel 1 la misión es activar el Bluetooth. Después del tutorial, tienes que pasar un código a tus amigos y ellos te lo pasan a ti si les toca de infectado. Yo jugué muchas y nunca me toca de infectado. Pero no se preocupen. Los códigos llegarán en 2030. Y las skins están en 2D pero messirve para ser un juego español. Ahora en serio: Los códigos de los positivos van con retraso, la app consume mucho y la usan 5 de los 47 millones que hay en España<br> :date: __2021-03-01 20:12:25__

> Funcionaría si el codigo que hay que poner se facilitara con el resultado del positivo... no se da tal codigo al paciente, no se promociona la app y ni los centros de salud están al tanto de ella. Después de tantos meses estamos así, es imposible que funcione...<br> :date: __2021-03-01 12:15:23__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="es.gob.radarcovid 2 reviews"/>
</p>

> Poco útil<br> :date: __2021-03-13 07:07:11__

> La aplicación está bien, pero la veo algo limitada para la situación actual, sería conveniente añadir una opción para declarar si tienes síntomas, ya que la aplicación solo sirve si oficialmente has dado positivo (cosa que está perfecto) pero hay muchas personas que aún no se han hecho una pcr y padecen síntomas de covid, pues opino que por prevención, sería útil añadir esta opción<br> :date: __2021-03-12 10:34:52__

> Desinstalando... La idea es buena la verdad, pero no está teniendo mucho éxito, ya que el covid me ha rozado ya varias veces, hemos estado hasta arriba de casos en Alicante y me dice que nunca he tenido contacto con ningún infectado y eso es porque la gente no conoce la app y/o porque a la gente no le interesa.<br> :date: __2021-03-12 02:34:54__

> No hace más que darme alertas de que no funciona correctamente<br> :date: __2021-03-09 17:42:02__

> No le han hecho la publicidad que está aplicación necesita, para que sea efectiva.<br> :date: __2021-03-07 18:29:09__

> Mi experiencia con está aplicación es nula<br> :date: __2021-03-04 13:47:50__

> Yo la eh descargado ase un mes y de momento no tengo ninguna notificación. Y ve q el el barrio donde vivo ay muchos pocitivos no se si, funciona o no , a quien le a funcionado,.<br> :date: __2021-03-03 17:57:42__

> Por favor, añadan integración con Portugal y Francia. No tiene ningún sentido que la aplicación no funcione con nuestros países vecinos.<br> :date: __2021-03-02 18:53:40__

> Me da pena en realidad, que una aplicación pueda funcionar y que la gente no se la instale y que las comunidades no la usen para nada. Llevo con la aplicación desde septiembre del 2020 y no he recibido nada. Tiene que mejorar drásticamente y que todo el mundo la use para lograr el funcionamiento óptimo.<br> :date: __2021-03-02 00:14:26__

> Buena iniciativa pero no vale para nada.<br> :date: __2021-03-01 15:04:49__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="es.gob.radarcovid 1 reviews"/>
</p>

> Confiar en que los contagiados por covid van a indicarlo en la app, aunque sea de manera anónima, es de ilusos. Esta app en este país no puede funcionar<br> :date: __2021-03-14 15:45:29__

> No sirve para nada, en un año no ha habido ningún contacto en toda Barcelona? La gente pasa de esta aplicación, la desinstalo y punto.<br> :date: __2021-03-14 14:28:30__

> coleta cabrón<br> :date: __2021-03-14 12:54:42__

> Es una app que ya no sirve para nada. La tenia puesta no detectaba nada en Hospitalet en varias olas de todo el año. A día hoy, menos todavía, ya que bajadas de contagios, vacunas sumistradas y puestadas, dia 14 marzo menos detectará ya no es necesaria ya que consume recursos para tu mobil y se funde la batería de tenerla puesta.<br> :date: __2021-03-14 11:35:49__

> Terrible la app<br> :date: __2021-03-14 10:05:52__

> No sirve para nada. Nunca avisa...y más si no se hacen las cosas bien, " como siempre" vecinos con COVID, en mi empresa más de 20 positivos, trabajo en el centro de la ciudad y una me ha dado un aviso. Hay gente que no sabe de la existencia de la app, ni de código.<br> :date: __2021-03-14 09:21:53__

> Inservible<br> :date: __2021-03-14 08:58:20__

> Constantes problemas, de Bluetooth, de modo ahorro de batería o simplemente que no funciona, y todo sin estar realmente el Bluetooth desactivado o el modo ahorro puesto<br> :date: __2021-03-14 08:56:46__

> Buena idea e intenciones pero no me funcionó y acabé desinstalándola. Todo porque no me facilitaron –no supieron– mi código al contagiarme: 'Para las cuestas arriba quiero yo el burro, que las cuestas abajo yo me las subo…'<br> :date: __2021-03-13 23:48:34__

> Komo se nota k el gobierno de españa a echo esto a su imagen y semejanza (inutil totalmente)<br> :date: __2021-03-13 21:32:39__


