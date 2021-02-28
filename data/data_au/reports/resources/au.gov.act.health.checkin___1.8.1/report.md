# Check In CBR
App version ``1.8.1``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="Check In CBR icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Check In CBR |
| **Unique identifier** | au.gov.act.health.checkin |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=au.gov.act.health.checkin](https://play.google.com/store/apps/details?id=au.gov.act.health.checkin) |
| **Summary**  | Fast, secure check in to Canberra businesses to support COVID-19 contact tracing |
| **Privacy policy** | [https://www.health.act.gov.au/privacy](https://www.health.act.gov.au/privacy) |
| **Latest version** | 1.8.1 |
| **Last update** | 2021-02-25 10:26:43 |
| **Recent changes** | Bug fixes and improvements |
| **Installs**  | 100,000+ |
| **Category** | Health & Fitness |
| **First release** | Aug 31, 2020 |
| **Size**  | 32M |
| **Supported Android version**  | 5.0 and up |

### Description
> Quickly and securely check in to a business in Canberra, Australia to support COVID-19 contact tracing. Simply scan the QR code displayed at the business, and you're done! 
<br>Your personal details are saved securely with ACT Government Health Directorate for the sole purpose of contact tracing.


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
| **Developer**  | ACT Health |
| **Website**  | [https://covid19.act.gov.au/business-and-work/check-in-cbr](https://covid19.act.gov.au/business-and-work/check-in-cbr) |
| **Email** | Digital.Support@act.gov.au |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=ACT+Health](https://play.google.com/store/apps/developer?id=ACT+Health) |

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
 **android.permission<br>CAMERA** | :warning:**Dangerous** | Required to be able to access the camera device. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>VIBRATE** | Normal | Allows access to the vibrator. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **com.google.android.finsky.permission<br>BIND_GET_INSTALL_REFERRER_SERVICE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | android.com | Google LLC | :us: US | 1997-06-23 04:00:00 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | cloudfront.net | Amazon.com, Inc. | :us: US | 2008-04-25 18:25:49 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Audio video eavesdropping**
> - This application records audio from the 'CAMCORDER' source <br>
> - This application records audio from the 'MIC' source <br>
> - This application captures video from the 'CAMERA' source<br>
> - This application captures video from the 'SURFACE' source<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the ': connect, resolve' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Pim data leakage**
> - This application accesses data stored in the clipboard<br>

**Code execution**
> - This application loads a native library<br>
> - This application loads a native library: 'Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;'<br>
> - This application executes a UNIX command<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The Check In CBR app has been installed by more than **100000** times. At this time, **124** rated the app and its average score is **2.3762376**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 28

:star::star::star::star:: 10

:star::star::star:: 8

:star::star:: 11

:star:: 67

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.act.health.checkin 5 reviews"/>
</p>

> Easy to use.<br> :date: __2021-02-22 08:09:10__

> This app works well. Should be used all across Australia.<br> :date: __2021-01-24 23:29:37__

> Cool app! I prefer this much more than writing my name down with a pen 50 other people have used that day. Great to see more places in Canberra are using it too.<br> :date: __2020-12-08 02:50:38__

> Red es DVR DVR you vf you have any other information you can get the best regards<br> :date: __2020-11-29 09:24:49__

> Used it a few times at the library, worked quickly, easily, and without issue. Wish more places would use this.<br> :date: __2020-11-10 07:32:34__

> Now that you remember frequent guests (eg, my husband) it takes under 5 seconds to check in. Great job.<br> :date: __2020-10-29 02:09:59__

> Good job Canberra! This is more in line with the privacy requirements than signing a sheet of paper.<br> :date: __2020-10-16 02:40:40__

> Works really well, much better than using a google form<br> :date: __2020-10-06 11:10:27__

> Easy to use but don't just scan QR and expect app to open. The QR does nothing but open a website, thats what they mostly do. Scanning a QR will just take you to website to download. It will not open app. Once I downloaded app and added my details, I clicked check in and then I scanned the QR (after giving app permission) Easy.<br> :date: __2020-10-05 02:41:02__

> Quick and easy to use, really good!<br> :date: __2020-09-27 10:53:21__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.act.health.checkin 4 reviews"/>
</p>

> Once loaded this app is easy to use, so much easier than NSW or Vic!<br> :date: __2021-02-26 00:06:07__

> Was easy to install particularly for a tech challenged person. Only issue is that does not allow me to check out unlike the nsw app<br> :date: __2021-02-12 01:47:53__

> App makes check-in easy and I like how it remembers dependents for easy future check-ins. Would be nice if locations you frequented could be remembered and used in the same way for easy repeat check-ins without needing a code or to huddle around a QR code that someone had posted on the wall.<br> :date: __2021-01-14 07:37:19__

> Its missing a checkout button to end ur visit to a place. It needs a time out to ensure correct contact tracing<br> :date: __2020-12-09 02:30:00__

> First try today - so very relieved to have no issues at Restaurant. Guess there's no need to checkout on departure?<br> :date: __2020-12-04 03:55:33__

> Not enough businesses on it. Many still using pen and paper.<br> :date: __2020-10-17 05:00:51__

> Samsung GS7 will not scan QR code. App has camera permission enabled. Phone will scan QR codes, but not in this app. Fixed! Thanks! App now returns "Not a check in CBR code" on invalid QR scans<br> :date: __2020-10-02 04:18:26__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.act.health.checkin 3 reviews"/>
</p>

> The graphics are too dark under some lighting.<br> :date: __2021-02-08 01:44:49__

> It works for scanning the QR code. But I can offarhim why do I have to reenter all my personal details everytime I use the app for myself on my phone. The nswservices app handles this very well. Please start considering the user when you write mobile apps. Many miss some simple things that would make many people's lives better. I hatdusing this app.<br> :date: __2021-02-05 20:04:05__

> Takes ages to open the camera scanner function.<br> :date: __2020-12-09 09:13:41__

> Seems to work ok. Slow to load, requiring data connection to do so. Cannot access QR code scanner without data connection. Suggest allowing access to QR code scanner without needing data connection to allow check in, uploading locations when data becomes available.<br> :date: __2020-12-05 21:58:59__

> Would be better if you could check in by typing name of check-in place, geolocation, or select from previous check-in history.<br> :date: __2020-11-15 01:20:33__

> Works for some places, not others, it just says enter manually code<br> :date: __2020-10-08 23:36:53__

> The App has not changed to daylight savings.<br> :date: __2020-10-06 01:02:09__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.act.health.checkin 2 reviews"/>
</p>

> . , zebra V te zbb3f<br> :date: __2021-02-24 07:23:12__

> Asked me for my credit card why?. Why is not the new south Wales app ok to use.<br> :date: __2021-02-24 04:22:07__

> Slow to load, my history has no check ins, so does it even work? Isn't it supposed to keep a record of where I have checked in?<br> :date: __2021-02-23 02:03:11__

> ACT Health, why do you check in but not check out, like the NSW app? If something does happen you have no idea if a person spent 10 mins or 2 hrs at a place. To stop people forgetting to log out, how bout a popup asking if you are still there 2-3 hrs after checking in if not already logged out?<br> :date: __2021-02-11 22:05:59__

> Worked as intended before, but recently has become very slow to load and the qr scanner is not working<br> :date: __2021-01-22 22:29:39__

> Takes to long to download<br> :date: __2020-12-06 04:07:36__

> App fails to install, despite several attempts...says it is installed but goes back tp wil instal shortly.....<br> :date: __2020-11-11 09:29:39__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.act.health.checkin 1 reviews"/>
</p>

> Since the latest update, it is unusable - the app keeps stopping and fails to work.<br> :date: __2021-02-27 13:10:56__

> No longer works on my Samsung 7 edge<br> :date: __2021-02-27 13:03:13__

> The app will no longer open since latest update. I'm not sure how I am supposed to check in to places where it is compulsory!<br> :date: __2021-02-27 11:37:23__

> It won't download!! I started to install, but it was taking too long, so I went to bed. In the morning it was still trying to download<br> :date: __2021-02-27 11:28:49__

> Not working at all since last update. Have reinstalled but still not working.<br> :date: __2021-02-27 09:18:07__

> Crashes every time I try to open it 😡<br> :date: __2021-02-27 07:53:18__

> No longer working. Have uninstalled and reinstalled several times today with it still refusing to open. Previously it was glitchy but never this bad.<br> :date: __2021-02-27 06:25:37__

> Can't open it hence unable to even process manually.<br> :date: __2021-02-27 05:53:16__

> Continuosly fails to open, reinstalled twice but still fails to open. Displays error message 'CBR code has stopped'<br> :date: __2021-02-27 05:49:45__

> Can't get this version to launch<br> :date: __2021-02-27 05:38:54__


