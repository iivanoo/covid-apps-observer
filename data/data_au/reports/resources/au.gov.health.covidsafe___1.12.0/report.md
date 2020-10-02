# COVIDSafe
App version ``1.12.0``

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
| **Latest version** | 1.12.0 |
| **Last update** | 2020-09-25 10:26:50 |
| **Recent changes** | Bug fixes and usability enhancements. |
| **Installs**  | 1,000,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 25, 2020 |
| **Size**  | 13M |
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
| **Declared target Android version**  | Pie, version 9 (API level 28) |
| **Effective target Android version**  | Pie, version 9 (API level 28) |
| **Minimum supported Android version**  | Lollipop, version 5.0 (API level 21) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_COARSE_LOCATION** | :warning:**Dangerous** | Allows an app to access approximate location. 
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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **13281** rated the app and its average score is **2.716939**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 4016

:star::star::star::star:: 947

:star::star::star:: 1253

:star::star:: 1391

:star:: 5674

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> Makes me feel better and safe.<br> :date: __2020-10-02 09:26:30__

> Love the idea great. We need to keep safe and others.<br> :date: __2020-10-01 22:18:24__

> THIS it's the reason our numbers are so low. Want to keep your freedom? Install the app. Nothing to lose. If you're worried about privacy, it records FAR less information from you than Google maps and Facebook<br> :date: __2020-10-01 00:22:06__

> N/A<br> :date: __2020-09-28 02:38:28__

> Ok a guess but a dont think it work's Thank you dean<br> :date: __2020-09-27 11:44:40__

> No.concerns and privacy respected.<br> :date: __2020-09-27 09:41:00__

> Not sure<br> :date: __2020-09-26 19:07:40__

> Seems to be working with no dramas. Doesn't appear to be affecting my battery life much (Samsung Galaxy s9).<br> :date: __2020-09-26 07:25:41__

> Update. All issues are resolved<br> :date: __2020-09-26 00:24:15__

> It's good<br> :date: __2020-09-25 00:22:01__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> This app has no effect on any aspect of your life unless you come into contact with someone else who has the app AND also has a positive test for COVID. all the scare-mongering about it comes from morons.<br> :date: __2020-10-02 13:06:27__

> Good<br> :date: __2020-10-02 12:00:43__

> Essential to help contains the virus<br> :date: __2020-10-01 00:01:22__

> Would be nice if it had a built-in QR reader so it can provide my encrypted details when checking-in to restaurants, so I don't have to give them my personal details.<br> :date: __2020-09-28 02:12:44__

> Its doing its job as intended, wirh only minor rare bluetooth dropouts.<br> :date: __2020-09-26 02:44:33__

> Happy to do my bit to help out with covid management. Having said that my battery usage has gone through the roof since last update. COVIDSafe is at the top of my battery use list by a country mile. Hopefully the update I have done this morning will fix.<br> :date: __2020-09-26 00:03:57__

> It's probably great but my poor old Android's battery can't handle the strain from running Bluetooth and keeps on switching it off. And, yes, I've checked all the phone settings. Sorry Federal Government. I can't help. Now uninstalled. UPDATE... New phone, now works quietly in the background.<br> :date: __2020-09-25 21:50:32__

> Stops itself at times but makes user feel they are 'doing the right thing'<br> :date: __2020-09-21 14:51:03__

> Nearby places Google calendar apps+maps<br> :date: __2020-09-19 18:22:11__

> Had no troubles, works ok from day1 of release. Now i find out the phone app had battery optimization enabled which prevents app from running correctly. Uninstalled + reloaded as i thought app was the issue. Then used PC and Google to locate how to ensure no optimization on the app. I only turn bluetooth on when i leave home. So no battery issues.<br> :date: __2020-09-06 14:33:07__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> Keeps turning off<br> :date: __2020-10-01 19:49:42__

> Initially worked ok but hasn't worked for a few months now. Back working again.<br> :date: __2020-09-26 08:06:08__

> Why is this app always on without having to turn LOCATIONS some phones and not others? Both our phones are same make and mine is newer model, yet I have to manually turn Location on even though I gave given it permission to be on all the time. Why is this?<br> :date: __2020-09-25 12:06:26__

> On screen icon keeps disappering. Keep needing to open app to keep it active<br> :date: __2020-09-23 11:23:51__

> Happy to use but better if app turns on automatically when Bluetooth and GPS is on, shows active case numbers, doesn't require GPS (drains battery).<br> :date: __2020-09-20 03:50:59__

> Is this even worthwhile anymore?<br> :date: __2020-09-16 14:41:22__

> No phone or battery issues on my samsung a5. Would like to see time shortened from 15 minutes to 1 or 2 minutes and warn me when I'm close to someone would be much better so I can move away. Otherwise it's fine. Can't see the point of having it if it waits 15 minutes to say I've been close to someone that's not good.<br> :date: __2020-09-14 00:47:04__

> A,s<br> :date: __2020-09-13 08:18:43__

> I have the internet connection. Covid app says no connection.???<br> :date: __2020-09-10 05:19:39__

> Okay dont mind it<br> :date: __2020-08-29 12:30:32__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> Well its ok and all its just 2 major problems. 1 absolutely battery drainer 2 absloute data drainer<br> :date: __2020-09-30 06:23:11__

> Obliterates my battery even when I'm working from home and don't leave the house all day (so wouldn't expect a lot of Bluetooth handshakes going on). Also seems to interfere with Bluetooth connections to already paired devices intermittently.<br> :date: __2020-09-24 14:25:51__

> Finding since the last update, battery usage has tripled.<br> :date: __2020-09-24 10:44:19__

> I realise it might not be your fault, more Google's permission issues but making me leave my location and Bluetooth on is a security risk I find unacceptable. Granted its not as bad as dying from a incurable disease so you get one star back.<br> :date: __2020-09-24 04:36:23__

> Does not work switch off all the time<br> :date: __2020-09-24 03:28:33__

> Interferes with garmin and resimed devices<br> :date: __2020-09-23 17:26:21__

> Would like to see how many "close contacts" this thing has picked up and even a dashboard somewhere showing nationwide app performance- case numbers are available elsewhere on the net. And yeh, the gps requirement is a worry.<br> :date: __2020-09-21 13:17:05__

> Ofx 777<br> :date: __2020-09-21 09:23:07__

> Unrefined. Doubtful functionality.<br> :date: __2020-09-21 04:55:18__

> App impacts bluetooth audio to car when near other phones<br> :date: __2020-09-20 06:44:45__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> Crashes as soon as it starts. I have submitted multiple reports.<br> :date: __2020-10-02 01:09:20__

> Battery settings keep changing<br> :date: __2020-10-02 00:16:36__

> Tried to do the right thing, installed and used the app. App unable to function without access to location data. Website says location data is not required. Adding my location data to the already questionable database is a deal breaker.<br> :date: __2020-10-01 09:56:55__

> Not enough update. The app drains battery consistently.<br> :date: __2020-10-01 08:22:15__

> This app was never supposed to need your location!<br> :date: __2020-09-30 21:55:13__

> My brand new phone keeps switching it off.<br> :date: __2020-09-30 07:17:09__

> Severely interfered with the Bluetooth performance on my phone, making my headphones nearly unusuable.<br> :date: __2020-09-29 03:54:53__

> When I have WIFI on, it says "No Internet Connection" but running on a mobile without WIFI, it connects. Why? My WIFI has internet connection, but this COVIDSafe app refuses to use it. Seems pretty stupid to me, that it can't connect for updates etc...<br> :date: __2020-09-28 07:08:50__

> Android needs location for Bluetooth to work. No, it doesn't. Bluetooth works fine on my Android device without location turned on for all other apps and services. Uninstalled.<br> :date: __2020-09-27 16:44:57__

> For a government app I would have expected better...<br> :date: __2020-09-27 12:08:33__


