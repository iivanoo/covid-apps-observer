# Protect Scotland
App version ``1.2.1``

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
| **Latest version** | 1.2.1 |
| **Last update** | 2021-02-17 10:10:01 |
| **Recent changes** | Minor test changes. |
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

The Protect Scotland app has been installed by more than **500000** times. At this time, **2827** rated the app and its average score is **4.216312**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 1986

:star::star::star::star:: 250

:star::star::star:: 130

:star::star:: 140

:star:: 321

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 5 reviews"/>
</p>

> Love you Scotland<br> :date: __2021-03-14 11:55:20__

> If it helps everyone to be safe and stay safe quickly, then of course it's not a problem 👌<br> :date: __2021-03-12 21:44:05__

> Great<br> :date: __2021-03-11 16:21:52__

> Very good<br> :date: __2021-03-09 21:22:00__

> Good<br> :date: __2021-03-07 17:29:29__

> Kept me covid free from all the halfwit mouth-breathers<br> :date: __2021-03-05 21:38:57__

> Very good<br> :date: __2021-03-01 10:07:11__

> Not used it for a long time,but it's brilliant so far<br> :date: __2021-02-28 10:54:25__

> Fantastic app easy to use<br> :date: __2021-02-27 10:12:44__

> Just had a message from track and trace so it works thanks<br> :date: __2021-02-26 09:40:37__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 4 reviews"/>
</p>

> Good helpful app<br> :date: __2021-02-23 17:24:21__

> Very good.<br> :date: __2021-02-22 14:00:38__

> The problem I have is police access but I'm using as the place is drowning in COVID19<br> :date: __2021-02-21 21:56:07__

> Good app but think you need everybody to sign up. Next door neibour had covid 19 but didnt know until a few weeks later.<br> :date: __2021-02-20 21:24:16__

> Had no interactions<br> :date: __2021-02-17 14:29:32__

> Notified<br> :date: __2021-02-14 15:57:22__

> Useful<br> :date: __2021-02-12 16:43:23__

> Very important app very good<br> :date: __2021-02-07 17:27:01__

> Excellent. Many thanks for making this app which keeps us all safer and aware.<br> :date: __2021-01-27 22:28:42__

> Updating review,,,track and trace provided me with new code which worked within the app. Will say I have been in contact with two people who tested positive but had no notification through app but dont know if they inputted the code 🤔<br> :date: __2021-01-20 13:31:05__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 3 reviews"/>
</p>

> Seems ok<br> :date: __2021-03-09 20:15:55__

> Oooft photo.yruk<br> :date: __2021-02-25 12:44:41__

> Not enough people using it to make it effective.<br> :date: __2021-02-19 17:56:39__

> None yet .<br> :date: __2021-02-18 22:15:08__

> I received a notification to self-isolate back in November. When I checked the periods of exposure on the Google notification page there had been no exposure checks for several days including the day I was allegedly exposed. It turned out I was nowhere near anybody that had corvid-19. My next door neighbour had tested positive a week or so before. The Bluetooth picked up the notification through the wall.<br> :date: __2021-02-12 14:22:32__

> None<br> :date: __2021-01-22 22:34:21__

> An ok app but my husband and I both tested positive on the same day. The following day, we each received a text to say we'd been in close contact with someone who had tested positive. Given we live in the same house ...<br> :date: __2021-01-20 18:16:11__

> Nice if there was a log of when it was working and when instead of praying that a notification comes up if you've been exposed.<br> :date: __2021-01-13 18:32:20__

> Update: appear to be getting daily exposure updates now. Will give the app another try. I have had zero response from the developer.<br> :date: __2021-01-09 00:16:58__

> The app used to work fine until the 10 Dec update but then stopped checking for exposures automatically. It was difficult to report the issue --- it feels like mails / app reviews only got attention after people made fuss on social media. The app works OK now, after the 5 Jan update, but I wish there was an easier way to report bugs, and more transparency regarding existing ones.<br> :date: __2021-01-08 13:18:19__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 2 reviews"/>
</p>

> Twice in three days I was contacted to isolate for 10 days despite never being in anyone's company inside or out within two meters I haven't even been near my own family. If passing someone on a pavement within seconds triggers the app for you to isolate then what's the point? They sell coffee at a door where people congregate on a pavement less than two meters to get past?<br> :date: __2021-03-13 10:03:34__

> Gave me a notification saying I had been in contact with someone with covid and had to self isolate....10 days AFTER I had been in contact with them and I only had to isolate for 1 day?? Not convinced it works or it is very slow to update you.<br> :date: __2021-02-19 14:05:01__

> When I first got the App I thought it was great to have it but now I am convinced it doesn't work giving people false confidence they've not been in contact with Covid, I have been in close contact with covid infected people yet never had notification. I think its flawed by requiring people to self input if they have it. Yet reading other reviews such as people in same household both entering details and none being informed that they've been in close contact? Raises suspension app authenticity<br> :date: __2021-02-14 10:44:35__

> I was quite naive and feeling safe because I hwe receuved zero contact alerts, so was blissfully confident that I was OK. Until today that is, when I discovered that a) there was an update that was not automatically applied, b) there are so many criticisms of the app and c) so many complaint communucations to the developer remain unanswered.... Is the app a complete con? Is it just to calm the naive and stupid like me. I had not encountered any issues, but then I didn't expect to.. I was safe???<br> :date: __2021-02-14 01:07:48__

> There is no way of knowing if it iseven working. Updates saying everything is fine you haven't been in contact with a positive person would be nice.<br> :date: __2021-02-12 13:30:55__

> Never had an alert no idea if that's working and there's no way to take two phones and do a diagnostic safe proximity test between them for reassurance. I simply don't trust this or the NHSEngland equivalent and I use both.<br> :date: __2021-02-12 04:20:30__

> I don't know if it works right..<br> :date: __2021-02-11 11:40:25__

> Cannot increase or adjust the font size. I am severely visually impaired/blind.<br> :date: __2021-02-04 14:05:45__

> I had a message via the app once but when I clicked on it, it disappeared.theres nothing in app about using QR code...or how.<br> :date: __2021-01-17 09:03:08__

> Known not to work as positive testing patients do not put in their results<br> :date: __2021-01-16 11:16:29__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.scot.covidtracker 1 reviews"/>
</p>

> Ok stop giving me this ad I don't go outside<br> :date: __2021-03-13 22:31:14__

> I have this app on both my phone and my works phone. I've been in contact with 5 people who have had covid . 5 of them gave my details as being close contact . I have my works phone and personal phone on me at all times. Yet not once did I get anything from track trace alerting me of my contact with covid. I did isolate and contacted people I was with to be vigilante of any symptoms. I didn't have any but i still isolated to protect others. Which is clearly not what this app is doing at all.<br> :date: __2021-03-11 22:05:24__

> Waste of tax payers money had this app downloaded from day 1 had to manually update the app a few months back. How long was I using an outdated app dont waste time downloading this lie of an app<br> :date: __2021-03-09 17:45:07__

> Had covid but no code given to make others aware from track and trace. Makes app useless. All it is is an app to monitor what your doing and when.<br> :date: __2021-03-06 00:52:40__

> Doesn't work with Huawei P40 mobile. Google play issue with Huawei. Therefore there needs to be another solution to download that does not involve Google Play.<br> :date: __2021-03-04 17:54:25__

> Total lack of confidence in this. I spent a lunch break across the table from a friend who tested positive, and worked with another person. Test and trace failed to notify me. Ludicrous and ineffective. Utter waste of time and has caused me much worry.<br> :date: __2021-03-02 23:16:31__

> I downloaded the app but then found you need to have Bluetooth enabled permanently. For those of you that don't know this is a security risk as you could be hacked. So back to just wearing a mask and being sensible.<br> :date: __2021-03-02 19:14:42__

> Don't know if it works as never see any messages?<br> :date: __2021-03-02 09:46:46__

> Haha. Why would you need to fake the rating. Is it because it's a fake virus...#Flu #Controlavirus<br> :date: __2021-02-27 20:48:08__

> Twice notified by the app to isolate and twice it has been ridiculously late in doing so. First instance was 8 days late and most recently 5 days late. Pointless app that simply doesn't protect anyone.... deleted.<br> :date: __2021-02-23 06:49:05__


