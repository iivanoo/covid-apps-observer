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

> It excellent and great service<br> :date: __2021-03-14 14:28:14__

> Nice app<br> :date: __2021-03-14 14:24:06__

> Love<br> :date: __2021-03-14 13:50:10__

> Excellent information gettng this apo<br> :date: __2021-03-14 12:39:14__

> Excellent<br> :date: __2021-03-14 12:32:09__

> تم<br> :date: __2021-03-14 11:05:16__

> Good<br> :date: __2021-03-14 10:07:34__

> Wonderful<br> :date: __2021-03-14 09:30:30__

> Good<br> :date: __2021-03-14 08:57:36__

> Exceptional<br> :date: __2021-03-14 08:23:03__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="doh.health.shield 4 reviews"/>
</p>

> There is no update for samsong phone<br> :date: __2021-03-14 05:26:43__

> After 2nd dose of covid vaccine 28 days have been completed but so far status not updated. I tried to call on help line but after few rings line disconnected. Need help on it.<br> :date: __2021-03-10 11:12:56__

> Good app<br> :date: __2021-03-09 18:25:44__

> i couldn't ope this app in my phone why<br> :date: __2021-03-09 07:31:06__

> It's been ovee 28 days since I received my second dose but still E did not appear on my Al horn app<br> :date: __2021-03-07 19:59:13__

> Nice<br> :date: __2021-03-06 20:51:08__

> I have cpmpleted 28 days after 2nd dose vaccine still the vaccinated details are not getting updated in the application<br> :date: __2021-03-06 18:59:48__

> Nice<br> :date: __2021-03-06 15:22:43__

> Good<br> :date: __2021-03-04 16:22:15__

> Good<br> :date: __2021-03-03 12:07:45__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="doh.health.shield 3 reviews"/>
</p>

> Test result not yet updated I have done my test yesterday and got negative result message on mobile but till now not updated in app.<br> :date: __2021-03-14 14:59:44__

> I download and installed the app. But its not starting to log.<br> :date: __2021-03-14 08:34:52__

> Tha best app use<br> :date: __2021-03-12 20:00:33__

> I'm still waiting my vaccine update massage.. Pls update my vaccination details<br> :date: __2021-03-11 17:32:41__

> Unreliable. Sometimes delayed in update of information/tests.<br> :date: __2021-03-11 06:47:29__

> I already vaccinated of 1st dose and 2nd dose and after 1 month with 4 consecutive swabtest my results in al hoshn still not mention that I am E-Vaccinated.<br> :date: __2021-03-10 09:15:48__

> Al Hosn app not updated,Two time I did the test after completing 28 days vaccination period.but still not showing my negative result (E) in application.<br> :date: __2021-03-08 15:54:06__

> Keep crashing, test results are not updating for past 2 days.<br> :date: __2021-03-04 05:58:17__

> Good<br> :date: __2021-03-03 11:02:12__

> Errors occur<br> :date: __2021-03-03 10:41:48__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="doh.health.shield 2 reviews"/>
</p>

> Results are not updating<br> :date: __2021-03-14 14:07:17__

> ol c<br> :date: __2021-03-14 11:30:31__

> Why it's not showing my last 2 PCR test results?<br> :date: __2021-03-13 08:09:55__

> This app.not totaly updated they said if u take secone doze of vaccine it shows here the letter E,,,until now i dont recieved mine i took 2nd doze last feb 10,2021 and i take weekly pcr...<br> :date: __2021-03-11 18:30:53__

> This app should be upgrade its service otherwise please stop .Last 6 days I am waiting for my result but still not come. I get already message from Meena Lab.<br> :date: __2021-03-11 04:46:12__

> I have been getting my results on Alhosn but latelyI have done 3 test got the result by SMS but yet to receive the result in Alhosn what could be the problem😢<br> :date: __2021-03-10 06:22:42__

> Cant access the app<br> :date: __2021-03-09 21:24:54__

> Even i receive msg from text to my pcr results but still not updated my results to get my e vaccinated why like this even updated apps still the same very disappointed really not good can u please fixed this because it's terrible i always updated apps but may pcr test results got message but in apps still nothing why they need to make apps if nothing really really disappointed really<br> :date: __2021-03-08 09:13:43__

> Pcr test after 4 days works<br> :date: __2021-03-07 20:19:11__

> no update 🥵<br> :date: __2021-03-07 10:23:10__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="doh.health.shield 1 reviews"/>
</p>

> Whay not coming my test results in this apps<br> :date: __2021-03-14 15:08:51__

> My covid vaccination already complete January 4 second dose 2 months complete still not showing covid vaccination also I have PCR test<br> :date: __2021-03-14 13:57:21__

> Not updated me the COVID-19 vaccinated details, after 2nd dose completed 28 days<br> :date: __2021-03-14 12:43:57__

> Why It' s Not Working In My Phone<br> :date: __2021-03-14 11:44:58__

> Appalling, same problems as everyone else. No customer service, my phone number is now 'not the one registered' when it my only number and was confirmed by the test centre. Still, the UAE can tick a box saying it has a nationwide test and trace system. The fact it doesn't work won't worry anyone from the government, they've ticked their box!<br> :date: __2021-03-14 10:53:25__

> What for bluetooth! What for GPS!<br> :date: __2021-03-14 07:22:35__

> This app not updated my vaccination details.<br> :date: __2021-03-14 06:21:22__

> It's not reflecting the tests results<br> :date: __2021-03-14 05:58:17__

> Sucks<br> :date: __2021-03-14 05:02:06__

> Actually I would not rate this app even 1 star (but have no choice to post it since it's required to put it to be able to post it)because it keeps on hanging up and it's not clear, lack of options for every detail of the info that every individual needs. This app needs more enhancements.<br> :date: __2021-03-14 04:23:32__


