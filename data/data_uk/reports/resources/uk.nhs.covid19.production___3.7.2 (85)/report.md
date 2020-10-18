# NHS COVID-19
App version ``3.7.2 (85)``

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
| **Latest version** | 3.7.2 (85) |
| **Last update** | 2020-10-14 17:54:55 |
| **Recent changes** | Bug fixes. |
| **Installs**  | 5,000,000+ |
| **Category** | Medical |
| **First release** | Aug 12, 2020 |
| **Size**  | 7.1M |
| **Supported Android version**  | 6.0 and up |

### Description
> The new NHS COVID-19 app is the Official NHS contact tracing app for England and Wales. 
<br>It is the fastest way of knowing when you’re at risk from Coronavirus. The quicker you know, the quicker you can alert your loved ones, and your community. 
<br>The more of us that use it, the better we can control coronavirus. 
<br>The app runs on proven software developed by Apple and Google, designed so that nobody will know who or where you are. And you can delete your data, or the app, at any time.
<br>It has a number of features: 
<br>- Trace: Find out when you’ve been near other app users who have tested positive for coronavirus
<br>- Alert: Lets you know the level of coronavirus risk in your postcode district. 
<br>- Check-in: Get alerted if you have visited a venue where you may have come into contact with coronavirus, using a simple QR code scanner. No more form filling. 
<br>- Symptoms: Check if you have coronavirus symptoms and see if you need to order a test. 
<br>- Test: Helps you order a test if you need to.
<br>- Isolate: Keep track of your self-isolation countdown and access relevant advice.
<br>Available in English, Welsh, Bengali, Urdu, Gujarati, Punjabi (Gurmukhi script), Chinese (Simplified), Romanian, Turkish and Arabic (Modern Standard). Additional languages and refinements will follow.
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

The NHS COVID-19 app has been installed by more than **5000000** times. At this time, **69244** rated the app and its average score is **4.1758432**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 43895

:star::star::star::star:: 10213

:star::star::star:: 5549

:star::star:: 2596

:star:: 6991

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 5 reviews"/>
</p>

> Alright, I mean it does the job but they could of added a scan thing where you scan you and tell if you have Covid but everything else is alright you should really get this app in my opinion Make sure to stay safe guys🤧☺<br> :date: __2020-10-18 10:45:23__

> Working as it should! No complaints from me 🤔<br> :date: __2020-10-18 10:35:21__

> On a personal basis, I dont see any affect. However, in the overall picture I am sure the app is helping me and my family, so, well done.<br> :date: __2020-10-18 10:32:59__

> Good<br> :date: __2020-10-18 10:32:08__

> GREAT ALERT 4 COVID-19 APP<br> :date: __2020-10-18 10:12:26__

> Very easy to use wherever there is a NHS COVID19 track and trace sign in.<br> :date: __2020-10-18 10:11:31__

> I think the app is very good I've had no problems at all until it first came out 100%<br> :date: __2020-10-18 09:31:40__

> Effective<br> :date: __2020-10-18 08:48:53__

> Good<br> :date: __2020-10-18 07:44:50__

> SAVE LIVES AND DOWNLOAD THIS APP - SO SIMPLE YET ANONYMOUS<br> :date: __2020-10-18 04:44:19__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 4 reviews"/>
</p>

> I had to change my screen width settings on my phone to not be classed as a tablet, so not a 5-star review, but otherwise a decent system. I love how when Google tells you someone who you passed in the street now has tested +ve, the app now sends a second notification saying that the NHS are aware and they don't consider it as a close enough contact. It really reassures me that the makers of the app care about getting it right, and are doing more than the bare minimum as some devs could.<br> :date: __2020-10-18 03:59:27__

> Needs past notification button, I've accidentally swiped notifications by accident so would be helpful if there was a place for them to come through and stay on the app with time /date to help pin point exsposure<br> :date: __2020-10-18 03:30:40__

> Hi I think it's great but I got a notification saying I've been exposed to covid-19 and am wondering if I should isolate or not and how do I get the notification up in the app to show me when the app has scanned.<br> :date: __2020-10-18 03:29:37__

> small issue my battery died and needed to be recharged. app stated i have. to remain isolated until tonight 23.00 hrs now states im fine. not had test results yet. ill still remain isolated but for how much longer i dont know. Single and need to shop as have pets that need food. to.<br> :date: __2020-10-18 02:59:07__

> odd hitch but important to have<br> :date: __2020-10-17 21:59:17__

> Good app, simple to use. However feel it would be better if location automatically updated, as I often forget to change my postcode/don't know the postcode. Would also be good if location would link to information on rules for that area.<br> :date: __2020-10-17 21:21:37__

> Generally pretty good and easy to use. No noticable battery drain. Only issue is the isolation count down. I tested positive on a Saturday (result received following Tuesday) but the 10 day countdown started on the Tuesday, not Saturday as guidelines would suggest. And I checked my account. This gives Saturday as 1st day of isolation So there appears to be a significant fault with the App which just adds to confusion.<br> :date: __2020-10-17 19:43:25__

> works well but had no notifications yet so can't comment on effectiveness<br> :date: __2020-10-17 18:10:16__

> good location helpful staff<br> :date: __2020-10-17 17:25:26__

> Not able to change location if I move.<br> :date: __2020-10-17 17:15:00__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 3 reviews"/>
</p>

> No longer opens after 14th Oct update. Google pixel 4a<br> :date: __2020-10-18 10:19:00__

> There should be an inbox for notifications. the pop up messages disappear and it is difficult to read them immediately.<br> :date: __2020-10-18 10:09:53__

> The level in my area is shown as different to the government website!!! When / can this be corrected?<br> :date: __2020-10-18 09:32:11__

> It is an OK app, but it would be better if you could see the notifications again. Once you've clicked off you can't see what it said. This morning I had one that said you've been in close contact, but don't worry. I clicked on the notification and it vanished and now I can't find it to read it properly.<br> :date: __2020-10-18 09:14:19__

> The sort of person who is selfish enough not to self isolate when needed to isn't likely to of bothered with downloading and using this app. Quite then why you've revealed that you'll share info with the police is beyond me. All you've done is hurt the success of the app and give the tin foil hat wearers an energy boost.<br> :date: __2020-10-18 08:47:45__

> Crashing on launch after last update.<br> :date: __2020-10-18 01:40:59__

> I'm a bit confused how so much money has been spent on this app. When you get a notification saying you may have been in contact, you click on it and it disappears. Its really unclear. Could do with a guide/key for all the different notifications you may get. I mean we were taught in primary school always make a guide/key for data someone other than yourself has to use.<br> :date: __2020-10-18 00:17:00__

> means to an end<br> :date: __2020-10-17 23:12:44__

> I mean, I've got it and everything but it's not downloaded any exposure data since Sept 25th so not quite sure how useful it's being for me. Turned off battery optimisation and made sure exposure notifications and Bluetooth is on. Not sure how much more manual fiddling of my Android settings will feel productive.<br> :date: __2020-10-17 22:58:30__

> When you install the app and when you try to set it up, it says you have to be over 16 to use the app. Why do you think is that?<br> :date: __2020-10-17 22:49:46__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 2 reviews"/>
</p>

> Downloaded app but was unimpressed not as good as I was expecting app deleted<br> :date: __2020-10-18 10:43:24__

> Pointless When you work on itu caring for confirmed cases of covid and the app still doesn't notify you it's obvious there is a serious flaw somewhere.<br> :date: __2020-10-18 10:27:28__

> Not too happy about having to have bluetooth switched on all the time.<br> :date: __2020-10-18 10:26:32__

> So how long does it take the app to notify you of exposure as I woke this morning to a notification, so unless someone broke in last night, exposed me and left, is this an error? Also when i clicked to read notification, it just disappeared and took me to the app. So I have no idea if I have been exposed or not. Should maybe include a way to read past notifications in the app.<br> :date: __2020-10-18 10:25:57__

> Not really that good. I keep receiving notifications telling me I've come in contact with someone that has Covid but there's no information in the app. I receive this notification 4-5 times a day, sometimes at 3/4 am.<br> :date: __2020-10-18 10:17:20__

> I know there are replies from the department of health to these reviews with regard to the disappearing "potential exposure" pop up, but surely this is fixable by the app developers? I had one of these and only managed to read the first three words before it disappeared for good, leaving me and family in a state of confused shock.<br> :date: __2020-10-18 10:14:09__

> The False messages about exposure are becoming annoying, both on mine and partners mobile<br> :date: __2020-10-18 09:16:24__

> Fails to scan QR code as I just get a blank screen, wife gets a message telling her where she has checked in. Have reinstalled once and still have same problem.<br> :date: __2020-10-18 09:15:59__

> Still getting notifications of exposure followed immediately by ones saying 'don't worry...', implying it's not actually a correct warning. Absolutely fundamental error, no idea how this made it through QA.<br> :date: __2020-10-18 05:28:21__

> The idea is good. I hope a lot of people will use it. HOWEVER I don't want to find out that I have been exposed to it from a notification which disappears as soon as you click on it and the app doesn't say anything about it. When? Where? How long? If there is nothing I can or should do about it, why notify me? If there is something I can or should do, then tell me in the app. This just worries me and offers no answers or advice.<br> :date: __2020-10-18 03:53:41__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 1 reviews"/>
</p>

> Was good until they decided to share information with the police. No longer respects your privacy. Uninstalled.<br> :date: __2020-10-18 10:57:52__

> Not allowing you to change your Postcode. Once entered it will not change. And if you go somewhere else it doesn't tell you where you are. GPS not working at all. Not showing if am home or at work<br> :date: __2020-10-18 10:49:47__

> Message disappeared when trying to open.<br> :date: __2020-10-18 10:38:34__

> total disregard of privacy<br> :date: __2020-10-18 10:37:11__

> Showing alerts on my smart watch that weren't on the phone, poorly made! very annoying, will install if I need to go out and about<br> :date: __2020-10-18 10:24:00__

> Police access is unacceptable.<br> :date: __2020-10-18 10:22:59__

> Does its job, however, the recent announcement that the police can access your location data is a gross violation of our privacy and I will now be uninstalling the app. Massive step backwards for public confidence.<br> :date: __2020-10-18 10:19:54__

> Removing due to the risk of days behind sent to the government. I don't want to be put in a situation where an application but leaves me in a situation where I'm in court. This is not the world I want to live in. Check recent news, where they intend to share data with the police force.<br> :date: __2020-10-18 10:13:42__

> I was going to install this till I found you have to keep Bluetooth on all the time. I'm not having Bluetooth on all the time to waste my battery power.<br> :date: __2020-10-18 10:11:05__

> Data is being shared with Police without explicit consent.<br> :date: __2020-10-18 10:00:45__


