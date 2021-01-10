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

> Excellent<br> :date: __2021-01-09 12:37:52__

> Best app<br> :date: __2021-01-09 12:33:59__

> Best way to stay safe and up-to-date<br> :date: __2021-01-09 12:06:49__

> Good app<br> :date: __2021-01-09 08:19:01__

> 👌<br> :date: __2021-01-09 04:38:20__

> ☝️<br> :date: __2021-01-08 18:15:27__

> Right time receiving result<br> :date: __2021-01-08 16:37:07__

> Good aap<br> :date: __2021-01-08 15:42:47__

> Nyc<br> :date: __2021-01-08 15:19:58__

> Very good<br> :date: __2021-01-08 11:02:54__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="doh.health.shield 4 reviews"/>
</p>

> Does what it says on the tin...would be better if you didn't have to have your location switch on to use it. Apart from that, no issues<br> :date: __2021-01-09 09:50:29__

> Very good<br> :date: __2021-01-06 18:10:20__

> َكطلفس٦ث<br> :date: __2021-01-05 13:38:10__

> Good<br> :date: __2021-01-03 20:28:16__

> Good<br> :date: __2021-01-03 09:25:31__

> V.good<br> :date: __2021-01-02 16:14:38__

> Found okay<br> :date: __2021-01-02 06:23:39__

> Excellent<br> :date: __2021-01-01 06:08:20__

> Good app<br> :date: __2020-12-26 14:50:44__

> The result is taking more time to get updated<br> :date: __2020-12-25 06:09:32__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="doh.health.shield 3 reviews"/>
</p>

> Ok<br> :date: __2021-01-06 22:19:14__

> Help me who ever cordinating it i want to change the number its still showing my old number which i am not able to asses any more<br> :date: __2021-01-06 09:28:01__

> My app is not working I took a test yesterday and I am trying too open my profile but it says error try later or contact customer service.<br> :date: __2021-01-05 05:17:24__

> useful<br> :date: __2020-12-31 16:56:18__

> Nice...<br> :date: __2020-12-25 02:24:19__

> The updated version is getting hanging..<br> :date: __2020-12-24 14:17:27__

> Excellent..<br> :date: __2020-12-21 05:19:25__

> Super<br> :date: __2020-12-18 11:45:39__

> Hi. I have a problem with the app. I have installed it on my phone but the app stays on home screen only and I am supposed to fly to UAE in a couple of days . What will happen if the app doesn't work on my phone? Do I have to buy a new phone in order to be allowed entry into the country? Can someone please give me some answers. I don't know who to contact about this . Thank you<br> :date: __2020-12-13 14:12:12__

> Good<br> :date: __2020-12-11 12:55:07__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="doh.health.shield 2 reviews"/>
</p>

> I know people using this app have way worse problems than I have but here is my take, I have one problem with the app why does it need my Bluetooth and location data all the time and why can't I make the choice if I want to get notified to know if there is anyone positive near me. The Bluetooth and location permission seems kinda creepy like they are trying to track your devices connected via bluetooth and track your location. That Is my problem with the app.<br> :date: __2021-01-03 14:43:47__

> It is not showing the update results of covid test<br> :date: __2021-01-01 21:07:29__

> Not working always<br> :date: __2021-01-01 13:06:23__

> Very slow<br> :date: __2020-12-31 11:11:18__

> Since the last update the app is getting stuck, displaying only the splash screen<br> :date: __2020-12-30 12:01:01__

> I've been re-installing, logging out/logging in again and again but still i cannot proceed to get my result. It always ask me some survey, can't able to submit because it keeps hangs up.<br> :date: __2020-12-30 06:55:43__

> Good<br> :date: __2020-12-29 18:16:42__

> Slow. .. can't understand the importance and value of using this application !!!!!<br> :date: __2020-12-29 05:39:11__

> System very slow<br> :date: __2020-12-29 04:09:05__

> Hi After installing this app, I can't proceed as it does not show the Yes / No option in the pre-conditions survey. So I can't move forward and do the submit. I tried the uninstallng of app and again installed the same. But still the same. Please rectify the issue. Thanks<br> :date: __2020-12-27 05:36:27__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="doh.health.shield 1 reviews"/>
</p>

> This app is not working<br> :date: __2021-01-09 06:03:47__

> Useless for me<br> :date: __2021-01-08 11:47:22__

> Its not opening .why didn't open this app<br> :date: __2021-01-08 08:10:50__

> What's the purpose of switching on Bluetooth and disabling the battery optimization.if disabling the battery option the battery drains very fast and also the loading the app is very slow as well.<br> :date: __2021-01-07 09:46:15__

> This app is not working as mentioned. It shows loading<br> :date: __2021-01-07 07:19:04__

> It keeps telling me wrong credentials even though my phone number is correct<br> :date: __2021-01-06 14:13:50__

> Doesn't work most of the times.. when it works it is very slow<br> :date: __2021-01-06 11:20:58__

> very high power consumption<br> :date: __2021-01-05 23:11:38__

> Pretty sad app. Poor support. Hasn't updated my star, or post vaccine status. No way to contact anyone through customer support, unless you want to spend a day waiting listening to the waiting tone. No response to emails. Frightful.<br> :date: __2021-01-05 09:14:14__

> Always crash on huawei android 10<br> :date: __2021-01-05 01:41:56__


