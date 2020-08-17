# CoronaMadrid
App version ``1.1.0``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="CoronaMadrid icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | CoronaMadrid |
| **Unique identifier** | org.madrid.CoronaMadrid |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=org.madrid.CoronaMadrid](https://play.google.com/store/apps/details?id=org.madrid.CoronaMadrid) |
| **Summary**  | Aplicación para la detección y auto-evaluación del Coronavirus, o COVID-19 |
| **Privacy policy** | [https://www.coronamadrid.com/proteccion-de-datos](https://www.coronamadrid.com/proteccion-de-datos) |
| **Latest version** | 1.1.0 |
| **Last update** | 2020-06-25 19:53:43 |
| **Recent changes** | Posibilidad de realizar pruebas a familiares desde el mismo dispositivo |
| **Installs**  | 50.000+ |
| **Category** | Medicina |
| **First release** | 23 mar. 2020 |
| **Size**  | 3,3M |
| **Supported Android version**  | 5.1 y versiones posteriores |

### Description
> La aplicación móvil CoronaMadrid permite a sus usuarios poder detectar, informarse y contactar con las autoridades en cualquier fase de la concepción de la enfermedad COVID-19.
<br>El virus SARS-CoV-2, también conocido como Coronavirus está en fase de pandemia global y por esta razón nace CoronaMadrid, una aplicación que tiene la misión de ayudar a los ciudadanos a poder detectar si están siendo afectados por la enfermedad y obtener las mejores recomendaciones dependiendo de su estado. En caso de estado grave las autoridades serán conocedoras de la situación y podrán comunicarse directamente con el afectado.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/>  | <img src="screenshot_5.png" alt="screenshot" width="300"/>  | <img src="screenshot_6.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_7.png" alt="screenshot" width="300"/>  | <img src="screenshot_8.png" alt="screenshot" width="300"/>  | <img src="screenshot_9.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_10.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Comunidad de Madrid |
| **Website**  | [https://coronavirus.comunidad.madrid](https://coronavirus.comunidad.madrid) |
| **Email** | sanidadinforma@salud.madrid.org |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Comunidad+de+Madrid](https://play.google.com/store/apps/developer?id=Comunidad+de+Madrid) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Pie, version 9 (API level 28) |
| **Effective target Android version**  | Pie, version 9 (API level 28) |
| **Minimum supported Android version**  | Jelly Bean, version 4.1.x (API level 16) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_COARSE_LOCATION** | :warning:**Dangerous** | Allows an app to access approximate location. 
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>ACCESS_WIFI_STATE** | Normal | Allows applications to access information about Wi-Fi networks. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 
 **com.google.android.finsky.permission<br>BIND_GET_INSTALL_REFERRER_SERVICE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | android.com | Google LLC | :us: US | 1997-06-23 04:00:00 |
 | googlesyndication.com | Google LLC | :us: US | 2003-01-21 06:17:24 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | app-measurement.com | Google LLC | :us: US | 2015-06-19 20:13:31 |
 | facebook.com | Facebook, Inc. | :us: US | 1997-03-29 05:00:00 |
 | pinterest.com | DNStination Inc. | :us: US | 2009-11-26 19:21:23 |
 | twitter.com | Twitter, Inc. | :us: US | 2000-01-21 16:28:17 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | googleadservices.com | Google LLC | :us: US | 2003-06-19 16:34:53 |
 | crashlytics.com | Google LLC | :us: US | 2011-01-21 15:30:40 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>
> - This application reads the phone number string for line 1, for example, the MSISDN for a GSM phone<br>

**Location lookup**
> - This application reads location information from all available providers (WiFi, GPS etc.)<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the ': connect, resolve' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Pim data leakage**
> - This application accesses the downloads folder<br>
> - This application accesses data stored in the clipboard<br>

**Code execution**
> - This application loads a native library<br>
> - This application loads a native library: 'Ljava/util/Iterator;->next()Ljava/lang/Object;'<br>
> - This application loads a native library: 'crashlytics'<br>
> - This application executes a UNIX command containing this argument: '2'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The CoronaMadrid app has been installed by more than **50000** times. At this time, **339** rated the app and its average score is **3.0**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 118

:star::star::star::star:: 33

:star::star::star:: 37

:star::star:: 27

:star:: 122

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="org.madrid.CoronaMadrid 5 reviews"/>
</p>

> Me la acabo de instalar<br> :date: __2020-08-10 11:40:23__

> Aún no le he usado, pero parece efectiva.<br> :date: __2020-08-08 18:45:23__

> Muy controlado<br> :date: __2020-07-24 00:04:41__

> Sencilla de utilizar y muy útil<br> :date: __2020-07-13 15:36:55__

> Te indica fácilmente si puedes tener coronavirus<br> :date: __2020-07-13 15:31:42__

> Ha sido muy facil de usar y muy práctica.<br> :date: __2020-07-08 21:14:07__

> Excelente, buen seguimiento.<br> :date: __2020-07-01 16:47:36__

> Funciona bien cumple lo que promete, ayuda al diagnóstico y a evitar riesgos<br> :date: __2020-06-27 14:18:58__

> En el centro de salud calle odonell no les dio la gana de hacerlo.con una oscultacion de 1 minuto la dictora ya te decia que no tenias nada .soy de riesgo y cronico .diabetico y con cancer como se explica esa actuacion tengo el nombre de la doctora si me pasa algo esta todo grabado .<br> :date: __2020-05-18 16:20:48__

> Mejorarla, meter más opciones de diagnóstico.<br> :date: __2020-05-09 17:01:13__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="org.madrid.CoronaMadrid 4 reviews"/>
</p>

> Bien, estaba tranquilo y confiado en las pautas, gracias Javier<br> :date: __2020-07-04 11:22:48__

> Parece ser que la aplicación es buena pero cuando introduces o intenta introducir tu fecha de nacimiento no lo puede hacer correctamente por lo menos los que han nacido antes del 2007<br> :date: __2020-07-01 16:59:45__

> Buena<br> :date: __2020-07-01 16:28:31__

> Muy util<br> :date: __2020-06-23 17:50:47__

> Esta bien la aplicación para hacerte autotest de coronavirus pero espero que mejore más está aplicación<br> :date: __2020-05-29 01:23:56__

> Te va avisando de cuando puedes ir haciéndote el test de las preguntas. Te da pautas a seguir según el resultado que te haya dado<br> :date: __2020-04-23 17:45:23__

> Buena<br> :date: __2020-04-13 09:25:49__

> Me ayuda a despejar las dudas<br> :date: __2020-04-12 14:47:41__

> Buena y tranquilizadora<br> :date: __2020-04-12 11:18:14__

> Me parece muy bien, pero no es un juicio si no si no, tienen que dejar escribir algo periódicamente, porque puede ser que haya tenido dolor de cabeza 2 días no 15 días. Pero el esfuerzo está bien, entre todos podemos. Aplicación se podía un saludo<br> :date: __2020-04-09 13:09:58__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="org.madrid.CoronaMadrid 3 reviews"/>
</p>

> Deberían actualizar las recomendaciones. Según la aplicación la mascarilla no es obligatoria....<br> :date: __2020-08-16 16:37:20__

> Debería actualizarse la información relacionada con la obligatoriedad de llevar mascarilla en todos los casos desde el pasado 30 de agosto.<br> :date: __2020-08-02 14:27:19__

> La fecha de nacimiento debería poder teclearse. Podria dejar incluir resultado de una prueba de Covid.<br> :date: __2020-07-23 00:49:34__

> Sería más que adecuado, que en la próxima actualización se modificara la recomendación sobre las mascarillas (ya que desde el 21 de mayo su uso es obligatorio en muchos lugares, con independencia de si se tiene o no síntomas). Gracias.<br> :date: __2020-05-21 12:01:07__

> De qué me atiendan lo pondre<br> :date: __2020-05-06 13:23:50__

> El contestar Sí o No, no es suficiénte. A veces hay concretar algo<br> :date: __2020-04-16 21:04:02__

> Insuficiente.Faltan síntomas como dolor de cabeza, mareos,, conjuntivitis , mucha gente lo está pasando sin los síntomas que aparecen en esta App.<br> :date: __2020-04-16 08:17:52__

> Creo que deberian modificarla para incluir la pregunta: "¿Has sufrido una repentina perdida de olfato?" Segun parece esto se esta mostrando bastante indicativo de posible contagio por coronavirus.<br> :date: __2020-04-15 08:06:01__

> Deberían sacarla para toda españa...ni que el virus solo estuviera en madrid. Es buena pero incompleta.<br> :date: __2020-04-07 09:46:43__

> Estaria bien que pudieses cambiar en vez de madrid de donde tu seas<br> :date: __2020-04-06 17:04:21__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="org.madrid.CoronaMadrid 2 reviews"/>
</p>

> No la veo ninguna utilidad, pero espero que alguien le valga para algo<br> :date: __2020-08-05 13:11:10__

> No hace falta pedir registro para esto<br> :date: __2020-08-03 12:12:42__

> Necesita una mejora para facilitar el rastreo: una simple agenda donde podamos anotar, cada noche ( que notifique), dónde y con quien hemos estado. A falta de una app dedicada con tecnología GPS y Bluetooth, podría ayuda mucho<br> :date: __2020-07-26 09:34:13__

> Hacer introducir mes a mes la fecha de nacimiento a alguien que haya nacido por ejemplo hace 50 años (no quiero pensar si se está muriendo, o tiene 80 años) me parece una idea maravillosa.<br> :date: __2020-07-11 20:35:49__

> No se conecta con los servicios de Android de Covid para mandar alertas a los posibles contactos cercanos. Es algo que apenas cuesta y sirve para la trazabilidad de rebrotes... Que en la CCAA de Madrid los hay (aunque pequeños), y no se están trazando por falta de personal cualificado. Por favor Ayuso, aprovéchate de la tecnología que te hace el trabajo y además quedas bien... Si pudiste llevar el Twitter de un perro es lo menos que puedes hacer.<br> :date: __2020-06-27 17:03:46__

> Lo que te dice lo sabes de antemano<br> :date: __2020-05-12 16:01:06__

> No vale para mucho, no permite hacer un seguimiento real de la evolución de los síntomas. Muy limitado. Y quienes te llaman ni siquiera son sanitarios a los que se puedan consultarles dudas.<br> :date: __2020-05-04 22:58:45__

> El día 2/4/20 tuve unas alteraciones en mi salud que me inducen a pensar que tuve Covid19 empece a tomar paracetamol y me fue bajando la fiebre y los escalofríos, a todo esto me dijeron que con los datos que les di no podían evaluar si estaba contagiado.¿ porque no hacen test masivos? a lo mejor lo he tenido de forma leve y he podido estar contagiando sin saberlo.<br> :date: __2020-05-04 10:59:47__

> Me parece que hacen muy pocas preguntas... Por ejemplo, no está el tema de los sarpullidos y picor en la piel, la diarrea, etc. El covid tiene más síntomas que la tos, fiebre y la falta de aire.<br> :date: __2020-04-25 23:27:59__

> La idea de la app es buena. Pero sabiéndose que hay otros síntomas de la enfermedad y que estos no se encuentran en las opciones, se resulta un tanto ineficaz para un real control.<br> :date: __2020-04-11 20:34:07__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="org.madrid.CoronaMadrid 1 reviews"/>
</p>

> malísima, menudos ineptos los desarrolladores, no puedes buscar centros de salud por dirección, solo en modo mapa, incompetentes total. después no hay botón para salir de la aplicación, como sois tan zopencos.<br> :date: __2020-08-16 11:56:56__

> Ni siquiera se abre, da error.<br> :date: __2020-08-12 21:33:34__

> Muy mejorable<br> :date: __2020-08-12 21:18:12__

> No me sirve de nada si no me informa de posibles contactos<br> :date: __2020-08-11 21:41:28__

> desinstalada, para poner la fecha de nacimiento y en vez de poner tres ruedas con los diferentes números y así poner la fecha de nacimiento, colocan el Lumbreras del desarrollador un calendario por hojas si tienes qué volver atrás 40 años desde la fecha qué instalas la app te tiras toda la tardecita y eso me dice mucho sobre la efectividad de la app, claro qué sabiendo los qué están gestionando la pandemia en Madrid pués puede pasar cualquier cosa, panda de inútiles.. no hacen una cosa bien..<br> :date: __2020-08-09 14:26:37__

> Una aplicación q no sirve para nada. Una estafa si pagaron por crearla. No ayuda en nada conozco mejores opciones de rastreo.<br> :date: __2020-08-06 14:21:19__

> Nefasto. Vivo en Valdemoro, cp 28341 y dice que no existe. Esta app la han hecho canis o cayetanos a dedo???<br> :date: __2020-08-05 13:15:02__

> O no he entendido para que sirve o es una patata...<br> :date: __2020-08-04 13:49:59__

> Es tan inútil como la retrasada de Ayuso<br> :date: __2020-08-02 11:26:09__

> Alguien ha conseguido poner la fecha de nacimiento? Habéis pagado por esto?<br> :date: __2020-07-31 22:32:42__


