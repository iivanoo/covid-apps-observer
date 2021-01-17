# COVID Coach
App version ``1.5``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="COVID Coach icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | COVID Coach |
| **Unique identifier** | gov.va.mobilehealth.ncptsd.covid |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=gov.va.mobilehealth.ncptsd.covid](https://play.google.com/store/apps/details?id=gov.va.mobilehealth.ncptsd.covid) |
| **Summary**  | Cope with stress &amp; stay well |
| **Privacy policy** | [https://www.ptsd.va.gov/appvid/mobile/](https://www.ptsd.va.gov/appvid/mobile/) |
| **Latest version** | 1.5 |
| **Last update** | 2020-12-21 19:29:46 |
| **Recent changes** | Spanish language mode is now available. To change COVID Coach&#39;s display language, open the menu and go to Personalize. |
| **Installs**  | 10,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 17, 2020 |
| **Size**  | 81M |
| **Supported Android version**  | 4.4 and up |

### Description
> The world as we know it has changed and we are living in unprecedented and uncertain times. COVID Coach is designed to help you build resilience, manage stress, and increase your well-being during this crisis. The app is free, secure, and helps connect you to important resources for coping and adapting during the COVID-19 pandemic. Customized tools are available to help you cope with stress, stay well, stay safe, stay healthy, stay connected, and navigate parenting, care-giving, and working from home while social distancing, quarantined, or sheltered in place. You can track your mood, visualize your progress, and find resources to seek additional help and support. No account or password is required and user data is not collected.
<br>COVID Coach was made by the mobile mental health team of the National Center for PTSD, Dissemination & Training Division.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/>  | <img src="screenshot_5.png" alt="screenshot" width="300"/>  | <img src="screenshot_6.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_7.png" alt="screenshot" width="300"/>  | <img src="screenshot_8.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | US Department of Veterans Affairs (VA) |
| **Website**  | [https://www.ptsd.va.gov/appvid/mobile/](https://www.ptsd.va.gov/appvid/mobile/) |
| **Email** | MobileMentalHealth@va.gov |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=US+Department+of+Veterans+Affairs+(VA)](https://play.google.com/store/apps/developer?id=US+Department+of+Veterans+Affairs+(VA)) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Android10, version 10 (API level 29) |
| **Effective target Android version**  | Android10, version 10 (API level 29) |
| **Minimum supported Android version**  | KitKat, version 4.4 - 4.4.4 (API level 19) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>ACCESS_WIFI_STATE** | Normal | Allows applications to access information about Wi-Fi networks. 
 **android.permission<br>CAMERA** | :warning:**Dangerous** | Required to be able to access the camera device. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>READ_CONTACTS** | :warning:**Dangerous** | Allows an application to read the user's contacts data. 
 **android.permission<br>READ_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to read from external storage. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>RECORD_AUDIO** | :warning:**Dangerous** | Allows an application to record audio. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **android.permission<br>WRITE_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to write to external storage. 
 **com.android.vending<br>CHECK_LICENSE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | mumbleserver.it | Mumble Srls | - | 2014-03-25 16:27:15 |
 | stanford.edu | Stanford University | - | 1985-10-04 00:00:00 |
 | w3.org | W3C | :us: US | 1994-07-06 04:00:00 |
 | psychologytoday.com | Sussex Publishers LLC | :us: US | 1997-12-29 05:00:00 |
 | addiction.com | Elements Behavioral Health | :us: US | 1998-04-08 04:00:00 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the ISO country code equivalent of the current registered operator's MCC (Mobile Country Code)<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Telephony services abuse**
> - This application makes phone calls<br>

**Audio video eavesdropping**
> - This application records audio from the 'MIC' source <br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The COVID Coach app has been installed by more than **10000** times. At this time, **169** rated the app and its average score is **4.62**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 134

:star::star::star::star:: 25

:star::star::star:: 3

:star::star:: 1

:star:: 6

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.va.mobilehealth.ncptsd.covid 5 reviews"/>
</p>

> This is a very professional and easy to use app w with useful applications for a range of people. I'm a counselor and educator and I recommend this app for personal and client use.<br> :date: __2021-01-12 23:49:14__

> Great very helpful and easy to use<br> :date: __2021-01-10 18:13:50__

> Easy to use.<br> :date: __2020-12-28 02:50:02__

> Great<br> :date: __2020-12-26 21:31:06__

> Is a good app and allows me to regain focus whenever needed.<br> :date: __2020-12-26 00:39:06__

> Just ran thru available topics and am pleasantly surprised. Shame you need to give access to phone files etc. DEVELOPERS: The "goals" page appears in Spanish in the English version.<br> :date: __2020-12-24 05:00:17__

> Some times when things are hard i need a reminder/ nudge to take a step back from the situation. short messages and practices.are just the thing for getting back on the track of mindfulness.<br> :date: __2020-12-24 00:54:23__

> Great suggestions<br> :date: __2020-12-16 01:26:16__

> It's a superb app. Covers everything.<br> :date: __2020-11-23 04:40:59__

> Very excited to use this app more! Thank you to the creators for these tools, your time and diligence to create an app that is easy to use and seems to pull you right out of a hard place.<br> :date: __2020-11-20 02:11:57__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.va.mobilehealth.ncptsd.covid 4 reviews"/>
</p>

> Soothing app<br> :date: __2021-01-07 06:14:57__

> So far I like it<br> :date: __2020-12-09 03:02:35__

> Great app jas measures features and you can chart your progress<br> :date: __2020-11-08 18:29:04__

> Great app. Lots of information to learn about your mental health.<br> :date: __2020-11-01 01:34:40__

> Haven't had to use it but it appears to have resources that would help someone in need<br> :date: __2020-10-10 19:35:22__

> Not a meditatong person but Wow! Body scan leaves me fresh as having a two hour nap.<br> :date: __2020-08-03 20:12:13__

> So far, so good.☺️<br> :date: __2020-07-15 02:32:24__

> Nothing else follows<br> :date: __2020-07-14 18:24:59__

> It is similar to other self help. Easy to use. Makes one think. Asks one questions. Offers advice. Keeps tracks of goals. It all come down to how much energy and honesty one puts into it.<br> :date: __2020-06-30 17:37:32__

> Got a lot of information<br> :date: __2020-06-27 18:12:00__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.va.mobilehealth.ncptsd.covid 3 reviews"/>
</p>

> Why does the app need access to my media and files? Can you offer some features without requiring that access?<br> :date: __2020-09-17 15:58:28__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.va.mobilehealth.ncptsd.covid 2 reviews"/>
</p>

> Can't see how it is useful for COVID. Name is missleading.<br> :date: __2021-01-13 15:11:08__

> Stops on staying well<br> :date: __2020-09-30 05:53:20__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.va.mobilehealth.ncptsd.covid 1 reviews"/>
</p>

> Requires access to your photos and files just to open the app. No thanks.<br> :date: __2020-11-13 01:54:50__

> App keeps crashing! Just use the older PTSD Coach, its basically the same thing.<br> :date: __2020-07-15 02:23:22__

> There should be no reason this app needs media, phone and Gallery permissions just to launch. Especially when it prompts you that you can disable them later.<br> :date: __2020-07-14 21:17:59__

> I was excited for this app. Unfortunately this app REQUIRES access to your phone. After downloading, a prompt will say: "Allow Covid Coach to access photos, media, and files on your device?" As soon as I tap on "deny" the app automatically closes and locks me out of the service. How is this supposed to be helping me? You don't need access to my phone. I'm disappointed.<br> :date: __2020-05-20 07:46:26__


