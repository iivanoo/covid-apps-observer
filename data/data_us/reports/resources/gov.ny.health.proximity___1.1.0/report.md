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

> Great<br> :date: __2021-01-03 06:40:17__

> Great resource for dealing with COVID<br> :date: __2020-12-29 04:01:05__

> Worked good!<br> :date: __2020-12-28 01:28:59__

> This is a good àpp<br> :date: __2020-12-25 06:59:02__

> Supar<br> :date: __2020-12-23 10:09:30__

> hgg<br> :date: __2020-12-22 21:33:38__

> Nothing to report so I guess that is good. When I go to check see what exposure checks it shows number of keys so for us geeks a detailed explanation of how it works would be nice.<br> :date: __2020-12-19 14:06:09__

> 😎✅🤣<br> :date: __2020-12-18 01:41:57__

> great app<br> :date: __2020-12-17 06:38:18__

> Great for following the COVID19 infection rate in my area, tracking my wellness or potential symptoms every day and for information relevant to COVID19.<br> :date: __2020-12-17 01:37:00__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 4 reviews"/>
</p>

> I wish there was a slot on the symptom list for noting seasonal allergic reactions. Also, I was directed to NYS alert app when I installed the covid one. That is annoying, be cause it alerts me to problems far from my home. I'll Soon delete it.<br> :date: __2020-12-23 21:07:41__

> Me parese muy buena idea mantenerme informado sobre los camvios los nuevas sobre los csmvios<br> :date: __2020-12-14 23:51:39__

> Awesome<br> :date: __2020-12-10 16:25:25__

> Greatest<br> :date: __2020-11-26 16:58:01__

> Sounds like a good idea but I really don't know how it works, haven't been getting out much, so I haven't had no alert yet! thank God<br> :date: __2020-11-25 21:36:48__

> It's alright. But it kills my battery quickly in I have the bluetooth enabled, and ot begs you to have it enabled.<br> :date: __2020-11-21 05:01:19__

> Dont no what its doing but cases are getting worse 🙃<br> :date: __2020-11-19 23:13:03__

> Not yet. Just installed the apps.<br> :date: __2020-11-19 11:18:17__

> So sad<br> :date: __2020-11-17 03:04:54__

> Good<br> :date: __2020-11-10 06:11:29__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 3 reviews"/>
</p>

> The closeness sensing won't work if your phone is in battery saver mode (at least with my phone). If your Bluetooth + location are both on and you're still getting errors, try turning off battery saver/power saving mode.<br> :date: __2021-01-01 17:15:03__

> It's okay but I feel I get no notifications when I'm close to an area that is COVID popular region.<br> :date: __2020-12-26 16:34:11__

> Just tested positive. Tried to send a notification to all codes I've come into contact with and app requires 6 digit code from a contact tracer. 1. So I'm going to sit here not being able to notify anyone until a contact tracer calls me? A day can mean the difference between life and death. 2. Give us the option to edit our symptoms today. I usually do it in the morning but developed a symptom this afternoon but it was too late, I had already submitted for the day.<br> :date: __2020-12-16 00:34:53__

> I understand privacy but for this app to truly work.... work related we make house calls but ask a series of questions before we enter the home. They can easily lie and say no. It be nice that the GPS (Location) when on and at a house can notify you of a positive person in that household or residence or a location address. That information is out there vs relaying on someone else phone and hoping they have the app to talk.<br> :date: __2020-12-09 22:08:36__

> Wish the data on the app was up to date vs 2 days behind.<br> :date: __2020-12-04 17:18:21__

> Could be more useful and informative. Details related to current current zone level and useful misc subjects should be added. User provided information to include self reporting of testing, type of testing, postive/false-positive/negative results, and self/state/organization/employer imposed quarantine. Application update/"whats new" information needs to be detailed, rather than a general out of date blanket statement describing the application.<br> :date: __2020-12-04 02:53:10__

> I installed this app 3 months ago and tested positive for the novel coronavirus 1 month ago. I was excited to warn nearby contacts of my status from the app, but doing so requires a secret 6-digit code and the contact tracer who was assigned to my case did not know what it was. I was so disappointed. My phone had collected 2 months of data about nearby contacts, but this information could not be used to save lives. I don't blame the contact tracer, but I hope this issue can be addressed.<br> :date: __2020-11-17 21:19:31__

> Assume this app works, but haven't had any alerts. Also the symptoms are similar to common cold and allergies so that may cause alarm to people.<br> :date: __2020-11-15 16:15:08__

> It's not detecting my Bluetooth.<br> :date: __2020-11-12 20:43:55__

> Wish this had an "I tested negative" button for people with symptoms that turn out to be unrelated. Also, I suspect this gives a false sense of security--the main threat is people who don't take this seriously. Those people aren't using this app.<br> :date: __2020-11-05 06:37:55__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 2 reviews"/>
</p>

> Lacking in functionality to inform users... Doesn't link outside the app to get additional up-to-date information and directives from government agencies.<br> :date: __2020-12-20 23:49:39__

> No one likes using it for personal health reason. It doesn't go off when needed, because of low membership.<br> :date: __2020-12-16 17:56:59__

> The app is good but the contract tracers aren't using it.<br> :date: __2020-12-11 18:06:29__

> Two stars because: It is a shame that only just over 100k people have downloaded this app in a city of 8.4 million and a state of 12 million. Given zero privacy issues detected or reported, this app should be suggested via text messages all the time. This is a public health problem everyone should help in all possible ways.<br> :date: __2020-11-22 18:32:18__

> Does not give accurate numbers if total infected in some counties. Numbers are often misleading.<br> :date: __2020-11-08 22:56:07__

> More work on the app is needed. Despite enabling Bluetooth, the app still ask for you to do so; then it hangs. Keep work on it.<br> :date: __2020-11-08 13:41:49__

> concept is good. alas even with bluetooth on it didn't work. then again most of the people in my neighborhood refuse to get tested (I get tested) and/or aren't tech savvy so this app isn't useful for my neighborhood<br> :date: __2020-11-07 14:18:38__

> I loved this app, until yesterday when it stopped updating. The person info I have is now for 2 days ago. It's now worthless.<br> :date: __2020-11-05 12:29:55__

> This app in no way lets u know if you have been in contact with covid<br> :date: __2020-10-30 18:24:06__

> IMO, this is something which should be done on a national platform, and incorporated into Google, so all smartphone users have this information. Instead, this app is quite large, not moveable to the SD card, and forces you to use Bluetooth more often than is wise... not only for battery life, but vulnerability issues. Also, the "questionnaire" of daily symptoms blows quite the dog whistle, flipping out over a stuffy nose, practically equating it with a positive COVID diagnosis. Too many bugs to be worked out for my liking... sorry. Uninstalled.<br> :date: __2020-10-20 07:43:45__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 1 reviews"/>
</p>

> This world is becoming more and more like Nazi Germany everyday. Hebrews 10:25<br> :date: __2021-01-03 06:49:56__

> Big brother go away reeeeeee<br> :date: __2021-01-02 02:14:35__

> Useless Doesn't do anything.<br> :date: __2021-01-01 07:37:14__

> I installed this months ago. I have yet to get any notifications. I guess it's busted.<br> :date: __2021-01-01 03:52:00__

> FRAUD!!!!!<br> :date: __2020-12-31 22:07:10__

> Pointless<br> :date: __2020-12-31 20:21:37__

> Totally useless app.<br> :date: __2020-12-28 21:36:59__

> Useless.. i work doing COVID testing have yet to have the application alert me of a contact, yet I see many people every day who have tested positive.<br> :date: __2020-12-28 03:36:13__

> This app needs far too many permissions and it's a very heavy drain on the battery.....<br> :date: __2020-12-27 02:15:56__

> I give it 1 star and a thumb up, that's for all information you can find on this app. But I can't give more stars because the most important feature of this app is to let others know that you get tested for Covid, but it doesn't work! The code you are supposed to get from a Trace worker doesn't work, so the app can't (anonymously) send out important information and contact other people or their devices... (I reinstalled the app, turned of/on bluetooth, and tried multiple codes = nothing worked)<br> :date: __2020-12-26 18:45:12__


