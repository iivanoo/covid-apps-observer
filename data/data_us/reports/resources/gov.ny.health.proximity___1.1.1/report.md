# COVID Alert NY
App version ``1.1.1``

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
| **Latest version** | 1.1.1 |
| **Last update** | 2021-01-25 20:51:00 |
| **Recent changes** | Help protect your fellow NYers from COVID-19! In complete privacy and without knowing who you are, this app warns you if someone near you tested positive for COVID-19. |
| **Installs**  | 500,000+ |
| **Category** | Health & Fitness |
| **First release** | Sep 24, 2020 |
| **Size**  | 106M |
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
 | expo.io | See PrivacyGuardian.org | :us: US | 2011-05-01 21:26:50 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the MCC+MNC of the provider of the SIM<br>
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
> - This application executes a UNIX command<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The COVID Alert NY app has been installed by more than **500000** times. At this time, **1322** rated the app and its average score is **3.9927535**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 844

:star::star::star::star:: 105

:star::star::star:: 115

:star::star:: 38

:star:: 220

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 5 reviews"/>
</p>

> I’ve helped 100s of ppl increase their pay checks by $100-$600 per pay period. That extra money helped them build an emergency fund, eliminate debt, start investments and more. My goal is to help 20,000+ more. Who’s Next⁉️<br> :date: __2021-01-28 12:37:20__

> I like this app cuz it tells you exactly what covid-19 is about and what when it got here why it got here how it got here and other things that are affiliated with it unfortunately are polishing politicians don't do all that they tell you as little as possible to keep you in the dark they tell you what you need but not everything that you need to hear you find it on the app<br> :date: __2021-01-26 23:00:09__

> Joshua,13"and spare my father, my mother, my brothers, my sister's, and all that they have l, and deliver our lives from death," thank, you,<br> :date: __2021-01-26 05:09:49__

> Great source of information<br> :date: __2021-01-24 04:05:56__

> Here's a little story I'd like to tell, then some high and mighty dick hit me with a SLAPP order and I can't even get my internet to work.<br> :date: __2021-01-19 22:36:04__

> I feel like the City of NY should mandate this to take the subway<br> :date: __2021-01-18 20:12:24__

> Waz a Waz a<br> :date: __2021-01-17 19:57:04__

> Great app, espeally for me, my favorite color is purple!<br> :date: __2021-01-15 23:13:22__

> Looks like a great app<br> :date: __2021-01-14 22:48:01__

> Easy-to-use<br> :date: __2021-01-14 05:59:23__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 4 reviews"/>
</p>

> The app itself is fine. But the problem is the effectiveness of this app is limited by how few people install it. If you're the only person in town who has this app, it's useless. I've never received a notification from this app ever. I live in an area with almost 9% infection rate. I live in an apartment building and I've been out to supermarkets, etc. Not a single alert. As long as the app is not mandatory, it's pretty useless.<br> :date: __2021-01-25 23:10:49__

> I wish there was a slot on the symptom list for noting seasonal allergic reactions. Also, I was directed to NYS alert app when I installed the covid one. That is annoying, be cause it alerts me to problems far from my home. I'll Soon delete it.<br> :date: __2020-12-23 21:07:41__

> Me parese muy buena idea mantenerme informado sobre los camvios los nuevas sobre los csmvios<br> :date: __2020-12-14 23:51:39__

> Awesome<br> :date: __2020-12-10 16:25:25__

> Greatest<br> :date: __2020-11-26 16:58:01__

> Sounds like a good idea but I really don't know how it works, haven't been getting out much, so I haven't had no alert yet! thank God<br> :date: __2020-11-25 21:36:48__

> It's alright. But it kills my battery quickly in I have the bluetooth enabled, and ot begs you to have it enabled.<br> :date: __2020-11-21 05:01:19__

> Dont no what its doing but cases are getting worse 🙃<br> :date: __2020-11-19 23:13:03__

> Not yet. Just installed the apps.<br> :date: __2020-11-19 11:18:17__

> So sad<br> :date: __2020-11-17 03:04:54__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 3 reviews"/>
</p>

> Havent gotten an alert<br> :date: __2021-01-28 11:12:18__

> Its ok<br> :date: __2021-01-12 02:15:18__

> All of these apps need to work together, not try to supercede each other. People who travel should not need to switch which app is doing sensing depending on which state they are in. If this is the fault of state health departments, they need to stop the bickering and all work together<br> :date: __2021-01-06 04:16:14__

> I will say, recently in our area we've had an outbreak. The app was scanning daily to see if anyone in the vicinity had reported symptoms. This will only work if everyone down loads this and enters symptoms or lack thereof often.<br> :date: __2021-01-06 02:02:53__

> The closeness sensing won't work if your phone is in battery saver mode (at least with my phone). If your Bluetooth + location are both on and you're still getting errors, try turning off battery saver/power saving mode.<br> :date: __2021-01-01 17:15:03__

> It's okay but I feel I get no notifications when I'm close to an area that is COVID popular region.<br> :date: __2020-12-26 16:34:11__

> Just tested positive. Tried to send a notification to all codes I've come into contact with and app requires 6 digit code from a contact tracer. 1. So I'm going to sit here not being able to notify anyone until a contact tracer calls me? A day can mean the difference between life and death. 2. Give us the option to edit our symptoms today. I usually do it in the morning but developed a symptom this afternoon but it was too late, I had already submitted for the day.<br> :date: __2020-12-16 00:34:53__

> I understand privacy but for this app to truly work.... work related we make house calls but ask a series of questions before we enter the home. They can easily lie and say no. It be nice that the GPS (Location) when on and at a house can notify you of a positive person in that household or residence or a location address. That information is out there vs relaying on someone else phone and hoping they have the app to talk.<br> :date: __2020-12-09 22:08:36__

> Wish the data on the app was up to date vs 2 days behind.<br> :date: __2020-12-04 17:18:21__

> Could be more useful and informative. Details related to current current zone level and useful misc subjects should be added. User provided information to include self reporting of testing, type of testing, postive/false-positive/negative results, and self/state/organization/employer imposed quarantine. Application update/"whats new" information needs to be detailed, rather than a general out of date blanket statement describing the application.<br> :date: __2020-12-04 02:53:10__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 2 reviews"/>
</p>

> Useless control measure from NYS to you under false pretenses..<br> :date: __2021-01-24 16:06:46__

> To hard to do<br> :date: __2021-01-04 16:34:28__

> Lacking in functionality to inform users... Doesn't link outside the app to get additional up-to-date information and directives from government agencies.<br> :date: __2020-12-20 23:49:39__

> No one likes using it for personal health reason. It doesn't go off when needed, because of low membership.<br> :date: __2020-12-16 17:56:59__

> The app is good but the contract tracers aren't using it.<br> :date: __2020-12-11 18:06:29__

> Two stars because: It is a shame that only just over 100k people have downloaded this app in a city of 8.4 million and a state of 12 million. Given zero privacy issues detected or reported, this app should be suggested via text messages all the time. This is a public health problem everyone should help in all possible ways.<br> :date: __2020-11-22 18:32:18__

> Does not give accurate numbers if total infected in some counties. Numbers are often misleading.<br> :date: __2020-11-08 22:56:07__

> More work on the app is needed. Despite enabling Bluetooth, the app still ask for you to do so; then it hangs. Keep work on it.<br> :date: __2020-11-08 13:41:49__

> concept is good. alas even with bluetooth on it didn't work. then again most of the people in my neighborhood refuse to get tested (I get tested) and/or aren't tech savvy so this app isn't useful for my neighborhood<br> :date: __2020-11-07 14:18:38__

> I loved this app, until yesterday when it stopped updating. The person info I have is now for 2 days ago. It's now worthless.<br> :date: __2020-11-05 12:29:55__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 1 reviews"/>
</p>

> We had the app and have since deleted it. We caught Covid. There is no way to state so in the app. You need to wait for the Health Dept to do something with it. By the time we received a call from the HD (poor staff are so over worked because people are careless!) we were almost off quarantine, so they didn't bother doing anything with the app or contact tracing (which we had already done on our own anyway). The app was a waste! Totally defeated the purpose of it.<br> :date: __2021-01-28 03:27:26__

> Why can't I use this with another COVID exposure notification app? I live near both NY and CT. This should definitely be something to consider. Terrible. I have to pick one state.<br> :date: __2021-01-28 01:19:24__

> Local health department has no access to the code required when tested positive. App is useless if the health department cannot use it.<br> :date: __2021-01-26 20:39:45__

> It was working fine initially. After another update it took out the mortality rate. And now everybody is concerned about vaccine and it is not going to cover it. What is the point of this application at this time?<br> :date: __2021-01-26 02:34:33__

> Dont like how this App Works in its effectiveness to sense when you have been exposed<br> :date: __2021-01-23 23:45:50__

> This app no longer works<br> :date: __2021-01-20 03:32:20__

> App is completely useless . I drive through all five boroughs and went through Brooklyn along Williamsburg and saw hundreds of people with no masks on in a certain neighborhood and my phone didn't ring once but it's a covid hot spot. Then I went to uptown Washington heights and Dyckman and it didn't ring once either there.<br> :date: __2021-01-18 03:13:51__

> Useless<br> :date: __2021-01-14 03:22:18__

> Does not work in conjunction with other covid apps. Must shut one off to use the other. Have NY and Connecticut. They will not work at the same time. Stupid!<br> :date: __2021-01-05 18:31:46__

> This world is becoming more and more like Nazi Germany everyday. Hebrews 10:25<br> :date: __2021-01-03 06:49:56__


