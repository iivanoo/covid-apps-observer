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

> It's not working properly even not come open<br> :date: __2021-02-13 18:16:59__

> Great<br> :date: __2021-02-13 17:18:10__

> Very good<br> :date: __2021-02-13 14:45:12__

> Nice<br> :date: __2021-02-12 20:51:58__

> Good<br> :date: __2021-02-12 15:20:38__

> I did a vaccine two time. And it doesn't show any thing about any one of them.   I did restart to the phone. I did uninstall and install again.  Nothing changed.  It only show my last PCR test not the vaccine<br> :date: __2021-02-12 11:19:39__

> My viccine second dos finish but app not show result<br> :date: __2021-02-12 10:08:12__

> Very good app... Its i can see my test result of corona virus<br> :date: __2021-02-12 08:27:30__

> I download this , Igot result from my first pcr test, I don't get dpi test and second pcr test results in alhosn ap. I got the results but it's not updated.<br> :date: __2021-02-12 08:17:05__

> The best 🎊🎉🥞<br> :date: __2021-02-12 00:37:07__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="doh.health.shield 4 reviews"/>
</p>

> Working well<br> :date: __2021-02-12 07:47:56__

> Good<br> :date: __2021-02-09 17:47:36__

> Nice app but it's soo loaded i don't know why opening time many's mints<br> :date: __2021-02-09 03:59:31__

> Good<br> :date: __2021-02-08 11:38:19__

> গুড অপশন ইউএই<br> :date: __2021-02-07 14:38:25__

> I did test last 02/02/2021 is still not showing my results..how.......<br> :date: __2021-02-07 07:50:27__

> Good<br> :date: __2021-02-05 07:02:27__

> this app helpful<br> :date: __2021-02-02 14:57:27__

> I like it 🙂😊<br> :date: __2021-02-02 04:02:02__

> Excellent<br> :date: __2021-02-01 05:34:27__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="doh.health.shield 3 reviews"/>
</p>

> Since, I have a terrible experience using this App. here are some pointers for all the users, and hope these helps: 1. Make sure to register the same Contact no. you gave during PCR test. Thus, it will show an error credentials. 2. Unfortunately, if you got infected after your quarantine. You are required to complete 2 negative results. Thus, it won't turn to green. IMPORTANT!!! MAKE SURE TO UNDERGO A PCR IN DHA ONLY. NOT TO THE CLINIC.<br> :date: __2021-02-11 06:00:07__

> The app is not working properly, covid 19 test report is not reflecting in my Al Hosn app, I tried to reach customer care to fix the issue more than trice today, they are just telling that it will be fix within 30 minutes each times. I am travelling from Dubai to Abu Dhabi and as per New rule border police will not allow me to enter Abu Dhabi until unless the report reflected in App.<br> :date: __2021-02-09 14:58:22__

> For anyone suffering from wrong credentials issue, you need to download and install UAE Pass application, and verify the information at an approved kiosk (you can do this at the FCA happiness centers), after that and one PCR test the Al Hosn app will work.<br> :date: __2021-02-09 04:52:16__

> Dear : Sir/Mam My vaccination finished 03/02/2021. still this app no any changes for my detailes. what is use for this app. how much day taken for this updation.please clear this matter for updation. Thanks : Best Regards<br> :date: __2021-02-08 07:05:10__

> I've reinstalled it and it's still not showing my E status.<br> :date: __2021-02-06 20:31:15__

> 2 doses of Vaccination is done. But more than 10 days finished but still not updated in alhosn app. message also come to my mobile regarding vaccination finish. Kindly update<br> :date: __2021-02-04 19:59:44__

> I don't have an ID card, I'm coming to travel, how do I drive?<br> :date: __2021-02-04 07:49:26__

> When i take the pcr test its not showing anymore. Now that i have covid19 still not showing.<br> :date: __2021-02-03 04:42:27__

> Fair<br> :date: __2021-02-02 12:22:13__

> Too much massage notifications pop up irritating<br> :date: __2021-01-31 23:15:02__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="doh.health.shield 2 reviews"/>
</p>

> Technical issues with this mean records don't get updated. No response from Alhosn team when try to contact them. Disappointed as this is required to prove vaccine status and pcr test results<br> :date: __2021-02-13 07:07:39__

> يعطل الجهاز<br> :date: __2021-02-11 07:25:29__

> Not working properly and no results yet.<br> :date: __2021-02-10 17:20:08__

> Very nice<br> :date: __2021-02-06 18:08:25__

> The App is battery intensive<br> :date: __2021-02-06 17:10:02__

> The app doesn't open, just showing the logo<br> :date: __2021-02-05 00:06:32__

> App used to work but not anymore. I tried setting up my account with no luck and tried sending the error message to the developer email but i bounced back saying the inbox is full. Let me know how to resolve it. Thanks<br> :date: __2021-01-31 11:15:07__

> I can't opened my Alhons i want the result from here<br> :date: __2021-01-31 06:18:12__

> Hopeful<br> :date: __2021-01-29 18:06:23__

> After one month it is not opening<br> :date: __2021-01-26 11:47:55__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="doh.health.shield 1 reviews"/>
</p>

> I have done covid test 3 times but doesnt show on this App As it reflects no test report available as i have given the same mobile no.to the test center. I received text msg of my covid test on the same no. But al hosn app says your no.is not registered try with your mob.no.as i dont have any other local no. I mail the support team but it says our mail box is full we r not able to help u try again later. Please check with this app i request the Al Hosn Support team. It will be very helpful to u<br> :date: __2021-02-13 17:19:34__

> Im tired for log in appear error .i need this apps what shall i do?<br> :date: __2021-02-13 13:43:17__

> I can't open it<br> :date: __2021-02-13 10:13:59__

> Its asking survey and no option more<br> :date: __2021-02-13 08:27:46__

> Not working well<br> :date: __2021-02-13 08:15:23__

> It's not showing my test results. No results found even I had two PCR test.<br> :date: __2021-02-12 23:51:31__

> I took 3 tests ..and still not even one showed in the app .<br> :date: __2021-02-12 21:52:05__

> No customer support. I have completed my vaccination but status till now not updated and there is no one to help.<br> :date: __2021-02-12 16:59:08__

> I downloaded this app ..to check my vaccinated records....it's not working showing error..... always can't scan ..<br> :date: __2021-02-12 11:15:27__

> Not even opening on samsung A70<br> :date: __2021-02-12 05:58:39__


