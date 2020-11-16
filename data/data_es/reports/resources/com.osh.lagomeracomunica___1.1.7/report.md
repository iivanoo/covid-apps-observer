# El Cabildo en tu móvil
App version ``1.1.7``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="El Cabildo en tu móvil icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | El Cabildo en tu móvil |
| **Unique identifier** | com.osh.lagomeracomunica |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=com.osh.lagomeracomunica](https://play.google.com/store/apps/details?id=com.osh.lagomeracomunica) |
| **Summary**  | Servicio de información del Cabildo Insular de La Gomera |
| **Privacy policy** | [https://www.lagomera.es/](https://www.lagomera.es/) |
| **Latest version** | 1.1.7 |
| **Last update** | 2020-07-22 17:19:29 |
| **Recent changes** | Se ha añadido un nuevo menú con los servicios de El Cabildo |
| **Installs**  | 100+ |
| **Category** | Comunicación |
| **First release** | 22 mar. 2020 |
| **Size**  | 18M |
| **Supported Android version**  | 4.1 y versiones posteriores |

### Description
> El Cabildo en tu móvil es una aplicación creada para recibir la información de interés ciudadano que a diario publica la Institución.
<br>Esta herramienta permite el acceso directo a noticias, avisos y alertas oficiales con las que obtener datos ante situaciones de emergencias, convocatorias o anuncios.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | OSH+ |
| **Website**  | [https://www.lagomera.es/](https://www.lagomera.es/) |
| **Email** | prensa@lagomera.es |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=OSH%2B](https://play.google.com/store/apps/developer?id=OSH%2B) |

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
 **android.permission<br>ACCESS_WIFI_STATE** | Normal | Allows applications to access information about Wi-Fi networks. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>READ_APP_BADGE** | - | - 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>VIBRATE** | Normal | Allows access to the vibrator. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **com.anddoes.launcher.permission<br>UPDATE_COUNT** | - | - 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 
 **com.google.android.finsky.permission<br>BIND_GET_INSTALL_REFERRER_SERVICE** | - | - 
 **com.htc.launcher.permission<br>READ_SETTINGS** | - | - 
 **com.htc.launcher.permission<br>UPDATE_SHORTCUT** | - | - 
 **com.huawei.android.launcher.permission<br>CHANGE_BADGE** | - | - 
 **com.huawei.android.launcher.permission<br>READ_SETTINGS** | - | - 
 **com.huawei.android.launcher.permission<br>WRITE_SETTINGS** | - | - 
 **com.majeur.launcher.permission<br>UPDATE_BADGE** | - | - 
 **com.oppo.launcher.permission<br>READ_SETTINGS** | - | - 
 **com.oppo.launcher.permission<br>WRITE_SETTINGS** | - | - 
 **com.osh.lagomeracomunica.permission<br>C2D_MESSAGE** | - | - 
 **com.sec.android.provider.badge.permission<br>READ** | - | - 
 **com.sec.android.provider.badge.permission<br>WRITE** | - | - 
 **com.sonyericsson.home.permission<br>BROADCAST_BADGE** | - | - 
 **com.sonymobile.home.permission<br>PROVIDER_INSERT_BADGE** | - | - 
 **me.everything.badger.permission<br>BADGE_COUNT_READ** | - | - 
 **me.everything.badger.permission<br>BADGE_COUNT_WRITE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | googlesyndication.com | Google LLC | :us: US | 2003-01-21 06:17:24 |
 | app-measurement.com | Google LLC | :us: US | 2015-06-19 20:13:31 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | onesignal.com | Domains By Proxy, LLC | :us: US | 2011-09-10 18:40:52 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>

**Pim data leakage**
> - This application accesses data stored in the clipboard<br>

**Code execution**
> - This application loads a native library: 'flutter'<br>
> - This application executes a UNIX command containing this argument: 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The El Cabildo en tu móvil app has been installed by more than **100** times. At this time, **-** rated the app and its average score is **0.0**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 0

:star::star::star::star:: 0

:star::star::star:: 0

:star::star:: 0

:star:: 0

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="com.osh.lagomeracomunica 5 reviews"/>
</p>

> Bienn<br> :date: __2020-04-12 00:13:50__



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

</p>

No recent reviews available with 1 stars.
