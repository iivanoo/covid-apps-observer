# STOP COVID19 CAT
App version ``1.0.2``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="STOP COVID19 CAT icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | STOP COVID19 CAT |
| **Unique identifier** | cat.gencat.mobi.StopCovid19Cat |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=cat.gencat.mobi.StopCovid19Cat](https://play.google.com/store/apps/details?id=cat.gencat.mobi.StopCovid19Cat) |
| **Summary**  | STOP Covidien 19 CAT es la aplicación móvil de / Salud en relación al Covid19 |
| **Privacy policy** | [http://sem.gencat.cat/ca/061CatSalutRespon/apps-mobils/STOPCOVID19/condicions-seguretat](http://sem.gencat.cat/ca/061CatSalutRespon/apps-mobils/STOPCOVID19/condicions-seguretat) |
| **Latest version** | 1.0.2 |
| **Last update** | 2020-04-02 13:10:54 |
| **Recent changes** | Petites millores. |
| **Installs**  | 500.000+ |
| **Category** | Medicina |
| **First release** | 18 mar. 2020 |
| **Size**  | 3,2M |
| **Supported Android version**  | 6.0 y versiones posteriores |

### Description
> STOP COVID 19 CAT és una aplicació mòbil de /Salut amb un doble objectiu: 
<br>1.  Donar resposta a les necessitats  d'informació de la ciutadania en relació al COVID 19, a través d’un qüestionari que els indica si tenen possibilitat de tenir COVID.   
<br>2. Recollir dades de la població per tal de poder crear mapes de calor pel quadre de comandament.


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
| **Developer**  | Generalitat de Catalunya |
| **Website**  | - |
| **Email** | mobilitat.ctti@gencat.cat |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Generalitat+de+Catalunya](https://play.google.com/store/apps/developer?id=Generalitat+de+Catalunya) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Pie, version 9 (API level 28) |
| **Effective target Android version**  | Pie, version 9 (API level 28) |
| **Minimum supported Android version**  | Marshmallow, version 6.0 (API level 23) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_COARSE_LOCATION** | :warning:**Dangerous** | Allows an app to access approximate location. 
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>READ_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to read from external storage. 
 **android.permission<br>READ_PHONE_STATE** | :warning:**Dangerous** | Allows read only access to phone state, including the phone number of the device, current cellular network information, the status of any ongoing calls, and a list of any PhoneAccounts registered on the device. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>VIBRATE** | Normal | Allows access to the vibrator. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **android.permission<br>WRITE_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to write to external storage. 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 
 **com.google.android.finsky.permission<br>BIND_GET_INSTALL_REFERRER_SERVICE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | googlesyndication.com | Google LLC | :us: US | 2003-01-21 06:17:24 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | app-measurement.com | Google LLC | :us: US | 2015-06-19 20:13:31 |
 | amazonaws.com | Amazon.com, Inc. | :us: US | 2005-08-18 02:10:45 |
 | backendcovid19.net | Whois Privacy Service | :us: US | 2020-03-15 19:07:14 |
 | microsoft.com | Microsoft Corporation | :us: US | 1991-05-02 04:00:00 |
 | mubiquo.com | MUBIQUO APPS, SL  -B65214918 | :es: ES | 2009-05-29 10:23:57 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | googleadservices.com | Google LLC | :us: US | 2003-06-19 16:34:53 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the ISO country code equivalent of the current registered operator's MCC (Mobile Country Code)<br>
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The STOP COVID19 CAT app has been installed by more than **500000** times. At this time, **1609** rated the app and its average score is **3.06875**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 693

:star::star::star::star:: 70

:star::star::star:: 130

:star::star:: 80

:star:: 633

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="cat.gencat.mobi.StopCovid19Cat 5 reviews"/>
</p>

> Esta guau<br> :date: __2020-05-29 12:24:23__

> Si bien el TEST no es del todo amplio y exacto, mi valoración de esta app es muy positiva en el aspecto del acompañamiento que los SANITARIOS han hecho, de forma muy correcta y amable, a las personas que hemos pasado la enfermedad en casa. Yo he recibido el mejor seguimiento y trato por parte de los sanitarios de la app que por parte de mi MÉDICO DE FAMILIA. Tristemente éste ni me llamó una vez. Todos los contactos que yo tuve con él han sido iniciados por mi misma. Muy agradecida a la app.<br> :date: __2020-05-28 11:47:04__

> Esta bien para no colapsar los sistemas sanitarios<br> :date: __2020-05-12 21:00:41__

> Muy buenas.<br> :date: __2020-05-12 18:38:01__

> Bona aplicacio<br> :date: __2020-05-11 16:15:28__

> Esto es muy interesante para todos<br> :date: __2020-05-02 21:51:43__

> Perfecte<br> :date: __2020-05-01 14:19:52__

> La aplicación es muy útil para hacer el seguimiento del virus a nivel de población<br> :date: __2020-04-27 18:36:32__

> Le falta mucho pero para las 4 cosas que tiene las hace bien eso sí le falta muchísimo<br> :date: __2020-04-24 14:51:42__

> Si se hacen controles como en china iriamos mejor pues aqui en españa lo tenemos crudo el control sanitario<br> :date: __2020-04-23 17:09:23__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="cat.gencat.mobi.StopCovid19Cat 4 reviews"/>
</p>

> Ha funcionat bé des de el primer día<br> :date: __2020-05-24 18:05:44__

> Haver perdut el gust i l'olfacte, que segons un estudi força ampli fet x una U. dels EE. UU., una de Suėcia i diverses de la G Bretanya, que deveu conėixer, són mės importants x detectar qui ja l'ha passat o ės contagiarà properament. Gràcies Senador J Cambra Int JIC<br> :date: __2020-05-19 13:57:13__

> Entiendo que es útil a nivel estadístico y que cuantas más personas la utilicemos mejor se colabora para establecer datos importantes.<br> :date: __2020-05-05 23:41:38__

> Incompleta, pero sirve para algo<br> :date: __2020-04-26 11:32:33__

> Estaría bien que recordase los datos para no introducirlos cada vez. Algunos síntomas bien podrían incluir una descripción más detallada de qué se considera ese síntoma. Puedo asegurar que si estás muy mal (según los síntomas) y dices que no puedes valerte por ti mismo en lo más básico te llaman, como el caso de mi madre<br> :date: __2020-04-12 16:40:09__

> Positiva<br> :date: __2020-04-08 13:45:06__

> Es lo que hay<br> :date: __2020-04-08 13:44:40__

> Util Para el seguimiento de síntomas que pudieran ser compatibles con coronavirus<br> :date: __2020-04-04 19:18:16__

> Al finalizar el test no he visto que haga referencia a problemas digestivos como nauseas y diarreas y sí lo contemplan otras fuentes<br> :date: __2020-04-02 19:32:22__

> Estic fent el seguiment però avui, quan intento prèmer el botó ACCEDEIX AL TEST, No hi accedeix..<br> :date: __2020-04-01 13:34:18__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="cat.gencat.mobi.StopCovid19Cat 3 reviews"/>
</p>

> No ñellsimplemente<br> :date: __2020-05-29 21:40:28__

> Poco detallada<br> :date: __2020-05-16 19:48:31__

> A casa som 4 i solament guarda el CIP de l'últim. És podria buscar la forma de que els guardés<br> :date: __2020-04-26 10:44:04__

> Los síntomas se deberían describir y poder precisar mejor. Por ejemplo, ¿36'6 es fiebre? Y si se pone como fiebre, ¿qué temperatura se debería poner, "36'5 o menos" o 37?<br> :date: __2020-04-23 11:46:06__

> Imposible fer el seguiment dels símptomes. L'aplicació falla constantment...<br> :date: __2020-04-17 21:45:08__

> trobo a faltar una opció a l inici pel cas de les persones que estan ngressades amb virus, que han estat donades d alta, que han obtingut un determinat resultat en un determinat tipus de test, etc Es a dir, només tracta el spossibles casos a l inici. I després ?<br> :date: __2020-04-13 11:25:02__

> No solo los sintomas son importantes, estaria bien tambien saber si por el trabajo que tenemos somos mas propensos a infectar a mas gente.<br> :date: __2020-04-09 15:27:55__

> Problemes per identificar-me<br> :date: __2020-04-07 00:12:52__

> Desconec si la LOPD té alguna cosa a veure però, és realment molest tenir que introduïr cada vegada el número de tarjeta sanitària.<br> :date: __2020-04-05 16:54:40__

> estaria be que recordes el numero de tarja sanitaria. es molt molest haver-lo de possar cada vegada<br> :date: __2020-04-05 16:26:29__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="cat.gencat.mobi.StopCovid19Cat 2 reviews"/>
</p>

> Dicen ke asi controlan a diario los datos y no los guarda ya me dirás tú ke manera de controlar.<br> :date: __2020-04-23 13:11:12__

> LO SIENTO PERO ES UNA COMPLETA INUTILIDAD. SI CLIKAS UNA DE LAS PRIMERAS, LA QUE SEA Y NINGUNA MAS EN TODO EL PPROCESO. AUTOMÁTICAMENTE TE DICE QUE TIENES SINTOMAS Y QUE TE QUEDES EN TU CASA Y PARACETAMOL. 1° SI TRABAJO COMO ME VOY A QUEDAR EN CASA? . QUE LE DICES AL JEFE ?(QUE ME QUEDO EN CASA PORQUE TENGO SINTOMAS. A LO QUE EL JEFE CON TODA RAZON DEL MUNDO TE DIRA TRAER BAJA DRL VIRUS.).AVER QUE HACES. PORQUE HACERTE LA PRUEBA ROTUNDAMENTE NO. SI NI SIQUIERA SE PONEN EN CONTACTO CON TIGO.<br> :date: __2020-04-10 09:06:41__

> Siempre da error de conexión<br> :date: __2020-04-05 13:25:16__

> No em serveix de res. Molt limitada en preguntes. Tinc mal de cap que em dura dias, sense febre. Doncs no és corona, és canvi de rutina, prenent ansiolítics.<br> :date: __2020-04-03 21:17:26__

> Falta mas desarroyo pero es un principio Seria mucho mas util un chat con profesionles medicos diario a las personas con sintomas.Me da bastantes fallos en las comunicaciones se bloquea pero igual es por la red.Lo intento mas tarde.<br> :date: __2020-04-01 16:41:46__

> No paráis de decirme que haga el seguimiento cada día pero cuando pongo el CIP me dice que no es correcto y con el dni no hace nada, a ver si lo hacéis mejor y solucionais esto<br> :date: __2020-04-01 15:49:43__

> Da error de conexión desde el sábado<br> :date: __2020-03-30 10:58:14__

> Lleva 2 días sin funcionar...<br> :date: __2020-03-29 16:57:39__

> Creo que no está muy bien calibrada. He puesto que tengo malestar general, sin tos, ni fiebre ni otro síntoma y ya me dice que tengo el virus... Estaria bien arreglar eso para no alarmar a la gente<br> :date: __2020-03-25 09:01:46__

> He intentado entrar varias veces en catalán y en castellano, incluso reiniciando el teléfono, pero siempre que marco la casilla para escribir el numero de la tarjeta de me cierra la app, que puedo hacer?<br> :date: __2020-03-24 09:41:33__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="cat.gencat.mobi.StopCovid19Cat 1 reviews"/>
</p>

> No entenc encara l'objectiu d'aquesta aplicació... més inversió en els equips de primària i no tanta app que només recomana quedar-se a cada, és millor apuntar-se a un paper la simptomatologia.<br> :date: __2020-05-29 11:17:45__

> Una basura, no serveix absolutament de res.<br> :date: __2020-05-28 20:11:40__

> No me deja acceder<br> :date: __2020-05-27 20:36:17__

> Desinstalada a los 5 min. No le veo sentido. No aporta nada útil.<br> :date: __2020-05-23 18:22:35__

> gracias a apps de este tipo vamos a vivir una distopía<br> :date: __2020-05-22 13:46:28__

> No serveix de massa falten altres dades, no tots els casos són de tipus respiratori, també hi han sintomes intestinals forts(edito, no serveix de res) llàstima<br> :date: __2020-05-14 15:24:24__

> Tan solo que tengas malestar general ya te dice que eres posible enfermo del virus. Apenas te pregunta mas sintomas de los muchos que da el covid. Desues de eso te dice ke te aisles en tu habiatacion, llames a tu medico y ya esta . No entiendo para que sirve esta app la verdad. Si al menos algun medico contactase cobtigo para contrastar sintomas o algo pero na d na.... Menuda app mas absurda<br> :date: __2020-05-14 02:23:31__

> Esta app és una castaña, llevo días intentando conectarme y siempre me da error, lo he intentado a diferentes horas. Pocas veces me ha dejado actualizar.<br> :date: __2020-05-11 07:32:05__

> No serveix de res, no truca ningú, a la fin has de fer el de sempre, anar a urgències. Però la medalla ja està col·locada<br> :date: __2020-05-10 19:36:40__

> Fatal, ya puedes intentar a diferentes horas del día que no funciona, eso sí, me a ayudado a memorizar mi targeta sanitaria de tantas veces ingresarla. Gracias¡<br> :date: __2020-05-08 22:16:50__


