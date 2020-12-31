# WA Notify
App version ``minted14017``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="WA Notify icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | WA Notify |
| **Unique identifier** | gov.wa.doh.exposurenotifications |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=gov.wa.doh.exposurenotifications](https://play.google.com/store/apps/details?id=gov.wa.doh.exposurenotifications) |
| **Summary**  | The official COVID-19 exposure notifications app for Washington |
| **Privacy policy** | [https://wanotify.cirg.washington.edu/privacy-policy](https://wanotify.cirg.washington.edu/privacy-policy) |
| **Latest version** | minted14017 |
| **Last update** | 2020-12-08 18:34:42 |
| **Recent changes** | Bug fixes and performance improvements |
| **Installs**  | 100,000+ |
| **Category** | Medical |
| **First release** | Nov 24, 2020 |
| **Size**  | 10M |
| **Supported Android version**  | 5.0 and up |

### Description
> WA Notify is the official COVID-19 exposure-notifications software for Washington State and Department of Health (DOH). The app is an instance of the Exposure Notifications Express platform developed by Apple and Google and configured by DOH.
<br>Your voluntary use of WA Notify will help anonymously alert you and fellow users in Washington state who may have been near someone with a positive COVID-19 diagnosis. When you enable WA Notify, you are doing your part to help your community slow the spread of COVID-19.
<br>How WA Notify works:
<br>When devices with WA Notify are in close contact, they exchange random identifiers. When someone tells their app they tested positive for COVID-19, other users who received their random identifiers receive an alert that they may have been exposed to COVID-19. Devices receiving random identifiers date-stamp them and record their signal strength so the app can estimate how close the devices were and for how long. Users within six feet for 15 minutes or more of the COVID-positive person are notified that they may have been exposed to COVID-19.
<br>Apple and Google's Exposure Notifications framework runs in the background, even when the WA Notify app is closed. It will not drain the device battery at a rate that would occur with other apps.
<br>How WA Notify Protects Your Privacy:
<br>Washington State Department of Health takes your privacy and confidentiality very seriously. The Apple and Google framework does not link any personal data or location information with the random identifiers exchanged by devices. DOH does not want or need to know where or who you are for WA Notify to work. When you are close enough to another app user, your device will exchange random identifiers with that user.
<br>State law requires that lab results for all persons who test positive for COVID-19 are sent to Washington state DOH. This is not associated with the app. Public health organizations (DOH or local public health) follow up with those who test positive for COVID-19, based on information provided by testing labs. As a courtesy to all app users, public health organizations will verify positive tests and then provide app users with a verification code. If you choose to share a positive test with the app, you must use that code. This prevents people from falsely reporting. DOH wants app users to feel confident that possible COVID-19 exposures notifications received via the app are legitimate.
<br>If you have the current Apple or Google operating system installed on your device, you may have noticed that Exposure Notifications are now included. You cannot enable this function until you have installed the WA Notify app. Apple and Google will delete the exposure notification service tools from their respective operating systems once the pandemic reaches a point that public health no longer requires the use of this technology.
<br>Thank you for installing WA Notify! Together, we can protect our family, friends, neighbors, and colleagues, and keep Washington state moving forward!


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Washington Department of Health |
| **Website**  | - |
| **Email** | wanotify@uw.edu |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Washington+Department+of+Health](https://play.google.com/store/apps/developer?id=Washington+Department+of+Health) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | - |
| **Effective target Android version**  | - |
| **Minimum supported Android version**  | Lollipop, version 5.0 (API level 21) |
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
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the ISO country code equivalent of the current registered operator's MCC (Mobile Country Code)<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Code execution**
> - This application loads a native library: 'prioclient'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The WA Notify app has been installed by more than **100000** times. At this time, **359** rated the app and its average score is **4.017857**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 239

:star::star::star::star:: 32

:star::star::star:: 12

:star::star:: 12

:star:: 64

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.wa.doh.exposurenotifications 5 reviews"/>
</p>

> Really like this and think it was a good idea<br> :date: __2020-12-27 06:08:25__

> Fine<br> :date: __2020-12-24 12:40:30__

> Easy to get on.<br> :date: __2020-12-22 23:26:19__

> Easy to install<br> :date: __2020-12-21 09:46:57__

> Would be move convenient were it an implant. Maybe next year. Regardless, this app will make it easier to earn credits and to locate suitable breeding mates.<br> :date: __2020-12-19 07:40:24__

> Keep it up to date as this is going to be 6 to 9 more months long. Permissions are actually at an os level for both Android and ios, meaning you probably got an os update that you opped into in July or August. Go to settings, search for Contact, and exposure tracing will come up.<br> :date: __2020-12-18 08:20:33__

> Easy to use, private, I've had no problems<br> :date: __2020-12-17 01:08:14__

> Seems great so far.<br> :date: __2020-12-13 20:25:40__

> Just happy.<br> :date: __2020-12-12 21:28:27__

> Ok<br> :date: __2020-12-11 18:10:14__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.wa.doh.exposurenotifications 4 reviews"/>
</p>

> Pierce County public health finally reached me for my interview today (12/26), over 10 days after testing posirive, but that is not the app's fault.<br> :date: __2020-12-27 03:33:19__

> "When someone in WA state tests positive for COVID-19 and public health reaches out to them, they will be asked if they have WA Notify and given a verification code. With surging cases, this may take several days." => Seriously? It takes you several days to generate a verification code? And I'm paying taxes for this kind of unprofessionalism? Gov. Inslee, please fire the team that is unable to generate codes instantly for people to add to the app and hire someone better.<br> :date: __2020-12-26 19:05:39__

> Downloaded when there was only 1500 other downloads and am so happy to see this app over 100k downloads now! Helps make me believe in doing this.<br> :date: __2020-12-16 15:24:58__

> Nice concept, but poor execution on letting the public know it is available, and letting them know how the app works and what safeguards are in place to protect their privacy. To many people think the app will share personal information, so are unwilling to download it. This is making the app unusable as it was designed to be used. If only one person out of a hundred has downloaded it and is using it, then what use is having it on your phone?<br> :date: __2020-12-13 21:01:07__

> A lot like pokemon go only you don't want to catch any.<br> :date: __2020-12-09 05:47:52__

> Update: I restarted my phone and was able to install WA Notify afterwards. It seems pretty straight forward to use. Old Review: Couldn't get it to install. Acted like it was installing, but the app didn't. Android 8 on unlocked Sony phone.<br> :date: __2020-12-08 00:10:56__

> I like the idea but it's a little hard on my older battery. I have to idle it when I'm by myself, like in my car. Even if I forget to turn it back on it's still better than not running it at all. I hope more people use it, the more the better.<br> :date: __2020-12-07 19:22:15__

> Update: It took 4 tries to install it but it is finally working on my phone, if you are having issues I would uninstall and try again. This is not working on my Samsung A20 Android phone. It appears to download but just keeps coming back to the download page when I try to open it.<br> :date: __2020-12-03 03:36:07__

> I will be sharing this app to friends and family as I wish to do my part in "flattening the curve." I really hope more people gets this app. I noticed some people commenting that they can't turn on notifications. From what I understand is; if you tested positive, you MUST inform the facility where you tested, that you have this app so that they can generate a "code" that you can enter on the app. I hope everyone picks up on this. 🤞<br> :date: __2020-12-01 09:09:41__

> Thanks for the creation and release of this. Found it a little difficult to find a link to download it however. Hope it helps, It should.<br> :date: __2020-12-01 05:12:37__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.wa.doh.exposurenotifications 3 reviews"/>
</p>

> The concept is good. I need to be able to put in co-workers who have tested positive but dont use the app.<br> :date: __2020-12-24 15:47:26__

> I think this app will be more useful if more people use it. People are afraid you are tracking their movement's. Need more advertising! The conspiracy theory people will never use it. Sane people will. Thank You<br> :date: __2020-12-24 15:41:03__

> I echo Josh McAllister's comments. Recently tried to upload my test result which came to a dead end with the elusive "verification code".<br> :date: __2020-12-18 17:23:03__

> Havent had none<br> :date: __2020-12-15 18:36:19__

> I like the idea and the app itself seems fine but I don't like keeping my Bluetooth on, so I'm installing.<br> :date: __2020-12-12 18:54:49__

> Phone only connects to my car for hands free sometimes since installing<br> :date: __2020-12-07 06:29:34__

> This app would be better on a new phone. I have android vs. 9 and it says I have to have both location and bluetooth on for it to work. Newer versions don't require location, apparently. Leaving location on drains my battery and I don't really want it on unless I am actively using it for maps. Even if I turn location and bluetooth on and off depending on when I go out or not, it is not clear if I will receive notifications or not when at home (where I spend most of my time working).<br> :date: __2020-12-05 18:50:38__

> The app is SUPER easy to find and download! No problems at all. Have not had it long enough to give more deatail though.<br> :date: __2020-12-03 16:25:57__

> So far so good on this app, though it's a little worrysome that the app doesn't have any explicit permissions granted, nor does it ask for any, yet still seems to be able to access a wide swath of things on the device. This feels like a security concern for the device itself, as without permissions requests, it's impossible for users to determine when something changes in the application which widens its permission scope. That's a concern because it's one of the more common malware vectors.<br> :date: __2020-12-03 06:55:26__

> I have not received a verification code.I will update my star review when I am able to use this app.<br> :date: __2020-11-30 23:42:30__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.wa.doh.exposurenotifications 2 reviews"/>
</p>

> Isn't invasive I'm just not sure its actually doing anything<br> :date: __2020-12-27 20:34:56__

> Had to uninstall to fix bluetooth connection problems with Fitbit and car audio bluetooth<br> :date: __2020-12-23 07:59:57__

> App seems like it would be useful, but you need a verification code to give a positive result, and nobody knows how to get this code. My friend tested positive and I didn't receive any alert after being near her because she didn't get any info about a verification code, even when she asked about it. Being able to self report would make this much more useful.<br> :date: __2020-12-20 01:52:58__

> Wish I didn't have to have my bluetooth on for it work.<br> :date: __2020-12-18 06:24:46__

> it doesn't notify me at all. we had 2 positive at work but this never notified me. its not working.<br> :date: __2020-12-14 14:55:24__

> As big of a joke as our leaders! SMH<br> :date: __2020-12-07 11:01:49__

> The verification code is next to impossible to get. Whatcom County doesn't seem to know much about how to produce the code or don't seem to care. Perhaps the number from the test results should be a code number.<br> :date: __2020-12-06 18:17:01__

> Day 2 of trying to download this app through Goggle. Keep getting that app is pending & won't complete downloading. Waste of time & battery power<br> :date: __2020-12-05 08:19:56__

> Great idea, but the execution needs improvement. Bluetooth function must be on all the time to get accurate notification. My bluetooth drains my battery so that's not going to work. Why can't the app communicate within itself to identify if another user has been nearby and has received a positive test? Also, if a person has all the symptoms they should be able to self report. I appreciate the states making an effort but this needs to be on a national level for people who need to travel.<br> :date: __2020-12-03 19:47:55__

> Great idea but it depends on positive people to add app. People who are positive should not be out and about<br> :date: __2020-12-02 17:28:47__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.wa.doh.exposurenotifications 1 reviews"/>
</p>

> I received a call 8 hours after doing a Covid test and was told I was positive but no one knew about the verification code for this app. This app is pointless if not all hospitals to include the military know how to use it or know how to provide the access code. It needs to be more user friendly.<br> :date: __2020-12-28 05:30:03__

> Not accurate at all. I have never received notification of a possible exposure ever. I do Mobile Covid Testing.<br> :date: __2020-12-25 02:45:49__

> It will not allow notifications so it's worthless as is. This is also after updating.<br> :date: __2020-12-24 23:46:51__

> Constantly alerts if you ever have gps or bluetooth off so if it ever tries to give me a virus alert, I won't notice it.<br> :date: __2020-12-22 23:17:39__

> Didn't work for me. Would not accept my verification code.<br> :date: __2020-12-22 14:40:32__

> Caused phone issues with Bluetooth and wifi. Removed and issues are resolved.<br> :date: __2020-12-22 06:24:14__

> I couldn't warn others I got covid since I didn't have a verification code! Makes it somewhat useless<br> :date: __2020-12-20 00:17:33__

> No code. Can't make it work. Complete trash. Not surprised considering our Governor.<br> :date: __2020-12-19 23:31:19__

> Useless app, can not turn on. Just waste of time to try<br> :date: __2020-12-17 21:02:34__

> Spam. F Inslee and his tracking device<br> :date: __2020-12-17 17:04:59__


