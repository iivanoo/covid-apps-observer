# Coronapp-HUG
App version ``0.0.66``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="Coronapp-HUG icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Coronapp-HUG |
| **Unique identifier** | com.hug_ge.coronapp |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=com.hug_ge.coronapp](https://play.google.com/store/apps/details?id=com.hug_ge.coronapp) |
| **Summary**  | Application visant à informer les patients et citoyens sur le coronavirus. |
| **Privacy policy** | [http://pedamines.com/coronapp/disclaimer.html](http://pedamines.com/coronapp/disclaimer.html) |
| **Latest version** | 0.0.66 |
| **Last update** | 2021-03-03 12:17:32 |
| **Recent changes** | Corrections de bugs et ajout d&#39;adresses manquantes dans la liste des adresses à sélectionner dans le module @choum. |
| **Installs**  | 1 000+ |
| **Category** | Médecine |
| **First release** | 12 mars 2020 |
| **Size**  | 19M |
| **Supported Android version**  | 4.4 ou version ultérieure |

### Description
> Cette application développée par les Hôpitaux universitaires de Genève regroupe des informations médicales relatives à la pandémie de COVID-19. 
<br>Elle permet également de participer à @choum, étude sur la détection précoce des clusters de COVID-19. 
<br>Fonctionnalités : 
<br>  - Informations sur le coronavirus (infos pratiques, FAQ, recommandations de santé, informations sur la vaccination, etc.). Sources : OFSP (Office fédéral de la santé publique) et site des HUG https://www.hug.ch/covid 
<br>  - Coronarisk: outil d’évaluation de la pertinence de passer un test COVID-19. 
<br>  - Informations en temps réel sur l’évolution du nombre de cas en Suisse et en Europe. Sources : Université John Hopkins et openZH. 
<br>  - Participation à l’étude @choum
<br>@choum est un outil de veille épidémiologique utilisé dans le cadre d’une étude pour surveiller la pandémie de COVID-19. Son but est de détecter de façon précoce les clusters de COVID-19 grâce à la participation citoyenne. L’étude est développée par des chercheurs du Service de médecine de premier recours des HUG (SMPR), de l’Université de Genève (UNIGE) et de l’École polytechnique fédérale de Lausanne (EPFL), en collaboration avec l’Université de Paris. Elle est approuvée par la Commission cantonale d’éthique de la recherche. 
<br>Conditions de participation:
<br>  - Avoir plus de 18 ans
<br>  - Résider ou travailler dans le canton de Genève 
<br>  - Disposer d’un smartphone et d’une connexion Internet 
<br>Plus d’infos : hug.plus/atchoum


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/>  | <img src="screenshot_5.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | HUG Hôpitaux universitaires de Genève |
| **Website**  | [https://www.hug-ge.ch/coronavirus](https://www.hug-ge.ch/coronavirus) |
| **Email** | hopitauxuniversitairegeneve@gmail.com |
| **Physical address**  | [rue Gabrielle Perret Gentil 4 1205 Genève Suisse](https://www.google.com/maps/search/rue%20Gabrielle%20Perret%20Gentil%204%201205%20Genève%20Suisse) (Google Maps) |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=HUG+H%C3%B4pitaux+universitaires+de+Gen%C3%A8ve](https://play.google.com/store/apps/developer?id=HUG+H%C3%B4pitaux+universitaires+de+Gen%C3%A8ve) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Pie, version 9 (API level 28) |
| **Effective target Android version**  | Pie, version 9 (API level 28) |
| **Minimum supported Android version**  | KitKat, version 4.4 - 4.4.4 (API level 19) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_COARSE_LOCATION** | :warning:**Dangerous** | Allows an app to access approximate location. 
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>CALL_PHONE** | :warning:**Dangerous** | Allows an application to initiate a phone call without going through the Dialer user interface for the user to confirm the call. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>WRITE_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to write to external storage. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | gstatic.com | Google LLC | :us: US | 2008-02-11 15:31:25 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the device phone type value<br>

**Telephony services abuse**
> - This application makes phone calls<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the ': connect, resolve' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The Coronapp-HUG app has been installed by more than **1000** times. At this time, **-** rated the app and its average score is **0.0**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 0

:star::star::star::star:: 0

:star::star::star:: 0

:star::star:: 0

:star:: 0

### Reviews 

#### 5-star reviews

<p align="center">

</p>

No recent reviews available with 5 stars.

#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="com.hug_ge.coronapp 4 reviews"/>
</p>

> Il devrait avoirs une application gratuite qui devrait existe et à m'être dans tout les téléphones lors d'un achats d'un portables ce serait une application pour pouvoir prendre sa température avec son portable. Sa existe des scaner pour alimentation alors pourquoi pas pour la santé public 😷<br> :date: __2021-03-18 14:45:31__

> Pratique et utile mais dommage que les données parfois datent de mars ou avril...certains points ayant changé !<br> :date: __2020-11-13 14:51:16__



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

</p>

No recent reviews available with 1 stars.
