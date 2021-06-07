# COVIDSafe
App version ``2.7``

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
| **Latest version** | 2.7 |
| **Last update** | 2021-06-04 06:03:39 |
| **Recent changes** | Improved support for international visitors, minor content and bug fixes. |
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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **19864** rated the app and its average score is **3.7760296**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 10416

:star::star::star::star:: 3033

:star::star::star:: 1654

:star::star:: 1075

:star:: 3686

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> chewing battery and use QR codes now..but it was great and good info and I trusted it<br> :date: __2021-06-06 13:17:27__

> Quiet useful<br> :date: __2021-06-06 12:58:20__

> Absolutely love this anywhere anytime<br> :date: __2021-06-06 10:41:17__

> Good app<br> :date: __2021-06-06 08:52:55__

> Very useful for everyone. If you don't know DON'T GO.. It's the app which keeps you notified<br> :date: __2021-06-05 09:56:35__

> REAL TIME UPDATES well done,<br> :date: __2021-06-05 08:41:58__

> We all need CovidSafe<br> :date: __2021-06-03 09:52:28__

> Good product all helps<br> :date: __2021-06-03 09:37:17__

> Let's all do our bit?<br> :date: __2021-06-03 01:40:52__

> Excellent<br> :date: __2021-06-02 14:50:24__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> It's seamless<br> :date: __2021-06-06 11:06:47__

> Does not always work<br> :date: __2021-06-06 09:45:56__

> Good, does the job. Not draining battery on my phone: 6% for over a day. Would be nice to see local transmissions as well as total cases per day. Update: latest version is now using way more battery: 23% at last count<br> :date: __2021-06-05 23:49:53__

> Easy to use<br> :date: __2021-05-28 10:58:03__

> Best options<br> :date: __2021-05-26 06:59:52__

> Depends on WiFi where ever you go<br> :date: __2021-05-26 05:24:01__

> It does what it says with no hassles so happy days<br> :date: __2021-05-24 16:29:19__

> All good<br> :date: __2021-05-24 09:37:08__

> Hangs when no internet available, possibly resolved by now.<br> :date: __2021-05-24 06:44:11__

> una me to get this app to work<br> :date: __2021-05-23 03:24:04__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> I don't understand why I always have to manually update this app. I have finally uninstalled it because as far as I understand it has contributed precisely nothing to any contact tracing efforts in Australia during any outbreak, and with mandatory check-ins now in place in Victoria for venues, I feel there is little reason to continue having this taking up space on my phone and notifications screen.<br> :date: __2021-06-06 04:43:27__

> Well, umm, its an app, and its on my phone. Of course I have no idea if it works or if its any good, but if it makes the life of a contact tracer easier and potentially reduces spread then ok lah<br> :date: __2021-06-04 16:23:43__

> I'm frustrated that it's not up to date, when I check.<br> :date: __2021-06-04 08:28:27__

> Not good for information it just sends you to the gov website. We already know to go to the website, I thought this would have all covid info at one touch. Disappointing.<br> :date: __2021-06-02 23:35:47__

> Contact Tracing. Is there evidence or proof of this App being used, to any advantage, by any State & Territory Health Dept's. If not, should I disable or remove it & rely only on QR Codes I capture?<br> :date: __2021-05-31 05:37:50__

> YOUR A DAY BEHIND ITS 30TH TODAY AND COVIDSAFE SAYS 29TH<br> :date: __2021-05-30 03:50:15__

> Nothing has happened to experience. I would like to know if it has been useful to contact tracers?<br> :date: __2021-05-29 11:38:35__

> Cannot find clear statistics for regional Victoria. Like many Victorians I do not reside in Greater Melbourne. I had expected clear information pertinent to me. I do have a vote!<br> :date: __2021-05-29 05:58:20__

> Its a little slow to react but over all it does work.<br> :date: __2021-05-29 05:56:12__

> Why can't the Covid safe app "handshake" with a device at venues where currently a QR scan us required?<br> :date: __2021-05-26 22:25:19__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> Dismal<br> :date: __2021-06-05 09:53:06__

> v2.6 prevents my phone from going to deep sleep which resulted in more battery drain. I have to resort to finding the older v2.5 and my phone can now have a more normal battery life.<br> :date: __2021-06-03 11:02:22__

> Didnt do anything.<br> :date: __2021-06-03 02:32:27__

> Iv.<br> :date: __2021-05-31 07:30:09__

> I like the idea of this app, I want to help keep myself and others safe, but it's 10 am and my battery is at 44% after having my phone sitting in my desk unused. Battery monitor says this app has used 33% of the battery usage so far. Uninstalling.<br> :date: __2021-05-31 02:35:53__

> What a waste<br> :date: __2021-05-30 09:27:22__

> If this app worked we wouldn't be doing QR code scans. Go figure.<br> :date: __2021-05-29 01:36:48__

> Ever since the update it drops out whenever I'm in town. Works best at home on my wifi, but as soon as I switch to data, it drops out at random times. Not very safe.<br> :date: __2021-05-28 04:12:29__

> Im hoping that this update is going to work, my covid app , wouldn't scan, kept coming up with the red alert,this started last friday, switching phone off didnt do a thing,.<br> :date: __2021-05-24 06:27:02__

> Latest update of May is causing phone battery drainage. It is responsible for 50% of battery usage and phone needs charging twice everyday. I have a brand new Samsung phone.<br> :date: __2021-05-24 02:34:47__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> Ducking useless<br> :date: __2021-06-06 12:39:12__

> It's done nothing. All announcement and no result<br> :date: __2021-06-06 11:43:00__

> Not very accurate im sorry to say<br> :date: __2021-06-05 13:21:28__

> Useless<br> :date: __2021-06-05 10:12:49__

> Why????? Does anyone actualy use this?<br> :date: __2021-06-05 09:13:24__

> Will not stay open.<br> :date: __2021-06-05 06:46:18__

> Some twerp thinks I can find your code in a few minutes!! 85 year old!!!<br> :date: __2021-06-05 05:37:03__

> Have a new phone. Tried to open app and was told my No had been used on too many phones. Tried to fix up. Would not accept anything so Uninstaller it. Tried to reinstall but it just sits spinning a circle and saying "pending". I'll probably die from covid before it installs. I give up and won't have this app. I tried!!<br> :date: __2021-06-05 03:19:00__

> Closes by itself. Have yet to get an appropriate alert and yet have visited an exposure site<br> :date: __2021-06-04 10:48:57__

> It crash won't down load .<br> :date: __2021-06-04 09:24:35__


