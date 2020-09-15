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

> I have a 3 years old phone & I've had no problem with my battery. When keeping Bluetooth on, in a 12 hour period the battery usage was only 0.7%. My only complaint is that it shows an icon in my status bar regardless if Bluetooth is on or off. Personally I would prefer that the icon only shows when Bluetooth is off. Until we get the National app here at least it's one thing I can do. Who knows when we'll get the National one!?! Hopefully sooner than later!<br> :date: __2020-09-05 04:37:30__

> I like to have the App to protect myself. I feel more confident wherever i go knowing that if iam exposed to the virus i will be informed immediately and that way i can be tested and get the treatment i need. Thank you<br> :date: __2020-09-02 08:15:09__

> I have not had any problems at all aside from the battery drain which I solved by turning off my Bluetooth at home and turning it on while I am out.<br> :date: __2020-08-09 00:29:04__

> I like this app because it will inform me if I've been in contact with anybody that has this virus because I definitely do not want to get it thank you<br> :date: __2020-07-31 20:43:34__

> Runs consistently in the background, not a serious drain on battery.<br> :date: __2020-07-31 20:36:56__

> Covid 19<br> :date: __2020-07-24 20:40:27__

> Always working. Dont even know it's on unless I check. No noticable battery drain. App is being improved. No privacy issues. Do your part.<br> :date: __2020-07-17 00:28:28__

> Authentication is not sending text message before but is now working for me.<br> :date: __2020-07-15 20:48:15__

> 5 stars but still......Google maps tracks your phone -where, when- what time and exact place literally on a bus, anyone with a Gmail account, their GPS or location setting on their Android or Apple phone can access their location history, even your commands to Ok Google. and easily share this information with health officials if the time arises. Just thought I'd point that out.<br> :date: __2020-07-04 04:12:15__

> Installed it. Hope I'll need to use it!<br> :date: __2020-06-29 22:14:01__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 4 reviews"/>
</p>

> It doesn't drain my battery like others say. Not sure why others are having issues...?<br> :date: __2020-08-17 21:50:04__

> No issues with the app (Samsung Note 9).<br> :date: __2020-08-10 04:24:28__

> needs an off button holy moly I believed all the battery drain hype, especially since I'm a server at a restaurant I just leave my phone plugged in at the front desk and it's not a problem (heats up a bit tho). when I get home however it's worse because it was charging all day consuming power-at-will. the choice for me is to turn off background activity on the app in the settings when I get home. there's no sense in exchanging keys with my fam 24hrs a day. but I could easily forget it off :/<br> :date: __2020-07-19 23:06:46__

> I noticed the last 2 days this app has been draining my battery. Use to have 45% left at bedtime, now only 10% at 1 pm. Just did the update, which I didn't know about. So hopefully it fixes this battery issue. (03-Jun-20). UPDATE: After the update the app no longer drained my battery. I noticed a drain on my battery again today (06-Jul-20) and checked for an update, which there was. If you notice your battery being drained, just update the app.<br> :date: __2020-07-06 16:07:00__

> I originally thought the app was draining my battery but it turned out to be something else. It seems to work fine and is unobtrusive except for the always on tray notification.<br> :date: __2020-07-05 16:46:23__

> I don't huv any pinyon<br> :date: __2020-06-30 07:19:48__

> Greetings to anyone who reads this, If the app is only getting a 3.0 (3 Stars), is there a problem with it? Please consider the following, none of which is/are (a) conspiracy theory/theories. I can say this because countless independent studies done across the world have all found these phenomena to be true. 1. Are delusional naysayers about the Covid-19 pandemic keeping the app from scoring higher by not subscribing to it? ; or 2. Is the low rating the possible result of most of the current subscribers not getting alerts, and that others - who haven't (yet) subscribed to the app - are being lulled into a false sense of safety, even complacency? ; or, 3. Is the app a bit of a lame-duck technology - on the part of the government - and the app is not functioning properly or at all? ; or, 4. Are Albertans simply complacent about the pandemic? Go into any store which has clearly defined and labelled "shopping lanes" and other forms of signage, along with PA and public service announcements exhorting shoppers to abide by the store's rules and Alberta Health's guidelines, and you'll experience first-hand what I'm talking about. Indifference, obtuse behaviour, willful or blind ignorance, etc. ; or, finally (at least for now) 5. Is the media, which continues to feed us only what is "news worthy" to it (as it has done for nearly 3 generations), the real problem? If the app is not being kept in front of viewers or in the ears of listeners, is that the reason for the low rating? The media, along with government, controls the access to news. More often than not, it's the media doing this because "news worthy" really means that which attracts and is supported by the most lucrative advertising revenue streams. As CFCN says "All the news you need to know", which translates, "All the news we want you to hear". CBC, CTV, and the American networks on cable and satellite TV are all complicit in this. I'll stop now, since I've run out of time to continue. However, I must add that if the government is truly engaged in leading Albertans out of this tragedy, it will not alter, delete, expunge, rephrase, or in any other way, edit my comments because some of them have suggested government shortcomings. I'm keeping a copy of this for my own files and for posterity. Clayton Walls, Calgary June 11, 2020 @ 1300 h MDT<br> :date: __2020-06-11 21:00:38__

> I think the idea is great as long as it's executed properly however there seems to be a glitch with the app as it's used 33% of my battery so far today.<br> :date: __2020-06-04 03:45:04__

> I don't need data on to run it. And it doesn't drain my battery despite having Bluetooth on . So far so good<br> :date: __2020-05-23 03:41:32__

> Same as others have said, works fine, installed fine, just wish there was an on /off button for scanning. I can't turn my Bluetooth off because I wear a smartwatch, and I don't need the app when I'm not leaving my house or going anywhere that I will not be in contact with other people. It is a bit of a hindrance having to go in and out of settings all of the time to enable the app permissions, please just add a button to this app.<br> :date: __2020-05-23 00:18:05__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 3 reviews"/>
</p>

> It's irritating that it has a large notification on my screen all the time to note that it's running, rather than an icon, or the option to just run in the background without that. Worse, it drains my battery, using as much power as almost everything else I run combined. I'd like to use it, but this isn't feasible.<br> :date: __2020-08-27 01:11:47__

> Extreme battery usage on a Pixel 2. Want to keep it don't know what to do<br> :date: __2020-08-20 06:30:42__

> Please listen to everyone and make an on/off option. This only needs to be on when we go out in public and will just be an added step such as bringing a mask.<br> :date: __2020-08-11 05:33:38__

> It's neither good or bad. It just sits in the background. I can only assume it works.<br> :date: __2020-07-20 08:28:08__

> Only installing for long periods of exposure It seems to cause overheating with my phone. If I have the app installed (paused or unpaused) it seems to ramp up internal temps. Also, there should be an option to say you are at home, so you don't have to pause the app. The constant need to have BT on, even while at home, is annoying. I get why but it is frustrating.<br> :date: __2020-07-03 00:54:11__

> I uninstalled the ap due to high battery usage from the app.<br> :date: __2020-06-28 21:23:04__

> I'm sure this a great service to use. The only issue I have is having Bluetooth on all the time. It drained my battery by 60% in 10 hours while I was at work. I'm out in the community a lot, so I would need to keep it on for it to be useful.<br> :date: __2020-06-26 16:41:45__

> Had it for a whole 20 minutes, battery went from 100% to 90% Im all for tracking it, but the app is kinda pointless if my phone is dead and I cant get notifactions<br> :date: __2020-06-24 19:21:26__

> Battery killer, but worth running if you can. Please add support for Androids "COVID-19 exposure notifications"<br> :date: __2020-06-20 22:25:38__

> I would have really liked to use this to help out but my battery life is non-existent. I just got a new S10 and my battery died a little over halfway through the day. If they could somehow fix this app to turn off when you're not moving or something then maybe it wouldn't drain your battery so bad? No idea, but I had to uninstall it.<br> :date: __2020-06-17 03:36:59__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 2 reviews"/>
</p>

> It's an absolute battery drainer! The intentions are good and the existence of it is important but it's just killing my battery and my phone is brand new.<br> :date: __2020-08-25 04:21:04__

> The idea behind this is great. But the implementation eats battery like candy. And there's no way to temporarily turn it off. I'd love to be able to turn it off while I'm driving or when I'm backpacking in PLUZ areas no where near another human. So because my phone having battery is more important when I'm in the middle of no where I'm uninstalling.<br> :date: __2020-08-19 17:33:47__

> This things drains battery real quick<br> :date: __2020-07-26 18:48:34__

> Takes way too much battery life. 39% over 4 hours....<br> :date: __2020-07-08 22:16:47__

> Can't connect to car without uninstalling. Ridiculous as it intereferes with other bluetooth so how can I even use it. Can't use it if I need bluetooth.<br> :date: __2020-07-08 03:36:51__

> I barely go outside, so all it did was eat my battery throughout the day. Even if I went outside, I never got a notification from the app.<br> :date: __2020-07-04 11:08:43__

> This app is a terrible battery drain. I had to uninstall to keep battery more than a few hours.<br> :date: __2020-06-29 19:45:55__

> Anybody else have to uninstall this app cause it makes your phone glitchy and kills the battery?<br> :date: __2020-06-23 15:02:58__

> Doesn't stay active. Will disappear sporadically and you have to restart your phone to make it appear again. I've gone days before I realize it's gone again so what's the point?<br> :date: __2020-06-18 05:40:47__

> I want to understand why the app needs permission to location data when the app description says they don't collect it. Is there any reasonable explanation?<br> :date: __2020-06-18 03:54:44__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 1 reviews"/>
</p>

> HELP Honestly the app doesn't work at all for me. I hit "upload data" and it doesn't send a pin. This app has been sub-par but I still have it downloaded.<br> :date: __2020-09-12 12:48:12__

> First time code didn't work. Now stuck at that point. Should be option to resend a code.<br> :date: __2020-09-06 22:38:04__

> Absolute garbage. It doesn't stay active on your phone. I have to restart my phone when I'm out and about several times so absolutely no point. Doesn't work.<br> :date: __2020-09-03 15:30:42__

> Eats batter, very very badly. 45% battery usage over 2 hrs.<br> :date: __2020-08-17 00:03:46__

> Battery Drainer!!!! Wow does this app eat battery!! What good is it to trace and notify me if my battery is dead?<br> :date: __2020-08-14 22:40:40__

> Badly developed. Developer did not enter code correctly as several functions are not operational. Not sure where the mo ey went?<br> :date: __2020-08-09 15:46:36__

> I live in Alberta but my phone number is fron Mexico (starts with +52). Please add other phone number options because I can't use the app without having a +1 phone number and I don't have one. I'm sure I'm not the only one.<br> :date: __2020-08-09 00:27:14__

> The app hasn't been updated in six weeks, but it suddenly started draining my battery the past couple days. No explanation why that's happening now.<br> :date: __2020-08-07 00:26:58__

> Such a battery hog! The federal one doesn't need as much battery as this one. Fix it if you want more people to use it.<br> :date: __2020-08-05 23:55:05__

> Terrible app, can't even register.<br> :date: __2020-08-05 16:04:20__


