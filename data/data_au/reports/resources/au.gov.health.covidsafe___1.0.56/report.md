# COVIDSafe
App version ``1.0.56``

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
| **Latest version** | 1.0.56 |
| **Last update** | 2020-08-14 04:35:53 |
| **Recent changes** | Improved notifications.<br>The app now includes Turkish and Punjabi translations. |
| **Installs**  | 1,000,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 25, 2020 |
| **Size**  | 12M |
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
| **Website**  | [https://www.health.gov.au/resources/apps-and-tools/covidsafe-app](https://www.health.gov.au/resources/apps-and-tools/covidsafe-app) |
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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **12939** rated the app and its average score is **2.7324052**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 3932

:star::star::star::star:: 870

:star::star::star:: 1280

:star::star:: 1511

:star:: 5343

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> Easy to instal Hope it works<br> :date: __2020-09-09 00:31:12__

> No notification so far. I need to uninstall to get function and readings from iHealth heart monitor a few times a week. Then reinstall COVIDSafe app. Any solutions less onerous? Nola<br> :date: __2020-09-08 09:49:21__

> I feel safe and protected<br> :date: __2020-09-07 02:08:59__

> Good.<br> :date: __2020-09-06 15:13:58__

> Good<br> :date: __2020-09-06 13:30:36__

> geez 9 zzz 222ss xxx 2w22<br> :date: __2020-09-06 02:43:13__

> Just follow the safe RULES<br> :date: __2020-09-03 16:40:51__

> It seems they have fixed the interruptions to Bluetooth and I am happy to use it again. Terrible interruptions to any Bluetooth stream. I can not listen to music without this app stopping the stream for 10 seconds or more. Tried to stop app while using my phone for music but it comes back on. I would have to uninstall and reinstall when interacting with people to tolerate it. Not worth it while SA is covid-19 free. I have uninstalled it until I hear that the Bluetooth is fixed.<br> :date: __2020-08-30 22:58:26__

> Network pro. Read source. Its safe.<br> :date: __2020-08-30 10:45:00__

> Helps<br> :date: __2020-08-28 23:46:16__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> Had no troubles, works ok from day1 of release. Now i find out the phone app had battery optimization enabled which prevents app from running correctly. Uninstalled + reloaded as i thought app was the issue. Then used PC and Google to locate how to ensure no optimization on the app. I only turn bluetooth on when i leave home. So no battery issues.<br> :date: __2020-09-06 14:33:07__

> I hope its just me. Sometimes randomly I have to briefly turn bluetooth off, to get mt wifi to work again. Then I forget to reactivate bluetooth. Android phone. There is nowhere on the covidsafe website to put technical feedback. No feedback is not really good for quality control. How will you know if its working, until you need it and then its too late.<br> :date: __2020-09-04 01:30:28__

> To all you one star raters, when all else fails, RTFM. For the benefit of the uneducated, that means Read the instructions!! At 18:03 on 26/4/20 activation worked perfectly. To the nay-sayers, stop trying to show the world how stupid, selfish and self-centred some Australians can be.<br> :date: __2020-09-01 13:41:00__

> Great initiative.<br> :date: __2020-08-27 06:29:57__

> Updated today but unsure if notifications sound comes on because I've just turned it on or because I have been exposed to the SARS COV 2! Also, I was not notified of recent update!<br> :date: __2020-08-21 05:08:51__

> Hope it works.<br> :date: __2020-08-21 04:36:40__

> Free anti virus software, I guess. BUT you may need to visit the play store to update it directly, as it seems resistant to auto updates.<br> :date: __2020-08-19 09:57:59__

> When it works that is.. 😁<br> :date: __2020-08-17 04:46:39__

> A useful app that causes slightly more battery usage but anything that helps to contact trace people potentially affected by the Chinese Communist Party Virus (CCP Virus), is worth having as an additional tool to help fight this Chinese biological weapon. If any good that came from this CCP Virus is that it revealed China's true colours & is helping the rest of the world in unititing in worldwide retribution against the CCP. Hopefully this brings a demise to this brutal and authoritarian regime.<br> :date: __2020-08-10 07:06:18__

> Had to delete cache & data & reregister after update, otherwise it crashes constantly<br> :date: __2020-08-10 06:54:42__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> Okay dont mind it<br> :date: __2020-08-29 12:30:32__

> This app needs location *permission* because Bluetooth can be used to locate us. It doesn't need our location though. It should not require location services to be enabled.<br> :date: __2020-08-28 17:00:11__

> This app needs to work with battery optimisation on, I get better battery life with battery optimisation on, I don't want to charge my phone every 12 hours which seems to be with this app active in background. Please fix<br> :date: __2020-08-28 07:14:20__

> When it works properly!<br> :date: __2020-08-28 04:59:06__

> Update on the 23/08 (Version number 1.0.56) is warning me "No internet connection" when my phone is connected to the internet. Tapping the warning takes me to a message on why it needs the internet with a back arrow.<br> :date: __2020-08-23 04:21:40__

> I get why people would be unhappy about the app draining phone batteries. The idea is great... but its bypassing a lot of precautions and restrictions to stay awake and pull bluetooth information (polling), and agressive pinned notifications tend to be the most annoying type. Phone OS updates should help reduce wakelocks Other than that, it doesn't do much beyond tracking bluetooth IDs, like WiFi names, your phone/SIM network has your geo location, google/apple do too. Theyre beyond invasive.<br> :date: __2020-08-22 06:16:41__

> Can i download the covidsafe app on a tablet<br> :date: __2020-08-15 08:03:45__

> Working from home in Sydney and go out less than once a week. I can't see any way to turn it off when not needed. Can't get IFTTT to turn off when in WiFi zone.<br> :date: __2020-08-14 23:05:52__

> It keeps dropping of.<br> :date: __2020-08-14 11:56:57__

> Has been working on Android 6.0.1 until the last few days, when it now requires Battery optimisation to be disabled. I have tried all help instruction and any other possible way to switch off battery optimisation but the COVIDSafe app (v 1.0.48) still will not work. Hope they fix the problem soon.<br> :date: __2020-08-14 07:01:21__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> The app is causing my Bluetooth headphones to stutter :(<br> :date: __2020-09-09 13:20:22__

> No support. Bluetooth weirdness = lost connectivity. Oh well. Nice idea. Uninstalled.<br> :date: __2020-09-08 14:16:41__

> I thought the app was working fine on my phone samsung s5. I did not have the battery issues others were reporting. But now it is behaving strangely. If i have the GPS turned on for another App and the turn it off. I now get a message saying the Covid Safe App is not working and needs location services. However the little icon at the top of the screen and the pull down menu both say it is active. I will not leave my GPS turned on. Covid Safe only has location services for bluetooth. Why GPS?<br> :date: __2020-09-08 01:57:59__

> Uninstall because it cause problems with bluetooth conectons.<br> :date: __2020-09-06 09:28:07__

> 5/9/20 update: for a few weeks been thinking my Bluetooth speakers were broken . Then I realised its the covid safe app using the Bluetooth interfering with the signal. Uninstalled the covid safe app and speakers working fine again. I pay $12 a month for spotify and not going to have the covid safe app ruin my music streaming. Would be good if I could turn the covid safe app off when at home and still have Bluetooth on for my speakers. Let me know if I can as I have uninstalled the app.<br> :date: __2020-09-05 10:33:15__

> Don't know. I don't use it.<br> :date: __2020-09-05 01:15:21__

> Glitchy<br> :date: __2020-09-04 10:12:54__

> Great idea, terrible implementation. Interferes with Bluetooth streaming, which is frustrating on the train ride home. Needs to be fixed if you want this to be a genuine tool to help contact tracers.<br> :date: __2020-09-03 09:46:50__

> I really don't know what's use of this apps except eating so much battery juice on my phone.<br> :date: __2020-09-03 03:36:21__

> Not Sure.<br> :date: __2020-09-01 13:01:21__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> App was not working at all on the Android 11 Beta. Stable final release of 11 is now out and COVIDSafe is still not working.<br> :date: __2020-09-09 01:40:33__

> it brokeded<br> :date: __2020-09-08 14:46:38__

> I have to force stop the app to use Bluetooth devices. I use them as a vision impaired person for navigation. The solution offered by these pelicans was to not use the app. Apparently my tax dollars aren't worth as much as fully sighted people. I think there are laws that protect me from discrimination like that developers. Shall I test that or will you fix the app?<br> :date: __2020-09-08 11:26:41__

> It worked for a few months, but for the last few weeks it has been crashing every time I've tried to run it, and crashing when it launches in startup.<br> :date: __2020-09-08 11:14:06__

> Every other week it just becomes inactive and has to be reloaded and all contact tracing is lost.<br> :date: __2020-09-08 08:00:30__

> ive deleted it for two reasons. it doesnt seem to work. but mainly in protest of the federal gov continued snipping of the vic responce to covid. all u r doing is undermining vic and fanning discontent.<br> :date: __2020-09-08 04:15:02__

> Always says it's inactive<br> :date: __2020-09-08 00:12:12__

> Such a waste of people's money<br> :date: __2020-09-08 00:05:47__

> Apart from using your phones battery, I don't know what else this app is good for? It hasn't proven to be helpful in tracking any contacts that human contact tracers haven't found.<br> :date: __2020-09-07 14:49:14__

> What's the point!<br> :date: __2020-09-07 14:22:01__


