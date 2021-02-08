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

> No issues. But should be compulsary.<br> :date: __2021-02-05 14:31:15__

> Safety with secure protection.<br> :date: __2021-02-04 17:06:43__

> Keeps you safe<br> :date: __2021-02-03 17:08:24__

> Couldn't ask for a better app,so helpful in every possible way,keeps you very much up to date of all that is happening & of any changes that is taking place.. Thank you so much, Protect Scotland Team, you are a real Godsend,& greatly appreciated..x<br> :date: __2021-02-02 14:23:50__

> Under these terrible circumstances just now with the pandemic its a vital app.<br> :date: __2021-02-01 13:12:47__

> Best place for updates<br> :date: __2021-01-30 22:33:40__

> Uninvasive and reassuring<br> :date: __2021-01-30 08:24:33__

> Understanding the rules<br> :date: __2021-01-30 04:37:49__

> first class<br> :date: __2021-01-28 13:58:10__

> Just started using<br> :date: __2021-01-22 19:13:26__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 4 reviews"/>
</p>

> Excellent. Many thanks for making this app which keeps us all safer and aware.<br> :date: __2021-01-27 22:28:42__

> Updating review,,,track and trace provided me with new code which worked within the app. Will say I have been in contact with two people who tested positive but had no notification through app but dont know if they inputted the code 🤔<br> :date: __2021-01-20 13:31:05__

> Ok<br> :date: __2021-01-14 15:36:03__

> OK<br> :date: __2021-01-07 10:58:35__

> It saves lives<br> :date: __2021-01-02 00:22:28__

> Have not needed to use<br> :date: __2020-12-23 00:24:50__

> Easy to use no problems except for the battery so had to use a back up facility<br> :date: __2020-12-16 22:14:09__

> Okay I think.I may just have been so Isolated I have not had a concern ..yet .<br> :date: __2020-12-14 23:01:39__

> I haven't had to use it so far<br> :date: __2020-11-26 23:25:03__

> Just downloaded the app, some folk saying you dont need to turn on location but the app says I have to keep both location and bluetooth on. Glad we have a safe app here in Scotland! 🏴󠁧󠁢󠁳󠁣󠁴󠁿<br> :date: __2020-11-18 14:51:54__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 3 reviews"/>
</p>

> None<br> :date: __2021-01-22 22:34:21__

> An ok app but my husband and I both tested positive on the same day. The following day, we each received a text to say we'd been in close contact with someone who had tested positive. Given we live in the same house ...<br> :date: __2021-01-20 18:16:11__

> Nice if there was a log of when it was working and when instead of praying that a notification comes up if you've been exposed.<br> :date: __2021-01-13 18:32:20__

> Update: appear to be getting daily exposure updates now. Will give the app another try. I have had zero response from the developer.<br> :date: __2021-01-09 00:16:58__

> The app used to work fine until the 10 Dec update but then stopped checking for exposures automatically. It was difficult to report the issue --- it feels like mails / app reviews only got attention after people made fuss on social media. The app works OK now, after the 5 Jan update, but I wish there was an easier way to report bugs, and more transparency regarding existing ones.<br> :date: __2021-01-08 13:18:19__

> Just got a notification after accidently turning off my.location to be informed I haven't been checked since 14th December !!!<br> :date: __2021-01-07 23:23:07__

> Was working for a while but not performed a check since 16th December 2020 despite always being on.<br> :date: __2021-01-03 22:07:19__

> I occasionally check this app and all is well. Thank God.<br> :date: __2020-12-30 23:14:17__

> No exposure checks in the last 14 days, yet I've had bluetooth & location switched on.<br> :date: __2020-12-30 14:39:08__

> Not enough information<br> :date: __2020-12-29 03:11:50__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 2 reviews"/>
</p>

> Cannot increase or adjust the font size. I am severely visually impaired/blind.<br> :date: __2021-02-04 14:05:45__

> I had a message via the app once but when I clicked on it, it disappeared.theres nothing in app about using QR code...or how.<br> :date: __2021-01-17 09:03:08__

> Known not to work as positive testing patients do not put in their results<br> :date: __2021-01-16 11:16:29__

> Entered my post code to see the restrictions in my post code and it can't find it<br> :date: __2021-01-13 16:28:03__

> Never tells me when I have been in known contact. Wouldn't except a code for positive result<br> :date: __2021-01-11 00:09:22__

> Is this app working.<br> :date: __2021-01-08 23:48:11__

> Does it do anything . No buttons seem active<br> :date: __2020-12-23 12:48:16__

> Its a good idea but while it was installed, it messed up my Bluetooth connections. Couldnt use any Bluetooth devices while it was installed<br> :date: __2020-12-22 04:04:22__

> Following the latest update It appears my phone had turned off the exposure notifications switch in settings / Google/ covid-19 exposure notifications. What is worrying was / is the Protect Scotland app did not notify me in any way, until I happened to open the app by chance and only then did a warning appear. Why doesn't the app generate a warning every time it tries to check or update it's database ? It seems a very basic failing. ☹️😳 Also why no exposure checks reported anymore ?<br> :date: __2020-12-19 02:35:30__

> Absolutely destroyed my battery life polling live connections for proximity checking. Also didn't warn of a close contact.<br> :date: __2020-12-14 12:29:30__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 1 reviews"/>
</p>

> So in a month this app has used 0.00mb of data.. it doesnt work and totally pointless. More SNP propaganda<br> :date: __2021-02-06 12:24:45__

> Unless you book a test through the app you cannot get a code to put in so it is near enough useless<br> :date: __2021-01-29 10:00:14__

> Useless<br> :date: __2021-01-28 09:25:38__

> Exposure checks stopped a while back, despite havin the updated version. Uninstalled & re-installed - checks restarted but stopped again. Switched bluetooth off & on to nudge checks back into action. Only works for a while. Emailed app developer weeks ago but no response. Utterly useless app which fails to address serious need for which it was meant; shortcomings could turn out to be lethal for anyone relying on its proper function as a layer of protection against Covid spread.<br> :date: __2021-01-27 21:46:16__

> Would be nice to be informed that app required updating to work!? Meanwhile I've been working not knowing anything ffs!! 😡🤬<br> :date: __2021-01-27 09:49:39__

> Pathetic even worse than the English one We are all Doomed 🙄👻👻🥴👻<br> :date: __2021-01-25 19:22:45__

> I have 4 matches in the last 13 days when I check exposures but I have had no alerts? I work in retail so around thousands of people a day so could have it and be spreading it without knowing 😣<br> :date: __2021-01-22 01:42:23__

> Waste of time. I tested positive so asked for a code to enter into the app but track and trace said I didn't need one as I would be self isolating and wouldn't be in contact with anyone. So what is the point of this app?<br> :date: __2021-01-21 20:50:31__

> Carried out three checks in one month. Have reinstalled and still not working properly.<br> :date: __2021-01-20 13:54:04__

> Basic and unreliable<br> :date: __2021-01-20 09:49:48__


