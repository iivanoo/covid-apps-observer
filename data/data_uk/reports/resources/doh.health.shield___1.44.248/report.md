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

> very effective<br> :date: __2020-11-29 16:41:41__

> Uhj<br> :date: __2020-11-29 16:07:02__

> Very useful this apps thanks!<br> :date: __2020-11-29 14:48:46__

> Bihgf<br> :date: __2020-11-29 09:35:56__

> Ease my work<br> :date: __2020-11-28 15:10:20__

> Easy and good<br> :date: __2020-11-28 12:35:40__

> Good<br> :date: __2020-11-27 15:08:53__

> Very good app<br> :date: __2020-11-27 13:50:08__

> Thank<br> :date: __2020-11-27 11:16:41__

> Great<br> :date: __2020-11-27 01:25:28__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="doh.health.shield 4 reviews"/>
</p>

> Good<br> :date: __2020-11-25 09:09:03__

> Good service<br> :date: __2020-11-17 10:53:49__

> It is hard to open the application<br> :date: __2020-11-14 15:22:10__

> Free testing centre of covid 19 testing<br> :date: __2020-11-14 07:21:24__

> Working fine just open location blootooth charging it's working.<br> :date: __2020-11-08 17:53:37__

> Good<br> :date: __2020-11-06 08:02:29__

> Good apps for me<br> :date: __2020-11-06 07:47:50__

> Good<br> :date: __2020-11-04 18:01:37__

> nice<br> :date: __2020-11-03 20:12:28__

> great app<br> :date: __2020-11-02 13:46:34__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="doh.health.shield 3 reviews"/>
</p>

> Did covid test at al zahra hospital sharjah but it was not registered on the alhosn app even though it was negative it should have been shown in app. Please instruct al zahra hosp sharjah esp Nmc group hospitals to register all covid tests or this app will soon become useless<br> :date: __2020-11-30 05:37:08__

> It's very frustrating that you cannot register with your number from day one. it always tell me to register with the number which I never use.. even calling several times to customer support they says check after sometime but no result..<br> :date: __2020-11-29 17:05:27__

> I just received the text message result. I wanna download the result document n need to upload to my HR portal. I just login to the app with the emirates ID and phone number. The current result is not reflecting.<br> :date: __2020-11-21 07:44:11__

> Not updating to vaccinated status. No one answering the al hosn support nor email not working.<br> :date: __2020-11-20 22:19:28__

> App crash. Can't open apps it's crash always<br> :date: __2020-11-16 20:03:12__

> It is ok I guess<br> :date: __2020-11-16 08:57:46__

> Hello i had pcr test yesterday and my result still not receive,anyone can help me my alhons not updated.<br> :date: __2020-11-11 08:48:20__

> Unable to register. Just a blank screen on opening the app .<br> :date: __2020-11-10 13:15:49__

> DPR Tests from dubai don't show here<br> :date: __2020-11-10 08:35:44__

> Update not ready<br> :date: __2020-11-08 07:05:38__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="doh.health.shield 2 reviews"/>
</p>

> It always says that, the mobile number linked with my Emirates Id is in correct. How to rectify this?<br> :date: __2020-11-30 05:53:10__

> Very slow.<br> :date: __2020-11-23 19:42:34__

> The latest update is unstable (frequently hanging) and also no longer shows how many days have past since the last testing date. With the previous version, the user/inspector can easily see how many days have passed since the last COVID19 test. In latest version, if you access the result after some time (4 days in my experience) it will just say "Negative - Expired". In the previous version, it would say "Negative for 4 days"..<br> :date: __2020-11-22 10:04:15__

> I can't open the app with mobile data or Wi-Fi I'm still out side the Country and I'm facing this issue<br> :date: __2020-11-18 14:16:54__

> App is very slow<br> :date: __2020-11-12 18:32:40__

> I couldnt check my status, and no option to answer pre survey..This app is not compatible with my mobile..please fix the issue, thank you<br> :date: __2020-11-11 13:56:02__

> Hello. This is a last resort from my side. I've done my pcr test last week and to date it has not been updated in the app. I've received the result via SMS too. I've called your hotline and they've promised it'll reflect by max yesterday. And still nothing. Please help.<br> :date: __2020-11-09 09:14:57__

> Good<br> :date: __2020-11-08 15:28:22__

> not moving to submit not abal to get result<br> :date: __2020-11-08 09:35:22__

> Battery usage is verh high while running this application<br> :date: __2020-11-05 11:36:27__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="doh.health.shield 1 reviews"/>
</p>

> Not working on samsung A8 had many time installed. But no use<br> :date: __2020-11-29 14:30:52__

> The app doesn't work at all.<br> :date: __2020-11-29 07:18:50__

> Not good<br> :date: __2020-11-29 06:02:41__

> This apps not working only green wallpaper. nothing else.<br> :date: __2020-11-28 15:40:13__

> It shows your number is not registered and shows two mobile numbers I have never seen, Coustomer care is not useful at all.<br> :date: __2020-11-28 13:53:20__

> Pathetic , App doesn't go beyond logo . Surprised how it's got 4.3 star rating with so many 1 star feedback. I would give 0 star if possible.<br> :date: __2020-11-28 04:50:42__

> I can't open this app..<br> :date: __2020-11-27 11:46:54__

> useless apps... no results showing... it's two days past but still no results.<br> :date: __2020-11-27 06:50:16__

> I am a covid vaccine volunteer and even after PCR I don't have the Volunteer status... And everytime I call the help line they answer but after hello they hangup on me very unprofessional they need to hire professional staff... Horrible experience after being on hold for 20 minutes they hangup this is frustrating<br> :date: __2020-11-26 06:23:50__

> It is not opening although<br> :date: __2020-11-25 17:14:02__


