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

> AL HOSN UAE<br> :date: __2021-02-23 18:19:06__

> Very good<br> :date: __2021-02-23 16:48:06__

> Best of the best apps<br> :date: __2021-02-23 16:00:27__

> Good<br> :date: __2021-02-23 14:30:30__

> It's very nice app thanks I took 1st dose 22 /12/2020 2nd dose 5/1/2021 until now not UPDATED on alhosan after 2nd dose 6 pcr test I make negative<br> :date: __2021-02-23 12:48:07__

> Very nice 👍👍👍<br> :date: __2021-02-23 11:26:59__

> very<br> :date: __2021-02-23 11:11:52__

> Excellent<br> :date: __2021-02-23 10:51:00__

> Amazing<br> :date: __2021-02-23 09:22:57__

> Excellant<br> :date: __2021-02-23 05:12:55__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="doh.health.shield 4 reviews"/>
</p>

> Excellent<br> :date: __2021-02-23 08:08:48__

> Good<br> :date: __2021-02-21 20:19:20__

> فحصت بتاريخ 16/1 في خمية صحة الكورنيش ابوظبي والى تاريخ اليوم لم نظهر النتيجة ونزلت علي مخالفة 5000 درهم وقدمت تظلم للأسف هذه المرة الثانية لا تظهر النتيجة علما بأن صحة أرسلت لي رسالة بالنتيجة.<br> :date: __2021-02-20 09:45:18__

> tth<br> :date: __2021-02-18 15:47:02__

> Good<br> :date: __2021-02-18 04:38:05__

> Working well<br> :date: __2021-02-12 07:47:56__

> Good<br> :date: __2021-02-09 17:47:36__

> Nice app but it's soo loaded i don't know why opening time many's mints<br> :date: __2021-02-09 03:59:31__

> Good<br> :date: __2021-02-08 11:38:19__

> গুড অপশন ইউএই<br> :date: __2021-02-07 14:38:25__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="doh.health.shield 3 reviews"/>
</p>

> Very nice and easy to us<br> :date: __2021-02-20 13:23:48__

> It's not easy to access<br> :date: __2021-02-19 07:53:06__

> It worked but now it's not even loading<br> :date: __2021-02-18 11:46:09__

> My old no. is not longer in service it means my sponsor cut it.. I reinstall my al hosn to put my new number that already exists to my pcr test clinic.. The problem now I can't sign in it said try again later or contact etc.. I did many times to sign in and contact the costumer services but the same.. Pls help me what should I do to activate my al hosn.. God bless to all<br> :date: __2021-02-18 11:35:57__

> AL HOSN APP HAS STOPPED WORKING IN MY MOBILE. WHATS GOING ON ANY UPDATES. I NEED TO ENTER ABU DHABI. HOW I WILL ENTER WITHOUT AL HOSN APP. ANY ONE GOING THROUGH THE SAME. WHAT ABOUT THE CHECKPOINT POLICE. HOW WE CAN SHOW THEM THE E LOGO WHICH WE USE TO SHOW THEM IN AL HOSN APP<br> :date: __2021-02-18 11:24:58__

> I download this app but not working I don't know why,<br> :date: __2021-02-17 21:20:20__

> Drains the battery<br> :date: __2021-02-17 15:50:10__

> Good<br> :date: __2021-02-16 20:07:15__

> Very goof<br> :date: __2021-02-14 04:44:30__

> Since, I have a terrible experience using this App. here are some pointers for all the users, and hope these helps: 1. Make sure to register the same Contact no. you gave during PCR test. Thus, it will show an error credentials. 2. Unfortunately, if you got infected after your quarantine. You are required to complete 2 negative results. Thus, it won't turn to green. IMPORTANT!!! MAKE SURE TO UNDERGO A PCR IN DHA ONLY. NOT TO THE CLINIC.<br> :date: __2021-02-11 06:00:07__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="doh.health.shield 2 reviews"/>
</p>

> Consume too much battery life<br> :date: __2021-02-23 15:39:55__

> No customer support<br> :date: __2021-02-19 07:55:05__

> Instructions are not clear, no contact number for a help centre, interface is clean but doesn't give enough info to the user. Design of the app makes a person feel that they have to go for a test but doesn't consider the time passed since last infection. Statuses should be re-evaluated. Location permissions has to be always on but doesn't say why. Annoying notification to fight COVID which you cannot fully read.<br> :date: __2021-02-19 06:06:07__

> I vaccinated second dose, already pass 28 days, i done PCR test on 28th days, i received PCR Test results, Al Hosn Apps updated PCR test results on mobile, but status E not appeared on mobile.<br> :date: __2021-02-19 04:13:20__

> Stuck in loading<br> :date: __2021-02-18 13:53:34__

> Some times not working<br> :date: __2021-02-18 11:55:37__

> Why not opan this aap today im in dubai road ples wana help<br> :date: __2021-02-18 11:17:29__

> Some times my results uploaded jnto app, sometimes no. Costumer service line not working. Email bouncing back. Horrible.<br> :date: __2021-02-18 10:00:00__

> To mach good app<br> :date: __2021-02-18 09:53:48__

> I have downloaded this app 2 times. It won’t open. when I double click or press the “open” button from the apps list it just goes to the first screen displays "ALHOSN" and nothing else. I tried to touch all over the screen to see if a menu will appear but nothing. It's mandatory to have this app and still won’t work.<br> :date: __2021-02-17 15:50:34__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="doh.health.shield 1 reviews"/>
</p>

> Not open app 😭<br> :date: __2021-02-23 16:47:40__

> Good<br> :date: __2021-02-23 16:34:09__

> Not showing any vaccine information<br> :date: __2021-02-23 10:47:52__

> Hi how are this application opening issue what happened please send me details I want covid 19 result for abudhabhi for 1 day<br> :date: __2021-02-23 09:32:21__

> Terrible app.<br> :date: __2021-02-23 08:51:27__

> Riazkhan<br> :date: __2021-02-23 08:37:54__

> Awful app wouldn't even give it 1 star, takes for ever to update(still didn't) and the customer support is none existing<br> :date: __2021-02-23 08:34:46__

> It's become mandatory to download this app to get your test results back. Still waiting for a result from the 18th to come back and it's been 5 days. This is unacceptable when you can only use the results within 48 hours. Then why have this app? The old school way text message worked great. This Is totally useless. Please fix this so people can get on with their life!!<br> :date: __2021-02-23 07:48:45__

> Doesn't work at most times. Was on my way to AlAin and the app wasn't working when I needed to show the star on this app ! Tried calling customer support and writing an email bit never had any response.<br> :date: __2021-02-23 00:41:17__

> app not responding<br> :date: __2021-02-23 00:11:14__


