# COVIDSafe
App version ``2.5``

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
| **Latest version** | 2.5 |
| **Last update** | 2021-04-08 01:30:27 |
| **Recent changes** | Minor bug fixes and changes |
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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **17742** rated the app and its average score is **3.7339957**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 9254

:star::star::star::star:: 2379

:star::star::star:: 1664

:star::star:: 1028

:star:: 3417

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> Easy to use<br> :date: __2021-05-01 14:04:49__

> We<br> :date: __2021-05-01 07:21:45__

> Feel safe ,04/21 Had astro Seneca jab slight headache ist day tip of nose dripping 2nd day .After jab had energy I saw freedom and hope for for all our neighbours,I trust all the Worlds Scientists that make the vaccines and health ministers only ,my next astro Seneca jab is June Then long term protection is done.take care godbless .🌈👪🌅⛑️🎁🙋✨🌼<br> :date: __2021-05-01 05:23:39__

> Good<br> :date: __2021-04-30 12:11:51__

> It is important to have a state and national approach to this pandemic.Better to have this in place, rather than nothing set up. Keep everyone safe.<br> :date: __2021-04-30 05:28:06__

> All good easy<br> :date: __2021-04-30 05:10:13__

> App now working for me<br> :date: __2021-04-30 00:30:59__

> Feel safe with covidsafe app<br> :date: __2021-04-29 21:10:16__

> It's been there helpful in my travel plans<br> :date: __2021-04-29 00:55:51__

> Easy to use.<br> :date: __2021-04-28 12:23:20__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> b0<br> :date: __2021-04-28 09:37:29__

> Arexff<br> :date: __2021-04-28 02:08:56__

> Very good<br> :date: __2021-04-28 00:32:38__

> Satisfied<br> :date: __2021-04-26 01:21:15__

> Turn it on when I leave the house. Can't have it on at home because partner also has his turned on and it kills my battery constantly connecting the two of us. Turning it off means I cant use anything that needs bluetooth. Should be able to tell it when your home and to stop connecting with someone else in your home so you can have it turned on without killing your battery<br> :date: __2021-04-25 09:08:10__

> Useful information but would be better if had relevant vaccination details ie where you can get vaccinated how when etc.<br> :date: __2021-04-25 04:22:27__

> None yet<br> :date: __2021-04-24 08:04:39__

> Just runs in the background, great little app for tracking your movements to ensure you are alerted if a covid victim has been in your vicinity.<br> :date: __2021-04-23 16:22:37__

> Good<br> :date: __2021-04-22 02:36:19__

> Easy to use and appears to be ok.<br> :date: __2021-04-22 01:58:13__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> Not sure it is working<br> :date: __2021-05-01 11:48:40__

> Disappointing. I used this from the word go as I believe it to be a useful tool for its purpose. In the last ?week? or so it has been responsible for massive power drains to the point my phone switched off. The last episode was 70% power usage, yesterday, so unfortunately it is gone.<br> :date: __2021-04-30 01:29:57__

> Ok app, simple to use. Dont like that the camera keeps locking up, so need to close app and try again<br> :date: __2021-04-29 13:08:42__

> I found this App instructions to be reasonably ok to follow☺..And I hate using phone for anything..But it's for humanity?.😕<br> :date: __2021-04-27 21:55:50__

> Sometime difficulty scanning<br> :date: __2021-04-27 10:29:05__

> A failure, due to insufficient uptake! Hey, fools, THIS APP DOES NOT TRACK YOUR MOVEMENTS!! You can easily verify this with Settings/Location/Recent. What's your excuse for not using the app now, you idiots? Also, you can force stop the app when not in use to help prolong battery life...<br> :date: __2021-04-26 11:33:22__

> Average<br> :date: __2021-04-26 09:51:55__

> I like how this keeps you safe from covid. I do wish it had covid testing where you put your finger on the screen and tells you if you have covid.<br> :date: __2021-04-24 16:05:28__

> What I don't understand is why are there separate check in Apps should they all link?<br> :date: __2021-04-23 14:33:35__

> Easy, must say... .<br> :date: __2021-04-23 09:01:43__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> I iPhone to see the money in the bank not it's been 4 years stop dragging<br> :date: __2021-05-01 07:23:23__

> So so a pointless app when you have to use service N.S.W to check in everywhere<br> :date: __2021-04-28 23:02:58__

> The latest update has stuffed up battery usage. I work in a large organisation and 8 hours of background usage chews up 43% of battery of my Samsung Note 9. I literally have to keep my phone plugged all day at work. This needs to be fixed ASAP.<br> :date: __2021-04-28 08:14:42__

> Always when I want to use it....it needs to be updated<br> :date: __2021-04-28 07:00:21__

> Doesn't work on old phones<br> :date: __2021-04-28 01:45:55__

> What does it actually do? Does it even work?<br> :date: __2021-04-24 09:14:11__

> The new update drains my phone battery. I charged before I slept and it went from 100% to 46% overnight. I've removed the app<br> :date: __2021-04-24 07:41:57__

> A wasted opportunity. This app should have included a single consistent venue registration system and give feedback to tbe users about how many/new contacts they are accumulating, so that we can improve our social distancing.<br> :date: __2021-04-23 10:33:01__

> As much as I like the idea of this app, it started using a lot of battery recently. Uninstalling.<br> :date: __2021-04-23 08:17:27__

> I don't see the point. Only works if I activate it and sorry but that's not always the most important thing I think of when out and about. Would be useful if always activated!<br> :date: __2021-04-21 13:14:51__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> It doesn't do anything!<br> :date: __2021-05-01 12:45:54__

> It was ok, but since last update started eating my battery, which is the one thing an app like this should absolutely avoid. Uninstalled.<br> :date: __2021-05-01 05:26:13__

> Other than wasting tax $$, this app didn't achieve anything on a federal level and on a personal level it simply drained my battery.<br> :date: __2021-04-30 16:00:15__

> Drains battery since latest update<br> :date: __2021-04-30 15:09:00__

> Doesn't seem to be able to trace very well..<br> :date: __2021-04-30 08:22:49__

> Total waste of time, does nothing.<br> :date: __2021-04-30 07:00:06__

> What experiance<br> :date: __2021-04-30 04:12:58__

> Uses too much processor<br> :date: __2021-04-29 09:53:07__

> Dosent work<br> :date: __2021-04-29 09:24:07__

> Waste of space<br> :date: __2021-04-28 23:55:42__


