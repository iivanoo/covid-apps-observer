# Integreat
App version ``2021.4.0``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="Integreat icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Integreat |
| **Unique identifier** | tuerantuer.app.integreat |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=tuerantuer.app.integreat](https://play.google.com/store/apps/details?id=tuerantuer.app.integreat) |
| **Summary**  | Integreat ist eine kommunale Informations-App für Zugewanderte und Geflüchtete |
| **Privacy policy** | [https://integreat-app.de/en/privacy/](https://integreat-app.de/en/privacy/) |
| **Latest version** | 2021.4.0 |
| **Last update** | 2021-04-08 05:04:20 |
| **Recent changes** | Wir haben hinter den Kulissen hart gearbeitet, um sicherzustellen, dass alles so funktioniert, wie es soll. Wenn Sie bemerken, dass etwas nicht funktioniert, lassen Sie es uns wissen!<br>* Vorherige Städte können nun ohne Internet wieder geöffnet werden.<br>* Um das Senden von Feedback einfacher zu machen wählen wir nun die Art von Feedback automatisch aus! |
| **Installs**  | 10.000+ |
| **Category** | Soziale Netzwerke |
| **First release** | 30.10.2015 |
| **Size**  | 33M |
| **Supported Android version**  | 5.0 oder höher |

### Description
> Mit Integreat haben Sie alle Informationen in einer App. In Ihrer Muttersprache stehen Ihnen aktuelle Tipps, Angebote und Kontaktdaten von lokalen Behörden, Organisationen und Initiativen zur Verfügung. Außerdem können Sie Ausbildungsplätze und Praktika finden. Die App funktioniert auch offline ohne mobiles Internet.


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
| **Developer**  | Tür an Tür - Digitalfabrik gGmbH |
| **Website**  | [https://integreat-app.de/en](https://integreat-app.de/en) |
| **Email** | support@integreat-app.de |
| **Physical address**  | [Wertachstr. 29 86153 Augsburg](https://www.google.com/maps/search/Wertachstr.%2029%2086153%20Augsburg) (Google Maps) |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=T%C3%BCr+an+T%C3%BCr+-+Digitalfabrik+gGmbH](https://play.google.com/store/apps/developer?id=T%C3%BCr+an+T%C3%BCr+-+Digitalfabrik+gGmbH) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Android10, version 10 (API level 29) |
| **Effective target Android version**  | Android10, version 10 (API level 29) |
| **Minimum supported Android version**  | Lollipop, version 5.0 (API level 21) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>ACCESS_WIFI_STATE** | Normal | Allows applications to access information about Wi-Fi networks. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **android.permission<br>WRITE_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to write to external storage. 
 **com.android.vending<br>CHECK_LICENSE** | - | - 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | android.com | Google LLC | :us: US | 1997-06-23 04:00:00 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | facebook.com | Facebook, Inc. | :us: US | 1997-03-29 05:00:00 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the MCC+MNC of the provider of the SIM<br>
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address ' returned no addresses for  ; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Lfi/iki/elonen/NanoHTTPD$ResponseException;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'NanoHttpd Shutdown' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Pim data leakage**
> - This application accesses the downloads folder<br>
> - This application accesses data stored in the clipboard<br>

**Code execution**
> - This application loads a native library<br>
> - This application loads a native library: 'c++_shared'<br>
> - This application loads a native library: 'jniPdfium'<br>
> - This application loads a native library: 'log'<br>
> - This application loads a native library: 'modft2'<br>
> - This application loads a native library: 'modpdfium'<br>
> - This application loads a native library: 'modpng'<br>
> - This application loads a native library: 'reanimated'<br>
> - This application loads a native library: 'sentry'<br>
> - This application loads a native library: 'sentry-android'<br>
> - This application executes a UNIX command<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The Integreat app has been installed by more than **10000** times. At this time, **150** rated the app and its average score is **4.41**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 121

:star::star::star::star:: 7

:star::star::star:: 1

:star::star:: 6

:star:: 15

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="tuerantuer.app.integreat 5 reviews"/>
</p>

> Gesetze über Aufebthaltstittel für geduldete menschen muss entwickelt werden um besser integration zu ermöglichen.<br> :date: __2021-04-03 14:30:44__

> Super zum informieren<br> :date: __2020-09-28 16:00:57__

> Vielen Dank. Es ist ein super App...<br> :date: __2020-04-08 14:16:37__

> Danke schon Abu Ghaida<br> :date: __2020-04-06 21:28:26__

> Super<br> :date: __2019-11-18 18:02:32__

> Heftig<br> :date: __2018-10-25 14:23:05__

> I love this App. DOWNLOAD IT!!!!!<br> :date: __2017-05-06 07:30:21__

> A lot of useful information, easy to access and well summarized. Used for the region Rottal am Inn / Pfarrkirchen<br> :date: __2017-04-09 13:23:52__

> Danke für diese app<br> :date: __2016-10-25 09:27:16__

> Ich.suche.brieffreunden.<br> :date: __2016-09-08 21:27:24__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="tuerantuer.app.integreat 4 reviews"/>
</p>

> Danke schön für dieses App.Die Idee ist super ,aber ich denke Sie sollen alle Städte schreiben und bie jeder Stadt soll ein Tastaur , bei dem man Ihnen informationen geben kann, sein.ZB ich habe viele informationen über Essen und möchte Ihnen sie geben.MFG . Ismaiel<br> :date: __2016-01-03 11:10:18__



#### 3-star reviews

<p align="center">

</p>

No recent reviews available with 3 stars.

#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="tuerantuer.app.integreat 2 reviews"/>
</p>

> Läßt sich nicht öffnen<br> :date: __2020-12-20 16:21:00__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="tuerantuer.app.integreat 1 reviews"/>
</p>

> Is it a feature that the app isn't working?<br> :date: __2018-03-06 08:04:45__


