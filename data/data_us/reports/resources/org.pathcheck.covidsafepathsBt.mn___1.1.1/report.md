# COVIDaware MN
App version ``1.1.1``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="COVIDaware MN icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | COVIDaware MN |
| **Unique identifier** | org.pathcheck.covidsafepathsBt.mn |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=org.pathcheck.covidsafepathsBt.mn](https://play.google.com/store/apps/details?id=org.pathcheck.covidsafepathsBt.mn) |
| **Summary**  | Receive alerts about potential exposure to COVID-19 in Minnesota |
| **Privacy policy** | [https://covidawaremn.com/privacy-policy.shtml](https://covidawaremn.com/privacy-policy.shtml) |
| **Latest version** | 1.1.1 |
| **Last update** | 2020-11-18 19:02:42 |
| **Recent changes** | -  Initial release of COVID-19 Exposure Notifications |
| **Installs**  | 50,000+ |
| **Category** | Tools |
| **First release** | Sep 30, 2020 |
| **Size**  | 65M |
| **Supported Android version**  | 6.0 and up |

### Description
> COVIDaware MN is the official exposure notification app of the State of Minnesota. With the COVIDaware MN app, your phone gets notified when you may have been exposed to COVID-19. The app is built with privacy-preserving Exposure Notification technology developed by Apple and Google in partnership with the nonprofit PathCheck Foundation. COVIDaware MN exchanges anonymous Bluetooth keys with other app users when you are within 6 feet of each other for more than 15 minutes. If an app user reports they tested positive for COVID-19, the phones they exchanged keys with are anonymously notified. The notifications let Minnesotans know when they should take extra care and get tested. Nobody ever knows your location or identity, and no information on the use of this app can be traced back to you.
<br>COVIDaware MN is made available by the State of Minnesota to help slow the spread of COVID-19 in our communities. Like wearing a mask, social distancing, and washing hands, it adds another layer to our defense against the virus. No single layer is completely effective by itself, but when used together, they make us all safer. The app is part of a comprehensive contact tracing initiative managed by the Minnesota Department of Health (MDH). If you test positive for COVID-19, an MDH contact investigator will provide a test verification code you enter into the COVIDaware MN app. After you enter the verification code, other app users will be anonymously notified that they were near someone who has recently tested positive. No personal data or location tracking occurs within this app. The app’s source code is available to the public and has been carefully inspected by privacy and security experts. For complete information, visit https://covidawaremn.com.
<br>Help us slow the spread of COVID-19 in Minnesota by sharing COVIDaware MN with your friends and family. Let’s be COVID aware, MN!


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | State of Minnesota |
| **Website**  | [https://covidawaremn.com](https://covidawaremn.com) |
| **Email** | covidawaremn@state.mn.us |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=State+of+Minnesota](https://play.google.com/store/apps/developer?id=State+of+Minnesota) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | - |
| **Effective target Android version**  | - |
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
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | bugsnag.com | Bugsnag Inc. | GB | 2011-08-18 03:26:10 |
 | android.com | Google LLC | :us: US | 1997-06-23 04:00:00 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | github.com | GitHub, Inc. | :us: US | 2007-10-09 18:20:50 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the ': connect, resolve' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'No route to  ' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Pim data leakage**
> - This application accesses data stored in the clipboard<br>

**Code execution**
> - This application loads a native library<br>
> - This application executes a UNIX command<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The COVIDaware MN app has been installed by more than **50000** times. At this time, **203** rated the app and its average score is **4.174603**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 150

:star::star::star::star:: 9

:star::star::star:: 9

:star::star:: 3

:star:: 32

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="org.pathcheck.covidsafepathsBt.mn 5 reviews"/>
</p>

> If you are worried about "Big Brother" then uninstall Facebook...that's the prob app.<br> :date: __2020-12-23 22:13:00__

> I don't have Covid<br> :date: __2020-12-16 04:54:47__

> Great<br> :date: __2020-12-15 19:37:45__

> I love the idea behind this app. However because of the climate of denial and disinformation surrounding covid, it's not likely to be as effective as it could be. The people most needing this app are not likely to download it, and people like me who are taking the proper precautions are most likely not to need it.<br> :date: __2020-12-14 19:41:58__

> Very easy setup. Only asked for Bluetooth.<br> :date: __2020-12-13 23:32:26__

> Protecting yourself and others is cool, pass it on.<br> :date: __2020-12-12 19:33:17__

> Works well on my Pixel. Did not ask me for permissions, as expected.<br> :date: __2020-12-12 15:59:34__

> Easy to setup and does exactly what it says it will do. It uses bluetooth for contacting other phones so you will need bluetooth on.<br> :date: __2020-12-12 03:46:12__

> thank you mn government :)<br> :date: __2020-12-10 17:02:36__

> This gives me great peace of mind. Another tool to track possible exposures. I turn off bluetooth and location if I'm at home, and on again before I leave the house, and everything works. No need to redo setup (which is just turning on both features anyway). Downside is you'll only get a possible exposure notification if the person you're exposed to also has the app, and has it enabled at the same time you do.<br> :date: __2020-12-06 08:08:51__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="org.pathcheck.covidsafepathsBt.mn 4 reviews"/>
</p>

> Very easy and personal.<br> :date: __2020-12-28 01:18:37__

> You have to leave your bluetooth and location on when your out and around. Otherwise I would have given it 5. It's a great app otherwise.<br> :date: __2020-12-20 10:32:09__

> Excellent information<br> :date: __2020-12-10 15:11:22__

> Great idea. But I don't know anyone that uses the app. I doubt a lot of people have the app install. It defeats the purpose of being useful if only a handful if people are using the app.<br> :date: __2020-12-08 23:56:12__

> Good idea but the app doesn't start on my phone (Pixel 4 XL). It just shows a white screen with the logo.<br> :date: __2020-12-07 15:36:10__

> the only reason I give it four stars is because I don't know if it works yet or not but it seems to function on my phone and my tablet and my laptop so until I know for sure that it works that's all I have to say.<br> :date: __2020-12-06 19:26:31__

> Carol M<br> :date: __2020-12-06 02:15:38__

> Good idea, but needs support of the places that provides the tests. which currently do not provide a verification code with a positive test.<br> :date: __2020-12-02 05:45:58__

> I wish that there was a nap so I can see where cases are getting bad it would be a good feature.<br> :date: __2020-11-27 19:22:55__

> Great Idea<br> :date: __2020-11-25 00:10:39__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="org.pathcheck.covidsafepathsBt.mn 3 reviews"/>
</p>

> Seems like a great idea, but the makers didn't think about this fully before releasing it. It sends a push notification everytime it checks to see if your exposed, without any way of changing it to only alert if potentially exposed. It just went off at 01:30 (in the morning) and all it was doing was checking, which isn't cool. Also, you actually have to add your test results, so someone who's positive still might be considered negative on the app. I'd give 5 stars otherwise.<br> :date: __2020-12-27 08:36:33__

> This app was totally amazing, it was sending my Meta Data all over the world. It even showed me that my neighbor was exposing him self to Covid with a un-natural hand sanitizer pump that doubles as an omelette maker. Keep up the good work. It's a winner for me.<br> :date: __2020-12-22 04:18:23__

> Every time this app does a check for exposures, it adds a file in my downloads. One day alone had 40 checks/40 files downloaded. These are a waste of space. Otherwise, i like the theory of this app, hopefully more people download it so it can actually do its job.<br> :date: __2020-12-22 02:51:26__

> So what is a verification code and how do you get one and from whom? A help function or more explanation is needed.<br> :date: __2020-12-21 02:33:56__

> Has only one notification type called "Exposure Notification" which fires everyday/night on exposure database updates. Had to silence this annoyance, but that also silences legit exposures! More fundamental flaws: doesn't account for PPE or if barriers between people, & relies on voluntary positive test input rather than MDH registry. Good: No location permissions required. App Info screens shows "No permissions requested". Double blind anon ID system is good. No BT issues like others.<br> :date: __2020-12-18 14:20:18__

> Needs a date range for exposure. Like the app, easy to use, pleasant interface. However, I was exposed about a month ago. It alerted me correctly, but it never cleared/updated the exposure notice. It says "Possible exposure 7-14 days ago". So after your first possible exposure, you'll be tempted to ignore it. It would be more effective if it either said "Possible exposure between "11/14 and 11/21" or simply added a timestamp to each exposure notification.<br> :date: __2020-12-14 20:54:39__

> Really you're putting out an app with no dark mode? Have you not paid attention to any other applications or operating system pushes and updates? I love staring into a flashlight.<br> :date: __2020-12-12 23:05:07__

> I'm not sure that this app is really doing anything useful. The way it's set up is completely voluntary. So even if a user has Covid-19, they don't actually have to record it. And what about the people who don't download the app and use it? I'm not convinced that this app is accomplishing it's intended purpose.<br> :date: __2020-12-12 14:19:09__

> I wish there was a way to effectively use it and not have bluetooth on 24/7.<br> :date: __2020-12-06 08:54:01__

> I've read some of the reviews and some are mentioning being alerted if exposed. That would only happen if you were near someone who was infected, had the app, and followed through to report. There's many ways you could be exposed without being alerted at all. The app may have an impact and if many many people used it the impact could be significant. But maybe not.<br> :date: __2020-12-06 03:10:14__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="org.pathcheck.covidsafepathsBt.mn 2 reviews"/>
</p>

> Very poorly engineered. The fact that there is only one notification category is a problem in-and-of itself. That my downloads list is full of exposure check files is another. Other reviews complain about requiring completely new setup every time a needed service is disabled and re-enabled. Overall, the functionality is important, but I cannot endorse the engineering effort here.<br> :date: __2020-12-26 21:37:47__

> I think this app is fine. However I live in a boarder area MN WI, and WI also has a tracking app. I can only use one at a time, not both. For me this is a problem. Isn't there a way you can create them to work at the same time and give people like me better coverage?<br> :date: __2020-12-26 13:51:11__

> Verification code is not work.<br> :date: __2020-12-20 06:19:01__

> Marketing the launch, this listing, and info via the app itself could use improvements. User is instructed most explicitly in receiving notifications, and not the other major function - reporting. Please include in how-to and link in more places to the FAQ where this entire part is even touched on. Why does the app say "Verify your diagnosis"? You literally already have your diagnosis from your doctor. Why not "send" or "report"? Thanks<br> :date: __2020-12-18 01:21:17__

> Didn't all around like because of the constant notifications even with the Bluetooth off.<br> :date: __2020-12-12 05:41:09__

> After having setup the app, now when I start it, it just shows the splash screen.<br> :date: __2020-12-12 02:53:31__

> An expected disappointment. The app itself is truthful that is doesn't save ur location or personal info .... ( I checked in my settings and looked at the app permissions - none)... but that statement is true only because CovidAware isn't , Google is .. on Android 10 and below , isn't that like almost every device . Smh . The app would be good if it wasnt on the Google platform .<br> :date: __2020-12-06 16:48:18__

> Battery killer<br> :date: __2020-12-06 06:25:44__

> I'm sure the app works but it gave no clear description on how to get a verification code<br> :date: __2020-12-02 23:36:53__

> While a good idea, currently the app does not work with my phone 😔 as it does not ask for permission for exposure notifications it simply tells you to enable them, which means the option to do so never appears on the phone. I like the idea and the app in general, until it asks the user for the access it won't work with all available devices<br> :date: __2020-11-26 22:56:42__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="org.pathcheck.covidsafepathsBt.mn 1 reviews"/>
</p>

> Only turns on when home........<br> :date: __2020-12-28 01:53:11__

> Awful, unusable, unable to access. Can't Uninstall. Worse than the plague in terms of frustration.<br> :date: __2020-12-27 01:30:08__

> No provision for self-reporting and only accepting a test code that many covid-19 test sites do not provide makes this app almost impossible to use. My doctor could say I absolutely have Covid-19, and without a code number, I can't report it to the app?!?<br> :date: __2020-12-26 11:13:32__

> Make orwell fiction again.<br> :date: __2020-12-24 09:23:18__

> I have never seen a notification that I have come in contact with anything COVID and I work at the second largest retailer in the world. I also think your site is purposely Grey when it comes to asking questions.<br> :date: __2020-12-24 06:52:11__

> Shortly after installing the app, I tested positive for Covid. I tried to alert the app but it asks for a verification code. No code to be found anywhere. No help available. This app is worthless.<br> :date: __2020-12-23 19:12:13__

> Mr Stark... I don't feel so good.....<br> :date: __2020-12-21 19:42:15__

> I find it pretty sad the local governments will try to alert you to carriers of a rapidly spreading virus as opposed to known sex offenders and child predators. If only registered offenders had been forced to get an app like this and have location on so anyone within 30ft can be notified instantly of a predator.<br> :date: __2020-12-20 18:35:25__

> Sucks!<br> :date: __2020-12-20 15:20:53__

> If youre willing to give up liberty for a small amount of security, you do not deserve either one.<br> :date: __2020-12-19 20:19:30__


