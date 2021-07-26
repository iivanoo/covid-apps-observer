# Coalition App | #StopCovid19
App version ``2.0.1``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="Coalition App | #StopCovid19 icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Coalition App | #StopCovid19 |
| **Unique identifier** | world.coalition.app |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=world.coalition.app](https://play.google.com/store/apps/details?id=world.coalition.app) |
| **Summary**  | Global, privacy-first contact tracing app to help stop the spread of COVID-19 |
| **Privacy policy** | [https://www.coalitionnetwork.org/privacy-policy](https://www.coalitionnetwork.org/privacy-policy) |
| **Latest version** | 2.0.1 |
| **Last update** | 2020-06-17 18:28:31 |
| **Recent changes** | - Minor bug fixes<br>- Support languages: Spanish, French, Portuguese (Brazilian), Arabic, Russian, Ukrainian, Polish, Swahili, German, Indonesian, Chinese, Greek, Turkish, Thai, Vietnamese, Tagalog, Hebrew |
| **Installs**  | 1,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 14, 2020 |
| **Size**  | 5.2M |
| **Supported Android version**  | 6.0 and up |

### Description
> Coalition is a global, privacy by design, contact tracing app to stop the spread of COVID-19.
<br>The Coalition App alerts you if you have crossed paths or spent time with another user showing symptoms, or those who have tested positive for the virus.
<br>Instead of using your location data, Coalition uses secured bluetooth to protect your privacy.  Your information stays anonymous and private, and isn't shared with anyone without your permission.
<br>Only when you confirm that you are sick, does Coalition share an anonymous ID with others who you have come into contact with.
<br>We believe that citizens can help fight pandemics without giving up their privacy, Coalition is the first step to a pandemic free future.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 


## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Nodle |
| **Website**  | [https://www.coalitionnetwork.org/](https://www.coalitionnetwork.org/) |
| **Email** | contact@coalitionnetwork.org |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Nodle](https://play.google.com/store/apps/developer?id=Nodle) |

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
 **android.permission<br>ACCESS_BACKGROUND_LOCATION** | :warning:**Dangerous** | Allows an app to access location in the background. 
 **android.permission<br>ACCESS_COARSE_LOCATION** | :warning:**Dangerous** | Allows an app to access approximate location. 
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>BLUETOOTH_ADMIN** | Normal | Allows applications to discover and pair bluetooth devices. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 
 **com.google.android.finsky.permission<br>BIND_GET_INSTALL_REFERRER_SERVICE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | googlesyndication.com | Google LLC | :us: US | 2003-01-21 06:17:24 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | app-measurement.com | Google LLC | :us: US | 2015-06-19 20:13:31 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | crashlytics.com | Google LLC | :us: US | 2011-01-21 15:30:40 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | googleadservices.com | Google LLC | :us: US | 2003-06-19 16:34:53 |
 | covid19api.com | WhoisGuard, Inc. | PA | 2020-03-13 11:54:47 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the ISO country code equivalent for the SIM provider's country code<br>
> - This application reads the ISO country code equivalent of the current registered operator's MCC (Mobile Country Code)<br>

**Location lookup**
> - This application reads location information from all available providers (WiFi, GPS etc.)<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address ': ; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ln/b/a/a/a;->a(Ljava/lang/String;)Ljava/lang/StringBuilder;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The Coalition App | #StopCovid19 app has been installed by more than **1000** times. At this time, **21** rated the app and its average score is **4.2380953**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 17

:star::star::star::star:: 0

:star::star::star:: 0

:star::star:: 0

:star:: 4

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="world.coalition.app 5 reviews"/>
</p>

> 👍<br> :date: __2021-07-23 09:22:08__

> It's a shame more people aren't downloading this app! It's also a problem when I search Google play store for COVID-19 apps and they only show 2 apps that aren't even for my area. I appreciate you and your team for helping with the issue 🙏<br> :date: __2020-07-29 18:18:00__

> Good concept and technology behind. Only a minor downside with some phone models draining the battwry but I see they are working to fix the issues.<br> :date: __2020-04-30 06:18:54__

> I like the level of privacy assured and I recommended it on NextDoor. But I have a question. As long as people are sheltered in place it won't be too bad, but even now: say you notify everyone who crosses paths with an infected person. All those people are going to want to be tested, naturally. Are tests available in that amount? And if someone is asymptomatic, how long are they contagious? I'll google it, but I like the idea of app, as a cautious UberEats delivery driver. SF Chron 👍<br> :date: __2020-04-25 02:24:34__

> The app we all need for reliable contact-tracing with security and privacy in mind.<br> :date: __2020-04-20 03:51:18__

> Privacy and security oriented tracker especially useful during pandemics.<br> :date: __2020-04-20 03:49:59__



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
<img src="2_star_reviews_wordcloud.png" alt="world.coalition.app 2 reviews"/>
</p>

> The app doesn't use Google's Exposure Notifications API, and therefore does nothing. The app is otherwise okay.<br> :date: __2021-02-17 13:36:29__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="world.coalition.app 1 reviews"/>
</p>

> Micha Benoliel - Do you go stalking everyone who leaves a negative review about your products? I know you visited my linkedin, so I guess you visited all my other social profiles. Privacy isn't much of a concern to you or your company. I definitly came to the right conclusion about this app. I saw your previous reply before you deleted it. I'm just a user. Your behaviour is disgusting. I'm reporting you to Google.<br> :date: __2020-05-03 01:33:33__


