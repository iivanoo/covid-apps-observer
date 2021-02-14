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

> Perfecto<br> :date: __2021-02-13 21:19:22__

> Me a gustado mucho la explicación gracias<br> :date: __2021-02-13 05:43:25__

> MUY ÚTIL<br> :date: __2021-02-13 04:28:54__

> Muy buena<br> :date: __2021-02-12 21:48:31__

> Buenisimo<br> :date: __2021-02-12 21:33:34__

> La aplicacion es muy buena, pero el uso es nefasto.el gobierno no la publicitado adecuadamente, por otro lado la gente contagiada, como no está bien informada no mete los datos y dudo que los médicos faciliten el código para incluir en la aplicación, por lo cual no sirve para mucho . En mi anterior teléfono ya la tuve instalada . Un dinero gastado inútilmente por parte de nuestro Gobierno.<br> :date: __2021-02-12 20:15:06__

> De.toda.la.vida.y.de.sienpre.<br> :date: __2021-02-12 11:17:28__

> Muy adictivo<br> :date: __2021-02-11 19:32:34__

> Es una ap muy buena<br> :date: __2021-02-11 18:14:37__

> Muy bien<br> :date: __2021-02-11 16:13:34__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="es.gob.radarcovid 4 reviews"/>
</p>

> Estube en el ambulatorio y me hicieron la prueba mi madre en la residencia que esta dio asintomática yo negativo cada vez que boy a verla me hacen la prueba estoy agradecida del control que hacen, sigo negativa ella ya está vacunada salud para todos<br> :date: __2021-02-10 15:13:55__

> Ok<br> :date: __2021-02-09 20:00:57__

> Me la instalaria pero casi no voy por la calle y no creo que haya tanto riesgo ahi. Si me contagio estoy seguro que sera porque estoy obligado a estar 6h diarias en una clase con 22 alumnos mas (aunque nos mezclamos con otras 3 clases en optativas) en un instituto que lleva 20 clases confinadas. A ver si inventais una app para eso!!<br> :date: __2021-02-09 17:20:55__

> No va bien<br> :date: __2021-02-08 18:32:24__

> Alguien puede decirme porqué es necesaria la geolocalizacion y la activación del GPS cuando el ministerio ha dicho siempre que no nos geolocalizan???<br> :date: __2021-02-08 08:17:01__

> A mi me aviso varias veces<br> :date: __2021-02-07 23:06:16__

> Buena<br> :date: __2021-02-04 22:11:06__

> Buena<br> :date: __2021-02-03 15:31:52__

> Bien<br> :date: __2021-02-01 14:45:13__

> Es. Muy. Util. Okey. Makey<br> :date: __2021-02-01 07:46:54__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="es.gob.radarcovid 3 reviews"/>
</p>

> Para lo que hace esta bastante bien aunque la podrían mejorar, pero no está mal.<br> :date: __2021-02-13 16:56:38__

> La instale para nada ya que nadie avisa cuando esta contagiado, y los poco que lo hicieron no alerto para nada. Buena idea pero aqui noo estamos concenciado en su uso<br> :date: __2021-02-12 01:23:50__

> Solo es una medida preventiva<br> :date: __2021-02-10 18:53:07__

> Creo que es muy importante esta App, pero le falta perfeccionamiento; ya que falla en algunas ocasiones, y no actuliza los datos en curso.<br> :date: __2021-02-10 13:41:14__

> 1.si es difícil conseguir el código ,imagínate conseguir que alguien se tome la molestia de informarlo donde debe,ya que desde otro ministerio es ilegal obtener dicha información,o sea hace falta un doble consentimiento ,una vez y llegue la información tarda algo en aparecer puede tardar horas ,o segundos si sabes darle a sincronizar ,suponiendo que todo haya llegado donde debe ... La app de Alemania falla ?Pues eso... España...<br> :date: __2021-02-08 22:11:58__

> Le doy tres estrellas porque tuve la aplicación instalada durante seis meses y nunca recibí ninguna alerta, entiendo que esto sucede porque la mayoría de las personas no se la han instalado; supongo, entonces, que el problema puede estar en la publicidad de la aplicación, pero si las personas no la descargan es inútil tenerla...<br> :date: __2021-02-07 17:32:53__

> Sabemos que la app tiene fallos y se comprende,pero para que nos la instalamos si luego cuando hay un positivo no se activa. Nadie del personal sanitario preguntó por ella. Como siempre mucha desorganización en el sistema. Una pena.<br> :date: __2021-02-07 12:52:59__

> No tengo<br> :date: __2021-02-07 07:53:01__

> No funciona, siempre me dice que tengo el modo ahorro de energía activado y no es verdad. Me funciono una semana y ya nada.<br> :date: __2021-02-06 19:21:07__

> Gracias por la app una iniciativa genial pero la desinstalo por que si soy el unico k la tiene no me sirve de nada,desde que salió la llevo instalada y nada , trabajo en un supermercado y por aqui pasa muchisima gente y solo tengo la app ocupando memoria en tlf,siento mucho que la gente no se lo tome enserio , cuidaos todos 😘<br> :date: __2021-02-05 12:53:39__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="es.gob.radarcovid 2 reviews"/>
</p>

> Lo descargué pensando que sería similar a un UAV o un V-SAT pero nada que ver. Aún tengo que probar sacarme 5 kills para ver su se activa. Les informaré. Conseguí 15 kills con la app activa y nada, esto no sirve.<br> :date: __2021-02-09 12:28:26__

> Cómo es que incluso "Corona Contact Tracing Germany" tiene más funciones?<br> :date: __2021-02-08 07:57:25__

> MEJOR QUE ESTO ESTE POR SANITARIOS O MEDICOS Y QUE HAGAIS PRUEBAS COMO CADA DIA SALE UNA COSA NUEVA PUES NO TENEIS NI IDEA DE QUIEN ESTA BIEN O MAL NO ES JUSTO EN MADRID QUE VOLVÁIS HA QUITAR MEDIDAS Y EL RADAR ESTE OUES NO TE DICE NADA MAS CONTROLES QUE SOMOS PERSONAS<br> :date: __2021-02-07 07:16:08__

> Lo instalé en dos ocasiones, pero me sigue dando error, no entiendo el motivo.<br> :date: __2021-02-06 15:05:33__

> ,todo anónimo y con esta aplicación puedes saber si hay exposición baja o alta y si hay contacto de riesgo.En caso de ser positivo , te informan y escribes código que te envían,de manera segura para que se use con responsabilidad.El problema que no funciona<br> :date: __2021-02-04 16:17:34__

> Creo que no sirve para nada creo que si imperan cambios seria mejor le doy 2 estrellas para que lo arregle<br> :date: __2021-02-04 15:33:50__

> Si no se da el código a los contagiados esta aplicación es inútil<br> :date: __2021-02-04 10:07:21__

> Una PM.no vale para nada<br> :date: __2021-02-02 01:47:12__

> Sí quienes tienen covi no lo notifican. Como lo sé yo?<br> :date: __2021-02-01 19:08:53__

> hay q mejorar todo<br> :date: __2021-02-01 00:25:36__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="es.gob.radarcovid 1 reviews"/>
</p>

> Si los que están contagiados no lo usan, y no se identifican como tal en la app, no tiene mucho sentido la aplicación usarla ya que nunca nos avisará. Además no sé actualiza con regularidad<br> :date: __2021-02-13 20:56:02__

> Una porquería, un amigo que la tiene puso su positivo y a mi no me avisó de nada. La aplicación no sirve para nada.<br> :date: __2021-02-13 20:15:30__

> Mala implementado,lo cierto es que la mayoría de la gente no la usa, ya que no tiene enganche de ningún tipo por ejemplo que obliguen a tenerla para entrar a espacios cerrados.<br> :date: __2021-02-13 19:51:58__

> Penoso<br> :date: __2021-02-13 19:34:08__

> Llevaba con ella instalada desde el principio y no ha funcionado bien NI UNA SOLA VEZ. Me parece vergonzoso que tengáis esta idea tan mal gestionada cuando facilitaría muchísimo la tarea de los rastreadores.<br> :date: __2021-02-13 18:01:30__

> Son muy pesados,conque te lo digan una vez basta,pero estos insisten,que pesadez...<br> :date: __2021-02-13 17:29:04__

> No vale para nada de hecho estoy pensando en desinstalarla no avisa de nada<br> :date: __2021-02-13 17:18:51__

> No funciona, siempre está notificando de error<br> :date: __2021-02-13 15:57:04__

> Estoy ingresado en UVI con Covid, rodeado de contagiados y me sale que estoy en una zona "sin riesgo" 🤦🏻<br> :date: __2021-02-13 15:29:32__

> No sirve para nada. Publicidad del gobierno solamente<br> :date: __2021-02-13 13:48:19__


