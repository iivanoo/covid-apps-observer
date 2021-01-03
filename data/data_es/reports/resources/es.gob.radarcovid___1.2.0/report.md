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

> Qwwe tu piel de gallina y<br> :date: __2021-01-03 16:28:02__

> No la tengo, la he instalado ahora pero me parece muy buena idea<br> :date: __2021-01-03 16:16:24__

> Esta aplicacion es muy buena<br> :date: __2021-01-03 13:14:24__

> A veces cuesta obtener información pero normalmente funciona bien<br> :date: __2021-01-03 10:20:28__

> Este tefefono no se qie le pasa pero quiro cargar cosas. Y.no.mesale.. Asi como. Esto. Del covic. Y cosas interesamtes. Asies que nose qie acer..fin....<br> :date: __2021-01-03 08:26:42__

> Normal<br> :date: __2021-01-03 03:01:20__

> Hace lo que tiene que hacer.<br> :date: __2021-01-02 23:13:56__

> Me encanta saber que pasa<br> :date: __2021-01-02 20:08:26__

> Muy interesante<br> :date: __2021-01-02 19:25:16__

> Debería de ser la administración la que metiese en la base de datos los positivos de COVID.19...<br> :date: __2021-01-02 17:37:16__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="es.gob.radarcovid 4 reviews"/>
</p>

> LA TENDRÍAMOS que tener todos activa<br> :date: __2021-01-03 11:47:42__

> Exelente<br> :date: __2021-01-02 16:24:15__

> Esperemos que sea útil<br> :date: __2021-01-02 10:01:16__

> No tengo aun experiencia para opinar.<br> :date: __2020-12-31 09:58:51__

> Lklmnbh Սզզղցն։շ<br> :date: __2020-12-31 01:18:50__

> Como puede tener informacion del Covid<br> :date: __2020-12-30 20:41:04__

> No entiendo bien lo su función<br> :date: __2020-12-30 15:30:36__

> Bueno un medicamento cualquiera tiene que pasar de 5 años a 6 para .ver los efectos Nocivos y lo bueno. ,,Aquí no a pasado ni 2 Años y no se comprometem. a Nada los Laboratorios sobre todo a posibles daños y evitarán cualquier Responsabilidad Civil ante los Pacientes .<br> :date: __2020-12-30 05:46:24__

> No tengo experiencia. Solo aprovechar para decir que tiene poco sentido mantener en blotus abierto para nada. Ya que solo detecta al infectado que esta reconocido oficialmente.<br> :date: __2020-12-29 15:40:22__

> Buena<br> :date: __2020-12-29 13:39:45__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="es.gob.radarcovid 3 reviews"/>
</p>

> Regulera...falta informacion general y akgunas graficas.<br> :date: __2021-01-01 21:43:36__

> Instalada. Espero que valga pra algo<br> :date: __2021-01-01 14:18:04__

> No la instalara ni el 20%de la poblacion por el miedo al rechazo y es que hay muchos prejuicios y estereotipos que no dejan a la gente ser ellos mismos porque yo la instale y me dijeron no veas si eres tonto asi lo estas promulgando al gobierno y a todos los estamentos.<br> :date: __2021-01-01 01:00:12__

> Buena idea mal aplicada. Estoy convencido de que el desarrollo ha sido realizado por profesionales, la app funcionaria si la colaboración con los servicios de salud de toda España fuera fluida y buena, hay que eliminar las particularidades de cada comunidad u crear un sistema que al menos para casos como éste haga que en todos los centros de salud exista un procedimiento claro que todos los trabajadores sepan seguir y aplicar. Y por último que los ciudadanos tomen conciencia.<br> :date: __2020-12-31 15:26:39__

> Es complicado porque quien avisa suele permanecer confinado o ingresado. Así es difícil cruzártelo por la calle o en lugares públicos.<br> :date: __2020-12-31 10:43:45__

> A ver la idea está bien .pero soy partidario de que pidan todos los datos y que sólo el hospital sepa los datos y que ellos automaticemte pueda poner que esa persona está con o sin virus .y tú desde tu móvil solo puedan ver si tienes o no el virus como ahora.porque hay gente mala y no te puedes fiar de nadie .al saber cuánta gente están comprando con el virus y esto no lo avisará si ellos no lo activan.ojala se acabe está pesadilla ya<br> :date: __2020-12-31 04:49:22__

> Aunque no sea totalmente fiable en cuanto a sus datos, la llevo de segunda opción, la primera es lavar manos, usar mascarilla y mantener las distancias.<br> :date: __2020-12-30 10:27:28__

> Le doy 3 estrellas porque cuando salió a mi familia le iba bien pero a mi me salió un error y estuve tiempo sin utilizarlo pero Ya se a solucionado. Por la actualización<br> :date: __2020-12-29 15:02:30__

> El fin de esta aplicación me parece muy bien y creo que debe de funcionar siempre y cuando se cumplan las siguientes condiciones: 1) Que Sanidad suministre el código a cada contagiado y 2) Que ese código el usuario lo introduzca en la app. Si eso no se cumple, la app no sirve para nada. Hasta ahora por lo que he comprobado por lo menos en la Comu. Valenc. no se suministra ningún código, luego la app no sirve, a pesar del millón de euros que parece ser costó su desarrollo, o sea DE VERGUENZA<br> :date: __2020-12-28 14:12:17__

> La llevó usando desde que salió nunca me ha llegado una notificación, no sé si eso es bueno o malo<br> :date: __2020-12-28 11:44:31__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="es.gob.radarcovid 2 reviews"/>
</p>

> No vale para nada<br> :date: __2021-01-02 13:13:58__

> Una app con buenas intenciones pero prácticamente inútil al no hacer uso de la geolocalización a diferencia de la versión asiática que por este motivo y una mayor concienciación de la población genera más avisos. A los occidentales nos preocupa que nos geolocalicen para salvar vidas pero no nos preocupa que nos geolocalicen para publicar estupideces en las redes sociales. Una pena.<br> :date: __2020-12-31 10:14:49__

> Me daba error siempre,la desintalé<br> :date: __2020-12-30 19:45:12__

> Buena idea lo de la app, mal hecha como siempre. Podría ser mejor si en lugar de bluetooth funcionara con datos, sería más instantánea. Debería ser obligatoria para que funcionara, para que todo el mundo la tuviera. El hecho de que tengas que activar tu propio positivo la hace más ineficaz todavía. La tuve instalada desde el primer día, a pesar de que no daba más que errores, nunca me dió un contacto positivo, lo cual es raro raro. La desinstale recientemente porque no me valía para nada<br> :date: __2020-12-30 16:54:44__

> hasta que el informe médico de positivo no venga por defecto el código a introducir no es útil (u utilizar el código dwl informe mismo) . Al tener un positivo si tienes que estar llamando a muchos sitios para obtener un código, y nss con la saturación del sistema de salud. .. mal vamos. para hacer eso llamo a los allegados que yo haya visitado directamente.<br> :date: __2020-12-30 14:55:50__

> La interfas es sencilla, lo malo es la mala recepcion en general, todo la gente hablando de la privacidad cuando tenemos cosas como Google o intagram que son peores , bueno si arreglan los errores y mejoran la covertura de los terrenos estara bien.<br> :date: __2020-12-30 14:01:15__

> Buena app si funcionase y si la gente fuese responsable.<br> :date: __2020-12-30 09:11:44__

> La intención es buena pero si no tenemos todos la aplicación instalada y no se indican correctamente los casos cercanos (por colaboración de las autoridades o los ciudadanos) Radar COVID es francamente inútil. Por ejemplo, probé en mi barrio cerca de un colegio que tuvo que cerrar por problemas de contagios. Incluso nuestro código postal fue seleccionado para hacernos la PCR si teníamos personas mayores viviendo con nosotros. Y, por supuesto, Radar COVID indicaba que el riesgo era casi nulo...<br> :date: __2020-12-29 12:00:16__

> Últimamente solo me sale un mensaje de error de la app, aún teniendo Bluetooth y GPS activados todo el día, no sé a qué se debe este error. De momento he decidido desinstalarla.<br> :date: __2020-12-28 10:41:22__

> La he instalado y desinstalado 2 veces, cuando salió y hace poco para ver si habían corregido los errores, pero no. Aparece el mismo error: desactivar modo ahorro batería para su correcto funcionamiento. Sin tener ese modo activado. Una lástima porque era una buena idea.<br> :date: __2020-12-28 01:12:49__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="es.gob.radarcovid 1 reviews"/>
</p>

> Te gasta la batería en menos de un día y se calienta el móvil mucho.<br> :date: __2021-01-03 16:32:13__

> Lo acabo de instalar y no funciona, da error, asi que desinstalo y le puntuo 0 estrellas<br> :date: __2021-01-03 15:20:18__

> Muy mala la aplicacion<br> :date: __2021-01-03 15:02:32__

> Es tan mala que estan borrando las opiniones.<br> :date: __2021-01-03 14:29:19__

> No funciona bien es un desastre , es una vergüenza .<br> :date: __2021-01-03 14:24:52__

> Nula<br> :date: __2021-01-03 13:47:12__

> Horrible una vez me asusté debido a que recibió una notificación en el autobús Y me doy cuenta que era porque no era la ubicación activada y porque no puedo y porque no puedo tener la ubicación desactivada ya que yo soy una persona privada y yo escribo esto para esto me la he desinstalado ya no la voy a usar más<br> :date: __2021-01-03 12:36:50__

> Después de elegir el idioma no me deja continuar a desinstalar no vale para nada<br> :date: __2021-01-03 11:27:30__

> No funciona. Habiendo estado en la misma habitación que un positivo de COVID con la aplicación instalada y que comunicó su positivo, sigue sin mostrar contactos de riesgo. También, continuamente sale una notificación que pone que "no está funcionando bien" y no sólo me sale a mí, a mis familiares más cercanos que la tienen también les sale. Esta aplicación, además de ocupar memoria, está entre las que más batería consume debido al Bluetooth. Sólo sirve para gastar batería y memoria.<br> :date: __2021-01-03 10:20:53__

> Es una vergüenza que a estas alturas no me aporte ningún aviso de ningún tipo. Que les jodan a los del gobierno<br> :date: __2021-01-03 09:45:25__


