# AlohaSafe Alert
App version ``1.0.12``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="AlohaSafe Alert icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | AlohaSafe Alert |
| **Unique identifier** | org.alohasafe.alert |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=org.alohasafe.alert](https://play.google.com/store/apps/details?id=org.alohasafe.alert) |
| **Summary**  | Official COVID-19 exposure notification app for the State of Hawaii |
| **Privacy policy** | [https://health.hawaii.gov/coronavirusdisease2019/alohasafe-alert/](https://health.hawaii.gov/coronavirusdisease2019/alohasafe-alert/) |
| **Latest version** | 1.0.12 |
| **Last update** | 2021-01-27 05:35:34 |
| **Recent changes** | Added COVID-19 summary metrics dashboard (replaces snapshot of county stats) |
| **Installs**  | 10,000+ |
| **Category** | Health & Fitness |
| **First release** | Nov 4, 2020 |
| **Size**  | 65M |
| **Supported Android version**  | 6.0 and up |

### Description
> AlohaSafe Alert is a voluntary new service that helps slow the spread of COVID-19. AlohaSafe Alert is the official exposure notification app of Hawaii and has been designed for use in Hawaii in coordination with the Hawaii State Department of Health.
<br>The goal of AlohaSafe Alert is to support the re-opening of Hawaii communities and economies.
<br>If you have enabled Exposure Notifications on your phone, whenever you are within close proximity (approximately 6 feet of someone for at least 15 minutes), your phones will exchange secure, anonymous tokens. If that person later tests positive for COVID-19, you will receive a notification about a possible exposure. If you test positive for COVID-19, you can share these anonymous tokens, which will send a notification to anyone with whom you have exchanged tokens recently, notifying them of possible exposure.
<br>This service has been designed for use in Hawaii. This service does not collect any personally identifying information or share it with the State of Hawaii, the Hawaii State Department of Health, Apple, or Google. AlohaSafe Alert is a source of up to date COVID-19 information & guidance. The AlohaSafe Alert app was built using the open source project developed by PathCheck Foundation.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/>  | <img src="screenshot_5.png" alt="screenshot" width="300"/>  | <img src="screenshot_6.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_7.png" alt="screenshot" width="300"/>  | <img src="screenshot_8.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Hawaii Department of Health |
| **Website**  | [https://health.hawaii.gov/](https://health.hawaii.gov/) |
| **Email** | doh.alohasafe@doh.hawaii.gov |
| **Physical address**  | [1250 Punchbowl St. Honolulu, HI  96813](https://www.google.com/maps/search/1250%20Punchbowl%20St.%20Honolulu,%20HI%2096813) (Google Maps) |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Hawaii+Department+of+Health](https://play.google.com/store/apps/developer?id=Hawaii+Department+of+Health) |

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
 | alohasafe.org | Contact Privacy Inc. Customer 1247641424 | :canada: CA | 2020-07-07 01:34:04 |
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

The AlohaSafe Alert app has been installed by more than **10000** times. At this time, **59** rated the app and its average score is **3.8644068**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 37

:star::star::star::star:: 4

:star::star::star:: 4

:star::star:: 1

:star:: 13

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="org.alohasafe.alert 5 reviews"/>
</p>

> At 10k downloads, roughly 0.71% of Hawaii's 1,416,000 population are using this app (unless my math is wrong). It's a great app, but more people need to know about it to be truly useful.<br> :date: __2021-02-05 09:51:33__

> Very thankful Hawaii has an app like this. It's straightforward and non-intrusive.<br> :date: __2021-02-02 12:32:58__

> It,s okay<br> :date: __2021-01-31 07:54:55__

> DeoGuinsatao<br> :date: __2021-01-30 20:01:10__

> No experience with this yet<br> :date: __2021-01-29 04:51:53__

> Easy to install. Like the concept.<br> :date: __2021-01-26 08:38:06__

> Easy access<br> :date: __2021-01-25 17:58:06__

> Very useful.<br> :date: __2021-01-24 03:19:46__

> How can you stay safe from the c_firus<br> :date: __2021-01-20 08:46:31__

> works as exactly designed to.<br> :date: __2021-01-17 12:51:54__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="org.alohasafe.alert 4 reviews"/>
</p>

> , .<br> :date: __2021-01-08 20:47:39__

> Easy, easy, easy. The app installed in seconds. There is NO setup. It doesn't ask for any input at all. You don't need a username, password, or email address. Just open the app, read the screens, and press the button to enable notifications. The whole process takes about 15 seconds, and then you never have to open the app again unless you receive notification that you may have been exposed to COVID-19.<br> :date: __2020-12-17 21:22:54__

> Works<br> :date: __2020-11-18 23:37:20__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="org.alohasafe.alert 3 reviews"/>
</p>

> Interesting app... Although with only around 5000+ downloads I'm not sure if the rate of population with this app installed is enough to achieve its intended purpose.<br> :date: __2021-01-22 09:37:13__

> Quick and easy Hope that more pplpz use this and let others know if get the virus by dem<br> :date: __2021-01-22 05:07:46__

> This app has a bug in it. On a moto 6 it grabs the Bluetooth and won't release it. So you have to reboot your phone to connect to your car's hands free system. It should also allow you to adjust exposure time. 15 mins is way too long given the higher contagion strain.<br> :date: __2021-01-21 22:11:42__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="org.alohasafe.alert 2 reviews"/>
</p>

> Got aloha safe app cause i live on maui, Hi and am worried about covid numbers rising dramaticly daily so i only activate it when im out grocery shopping or going to the doctors office or anywhere in public then i deactivate it cause it drains battery life and does weird things to my phones touch screen and interferes with other apps on my phone when its on<br> :date: __2021-02-04 18:06:22__

> Good idea ... But not yet ready for prime time, methinks. After I installed it, I could no longer use my Qardio Blood Pressure machine, which also communicates via Bluetooth. So I uninstalled this Nov. 30, 2020, and the Qardio app could connect again. Possibly a coincidence. I'll try this app again in a few weeks, after they've had a chance to iron out the wrinkles. Like I said ... a good idea ... assuming that the app attracts enough users to be useful. It'll need a lot.<br> :date: __2020-12-06 08:23:53__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="org.alohasafe.alert 1 reviews"/>
</p>

> Stupid<br> :date: __2021-02-03 18:15:43__

> Hope it works doesent sound great. Tbh<br> :date: __2021-01-29 19:42:46__

> Force install?!? Goodbye, deleted..<br> :date: __2021-01-29 15:21:42__

> unconstitutional mandatory download of app. infringement of rights. state of hawaii gov will be sued over this. developers of app should be ashamed of themselves.<br> :date: __2021-01-27 23:04:21__

> Horrible. Forced installed. UNSAFE!!!! UNINSTALLED!!! BEWARE<br> :date: __2021-01-24 10:32:51__

> This app downloaded itself on my phone do not trust this app at all. This is not okay.<br> :date: __2021-01-23 07:38:41__

> I can take care of myself as well as people around me. Don't need this. Shame on victorino for forcing.<br> :date: __2021-01-22 08:00:16__

> This app will never work! People who have covid-19 break quarantine all the time, you still see people not wearing mask, no ones checking on people in quarantine, everyone's still having gatherings with more then 10 ppl.. The list goes on... So don't download this it's worthless you'll never get a notification!<br> :date: __2021-01-18 05:14:49__

> Horrible APP. Not accessible to download on my ipad mini which I always carry. Don't have an apple phone, and it is not downloading on my Samsung phone. I find it offensive that Big Brother is tracking me. Will probably cancel my trip to Maui . Too much trouble yo go there.<br> :date: __2021-01-18 03:54:23__

> My mother is high risk so I felt this app was a great idea. I tried downloading it but it said I didn't have enough space. So I delete three apps that I don't need and some useless pictures. It still says I don't have enough space. So I check how much space I have and it says 615 MB, which should be more than enough to download the stupid app. I check and this app only requires 22MB. I try to redownload and it doesn't work again. Great concept but it won't even let me try it out.<br> :date: __2021-01-17 02:44:44__


