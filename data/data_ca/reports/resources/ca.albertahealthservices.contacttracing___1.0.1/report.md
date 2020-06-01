# ABTraceTogether
App version ``1.0.1``

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
| **Latest version** | 1.0.1 |
| **Last update** | 2020-05-08 00:24:36 |
| **Recent changes** | We’re always updating the ABTraceTogether App to be the best tracing tool.<br><br>We love customer feedback! If you have any thoughts, ideas or feedback to share, please contact us at ABTraceTogetherSupport@gov.ab.ca<br><br>This version includes:<br>- Enhanced upload data flow to help ensure data logs are only uploaded when a user is contacted by a contact tracer<br>- Minor UI enhancements<br>- Updates to avoid users experiencing crashes during registration |
| **Installs**  | 10,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 30, 2020 |
| **Size**  | 9.7M |
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

The ABTraceTogether app has been installed by more than **10000** times. At this time, **320** rated the app and its average score is **3.3**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 134

:star::star::star::star:: 32

:star::star::star:: 28

:star::star:: 44

:star:: 80

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 5 reviews"/>
</p>

> Very " nice " Thanks !!<br> :date: __2020-05-26 04:25:34__

> Installed & activated on Samsung S9 without any issues. Runs fine. There is extra battery usage, but it's tolerable for me.<br> :date: __2020-05-25 03:53:49__

> Amazing app, feels so good to know the government knows all. I cannot wait for the vaccine. Please increase my taxes and fund more the media.<br> :date: __2020-05-25 03:45:04__

> Easy to install. Not noticing any power drain and analysis agrees. Bluetooth speaker works fine at same time. Reminds me to turn bluetooth back on when I shut off for a phone call not to be via my bluetooth speaker.<br> :date: __2020-05-24 18:39:00__

> Great idea except for the power usage. The only way to stop is is to go into the app's app setting and "force stop" it to turn it off when I'm at home. It's easy enough to turn it back on again by tapping the app icon. But this is a hassle.You should be able to just pin it and minimize it when you need it to run in the background, and close it when your at home.<br> :date: __2020-05-24 10:44:48__

> Does it work in Ontario too??<br> :date: __2020-05-23 14:18:59__

> Seems to be working. If you don't drink the kool-aid, and stay away from Apple this works just fine. I have not even noticed any battery drain on my Android phone.<br> :date: __2020-05-23 02:12:06__

> Have downloaded this on both my mom's and my phone (Samsungs), and haven't had any problems. It only asks for bluetooth to be turned on and for you to enter a phone number to contact you should you encounter someone who later tests positive.<br> :date: __2020-05-23 02:11:24__

> Unlike others here, my experience is that this app's battery usage on my S9 is very minimal. That is with Bluetooth always being on. I suspect that some people are misreading their battery usage. The problem with having a manual on/off switch is that you will forget to turn the app back on when you go out. My only criticism is that Alberta has not done enough to encourage the public to use this app. As of this writing, there have been only 50,000 downloads.<br> :date: __2020-05-22 18:24:21__

> Battery drainage not an issue for me, everything works fine. (Galaxy S9)<br> :date: __2020-05-17 21:23:06__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 4 reviews"/>
</p>

> I don't need data on to run it. And it doesn't drain my battery despite having Bluetooth on . So far so good<br> :date: __2020-05-23 03:41:32__

> Same as others have said, works fine, installed fine, just wish there was an on /off button for scanning. I can't turn my Bluetooth off because I wear a smartwatch, and I don't need the app when I'm not leaving my house or going anywhere that I will not be in contact with other people. It is a bit of a hindrance having to go in and out of settings all of the time to enable the app permissions, please just add a button to this app.<br> :date: __2020-05-23 00:18:05__

> Won't know if it works till it's needed. Hopefully never. Always has a 1 superimposed on the icon, but nothing apparent when I open the app.<br> :date: __2020-05-15 20:40:40__

> I was totally surprised on how much this app draws dowm my battery , worse than f-cebook app, will be definitely removed once things cool down ...<br> :date: __2020-05-15 00:48:59__

> Good app and hopefully it gets installed and used more. Like others are saying, it needs and off button because of the battery drain when using it at home. Most people are at home now so this should be a feature available....<br> :date: __2020-05-12 17:49:39__

> Installed easily and seems to work fine.<br> :date: __2020-05-12 00:44:52__

> No problems, but also I don't get any feedback about whether I'm near another person with the app, so I can't verify whether it's actually doing anything.<br> :date: __2020-05-11 18:46:13__

> Works as advertised, used 0% to 1% of battery daily. A must have with the reopening strategy as it will make it easier to stop a second wave and stop the spread. Smart way to prevent a second closure....<br> :date: __2020-05-11 07:36:00__

> Overall, same as other reviews. Installs and runs smooth. The issue is the constant "on" state, with you needing to disable Bluetooth to effectively disable the battery draining searching for other Bluetooth devices. It would be nice to just have a button to click to enable when I leave the house. No need for it to be on when at home, but I'd like to use my headphones please. Thanks!!<br> :date: __2020-05-09 04:44:38__

> The daily power consumption is high. It never runs in the background. Hopefully the next release will reduce per consumption.<br> :date: __2020-05-08 21:57:57__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 3 reviews"/>
</p>

> Great idea but this draining if my battery!! Very frustrating 😡<br> :date: __2020-05-31 22:18:36__

> The first few weeks it was great all around. Last couple of days it has been draining my battery. I've always turned Bluetooth off at home, and on for the occasions I leave the house. It's jumped from 2%, 27%, 48% of battery use! I had to force stop it after Bluetooth off failed to curb its battery appetite.<br> :date: __2020-05-26 05:00:05__

> It works fine But has sliced my battery life pretty much in half. The app is useless if my phone is dead<br> :date: __2020-05-26 03:30:16__

> I experienced many of the listed faults to this app. Installed as I could understand the advantages and think it's important to help the greater good. However, the battery drainage on my phone will be the reason i uninstall. Would love to reinstall once this is fixed.<br> :date: __2020-05-26 01:29:38__

> My friend Brian hates this app<br> :date: __2020-05-24 20:51:52__

> Draining my battery. Did not seem to start until about 1 week after installing it. Sadly had to uninstall.<br> :date: __2020-05-18 07:52:49__

> Battery consuption is way too high. Currently 13% on a day when I was only out of my house 1 hour. App needs to detect home WiFi and stop scanning unless it detects no wifi. It is the third largest app draining my battery. Not acceptable. May have to discontinue use.<br> :date: __2020-05-17 06:56:45__

> I haven't noticed any drastic battery drain on my device yet but as others mentioned the app should be able to be turned off as 95% of my time is spent in my own home. People are more likely to use the app if they don't feel that they don't need it 95% of the time but rather have the option for the 5% of the time it could be helpful.<br> :date: __2020-05-13 16:32:13__

> It's fine but battery draining lately. Seemed to run pretty efficiently in the background at the start but I'm charging my phone 3 times a day now.<br> :date: __2020-05-11 06:52:48__

> Please add an "off" button. I shouldn't have to keep the app running while I'm sleeping or just sitting at home. Turning off bluetooth is not an "off" button since this app isn't the only thing that people use bluetooth for. I don't mind the battery drain since it's a useful app and I think the battery drain, when I want to use the app, is worth it. Would rate 5 stars if you had an off button.<br> :date: __2020-05-10 22:42:27__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 2 reviews"/>
</p>

> It was fine until 3 days ago when it went from draining 1% of my battery to >80%. Can't track anything if my phone is dead by 9am. I had to uninstall until this is fixed.<br> :date: __2020-05-31 02:36:09__

> I installed this app, however it was causing issues with some of my other apps and they would not load so I had to uninstall. Once I uninstalled everything else worked fine. Unfortunately the app is not going to be very effective unless more people use it and with all the issues people are having with it fewer people will be using it. I hope you are able to find a solution to those issues and relaunch an app that will be effective. I may consider reinstalling after it is fixed.<br> :date: __2020-05-29 22:39:00__

> Had to uninstall, this app is a battery eater.<br> :date: __2020-05-25 01:17:19__

> Was running fine for the first couple of weeks but in the past 2-3 days battery consumption has become intolerable.<br> :date: __2020-05-21 03:37:20__

> I downloaded it on my android phone and it worked okay, but the battery drain is horrible as noted by lots of other users. I was also irritated that despite the fact that they say it only uses bluetooth, location services had to be enabled as well or it wont work. Uninstalled it.<br> :date: __2020-05-20 13:44:22__

> Destroys your battery. I now have to charge my battery 3 times a day because of this app. It's insane how much battery it uses.<br> :date: __2020-05-19 07:57:16__

> I've had this app installed for a few weeks, this weekend I noticed battery usage of 13.3% in two hours. I did a phone reboot, recharged and tested again. Battery use at 15% for this application, I have removed the app until this issue can be resolved.<br> :date: __2020-05-10 19:00:10__

> Good intentions, but battery hog! This thing is a background app, so why does it use the most battery of any app? It sucks up 150% of the battery compared to apps I do actively use a lot! Dead phones don't trace -- they'll need to address this in order to get people on board.<br> :date: __2020-05-09 22:03:36__

> Worked for a few days now won't let me upload. No one sends a text either.<br> :date: __2020-05-09 00:22:08__

> Couldn't install in my Android 6.0 phone.<br> :date: __2020-05-08 23:38:53__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 1 reviews"/>
</p>

> Great idea - but drains your battery very quickly - constantly trying bluetooth for others... once app installed and setup - battery life averaged 4-5 hours - close to 2 days without the app...<br> :date: __2020-06-01 04:32:54__

> So I don't download a lot of new apps onto my phone and I did add this one and made a good review of IT thinking that it was a great thing to have and I do still think that but here's the problem it screwed my phone up I was lagging freezing my phone would restart it's a good concept guys but you need to fix it because I took it off I need my phone I can't have it glitching like that. Sorry<br> :date: __2020-05-31 05:10:18__

> total piece of garbage! not only does it NOT work, it violates your privacy! this is sad when there is a known working solution available<br> :date: __2020-05-29 18:20:37__

> I enter my phone number and it keeps saying something went wrong. So I can't even use the damn thing<br> :date: __2020-05-28 17:52:50__

> Completely useless<br> :date: __2020-05-25 08:10:11__

> Totally drained batter every day!<br> :date: __2020-05-25 04:16:05__

> Was excited for the app, until i find out it only records ppl in contact longer than 15min. Thats bs and useless, it takes less than 15seconds to infect someone. Uninstalled, thx. With so few people downloading this app, having this on my phone is a joke.<br> :date: __2020-05-24 10:18:29__

> It is utilizing too much battery (39.5%) which is causing me to have to plug in my phone every 4 to 6 hours.<br> :date: __2020-05-23 02:00:50__

> As so many others are reporting on social media, I tried multiple times but no code was sent to my number. Update: Tried again and it worked, but uninstalled it after it had an undismissable notification when I turned off my Bluetooth when I got home and then stopped working when I turned off push notifications so it would stop doing that. Clunky design.<br> :date: __2020-05-22 04:05:47__

> One rating is for the attempt.<br> :date: __2020-05-22 02:08:48__


