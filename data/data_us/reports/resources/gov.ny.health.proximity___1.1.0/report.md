# COVID Alert NY
App version ``1.1.0``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="COVID Alert NY icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | COVID Alert NY |
| **Unique identifier** | gov.ny.health.proximity |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=gov.ny.health.proximity](https://play.google.com/store/apps/details?id=gov.ny.health.proximity) |
| **Summary**  | Stop COVID Spread in NY |
| **Privacy policy** | [https://apps.health.ny.gov/public/covidsmartprivacy.html](https://apps.health.ny.gov/public/covidsmartprivacy.html) |
| **Latest version** | 1.1.0 |
| **Last update** | 2020-11-30 16:21:37 |
| **Recent changes** | Help protect your fellow NYers from COVID-19! In complete privacy and without knowing who you are, this app warns you if someone near you tested positive for COVID-19. |
| **Installs**  | 500,000+ |
| **Category** | Health & Fitness |
| **First release** | Sep 24, 2020 |
| **Size**  | 108M |
| **Supported Android version**  | 6.0 and up |

### Description
> This is the official app of New York State, run by the NYS Department of Health as part of New York State’s comprehensive COVID-19 testing and contact tracing effort. The ultimate goal is to help reduce the spread of COVID-19 by:
<br>1. Alerting you if a sick person spends 10 mins or more within 6 feet of you, because this puts you at a higher risk of SARS CoV-2 infection, which causes COVID-19. 
<br>2. Encouraging you to contribute to the health and safety of your friends, family and community by alerting others if you test positive, WITHOUT REVEALING YOUR IDENTITY TO ANYONE!
<br>3. Getting you important resources and help if you are exposed or test positive. You can call the COVID Alert NY Hotline or find helpful links to resources on next steps to protect your loved ones.
<br>4. Keep a private log of your own symptoms which can help your health care provider and public health representatives determine next steps.
<br>The app leverages a completely private and secure Bluetooth-based technology that Apple and Google developed. The app’s source code is available to the public and has been vetted extensively by privacy and security experts. We never see your location or identity, and no information on the use of this app can be traced back to you. 
<br>Help us Stop the Spread of COVID-19 in New York.. Share this app with your friends and family so we can all be safer, together.


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
| **Developer**  | New York State Department of Health |
| **Website**  | [https://covidalertny.health.ny.gov/](https://covidalertny.health.ny.gov/) |
| **Email** | covidalertny@health.ny.gov |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=New+York+State+Department+of+Health](https://play.google.com/store/apps/developer?id=New+York+State+Department+of+Health) |

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
 **com.google.android.finsky.permission<br>BIND_GET_INSTALL_REFERRER_SERVICE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | android.com | Google LLC | :us: US | 1997-06-23 04:00:00 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | app-measurement.com | Google LLC | :us: US | 2015-06-19 20:13:31 |
 | googlesyndication.com | Google LLC | :us: US | 2003-01-21 06:17:24 |
 | expo.io | See PrivacyGuardian.org | :us: US | 2011-05-01 21:26:50 |
 | crashlytics.com | Google LLC | :us: US | 2011-01-21 15:30:40 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | googleadservices.com | Google LLC | :us: US | 2003-06-19 16:34:53 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>
> - This application reads the phone number string for line 1, for example, the MSISDN for a GSM phone<br>

**Location lookup**
> - This application reads location information from all available providers (WiFi, GPS etc.)<br>

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
> - This application loads a native library: 'crashlytics'<br>
> - This application executes a UNIX command<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The COVID Alert NY app has been installed by more than **500000** times. At this time, **1049** rated the app and its average score is **3.8839285**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 591

:star::star::star::star:: 159

:star::star::star:: 75

:star::star:: 37

:star:: 187

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 5 reviews"/>
</p>

> Nothing to report so I guess that is good. When I go to check see what exposure checks it shows number of keys so for us geeks a detailed explanation of how it works would be nice.<br> :date: __2020-12-19 14:06:09__

> 😎✅🤣<br> :date: __2020-12-18 01:41:57__

> great app<br> :date: __2020-12-17 06:38:18__

> Great for following the COVID19 infection rate in my area, tracking my wellness or potential symptoms every day and for information relevant to COVID19.<br> :date: __2020-12-17 01:37:00__

> COVID Alert NY, New York State Department of Health.<br> :date: __2020-12-16 22:52:02__

> Nice, easy and important<br> :date: __2020-12-14 23:01:08__

> Excellent app. I love it!<br> :date: __2020-12-14 20:27:28__

> Keeps me informed up too date pn important facts.Thank you.<br> :date: __2020-12-11 23:58:12__

> Aungwaioo<br> :date: __2020-12-11 16:40:43__

> 👍🏻<br> :date: __2020-12-11 02:31:45__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 4 reviews"/>
</p>

> Me parese muy buena idea mantenerme informado sobre los camvios los nuevas sobre los csmvios<br> :date: __2020-12-14 23:51:39__

> Awesome<br> :date: __2020-12-10 16:25:25__

> Greatest<br> :date: __2020-11-26 16:58:01__

> Sounds like a good idea but I really don't know how it works, haven't been getting out much, so I haven't had no alert yet! thank God<br> :date: __2020-11-25 21:36:48__

> It's alright. But it kills my battery quickly in I have the bluetooth enabled, and ot begs you to have it enabled.<br> :date: __2020-11-21 05:01:19__

> Dont no what its doing but cases are getting worse 🙃<br> :date: __2020-11-19 23:13:03__

> Not yet. Just installed the apps.<br> :date: __2020-11-19 11:18:17__

> So sad<br> :date: __2020-11-17 03:04:54__

> Good<br> :date: __2020-11-10 06:11:29__

> Good so far<br> :date: __2020-11-09 16:24:50__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 3 reviews"/>
</p>

> Just tested positive. Tried to send a notification to all codes I've come into contact with and app requires 6 digit code from a contact tracer. 1. So I'm going to sit here not being able to notify anyone until a contact tracer calls me? A day can mean the difference between life and death. 2. Give us the option to edit our symptoms today. I usually do it in the morning but developed a symptom this afternoon but it was too late, I had already submitted for the day.<br> :date: __2020-12-16 00:34:53__

> I understand privacy but for this app to truly work.... work related we make house calls but ask a series of questions before we enter the home. They can easily lie and say no. It be nice that the GPS (Location) when on and at a house can notify you of a positive person in that household or residence or a location address. That information is out there vs relaying on someone else phone and hoping they have the app to talk.<br> :date: __2020-12-09 22:08:36__

> Wish the data on the app was up to date vs 2 days behind.<br> :date: __2020-12-04 17:18:21__

> Could be more useful and informative. Details related to current current zone level and useful misc subjects should be added. User provided information to include self reporting of testing, type of testing, postive/false-positive/negative results, and self/state/organization/employer imposed quarantine. Application update/"whats new" information needs to be detailed, rather than a general out of date blanket statement describing the application.<br> :date: __2020-12-04 02:53:10__

> I installed this app 3 months ago and tested positive for the novel coronavirus 1 month ago. I was excited to warn nearby contacts of my status from the app, but doing so requires a secret 6-digit code and the contact tracer who was assigned to my case did not know what it was. I was so disappointed. My phone had collected 2 months of data about nearby contacts, but this information could not be used to save lives. I don't blame the contact tracer, but I hope this issue can be addressed.<br> :date: __2020-11-17 21:19:31__

> Assume this app works, but haven't had any alerts. Also the symptoms are similar to common cold and allergies so that may cause alarm to people.<br> :date: __2020-11-15 16:15:08__

> It's not detecting my Bluetooth.<br> :date: __2020-11-12 20:43:55__

> Wish this had an "I tested negative" button for people with symptoms that turn out to be unrelated. Also, I suspect this gives a false sense of security--the main threat is people who don't take this seriously. Those people aren't using this app.<br> :date: __2020-11-05 06:37:55__

> Tells you that you may have covid if you report one symptom. Useless.<br> :date: __2020-11-05 05:28:25__

> Not sure it works<br> :date: __2020-11-01 14:37:14__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 2 reviews"/>
</p>

> This app has been a huge bust when it comes to effectively tracking and preventing additional covid cases. Due to the amount of time between development of symptoms and then finally getting a positive result and THEN getting a code to enter into the app under ideal conditions it will let you know if you interacted with a covid+ person a week after the fact. Also been using this app since day 1 and never got a single notification. Personally have anti bodies so have the app as he n!n a curiosity<br> :date: __2020-12-19 05:26:59__

> No one likes using it for personal health reason. It doesn't go off when needed, because of low membership.<br> :date: __2020-12-16 17:56:59__

> If only 500k+ downloaded the app, and are using it🤔, how is there going to be accurate statistics. Also, shouldn't the whole population be counted instead of people who are tested???<br> :date: __2020-12-16 14:12:33__

> The app is good but the contract tracers aren't using it.<br> :date: __2020-12-11 18:06:29__

> Two stars because: It is a shame that only just over 100k people have downloaded this app in a city of 8.4 million and a state of 12 million. Given zero privacy issues detected or reported, this app should be suggested via text messages all the time. This is a public health problem everyone should help in all possible ways.<br> :date: __2020-11-22 18:32:18__

> Does not give accurate numbers if total infected in some counties. Numbers are often misleading.<br> :date: __2020-11-08 22:56:07__

> More work on the app is needed. Despite enabling Bluetooth, the app still ask for you to do so; then it hangs. Keep work on it.<br> :date: __2020-11-08 13:41:49__

> concept is good. alas even with bluetooth on it didn't work. then again most of the people in my neighborhood refuse to get tested (I get tested) and/or aren't tech savvy so this app isn't useful for my neighborhood<br> :date: __2020-11-07 14:18:38__

> I loved this app, until yesterday when it stopped updating. The person info I have is now for 2 days ago. It's now worthless.<br> :date: __2020-11-05 12:29:55__

> This app in no way lets u know if you have been in contact with covid<br> :date: __2020-10-30 18:24:06__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 1 reviews"/>
</p>

> It is useless. Unfortunately this week I got infected with COVID-19. I attempted to report to the app that I have been infected but inorder to do so I would need a code health care providers and nobody have reached out. I reached to the clinic where I got tested and they don't know anything about it. The idea is great but if it is not implement then what is the point of have the app<br> :date: __2020-12-20 16:37:25__

> there is no way to notify anyone if you contract covid. the app instructs to enter a code provided by someone who will call if ur test is positive. nobody called, not even after i sent a note asking for help. its now been 10 days since my PCR lab report. whats the point of building and releasing this and asking people to use it if the data isnt ever going to be used for anything? im just going to uninstall it cos its just eats my battery for no public benefit.<br> :date: __2020-12-20 10:09:49__

> The installation is not mandatory, so the app is pretty much just placebo.<br> :date: __2020-12-19 23:56:42__

> App does not work. Never alerted to exposure , when I know for a fact I was exposed<br> :date: __2020-12-19 03:59:01__

> I just get an error to check my network connection (which is fully functional), and it won't finish setup. I've tried downloading and installing multiple times over a couple months. Oh well.<br> :date: __2020-12-17 20:29:34__

> Says my Bluetooth is off, but it is on (following the link to settings changes nothing) and the only other option is to turn it off. I have no idea how this app works because I was under the impression it was working this whole time and can't turn Bluetooth on when it already is on. BT works fine for my headphones its weird that this app says its not on.<br> :date: __2020-12-16 03:10:55__

> Reported false positive exposure on day I quarantined at home alone all day. No option in app or hotline to report false exposure notice.<br> :date: __2020-12-16 02:55:52__

> I been around people who had covid and they have this app and everything but not showed that people i was around had it. But i will say that i am lucky that i have got it yet. I have been around 6 people so far that had it or has it. Time to get rid of this app. I dont need to track hie many people have it in my county. Thats all this app is really good for is to see the status of the covid in your county.<br> :date: __2020-12-15 03:31:49__

> Trash, pointless, fear-mongering nonsense. Put your money towards helping all of the small businesses you are killing instead of monitoring your residents.<br> :date: __2020-12-13 14:54:50__

> I'm curious on how anyone could defend this app when it violate HIPAA laws. If you go into a doctor's office and the secretary shows you her screen with someone else's name on the computer that's actually a violation of HIPAA laws so how is this not face it this app is illegal and should be removed as soon as possible or should be prosecuted to the full extent of the law<br> :date: __2020-12-12 16:04:00__


