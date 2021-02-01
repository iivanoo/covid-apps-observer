# COVIDaware MN
App version ``1.6.1``

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
| **Latest version** | 1.6.1 |
| **Last update** | 2020-12-23 02:24:55 |
| **Recent changes** | Thank you for using COVIDaware MN!  This update includes:<br><br>- Improved multi-language support<br>- Clearer information about verification codes<br>- More accurate exposure detection settings<br>- Support for simpler verification code entry links |
| **Installs**  | 100,000+ |
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

The COVIDaware MN app has been installed by more than **100000** times. At this time, **404** rated the app and its average score is **3.4455445**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 184

:star::star::star::star:: 40

:star::star::star:: 48

:star::star:: 36

:star:: 96

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="org.pathcheck.covidsafepathsBt.mn 5 reviews"/>
</p>

> (optional)<br> :date: __2021-01-20 08:52:59__

> Edit: the below issue has been addressed. Much better now! Old review: "Like the app, easy to use, pleasant interface. However, I was exposed about a month ago. It alerted me correctly, but it never cleared/updated the exposure notice. It says "Possible exposure 7-14 days ago". So after your first possible exposure, you'll be tempted to ignore it. It would be more effective if it either said "Possible exposure between "11/14 and 11/21" or simply added a timestamp to each exposure notification."<br> :date: __2021-01-13 15:17:30__

> No personal data taken and easy to use.<br> :date: __2021-01-13 03:44:15__

> I want to be informed so I can do what is best for me.<br> :date: __2021-01-11 19:58:14__

> Thank u for keeping us safe. Blessings. I love Minnesota so very much.<br> :date: __2021-01-10 01:04:21__

> I put it on my phone<br> :date: __2021-01-04 01:10:39__

> Technology is awesome! Needs some further development but I doubt there's money there.<br> :date: __2020-12-31 02:03:56__

> If you are worried about "Big Brother" then uninstall Facebook...that's the prob app.<br> :date: __2020-12-23 22:13:00__

> I don't have Covid<br> :date: __2020-12-16 04:54:47__

> Great<br> :date: __2020-12-15 19:37:45__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="org.pathcheck.covidsafepathsBt.mn 4 reviews"/>
</p>

> Good medicine<br> :date: __2021-01-12 19:16:40__

> Very easy and personal.<br> :date: __2020-12-28 01:18:37__

> You have to leave your bluetooth and location on when your out and around. Otherwise I would have given it 5. It's a great app otherwise.<br> :date: __2020-12-20 10:32:09__

> Excellent information<br> :date: __2020-12-10 15:11:22__

> Great idea. But I don't know anyone that uses the app. I doubt a lot of people have the app install. It defeats the purpose of being useful if only a handful if people are using the app.<br> :date: __2020-12-08 23:56:12__

> Good idea but the app doesn't start on my phone (Pixel 4 XL). It just shows a white screen with the logo.<br> :date: __2020-12-07 15:36:10__

> the only reason I give it four stars is because I don't know if it works yet or not but it seems to function on my phone and my tablet and my laptop so until I know for sure that it works that's all I have to say.<br> :date: __2020-12-06 19:26:31__

> Carol M<br> :date: __2020-12-06 02:15:38__

> Good idea, but needs support of the places that provides the tests. which currently do not provide a verification code with a positive test.<br> :date: __2020-12-02 05:45:58__

> I wish that there was a nap so I can see where cases are getting bad it would be a good feature.<br> :date: __2020-11-27 19:22:55__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="org.pathcheck.covidsafepathsBt.mn 3 reviews"/>
</p>

> App is simple to use. Haven't been exposed so not sure if it's working. But a new bug has emerged. It's no longer updating my exposure checks. The notification stays active and can't be dismissed. I am uninstalling until it can be fixed. Don't feel like seeing a constant notification but isn't actually checking my exposure.<br> :date: __2021-01-13 14:40:41__

> Broken! The checking exposure notification doesn't ever go away. This is completely unacceptable as it will cause people to delete the app.<br> :date: __2021-01-13 06:56:40__

> Virus control<br> :date: __2021-01-08 00:06:45__

> So far, I can't tell, but tomorrow I go to hospital. I expect it will go off like crazy there. Not sure what the range is...6'? 20'? For airborne virus, 6' is no where near enough distance. I surmized that in January 2020, based on YouTube reports of medical analyst Dr. John Campbell. Check his channel out.<br> :date: __2020-12-29 19:44:24__

> Seems like a great idea, but the makers didn't think about this fully before releasing it. It sends a push notification everytime it checks to see if your exposed, without any way of changing it to only alert if potentially exposed. It just went off at 01:30 (in the morning) and all it was doing was checking, which isn't cool. Also, you actually have to add your test results, so someone who's positive still might be considered negative on the app. I'd give 5 stars otherwise.<br> :date: __2020-12-27 08:36:33__

> This app was totally amazing, it was sending my Meta Data all over the world. It even showed me that my neighbor was exposing him self to Covid with a un-natural hand sanitizer pump that doubles as an omelette maker. Keep up the good work. It's a winner for me.<br> :date: __2020-12-22 04:18:23__

> Every time this app does a check for exposures, it adds a file in my downloads. One day alone had 40 checks/40 files downloaded. These are a waste of space. Otherwise, i like the theory of this app, hopefully more people download it so it can actually do its job.<br> :date: __2020-12-22 02:51:26__

> So what is a verification code and how do you get one and from whom? A help function or more explanation is needed.<br> :date: __2020-12-21 02:33:56__

> Really you're putting out an app with no dark mode? Have you not paid attention to any other applications or operating system pushes and updates? I love staring into a flashlight.<br> :date: __2020-12-12 23:05:07__

> I'm not sure that this app is really doing anything useful. The way it's set up is completely voluntary. So even if a user has Covid-19, they don't actually have to record it. And what about the people who don't download the app and use it? I'm not convinced that this app is accomplishing it's intended purpose.<br> :date: __2020-12-12 14:19:09__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="org.pathcheck.covidsafepathsBt.mn 2 reviews"/>
</p>

> Gives a notification for 'checking exposures' that doesn't go away and you can't dismiss the notification. Would like to have the app, but I don't want it if it has this annoying bug.<br> :date: __2021-01-18 17:25:50__

> Why is this app downloading multiples of files every day? Dear God there is no settings I have limited data and there is no download with confirmation to see if we want to wait on the updates. It's downloading a bunch do notifications files. This behavior is not acceptable to me...<br> :date: __2021-01-17 23:04:18__

> don't know but bluetooth bad for me<br> :date: __2021-01-13 15:40:34__

> I didn't find the app useful as it only searched to see if I was around anyone exposed while I was alone at home. Not helpful!!!!<br> :date: __2021-01-13 04:02:06__

> So I got a positive test; the app REFUSES my code saying that theres an error or that something went wrong i deleted the app; redownloaded it; cleared the cache and nothing works but the MDH wanted me to download the app.<br> :date: __2020-12-30 02:19:23__

> Very poorly engineered. The fact that there is only one notification category is a problem in-and-of itself. That my downloads list is full of exposure check files is another. Other reviews complain about requiring completely new setup every time a needed service is disabled and re-enabled. Overall, the functionality is important, but I cannot endorse the engineering effort here.<br> :date: __2020-12-26 21:37:47__

> I think this app is fine. However I live in a boarder area MN WI, and WI also has a tracking app. I can only use one at a time, not both. For me this is a problem. Isn't there a way you can create them to work at the same time and give people like me better coverage?<br> :date: __2020-12-26 13:51:11__

> Verification code is not work.<br> :date: __2020-12-20 06:19:01__

> Marketing the launch, this listing, and info via the app itself could use improvements. User is instructed most explicitly in receiving notifications, and not the other major function - reporting. Please include in how-to and link in more places to the FAQ where this entire part is even touched on. Why does the app say "Verify your diagnosis"? You literally already have your diagnosis from your doctor. Why not "send" or "report"? Thanks<br> :date: __2020-12-18 01:21:17__

> Didn't all around like because of the constant notifications even with the Bluetooth off.<br> :date: __2020-12-12 05:41:09__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="org.pathcheck.covidsafepathsBt.mn 1 reviews"/>
</p>

> It's an app that will track YOU even when it's off. Supreme Court ruled that they cannot track you without a Search Warrant. This popped up on my new phone...unrequested!<br> :date: __2021-01-28 06:07:15__

> Oh noes a virus whose average age of death is higher than the average life expectancy! Quick, embrace technocommunism and report undesirables to authorities for medical confinement in a *cough* gulag. What could go wrong? Are you afraid yet? Have you consented to give all private property rights over to the state yet? Hello, 911? I'd like to report someone not living in fear of this common cold Trump and Giuliani beat in 72 hours.<br> :date: __2021-01-25 00:03:41__

> This app is bad delete this app it said covid is dangerous<br> :date: __2021-01-24 19:16:03__

> It's been goodnight<br> :date: __2021-01-21 20:21:50__

> So, the app works pretty decently. My complaint is, I just recently was exposed to someone who has covid. There is no way to input a possible exposure in the app. The idea is to prevent. But you can only report if you have a code from a positive test result... Kinda worthless then.. so who are we actually helping?<br> :date: __2021-01-19 21:47:53__

> Buggy and annoying. The "checking exposures" notification will pop up on top of literally everything else even though a background process running is my lowest priority unless I've actually been exposed. And sometimes it gets stuck in a loop causing it to pop up over and over for a period of about 5 minutes. And during that 5 minutes, the app itself won't even open - it gets stuck on the splash screen.<br> :date: __2021-01-18 15:47:24__

> Tells me I need to authorize covid exposure notifications in settings but settings won't allow me to authorize them until the app is finished downloading<br> :date: __2021-01-17 18:33:05__

> Useless, as no one in the US will self report having COVID-19. I installed and absolutely nothing ever happened, even when my close contact colleague got the virus, and was out for weeks.<br> :date: __2021-01-16 19:58:50__

> This app is pretty much useless! I got COVID last week from an unknown exposure and didn't get any app exposure notifications. After my test came back positive, I had to ask the MN Department of Health for the app code 3 times! After I entered the code, my husband didn't get an exposure notification until 8 hours later - after he touched the "Check for exposures" button while sitting next to me. The app said he was potentially exposed within the last 2 days. I've been contagious for at least 7.<br> :date: __2021-01-15 23:53:44__

> As others have stated, I have my doubts about the effectiveness of the app. I'm sure it uploads all kinds of information about you to some database somewhere, but It does not seem to provide any meaningful information to back to the user. Over New Years I went to Las Vegas. I got on a plane, spent 5 days in a casino/hotel, got back on a plane and came home. The app shows no exposures? I find this hard to believe.<br> :date: __2021-01-15 15:16:52__


