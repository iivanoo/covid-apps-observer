# COVID Alert NJ
App version ``1.1.1``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="COVID Alert NJ icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | COVID Alert NJ |
| **Unique identifier** | com.nj.gov.covidalert |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=com.nj.gov.covidalert](https://play.google.com/store/apps/details?id=com.nj.gov.covidalert) |
| **Summary**  | Help us stop the spread of COVID-19 in New Jersey! |
| **Privacy policy** | [https://www.nj.gov/health/documents/DPP_COVIDALERTNJ.pdf](https://www.nj.gov/health/documents/DPP_COVIDALERTNJ.pdf) |
| **Latest version** | 1.1.1 |
| **Last update** | 2021-02-17 10:48:21 |
| **Recent changes** | Minor text updates |
| **Installs**  | 100,000+ |
| **Category** | Health & Fitness |
| **First release** | Sep 18, 2020 |
| **Size**  | 106M |
| **Supported Android version**  | 6.0 and up |

### Description
> COVID Alert NJ App is being made available by the New Jersey Department of Health (DOH) to complement New Jersey’s comprehensive COVID-19 contact tracing effort. COVID Alert NJ is a free and secure mobile phone app that allows New Jerseyans:
<br>1.	To be alerted if they have been in close contact with another app user who has tested positive for COVID-19 – even if that person is a stranger
<br>2.	To track their symptoms and get advice on what to do to protect themselves and others
<br>3.	To be able to anonymously warn other app users whom they were in close contact with, if they tested positive for COVID-19 – especially people they do not know or remember being in close contact with (e.g., during bus/train ride, at public places)
<br>4.	To monitor the latest information and statistics related to the COVID-19 pandemic
<br>5.	To reach NJ public health representatives and be connected with support services 
<br>For all this to work, all you have to do is push “Allow” COVID-19 Exposure Notification Services (ENS) on your phone within your App.
<br>You can also choose to “Allow” your phone to turn on the COVID-19 Exposure Notification Services (ENS) and also “Allow” your phone to display notifications so that you also receive an alert that you have been exposed to someone who has tested positive for COVID-19. You can also turn off this functionality, at any time, in the Settings page of the App. 
<br>In the event you receive an Exposure Notification, you may read NJ DOH advice under Exposure Notification Information or get in touch with a public health representative.
<br>It is important to note that COVID Alert NJ will never reveal the identity of any person using the app to other app users, and never reveals who has been diagnosed as positive for COVID-19. 
<br>Help us Stop the Spread of COVID-19 in New Jersey. Share this app with your friends and family.
<br>The use of this App is entirely voluntary and it is available to download for free from the Google Play Store. The App runs Android phones running Android 6.0 and higher. The App is not intended for use by persons under 18 years of age, as they are considered not to have reached the digital age of consent or agreement with the State of New Jersey. You will be asked to confirm that you are 18 years or older after you download the App.
<br>View our privacy policy here: https://www.nj.gov/health/documents/DPP_COVIDALERTNJ.pdf


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
| **Developer**  | State of New Jersey  Applications |
| **Website**  | [https://covid19.nj.gov/index.html](https://covid19.nj.gov/index.html) |
| **Email** | COVIDapp@doh.nj.gov |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=State+of+New+Jersey++Applications](https://play.google.com/store/apps/developer?id=State+of+New+Jersey++Applications) |

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
 **android.permission<br>ACCESS_WIFI_STATE** | Normal | Allows applications to access information about Wi-Fi networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>VIBRATE** | Normal | Allows access to the vibrator. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | android.com | Google LLC | :us: US | 1997-06-23 04:00:00 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | expo.io | See PrivacyGuardian.org | :us: US | 2011-05-01 21:26:50 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the MCC+MNC of the provider of the SIM<br>
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address ' returned no addresses for  ; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Pim data leakage**
> - This application accesses data stored in the clipboard<br>

**Code execution**
> - This application loads a native library<br>
> - This application executes a UNIX command<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The COVID Alert NJ app has been installed by more than **100000** times. At this time, **693** rated the app and its average score is **4.2403846**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 474

:star::star::star::star:: 80

:star::star::star:: 46

:star::star:: 20

:star:: 73

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="com.nj.gov.covidalert 5 reviews"/>
</p>

> In the year of the begin stroke and stage of covid it hands down help to get information and clear image a covid 19 wear and tear Thank you for the strong verification Ps Sylvester J Ali<br> :date: __2021-03-21 08:20:22__

> It has check in every day and also has alerts if you have been near a person with Covid 19.<br> :date: __2021-03-19 12:19:46__

> It's the best app and with very accurate information.<br> :date: __2021-03-16 22:58:35__

> Has done what it says. As long as other people have this on their phone you are safer. It always you if someone nearby has had covid-19, as long as they use the app.<br> :date: __2021-03-16 16:24:59__

> This is so usefull<br> :date: __2021-03-16 02:56:12__

> Good information about COVID-19.<br> :date: __2021-03-08 15:39:22__

> I LOVE THIS APP! I Live In Essex County, NJ Which Is The 2nd Highest In The State. While Taking NJ Transit Yesterday, I Actually Received An Exposure Alert While On The Bus! I Immediately Got Off The Bus, And Waited For The Next One, And The Exposure Alert Stopped!<br> :date: __2021-03-07 19:04:04__

> Nice apk<br> :date: __2021-03-05 01:13:37__

> Keeps me well informed<br> :date: __2021-03-04 03:56:02__

> Had 1st shot. 2nd scheduled for 10th of March. But I have a head cold & a mild sore throat with a dormant ache in my chest!<br> :date: __2021-03-02 12:53:45__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="com.nj.gov.covidalert 4 reviews"/>
</p>

> bi.d.e.n<br> :date: __2021-02-22 02:00:15__

> This app works well as far as the exposure system goes. Only downside is that the Covid tally for the state total is not accurate. It has been stuck at 615K for me, when obviously the numbers keep getting higher. Please fix this.<br> :date: __2021-01-30 09:39:17__

> Help us stop the spread of COVID-19 in New Jersey! COVID Alert NJ App is being made available by the New Jersey Department of Health (DOH) to complement New Jersey’s comprehensive COVID-19 contact tracing effort. COVID Alert NJ is a free and secure mobile phone app that allows New Jerseyans: 1. To be alerted if they have been in close contact with another app user who has tested positive for COVID-19 – even if that person is a stranger 2. To track their symptoms and get advice on what to do to<br> :date: __2021-01-25 03:35:13__

> Want info on getting vaccine !!<br> :date: __2021-01-08 20:39:52__

> It should show where I am in the queue for vaccination.<br> :date: __2021-01-06 14:58:41__

> Need to have an option to change the "How are you feeling?" response for when you select the incorrect response by mistake.<br> :date: __2020-12-26 19:43:12__

> Optimistic about the potential.<br> :date: __2020-12-12 17:22:21__

> I like that you can take a moment to store daily check ups. SJZ<br> :date: __2020-12-11 19:49:58__

> Informative<br> :date: __2020-11-30 11:57:38__

> This is a very informative app.<br> :date: __2020-11-18 01:56:53__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="com.nj.gov.covidalert 3 reviews"/>
</p>

> It's fine for the State of NJ tracking you. But, if you like me are struggling to get vaccinated it is totally useless, much like the State of NJ's vaccine site.<br> :date: __2021-03-02 13:23:05__

> no data update for several days<br> :date: __2021-02-23 18:09:44__

> Never received any alerts<br> :date: __2021-02-12 03:18:12__

> The app icon went from filling in the whole circle to becoming an unreadable tiny square in a circle.<br> :date: __2021-02-07 18:56:39__

> Okay<br> :date: __2021-01-30 07:35:25__

> The numbers for confirmed cases and deaths are wrong.<br> :date: __2021-01-18 21:33:16__

> This app needs improvement. When you get an exposure alert it doesn't tell you the date of exposure, just that it was within the past 14 days. So you could already be out of the quarantine period or only need to test and isolate for a few days. Giving the date of exposure seems important.<br> :date: __2021-01-06 00:25:46__

> Rite aid Cov 19 testing<br> :date: __2020-12-13 15:43:07__

> I Certainly can't actually Rate something I just got.<br> :date: __2020-11-18 22:11:50__

> Works ONLY: #1. If an infected person ALSO has the APP and you both have Bluetooth &. Location turned on. And #2. You come within 6 Feet for more than 10 minutes of an infected person AND #3 The infected person AGREES to allow the Tracers to access the app code information. What code? When your phone meets another phone ( see #1) a code is sent via bluetooth to both phones. The app remembers the code info. The tracer simply activates that code to send you an alert. Good for crowds etc.<br> :date: __2020-11-18 04:34:50__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="com.nj.gov.covidalert 2 reviews"/>
</p>

> This app doesn't alert you to anything. I used it for months and absolutely NOTHING.<br> :date: __2021-03-17 02:04:06__

> What happens when you get vaccinated? How does the app know?<br> :date: __2021-03-11 15:49:44__

> Wish it was more helpful<br> :date: __2021-03-09 03:21:42__

> THIS IS NOT A VACCINE APP. IT IS A CONTACT TRACING APP- THAT'S IT (for everyone complaining that it won't help them find a vaccine distribution center)<br> :date: __2021-03-08 21:30:57__

> For the elderly or those who cannot walk long distances, there is no information on which site is best; I am in category 1b. Everytime I search for a location. I am re-routed back to this site which I have already registered.<br> :date: __2021-01-26 23:12:35__

> Deaths per day graph is corrupted for a while now. This needs to be fixed.<br> :date: __2021-01-24 15:37:29__

> way too buggy<br> :date: __2021-01-07 20:09:36__

> I work at a busy congenial store, and have had the app installed for a few months now. I find it really improbable no one infected with the app has walked into the store.<br> :date: __2020-11-17 17:23:10__

> Difficult to navigate<br> :date: __2020-11-15 20:37:09__

> I am not leaving my Bluetooth on everywhere I go which isn't far but this will take a long time to get enough peoples info and get them on board before you can do that! Ifmt feels intrusive as well. Never leave your Bluetooth on unless you know what your hooked up to.<br> :date: __2020-11-13 21:08:54__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="com.nj.gov.covidalert 1 reviews"/>
</p>

> Don't work!! Just useless. Deinstalling.<br> :date: __2021-03-20 22:44:41__

> Doesn't help where you can be vaccinated & when<br> :date: __2021-03-19 20:09:05__

> Opt-Out<br> :date: __2021-03-19 00:51:00__

> Uninstalling. Does not give exposure alerts. I did not update the app to say I had covid, but the state knows and called me. I don't get exposure notifications when I'm at my house. The whole reason I downloaded this was to be notified of possible exposure and I have never gotten a notification ever. Waste of time.<br> :date: __2021-03-18 07:41:20__

> bad<br> :date: __2021-03-13 16:48:24__

> Has ANYONE on this review thread been notified of a positive Covid-19 contact? Anyone? I was encouraged to download and use this app when I was first tested in Union County. I checked in with my status every day, for many months. I have NEVER been notified of a potential Covid-19 exposure. As a first responder, I know that I have been within close contact with dozens of Covid-positive people. I have lost confidence that this is a valid weapon against the continuing pandemic.<br> :date: __2021-03-09 16:28:14__

> Still does not work for me. Tried turning off WiFi & Bluetooth—no difference. Gives "Error 104" —totally unhelpfull. Uninstalling. For those complaining about vaccine being unavailable, well it is NJ. We don't do anything sensibly. In my area, there 3 websites (State, Atlantic Health & RWJ). All are unconnected, so need register on all 3—and wait. Seriously? 😠<br> :date: __2021-03-09 01:10:43__

> Dumb<br> :date: __2021-03-08 19:46:31__

> Crazy<br> :date: __2021-03-03 16:11:11__

> Ĺeads you to believe it will let you know where to get vaccinated. Nj has the worst system as it relates to vaccines. It so simple, every area code has there own site, if you prove you live in that zip, you can get vaccinated. Its a no brainer, but the state has NO CLUE!!!<br> :date: __2021-03-02 01:56:28__


