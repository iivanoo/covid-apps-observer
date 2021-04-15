# Covidom Patient
App version ``1.5.21``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="Covidom Patient icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Covidom Patient |
| **Unique identifier** | fr.aphp.covidom |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=fr.aphp.covidom](https://play.google.com/store/apps/details?id=fr.aphp.covidom) |
| **Summary**  | L’assistant de suivi médical pour les patients porteurs du virus COVID-19 |
| **Privacy policy** | [https://www.covidom.fr/politique-confidentialite](https://www.covidom.fr/politique-confidentialite) |
| **Latest version** | 1.5.21 |
| **Last update** | 2020-05-07 11:24:53 |
| **Recent changes** | Vous pouvez désormais activer votre compte Covidom, à l&#39;aide de votre identifiant et du code d&#39;activation transmis, directement sur l&#39;application Android |
| **Installs**  | 10 000+ |
| **Category** | Médecine |
| **First release** | 10 mars 2020 |
| **Size**  | 4,1M |
| **Supported Android version**  | 4.3 ou version ultérieure |

### Description
> *** La solution COVIDOM n'est pas en libre accès et est UNIQUEMENT disponible pour les patients suivis par des services hospitaliers utilisateurs de la plateforme.*** 
<br>Covidom est une application qui permet aux patients porteurs du virus COVID-19 de bénéficier d’un suivi à distance (ou télésuivi) quotidien. Il peut répondre à des questionnaires médicaux qui sont analysés en temps réel. De son côté, l’équipe soignante sait comment le patient vit au quotidien et est alertée si le patient a besoin d’une attention plus particulière. En cas de besoin, le personnel soignant prend le relais et rentre en contact directement avec le patient pour lui donner ses consignes.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 


## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Assistance Publique - Hôpitaux de paris (AP-HP) |
| **Website**  | [https://www.covidom.fr](https://www.covidom.fr) |
| **Email** | contact.devmobile@aphp.fr |
| **Physical address**  | [AP-HP / DSI / WIND 33 bd de Picpus 75012 Paris France](https://www.google.com/maps/search/AP-HP%20/%20DSI%20/%20WIND%2033%20bd%20de%20Picpus%2075012%20Paris%20France) (Google Maps) |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Assistance+Publique+-+H%C3%B4pitaux+de+paris+(AP-HP)](https://play.google.com/store/apps/developer?id=Assistance+Publique+-+H%C3%B4pitaux+de+paris+(AP-HP)) |

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
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>READ_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to read from external storage. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **android.permission<br>WRITE_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to write to external storage. 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 
 **com.google.android.finsky.permission<br>BIND_GET_INSTALL_REFERRER_SERVICE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | googleadservices.com | Google LLC | :us: US | 2003-06-19 16:34:53 |
 | app-measurement.com | Google LLC | :us: US | 2015-06-19 20:13:31 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | googlesyndication.com | Google LLC | :us: US | 2003-01-21 06:17:24 |
 | covidom.fr | Nouveal | - | 2020-03-06 20:03:16 |
 | crashlytics.com | Google LLC | :us: US | 2011-01-21 15:30:40 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | e-fitback.com | Nouveal | :fr: FR | 2015-11-16 13:24:32 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Telephony services abuse**
> - This application makes phone calls<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address ': ; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Lf/a;->a(Ljava/lang/String;)Ljava/lang/StringBuilder;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The Covidom Patient app has been installed by more than **10000** times. At this time, **100** rated the app and its average score is **3.17**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 45

:star::star::star::star:: 7

:star::star::star:: 6

:star::star:: 4

:star:: 38

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="fr.aphp.covidom 5 reviews"/>
</p>

> Very good<br> :date: __2020-04-24 15:31:55__



#### 4-star reviews

<p align="center">

</p>

No recent reviews available with 4 stars.

#### 3-star reviews

<p align="center">

</p>

No recent reviews available with 3 stars.

#### 2-star reviews

<p align="center">

</p>

No recent reviews available with 2 stars.

#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="fr.aphp.covidom 1 reviews"/>
</p>

> Completement inutile, n'a jamais marché.<br> :date: __2020-11-05 09:48:36__


