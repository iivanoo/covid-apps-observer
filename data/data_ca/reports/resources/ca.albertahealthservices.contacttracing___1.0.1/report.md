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

> Works well on my pixel 3. No issues.<br> :date: __2020-05-16 02:32:19__

> Will not send 6 digit code.<br> :date: __2020-05-15 03:08:34__

> Running on a Huawei P30 Lite with Android 9 patched to latest. App runs fine and I don't notice any battery drain issues. However, I find that the app self-terminates regularly. I see this when I wake the phone up without entering the password - the status screen shows that the app is running or not. Starting it up is easy - just go to the apps page and start the app again. It's good for anywhere from 1 to 3 days before it dies again. This app seems to strike a decent balance between privacy and usefulness.<br> :date: __2020-05-13 00:57:07__

> Battery drain bluetooth issue fix: you do NOT have to disable bluetooth to disable the app, although this is the easiest and fastest method. The other method is to disable location permissions for the app under apps & notifications tab in phone's settings. This disables the ability for the app to use bluetooth. Another method would be to uninstall the app altogether lol<br> :date: __2020-05-13 00:11:47__

> App seems to do what it's designed for. Battery drain doesn't seem an issue on my 2+ year old Galaxy S9. So far today, my phone has been on for 3 hours, the app has been active for less than one minute and running in the background the rest of the time, using 0.2% of my battery in that time, according to my battery stats. Battery usage is negligible. People are going to complain about anything, but this app doesn't seem to deserve the criticism it is getting.<br> :date: __2020-05-12 18:44:35__

> Same experience as others. Installed smoothly on my Android 10 device. Report shows that it has used 3% of my battery over the last 3 days.<br> :date: __2020-05-11 15:27:53__

> Thank you, thank you, thank you! Anything to help keep better tabs on the spread and potential exposure is great.<br> :date: __2020-05-11 00:29:38__

> Contact tracing using technology is an obvious and effective way to fight the covid-19 crisis. Well done!<br> :date: __2020-05-09 07:37:24__

> Thank you all for your service!!!<br> :date: __2020-05-09 00:57:11__

> I havent experienced any problems or crashings, during registration. So far, it is a good app! My only question is, how reliable is this app?<br> :date: __2020-05-08 06:02:30__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 4 reviews"/>
</p>

> Won't know if it works till it's needed. Hopefully never. Always has a 1 superimposed on the icon, but nothing apparent when I open the app.<br> :date: __2020-05-15 20:40:40__

> I was totally surprised on how much this app draws dowm my battery , worse than f-cebook app, will be definitely removed once things cool down ...<br> :date: __2020-05-15 00:48:59__

> Good app and hopefully it gets installed and used more. Like others are saying, it needs and off button because of the battery drain when using it at home. Most people are at home now so this should be a feature available....<br> :date: __2020-05-12 17:49:39__

> Installed easily and seems to work fine.<br> :date: __2020-05-12 00:44:52__

> No problems, but also I don't get any feedback about whether I'm near another person with the app, so I can't verify whether it's actually doing anything.<br> :date: __2020-05-11 18:46:13__

> Works as advertised, used 0% to 1% of battery daily. A must have with the reopening strategy as it will make it easier to stop a second wave and stop the spread. Smart way to prevent a second closure....<br> :date: __2020-05-11 07:36:00__

> Overall, same as other reviews. Installs and runs smooth. The issue is the constant "on" state, with you needing to disable Bluetooth to effectively disable the battery draining searching for other Bluetooth devices. It would be nice to just have a button to click to enable when I leave the house. No need for it to be on when at home, but I'd like to use my headphones please. Thanks!!<br> :date: __2020-05-09 04:44:38__

> The daily power consumption is high. It never runs in the background. Hopefully the next release will reduce per consumption.<br> :date: __2020-05-08 21:57:57__

> Works as expected. Have not experienced issues with high battery usage. The app has used about 1% over the entire day while the phone is off the charger. Using a Samsung Galaxy S10. Data usage - it has used just under 1 MB in the 4 days installed. 4 stars because the app gives a constant notification that it is in use, but you can't swipe it away. I turned notifications off and will to turn them on when I am out. The app should have a badge system based on consecutive days stayed home!<br> :date: __2020-05-08 00:58:51__

> Easy to install. Would be better if it had a way to pause scanning when just at home.<br> :date: __2020-05-05 01:00:27__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 3 reviews"/>
</p>

> Battery consuption is way too high. Currently 13% on a day when I was only out of my house 1 hour. App needs to detect home WiFi and stop scanning unless it detects no wifi. It is the third largest app draining my battery. Not acceptable. May have to discontinue use.<br> :date: __2020-05-17 06:56:45__

> I haven't noticed any drastic battery drain on my device yet but as others mentioned the app should be able to be turned off as 95% of my time is spent in my own home. People are more likely to use the app if they don't feel that they don't need it 95% of the time but rather have the option for the 5% of the time it could be helpful.<br> :date: __2020-05-13 16:32:13__

> It's fine but battery draining lately. Seemed to run pretty efficiently in the background at the start but I'm charging my phone 3 times a day now.<br> :date: __2020-05-11 06:52:48__

> Please add an "off" button. I shouldn't have to keep the app running while I'm sleeping or just sitting at home. Turning off bluetooth is not an "off" button since this app isn't the only thing that people use bluetooth for. I don't mind the battery drain since it's a useful app and I think the battery drain, when I want to use the app, is worth it. Would rate 5 stars if you had an off button.<br> :date: __2020-05-10 22:42:27__

> No experience. Just hope it works, it will kill me if I get it with my health issues<br> :date: __2020-05-09 06:18:52__

> Used 50% if the battery on my S9 in half a day and I never left the house. Good idea but bad implementation. Uninstalled.<br> :date: __2020-05-08 23:50:50__

> Keeps resizing my phone wallpaper. Never had this issue till I downloaded this app.<br> :date: __2020-05-08 18:32:34__

> OK. But it should record any time you're within 2m of another. Not just waiting for 15 minutes. Only takes a second to catch the virus.<br> :date: __2020-05-08 00:15:20__

> Finally got it loaded. The app requires Android 8+ to run so I had to go to my play phone, Copy an image of TWRP to it, Copy an open source zip of Android 10 to it, copy a zip of Opengapps to it, flash the recovery with TWRP, use TWRP recovery to wipe the phone and flash Android 10 and the basic Google apps, then configure the phone and install the app. I took two days to plan it rather than risk bricking the phone. Could they simply have ported to more revisions of Android?<br> :date: __2020-05-07 03:51:29__

> Constantly trying to pair with my laptop even when it's already paired and connected via Bluetooth.<br> :date: __2020-05-06 16:46:32__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 2 reviews"/>
</p>

> I've had this app installed for a few weeks, this weekend I noticed battery usage of 13.3% in two hours. I did a phone reboot, recharged and tested again. Battery use at 15% for this application, I have removed the app until this issue can be resolved.<br> :date: __2020-05-10 19:00:10__

> Good intentions, but battery hog! This thing is a background app, so why does it use the most battery of any app? It sucks up 150% of the battery compared to apps I do actively use a lot! Dead phones don't trace -- they'll need to address this in order to get people on board.<br> :date: __2020-05-09 22:03:36__

> Worked for a few days now won't let me upload. No one sends a text either.<br> :date: __2020-05-09 00:22:08__

> Couldn't install in my Android 6.0 phone.<br> :date: __2020-05-08 23:38:53__

> Great idea but the app eats battery life to the point where I need to charge in the middle of the day. I got a message regarding my phone needing to shut down software that vanished once I deleted the app. I want to use the app but it just requires to many resources.<br> :date: __2020-05-08 01:48:17__

> Easy to install. However drained my battery in a very short time. Fully charged in the morning down to 15% just before noon. Not practical.<br> :date: __2020-05-08 01:43:14__

> I wanted to continue using this app, but unfortunately it eats up too much of my battery- the first day that I had it installed, my phone died after only a few hours with hardly using my phone and settings showed it was majorly consuming power. Had to uninstall!<br> :date: __2020-05-07 14:02:19__

> Not everyone here has a N.A. area code...<br> :date: __2020-05-06 10:40:58__

> No off switch for when you are staying home. High battery usage.<br> :date: __2020-05-06 01:50:10__

> Having an issue where it seems to constantly trigger my laptop to try and pair with it. My phone beeps every couple of minutes and no way to prevent it short of killing the app (or switching off bluetooth). If the devs want to contact me to find out what's happening feel free.<br> :date: __2020-05-06 00:17:53__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 1 reviews"/>
</p>

> I deal with the public all day so I thought the idea behind the app was great. Knowing you could reach out to anyone I had steady contact with if I ever got sick gave me peace of mind. However, it drains my battery so quickly that I have since deleted the app. I can't have a phone that won't work when I need it to because my battery has died.<br> :date: __2020-05-16 20:04:56__

> Installed without activating the app. After giving it some thought I uninstalled it. I do not trust the current Wildrose Party aka UCP government with unlimited data access. It's easy to see by the number of installs how many Albertans feels the same as I do. I will stay with the simple Federal government app for reporting daily conditions. No name, phone number required. Location only.<br> :date: __2020-05-16 16:22:48__

> Kills your battery<br> :date: __2020-05-15 05:05:17__

> Used 29% of my battery today, while it was in airplane mode. This needs to be fixed before I'll download it again.<br> :date: __2020-05-14 22:15:27__

> 2 weeks and only 10,000 downloads. Seems like a waste if you can't get more people on board.<br> :date: __2020-05-14 05:22:08__

> Kills your battery like your mom does to a piece of cake. 4 hours from full charge, and my phone is almost dead. Useless<br> :date: __2020-05-13 16:55:29__

> Will download app if battery drain issues are solved. I use Bluetooth in my home so disabling Bluetooth isn't an option for me<br> :date: __2020-05-12 22:04:33__

> Do I trust the Utterly Corrupt Party government with information about my every movement? Absolutely not. If they really want to make a difference against COVID they can allow the user to control the data. DO NOT RECOMMEND!<br> :date: __2020-05-12 15:46:49__

> It was chewing through my battery life. Will come back in 30 days once improved.<br> :date: __2020-05-12 00:37:30__

> I dont find any useful this app.. draining battery alot... Disconnect many time.. in day...<br> :date: __2020-05-11 00:28:27__


