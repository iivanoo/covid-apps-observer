# Stadt Garbsen
App version ``1.1.0``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="Stadt Garbsen icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Stadt Garbsen |
| **Unique identifier** | de.stadtgarbsen.hellofomo |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=de.stadtgarbsen.hellofomo](https://play.google.com/store/apps/details?id=de.stadtgarbsen.hellofomo) |
| **Summary**  | Informationen der Stadt Garbsen. |
| **Privacy policy** | [https://www.garbsen.de/portal/seiten/datenschutz-904000790-21200.html](https://www.garbsen.de/portal/seiten/datenschutz-904000790-21200.html) |
| **Latest version** | 1.1.0 |
| **Last update** | 2020-06-22 12:35:01 |
| **Recent changes** | Dieses Update verbessert die Stadt Garbsen App für Sie dank besserer Leistung und behobener Programmfehler. |
| **Installs**  | 500+ |
| **Category** | Nachrichten & Zeitschriften |
| **First release** | 30.03.2020 |
| **Size**  | 33M |
| **Supported Android version**  | 5.0 oder höher |

### Description
> Diese App bietet ihnen aktuelle Informationen der Stadtverwaltung. Es handelt sich um die offizielle App der Stadt Garbsen.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | RGC Manager GmbH & Co. KG |
| **Website**  | [https://www.garbsen.de/](https://www.garbsen.de/) |
| **Email** | pressestelle@garbsen.de |
| **Physical address**  | [Drostestraße 16 30161 Hannover](https://www.google.com/maps/search/Drostestraße%2016%2030161%20Hannover) (Google Maps) |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=RGC+Manager+GmbH+%26+Co.+KG](https://play.google.com/store/apps/developer?id=RGC+Manager+GmbH+%26+Co.+KG) |

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
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>ACCESS_NOTIFICATION_POLICY** | Normal | Marker permission for applications that wish to access notification policy. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>READ_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to read from external storage. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
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
 | hellofomo.org | Registrant State/Province: | :de: DE | 2017-08-31 22:44:44 |
 | dashif.org | VTM Group | :us: US | 2012-04-27 13:02:46 |
 | w3.org | W3C | :us: US | 1994-07-06 04:00:00 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | googleadservices.com | Google LLC | :us: US | 2003-06-19 16:34:53 |
 | rgc-manager.de | - | - | - |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the ISO country code equivalent of the current registered operator's MCC (Mobile Country Code)<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Code execution**
> - This application loads a native library<br>
> - This application loads a native library: 'jniPdfium'<br>
> - This application loads a native library: 'modft2'<br>
> - This application loads a native library: 'modpdfium'<br>
> - This application loads a native library: 'modpng'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The Stadt Garbsen app has been installed by more than **500** times. At this time, **5** rated the app and its average score is **2.8**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 2

:star::star::star::star:: 0

:star::star::star:: 0

:star::star:: 1

:star:: 2

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="de.stadtgarbsen.hellofomo 5 reviews"/>
</p>

> Top!<br> :date: __2020-05-03 15:35:25__

> Ich weiß gar nicht was ihr so rum nörgelt. Die app ist technisch super und das die Inhalte dieselben wie auf der Website sind finde ich nicht schlimm, da ich diese jetzt entspannt auf meinem Handy genießen kann. Außerdem werde ich benachrichtigt wenn es etwas wichtiges gibt und muss nicht aktiv nachschauen.<br> :date: __2020-04-21 20:11:27__



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
<img src="2_star_reviews_wordcloud.png" alt="de.stadtgarbsen.hellofomo 2 reviews"/>
</p>

> Die App bietet die gleichen Informationen vom Internetauftritt der Stadt Garbsen. Die Push-Nachricht bringt die "aktuellsten Meldungen" der Stadt Garbsen - diese sind im Bereich Corona aber langsamer als KATWARN oder NINA. Belegt 58MB im Smartphone Speicher und braucht ne durchgehende Internetverbindung.<br> :date: __2020-04-21 18:17:52__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="de.stadtgarbsen.hellofomo 1 reviews"/>
</p>

> Die Seite wird zu selten aktualisiert. Die interessanten Nachrichten sucht man besser in der Tageszeitung.<br> :date: __2020-09-30 15:50:02__

> Diese app ist eigentlich sinnlos und nicht brauchbar. Uralte Informationen (z.T. älter als 5 bis 10 Tage) für mich völlig ungeeignet. Entweder komplett neu überdenken oder einfach entfernen. Mich als Abonnenten haben sie jedenfalls verloren. Da war ja die gedruckte Version der HAZ von heute morgen aktueller und interessanter. Es gibt einen schönen Spruch aus der Zeitungswelt, es gibt nichts uninteressanteres als die Zeitung von gestern. Den Stern gab es nur um Posten zu können<br> :date: __2020-05-07 13:57:49__


