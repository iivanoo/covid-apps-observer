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

> Contact tracing using technology is an obvious and effective way to fight the covid-19 crisis. Well done!<br> :date: __2020-05-09 07:37:24__

> Thank you all for your service!!!<br> :date: __2020-05-09 00:57:11__

> I havent experienced any problems or crashings, during registration. So far, it is a good app! My only question is, how reliable is this app?<br> :date: __2020-05-08 06:02:30__

> The app runs in the background. For those worried about battery drainage, turn off Bluetooth when in your home. I hope this will help AHS deal with COVID19<br> :date: __2020-05-08 00:04:13__

> Easy to install and no noticeable battery drain ... thanks Alberta<br> :date: __2020-05-07 20:11:05__

> Great work getting it created quickly!<br> :date: __2020-05-07 05:20:38__

> Doesn't send the code,now works<br> :date: __2020-05-06 01:18:23__

> Good app. Doing my part to help feels good. Also the more people download this the better the app will work.<br> :date: __2020-05-04 21:36:13__

> Works as advertised.<br> :date: __2020-05-04 20:30:59__

> Works great, but why location? The whole point of the contact tracing API developed by Apple & Google was to facilitate contact tracing without the need for location access. Even from the app description: "The app uses Bluetooth to log contact with other individuals[...]" and "Geolocation data is not collected by the app or by [AHS]". SO WHY DO YOU NEED LOCATION? Please update explanation. Edit: Per AHS website & Android docs, location required for Bluetooth. Please update this in description.<br> :date: __2020-05-04 16:53:18__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 4 reviews"/>
</p>

> Overall, same as other reviews. Installs and runs smooth. The issue is the constant "on" state, with you needing to disable Bluetooth to effectively disable the battery draining searching for other Bluetooth devices. It would be nice to just have a button to click to enable when I leave the house. No need for it to be on when at home, but I'd like to use my headphones please. Thanks!!<br> :date: __2020-05-09 04:44:38__

> The daily power consumption is high. It never runs in the background. Hopefully the next release will reduce per consumption.<br> :date: __2020-05-08 21:57:57__

> Works as expected. Have not experienced issues with high battery usage. The app has used about 1% over the entire day while the phone is off the charger. Using a Samsung Galaxy S10. Data usage - it has used just under 1 MB in the 4 days installed. 4 stars because the app gives a constant notification that it is in use, but you can't swipe it away. I turned notifications off and will to turn them on when I am out. The app should have a badge system based on consecutive days stayed home!<br> :date: __2020-05-08 00:58:51__

> Easy to install. Would be better if it had a way to pause scanning when just at home.<br> :date: __2020-05-05 01:00:27__

> Obviously I haven't had to use the upload feature and haven't been contacted, so no comment on those features, but installation and verification went smoothly. It has been running issue free over a weekend.<br> :date: __2020-05-04 15:41:13__

> Had troubles getting the code at first, had to delay getting this set up by a day, but got it installed now so maybe they worked out some bugs. Won't really know if it's working unless I get an alert or something. More for their use than mine but I hope it works.<br> :date: __2020-05-04 14:14:38__

> It runs just fine in the background and doesn't seem to have any affect on battery<br> :date: __2020-05-04 04:14:09__

> So far, so good very little power drain on the cell. I like the privacy options. Especially the deletion of all my data at my request when this pandemic is over.<br> :date: __2020-05-03 20:03:18__

> Seems to be working fine. Was easy to set up. The only thing I dislike is that it keeps a notification open 24/7 when usually I make sure I've dealt with and gotten rid of all notifications. I'll get used to it, I'm sure.<br> :date: __2020-05-03 16:31:41__

> Downloaded fine / easy to set up. I'd like to see how many downloads have happened.<br> :date: __2020-05-03 15:57:03__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 3 reviews"/>
</p>

> No experience. Just hope it works, it will kill me if I get it with my health issues<br> :date: __2020-05-09 06:18:52__

> Used 50% if the battery on my S9 in half a day and I never left the house. Good idea but bad implementation. Uninstalled.<br> :date: __2020-05-08 23:50:50__

> Keeps resizing my phone wallpaper. Never had this issue till I downloaded this app.<br> :date: __2020-05-08 18:32:34__

> OK. But it should record any time you're within 2m of another. Not just waiting for 15 minutes. Only takes a second to catch the virus.<br> :date: __2020-05-08 00:15:20__

> Finally got it loaded. The app requires Android 8+ to run so I had to go to my play phone, Copy an image of TWRP to it, Copy an open source zip of Android 10 to it, copy a zip of Opengapps to it, flash the recovery with TWRP, use TWRP recovery to wipe the phone and flash Android 10 and the basic Google apps, then configure the phone and install the app. I took two days to plan it rather than risk bricking the phone. Could they simply have ported to more revisions of Android?<br> :date: __2020-05-07 03:51:29__

> Constantly trying to pair with my laptop even when it's already paired and connected via Bluetooth.<br> :date: __2020-05-06 16:46:32__

> What is the point if IPhone users can't run their version of the app in the background. No IPhone user is going to have the app running in the foreground with their screen on. Because of the sheer volume of iPhone users this makes the android app pointless.<br> :date: __2020-05-06 13:09:07__

> I don't like the notification that has to be present at all times but oh well. My main complaint is that this app needs to be compatible with older model smartphones. My mother is older and has an older phone as I'm sure many older people do. She now can't use this app even though seniors are the most at risk.<br> :date: __2020-05-05 23:04:32__

> Had to get code four times because, even though I entered the correct number, it told me either the number was wrong or did nothing at all. Had to press other keys multiple times to get it to advance. Annoying. Hope it works better than the set up.<br> :date: __2020-05-05 03:06:42__

> Just downloaded it last night, so no valid remarks yet. I'll update when I have something useful to say.<br> :date: __2020-05-04 22:26:36__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 2 reviews"/>
</p>

> Good intentions, but battery hog! This thing is a background app, so why does it use the most battery of any app? It sucks up 150% of the battery compared to apps I do actively use a lot! Dead phones don't trace -- they'll need to address this in order to get people on board.<br> :date: __2020-05-09 22:03:36__

> Worked for a few days now won't let me upload. No one sends a text either.<br> :date: __2020-05-09 00:22:08__

> Couldn't install in my Android 6.0 phone.<br> :date: __2020-05-08 23:38:53__

> Great idea but the app eats battery life to the point where I need to charge in the middle of the day. I got a message regarding my phone needing to shut down software that vanished once I deleted the app. I want to use the app but it just requires to many resources.<br> :date: __2020-05-08 01:48:17__

> Easy to install. However drained my battery in a very short time. Fully charged in the morning down to 15% just before noon. Not practical.<br> :date: __2020-05-08 01:43:14__

> I wanted to continue using this app, but unfortunately it eats up too much of my battery- the first day that I had it installed, my phone died after only a few hours with hardly using my phone and settings showed it was majorly consuming power. Had to uninstall!<br> :date: __2020-05-07 14:02:19__

> Not everyone here has a N.A. area code...<br> :date: __2020-05-06 10:40:58__

> No off switch for when you are staying home. High battery usage.<br> :date: __2020-05-06 01:50:10__

> Having an issue where it seems to constantly trigger my laptop to try and pair with it. My phone beeps every couple of minutes and no way to prevent it short of killing the app (or switching off bluetooth). If the devs want to contact me to find out what's happening feel free.<br> :date: __2020-05-06 00:17:53__

> Yes it probably tracks you to see if you have come into contact with someone sick. But drains your phone battery.<br> :date: __2020-05-05 23:50:23__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="ca.albertahealthservices.contacttracing 1 reviews"/>
</p>

> Read other reviews, including comments re battery drain. Installed app at about 11.00 am with about 90% battery. By 11.00 pm, down to 15%. About to uninstall.<br> :date: __2020-05-10 08:18:29__

> Drained my battery! Downloaded the app yesterday, woke up & my phone was dead. For functionality of Covid-19 tracing, don't we need an app that won't kill off our battery so we can be reached?<br> :date: __2020-05-09 14:08:50__

> Despite claiming that it doesn't recited your location it requires your location to work.<br> :date: __2020-05-09 10:15:14__

> Eats your battery and interferes with other apps on my phone that worked perfectly fine before I installed. I have no problem with the info being shared. Just wish it wasn't such a phone killer<br> :date: __2020-05-09 04:50:08__

> Installed the app on two different S8 phones but had to remove because of excessive battery use. Would kill the battery overnight. Battery usage showed between 40% and 70%. This has to be fixed before I will reinstall.<br> :date: __2020-05-09 00:17:55__

> Battery hog! While the app has good intentions it is a major battery hog. Uninstalling it.<br> :date: __2020-05-08 23:15:09__

> Public health is important so an app like this could really help, but having it use Bluetooth drains peoples batteries quickly and the constant notification is very annoying. There are also privacy concerns of course<br> :date: __2020-05-08 20:19:40__

> Keeps saying "something went wrong try again"<br> :date: __2020-05-08 10:31:31__

> Cant even put my cell number in. It's a 403 number, so I cant even get in to the app<br> :date: __2020-05-08 07:01:07__

> Won't accept valid phone number<br> :date: __2020-05-08 06:50:52__


