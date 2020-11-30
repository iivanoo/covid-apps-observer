# Guam Covid Alert
App version ``1.0.10``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="Guam Covid Alert icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Guam Covid Alert |
| **Unique identifier** | org.pathcheck.guam.bt |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=org.pathcheck.guam.bt](https://play.google.com/store/apps/details?id=org.pathcheck.guam.bt) |
| **Summary**  | Receive alerts about potential exposure to COVID-19 in Guam. |
| **Privacy policy** | [https://guamcovidalert.guam.gov/privacy-policy/](https://guamcovidalert.guam.gov/privacy-policy/) |
| **Latest version** | 1.0.10 |
| **Last update** | 2020-11-17 04:34:09 |
| **Recent changes** | - New Home Screen and Navigation<br>- Priority Polling for Exposure History Jobs<br>- Accessibility Updates |
| **Installs**  | 5,000+ |
| **Category** | Health & Fitness |
| **First release** | Sep 8, 2020 |
| **Size**  | 65M |
| **Supported Android version**  | 6.0 and up |

### Description
> Guam Covid Alert, an app by the Guam Department of Public Health and Social Services helps aid contact tracing for COVID-19 by using the privacy centric Exposure Notification System. Subscribe to Healthcare Authorities in your area for information about COVID-19 near you, where available.
<br>Receive alerts from the local Healthcare Authority with information about potential exposure to COVID-19.
<br>The goal of Guam Covid Alert by the Guam Department of Public Health and Social Services is to help enable the reemergence and re-opening of economies and communities. Through global partnerships, we are prepared to support public health officials everywhere in the effort to slow the spread of COVID-19.
<br>The Guam Covid Alert app was built using an open source project developed by PathCheck Foundation.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 


## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Otech Developer |
| **Website**  | [https://guamcovidalert.guam.gov/](https://guamcovidalert.guam.gov/) |
| **Email** | developer@dma.guam.gov |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Otech+Developer](https://play.google.com/store/apps/developer?id=Otech+Developer) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | - |
| **Effective target Android version**  | - |
| **Minimum supported Android version**  | Marshmallow, version 6.0 (API level 23) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>ACCESS_WIFI_STATE** | Normal | Allows applications to access information about Wi-Fi networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>VIBRATE** | Normal | Allows access to the vibrator. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | bugsnag.com | Bugsnag Inc. | GB | 2011-08-18 03:26:10 |
 | android.com | Google LLC | :us: US | 1997-06-23 04:00:00 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | github.com | GitHub, Inc. | :us: US | 2007-10-09 18:20:50 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the ': connect, resolve' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'No route to  ' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Pim data leakage**
> - This application accesses data stored in the clipboard<br>

**Code execution**
> - This application loads a native library<br>
> - This application executes a UNIX command<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The Guam Covid Alert app has been installed by more than **5000** times. At this time, **43** rated the app and its average score is **4.3023257**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 30

:star::star::star::star:: 5

:star::star::star:: 2

:star::star:: 3

:star:: 3

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="org.pathcheck.guam.bt 5 reviews"/>
</p>

> Google<br> :date: __2020-11-01 21:04:08__

> Great to have and keeps us alert for COVID virus<br> :date: __2020-10-19 07:47:15__

> My president BT said her dad can choose who will die so I have to vote 5 stars for this. Otherwise it's a pretty good app<br> :date: __2020-10-18 16:14:04__

> 💙💙💙<br> :date: __2020-10-05 02:24:55__

> It does what's it supposed to. I feel better knowing this app is available to help If the need arises.<br> :date: __2020-09-28 09:47:53__

> Cool, whatever helps, even if the app isn't what everybody expected, atleast it's a value and can probably get you started on preperation.<br> :date: __2020-09-27 02:44:47__

> The best!<br> :date: __2020-09-15 11:11:33__

> Easy onboarding<br> :date: __2020-09-14 07:47:45__

> *Love* the design and ease of installation. Good job Guam and Path Check Foundation! Bias toward action. I like the transparency around privacy, but I wish there were external links to a credible audit of the open source code so that the in-app marketing assertions could be 3rd-party verified. I don't live in Guam and don't work as a Path Check developer, so I can't judge how the EN functionality works, but as an interested consumer, I say thumbs up.<br> :date: __2020-09-11 19:29:00__



#### 4-star reviews

<p align="center">

</p>

No recent reviews available with 4 stars.

#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="org.pathcheck.guam.bt 3 reviews"/>
</p>

> Not from Guam works fine<br> :date: __2020-11-29 13:22:18__

> HOW WILL I KNOW WHEN SOMEONE IS INFECTED? I ALWAYS HAVE TO KEEP MY BLUETOOTH ON. I WISH THIS APP WILL LET ME KNOW IF SOMEONE NEXT TOO ME IS INFECTED WITH COVID-19.<br> :date: __2020-10-01 11:11:11__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="org.pathcheck.guam.bt 2 reviews"/>
</p>

> I'm just curious as to why Bluetooth has to be turned on<br> :date: __2020-10-08 23:35:34__

> It doesn't open<br> :date: __2020-09-22 13:24:07__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="org.pathcheck.guam.bt 1 reviews"/>
</p>

> Do people really think someone positive would report it in this app for nearby people to know<br> :date: __2020-09-12 01:55:52__

> The app won't open<br> :date: __2020-09-10 05:36:45__


