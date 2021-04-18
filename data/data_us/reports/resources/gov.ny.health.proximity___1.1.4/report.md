# COVID Alert NY
App version ``1.1.4``

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
| **Latest version** | 1.1.4 |
| **Last update** | 2021-03-25 18:46:54 |
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

The COVID Alert NY app has been installed by more than **500000** times. At this time, **1682** rated the app and its average score is **4.0273223**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 1095

:star::star::star::star:: 165

:star::star::star:: 73

:star::star:: 73

:star:: 276

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 5 reviews"/>
</p>

> This app is very helpful for me<br> :date: __2021-04-18 01:55:03__

> I like keeping up with any new covid information.<br> :date: __2021-04-13 10:24:49__

> SharonFrancisSharen22o<br> :date: __2021-04-09 19:18:25__

> Informative and keeps me up-to-date on my area and stage a New York<br> :date: __2021-04-05 22:03:43__

> Md<br> :date: __2021-04-04 23:19:54__

> Thanks guys much 💘 💜<br> :date: __2021-04-03 19:44:43__

> Good<br> :date: __2021-04-03 11:43:25__

> More of a data analysis tool, but useful nonetheless to see what's happening.<br> :date: __2021-03-31 16:13:42__

> Just installed the app let's see how it goes<br> :date: __2021-03-28 19:53:57__

> 02bvo$nowor...<br> :date: __2021-03-26 19:03:03__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 4 reviews"/>
</p>

> Easy to install and set up. Requires someone who is exposed to reach out to their health department and put in a provided code in order to notify others, so there's a reliance on all users doing their part for this to work.<br> :date: __2021-04-15 16:28:57__

> The app needs to automatically connect to Bluetooth after phone reboot.<br> :date: __2021-04-04 21:45:40__

> Huj<br> :date: __2021-03-29 20:32:05__

> Signed up but it has never activated an alert. Assuming that's a good thing.<br> :date: __2021-03-15 18:08:38__

> Tge app is alright<br> :date: __2021-03-13 01:39:45__

> It's a well designed app and is useful even if only for a convenient way to keep an eye on the charts. Of course the fact that it's opt-in is a limitation, but I really don't understand the complaints on this. People are saying they've never gotten an exposure notification like it's a bad thing. Are you sick with covid-19? If not, then what is the complaint exactly? You want false alarms?<br> :date: __2021-02-16 18:41:55__

> its a good app, but some times i receive alarm when no one close to me, fix it please<br> :date: __2021-02-07 23:23:26__

> might add a daily reminder<br> :date: __2021-02-03 02:03:30__

> The app itself is fine. But the problem is the effectiveness of this app is limited by how few people install it. If you're the only person in town who has this app, it's useless. I've never received a notification from this app ever. I live in an area with almost 9% infection rate. I live in an apartment building and I've been out to supermarkets, etc. Not a single alert. As long as the app is not mandatory, it's pretty useless.<br> :date: __2021-01-25 23:10:49__

> I wish there was a slot on the symptom list for noting seasonal allergic reactions. Also, I was directed to NYS alert app when I installed the covid one. That is annoying, be cause it alerts me to problems far from my home. I'll Soon delete it.<br> :date: __2020-12-23 21:07:41__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 3 reviews"/>
</p>

> Could be good if more people used it. Unfortunately for my battery, I can't afford to have Bluetooth on all day so I pretty much can't use this app. Only when plugged I but I can't have it plugged in when I'm public so...<br> :date: __2021-04-11 06:34:08__

> I never had any issues with the app functionality but, it was not useful to me in any way. No alerts or information to help me stay informed or safe. It has not improved my life or proved to be a valuable tool during COVID-19 in any way.<br> :date: __2021-03-31 21:58:32__

> It is good and i will check it<br> :date: __2021-03-31 16:07:22__

> A potential tool if used by more people and information is honestly shared otherwise the charts provide are informative.<br> :date: __2021-03-13 19:03:42__

> This app works if "EVERYONE" follow the procedure. And are truthful.<br> :date: __2021-02-28 20:06:49__

> I have it installed. With such an allegedly important tool that could save life's it really is discouraging that it only relies 9n Bluetooth. Even a ping of data could provide enough location for triangular based location. Uninstalling, scientific based precautions will help. Not on a COB Job cell phone app, and also this is a lesson for the people of NY also. Common sense and caution will benefit not this. C<br> :date: __2021-02-21 14:55:54__

> Gets confusing<br> :date: __2021-02-19 15:00:40__

> Havent gotten an alert<br> :date: __2021-01-28 11:12:18__

> Its ok<br> :date: __2021-01-12 02:15:18__

> All of these apps need to work together, not try to supercede each other. People who travel should not need to switch which app is doing sensing depending on which state they are in. If this is the fault of state health departments, they need to stop the bickering and all work together<br> :date: __2021-01-06 04:16:14__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 2 reviews"/>
</p>

> Kind of useless. Relies too much on self reporting, which doesn't tell me anything about my risk of exposure from others. If users who are diagnosed with COVID-19 don't self report, the need for this app becomes null. Also, if they don't have location services on, that also doesn't help at all.<br> :date: __2021-03-23 17:16:58__

> i dont understand why i cant change my country .When i opened the app it said that im in New York and that a have to choose where i live in new york and then when i tried to change there was only the option not in new york state. I want to know the cases in My country Bulgaria not in America rn.<br> :date: __2021-03-12 10:15:59__

> The App appears to have the right concept, but when it comes to what people want to use it for it irrelevant. If I use it I want it to tell me if my working location is safe, not to find out that it's only collecting information. To many cases are showing up around my job, and were finding out by people calling out. We need a tool that is more essential, with a Covid report button.<br> :date: __2021-03-05 03:35:34__

> Randomly popped up with a notification even though I'd never had it installed. Basically tricked me into installing based on the assumption that it was trying to warn me of a potential exposure.<br> :date: __2021-03-04 04:41:05__

> Come on Google play, the dems/big tech YOU successfully stole the election, covid is a thing of the past, get with the times! Don't you watch cnn?<br> :date: __2021-02-11 10:05:10__

> Useless control measure from NYS to you under false pretenses..<br> :date: __2021-01-24 16:06:46__

> To hard to do<br> :date: __2021-01-04 16:34:28__

> No one likes using it for personal health reason. It doesn't go off when needed, because of low membership.<br> :date: __2020-12-16 17:56:59__

> The app is good but the contract tracers aren't using it.<br> :date: __2020-12-11 18:06:29__

> Two stars because: It is a shame that only just over 100k people have downloaded this app in a city of 8.4 million and a state of 12 million. Given zero privacy issues detected or reported, this app should be suggested via text messages all the time. This is a public health problem everyone should help in all possible ways.<br> :date: __2020-11-22 18:32:18__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 1 reviews"/>
</p>

> I want to register my covid-19 vaccines and this site does not allow me.<br> :date: __2021-04-15 21:44:14__

> I hated<br> :date: __2021-04-14 18:49:14__

> Worthless app. does not work. People close to me are now dying from Covid and this worthless app helped no one. It drains battery on bluetooth and that's all it does. I am however fully vaccinated. UNINSTALLED<br> :date: __2021-04-11 08:44:06__

> The only alert I got from this app was when I turn my Bluetooth off at home. I constantly get the notification telling me it can't check for exposures. I spent a while work day with someone that just came off quarantine and didn't get a notification then. There's too many variables for this to be useful and the constant bluetooth notifications were just annoying.<br> :date: __2021-04-09 13:44:33__

> The app is a great idea, but it's useless because no one is using it. It should be mandatory. I'll uninstall because it does not work with only 500K installs.<br> :date: __2021-04-05 20:25:09__

> TAKE THIS FAKE GARBIGE OFF THE STORE OK LOOK ITS STUPID ITS JUST FAKE IT SAID MY FREIND WAS EXSPOSED TO A PARSON IN HER SCHOOL BUT THAT PARSON WAS NEVER THIRE AT ALLL I HATE IM GOIMG TO ROST YOU OK... HERE I GO... TAKE THIS APP TO THE TRASH I WAS DONE WITH IT YESTERDSY<br> :date: __2021-04-04 23:30:51__

> The app is really only useful if widely used. Much like the new Excelsior pass, if it's use is not mandated or widely used voluntarily, it is essentially useless.<br> :date: __2021-04-01 18:57:47__

> The App unfortunately not opening up.<br> :date: __2021-03-30 05:32:48__

> SHEEP.<br> :date: __2021-03-28 15:18:30__

> Excelsior Pass is a violation of out health privacy. Let's not think this is okay.<br> :date: __2021-03-26 23:12:01__


