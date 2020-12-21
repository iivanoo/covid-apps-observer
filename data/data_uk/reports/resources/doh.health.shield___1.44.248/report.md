# ALHOSN UAE
App version ``1.44.248``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="ALHOSN UAE icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | ALHOSN UAE |
| **Unique identifier** | doh.health.shield |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=doh.health.shield](https://play.google.com/store/apps/details?id=doh.health.shield) |
| **Summary**  | ALHOSN UAE allows you to keep your COVID-19 results on your mobile device |
| **Privacy policy** | [https://alhosnapp.ae/en/privacy-policy/](https://alhosnapp.ae/en/privacy-policy/) |
| **Latest version** | 1.44.248 |
| **Last update** | 2020-11-10 11:38:29 |
| **Recent changes** | - Improved user experience<br>- App stability |
| **Installs**  | 1,000,000+ |
| **Category** | Medical |
| **First release** | Apr 7, 2020 |
| **Size**  | 12M |
| **Supported Android version**  | 5.0 and up |

### Description
> The ALHOSN UAE app is the official COVID-19 testing channel for health authorities in the United Arab Emirates, by the Ministry of Health and Prevention.
<br>By using the app, everyone can help stop the spread of COVID-19 and keep their family and friends safe.
<br> 
<br>You can receive your COVID-19 test results directly on your phone with a unique QR code that is proof of your status and that of everyone else around you who also have the app, giving you peace of mind that you can safely interact.
<br>The app can also help trace people who may have come within close proximity to confirmed COVID-19 cases for an extended period of time. It uses short-distance Bluetooth signals to determine when your phone is near another phone that also has the app installed.  Both phones exchange anonymized IDs which are then stored in encrypted form on your phone. Using the anonymized IDs, health authorities can quickly identify and contact people at risk of infection so they can be retested.
<br> 
<br>Put your health in your hands with 3 easy steps:
<br>1.      Download the ALHOSN UAE app
<br>2.      Authenticate with your Emirates ID and phone number
<br>3.      Turn on Bluetooth and push notifications on your smartphone
<br> 
<br>Download the ALHOSN UAE app today and share it with your family and friends.
<br>Together, we can stop the spread of COVID-19
<br>Safer Together.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Ministry of Health and Prevention - UAE |
| **Website**  | [https://alhosnapp.ae/en/contact-us/](https://alhosnapp.ae/en/contact-us/) |
| **Email** | info@alhosnapp.ae |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Ministry+of+Health+and+Prevention+-+UAE](https://play.google.com/store/apps/developer?id=Ministry+of+Health+and+Prevention+-+UAE) |

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
 **android.permission<br>ACCESS_BACKGROUND_LOCATION** | :warning:**Dangerous** | Allows an app to access location in the background. 
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>BLUETOOTH_ADMIN** | Normal | Allows applications to discover and pair bluetooth devices. 
 **android.permission<br>CAMERA** | :warning:**Dangerous** | Required to be able to access the camera device. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>QUICKBOOT_POWERON** | - | - 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>REQUEST_IGNORE_BATTERY_OPTIMIZATIONS** | Normal | Permission an application must hold in order to use Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **android.permission<br>WRITE_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to write to external storage. 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | adobe.com | Adobe Inc. | :us: US | 1986-11-17 05:00:00 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | healthshielduae.com | Domains By Proxy, LLC | :us: US | 2020-03-31 19:30:02 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address 'Li/b/a/a/a;->f(Ljava/lang/String;)Ljava/lang/StringBuilder;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'hostname == null ' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Code execution**
> - This application loads a native library<br>
> - This application loads a native library: 'tool-checker'<br>
> - This application executes a UNIX command<br>
> - This application executes a UNIX command containing this argument: 'getprop'<br>
> - This application executes a UNIX command containing this argument: 'mount'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The ALHOSN UAE app has been installed by more than **1000000** times. At this time, **6085** rated the app and its average score is **4.3555193**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 4545

:star::star::star::star:: 543

:star::star::star:: 266

:star::star:: 79

:star:: 652

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="doh.health.shield 5 reviews"/>
</p>

> Good<br> :date: __2020-12-20 16:29:50__

> Convenient<br> :date: __2020-12-20 15:36:14__

> Very good results<br> :date: __2020-12-20 12:39:38__

> Nice<br> :date: __2020-12-20 08:38:31__

> Very good<br> :date: __2020-12-20 05:01:31__

> Very good<br> :date: __2020-12-19 16:12:20__

> Good app<br> :date: __2020-12-19 15:57:40__

> Very useful<br> :date: __2020-12-19 15:47:16__

> Nice and helpful app<br> :date: __2020-12-19 13:40:49__

> 100% Trust<br> :date: __2020-12-19 12:24:48__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="doh.health.shield 4 reviews"/>
</p>

> Best way<br> :date: __2020-12-20 06:55:11__

> Very good<br> :date: __2020-12-19 08:33:26__

> Good<br> :date: __2020-12-16 11:33:48__

> good 👍<br> :date: __2020-12-16 06:27:52__

> Good<br> :date: __2020-12-14 19:42:45__

> very good app<br> :date: __2020-12-13 08:31:28__

> UAE always good<br> :date: __2020-12-13 05:55:28__

> Good<br> :date: __2020-12-12 12:46:31__

> Good<br> :date: __2020-12-12 07:03:49__

> Good<br> :date: __2020-12-11 14:25:45__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="doh.health.shield 3 reviews"/>
</p>

> Super<br> :date: __2020-12-18 11:45:39__

> Dear All, plz confirm if this app is working outside UAE or not? For me it is just showing first loading page only.<br> :date: __2020-12-17 21:02:36__

> Hi. I have a problem with the app. I have installed it on my phone but the app stays on home screen only and I am supposed to fly to UAE in a couple of days . What will happen if the app doesn't work on my phone? Do I have to buy a new phone in order to be allowed entry into the country? Can someone please give me some answers. I don't know who to contact about this . Thank you<br> :date: __2020-12-13 14:12:12__

> Good<br> :date: __2020-12-11 12:55:07__

> Why my photo won't appear in the app?<br> :date: __2020-12-10 19:45:41__

> Good<br> :date: __2020-12-10 09:05:54__

> Did covid test at al zahra hospital sharjah but it was not registered on the alhosn app even though it was negative it should have been shown in app. Please instruct al zahra hosp sharjah esp Nmc group hospitals to register all covid tests or this app will soon become useless<br> :date: __2020-11-30 05:37:08__

> It's very frustrating that you cannot register with your number from day one. it always tell me to register with the number which I never use.. even calling several times to customer support they says check after sometime but no result..<br> :date: __2020-11-29 17:05:27__

> I just received the text message result. I wanna download the result document n need to upload to my HR portal. I just login to the app with the emirates ID and phone number. The current result is not reflecting.<br> :date: __2020-11-21 07:44:11__

> Not updating to vaccinated status. No one answering the al hosn support nor email not working.<br> :date: __2020-11-20 22:19:28__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="doh.health.shield 2 reviews"/>
</p>

> Every time asking update why<br> :date: __2020-12-20 17:16:51__

> حسنه<br> :date: __2020-12-17 21:45:18__

> وجود خلل في تحديث البيانات المستحدثة<br> :date: __2020-12-17 06:58:04__

> Some times take long time to have the result<br> :date: __2020-12-16 23:00:00__

> raju hain.<br> :date: __2020-12-16 20:45:18__

> Why not working after no options come when singn id nd Number nd code<br> :date: __2020-12-01 14:02:54__

> It always says that, the mobile number linked with my Emirates Id is in correct. How to rectify this?<br> :date: __2020-11-30 05:53:10__

> Very slow.<br> :date: __2020-11-23 19:42:34__

> The latest update is unstable (frequently hanging) and also no longer shows how many days have past since the last testing date. With the previous version, the user/inspector can easily see how many days have passed since the last COVID19 test. In latest version, if you access the result after some time (4 days in my experience) it will just say "Negative - Expired". In the previous version, it would say "Negative for 4 days"..<br> :date: __2020-11-22 10:04:15__

> I can't open the app with mobile data or Wi-Fi I'm still out side the Country and I'm facing this issue<br> :date: __2020-11-18 14:16:54__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="doh.health.shield 1 reviews"/>
</p>

> Its ok<br> :date: __2020-12-20 16:37:49__

> I try to open the app,but I was not able to enter the app<br> :date: __2020-12-20 14:29:43__

> My app hang why<br> :date: __2020-12-20 14:26:04__

> My app is not opening up and I need to travel tomorrow can anyone help out<br> :date: __2020-12-20 08:36:38__

> It takes long way to start<br> :date: __2020-12-19 19:23:36__

> I kept waiting for one time code during login, tried multiple times, no message ever.<br> :date: __2020-12-19 17:47:51__

> Doesn't work<br> :date: __2020-12-19 06:18:39__

> Why this app is not working? How to operate this app?<br> :date: __2020-12-19 05:26:08__

> The App doesn't work, its stuck at the very first page.<br> :date: __2020-12-18 15:43:46__

> The app keeps stopping. Tried to resikve with an it specialist in all ways? Still to no avail.<br> :date: __2020-12-18 06:29:24__


