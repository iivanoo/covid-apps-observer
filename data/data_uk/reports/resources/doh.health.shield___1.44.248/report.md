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

> Good service<br> :date: __2020-12-13 18:14:15__

> Very helpful apps.<br> :date: __2020-12-13 13:22:37__

> Good ap<br> :date: __2020-12-13 12:08:48__

> It is great<br> :date: __2020-12-13 11:52:44__

> so fast wonderfull<br> :date: __2020-12-13 10:28:39__

> Good<br> :date: __2020-12-13 09:29:37__

> Good<br> :date: __2020-12-13 08:02:55__

> Exelent<br> :date: __2020-12-13 07:46:52__

> تحياتي لامارة ابوظبي والقائمين عليها<br> :date: __2020-12-13 07:28:24__

> Very good app<br> :date: __2020-12-13 05:53:24__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="doh.health.shield 4 reviews"/>
</p>

> very good app<br> :date: __2020-12-13 08:31:28__

> UAE always good<br> :date: __2020-12-13 05:55:28__

> Good<br> :date: __2020-12-12 12:46:31__

> Good<br> :date: __2020-12-12 07:03:49__

> Good<br> :date: __2020-12-11 14:25:45__

> Nice application to track the people around with specific eequirement<br> :date: __2020-12-10 10:32:02__

> I Need To Replace My Old Number, because Old Number Belongs to Some Ome Else. Now I Have My Own Number, Let Me Know How To Replace Thanks Team AlHosn<br> :date: __2020-12-09 08:37:35__

> Good<br> :date: __2020-12-07 20:52:05__

> Not able to go pass login<br> :date: __2020-12-06 19:14:37__

> It is a best tracing app.<br> :date: __2020-12-05 08:43:27__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="doh.health.shield 3 reviews"/>
</p>

> Hi. I have a problem with the app. I have installed it on my phone but the app stays on home screen only and I am supposed to fly to UAE in a couple of days . What will happen if the app doesn't work on my phone? Do I have to buy a new phone in order to be allowed entry into the country? Can someone please give me some answers. I don't know who to contact about this . Thank you<br> :date: __2020-12-13 14:12:12__

> Good<br> :date: __2020-12-11 12:55:07__

> Why my photo won't appear in the app?<br> :date: __2020-12-10 19:45:41__

> Good<br> :date: __2020-12-10 09:05:54__

> Did covid test at al zahra hospital sharjah but it was not registered on the alhosn app even though it was negative it should have been shown in app. Please instruct al zahra hosp sharjah esp Nmc group hospitals to register all covid tests or this app will soon become useless<br> :date: __2020-11-30 05:37:08__

> It's very frustrating that you cannot register with your number from day one. it always tell me to register with the number which I never use.. even calling several times to customer support they says check after sometime but no result..<br> :date: __2020-11-29 17:05:27__

> I just received the text message result. I wanna download the result document n need to upload to my HR portal. I just login to the app with the emirates ID and phone number. The current result is not reflecting.<br> :date: __2020-11-21 07:44:11__

> Not updating to vaccinated status. No one answering the al hosn support nor email not working.<br> :date: __2020-11-20 22:19:28__

> App crash. Can't open apps it's crash always<br> :date: __2020-11-16 20:03:12__

> It is ok I guess<br> :date: __2020-11-16 08:57:46__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="doh.health.shield 2 reviews"/>
</p>

> Why not working after no options come when singn id nd Number nd code<br> :date: __2020-12-01 14:02:54__

> It always says that, the mobile number linked with my Emirates Id is in correct. How to rectify this?<br> :date: __2020-11-30 05:53:10__

> Very slow.<br> :date: __2020-11-23 19:42:34__

> The latest update is unstable (frequently hanging) and also no longer shows how many days have past since the last testing date. With the previous version, the user/inspector can easily see how many days have passed since the last COVID19 test. In latest version, if you access the result after some time (4 days in my experience) it will just say "Negative - Expired". In the previous version, it would say "Negative for 4 days"..<br> :date: __2020-11-22 10:04:15__

> I can't open the app with mobile data or Wi-Fi I'm still out side the Country and I'm facing this issue<br> :date: __2020-11-18 14:16:54__

> App is very slow<br> :date: __2020-11-12 18:32:40__

> I couldnt check my status, and no option to answer pre survey..This app is not compatible with my mobile..please fix the issue, thank you<br> :date: __2020-11-11 13:56:02__

> Hello. This is a last resort from my side. I've done my pcr test last week and to date it has not been updated in the app. I've received the result via SMS too. I've called your hotline and they've promised it'll reflect by max yesterday. And still nothing. Please help.<br> :date: __2020-11-09 09:14:57__

> Good<br> :date: __2020-11-08 15:28:22__

> not moving to submit not abal to get result<br> :date: __2020-11-08 09:35:22__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="doh.health.shield 1 reviews"/>
</p>

> I downloaded this app at two different android devices but unable to open the app<br> :date: __2020-12-13 09:34:59__

> Not opening in huawei y9<br> :date: __2020-12-12 21:50:43__

> Not possible to change Bluetooth permission enabled<br> :date: __2020-12-12 11:24:12__

> Keep asking about my location even my location is on<br> :date: __2020-12-12 05:15:49__

> Why can't lodging In<br> :date: __2020-12-12 02:37:54__

> Am vaccine volunteer. Took my vaccine at adnec. Arrived today at abu Dhabi airport. There they didn't recognise the al hosn app and the volunteer star on al hosn app. They sent me to quarantine. There was a article published that vaccine volunteers are exempted from quarantine. struck here at razeen camp. No communication no updates. Covid test was performed at airport & its negative. Management here at razeen and airport has clearly denied looking into al hosn app.<br> :date: __2020-12-11 21:00:21__

> Not working outside the country<br> :date: __2020-12-11 18:37:17__

> Is complicated app<br> :date: __2020-12-11 06:10:40__

> Hosn app is down in pakistan<br> :date: __2020-12-11 05:16:39__

> Best<br> :date: __2020-12-09 13:17:22__


