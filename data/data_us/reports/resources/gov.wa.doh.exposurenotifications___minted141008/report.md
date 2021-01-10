# WA Notify
App version ``minted141008``

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
| **Latest version** | minted141008 |
| **Last update** | 2020-12-23 21:40:24 |
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
<br>When devices with WA Notify are in close contact, they exchange random codes. When someone tells their app they tested positive for COVID-19, other users who received their random codes receive an alert that they may have been exposed to COVID-19. Devices receiving random codes date-stamp them and record their signal strength so the app can estimate how close the devices were and for how long. Users within six feet for 15 minutes or more of the COVID-positive person are notified that they may have been exposed to COVID-19.
<br>Apple and Google's Exposure Notifications framework runs in the background, even when the WA Notify app is closed. It will not drain the device battery at a rate that would occur with other apps.
<br>How WA Notify Protects Your Privacy:
<br>Washington state DOH takes your privacy and confidentiality very seriously. The Apple and Google framework does not link any personal data or location information with the random codes exchanged by devices. DOH does not want or need to know where or who you are for WA Notify to work. When you are close enough to another app user, your device will exchange random codes with that user.
<br>State law requires that lab results for all persons who test positive for COVID-19 are sent to Washington state DOH. This is not associated with the app. Public health organizations (DOH or local public health) follow up with those who test positive for COVID-19, based on information provided by testing labs. As a courtesy to all app users, public health organizations will verify positive tests and then provide app users with a verification code. If you choose to share a positive test with the app, you must use that code. This prevents people from falsely reporting. DOH wants app users to feel confident that possible COVID-19 exposure notifications received via the app are legitimate.
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

The WA Notify app has been installed by more than **100000** times. At this time, **462** rated the app and its average score is **3.52**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 218

:star::star::star::star:: 55

:star::star::star:: 51

:star::star:: 27

:star:: 111

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.wa.doh.exposurenotifications 5 reviews"/>
</p>

> Very helpful<br> :date: __2021-01-05 12:31:36__

> I like the idea of having it tell me<br> :date: __2021-01-05 08:26:57__

> A bit intrusive for my likes but how else you going to know the truth of this deadly virus.<br> :date: __2021-01-04 22:21:20__

> Very useful in the current climate.<br> :date: __2021-01-04 07:52:12__

> I got the app because I just never know what could happen.<br> :date: __2021-01-04 07:24:12__

> It's been a few escrering moment but, better get the alert than the 🤒.<br> :date: __2021-01-03 03:15:43__

> Too soon to tell but could be very useful. They need to have a share that you can choose which app store to refer people Apple or Google. This one just sends a Google link which is useless for my wife and daughter. Hopefully they will add this. The real key is getting enough people to use it in this paranoid, conspiracy following world. Thanks for the quick response and good luck!<br> :date: __2021-01-02 05:30:16__

> This app doesn't track you! Google does that. The more downloads the better it will work. Get it!<br> :date: __2021-01-02 04:49:24__

> Really like this and think it was a good idea<br> :date: __2020-12-27 06:08:25__

> Fine<br> :date: __2020-12-24 12:40:30__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.wa.doh.exposurenotifications 4 reviews"/>
</p>

> Not sure at 77 & vulnerable go<br> :date: __2021-01-07 23:36:31__

> Pierce County public health finally reached me for my interview today (12/26), over 10 days after testing posirive, but that is not the app's fault.<br> :date: __2020-12-27 03:33:19__

> "When someone in WA state tests positive for COVID-19 and public health reaches out to them, they will be asked if they have WA Notify and given a verification code. With surging cases, this may take several days." => Seriously? It takes you several days to generate a verification code? And I'm paying taxes for this kind of unprofessionalism? Gov. Inslee, please fire the team that is unable to generate codes instantly for people to add to the app and hire someone better.<br> :date: __2020-12-26 19:05:39__

> Downloaded when there was only 1500 other downloads and am so happy to see this app over 100k downloads now! Helps make me believe in doing this.<br> :date: __2020-12-16 15:24:58__

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

> Not sure if it's even working<br> :date: __2021-01-08 19:59:09__

> Nobody knows how to get this code. When state officials reached out, they didn't even know what this app is and couldn't give me the code. UPDATE: the process is improving and I ended up getting the code. Changing from 1 to 4 stars. This app can save many lives.<br> :date: __2021-01-06 00:17:39__

> Just got this so too soon to rate, but I have a question. I am an urgent care provider testing patients for COVID so will definitely be in proximity to positive cases. I wish this app had a setting for when you are at work where exposures are protected and another for when you are away from work where exposures may be unprotected.<br> :date: __2020-12-30 03:18:41__

> Need to fix the battery drain on the app<br> :date: __2020-12-29 22:15:48__

> Literally never get a warning but numbers are going up all around me.... Not sure if this even works.... Just hoping it does while I'm battling being homeless and a support for a cancer patient partner.<br> :date: __2020-12-29 04:09:31__

> The concept is good. I need to be able to put in co-workers who have tested positive but dont use the app.<br> :date: __2020-12-24 15:47:26__

> I think this app will be more useful if more people use it. People are afraid you are tracking their movement's. Need more advertising! The conspiracy theory people will never use it. Sane people will. Thank You<br> :date: __2020-12-24 15:41:03__

> I echo Josh McAllister's comments. Recently tried to upload my test result which came to a dead end with the elusive "verification code".<br> :date: __2020-12-18 17:23:03__

> Havent had none<br> :date: __2020-12-15 18:36:19__

> I like the idea and the app itself seems fine but I don't like keeping my Bluetooth on, so I'm installing.<br> :date: __2020-12-12 18:54:49__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.wa.doh.exposurenotifications 2 reviews"/>
</p>

> Soy positivo y e querido compartir mis resultados pero no reconoce mi código<br> :date: __2021-01-07 23:59:26__

> The concept is fine but the fact that we are relying on someone who has the virus to input a code that no one seems to know about makes this app pretty useless. The last year has proven to us that we cannot rely on people to do the right thing so that makes this app double useless. This would have been far more useful if it kept the bluetooth device pinging but used every device's phone number and compared it against a database of known infected person's phone numbers.<br> :date: __2021-01-06 15:09:14__

> I was just wondering if you have to have bluetooth on all the time in order for the exchange of private codes or it it does it automatically?<br> :date: __2021-01-04 07:11:42__

> Nice concept, but poor execution on letting the public know it is available, and letting them know how the app works and what safeguards are in place to protect their privacy. To many people think the app will share personal information, so are unwilling to download it. This is making the app unusable as it was designed to be used. If only one person out of a hundred has downloaded it and is using it, then what use is having it on your phone?<br> :date: __2021-01-01 09:30:17__

> Isn't invasive I'm just not sure its actually doing anything<br> :date: __2020-12-27 20:34:56__

> Had to uninstall to fix bluetooth connection problems with Fitbit and car audio bluetooth<br> :date: __2020-12-23 07:59:57__

> App seems like it would be useful, but you need a verification code to give a positive result, and nobody knows how to get this code. My friend tested positive and I didn't receive any alert after being near her because she didn't get any info about a verification code, even when she asked about it. Being able to self report would make this much more useful.<br> :date: __2020-12-20 01:52:58__

> Wish I didn't have to have my bluetooth on for it work.<br> :date: __2020-12-18 06:24:46__

> it doesn't notify me at all. we had 2 positive at work but this never notified me. its not working.<br> :date: __2020-12-14 14:55:24__

> As big of a joke as our leaders! SMH<br> :date: __2020-12-07 11:01:49__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.wa.doh.exposurenotifications 1 reviews"/>
</p>

> I work at the post office and we had 3 positive results and I never received 1 alert from this app<br> :date: __2021-01-09 02:58:01__

> Constantly alerts if you ever have gps or bluetooth off so if it ever tries to give me a virus alert, I won't notice it. Update: I don't care about data or battery. I turn things off because I don't want internet dog food ads for driving past a pet store and I only go out once a week for groceries; no guests.<br> :date: __2021-01-07 15:44:25__

> I am a healthcare worker who has been exposed to numerous COVID positive patients but am told on a daily basis that I have had No Recent Exposures. Hmmm.<br> :date: __2021-01-06 18:04:42__

> I came into contact with 2 people for a few hrs that tested positive 2 days later. They both have this app.. They were both called by the health dept and neither of them were asked about the App or given a code. None of us were aware that you had to be given a code?<br> :date: __2021-01-06 08:14:32__

> No code. Can't make it work. UPDATE: According to developer reply, I should have gotten a code from health Dept... I did not. I did an online interview a month after having covid-19, but no code.<br> :date: __2021-01-04 21:10:20__

> JUST TO GIVE ME MY PRIZES ALREADY. I WANT TO BE RELEASED FROM THIS STATE OF HELL<br> :date: __2021-01-04 01:36:08__

> Wow, they really thought this would work??? 🙄<br> :date: __2021-01-01 00:46:38__

> doesn't allow me? to turn on ，keep asking try again. NOT be able to use it. useless.<br> :date: __2020-12-31 05:58:54__

> I've had it since release and haven't gotten any notifications. At this point I'm wondering if this is even working! Seems unlikely that I've not been in a place where someone tested positive in all of this time. Useless app!<br> :date: __2020-12-29 03:56:41__

> I received a call 8 hours after doing a Covid test and was told I was positive but no one knew about the verification code for this app. This app is pointless if not all hospitals to include the military know how to use it or know how to provide the access code. It needs to be more user friendly.<br> :date: __2020-12-28 05:30:03__


