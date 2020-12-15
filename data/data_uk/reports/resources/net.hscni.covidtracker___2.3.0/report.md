# StopCOVID NI
App version ``2.3.0``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="StopCOVID NI icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | StopCOVID NI |
| **Unique identifier** | net.hscni.covidtracker |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=net.hscni.covidtracker](https://play.google.com/store/apps/details?id=net.hscni.covidtracker) |
| **Summary**  | The coronavirus contact tracing app for Northern Ireland |
| **Privacy policy** | [https://covid-19.hscni.net/privacy-notice/](https://covid-19.hscni.net/privacy-notice/) |
| **Latest version** | 2.3.0 |
| **Last update** | 2020-11-13 18:21:47 |
| **Recent changes** | - Create and send a certificate proving you need to self-isolate to other people and organisations, e.g. your employer or the Social Security Agency.<br>- Self-isolation periods are now calculated based on the date of exposure.  |
| **Installs**  | 100,000+ |
| **Category** | Medical |
| **First release** | Jul 29, 2020 |
| **Size**  | 108M |
| **Supported Android version**  | 6.0 and up |

### Description
> If you are 11 or older and live in Northern Ireland you can use this HSC contact tracing app. By using it you will help stop or slow the spread of coronavirus.
<br>** Support the health services **
<br>** Help avoid more lockdowns **
<br>** Save lives **
<br>How does the app work?
<br>If you are in close contact with an app user who has told their app that they have COVID-19, you will get an alert from this app. You won’t know who it was or where it happened. You must then self-isolate for the period shown in the app. There’s advice on how to self-isolate and answers to common questions about this in the app.
<br>If you test positive for COVID-19 you can tell this app. Other app users that you’ve been close to will then be alerted. They won’t know that it was you or where it happened.
<br>** Works in the background on Bluetooth, not GPS, and uses very little battery **
<br>** Please keep Bluetooth on so the app can work properly **
<br>How is my privacy protected?
<br>** This app never knows your name or where you are, so it’s completely private **
<br>It uses the ‘Exposure Notification API’ developed by Apple and Google in a joint effort to help governments and health agencies reduce the spread of COVID-19 through contact tracing, with user privacy and security core to the design. This is sometimes called the ‘decentralised’ model.
<br>If you test positive for COVID-19 you will get a code by SMS text message from 'HSCresult'. When you put your code into this app you will be asked to share the 'Random IDs’ that your phone has been swapping with other app users over the last 14 days. This will allow us to tell those people that they have been exposed to COVID-19. 
<br>** We will never ask you to reply to the SMS text message **
<br>** Please ignore any message if it asks you to reply or send information **
<br>So that you can use this app when travelling abroad we will securely share 'Random IDs' with other countries. This also means that apps used by visitors from those countries will work here.
<br>** This app will never track your identity or location **


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/>  | <img src="screenshot_5.png" alt="screenshot" width="300"/>  | <img src="screenshot_6.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_7.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Health & Social Care Northern Ireland |
| **Website**  | [https://covid-19.hscni.net/contact-tracing/](https://covid-19.hscni.net/contact-tracing/) |
| **Email** | StopCOVIDNIApp@hscni.net |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Health+%26+Social+Care+Northern+Ireland](https://play.google.com/store/apps/developer?id=Health+%26+Social+Care+Northern+Ireland) |

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

The StopCOVID NI app has been installed by more than **100000** times. At this time, **478** rated the app and its average score is **2.67**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 148

:star::star::star::star:: 19

:star::star::star:: 43

:star::star:: 62

:star:: 206

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="net.hscni.covidtracker 5 reviews"/>
</p>

> Perfect<br> :date: __2020-12-10 13:47:17__

> Absolutely essential app.<br> :date: __2020-12-07 08:47:11__

> excellent service staving propjes live om no racis or colour kust a hitman Boeing me xXxjetiame xXx<br> :date: __2020-12-05 16:27:26__

> We are in a Lockdown for 2weeks Christmas Cancelled This Year<br> :date: __2020-11-29 08:12:05__

> I am a father and this app is help bust my lokel drug deler(he was my lokel deler UWU), and my dother infrormaeshen was stolen (shes 4)😁 Thank god the worden let me downlode (I foed my wife an this app )XD<3:3<br> :date: __2020-11-23 11:01:57__

> Great to see and well designed. Fantastic to have an app like this so quickly for NI<br> :date: __2020-11-22 23:32:11__

> Respect to our great NHS , and listen to them .<br> :date: __2020-11-20 15:20:02__

> It does what it says and this update will make things much clearer for anyone receiving notifications<br> :date: __2020-11-17 12:56:54__

> Thankfully no alerts yet<br> :date: __2020-11-06 22:40:58__

> Very good<br> :date: __2020-10-28 00:13:57__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="net.hscni.covidtracker 4 reviews"/>
</p>

> Zoe123<br> :date: __2020-11-22 15:45:06__

> Just discovered the app had been "Auto Disabled" on my android phone. Something to watch out for (When it's running you should get a notification once a week, reminding you and confirming that it is indeed running).<br> :date: __2020-10-21 23:33:44__

> Please add the capacity to scan QR codes like the NHS app does, not having this function leads to confusion in dealing with GB businesses in NI<br> :date: __2020-10-10 08:57:01__

> It seems to work, and I really hope it does.. it is simple, and not intrusive. I look forward to seeing his it pans out.<br> :date: __2020-10-08 01:00:45__

> This app only checks exposure if it comes within a short distance of someone else who has the app. No exposure checks mean you havent been close enough to someone for it to check.<br> :date: __2020-10-02 20:06:28__

> QUERY! If having to move devices, how are you supposed to transfer the existing exposure checks from the previous 14 days to the new device, in case any of those report a positive case?<br> :date: __2020-09-21 22:39:02__

> Once running, seems to be very good. But was hard to find. Wasn't immediately clear if there was a background daemon service running or the app had to be "minimized" but not closed to work. Samsung Galaxy 8 running Android 9: It seems Samsung's battery optimisation service was killing the app. After a reboot, it seemed OK, though. Closing/swiping away the app and then toggling bluetooth on/off showed it was still running (I got an alert from the app saying bluetooth needs enabled).<br> :date: __2020-08-13 21:40:20__

> No problems downloading and it appears active on my Samsung S10. Would love to understand more about the keys as we're registering them without leaving the house!<br> :date: __2020-08-12 22:11:42__

> Seems to work just fine, but the interface is slow and it's hard to know if this is actually running or if I have to load up the app manually every time.<br> :date: __2020-08-07 11:52:24__

> I found it easily, I just typed in covid and found the app. But like others have said, when you close the app and open it it says tracing not active then changes to active. Unsure if it is working when the app isn't open.<br> :date: __2020-08-04 11:47:01__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="net.hscni.covidtracker 3 reviews"/>
</p>

> Can you make a version of this app for the huawei app gallery?<br> :date: __2020-11-26 21:32:22__

> Does not give n Ireland<br> :date: __2020-11-20 13:22:56__

> The App keeps disabling itself.<br> :date: __2020-10-26 07:53:08__

> C. Nmu<br> :date: __2020-10-17 23:19:09__

> No log updates. Uninstalled and reinstalled the app for NI. Made no difference. How can we trust it.<br> :date: __2020-10-16 14:07:46__

> I don't know<br> :date: __2020-10-11 18:11:48__

> Downloaded this when it became available, but after the last update, it keeps pushing me to turn my bluetooth on and restart the app; my Bluetooth has been on, and restarting the app doesn't help. Only had this issue since the update, but makes having the app pretty much useless.<br> :date: __2020-10-11 15:06:04__

> Mine barely checks (once in 14 days) but my friends checks multiple times a day. I'm nearer much more people than them so I don't understand.<br> :date: __2020-10-11 11:19:25__

> I downloaded the app. I get that someone will notify me if I come into contact with someone who has the app and then tests positive. However, I feel it should give people either daily or weekly updates of places that the person has been and I wonder when two mobile phones that have the app downloaded on the phones - do they react to each other. Another thing is people on the island of ireland both north and south of the island should be able to use both apps together.<br> :date: __2020-10-06 23:59:37__

> Whose bright idea was it to remove the statistics section (daily number changes etc.) from the app, and not adding a link to where the information can be found?<br> :date: __2020-10-05 18:42:45__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="net.hscni.covidtracker 2 reviews"/>
</p>

> Got a notification to say i was in contact and had to isolate. Only problem was i had been in contact the 10th. First told of it the 23rd with 1day left to isolate. Its reliant on people updating the app with their test results and if they dont do that then nobody knows<br> :date: __2020-11-23 21:34:22__

> I had hoped that this app would provide useful timely and accurate information to users. Instead I see that the statistics are not kept up to date. By way of example today is 05/11/20 but the R number estimate is from 16/10/20. Come on people for the sake of credibility must do better!<br> :date: __2020-11-05 23:37:19__

> I don't see the point in this app. As I checked today 2nd November as I'd accidentally knocked off Bluetooth. Seen it last checked on 12th October. I am a key worker, I could potentially come into contact with this virus. And after 14 days it removes data. So that is a lot of potential contact with this virus missed. If it's not going to work and check then why have it installed?<br> :date: __2020-11-02 09:56:14__

> Either it doesn't work or nobody has it... since the 20th of October (it is now the 1st of Nov) I have had 2 notifications (checks), 1 of which are my partner. Pointless.<br> :date: __2020-11-01 20:20:25__

> Its not working keeps telling me connect to blutooth and I have!<br> :date: __2020-10-28 18:45:24__

> The app worked well but I noticed at times when I was out that no checks had been made. I did recieve an alert to isolate for 14 days which I did, yet on the 5th day into isolation I got another notification saying that I've been exposed and have to isolate for 14 days. I hadn't left to house, I didnt even leave my bedroom so I'm not sure how accurate this app is which is why I removed it.<br> :date: __2020-10-26 09:57:00__

> No alert given for App update. No weekly alerts given for 2 consecutive weeks<br> :date: __2020-10-24 04:50:41__

> Despite having my Bluetooth on constantly, the app is telling me tracing is not active. There is clearly a bug in the app that needs fixed.<br> :date: __2020-10-23 23:31:59__

> Fault app. Tells me in early hours of morning that there has been a huge number of checkins like 2000+/3000+ while im at home. But also saying 0 check ins in last 4 days-14 days. Have to open it again to start checks and i never switch off the bluetooth so no idea what happening.<br> :date: __2020-10-23 23:17:28__

> Dont think this works to well<br> :date: __2020-10-23 16:04:28__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="net.hscni.covidtracker 1 reviews"/>
</p>

> Shite dont work week late 😂😂😂😂🤬🤬🤬<br> :date: __2020-12-11 10:05:12__

> I got an alert tonight showing close contact on the 26th November.. Problem being the alert only came through when the isolation period ended that being 10th December? Very worrying!<br> :date: __2020-12-11 02:19:31__

> Downloaded app i was in touch with 3 people who tested positive nothing came up i rang the helpline says not to worry its not 100%<br> :date: __2020-12-06 11:30:28__

> Makes the phone sooo slooooow that it's unusable. Had to uninstall.<br> :date: __2020-12-05 22:01:17__

> Never seems to check, always a week or so behind.<br> :date: __2020-12-01 08:27:55__

> This app is completely pointless. Mine has to be reinstalled every couple of days after which it will carry out exposure checks for a day or 2 and then completely stop. I could have been in contact with numerous people and had to self isolate but I dont know because the app isn't doing the checks.<br> :date: __2020-11-29 10:37:50__

> Not getting anything from this site when first started told everyday now nowt<br> :date: __2020-11-27 15:11:31__

> Loads of Rubbish.<br> :date: __2020-11-22 18:35:12__

> Government surveillance scam,shhep fell for it!<br> :date: __2020-11-21 05:18:56__

> isn't it supposed to send notifications? because that's not happening<br> :date: __2020-11-18 09:53:06__


