# COVIDSafe
App version ``2.0``

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
| **Latest version** | 2.0 |
| **Last update** | 2020-12-18 09:16:28 |
| **Recent changes** | This release introduces the new Herald Protocol that improves COVIDSafe&#39;s ability to capture close contacts and keeps users better informed about important COVID-19 information.  |
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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **13917** rated the app and its average score is **2.7911618**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 4394

:star::star::star::star:: 1190

:star::star::star:: 1200

:star::star:: 1379

:star:: 5754

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> ... Ok l. Og<br> :date: __2021-01-15 05:41:15__

> Great<br> :date: __2021-01-15 02:57:42__

> Good if it is used as intended<br> :date: __2021-01-14 22:48:44__

> A very necessary app, indeed. It has played a major role in containing this pandemic by informing citizens of needed information for precautionary measures. Thanks to the Morrison Government and the team that founded this app.<br> :date: __2021-01-11 07:54:45__

> Make it easy to get updates on covid19 cases<br> :date: __2021-01-10 23:31:33__

> Best thing the government did.<br> :date: __2021-01-09 23:47:43__

> They're not lying on the only thing I have a great day and I have to do the same to be a good idea and you please confirm receipt<br> :date: __2021-01-05 15:44:31__

> Good application<br> :date: __2021-01-05 03:37:02__

> This needs to incorporate the ability to use QR code scanning in addition to the existing features. I avoid QR checkins due to the fact that none of the data is regulated in any way and there are just too many providers. If it could be incorporated in to the app itself it means only one registration and the QR scanning is simply to verify precisely your location at a specific time. If the QR logins can be available to contact tracers in real time it would greatly simplify the process. A notification can be sent to the user of the app that someweher they have checked in to is now an exposure site and the remaining data can be uploaded.<br> :date: __2021-01-05 00:26:52__

> Very good<br> :date: __2021-01-04 23:32:47__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> App has started to drain my battery.... When it first came out I installed it and it only used about 1 to 2% battery in a day but now it's over 20% of my battery and I can not get a full day's use out of my phone as of this I might have to delete it as what is the point of havin git if I can not use my phone anyway if it's flat<br> :date: __2021-01-07 10:05:45__

> Great idea. Originally I couldnt keep the app open on my Oppo phone but I finally solved it. I turned off all the battery saving features as described on the Covidsafe help page, but the missing link was on the open app page, you have to swipe down on Covidsafe to lock the app. This prevents Oppo's aggressive battery management from shutting it down.<br> :date: __2021-01-06 11:49:27__

> Had similar battery issues like many others here. But clearing the cache, uninstalling and reinstalling, worked wonders. My phone now lasts more than a day again.<br> :date: __2021-01-05 11:05:05__

> Very sound<br> :date: __2021-01-05 06:10:56__

> This app does not alert to not being active or requiring an update unless you actually open it...should be better than this.. Update 21 12 20 just got my 1st alert to an update being available..much better<br> :date: __2020-12-21 08:05:41__

> Seems ok<br> :date: __2020-12-21 08:04:09__

> It's a nessasary for the Government to have this, if those that think it's not real, well it's very real so it's an a Must cheers<br> :date: __2020-12-20 23:49:00__

> Works perfectly. Would be 5 star if it didn't stop when it needed an update.<br> :date: __2020-12-20 08:40:56__

> good<br> :date: __2020-12-18 02:03:55__

> Y ?<br> :date: __2020-12-10 10:29:29__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> Drains the battery way to fast<br> :date: __2021-01-12 05:39:33__

> 2h🥰🐪but<br> :date: __2021-01-10 23:35:48__

> It is killing my battery recently.<br> :date: __2021-01-09 06:39:25__

> Something seems to be seriously wrong with the current version. I was woken up this morning by my phone buzzing as it turned itself off due to 0% battery. It was 90%+ less than 7 hours ago. Battery manager shows it was the Covidsafe app that caused it. It has always hit my battery fairly hard but it's getting ridiculous now. (Update) Uninstalling, reinstalling, and clearing the cache seems to have helped. Next night I went from 100% to 83% in ~ 7 hrs.<br> :date: __2021-01-06 22:58:44__

> The user interface is great but the app has been running my battery flat overnight so I uninstalled it and gave a 3 start rating.<br> :date: __2021-01-05 12:36:55__

> C.<br> :date: __2021-01-04 09:33:25__

> ( edited for later versions) uninstalling. No.one i know is still using it. I don't trust its status or capacity anymore. Maybe if its refreshed and included the QR functionality. Bye.<br> :date: __2021-01-03 12:19:41__

> Battery issue, I have revert back to old version, rather latest version. Please fix the battery using too much issue, so i can update.<br> :date: __2021-01-02 07:36:13__

> Never been notified of any cases or update<br> :date: __2021-01-01 06:46:10__

> App should include a unique personalised QR code for venues to scan, much easier than the current system and would remove the issues with incorrect data entry when entering facilities. As many others have reported Bluetooth drains battery so too tempting to turn if off<br> :date: __2020-12-31 23:37:22__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> App definately causes bluetooth to drop out and high battery usage.<br> :date: __2021-01-16 07:40:15__

> Battery drain issues after update consuming between 20 and 40% of a full battery charge consistently on S20 ultra.<br> :date: __2021-01-16 03:47:24__

> Latest version destroys your battery. Was good until this week.<br> :date: __2021-01-15 08:41:23__

> Been running ok for the past several months but had to uninstall due to it draining my battery while in stand by. Couldn't get through the day not using my phone<br> :date: __2021-01-14 15:21:38__

> The most recent update is draining about 15-20% per day. Please fix<br> :date: __2021-01-13 13:35:31__

> No contacts found by this app apparently<br> :date: __2021-01-13 08:19:08__

> Working well until past week when it started draining my battery. Have uninstalled<br> :date: __2021-01-13 01:31:57__

> Uses 15% of my battery per day. More than any any other app I have. More than even my screen uses per day. Can no longer make it through the day on a single charge.<br> :date: __2021-01-12 20:07:51__

> * Update 12/1/21 I was wondering what was sucking up my battery. 21% in 12 hours, fix or it stays uninstalled. *Update 5/5* Have been using this since its release. Couple of things to clarify: With Android it does ask for location services - this is to activate the Bluetooth constantly on initial install, it does not track you by location Battery drain is almost non existence, about 1.5% every day - I work in Hospitality so come in contact with a lot of people so a lot of pings<br> :date: __2021-01-12 09:49:03__

> I thought my phone was faulty with the unmissable increased battery usage. After checking battery usage saw it was this app. Checked the app comments and glad I wasn't going crazy. I want to keep using it and believe in the purpose but if it keeps functioning like this I can't keep charging my phone 2-3 times a day. Please find alternative to latest update, thanks in advance development team 👍🏻<br> :date: __2021-01-11 12:11:35__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> Sorry. I want to help with covid and was one of the first adopters. But it's killing my battery. Half the time I'm out, my phone is off because the battery died so the app is essentially useless.<br> :date: __2021-01-16 05:30:17__

> Uses up most of my battery<br> :date: __2021-01-16 05:01:41__

> Downloaded no explaining how to use it. Now what.do i do<br> :date: __2021-01-16 03:12:28__

> Had to remove it because of the extreme battery usage.<br> :date: __2021-01-16 01:26:06__

> Will not accept mobile number<br> :date: __2021-01-16 00:56:05__

> Why does the app now require location setting to work where before it only required Bluetooth? Battery drain too. You want people to use it, so make it easier. Otherwise no one gonna use it.<br> :date: __2021-01-16 00:08:59__

> As with others, it's killing my battery. The gps is active permanently. Please take note.<br> :date: __2021-01-15 11:38:14__

> 51% of my battery usage on my S10+. I've gone from 100% battery at 6.10am to 21% battery at 4.37pm and have been flat out at work all day, haven't read any Facebook notifications or anything. I'm uninstalling this, you can run another marketing campaign when you fix it.<br> :date: __2021-01-15 07:38:53__

> Joining the crowd of users experiencing very high battery consumption (and Bluetooth app crashes) with this update. Devs need to acknowledge this issue and not dismiss the battery issue as is currently occurring on the github page for the app. Will be uninstalling until resolved :(<br> :date: __2021-01-15 05:18:13__

> It's draining about 25% battery. This app is using max battery when compared with other apps on my phone.<br> :date: __2021-01-15 01:04:28__


