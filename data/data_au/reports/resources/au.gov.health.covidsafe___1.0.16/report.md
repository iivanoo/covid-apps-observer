# COVIDSafe
App version ``1.0.16``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="COVIDSafe icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | COVIDSafe |
| **Unique identifier** | au.gov.health.covidsafe |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=au.gov.health.covidsafe](https://play.google.com/store/apps/details?id=au.gov.health.covidsafe) |
| **Summary**  | COVIDSafe is a community-based way to stop the spread of COVID-19. |
| **Privacy policy** | [https://www.health.gov.au/using-our-websites/privacy](https://www.health.gov.au/using-our-websites/privacy) |
| **Latest version** | 1.0.16 |
| **Last update** | 2020-05-04 13:47:21 |
| **Recent changes** | Updated design<br>Bug fixes |
| **Installs**  | 1,000,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 25, 2020 |
| **Size**  | 6.0M |
| **Supported Android version**  | 6.0 and up |

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
| **Website**  | [https://www.health.gov.au/resources/apps-and-tools/covidsafe-app](https://www.health.gov.au/resources/apps-and-tools/covidsafe-app) |
| **Email** | support@COVIDSafe.gov.au |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Australian+Department+of+Health](https://play.google.com/store/apps/developer?id=Australian+Department+of+Health) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Android10, version 10 (API level 29) |
| **Effective target Android version**  | Android10, version 10 (API level 29) |
| **Minimum supported Android version**  | Marshmallow, version 6.0 (API level 23) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>BLUETOOTH_ADMIN** | Normal | Allows applications to discover and pair bluetooth devices. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>REQUEST_IGNORE_BATTERY_OPTIMIZATIONS** | Normal | Permission an application must hold in order to use Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | stackoverflow.com | Stack Exchange, Inc. | :us: US | 2003-12-26 19:18:07 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |


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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **10041** rated the app and its average score is **3.6407669**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 5451

:star::star::star::star:: 840

:star::star::star:: 739

:star::star:: 709

:star:: 2300

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> Not atm<br> :date: __2020-05-10 11:52:52__

> Just get it guys! Then we can get drunk again! By not getting it you are taking away fun! They are not tracking you for personal gain... Please remove the tin foil hats and get it! Do it for me! I need some Gin!!!<br> :date: __2020-05-10 11:29:16__

> It good<br> :date: __2020-05-10 11:19:47__

> Works as advertised. Data stays in the device until you personally authorise upload of information. Can't fault this app to help get us back to normal life. Contrary to what some are saying, it had almost zero effect on battery. I can only assume that people complaining about battery are trying to push their barrow to stop other people using the app.<br> :date: __2020-05-10 10:51:08__

> Excellent app ! However, my phone has an annoying habit of constantly turning off the Bluetooth function ( with no input from me ) . Extremely irritating , but I will try and sort it out. Not sure if anyone else having similar problems ???? Still having problems with my Motorola / Lenovo Moto G4+ and the bluetooth switching off all the time.<br> :date: __2020-05-10 10:19:51__

> Very good<br> :date: __2020-05-10 09:59:32__

> Easy<br> :date: __2020-05-10 08:24:44__

> Oh yes i love this app absolutely beautiful<br> :date: __2020-05-10 06:45:07__

> Everything seems to be working except it's not showing up when doing a scan to find it.<br> :date: __2020-05-10 06:13:14__

> Problem on Moto 3G, generally, it seems to work ok, but, on two or three occasions it goes haywire, it comes up with a modal popup "Unfortunately Bluetooth share has stopped" The popup keeps poping up faster than I can OK it.<br> :date: __2020-05-10 01:29:20__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> Works pretty well. Would prefer it if the symbol would go away from the top of the phone. Type A's hate that. Considering deleting it to get rid of the icon.<br> :date: __2020-05-10 10:37:08__

> Minor issue with Bluetooth headphones cutting out in crowded areas.<br> :date: __2020-05-10 08:50:25__

> appreciate the updates<br> :date: __2020-05-10 05:52:10__

> Installed and works ok on Samsung Galaxy J5 pro with Android 9.<br> :date: __2020-05-10 03:12:56__

> 5j k5jj55555555555555555555 55555555⁵555555555555555556224555555555555555555555j5555555555 5555555555555555555555555565555555555555555555555555555555555555555<br> :date: __2020-05-10 02:46:56__

> New update offers much better stability.<br> :date: __2020-05-09 13:55:34__

> The app does not work tried to download it 3 times<br> :date: __2020-05-09 07:19:40__

> Happy with the premise of the app, but it interrupts the use of my Bluetooth speaker and headphones so I've had o emporsrily uninstall it. Can this be looked into please?<br> :date: __2020-05-09 04:03:10__

> Possibly life saving<br> :date: __2020-05-09 03:45:41__

> Up to date info.<br> :date: __2020-05-09 01:44:11__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> If there is a chance the app can save lives it's worth the bugs. Yes it compromises other Bluetooth connections and battery usage slightly increases, but both are preferable to death. And to those concerned about 'giving away' your location; you gave that away when you bought a mobile phone.<br> :date: __2020-05-10 03:10:44__

> Since installing the app my Bluetooth earphones seem to be a bit glitchy.. The sound is very broken with short pauses in between. A friend experiences the same (both Samsung, but different brands of earphones).. Would be great to get this fixed. It is pretty annoying.<br> :date: __2020-05-10 00:44:18__

> I had to uninstall temporarily to use my skullcandy headphones as the Bluetooth kept cutting the music out, my husband didn't have the same problem with his Bose Bluetooth headphones, both using Samsung Galaxy S9.<br> :date: __2020-05-09 23:39:59__

> It chews through the battery usage. Have to recharge through the day as well as at night. Other than that, it just sits there unobtrusively in the background.<br> :date: __2020-05-09 13:42:17__

> No negative or positive experience with the app as yet.<br> :date: __2020-05-09 12:04:54__

> I downloaded this app ok but when I started the registration procee I fould it up somehown the I uninstalled the app so I could start all over but no I dont know how the reload the app. I am 88 years of age and not very computer literate<br> :date: __2020-05-09 11:17:25__

> Stops me playing my music via Bluetooth in the car. Keeps turning my music player on to pause. Damn annoying<br> :date: __2020-05-09 11:07:33__

> Want to have this app but it interferes with Bluetooth devises like headphones and speakers, causing them to glich regularly while trying to listen to things.<br> :date: __2020-05-09 10:16:44__

> Why does the app now require location setting to work where before it only required Bluetooth?<br> :date: __2020-05-09 06:13:24__

> Told you don't need to put in name, app demands first and last. Requires postcode for unknown reasons given it tracks you. Requires Bluetooth location data because app is locating you. App ToS tells a different story to ScoMo. Keep alive notification is obnoxiously coloured bright green for no clear reason<br> :date: __2020-05-09 05:08:55__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> Compeltey drains the battery life on your phone<br> :date: __2020-05-10 11:45:32__

> Totally 100% agree with everyone using this app, please work on improving the app to eliminate existing interruption to other bluetooth software. It's irritating!<br> :date: __2020-05-10 08:49:38__

> The app disappears from the background or deactivates automatically after some time. I realize this happened many time... I had to start the app again manually. I may have went out without realizing the app has died and it would not record my movement.<br> :date: __2020-05-10 08:31:23__

> Bluetooth music to my jbl bluetooth speaker has very annoying drop out very 30 seconds or couple of minutes with this app running<br> :date: __2020-05-10 06:29:28__

> Hmm not sure about this app. Hate that it has a permanent notification. So annoying and pointless, just run in the background. Won't appear in the app store on my parents phone and they are elderly and need it. Once again, not good enough.<br> :date: __2020-05-10 04:45:43__

> All was good till this last update. Now it says I'm not connected and to check permissions. I did and it still didn't work.. I restarted my phone but that didn't help either. I just uninstalled and reinstalled it seems to have worked<br> :date: __2020-05-10 00:25:22__

> When running in the back ground battery optermizer keeps dropping out and app stops working<br> :date: __2020-05-09 06:57:04__

> Easy sign up and was happy to have it but had to uninstall as not working the battery approval keeps turning app off so then it doesn't work have heard other oppo phones are having trouble too please look at fixing as would really like to have it working properly as the idea is good<br> :date: __2020-05-09 05:20:54__

> Have to turn bluetooth off to use wifi for some reason now when at home why I'm not sure. Will forget to turn on/off eventually. Have to allow my location which gives my home address. Been trying to avoid this ever since coroner spolated evidence to cover-up how sister met her end but now this is open info. To what ever gov agency wants location. Born to be hunted. Just don't go wife and kids.<br> :date: __2020-05-09 02:36:33__

> this app is a major drain on your battery life<br> :date: __2020-05-08 19:32:32__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> Every time i try to get a pin it tells me to get the internet. But it was download through the net.<br> :date: __2020-05-10 12:05:06__

> Can't play music over Bluetooth without it pausing at frequent intervals (3-4 times per song at least) tried on two seperate Samsung's and does it on both<br> :date: __2020-05-10 11:42:28__

> Useless won't let me register<br> :date: __2020-05-10 10:29:36__

> Installed no problem on S9, but I have a smart watch BT for tracking 24/7 in case of seizure when away from home & BT headset to make/receive calls, App disconnects headset or watch to handshake other phones all the time. Had to uninstall it.<br> :date: __2020-05-10 07:37:41__

> Spent over 30 mins, got issued with 4 "6-digit codes" - NONE of which were acceptable ie none "worked". SO! thanks but no thanks, get your System to work, not just for Astronauts!! WHAT a waste of time this was!!<br> :date: __2020-05-10 07:36:25__

> I installed this app, and through the setup process it informed me that for it to work, it is mandatory for me to give my permission for it to access my location. A major red flag for me, so i like many others will be uninstalling this app immediately after i submit this review. They say that it's an Android thing, but i have other apps that use bluetooth without requiring my location. It's a liberal party lie. They say xx people have downloaded it, i bet that number doesn't reduce when deleted<br> :date: __2020-05-10 05:59:27__

> When active the app interferes with connected bluetooth devices.<br> :date: __2020-05-10 05:27:04__

> idk<br> :date: __2020-05-10 04:56:44__

> Poor<br> :date: __2020-05-10 04:43:29__

> It doesn't recognise my mobile number as valid. Followed all the instructions to fix it but no dice.<br> :date: __2020-05-10 04:37:18__


