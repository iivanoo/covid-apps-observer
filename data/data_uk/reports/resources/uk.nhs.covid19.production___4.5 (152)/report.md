# NHS COVID-19
App version ``4.5 (152)``

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
| **Latest version** | 4.5 (152) |
| **Last update** | 2021-02-19 17:46:26 |
| **Recent changes** | We have introduced a change which means that users who enter a positive test result from a lab into the app, but did not book the test through the app, will be asked to state when their symptoms started. This is to make sure the self-isolation countdown in the app aligns with the advice from the contact tracing teams in the wider programme. Other design, language and accessibility optimisations.  |
| **Installs**  | 5,000,000+ |
| **Category** | Medical |
| **First release** | Aug 12, 2020 |
| **Size**  | 8.5M |
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

The NHS COVID-19 app has been installed by more than **5000000** times. At this time, **99515** rated the app and its average score is **3.6966133**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 52634

:star::star::star::star:: 11760

:star::star::star:: 8430

:star::star:: 5680

:star:: 21011

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 5 reviews"/>
</p>

> I have not been exposed to covid<br> :date: __2021-03-06 11:11:32__

> I like this App.<br> :date: __2021-03-05 10:11:37__

> Good<br> :date: __2021-03-04 23:37:00__

> Great<br> :date: __2021-03-04 06:30:22__

> Exelent app having problems at the moment I constantly have the shield 🛡 symbol at the top of my ohine saying loading<br> :date: __2021-03-03 22:38:38__

> A must<br> :date: __2021-03-03 16:56:04__

> Excellent app, and a brilliant way of protecting our fellow man. Never leave home without the app running.<br> :date: __2021-03-03 15:19:48__

> Awesome<br> :date: __2021-03-03 14:36:46__

> Unfortunately I cannot download this app, I get a message after entering my post code, it does not support it, download app for your area 🤔<br> :date: __2021-03-03 13:21:28__

> Great for keeping track of tests but also notifying you if you have potentially been infected. This will not track you as a person.<br> :date: __2021-03-03 07:48:25__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 4 reviews"/>
</p>

> Apart from putting in test results function, can we have the NHS jab card to put in the app to proof we have done the jab? Like test results function. Thank you!<br> :date: __2021-03-05 16:49:57__

> OK, needed now for school. As children are back at school, adults must test twice a week and we have to put data into this app. Easy to use.<br> :date: __2021-03-05 15:49:42__

> Good app<br> :date: __2021-03-04 04:59:02__

> Loading... notification bug is back!<br> :date: __2021-03-02 09:36:07__

> Great updates<br> :date: __2021-03-01 17:36:00__

> it's very good helped through covid-19<br> :date: __2021-02-28 20:57:05__

> Why not have a facility on the app to record your jab details?<br> :date: __2021-02-23 20:02:16__

> This week the app won't open at all. Immediately crashes every time. I'm on a Pixel 3. Was fine previously (apart from the usual meaningless notifications).<br> :date: __2021-02-23 19:35:14__

> Works fine 99% of the time. Previous problems resolved.<br> :date: __2021-02-23 15:29:09__

> Updated review — hopefully the Pixel issues have been resolved now. So far, so good.<br> :date: __2021-02-23 14:05:28__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 3 reviews"/>
</p>

> After testing positive I input my results for the app to then notify my next door neighbours, who I had not been in any contact with. It also contacted my boss who I hadn't seen for 4 days, surely it should onlu ping those who you've been in close contact with within the last 48 hours. Its all well and good having this app, as it can be useful but surely it needs updating to it being within 2 meters and 48 hours with and not the 10-20 meters bluetooth range of most phones.<br> :date: __2021-03-06 07:02:14__

> Doesn't distinguish whether walls are between you and infected person (terraced houses) as it uses Bluetooth technology that can transmit through walls.<br> :date: __2021-03-04 17:16:10__

> The app is very helpful but one thing I would like to find out is there any way the app can have a checkout button.<br> :date: __2021-03-04 14:27:00__

> I used this app once. I found it useful but the downside with this app is it drains my battery life!<br> :date: __2021-03-03 23:25:42__

> This app also won't allow you to input negative results from tests that were booked outside the app. It also doesn't accept results from labs like the Public Health England lab or NHS hospital, or as part of national surveillance testing conducted by the Office for National Statistics. It also comes up with the notification "NHS Covid-19 Loading..." after the phone has rebooted and this notification won't go away.<br> :date: __2021-03-03 15:28:55__

> the qr scanner doesn't always work !<br> :date: __2021-03-03 14:35:52__

> I have the figure 1 on the app on my home page and I have been searching the app for the notification but can't find any. Why is this??! I always use the QR scanner if I go out, however, that isn't very often as very few places have the QR code to scan!<br> :date: __2021-03-02 23:43:06__

> Bluetooth has to be on 24/7 if you turn it off the app keeps telling you it becomes annoying why should i have it scanning when at home on my own pain in the back side<br> :date: __2021-03-02 13:22:21__

> Don't know if I'm coming or going just hurry up and get the hairdressers open cos I feel like one of the flintstones here.<br> :date: __2021-03-01 12:19:40__

> Well it's poor considering your life may depend on it this is twice I've had this app 1st time didn't even open now it dose Nd I just hope that this can be sorted out Nd fixed as this covid is going to be around for a long time it's the new plague<br> :date: __2021-02-28 20:31:58__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 2 reviews"/>
</p>

> The same previous old bike has returned and it's the one that has the constant loading notification that doesn't go away even if you try to clear the notifications and also try to restart the app<br> :date: __2021-03-04 11:38:46__

> Using a note edge paired with smart watch, kept getting notifications on the watch telling me to check the phone for details, but when I do there is nothing; 68 (empty) notifications on the watch, none of which I could read.<br> :date: __2021-03-03 15:32:44__

> I've had 2 negative tests and it's not accepted either code! The codes were entered correctly and were not recognised at any point. I'm afraid the FAQ answer does not help.<br> :date: __2021-03-02 16:20:30__

> When you change areas the app does not pick up location change<br> :date: __2021-02-27 18:00:48__

> Loading notification never goes away<br> :date: __2021-02-25 15:35:52__

> Not recognising test code...so track and trace usless....after reading below response by developer, we have this app on 4 phones in the house all 4 of us are positive and have a valid NHS test code...NONE of these are recognised by the app....do alerting others is useless Read answer and still does validate the positive test code, therefore it won't alert and close contacts...useless and uninstalled<br> :date: __2021-02-24 20:53:15__

> Keep getting a Loading... notification stuck on notification bar, have to keep force stopping and restarting to get going again.<br> :date: __2021-02-24 13:59:44__

> Had to uninstall for few reasons, it told me at 3am I was in contact with someone, but I wasn't near anyone as was sitting at home alone. Other reason for uninstall was because it was interfering with my other apps and games and causing lag<br> :date: __2021-02-23 12:36:50__

> Bubby I love bubby<br> :date: __2021-02-23 01:04:06__

> I have this app on two phones, my personal mobile and my work mobile. I tested positive last month and updated my personal mobile with my code to confirm I was positive. As a test I waited for my work mobile to notify me to self isolate as I'd been in contact with someone who had tested positive but it didn't. No harm done but surely my work phone should have notified me as the app doesn't know I own both phones!<br> :date: __2021-02-22 23:54:23__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 1 reviews"/>
</p>

> A complete waste UK tax payers money that has solved and achieved nothing.<br> :date: __2021-03-06 12:06:32__

> Drains battery with constant 'loading' notifications.<br> :date: __2021-03-06 09:50:35__

> Absolutely awful. I've been in close contact with at least 3 people I know of who have had the virus yet not a single alert. Total waste of time and tax payers money!<br> :date: __2021-03-05 23:19:40__

> Drained my battery way too much for no discernable benefit<br> :date: __2021-03-05 22:01:25__

> I've had something loading for over a week now? I've uninstall and reinstall app and it's still there. What does this mean please?<br> :date: __2021-03-05 19:03:56__

> "Loading..." Notification will not go away. No reference number if told to isolate. All in all I'd expect more from an app that cost 70 times the development cost of Pokémon Go to create. All in all a massive rip off of the British taxpayer for an app that doesn't work. I also know I've been close to people who have tested positive but have not been notified.<br> :date: __2021-03-05 18:33:42__

> This app crashes all the time. Matt Hancock's chums did a terrible job at creating it.<br> :date: __2021-03-05 15:15:25__

> This ain't it chief.<br> :date: __2021-03-05 11:34:41__

> Unfortunately I can't make it zero stars cause let's be frank, ducking 37 billion on this garbage should be criminal and stop calling it the NHS track and trace unless you're willing to hand them over some billions. The SERCO TRACK AND TRACE APP is shite. Thanks for listening to my ted talk ✌️<br> :date: __2021-03-05 11:24:56__

> No link up or provision to log vaccination. Bluetooth energy use to high Poor design Wasted opportunity to do something good.<br> :date: __2021-03-05 09:40:00__


