# NHS COVID-19
App version ``4.1.1 (124)``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="NHS COVID-19 icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | NHS COVID-19 |
| **Unique identifier** | uk.nhs.covid19.production |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=uk.nhs.covid19.production](https://play.google.com/store/apps/details?id=uk.nhs.covid19.production) |
| **Summary**  | Protect your loved ones with the NHS contact tracing app for England and Wales. |
| **Privacy policy** | [https://covid19.nhs.uk/our-policies.html](https://covid19.nhs.uk/our-policies.html) |
| **Latest version** | 4.1.1 (124) |
| **Last update** | 2020-12-18 15:54:37 |
| **Recent changes** | Bug Fixes. |
| **Installs**  | 5,000,000+ |
| **Category** | Medical |
| **First release** | Aug 12, 2020 |
| **Size**  | 8.2M |
| **Supported Android version**  | 6.0 and up |

### Description
> The NHS COVID-19 app is the official contact tracing app for England and Wales. 
<br>It is the fastest way of knowing when you’re at risk from coronavirus. The quicker you know, the quicker you can alert your loved ones, and your community. 
<br>The more of us that use it, the better we can control coronavirus. 
<br>The app runs on proven software developed by Apple and Google, designed so that nobody will know who or where you are. And you can delete your data, or the app, at any time.
<br>It has a number of features: 
<br>Trace: Find out when you’ve been near other app users who have tested positive for coronavirus
<br>Alert: Lets you know the level of coronavirus risk in your postcode district. 
<br>Check-in: Use our simple QR code scanner to check-in to venues like bars and restaurants. You will get alerted if you have visited a venue where you may have come into contact with coronavirus.
<br>Symptoms: Check if you have coronavirus symptoms and see if you need to order a test. 
<br>Test: Helps you order a test if you need to.
<br>Isolate: Keep track of your self-isolation countdown and access relevant advice.
<br>Available in English, Welsh, Arabic (Modern Standard), Bengali, Chinese (Simplified), Gujarati, Polish, Punjabi (Gurmukhi script), Romanian, Somali, Turkish and Urdu.
<br>The app can be used across UK borders in England, Wales, Scotland, Northern Ireland, Jersey and Gibraltar, detecting all relevant contact tracing app users (regardless of them using different official apps), alerting them if they have been in contact with coronavirus. 
<br>The app has been built in collaboration with some of the most innovative organisations in the world. We have worked with medical experts, privacy groups, at-risk communities and we’ve shared knowledge with the teams working on similar apps in many countries.
<br>Protect your loved ones. Please download the app. 
<br>The App is CE marked as a class I medical device in the United Kingdom and developed in compliance with European Commission Directive 93/42/EEC for class I devices.


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
| **Developer**  | Department of Health and Social Care |
| **Website**  | [https://covid19.nhs.uk/](https://covid19.nhs.uk/) |
| **Email** | NHSCovid-19AppStoreSupport@nhsbsa.nhs.uk |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Department+of+Health+and+Social+Care](https://play.google.com/store/apps/developer?id=Department+of+Health+and+Social+Care) |

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
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>CAMERA** | :warning:**Dangerous** | Required to be able to access the camera device. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | ietf.org | IETF Trust | :us: US | 1995-03-11 05:00:00 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | apache.org | The Apache Software Foundation | :us: US | 1995-04-11 04:00:00 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address ' returned no addresses for  ; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Code execution**
> - This application loads a native library<br>
> - This application loads a native library: 'Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The NHS COVID-19 app has been installed by more than **5000000** times. At this time, **95001** rated the app and its average score is **3.9574847**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 56378

:star::star::star::star:: 12680

:star::star::star:: 6932

:star::star:: 3550

:star:: 15461

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 5 reviews"/>
</p>

> Good<br> :date: __2020-12-27 06:25:39__

> Alerted me correctly<br> :date: __2020-12-27 00:31:30__

> Easy to use<br> :date: __2020-12-26 21:15:45__

> Good<br> :date: __2020-12-26 18:00:57__

> Very Helpful!<br> :date: __2020-12-26 14:05:37__

> Boris my g go on my guy<br> :date: __2020-12-26 13:48:50__

> fantastic app<br> :date: __2020-12-26 13:47:49__

> It is old new we are in tier 4 now<br> :date: __2020-12-26 05:02:31__

> 🏴<br> :date: __2020-12-25 21:44:18__

> A great and fast way to check into places to keep your self and others safe. It also provides basic information about the virus and rules.<br> :date: __2020-12-25 20:20:18__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 4 reviews"/>
</p>

> Easy to install and use .<br> :date: __2020-12-27 16:13:40__

> The app didn't really seem to have much stuff on it other than just telling people what tier in the UK they're areas are in. Did uninstall after. I also don't see the point for it having to use Bluetooth for it to work, it just doesn't make any sense at all, like it's not like it has to connect to some physical device or something.<br> :date: __2020-12-27 03:24:12__

> It has worked fine for me so far. Very useful for checking my local restrictions. I have never booked a test or been told to self isolate via this app so I cannot comment on those features. However, from what I have experienced, an all round good app. It will become more effective the more people install it.<br> :date: __2020-12-26 21:56:13__

> Nice place to take a brake, with excellent coffee, fine space, enough for current situation.<br> :date: __2020-12-26 13:47:12__

> Is now up dating, thank you for fixing this.<br> :date: __2020-12-26 09:41:27__

> Quick response detects problems<br> :date: __2020-12-26 09:31:09__

> Not helpful yet, can't see an option to log LFDT result.<br> :date: __2020-12-24 23:07:33__

> The app seems to be fine, however, the message received mentioning that one may have been exposed to someone with covid and to self isolate seems to disappear very quickly from the screen and cannot be read again. Could not your team work on a text message being sent too so the person is informed via app and text message ? I could not re-read the message on the app as unfortunately, it went off the screen very fast..<br> :date: __2020-12-24 11:48:08__

> I think that it's a good idea but my app keeps giving me a notification that all it says is loading.??<br> :date: __2020-12-24 07:35:34__

> Good app, bit buggy regarding notifications but overall useful.<br> :date: __2020-12-23 15:59:37__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 3 reviews"/>
</p>

> Well it works and probably works well because today I had a notification to isolate .... heres where the app fails though. I came into contact with an infected person on the 20th December. Todays date is the 27th December and I now only have to isolate for 4 days. So thats potentially 6 days infecting ppl assuming I'm asymptomatic or my symptoms haven't come out yet. I assume, I may be wrong that the person I had the dangerous encounter with only got tested a couple of days ago and result today?<br> :date: __2020-12-27 20:46:17__

> The app has suddenly started to say it is loading and says it has a message. But the loading never finishes and there is nothing listed in the app. I think this occurred after the app updated to 4.1.1(124). There is only the remotest chance that this might be a genuine alert but why would it disappear if it was and how will I tell if any future notification is a real alert not a bug.<br> :date: __2020-12-27 11:36:36__

> Saying Wales in tier 4, but we are in level 4. No tiers in Wales. Shows high when we were low but neighbouring town 10 miles away is high. Could be so much more informative<br> :date: __2020-12-27 07:37:01__

> Uninstalled since Bluetooth made compulsory. I'm not going to allow an app to put me into quarantine just because I happen to pass someone in the street who later tests positive for COVID<br> :date: __2020-12-26 10:57:44__

> I know we are tier 4 but my app sais tier 2. Maybe where we live is tier 2 which doesn't make sense as my country and borough is tier 4 as are surrounding areas. Not so much the app but the tier system but so confusing better to just lockdown and be done but as it stands I am tier 2 in a tier 4 area so guess I'm kinda lucky.<br> :date: __2020-12-26 07:11:11__

> Constantly getting false alerts!<br> :date: __2020-12-25 11:59:53__

> Appears to work... I guess, but I had a thought! I remember reading somewhere that "people don't care about contact tracing", with regards to being called by contact tracers. But surely this is down to people not wishing to answer their phones to unknown callers? So here's a thought... Could you not tell the country what the phone number you will be called from is or when people install this app, make it so that it also creates a contact tracing contact on the phone?<br> :date: __2020-12-25 08:48:24__

> Improving<br> :date: __2020-12-24 22:06:10__

> Latest update not launching on my android 11 device<br> :date: __2020-12-24 14:24:40__

> dies not automatically update<br> :date: __2020-12-24 09:53:08__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 2 reviews"/>
</p>

> Told me to self isolate 2 days later than it was suposed to. But 2 days previous when i was supposed to have come in contact with a person testing positive, I was at home and no one had left the house in the 3 days previous . App was fine until the tier4 update<br> :date: __2020-12-28 08:32:50__

> It doesn't seem to work properly in the background. I'm not sure what does this (maybe an update) but it hasn't notified (without opening the app) to isolate. I've also gotten the impression that it's updated and lost settings. I'm not confident that this app works properly. Also, a friend in Wales says it links to the English rules!<br> :date: __2020-12-28 00:05:50__

> Gave me the "you have been contact with someone who tested positive," late Christmas day. Oh I've got the family here, yet not one got a message and still haven't. Couldn't work out what when or why I got the message. I know you won't identify name or venue BUT why not firm date and rough location?? 100% I've not been next to anyone for 15 minute nor 10 nor 5. I've hardly been out, always worn a mask kept 2m from people. Family xmas seems to be 2 or 3 days after the alleged contact, frustrated.<br> :date: __2020-12-27 10:12:39__

> Does not recognise NHS rapid test center bar code, on entering the Wolverhampton civic center would not register<br> :date: __2020-12-27 08:54:49__

> I'm in teir 4 but the app says I'm in teir 2.<br> :date: __2020-12-26 12:57:15__

> It is 7am on Boxing Day. The press told me that I would be in Tier 3. This app tells me that I am in Tier 2. This is ridiculous from an app such as this. I am now considering deleting the app now. Now at 8am it is correct. Pretty lame that this official app is delayed like this.<br> :date: __2020-12-26 09:20:50__

> Tier level not updated despite Cambridge moving from tier 2 to 4. Pretty basic requirement!!<br> :date: __2020-12-26 08:13:34__

> The app is inaccurate. It has not updated my area to the correct tier more than 6 hours after the change came into force. In areas of poor internet connectivity it is not possible to use the scanner for checking into a venue. You will still need to use the paper system.<br> :date: __2020-12-26 07:50:43__

> Good and bad stuff bout it So....good stuff. 1. It said what tier im in and i didnt know i was in tier 3<br> :date: __2020-12-26 06:55:19__

> Late notification, strange isolating periods and no trace call or any follow up<br> :date: __2020-12-25 15:26:15__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 1 reviews"/>
</p>

> Notification for no reason!<br> :date: __2020-12-28 11:47:17__

> Contact tracing doesn't work. I've been in close proximity to my other half who tested positive for covid and the app never gave me a notification. Battery life has taken a significant hit since installing. I only use the app to quick check my tier and rules now, will probably uninstall as I can use the .gov for this without the battery hit.<br> :date: __2020-12-28 07:55:20__

> No point as covid is a government lie for a cover up<br> :date: __2020-12-28 00:13:10__

> Have been in contact with potential covid cases and not 1 notification.. Just a bonus there are some honest people about<br> :date: __2020-12-27 23:56:17__

> A really bad app, I know some many people have been told they're okay and they weren't. The app keeps popping up as a notification with no notification. It's not even scanning the area. Uninstalled like I am sure many have or will as its not been created well or thought through.<br> :date: __2020-12-27 19:14:31__

> App doesn't work on my phone at all! Been uninstalled and installed countless times and keeps freezing. A load of rubbish!!! 🤬🤬🤬<br> :date: __2020-12-27 17:35:03__

> Poo<br> :date: __2020-12-27 16:33:02__

> Received a message and was told to self-isolate for...wait for it...1day. Seems a pointless exercise if you aren't notified when you potentially could be at your most infectious. Would help to know where & when this was triggered so you can make a judgement yourself to the risk. I like to think I am responsible but this experience completely undermined my ability to manage my own situation and any credibility in the app has been lost.<br> :date: __2020-12-27 16:14:02__

> Its usless, all is says is loading, 24 hours a day.waste if time downloading this.<br> :date: __2020-12-27 13:52:52__

> Just been notified I've been in contact with someone even though I've not left my house in 12 days? During those 12 days I've had a negative test result.<br> :date: __2020-12-27 13:28:13__


