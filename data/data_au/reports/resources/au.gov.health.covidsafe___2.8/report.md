# COVIDSafe
App version ``2.8``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="COVIDSafe icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | COVIDSafe |
| **Unique identifier** | au.gov.health.covidsafe |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=au.gov.health.covidsafe](https://play.google.com/store/apps/details?id=au.gov.health.covidsafe) |
| **Summary**  | COVIDSafe is a community-based way to stop the spread of COVID-19. |
| **Privacy policy** | [https://covidsafe.gov.au/privacy-policy.html](https://covidsafe.gov.au/privacy-policy.html) |
| **Latest version** | 2.8 |
| **Last update** | 2021-07-01 07:35:27 |
| **Recent changes** | Under investigation COVID-19 case numbers added to home screen to align to Department of Health website.  |
| **Installs**  | 1,000,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 25, 2020 |
| **Size**  | 28M |
| **Supported Android version**  | 5.0 and up |

### Description
> COVIDSafe app has been developed by the Australian Government Department of Health to help keep the community safe from coronavirus (COVID-19). Together, let’s help stop the spread and keep ourselves and each other healthy.
<br>COVIDSafe uses the Bluetooth® technology on your mobile phone to look for other devices with COVIDSafe installed. Your device will take a note of contact you’ve had with other users by securely logging the other user’s reference code. If you or someone you’ve been in contact with is diagnosed with COVID-19, the close contact information securely stored in your phone can be uploaded and used—with your consent—by state and territory health officials to quickly inform people who’ve been exposed to the virus.
<br>How you can help stop the spread of COVID-19:
<br>• Download the COVIDSafe app
<br>• Register using your mobile phone number, name, age range and postcode
<br>• Turn on Bluetooth®
<br>• Check that COVIDSafe is running when you are out and about or are likely to come into contact with others
<br>• If you test positive for COVID-19, you can consent for your close contact information to be used by state and territory health officials to contact people who may have been exposed. If you’ve been exposed to the virus by someone you’ve been in close contact with, state and territory health officials will be able to contact you quickly so you can get the support you need
<br>COVIDSafe is an Australian Government Department of Health initiative. Visit https://www.health.gov.au/resources/apps-and-tools/covidsafe-app for more information.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/>  | <img src="screenshot_5.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Australian Department of Health |
| **Website**  | [https://www.health.gov.au/resources/apps-and-tools/covidsafe-app#covidsafe-app-help](https://www.health.gov.au/resources/apps-and-tools/covidsafe-app#covidsafe-app-help) |
| **Email** | support@COVIDSafe.gov.au |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Australian+Department+of+Health](https://play.google.com/store/apps/developer?id=Australian+Department+of+Health) |

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
 **android.permission<br>ACCESS_COARSE_LOCATION** | :warning:**Dangerous** | Allows an app to access approximate location. 
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>BLUETOOTH_ADMIN** | Normal | Allows applications to discover and pair bluetooth devices. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>REQUEST_IGNORE_BATTERY_OPTIMIZATIONS** | Normal | Permission an application must hold in order to use Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | stackoverflow.com | Stack Exchange, Inc. | :us: US | 2003-12-26 19:18:07 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address ' returned no addresses for  ; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The COVIDSafe app has been installed by more than **1000000** times. At this time, **21081** rated the app and its average score is **3.7387688**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 10971

:star::star::star::star:: 3025

:star::star::star:: 1806

:star::star:: 1166

:star:: 4113

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> eccellent<br> :date: __2021-07-19 13:08:51__

> I am happy with this system<br> :date: __2021-07-19 12:08:13__

> Easy to use, wish there was consistency with Check In / Check Out rather than Check in / Done.<br> :date: __2021-07-19 11:37:48__

> Best government app. Hope they start including passport, vaccination certificate and national identity number.<br> :date: __2021-07-19 08:56:55__

> very good. we can get the information right away.<br> :date: __2021-07-19 06:15:59__

> Easy to use<br> :date: __2021-07-18 16:07:47__

> We're all in this together<br> :date: __2021-07-18 05:47:04__

> Very informative,simple to navigate.<br> :date: __2021-07-18 02:23:04__

> Handy to have details re restrictiions. Ty<br> :date: __2021-07-17 09:29:53__

> No problems<br> :date: __2021-07-17 08:19:46__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> Blue tooth keeps dropping out<br> :date: __2021-07-19 06:55:32__

> Use to check daily<br> :date: __2021-07-19 05:52:33__

> It's set and forget...although Google maps tracks me better from my side.....<br> :date: __2021-07-18 04:41:24__

> Unable to figure out how to indicate messages are read.<br> :date: __2021-07-17 11:40:43__

> Not too bad for novice.<br> :date: __2021-07-17 10:18:52__

> The Vic app is really good it is faster which saves time at each venue<br> :date: __2021-07-17 06:52:40__

> Not to bad setting up.<br> :date: __2021-07-17 02:34:16__

> You need to wait until 11 am before you get the days tally<br> :date: __2021-07-15 22:44:03__

> Happy with how the QR works for my wife and myself<br> :date: __2021-07-15 11:08:39__

> Good<br> :date: __2021-07-15 09:28:27__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> Good<br> :date: __2021-07-19 06:09:15__

> One thing seems to be missing and that's some idea of how it effects the deaf community! I sign AUSLAN the Australian Deaf Language we rely on facial expressions and body language. How can I express emotion while my face is covered? How can my lips be read if my face is covered? Also it needs to allow more than one place at a time or when in a shopping complex one sign in, into the complex as I'm mixing with all inside. If I clock into the complex I have to log out and into another store.<br> :date: __2021-07-18 00:48:19__

> No issues.<br> :date: __2021-07-18 00:01:47__

> Power hungry, reliably uses 60% of my battery a day.<br> :date: __2021-07-16 14:38:56__

> Doesn't tell me hotspots or dates<br> :date: __2021-07-16 00:10:52__

> Seems to use up battery quickly.<br> :date: __2021-07-14 02:32:47__

> Unsure really of what benefit this app has.<br> :date: __2021-07-13 14:17:32__

> Chews up battery time<br> :date: __2021-07-12 09:23:31__

> The rate at which information is updated is appalling. Faster more reliable info from YouTube<br> :date: __2021-07-12 08:38:46__

> Who would know if it is working?<br> :date: __2021-07-11 23:36:10__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> I'm not sure that this app actually does anything. Has it actually been used for any contact tracing? I'll keep it on the phone for now, as it's fairly harmless (If you're worried about Big Brother tracking you on your phone, he's had that ability for more than 20 years now and with better technology than this app.). Just applied another update (19/7/21). Still think it's useless.<br> :date: __2021-07-19 06:14:45__

> Guys I hate this app real bad<br> :date: __2021-07-18 10:01:53__

> Am unable to access western australia info. An info bar at the bottom of the page is still in the way. Im surprised it has'nt been noted before now.<br> :date: __2021-07-17 08:21:20__

> Qr codes appear to be more reliable<br> :date: __2021-07-15 20:40:31__

> Poor design. You could use GPS and maintain 100% privacy. Contact me to ask how. Victoria just locked down over 2 cases. How much by is that costing?<br> :date: __2021-07-15 09:32:44__

> Please stop popping up minor update notification. Or I'll disable it and make it useless.<br> :date: __2021-07-15 06:35:16__

> this is about the most confusing appbever used<br> :date: __2021-07-13 19:33:43__

> Like most govt websites easier to go to 7 news or abc news<br> :date: __2021-07-13 05:46:12__

> No idea how successful (or relevant) this App really is? It would be great is the Federal Government took REAL leadership and used Fiscal measures to force ALL States to follow one set of rules for all matters relating to Masks, Lockdowns, Hot Spots etc.<br> :date: __2021-07-12 10:03:45__

> Jmummm<br> :date: __2021-07-12 05:22:23__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> Terrible<br> :date: __2021-07-19 14:00:13__

> It obviously doesn't work. Never heard of it ever being used to trace anyone.<br> :date: __2021-07-19 13:24:51__

> This app is complete junk! Is everyone aware that it does not work without bluetooth on! Please explain why it needs bluetooth to operate? Because of that.. i will delete this ap right now!<br> :date: __2021-07-19 11:23:50__

> How is this app helping?<br> :date: __2021-07-19 08:33:01__

> What? An update? Will this make it work? If this app worked as it should the states wouldn't be chasing their arses when contact tracing. As usual it's another of ProMo's flops.<br> :date: __2021-07-19 08:10:54__

> Doesn't do anything. Waste of space.<br> :date: __2021-07-19 05:40:34__

> It never did what it was supposed to. It cost millions and now in Sydney we have the Service NSW app that does everything<br> :date: __2021-07-19 02:26:03__

> Useless water of tax payer money. Would rate 0 stars if possible.<br> :date: __2021-07-19 01:54:16__

> Cant understand at many places i have to tap in numbers manually and minimum few other places i can just hold phone to APP<br> :date: __2021-07-18 12:42:45__

> Thought I'd give it another go to help with contact tracing. App still kills my battery. Unfortunately I can't have an app that will drain most of my battery when I haven't seen a single instance in the news that it's actually helping contact tracing efforts.<br> :date: __2021-07-18 09:15:16__


