# Protect Scotland
App version ``1.1.1``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="Protect Scotland icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Protect Scotland |
| **Unique identifier** | gov.scot.covidtracker |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=gov.scot.covidtracker](https://play.google.com/store/apps/details?id=gov.scot.covidtracker) |
| **Summary**  | Help stop the spread of Covid-19 in Scotland by using the Protect Scotland app. |
| **Privacy policy** | [https://protect.scot/privacy-policy-app](https://protect.scot/privacy-policy-app) |
| **Latest version** | 1.1.1 |
| **Last update** | 2021-01-05 18:46:50 |
| **Recent changes** | Minor fixes and text changes |
| **Installs**  | 500,000+ |
| **Category** | Medical |
| **First release** | Sep 4, 2020 |
| **Size**  | 107M |
| **Supported Android version**  | 6.0 and up |

### Description
> Help Scotland keep the spread of coronavirus under control by downloading and using the free Protect Scotland app from NHS Scotland’s Test and Protect service. 
<br>Using the app is entirely voluntary.  When you use the app, you will be alerted if you have been in close contact with another app user who has tested positive for coronavirus. If you test positive and you enter the unique code sent to you into the app, it will anonymously warn other app users whom you have been in close contact with.
<br>Using Bluetooth, the app will search for other devices with the Protect Scotland app installed, which are within 2m of your phone. You don’t need to have a WiFi connection. The app uses a very small amount of your mobile phone data.  
<br> Once you’ve downloaded the app, encourage your friends, family and colleagues to do so too. The more people who download and use the Protect Scotland app, the more likely we are to keep coronavirus under control. . The benefits of using the app are:  Speeds up the process of identifying and notifying people that have been at risk of catching coronavirus, particularly of unknown contacts Slows the spread of the virus Reduces the likelihood of further lockdowns Helps protect the health service, your family and friends, yourself and the people of Scotland
<br>Ultimately, you can help to stop the spread of coronavirus in Scotland by downloading and using the Protect Scotland app.
<br>Privacy and Data
<br>The Protect Scotland app is designed to protect the privacy of all users. It doesn’t store or share any personally identifiable information, like your name or address. Nobody can track your location by using the app or tell who you are.
<br>You can remove the app from your device at any time, and all the data stored on your phone will be deleted.


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
| **Developer**  | NHS Education for Scotland |
| **Website**  | [https://protect.scot/index.html](https://protect.scot/index.html) |
| **Email** | testandprotect@nhs.scot |
| **Physical address**  | [NHS Education for Scotland Knowledge Services 2 Central Quay 3rd Floor 89 Hydepark Street Glasgow G3 8BW ](https://www.google.com/maps/search/NHS%20Education%20for%20Scotland%20Knowledge%20Services%202%20Central%20Quay%203rd%20Floor%2089%20Hydepark%20Street%20Glasgow%20G3%208BW%20) (Google Maps) |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=NHS+Education+for+Scotland](https://play.google.com/store/apps/developer?id=NHS+Education+for+Scotland) |

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
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>ACCESS_WIFI_STATE** | Normal | Allows applications to access information about Wi-Fi networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>VIBRATE** | Normal | Allows access to the vibrator. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | android.com | Google LLC | :us: US | 1997-06-23 04:00:00 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | expo.io | See PrivacyGuardian.org | :us: US | 2011-05-01 21:26:50 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the MCC+MNC of the provider of the SIM<br>
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address ' returned no addresses for  ; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Pim data leakage**
> - This application accesses data stored in the clipboard<br>

**Code execution**
> - This application loads a native library<br>
> - This application executes a UNIX command<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The Protect Scotland app has been installed by more than **500000** times. At this time, **2453** rated the app and its average score is **3.808765**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 1506

:star::star::star::star:: 146

:star::star::star:: 176

:star::star:: 78

:star:: 547

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 5 reviews"/>
</p>

> 👍🏻 keep safe everyone<br> :date: __2021-01-09 15:14:11__

> Great<br> :date: __2021-01-09 01:06:12__

> So good. Everybody should have one<br> :date: __2021-01-08 20:37:56__

> Excellent<br> :date: __2021-01-08 11:32:33__

> Please, download, we need the R number and lives to be saved, let's do this together, we've got it Scotland! 🙏🙏🏴󠁧󠁢󠁳󠁣󠁴󠁿🏴󠁧󠁢󠁳󠁣󠁴󠁿<br> :date: __2021-01-08 01:12:12__

> Ray of light<br> :date: __2021-01-08 00:24:09__

> Amazing<br> :date: __2021-01-07 23:48:39__

> Absolutely essential.<br> :date: __2021-01-07 19:31:37__

> Yes I think this is a great app.and to help the N HS 🇫🇮💙👌<br> :date: __2021-01-07 18:48:03__

> All good!<br> :date: __2021-01-07 15:43:44__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 4 reviews"/>
</p>

> OK<br> :date: __2021-01-07 10:58:35__

> It saves lives<br> :date: __2021-01-02 00:22:28__

> Have not needed to use<br> :date: __2020-12-23 00:24:50__

> Easy to use no problems except for the battery so had to use a back up facility<br> :date: __2020-12-16 22:14:09__

> Okay I think.I may just have been so Isolated I have not had a concern ..yet .<br> :date: __2020-12-14 23:01:39__

> I haven't had to use it so far<br> :date: __2020-11-26 23:25:03__

> Just downloaded the app, some folk saying you dont need to turn on location but the app says I have to keep both location and bluetooth on. Glad we have a safe app here in Scotland! 🏴󠁧󠁢󠁳󠁣󠁴󠁿<br> :date: __2020-11-18 14:51:54__

> I have not, thankfully been exposed to anyone who have tested positive for covid, but I have friends who use this app who have. From listening to them and hearing their experience proves that the Scottish app works<br> :date: __2020-11-15 03:26:08__

> Very easily understood and concise information explained simple and clearly. I would urge anyone I know to use this app to track and trace to protect the most vulnerable in not just our community, but our own families and friends!!<br> :date: __2020-10-25 13:23:33__

> YES I KNOW ITS MENT TO PROTECT SCOTLAND FROM COVID BUT im 12 in secondary school and This app was recommended by google play its self it said Pegi 3 so i downloaded it yesterday i forgot about then went back into it today and it came with two options im over 16 or under i said under as I am it said you are not entitled to use this app so undownload it so i did the point to this is *what is the point of making this a pegi 3 and only 16 are entitled to use this app* Thank you goodbye.............<br> :date: __2020-10-22 22:52:46__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 3 reviews"/>
</p>

> Update: appear to be getting daily exposure updates now. Will give the app another try. I have had zero response from the developer.<br> :date: __2021-01-09 00:16:58__

> The app used to work fine until the 10 Dec update but then stopped checking for exposures automatically. It was difficult to report the issue --- it feels like mails / app reviews only got attention after people made fuss on social media. The app works OK now, after the 5 Jan update, but I wish there was an easier way to report bugs, and more transparency regarding existing ones.<br> :date: __2021-01-08 13:18:19__

> Just got a notification after accidently turning off my.location to be informed I haven't been checked since 14th December !!!<br> :date: __2021-01-07 23:23:07__

> Was working for a while but not performed a check since 16th December 2020 despite always being on.<br> :date: __2021-01-03 22:07:19__

> I occasionally check this app and all is well. Thank God.<br> :date: __2020-12-30 23:14:17__

> No exposure checks in the last 14 days, yet I've had bluetooth & location switched on.<br> :date: __2020-12-30 14:39:08__

> Not enough information<br> :date: __2020-12-29 03:11:50__

> Periodically tells me that Bluetooth is turned off, even when (as far as I can see) it's not...<br> :date: __2020-12-28 19:22:14__

> Won't install. When I click next after accepting T&C it says I'm not connected to the Internet. Could it be because I have the covid tracker program installed? Turns out if you have a VPN installed it will not work.<br> :date: __2020-12-20 12:00:57__

> Good idea but drains battery extremely fast. Cant be in public spaces anymore than an hour with it on or my phone dies<br> :date: __2020-12-18 04:02:10__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 2 reviews"/>
</p>

> Is this app working.<br> :date: __2021-01-08 23:48:11__

> Does it do anything . No buttons seem active<br> :date: __2020-12-23 12:48:16__

> Its a good idea but while it was installed, it messed up my Bluetooth connections. Couldnt use any Bluetooth devices while it was installed<br> :date: __2020-12-22 04:04:22__

> Following the latest update It appears my phone had turned off the exposure notifications switch in settings / Google/ covid-19 exposure notifications. What is worrying was / is the Protect Scotland app did not notify me in any way, until I happened to open the app by chance and only then did a warning appear. Why doesn't the app generate a warning every time it tries to check or update it's database ? It seems a very basic failing. ☹️😳 Also why no exposure checks reported anymore ?<br> :date: __2020-12-19 02:35:30__

> Absolutely destroyed my battery life polling live connections for proximity checking. Also didn't warn of a close contact.<br> :date: __2020-12-14 12:29:30__

> How do I know this app is working?<br> :date: __2020-11-24 19:52:43__

> Great idea. Had to uninstall though as it started draining memory and wouldn't push notifications as a result. Might not be apps fault, could be mine or my phone's ability. Either way, can no longer use.<br> :date: __2020-11-20 07:16:33__

> Doesn't work, went on the app and then got a notification that ive been in close contact with an infexted person. This was 13 days after i was in contact with the person. Never got a text phone or email either. Just aswell i dont have any symptoms<br> :date: __2020-11-17 22:25:32__

> I have an android phone. This app gives me no notifications. Other users with iPhones tell me they get notifications saying they have no contacts and how many people they have been matched against etc. Why would that be?<br> :date: __2020-11-15 21:56:30__

> I WASNT NOTIFIED OF MY EXPOSURE TO SOMEONE WHO TESTED POSITIVE WITH COVID-19 TILL 6 DAYS LATER. NOT MUCH GOOD IF I HAD OF UNKNOWINGLY BEEN POSITIVE AND ASYMPTOMATIC. CLEARLY THE APP NEEDS TO BE IMPROVED AS WELL AS USED - DOWNLOADED BY MILLIONS MORE PEOPLE IF IT IS TO BE EFFECTIVE OR WORTHWHILE.<br> :date: __2020-11-12 23:38:12__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 1 reviews"/>
</p>

> It hasn't checked for any exposure in weeks another failed job by nicola sturgeon and the snp<br> :date: __2021-01-08 20:09:29__

> This app has serious glinch in notifying you if you have been in contract with anyone thats has tested positive for covid. I received an alert last night notifying me to self isolate for 1 day after someone tested positive nearly 10 day prior. Luckily I was aware of this persons positive test and have following the guidelines keeping myself& others safe. I feel this app needs to be relooked at as a whole as it is giving people a false sense of security<br> :date: __2021-01-08 10:11:31__

> I never installed the app after reading the reviews saying it hadn't worked? I don't see the point in using this as it could get you killed.<br> :date: __2021-01-07 23:26:57__

> App doesn't seem to be doing exposure checks any more??<br> :date: __2021-01-07 21:36:03__

> Absolutely useless, my wife and myself all had Covid. Despite entering details on the app on both our phones we received zero notifications. Other close relatives also received zero notifications despite close contact. Not fit for purpose.<br> :date: __2021-01-07 19:44:31__

> I have been in close contact with someone who tested positive and uploaded their details. They were in an identical position. Neither of us received any notification. I have been working all through this pandemic, use public transport every day, no notifications. I suspect this app is a gimmick to make us feel better. It's pointless and should be deleted. Wash your hands, keep your distance, wear your mask, isolate if symptoms appear. This app is rubbish.<br> :date: __2021-01-07 14:52:30__

> CONTROLAVIRUS. . Switch off your TV..bin the mask.. Hug each other.. Educate yourselves. Seriously people wake up.. Your old and young are suffering because of your stupidity ...Dont be a sheep..<br> :date: __2021-01-07 07:50:04__

> Stopped checking in the background, So what is the point in the install now?<br> :date: __2021-01-07 02:32:07__

> Has only done 1 exposure check in 14 days which was the check I kicked off after the last time I checked and it also hadn't performed any checks in weeks. App is broken, needs fixed<br> :date: __2021-01-06 23:07:14__

> App no longer works, no exposure checks. Reinstalling didn't fix.<br> :date: __2021-01-06 21:50:33__


