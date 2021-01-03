# Protect Scotland
App version ``1.1.0``

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
| **Latest version** | 1.1.0 |
| **Last update** | 2020-12-10 19:46:00 |
| **Recent changes** | Accessibility improvements: Amended content and age verification for secondary school age users<br>Guidance updates: updated content to reflect changes to self-isolation rules |
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

The Protect Scotland app has been installed by more than **500000** times. At this time, **2247** rated the app and its average score is **4.0528636**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 1496

:star::star::star::star:: 168

:star::star::star:: 158

:star::star:: 59

:star:: 366

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 5 reviews"/>
</p>

> Brilliant app so easy to use<br> :date: __2021-01-02 13:08:27__

> Very pleased with the app thank you<br> :date: __2021-01-01 11:23:29__

> A app that doesn't harvest your information.<br> :date: __2021-01-01 01:39:35__

> Easy install, anonymous and unobtrusive. No personal details required. Get alerted if you have been in close contact with anyone recently testing positive. What you choose to do then is up to you. Similarly if you have a positive test, you choose to allow the app/system. A win-win for everyone, and it will help restrict and limit any spread. Update: 31st Jan 20: The app/system works. My partner got a +ve test result this morning. She entered her code and I was notified a few hours later.<br> :date: __2020-12-31 14:53:28__

> Every one should have this.<br> :date: __2020-12-31 10:03:37__

> Walk and keep positive. X<br> :date: __2020-12-30 19:41:21__

> Explosheed to covid<br> :date: __2020-12-30 19:33:21__

> Very good service<br> :date: __2020-12-29 09:39:36__

> On my phone 24×7 - and on yours too, right? Never causes any perceivable problems.<br> :date: __2020-12-28 19:38:12__

> All good works as described<br> :date: __2020-12-27 18:07:54__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 4 reviews"/>
</p>

> It saves lives<br> :date: __2021-01-02 00:22:28__

> Have not needed to use<br> :date: __2020-12-23 00:24:50__

> Easy to use no problems except for the battery so had to use a back up facility<br> :date: __2020-12-16 22:14:09__

> Okay I think.I may just have been so Isolated I have not had a concern ..yet .<br> :date: __2020-12-14 23:01:39__

> I haven't had to use it so far<br> :date: __2020-11-26 23:25:03__

> Just downloaded the app, some folk saying you dont need to turn on location but the app says I have to keep both location and bluetooth on. Glad we have a safe app here in Scotland! 🏴󠁧󠁢󠁳󠁣󠁴󠁿<br> :date: __2020-11-18 14:51:54__

> I have not, thankfully been exposed to anyone who have tested positive for covid, but I have friends who use this app who have. From listening to them and hearing their experience proves that the Scottish app works<br> :date: __2020-11-15 03:26:08__

> Very easily understood and concise information explained simple and clearly. I would urge anyone I know to use this app to track and trace to protect the most vulnerable in not just our community, but our own families and friends!!<br> :date: __2020-10-25 13:23:33__

> YES I KNOW ITS MENT TO PROTECT SCOTLAND FROM COVID BUT im 12 in secondary school and This app was recommended by google play its self it said Pegi 3 so i downloaded it yesterday i forgot about then went back into it today and it came with two options im over 16 or under i said under as I am it said you are not entitled to use this app so undownload it so i did the point to this is *what is the point of making this a pegi 3 and only 16 are entitled to use this app* Thank you goodbye.............<br> :date: __2020-10-22 22:52:46__

> The app is great the alerts go off all the time outside the parligment building Edinburgh so who's not telling they have it<br> :date: __2020-10-19 18:17:39__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 3 reviews"/>
</p>

> I occasionally check this app and all is well. Thank God.<br> :date: __2020-12-30 23:14:17__

> No exposure checks in the last 14 days, yet I've had bluetooth & location switched on.<br> :date: __2020-12-30 14:39:08__

> Not enough information<br> :date: __2020-12-29 03:11:50__

> Periodically tells me that Bluetooth is turned off, even when (as far as I can see) it's not...<br> :date: __2020-12-28 19:22:14__

> Won't install. When I click next after accepting T&C it says I'm not connected to the Internet. Could it be because I have the covid tracker program installed? Turns out if you have a VPN installed it will not work.<br> :date: __2020-12-20 12:00:57__

> Good idea but drains battery extremely fast. Cant be in public spaces anymore than an hour with it on or my phone dies<br> :date: __2020-12-18 04:02:10__

> Okay good<br> :date: __2020-12-15 16:23:30__

> Think it works!<br> :date: __2020-12-06 07:48:00__

> It would be great if updates of local area were posted, and the latest government updates policy in the area.<br> :date: __2020-11-30 17:37:16__

> App is fine but uses a LOT of data.<br> :date: __2020-11-27 16:07:22__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 2 reviews"/>
</p>

> Does it do anything . No buttons seem active<br> :date: __2020-12-23 12:48:16__

> Its a good idea but while it was installed, it messed up my Bluetooth connections. Couldnt use any Bluetooth devices while it was installed<br> :date: __2020-12-22 04:04:22__

> Following the latest update It appears my phone had turned off the exposure notifications switch in settings / Google/ covid-19 exposure notifications. What is worrying was / is the Protect Scotland app did not notify me in any way, until I happened to open the app by chance and only then did a warning appear. Why doesn't the app generate a warning every time it tries to check or update it's database ? It seems a very basic failing. ☹️😳 Also why no exposure checks reported anymore ?<br> :date: __2020-12-19 02:35:30__

> Absolutely destroyed my battery life polling live connections for proximity checking. Also didn't warn of a close contact.<br> :date: __2020-12-14 12:29:30__

> How do I know this app is working?<br> :date: __2020-11-24 19:52:43__

> Great idea. Had to uninstall though as it started draining memory and wouldn't push notifications as a result. Might not be apps fault, could be mine or my phone's ability. Either way, can no longer use.<br> :date: __2020-11-20 07:16:33__

> Doesn't work, went on the app and then got a notification that ive been in close contact with an infexted person. This was 13 days after i was in contact with the person. Never got a text phone or email either. Just aswell i dont have any symptoms<br> :date: __2020-11-17 22:25:32__

> I have an android phone. This app gives me no notifications. Other users with iPhones tell me they get notifications saying they have no contacts and how many people they have been matched against etc. Why would that be?<br> :date: __2020-11-15 21:56:30__

> I WASNT NOTIFIED OF MY EXPOSURE TO SOMEONE WHO TESTED POSITIVE WITH COVID-19 TILL 6 DAYS LATER. NOT MUCH GOOD IF I HAD OF UNKNOWINGLY BEEN POSITIVE AND ASYMPTOMATIC. CLEARLY THE APP NEEDS TO BE IMPROVED AS WELL AS USED - DOWNLOADED BY MILLIONS MORE PEOPLE IF IT IS TO BE EFFECTIVE OR WORTHWHILE.<br> :date: __2020-11-12 23:38:12__

> To be honest I put this app on my phone when I was in Scotland for a week it didn't really seem to do anything like the nhs app in England<br> :date: __2020-11-12 15:01:09__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 1 reviews"/>
</p>

> Not being updated with exposure checks sitting at 0 in 14 days not sure if this is a problem.??<br> :date: __2021-01-03 12:35:47__

> Stopped checking without notifying me. So hasn't worked for god knows how long.<br> :date: __2021-01-02 20:51:21__

> This app has stopped working and no notifications reported since early December. This software is supposed to help keep us safe !!! This is scandalous. FIX IT !!!!!<br> :date: __2021-01-02 11:04:19__

> Totally useless. I've known several people who've had it and the app hasn't alerted me. Apparently they aren't managing to trace most cases. Not surprising from the same track and trace that told me I didn't need to isolate, can return to work etc. despite someone I live with being told to isolate because they tested positive (we all tested at the same time). ScotGov and Scot NHS have messed this up entirely. They only look better in comparison to the disaster that is BoJo and the UK Gov.<br> :date: __2021-01-02 09:44:03__

> Absolutely useless; people who are positive are going to go out with app running and Bluetooth on? REALLY? Dumbfounded that anyone even tried to use this Uninstalling....<br> :date: __2021-01-01 01:53:27__

> Not performing checks. One check don in 14 days. The only way I got it to perform the check at all was to turn Bluetooth off and on. Have had iss for 2 months. Reinstalled and insured all battery optimisations off. All emails to developer ignored. May just uninstall.<br> :date: __2020-12-31 22:24:22__

> Exposure notification has not been updated since the 8th of December. This is the 31st at time of writing. I assume for 23 days i have had no protection from this app. Seems absolutely pointless.<br> :date: __2020-12-31 20:01:16__

> Won't check me automatically, have to manually refresh the app.<br> :date: __2020-12-31 16:59:52__

> 0 checks in 14 days. Another SNP failure<br> :date: __2020-12-31 14:30:27__

> I've been diagnosed with Covid, have been given a code, however when I try to input it into the App, the code is too long. So it doesn't work. Pointless<br> :date: __2020-12-31 02:46:28__


