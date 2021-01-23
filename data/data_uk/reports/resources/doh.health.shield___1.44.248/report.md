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

> Good<br> :date: __2021-01-22 17:59:06__

> Perfect apps for information<br> :date: __2021-01-22 17:46:11__

> Great app<br> :date: __2021-01-22 16:16:12__

> Ok<br> :date: __2021-01-22 16:15:39__

> Fine<br> :date: __2021-01-22 04:54:31__

> Good<br> :date: __2021-01-21 20:17:32__

> Very good<br> :date: __2021-01-21 17:38:18__

> Good<br> :date: __2021-01-21 17:10:40__

> Excellent<br> :date: __2021-01-21 13:34:30__

> very nice<br> :date: __2021-01-21 13:27:56__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="doh.health.shield 4 reviews"/>
</p>

> Before this was ok but now it is not showing my results it is asking pre condition surveys question?<br> :date: __2021-01-22 10:42:17__

> Good<br> :date: __2021-01-21 06:26:39__

> Keep improving as there are bugs. Thank you.<br> :date: __2021-01-19 18:54:51__

> Very good<br> :date: __2021-01-19 18:45:29__

> Good<br> :date: __2021-01-19 18:30:25__

> Hi , I take covid vaccine but alhosn app not showing my vaccine report<br> :date: __2021-01-17 10:16:47__

> It's a good application<br> :date: __2021-01-17 05:46:57__

> Nice working<br> :date: __2021-01-16 05:24:46__

> Does what it says on the tin...would be better if you didn't have to have your location switch on to use it. Apart from that, no issues<br> :date: __2021-01-09 09:50:29__

> Very good<br> :date: __2021-01-06 18:10:20__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="doh.health.shield 3 reviews"/>
</p>

> Greetings and more, my PCR test result and phase III trials volunteer star is not being updated.Kindly advice.<br> :date: __2021-01-21 12:18:50__

> Good<br> :date: __2021-01-19 18:25:21__

> User details not available<br> :date: __2021-01-16 19:03:03__

> its showing wrong credentials error while am trying login the app. since i am using same number from the beginning and I have registered with the same number, but now its showing that logout and login with another number ending with 748 which is not under my name. i have already send the mail but still there is no response. kindly advise me<br> :date: __2021-01-16 11:41:13__

> Due to some reson I change my mobile num now i want to cheak my covid19 test result on alhosan uae app but i unable to cheak my result i already change my num at scraning center<br> :date: __2021-01-16 04:20:29__

> Hi can you please tell me how i can get e letter on al hosn app , just today i got covid 19 first shot , please guide me<br> :date: __2021-01-15 20:16:00__

> How can I change the associated mobile number?<br> :date: __2021-01-14 09:28:14__

> Ok<br> :date: __2021-01-06 22:19:14__

> My app is not working I took a test yesterday and I am trying too open my profile but it says error try later or contact customer service.<br> :date: __2021-01-05 05:17:24__

> useful<br> :date: __2020-12-31 16:56:18__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="doh.health.shield 2 reviews"/>
</p>

> My covid result is coming but al hosn app says some time not result yet, some time mobile no. Is not register why<br> :date: __2021-01-19 18:44:18__

> There is no feedback from call center<br> :date: __2021-01-17 07:43:42__

> First 4 months this application works very smoothly.But last December I did one covid test but still I didn't get report on alhosn.i registered 3 times complaints. But nothing happened. Finally one customer service madam provide me a watsapp no and informed me to send Emirates I'd,my covid report and screenshot of alhosan app.i send all details.But still no progress. Seriously worried about this application<br> :date: __2021-01-14 07:00:37__

> Tests are not always showing and difficult to get contact with al hosn people. No one answering the phone or email.<br> :date: __2021-01-11 16:17:01__

> How long this apps took to update covid- 19 vaccine status ???? Or star<br> :date: __2021-01-11 04:00:14__

> I want to log in bt last one hour still didn't take password. Plz provide code<br> :date: __2021-01-10 19:57:06__

> I know people using this app have way worse problems than I have but here is my take, I have one problem with the app why does it need my Bluetooth and location data all the time and why can't I make the choice if I want to get notified to know if there is anyone positive near me. The Bluetooth and location permission seems kinda creepy like they are trying to track your devices connected via bluetooth and track your location. That Is my problem with the app.<br> :date: __2021-01-03 14:43:47__

> It is not showing the update results of covid test<br> :date: __2021-01-01 21:07:29__

> Not working always<br> :date: __2021-01-01 13:06:23__

> Very slow<br> :date: __2020-12-31 11:11:18__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="doh.health.shield 1 reviews"/>
</p>

> It says wrong credentials and asking me to use some unknown number. In my all other official documents, id's and government applications, i have my personal number and its working fine. But only for this application it's not. I did my covid vaccination and want to see my result. Please do the needful give user some meaningful options and settings.<br> :date: __2021-01-22 18:50:37__

> البرنامج يستهلك بطاريه يرسل كثير من الاشعارات<br> :date: __2021-01-22 16:43:22__

> Horrible user experience. Why does it not have a reliable spell check? Says that my number is not registered especially when it says that my number is registered. That also after I recieved a successful screening. Fix it<br> :date: __2021-01-22 11:18:12__

> It's not working 😤😦<br> :date: __2021-01-22 08:20:16__

> Prompting my number (current number registered on my recent test) is not registered. Log out and log in with your numbers: (my old number) I followed the procedure but I did not received the on my old number. I tried again on my current number, I easily got the code but still prompted "Not registered".... Any work around for this?<br> :date: __2021-01-22 06:24:55__

> Why it need your location all the time?<br> :date: __2021-01-21 13:28:23__

> Not able to select location on, pressing multiple times but x sign is not changing to a green tick and that mean i can not proceed with use of the app. Any suggestions?<br> :date: __2021-01-21 08:49:46__

> سيء<br> :date: __2021-01-20 19:14:31__

> Why blue tooth need ON, or battery too much consume...good thing covid 19 r and vaccination ecord save☺️<br> :date: __2021-01-20 15:31:53__

> Horrible app<br> :date: __2021-01-20 14:29:13__


