# COVIDSafe
App version ``1.0.33``

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
| **Latest version** | 1.0.33 |
| **Last update** | 2020-07-04 23:25:57 |
| **Recent changes** | The app now supports 5 more languages: Mandarin, Cantonese, Vietnamese, Arabic and Korean<br>Accessibility enhancements<br>Bug fixes. |
| **Installs**  | 1,000,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 25, 2020 |
| **Size**  | 11M |
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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **11936** rated the app and its average score is **3.1705883**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 5005

:star::star::star::star:: 922

:star::star::star:: 992

:star::star:: 1133

:star:: 3881

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> Persistent notification is annoying but I understand the priority is keeping it running to keep the Bluetooth pinging. Reverse-engineering has shown the security of the app to be good but I hope the source is released soon.<br> :date: __2020-07-05 14:06:31__

> Installed. registered. Not had an issue since.<br> :date: __2020-07-05 11:51:07__

> Worthy aim and a way we can all help. 1.0.28 stays alive long enough to be useful. Still stops working after several hours and rebooting is needed to get going again. Version 6.0.1 of Android. Err message flashes with description "Unfortunately, Bluetooth Share has stopped". In this state I couldn't even answer a call before 1.0.28. Just usable with my Motorola Moto G 3rd generation.<br> :date: __2020-07-05 09:47:20__

> The persistent notification doesn't appear on the lock screen anymore<br> :date: __2020-07-05 07:54:30__

> It gives me all the details I need to know about COVID 19<br> :date: __2020-07-05 05:47:53__

> It keeps closing...not very useful when I get home and realise it hasn't been tracking. I make sure I reopen the app every morning but it closes within a couple hours. I have selected the not allowed option within battery optimisation, so it's not due to that. Update: newer updates have fixed this issue<br> :date: __2020-07-05 00:48:34__

> Installed from it's release. Worked. No problems at all. It doesn't drain the battery. It doesn't crash. It's totally fine. I haven't been dragged into the back of a van, taken to an underground bunker and questioned by spies.<br> :date: __2020-07-03 10:31:09__

> Very Good<br> :date: __2020-07-02 11:56:22__

> Just wear a mask, it's not that hard.<br> :date: __2020-07-02 02:47:55__

> The latest version of this app on my Motorola G7 is all good - battery life, connectivity to Bluetooth, and operation of other apps (issues reported by other users) all normal. The previous version meant I had to manually connect to other Bluetooth devices, but I wasn't experiencing any dropouts so it was worth the minor inconvenience. Would recommend people at least try it on their mobile for the possible future benefit of yourself and others.<br> :date: __2020-07-01 01:33:50__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> Sits quietly in the background can't complain<br> :date: __2020-07-05 13:21:45__

> Using this app makes audio headset bluetooth connection unstable, but still worth using it<br> :date: __2020-07-02 02:43:49__

> It's this one of those, pay-to-win games? I haven't leveled up once yet !?!<br> :date: __2020-07-01 23:23:24__

> My screen locks and goes blank any time I revive or make call. Have to uninstalled, friend has same issue. Tried re installing, issue is back.<br> :date: __2020-07-01 00:11:47__

> On my Note 10, I don't have any of the problems others mention about bluetooth drop outs to car or Senheisser headphones or Samsung Watch, the only problem I have is the app doesn't start up when I restart the phone, I rarely restart so not a big problem.<br> :date: __2020-06-28 04:21:25__

> The app conflicts with my Bluetooth headphones, here's the fix: Settings > apps > force stop. Remember to turn the app back on when you go outside. Good luck everyone.<br> :date: __2020-06-27 08:52:54__

> I don't mind the app but I don't understand wire displays how many minutes and the time when I pull down my home screen and it's running in the background what do the minutes mean? Eg: covidsafe 12m ??<br> :date: __2020-06-24 17:17:19__

> Excellent<br> :date: __2020-06-24 08:54:38__

> I installed this app, hoping people do the right thing. If they have the virus they too should install and updated information for the public to know about it. Noone knows who the infected person/s are, but you are made aware that someone near you is.<br> :date: __2020-06-23 14:53:07__

> Always on keeping myself and others safe<br> :date: __2020-06-23 09:13:15__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> Not had experience yet<br> :date: __2020-07-05 02:51:10__

> Not sure why the app needs access to bluetooth, also doesn't seem like an intuitive app<br> :date: __2020-07-02 07:16:01__

> Still being asked to fill details in on contact tracing forms 🙄 could be better!<br> :date: __2020-07-02 01:00:09__

> I want to like this. But it's messing with Bluetooth audio. So do I accept the drop outs or uninstall?<br> :date: __2020-06-30 11:56:40__

> It is unobtrusive and altruistic<br> :date: __2020-06-30 04:51:52__

> Constantly requires restarting. Haven't had to supply data at all but if I did I don't know how much would have been captured cause it seems to always shut itself down<br> :date: __2020-06-29 03:39:07__

> didn't detect anything<br> :date: __2020-06-29 02:08:33__

> Useless<br> :date: __2020-06-28 01:05:52__

> Might be useful, but can't be sure. I've installed this app and so far haven't got Covid 19 (that I know of). Registration was easy, and can be done using a pseudonym. Battery usage is quite low. Ongoing notification to tell you that it is working, and will let you know if it stops working (eg. you turn off Bluetooth). However, the icon (Australia with tick) shows whether it is working or not (eg. When Bluetooth turned off).<br> :date: __2020-06-27 14:26:06__

> Doesn't work properly<br> :date: __2020-06-26 18:15:48__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> Effected blutooth dramatically. Uninstalling.<br> :date: __2020-07-05 11:07:18__

> App causes music to be interrupted every few seconds on blue tooth heaphones. And extra battery drain. Makes my brand new bluetooth headphones useless. Cant listen from my phone at all.<br> :date: __2020-07-05 07:05:46__

> It complains that it's not running because I turned off push notifications. I hate being bothered by apps. Why can't it run without bothering me?<br> :date: __2020-07-05 06:49:23__

> Until the recent update this app was okay a few gripes mentioned below. Unfortunately It now eats my battery and caused my Bluetooth headphones to be completely out of sync with video! I am going to uninstall it until we get the second wave in Tassie! I also really don't like the permanent icon and status in my notifications bar. Please make this app so that it only notifies me if there is a problem!!!!!!!!<br> :date: __2020-07-04 13:49:12__

> App should be named COVIDTrace as this is its purpose. Doesn't do anything to keep me safe.<br> :date: __2020-07-04 08:25:09__

> Keeps saying my phone is an invalid mobile nb. Can't even register.<br> :date: __2020-07-03 16:08:03__

> Battery drains a lot faster and my phone has been freezing since installing this app.<br> :date: __2020-07-03 01:09:54__

> Good idea, if it would work. Every time I go into the app to check if it's still working it isn't and I have to re-allow battery optimisation, I'm not sure why this gets turned off because I've re-allowed it at least 10 times by now.<br> :date: __2020-07-02 23:56:06__

> Since installing this app Bluetooth music playing in my car keeps momentarily pausing a number of times per minute. Force Stopping the app lets the music play normally so it's definitely the app.<br> :date: __2020-07-02 12:17:37__

> Great idea. But it interferes with my earphones and car system. So I use it only when I don't use bluetooth for anything else and when I remember to a enable bluetooth in covid safe app.<br> :date: __2020-07-02 11:48:25__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> The fact that it doesnt seem to work while the phone is locked (samsung s5) makes it pretty much useless.<br> :date: __2020-07-05 13:01:40__

> No virus it's a scam<br> :date: __2020-07-05 11:04:31__

> Congrats, the latest update completely glitches the displaying of all lockscreen notifications, rendering them unreadable. Thankfully I can simply disable the CovidSafe notification from appearing altogether, though this obviously defeats its purpose. Galaxy S9, Android 10.<br> :date: __2020-07-05 08:14:06__

> Never trust an APP made in China.<br> :date: __2020-07-05 07:40:25__

> Useless. Doesn't do anything to help against covid 19<br> :date: __2020-07-05 06:50:21__

> I'm not sure what happened, but after the last two updates, the app keeps force closing, so it doesn't run at all. A system error message pops up as well saying that the app stopped working. Please fix.<br> :date: __2020-07-05 05:37:10__

> Latest update to have the app in 100 languages has broken my notifications panel on my Samsung S10 5G. Have switched off foreground service until fixed.<br> :date: __2020-07-05 05:21:11__

> The status bar has gone blank with the latest update, using Android Samsung Galaxy S7 Edge<br> :date: __2020-07-05 02:27:05__

> Stop download what ever they saying 😠 and stop to be a 🐑<br> :date: __2020-07-05 02:09:57__

> Cuts spotify off regularly with bluetooth headphones and car.<br> :date: __2020-07-05 01:35:32__


