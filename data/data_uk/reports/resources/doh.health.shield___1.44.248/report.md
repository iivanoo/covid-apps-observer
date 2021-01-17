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

> Very good<br> :date: __2021-01-16 18:03:13__

> Plise open the ap my mobile all Hussain app<br> :date: __2021-01-16 15:48:32__

> ويارا يارا 🤣😘😘😘😘😘😘🤣<br> :date: __2021-01-16 15:31:00__

> A1 app<br> :date: __2021-01-16 12:39:13__

> Good<br> :date: __2021-01-16 11:33:59__

> Well Mantained records<br> :date: __2021-01-16 10:50:55__

> Good<br> :date: __2021-01-16 07:01:22__

> Good very good<br> :date: __2021-01-15 19:07:30__

> thes app very fast and very esy thats whay I like<br> :date: __2021-01-15 15:40:50__

> Excellence app.very informative<br> :date: __2021-01-15 15:22:28__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="doh.health.shield 4 reviews"/>
</p>

> Nice working<br> :date: __2021-01-16 05:24:46__

> Does what it says on the tin...would be better if you didn't have to have your location switch on to use it. Apart from that, no issues<br> :date: __2021-01-09 09:50:29__

> Very good<br> :date: __2021-01-06 18:10:20__

> َكطلفس٦ث<br> :date: __2021-01-05 13:38:10__

> Good<br> :date: __2021-01-03 20:28:16__

> Good<br> :date: __2021-01-03 09:25:31__

> V.good<br> :date: __2021-01-02 16:14:38__

> Found okay<br> :date: __2021-01-02 06:23:39__

> Excellent<br> :date: __2021-01-01 06:08:20__

> Good app<br> :date: __2020-12-26 14:50:44__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="doh.health.shield 3 reviews"/>
</p>

> its showing wrong credentials error while am trying login the app. since i am using same number from the beginning and I have registered with the same number, but now its showing that logout and login with another number ending with 748 which is not under my name. i have already send the mail but still there is no response. kindly advise me<br> :date: __2021-01-16 11:41:13__

> Due to some reson I change my mobile num now i want to cheak my covid19 test result on alhosan uae app but i unable to cheak my result i already change my num at scraning center<br> :date: __2021-01-16 04:20:29__

> Hi can you please tell me how i can get e letter on al hosn app , just today i got covid 19 first shot , please guide me<br> :date: __2021-01-15 20:16:00__

> How can I change the associated mobile number?<br> :date: __2021-01-14 09:28:14__

> Ok<br> :date: __2021-01-06 22:19:14__

> Help me who ever cordinating it i want to change the number its still showing my old number which i am not able to asses any more<br> :date: __2021-01-06 09:28:01__

> My app is not working I took a test yesterday and I am trying too open my profile but it says error try later or contact customer service.<br> :date: __2021-01-05 05:17:24__

> useful<br> :date: __2020-12-31 16:56:18__

> Nice...<br> :date: __2020-12-25 02:24:19__

> The updated version is getting hanging..<br> :date: __2020-12-24 14:17:27__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="doh.health.shield 2 reviews"/>
</p>

> First 4 months this application works very smoothly.But last December I did one covid test but still I didn't get report on alhosn.i registered 3 times complaints. But nothing happened. Finally one customer service madam provide me a watsapp no and informed me to send Emirates I'd,my covid report and screenshot of alhosan app.i send all details.But still no progress. Seriously worried about this application<br> :date: __2021-01-14 07:00:37__

> Tests are not always showing and difficult to get contact with al hosn people. No one answering the phone or email.<br> :date: __2021-01-11 16:17:01__

> How long this apps took to update covid- 19 vaccine status ???? Or star<br> :date: __2021-01-11 04:00:14__

> I want to log in bt last one hour still didn't take password. Plz provide code<br> :date: __2021-01-10 19:57:06__

> I know people using this app have way worse problems than I have but here is my take, I have one problem with the app why does it need my Bluetooth and location data all the time and why can't I make the choice if I want to get notified to know if there is anyone positive near me. The Bluetooth and location permission seems kinda creepy like they are trying to track your devices connected via bluetooth and track your location. That Is my problem with the app.<br> :date: __2021-01-03 14:43:47__

> It is not showing the update results of covid test<br> :date: __2021-01-01 21:07:29__

> Not working always<br> :date: __2021-01-01 13:06:23__

> Very slow<br> :date: __2020-12-31 11:11:18__

> Since the last update the app is getting stuck, displaying only the splash screen<br> :date: __2020-12-30 12:01:01__

> I've been re-installing, logging out/logging in again and again but still i cannot proceed to get my result. It always ask me some survey, can't able to submit because it keeps hangs up.<br> :date: __2020-12-30 06:55:43__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="doh.health.shield 1 reviews"/>
</p>

> Poor performance<br> :date: __2021-01-16 18:49:59__

> This app does not login now which used to work perfectly before. Now it states "user not found" message. Also test results are not updated.<br> :date: __2021-01-16 18:11:28__

> i download this app then i enter my number and it saying that "User not found & Wrong Credentials" so how I can know my result? what can i do? any help?<br> :date: __2021-01-16 17:57:35__

> Not consistent apps and services<br> :date: __2021-01-16 14:27:19__

> My friend result is not reflecting in the app<br> :date: __2021-01-16 13:55:40__

> This app gives the wrong status Post Covid-19<br> :date: __2021-01-16 13:36:15__

> Not working ...its given headache to activate profile .current number using for this apps but apps give others namber which I m not useing any more. .........................<br> :date: __2021-01-16 11:02:19__

> I keep getting a wrong credentials when logging in. Its say i entered a different mobile number.<br> :date: __2021-01-16 10:06:29__

> wont even open on my phone anymore, I keep opening the app only for it to close.<br> :date: __2021-01-15 11:40:33__

> The app doesn't work....<br> :date: __2021-01-15 10:48:13__


