# ALHOSN UAE
App version ``1.46.610``

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
| **Latest version** | 1.46.610 |
| **Last update** | 2021-04-08 16:26:26 |
| **Recent changes** | - Improved user experience <br>- App stability |
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
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
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
> - This application opens a Socket and connects it to the remote address 'Lh/b/a/a/a;->f(Ljava/lang/String;)Ljava/lang/StringBuilder;' on the 'N/A' port <br>
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

The ALHOSN UAE app has been installed by more than **1000000** times. At this time, **18475** rated the app and its average score is **4.2978005**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 13717

:star::star::star::star:: 1508

:star::star::star:: 601

:star::star:: 336

:star:: 2313

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="doh.health.shield 5 reviews"/>
</p>

> The best app ever for covid-19 QR code<br> :date: __2021-04-12 12:12:59__

> Good and updated app<br> :date: __2021-04-12 09:20:17__

> Perfect<br> :date: __2021-04-12 06:16:37__

> Masallah<br> :date: __2021-04-12 05:44:19__

> I am fine.so very good usefully app<br> :date: __2021-04-12 04:28:53__

> Good and helpful<br> :date: __2021-04-11 20:19:43__

> کھولتا نہیں ہے<br> :date: __2021-04-11 19:23:42__

> 👍<br> :date: __2021-04-11 17:48:05__

> it very useful<br> :date: __2021-04-11 17:42:07__

> A comprehensive app<br> :date: __2021-04-11 16:15:42__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="doh.health.shield 4 reviews"/>
</p>

> Good<br> :date: __2021-04-12 11:11:07__

> I am unable to open this app<br> :date: __2021-04-12 09:23:16__

> Very good app<br> :date: __2021-04-11 18:46:40__

> Nice app<br> :date: __2021-04-11 12:24:40__

> Im a first timer<br> :date: __2021-04-10 18:20:46__

> Muhammad and<br> :date: __2021-04-10 17:19:02__

> It's a useful tool and it certainly works. My app wasn't working. Initially I restarted my mob to see it works but gave the same error. Then I uninstalled the app and reinstalled the app. It finally worked as it gets the updated information. Now both dose info is displayed on the Al Hosn app. Give it a try.<br> :date: __2021-04-06 05:26:36__

> Good<br> :date: __2021-04-06 04:51:51__

> It's so convenient<br> :date: __2021-04-04 16:13:08__

> Good<br> :date: __2021-04-04 02:54:09__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="doh.health.shield 3 reviews"/>
</p>

> Isn't it suppose to say when the person took the first and second dose of the vaccine? How do I contact to say I should have the E status.<br> :date: __2021-04-09 22:46:56__

> Is not updated i have my result of pcr test today from sms but in alhosn app still in march 22,,,update pls..thank u..<br> :date: __2021-04-09 21:48:31__

> Application crashes while opening after the update on Android.<br> :date: __2021-04-08 13:40:04__

> Good<br> :date: __2021-04-07 11:36:49__

> NOT update last pcr test result<br> :date: __2021-04-05 18:03:30__

> My Alhosan app last month 23 to not showing Update results. Please help.<br> :date: __2021-04-05 10:03:50__

> I have done my PCR test yesterday. Since last night the App shows 'error'<br> :date: __2021-04-05 08:01:58__

> App is not open....plz help me<br> :date: __2021-04-05 07:52:32__

> Today I took a pcr test and after that the app stopped working. When I try to open, it gives me a message "an error has occurred, please try again later or contact customer support". And no phone number was given for customers support!<br> :date: __2021-04-04 16:12:52__

> Its not working since 20th march . I tried many time but app doesn't open. Even i tried reinstalling . No chance i hope they will solve it soon<br> :date: __2021-04-04 14:47:11__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="doh.health.shield 2 reviews"/>
</p>

> My app is not working, it only show results of the DPI. I have called, emailed, deleted and re-installed the app and nothing works. Government needs the app to cross the checkpoint and its placing unnecessary stress on me as I fear I will not be able to go to work. My colleagues apps is working fine. It looks like I have excuses to go to work. Please help 🙏<br> :date: __2021-04-10 12:44:25__

> Good<br> :date: __2021-04-08 14:44:41__

> Hi, Is there any rule that the details in the app doesn't get updated, if have recently travelled and stayed for less than 14 days in dubai?<br> :date: __2021-04-08 13:58:38__

> I can't register my App because even though it shows my correct name and UID number, it isn't recognizing my cell and says it's not the correct number on file. What "file"??? Of course you can't get anyone from Al Hosn to answer phone or return messages to help me with this change. So I am basically out of luck crossing the border until it's fixed. Ridiculous to just register with your cell number and not having the option for also registering with email, when cell numbers can change.<br> :date: __2021-04-07 14:37:26__

> Super<br> :date: __2021-04-05 20:44:45__

> Application is not working after update<br> :date: __2021-04-05 12:23:13__

> Good apps<br> :date: __2021-04-05 11:50:08__

> Good but sometimes not working<br> :date: __2021-04-04 11:22:14__

> Not working right now<br> :date: __2021-04-03 23:51:15__

> Not updating and the results come after I delete then install again<br> :date: __2021-04-02 11:10:03__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="doh.health.shield 1 reviews"/>
</p>

> Canoot download<br> :date: __2021-04-12 19:03:59__

> It doesn't update the test even after 14 days. IT'S JUST NOT WORKING!!!!!! PLEASE FIX THIS!!!!!!!!!!<br> :date: __2021-04-12 18:56:20__

> My 2nd dosage was not in the App eventhoughi finished all dosages. Their number can't be contacted as well<br> :date: __2021-04-12 15:14:26__

> Not working, need to access most recent results but they are not showing.<br> :date: __2021-04-12 14:14:56__

> One of the worst app. How can they recommend this app at check point. I want to travel from dubai to abu dhabi. When I did my vaccination i provide my old number now i have different number. There is no technical assistant. Its been a week now. You cant send email. There is no response in call. At least there should be some way to communicate. Now im stuck here and i cant go to abu dhabi becoz of this app.<br> :date: __2021-04-12 09:58:25__

> App is not work even not getting open. Kinda fix the issue "ALHOSN keeps stopping " shows like this whenever tried to open.<br> :date: __2021-04-12 05:52:09__

> App not working<br> :date: __2021-04-12 04:55:45__

> Not working on a rooted device or bootloader unlocked device any idea?<br> :date: __2021-04-12 02:14:24__

> My rtpcr test result is not updated yet I have used UID<br> :date: __2021-04-12 01:35:41__

> It's not opening on my phone<br> :date: __2021-04-11 22:05:21__


