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

> Muy interesante<br> :date: __2021-02-23 09:45:35__

> Me da seguridad<br> :date: __2021-02-23 09:06:13__

> No he estado nunca cerca de nadie<br> :date: __2021-02-23 07:29:04__

> No tengo.Llevo encerrada un año.aislada en el campo.Solo salgo 1 vez al mes cuando dan la paga por incapacidad. Y compro lo básico,leche,legumbres,verdura congelada. Tengo una enfermedad grave pero,no hay citas ni nada.Ya lo he asumido.Hay que morir.De lo que sea.<br> :date: __2021-02-22 21:52:34__

> Debería ser obligatorio<br> :date: __2021-02-22 16:11:16__

> Me parece correcto para avanzar sobre el covid<br> :date: __2021-02-22 08:41:15__

> Salgo lo indispensable con la FFP2 pero parece que nunca me encuentro con personas contagiadas. Pienso que no tienen instaladas esta aplicacion<br> :date: __2021-02-22 06:37:12__

> Haya ahora no tengo ninguna experiencia.<br> :date: __2021-02-21 21:38:10__

> Buen app muchas gracias ☺️☺️<br> :date: __2021-02-21 20:19:43__

> Mala<br> :date: __2021-02-21 19:40:37__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="es.gob.radarcovid 4 reviews"/>
</p>

> Parece que ya va bien.<br> :date: __2021-02-23 18:28:27__

> Bien hasta hasta hora<br> :date: __2021-02-23 07:46:54__

> Bien<br> :date: __2021-02-22 15:49:33__

> El juego un poco difícil si no mezclas el virus con la plaga porque es una combinación bastante chetada. El boss final no tiene muchos ataques pero te infectan con vacunas y te dejan veneno y sangrado. Un juego mediocre 4 estrellas se merece.<br> :date: __2021-02-22 12:58:14__

> Buena. Si tiene Efectos!<br> :date: __2021-02-21 20:11:27__

> Necesaria<br> :date: __2021-02-21 18:36:59__

> No lo entiendo bien pero mi.experienza fue horrible b al descargar.la aplicación de Radar Covid19 y veo positivo avisé a el hospital. Y los con .<br> :date: __2021-02-21 04:23:37__

> Muy bien<br> :date: __2021-02-21 00:00:33__

> Por suerte no he tenido a nadie cerca de mi, con la pandemia, pero reconozco que el sistema es muy bueno.<br> :date: __2021-02-20 15:42:33__

> En alguna ocasión me falla<br> :date: __2021-02-20 15:21:01__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="es.gob.radarcovid 3 reviews"/>
</p>

> Aparentemente funciona bien, pero si intento abrir la pestaña «como actuar si tengo sintomas», aparece error «no ae puede abrir pdf». ¿Se puede solucionar ese error? Gracias<br> :date: __2021-02-23 12:21:10__

> Poca aceptacion ciudadana, debido a poca pedagogia<br> :date: __2021-02-22 10:42:26__

> De momento no me habran tenido que avisar creo yo.Asi que no se como funciona aun.<br> :date: __2021-02-21 20:56:50__

> Con la última actualización se ha quedado colgado y no termina<br> :date: __2021-02-21 11:38:42__

> Porque hay mantener el bluetooth<br> :date: __2021-02-21 11:00:19__

> Me parece buena idea la app, pero deberían arreglar los fallos. Me sale continuamente un mensaje diciendo que no funciona correctamente, que quite el ahorro de datos (cosa que nunca está puesto) y me desespera. Ojalá la gente la usase de verdad.<br> :date: __2021-02-21 08:11:01__

> La verdad es que no sé como valorarla; no he recibido ningún aviso...<br> :date: __2021-02-20 17:24:31__

> No me gusta pero es un poco útil,enhorabuena!!!!<br> :date: __2021-02-20 12:10:20__

> Nuca me avisa si tengo alguien con covid a mi lado<br> :date: __2021-02-20 01:08:53__

> La tengo desde el principio, y creo que en ningún momento ha sido útil.<br> :date: __2021-02-20 01:02:22__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="es.gob.radarcovid 2 reviews"/>
</p>

> Losiento ¿govierno pero vamos pudiese no atacar ala privacidad?? Graciaaas<br> :date: __2021-02-23 17:34:11__

> La idea es buena, pero la ejecución ha sido nefasta. La tasa de contagios declarada con la aplicación ha sido ínfima,y su coste no habrá sido pequeño.<br> :date: __2021-02-23 07:53:03__

> No me gusta no lo veo fiable<br> :date: __2021-02-21 00:03:08__

> No es de utilidad<br> :date: __2021-02-20 19:45:06__

> Muy bien<br> :date: __2021-02-20 19:29:06__

> De momento no es útil.La gente no está concienciada para usarla. Veo que la única opción es que sea obligatoria.<br> :date: __2021-02-20 18:45:28__

> La aplicación no es efectiva si se tarda mas de 4 dias en que te den el código para confirmar un positivo.<br> :date: __2021-02-20 14:31:52__

> La gente no lo usa y siempre da fuera de riesgo<br> :date: __2021-02-20 10:52:58__

> La APP es fácil de manejar y supongo que avisará en caso de contacto con alguien con covid, pero no deja de ser una birria. Casi nadie la instala porque es "opcional" cuando debería ser obligatoria y su tecnología deja bastante que desear; ni geoposicionamiento, ni identificación, necesita 15 minutos de contacto y además por bluetooth... todo para salvaguardar unos "derechos fundamentales" que parecen estar muy por encima de la vida que millones de personas.<br> :date: __2021-02-20 07:52:31__

> no vale de mucho<br> :date: __2021-02-19 21:35:18__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="es.gob.radarcovid 1 reviews"/>
</p>

> No me gusta no lo veo efectivo<br> :date: __2021-02-23 17:43:08__

> No se entiende porqué omiten que es necesario activar el GPS al final de la instalación. Generan desconfianza y la población no instala la App. Sólo detectó el 2% de infectados y cuesta 2 millones de Euros.<br> :date: __2021-02-23 17:38:07__

> No sirve de nada<br> :date: __2021-02-23 16:32:42__

> Esto no funciona<br> :date: __2021-02-23 14:27:47__

> No actualiza<br> :date: __2021-02-23 13:30:25__

> No sirve para nada he estado en el hospital junto a los covid19 y no me ha avisado. Esto es un rollo<br> :date: __2021-02-23 12:14:49__

> A mi me funciona fatal siempre me da algún tipo de error, la desinstale y la volvi a instalar y sigue igual<br> :date: __2021-02-23 11:08:05__

> No aparecen casos cerca una basura siempre limpio de covid, genial para el gobierno y su campaña<br> :date: __2021-02-22 23:57:09__

> No me dicen cuando tendre la primera vacuna tengo 62 años y patologias graves<br> :date: __2021-02-22 21:38:51__

> Subscribanse todos a DjMariio<br> :date: __2021-02-22 17:44:44__


