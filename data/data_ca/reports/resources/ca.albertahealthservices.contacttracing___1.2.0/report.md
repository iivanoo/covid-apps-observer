# ABTraceTogether
App version ``1.2.0``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="ABTraceTogether icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | ABTraceTogether |
| **Unique identifier** | ca.albertahealthservices.contacttracing |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=ca.albertahealthservices.contacttracing](https://play.google.com/store/apps/details?id=ca.albertahealthservices.contacttracing) |
| **Summary**  | This app is from the Government of Alberta to augment manual contact tracing. |
| **Privacy policy** | [https://alberta.ca/ABTraceTogetherPrivacy](https://alberta.ca/ABTraceTogetherPrivacy) |
| **Latest version** | 1.2.0 |
| **Last update** | 2020-06-18 01:42:41 |
| **Recent changes** | Minor Bug Fixes |
| **Installs**  | 50,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 30, 2020 |
| **Size**  | 9.5M |
| **Supported Android version**  | 8.0 and up |

### Description
> This app is being brought to you by the Government of Alberta.
<br>This app is intended for ages 14+.
<br>Some of the key benefits of this app are to:
<br>• Augment our current contact tracing efforts to provide guidance and care to those who are or may be infected
<br>• Help keep Albertans safe by limiting the spread of COVID-19 through more individuals self-isolating earlier
<br>The app is most effective if it reaches a strong penetration of usage among Albertans, which means the more people that use the app, the better the app works.
<br>Once a user registers their phone number with the app, the app uses bluetooth to log contact with other individuals who have the app when that contact is within approximately 2 meters. If a user tests positive for COVID-19, they will be contacted by an Alberta Health Service Contact Tracer, and asked to voluntarily upload their data to Alberta Health Services so that anyone the user came into close contact with over the previous 14 days can be notified.
<br>Geolocation data is not collected by the app or by Alberta Health Services. The Bluetooth exchange ID log data collected is stored locally in your phone in an encrypted form. This data will not be accessed by Alberta Health Services unless and until you choose to upload it as a result of being diagnosed with COVID-19. Mobile numbers or any other personal information are not revealed to other app users.
<br>Personal Information collected:
<br>- Phone number
<br>Permissions required:
<br>- Bluetooth enabled
<br>- Location 
<br>- Push notifications
<br>Copyright 2020 Government of Alberta


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 


## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Government of the Province of Alberta |
| **Website**  | [http://alberta.ca/ABTraceTogether](http://alberta.ca/ABTraceTogether) |
| **Email** | ABTraceTogetherSupport@gov.ab.ca |
| **Physical address**  | [3720 - 76 Avenue Edmonton, AB T6B 2N9](https://www.google.com/maps/search/3720%20-%2076%20Avenue%20Edmonton,%20AB%20T6B%202N9) (Google Maps) |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Government+of+the+Province+of+Alberta](https://play.google.com/store/apps/developer?id=Government+of+the+Province+of+Alberta) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Android10, version 10 (API level 29) |
| **Effective target Android version**  | Android10, version 10 (API level 29) |
| **Minimum supported Android version**  | Oreo, version 8.0.0 (API level 26) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_BACKGROUND_LOCATION** | :warning:**Dangerous** | Allows an app to access location in the background. 
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_WIFI_STATE** | Normal | Allows applications to access information about Wi-Fi networks. 
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

**Telephony identifiers leakage**
> - This application reads the unique device ID, i.e the IMEI for GSM and the MEID or ESN for CDMA phones<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the ': connect, resolve' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Code execution**
> - This application loads a native library: 'authjni'<br>
> - This application loads a native library: 'crypto'<br>
> - This application loads a native library: 'uvpn'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The ABTraceTogether app has been installed by more than **50000** times. At this time, **453** rated the app and its average score is **2.98**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 144

:star::star::star::star:: 36

:star::star::star:: 77

:star::star:: 54

:star:: 140

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 5 reviews"/>
</p>

> 5 stars but still......Google maps tracks your phone -where, when- what time and exact place literally on a bus, anyone with a Gmail account, their GPS or location setting on their Android or Apple phone can access their location history, even your commands to Ok Google. and easily share this information with health officials if the time arises. Just thought I'd point that out.<br> :date: __2020-07-04 04:12:15__

> Installed it. Hope I'll need to use it!<br> :date: __2020-06-29 22:14:01__

> Works well on S10, no issues to report here. Impressive beard illustrations to boot!<br> :date: __2020-06-28 14:37:55__

> Bring app please to every one mandatory.<br> :date: __2020-06-23 03:30:47__

> I have entered my phone number but no six digit code has been sent to me. I am stuck in step 1 of the process. Update: app is working now. Great app.<br> :date: __2020-06-21 04:03:50__

> Well designed app that has had no adverse effect on battery life! When I first got it I was force closing it when not out to conserve battery. I decided to test leaving it on 24/7 and over two days I couldn't see any extra battery consumption. I was honestly shocked and have left it on since. Also really like that this app DOESN'T use GPS only my Bluetooth to see who I've been in contact with instead of tracking my every movement.<br> :date: __2020-06-08 00:40:09__

> Very important and we'll designed application, privacy is protected and will help keep spread under control<br> :date: __2020-06-02 04:31:45__

> Very " nice " Thanks !!<br> :date: __2020-05-26 04:25:34__

> Installed & activated on Samsung S9 without any issues. Runs fine. There is extra battery usage, but it's tolerable for me.<br> :date: __2020-05-25 03:53:49__

> Amazing app, feels so good to know the government knows all. I cannot wait for the vaccine. Please increase my taxes and fund more the media.<br> :date: __2020-05-25 03:45:04__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 4 reviews"/>
</p>

> I noticed the last 2 days this app has been draining my battery. Use to have 45% left at bedtime, now only 10% at 1 pm. Just did the update, which I didn't know about. So hopefully it fixes this battery issue. (03-Jun-20). UPDATE: After the update the app no longer drained my battery. I noticed a drain on my battery again today (06-Jul-20) and checked for an update, which there was. If you notice your battery being drained, just update the app.<br> :date: __2020-07-06 16:07:00__

> I originally thought the app was draining my battery but it turned out to be something else. It seems to work fine and is unobtrusive except for the always on tray notification.<br> :date: __2020-07-05 16:46:23__

> I don't huv any pinyon<br> :date: __2020-06-30 07:19:48__

> Greetings to anyone who reads this, If the app is only getting a 3.0 (3 Stars), is there a problem with it? Please consider the following, none of which is/are (a) conspiracy theory/theories. I can say this because countless independent studies done across the world have all found these phenomena to be true. 1. Are delusional naysayers about the Covid-19 pandemic keeping the app from scoring higher by not subscribing to it? ; or 2. Is the low rating the possible result of most of the current subscribers not getting alerts, and that others - who haven't (yet) subscribed to the app - are being lulled into a false sense of safety, even complacency? ; or, 3. Is the app a bit of a lame-duck technology - on the part of the government - and the app is not functioning properly or at all? ; or, 4. Are Albertans simply complacent about the pandemic? Go into any store which has clearly defined and labelled "shopping lanes" and other forms of signage, along with PA and public service announcements exhorting shoppers to abide by the store's rules and Alberta Health's guidelines, and you'll experience first-hand what I'm talking about. Indifference, obtuse behaviour, willful or blind ignorance, etc. ; or, finally (at least for now) 5. Is the media, which continues to feed us only what is "news worthy" to it (as it has done for nearly 3 generations), the real problem? If the app is not being kept in front of viewers or in the ears of listeners, is that the reason for the low rating? The media, along with government, controls the access to news. More often than not, it's the media doing this because "news worthy" really means that which attracts and is supported by the most lucrative advertising revenue streams. As CFCN says "All the news you need to know", which translates, "All the news we want you to hear". CBC, CTV, and the American networks on cable and satellite TV are all complicit in this. I'll stop now, since I've run out of time to continue. However, I must add that if the government is truly engaged in leading Albertans out of this tragedy, it will not alter, delete, expunge, rephrase, or in any other way, edit my comments because some of them have suggested government shortcomings. I'm keeping a copy of this for my own files and for posterity. Clayton Walls, Calgary June 11, 2020 @ 1300 h MDT<br> :date: __2020-06-11 21:00:38__

> I think the idea is great as long as it's executed properly however there seems to be a glitch with the app as it's used 33% of my battery so far today.<br> :date: __2020-06-04 03:45:04__

> I don't need data on to run it. And it doesn't drain my battery despite having Bluetooth on . So far so good<br> :date: __2020-05-23 03:41:32__

> Same as others have said, works fine, installed fine, just wish there was an on /off button for scanning. I can't turn my Bluetooth off because I wear a smartwatch, and I don't need the app when I'm not leaving my house or going anywhere that I will not be in contact with other people. It is a bit of a hindrance having to go in and out of settings all of the time to enable the app permissions, please just add a button to this app.<br> :date: __2020-05-23 00:18:05__

> Won't know if it works till it's needed. Hopefully never. Always has a 1 superimposed on the icon, but nothing apparent when I open the app.<br> :date: __2020-05-15 20:40:40__

> I was totally surprised on how much this app draws dowm my battery , worse than f-cebook app, will be definitely removed once things cool down ...<br> :date: __2020-05-15 00:48:59__

> Good app and hopefully it gets installed and used more. Like others are saying, it needs and off button because of the battery drain when using it at home. Most people are at home now so this should be a feature available....<br> :date: __2020-05-12 17:49:39__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 3 reviews"/>
</p>

> Only installing for long periods of exposure It seems to cause overheating with my phone. If I have the app installed (paused or unpaused) it seems to ramp up internal temps. Also, there should be an option to say you are at home, so you don't have to pause the app. The constant need to have BT on, even while at home, is annoying. I get why but it is frustrating.<br> :date: __2020-07-03 00:54:11__

> I uninstalled the ap due to high battery usage from the app.<br> :date: __2020-06-28 21:23:04__

> I'm sure this a great service to use. The only issue I have is having Bluetooth on all the time. It drained my battery by 60% in 10 hours while I was at work. I'm out in the community a lot, so I would need to keep it on for it to be useful.<br> :date: __2020-06-26 16:41:45__

> Had it for a whole 20 minutes, battery went from 100% to 90% Im all for tracking it, but the app is kinda pointless if my phone is dead and I cant get notifactions<br> :date: __2020-06-24 19:21:26__

> Battery killer, but worth running if you can. Please add support for Androids "COVID-19 exposure notifications"<br> :date: __2020-06-20 22:25:38__

> I would have really liked to use this to help out but my battery life is non-existent. I just got a new S10 and my battery died a little over halfway through the day. If they could somehow fix this app to turn off when you're not moving or something then maybe it wouldn't drain your battery so bad? No idea, but I had to uninstall it.<br> :date: __2020-06-17 03:36:59__

> This should also include covid 19 stats available at AHS website. Push notifications for outbreaks of chosen locations by the user or if there is any change in current restrictions. Info on current public health order, public health guidance. Latest news and announcements (ie. Change in testing policies, etc), provide relevant links (ie. Biz connect), then it may encourage people to install it.<br> :date: __2020-06-16 17:28:05__

> Install was very easy. Done in under 2 minutes. App is a great idea for the times. Having said that, yes the battery drain is amazing. Started as a 5 but now a 3. I wish it was more.<br> :date: __2020-06-13 01:17:26__

> The principle is good and I'd really like to help by using this app but a week after installing it, my battery is drained before the afternoon is over. I have to uninstall. When the developers can make it more efficient in power usage I'd be happy to install it again<br> :date: __2020-06-09 23:39:11__

> I've had no complaints up until a couple of days ago when my phone indicated that AB Trace Together has been using 35.6% of my battery, while at home. I disabled Bluetooth and it didn't change or conserve the battery. My phone has been on for 20 minutes this morning and its already used 6.1% of my battery. Prior to this, battery usage was negligible. Updated it and hoping that helps.<br> :date: __2020-06-08 16:52:26__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 2 reviews"/>
</p>

> Takes way too much battery life. 39% over 4 hours....<br> :date: __2020-07-08 22:16:47__

> Can't connect to car without uninstalling. Ridiculous as it intereferes with other bluetooth so how can I even use it. Can't use it if I need bluetooth.<br> :date: __2020-07-08 03:36:51__

> I barely go outside, so all it did was eat my battery throughout the day. Even if I went outside, I never got a notification from the app.<br> :date: __2020-07-04 11:08:43__

> This app is a terrible battery drain. I had to uninstall to keep battery more than a few hours.<br> :date: __2020-06-29 19:45:55__

> Anybody else have to uninstall this app cause it makes your phone glitchy and kills the battery?<br> :date: __2020-06-23 15:02:58__

> Doesn't stay active. Will disappear sporadically and you have to restart your phone to make it appear again. I've gone days before I realize it's gone again so what's the point?<br> :date: __2020-06-18 05:40:47__

> I want to understand why the app needs permission to location data when the app description says they don't collect it. Is there any reasonable explanation?<br> :date: __2020-06-18 03:54:44__

> Battery drain.<br> :date: __2020-06-14 23:21:25__

> Phone - Essential PH-1 I don't know if it's just me, but my phone heats up quite spectacularly, draining the battery. The app also has huge buttons and small text, and literally has a huge button saying NEXT----> with small text above it saying don't press unless asked to. I haven't used it long enough to get any results, but with the issues immediately apparent, I don't recommend it.<br> :date: __2020-06-14 06:37:14__

> This app was fine for a few weeks then all of the sudden started eating the battery life. No idea why. I had to uninstall because I was no longer making it through the work day with enough battery.<br> :date: __2020-06-11 11:48:28__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 1 reviews"/>
</p>

> Here's a tip; if my device can see yours via Bluetooth, there's a good chance I can access your device and everything on it using an apk like Superblue. Don't be an idiot. This is exploitable Traceware.<br> :date: __2020-07-10 02:31:24__

> Started to drain my battery of my fairly new phone.<br> :date: __2020-07-08 21:01:53__

> Allow me to turn off bluetooth when at home or better yet, have a home zone that automatically turns bluetooth off and I'll put it back on my phone. Too invasive.<br> :date: __2020-07-08 02:19:45__

> Ir drains my battery big time<br> :date: __2020-07-08 00:43:59__

> Unable to activate. Installs okay but when asking for cell phone number it always says the server is down for the last month.<br> :date: __2020-07-06 23:48:44__

> I want to keep this app but it's draining my battery. It seemed okay the first few weeks of using it but recently it's been overheating my phone. I checked my battery usage and it says this app is using 44% of my battery. Doesn't seem feasible to keep running it if I'm going to have to keep my phone on a charger most of the day.<br> :date: __2020-07-06 03:09:24__

> dont like it didnt do anything to help me wast of time<br> :date: __2020-07-04 07:06:04__

> I had this a few days after release and didn't feel the usefulness. But it kept draining my battery. 39% use compared to all other apps. My battery kept heating up. Uninstalled.<br> :date: __2020-06-25 01:11:32__

> Wanted to help prevent the spread of covid. This app is garbage. Used 76% of my phone battery in 12 hours. Uninstalled. Now we are all gonna get covid.<br> :date: __2020-06-23 04:27:55__

> This app is 100% not anonymous, it starts out by asking for your phone number, which allows the government to get your name and then track you. If you care at all about your privacy do not install this app. There is no need to provide your phone number for what they have proposed the goal of this app to be. They could have notified you within the app.<br> :date: __2020-06-22 11:53:21__


