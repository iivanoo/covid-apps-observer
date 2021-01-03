# GuideSafe
App version ``v1.3``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="GuideSafe icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | GuideSafe |
| **Unique identifier** | gov.adph.exposurenotifications |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=gov.adph.exposurenotifications](https://play.google.com/store/apps/details?id=gov.adph.exposurenotifications) |
| **Summary**  | A future safe from COVID-19 is in all of our hands with Alabama’s GuideSafe app. |
| **Privacy policy** | [https://www.guidesafe.org/privacy-statement/](https://www.guidesafe.org/privacy-statement/) |
| **Latest version** | v1.3 |
| **Last update** | 2020-09-11 17:33:27 |
| **Recent changes** | Spread the app, not COVID. For this version of the GuideSafe™ app, we&#39;ve made some minor improvements to help you better understand exposure dates and what to do if you receive an exposure. |
| **Installs**  | 50,000+ |
| **Category** | Medical |
| **First release** | Aug 12, 2020 |
| **Size**  | 2.3M |
| **Supported Android version**  | 7.0 and up |

### Description
> Use the GuideSafe™ Exposure Notification app to anonymously share a positive COVID-19 test result — and be anonymously notified of your own possible exposure to someone who later reports a positive COVID-19 test result — all without sharing anyone’s identity. The app protects your privacy while giving you the power to protect your health, your family’s and your community’s. 
<br> 
<br>Using the app is easy: 
<br>Step one: Download the GuideSafe™ Exposure Notification app and enable Bluetooth. 
<br>Step two: If you have tested positive for COVID-19, you can choose to report it. Your test will be verified by the Alabama Department of Public Health. 
<br>Step three: Those who may have been in close contact with you in the last 14 days will be notified they were near someone with a positive test, but they won’t know who or where. Your identity and location remain completely anonymous, and your personal information isn’t disclosed, no matter what. 
<br> 
<br>Why it’s important 
<br>Stopping the spread of COVID-19 is essential to helping our communities, schools and businesses reopen and stay open. When someone tests positive for COVID-19, contact tracers with the Alabama Department of Public Health will help notify those the person has been near — but they won’t know every person’s close contacts. The more people who use the app, the better the ability to notify those who have been exposed. 
<br> 
<br>How it works 
<br>When you are within about six feet of others, phones using the GuideSafe™ Exposure Notification app exchange encrypted, anonymous codes via low-energy Bluetooth. If you test positive for COVID-19, those with whom you came in close contact — defined as within six feet for at least 15 minutes over the last 14 days — will get an anonymous notification that they were exposed. The notification they get is completely anonymous — they will not know who tested positive, the time, or the location — only the date of the possible exposure. 
<br> 
<br>Your privacy is our priority 
<br>The GuideSafe™ Exposure Notification app was developed by the Alabama Department of Public Health in cooperation with the University of Alabama at Birmingham and MotionMobs, using technology from a collaboration between Apple and Google. Users of the app exchange anonymous codes among their phones using Bluetooth — no location data is ever stored or exchanged, and your personal information is never shared.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 


## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Alabama Department of Public Health |
| **Website**  | - |
| **Email** | alabamapublichealth@gmail.com |
| **Physical address**  | [201 Monroe Street Montgomery, Alabama 36104](https://www.google.com/maps/search/201%20Monroe%20Street%20Montgomery,%20Alabama%2036104) (Google Maps) |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Alabama+Department+of+Public+Health](https://play.google.com/store/apps/developer?id=Alabama+Department+of+Public+Health) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Android10, version 10 (API level 29) |
| **Effective target Android version**  | Android10, version 10 (API level 29) |
| **Minimum supported Android version**  | Nougat, version 7.0 (API level 24) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | guidesafe.org | Contact Privacy Inc. Customer 1247737132 | :canada: CA | 2020-07-18 15:39:08 |
 | azure-api.net | Microsoft Corporation | :us: US | 2014-01-09 14:55:23 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | azureedge.net | Microsoft Corporation | :us: US | 2014-01-22 16:14:52 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address ': ; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Lg/a/a/a/a;->c(Ljava/lang/String;)Ljava/lang/StringBuilder;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The GuideSafe app has been installed by more than **50000** times. At this time, **127** rated the app and its average score is **3.3**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 59

:star::star::star::star:: 11

:star::star::star:: 9

:star::star:: 6

:star:: 42

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.adph.exposurenotifications 5 reviews"/>
</p>

> Was good to know about the App<br> :date: __2020-11-28 18:00:06__

> People saying this app is not working what is this used for I will try it anyway if it doesn't work then I'll take it off my phone<br> :date: __2020-11-20 01:08:13__

> Amazing<br> :date: __2020-11-12 13:16:22__

> Eh Um.... HMMM 1# question tho why this app 4 all the phone's?.. Just wondering...<br> :date: __2020-10-27 02:22:20__

> Be. Safe<br> :date: __2020-10-16 04:11:57__

> I don't know it want let me download it<br> :date: __2020-10-13 18:44:15__

> Very nice<br> :date: __2020-10-13 18:03:47__

> Good app<br> :date: __2020-10-13 01:25:16__

> Great Idea. Thank you. It is at the top of my list of worries. With my age and health issues.<br> :date: __2020-10-11 21:28:21__

> Everyone in Alabama needs to download this. It doesn't work at all. If you catch covid and use this app you get to sue the developer as well as the state of Alabama. Definitely a better payout than a stimulus check.<br> :date: __2020-10-11 16:41:29__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.adph.exposurenotifications 4 reviews"/>
</p>

> They should add something for the blind site challenge<br> :date: __2020-12-22 14:23:39__

> Haven't actually tried it out,but the idea it self is brilliant. If everything play the part being identified I will give you five.<br> :date: __2020-12-21 13:33:27__

> When trying to report test results, it only says "Server Failure" and won't allow them to be reported. Makes me very skeptical about others being able to report positive tests and alert others. This app has one very important function and it's failing to do its one job.<br> :date: __2020-12-04 00:17:48__

> The app itself was easy enough to set up. I think most of the issues people are having with this all is not understanding it won't work as accurately if more people don't use it, and people not understanding how the technology works. I will continue to use the app and update my review later.<br> :date: __2020-11-27 07:41:56__

> The Whole Problem With This Is Unless Everyone Uses App Kinda Useless Because No Matter How Many People I Try To Educate On The Importance Of Everyone Doing This No One Sees The Importance ! Needs To Be Mandatory !<br> :date: __2020-11-23 03:04:20__

> Just started the app.<br> :date: __2020-11-04 21:03:09__

> Ok<br> :date: __2020-10-18 23:44:48__

> It works<br> :date: __2020-10-11 15:57:28__

> No issues. Does this share exposure notifications with the other notification apps or only with users of this app?<br> :date: __2020-08-23 14:57:47__

> No issues downloading. I agree with a previous review, it would be more useful if it was utilized by more people. But i do feel better that this tool is avaliable! Thanks.<br> :date: __2020-08-18 14:39:51__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.adph.exposurenotifications 3 reviews"/>
</p>

> I just wish more people used it. I kinda feel like it is not useful since people have to opt in for each aspect... BUT I will keep using it as long as this pandemic drags on. Update: This app is a fail. :( Very disappointed but not surprised at this point. It just stopped updating early Dec. Then 2 days ago it locked my phone up downloading. I had to force close & uninstall to stop it from locking up my phone. I wish this worked better.<br> :date: __2021-01-01 15:38:52__

> Why hasn't it updated since December 13th!?<br> :date: __2020-12-19 00:11:33__

> The app started working wonderfully. But at the end of October, it stopped. No new upgrades and no notifications. I will try and download the app again.<br> :date: __2020-12-06 13:31:12__

> Great if it would work. I tested positive and want to alert others by using the app. When it asks me to verify the code sent to my phone, I can't because it never sends the code. I've tried over and over.<br> :date: __2020-12-01 18:35:17__

> None<br> :date: __2020-11-25 00:11:08__

> Up front everything is bluetooth, bluetooth, bluetooth. Then after install the app demands location, too. Good privacy policy, but I can't leave both bluetooth and location on at all times or my phone would have to stay on the charger 24/7. Maybe my fault for having an old phone. I'll leave it installed and just enable everything as the Austin e demands.<br> :date: __2020-11-18 21:28:03__

> it would be better if it reported an estimate of how many unique devices it detected and has checked itself against just to know it is working and seeing other people with the app.<br> :date: __2020-11-16 17:07:14__

> Giving a 3 star review now because I've not used this app on an Android device. I have both Android and iPhone devices. Upon reading reviews of when using on Android devices, as opposed to iPhone devices, I know my iPhone works in real time notifications. Update was recently done on this application, so I'm going to give it a try. He!l, in reality even it notifying a few days later is better than NOT BEING NOTIFIED AT ALL. I will update with a comparison review. Stay safe, do the right thing masks don't hurt ya, and vote. Truly, Your Fellow American<br> :date: __2020-10-12 15:50:41__

> Works but Annoyed - had this for UAB support, though it kept saying I had been exposed, the problem my phone was charging at the time it said the exposure happened on 2 different days at the same time of day (late Sunday evenings) I didn't go anywhere during those timeframes. It has to be binging off one of my neighbors but I had to quarantine and not attend classes. I've now removed it.<br> :date: __2020-10-04 08:18:57__

> Easy to use.<br> :date: __2020-08-18 01:12:50__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.adph.exposurenotifications 2 reviews"/>
</p>

> Doesn't seem to work. My wife and I both have this installed. She tested positive, I went through the process of telling the app she was positive. And I never received a notification that I had been exposed. I noticed that her bluetooth was off. I turned it back on, waited a couple of days and tried the notification process again and verified that her bluetooth was still on. I still didn't get an exposure notification. I've been a big advocate for this technology... Why isn't it working?<br> :date: __2020-12-18 13:58:55__

> App questionnaire requires email verification, but doesn't work, so don't bother. If that basic feature does not work then how can you rely on it to correctly perform contact tracing?! This is not an in consequential function. Get it right!<br> :date: __2020-09-29 19:27:11__

> It would work better if more people had it on their phones.<br> :date: __2020-08-18 18:54:55__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.adph.exposurenotifications 1 reviews"/>
</p>

> Won't let me report a positive test<br> :date: __2021-01-01 02:38:03__

> This app is pretty much inert. Not enough people using it.<br> :date: __2020-12-31 16:02:49__

> This is from the State of Alabama which means somebody's relative got paid a lot of money to write this piece of.. Install this if you want them to know where you are. Don't install it if you think it's going to protect you from anything. This is Alabama, a State that sued Pennsylvania cuz they didn't like how they voted. The state motto here is "politicians don't care about you." If you were a mask, they think you are communist. Alabama... Ignoring syphilis infections since 19 something.<br> :date: __2020-12-29 21:56:46__

> The app checked for exposure every 24-48 hours when I first installed. In the last month, the app hasn't checked for exposure at all. Uninstalled, reinstalled, checked and rechecked settings and still no exposure check. Uninstalling permanently. Worthless unless it consistently checks for exposure.<br> :date: __2020-12-28 04:22:21__

> Doesn't work!<br> :date: __2020-12-27 08:56:05__

> Doesn't work<br> :date: __2020-12-27 05:25:56__

> My app has not updated exposure checks since November 27th. Is it broken? Should I just uninstall?<br> :date: __2020-12-24 05:58:48__

> No longer working as of November. I have reinstalled it twice and it just shows "never checked for exposure."<br> :date: __2020-12-23 21:54:28__

> The app doesnt do what its suppose to at all unfortunately.<br> :date: __2020-12-23 04:05:02__

> App is a joke if no one is reporting they have covid. Daughter tested postive and i am exposed. App never notified me.<br> :date: __2020-12-19 21:14:34__


