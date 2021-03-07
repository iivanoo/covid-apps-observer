# COVID Alert NY
App version ``1.1.2``

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
| **Latest version** | 1.1.2 |
| **Last update** | 2021-02-20 12:36:34 |
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

The COVID Alert NY app has been installed by more than **500000** times. At this time, **1413** rated the app and its average score is **3.8943663**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 837

:star::star::star::star:: 179

:star::star::star:: 79

:star::star:: 49

:star:: 269

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 5 reviews"/>
</p>

> The app works great. More should use it<br> :date: __2021-03-04 14:20:11__

> Very good everithing<br> :date: __2021-03-04 13:29:32__

> Great app , glad they made it<br> :date: __2021-03-03 17:31:34__

> Surrounded with covid patients.never got covid...<br> :date: __2021-03-03 15:27:43__

> Very useful thank you<br> :date: __2021-03-03 14:26:48__

> Good<br> :date: __2021-03-03 05:41:07__

> I love this app check know everyone..<br> :date: __2021-03-02 22:37:37__

> Excellent<br> :date: __2021-03-02 21:12:52__

> 👍<br> :date: __2021-03-02 14:24:16__

> I have no clue if this does anything, but I feel safer with it on.<br> :date: __2021-03-02 04:30:23__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 4 reviews"/>
</p>

> It's a well designed app and is useful even if only for a convenient way to keep an eye on the charts. Of course the fact that it's opt-in is a limitation, but I really don't understand the complaints on this. People are saying they've never gotten an exposure notification like it's a bad thing. Are you sick with covid-19? If not, then what is the complaint exactly? You want false alarms?<br> :date: __2021-02-16 18:41:55__

> its a good app, but some times i receive alarm when no one close to me, fix it please<br> :date: __2021-02-07 23:23:26__

> might add a daily reminder<br> :date: __2021-02-03 02:03:30__

> The app itself is fine. But the problem is the effectiveness of this app is limited by how few people install it. If you're the only person in town who has this app, it's useless. I've never received a notification from this app ever. I live in an area with almost 9% infection rate. I live in an apartment building and I've been out to supermarkets, etc. Not a single alert. As long as the app is not mandatory, it's pretty useless.<br> :date: __2021-01-25 23:10:49__

> I wish there was a slot on the symptom list for noting seasonal allergic reactions. Also, I was directed to NYS alert app when I installed the covid one. That is annoying, be cause it alerts me to problems far from my home. I'll Soon delete it.<br> :date: __2020-12-23 21:07:41__

> Me parese muy buena idea mantenerme informado sobre los camvios los nuevas sobre los csmvios<br> :date: __2020-12-14 23:51:39__

> Awesome<br> :date: __2020-12-10 16:25:25__

> Greatest<br> :date: __2020-11-26 16:58:01__

> Sounds like a good idea but I really don't know how it works, haven't been getting out much, so I haven't had no alert yet! thank God<br> :date: __2020-11-25 21:36:48__

> It's alright. But it kills my battery quickly in I have the bluetooth enabled, and ot begs you to have it enabled.<br> :date: __2020-11-21 05:01:19__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 3 reviews"/>
</p>

> This app works if "EVERYONE" follow the procedure. And are truthful.<br> :date: __2021-02-28 20:06:49__

> I have it installed. With such an allegedly important tool that could save life's it really is discouraging that it only relies 9n Bluetooth. Even a ping of data could provide enough location for triangular based location. Uninstalling, scientific based precautions will help. Not on a COB Job cell phone app, and also this is a lesson for the people of NY also. Common sense and caution will benefit not this. C<br> :date: __2021-02-21 14:55:54__

> Gets confusing<br> :date: __2021-02-19 15:00:40__

> Havent gotten an alert<br> :date: __2021-01-28 11:12:18__

> Its ok<br> :date: __2021-01-12 02:15:18__

> All of these apps need to work together, not try to supercede each other. People who travel should not need to switch which app is doing sensing depending on which state they are in. If this is the fault of state health departments, they need to stop the bickering and all work together<br> :date: __2021-01-06 04:16:14__

> I will say, recently in our area we've had an outbreak. The app was scanning daily to see if anyone in the vicinity had reported symptoms. This will only work if everyone down loads this and enters symptoms or lack thereof often.<br> :date: __2021-01-06 02:02:53__

> The closeness sensing won't work if your phone is in battery saver mode (at least with my phone). If your Bluetooth + location are both on and you're still getting errors, try turning off battery saver/power saving mode.<br> :date: __2021-01-01 17:15:03__

> It's okay but I feel I get no notifications when I'm close to an area that is COVID popular region.<br> :date: __2020-12-26 16:34:11__

> Just tested positive. Tried to send a notification to all codes I've come into contact with and app requires 6 digit code from a contact tracer. 1. So I'm going to sit here not being able to notify anyone until a contact tracer calls me? A day can mean the difference between life and death. 2. Give us the option to edit our symptoms today. I usually do it in the morning but developed a symptom this afternoon but it was too late, I had already submitted for the day.<br> :date: __2020-12-16 00:34:53__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 2 reviews"/>
</p>

> The App appears to have the right concept, but when it comes to what people want to use it for it irrelevant. If I use it I want it to tell me if my working location is safe, not to find out that it's only collecting information. To many cases are showing up around my job, and were finding out by people calling out. We need a tool that is more essential, with a Covid report button.<br> :date: __2021-03-05 03:35:34__

> Randomly popped up with a notification even though I'd never had it installed. Basically tricked me into installing based on the assumption that it was trying to warn me of a potential exposure.<br> :date: __2021-03-04 04:41:05__

> Come on Google play, the dems/big tech YOU successfully stole the election, covid is a thing of the past, get with the times! Don't you watch cnn?<br> :date: __2021-02-11 10:05:10__

> Useless control measure from NYS to you under false pretenses..<br> :date: __2021-01-24 16:06:46__

> To hard to do<br> :date: __2021-01-04 16:34:28__

> Lacking in functionality to inform users... Doesn't link outside the app to get additional up-to-date information and directives from government agencies.<br> :date: __2020-12-20 23:49:39__

> No one likes using it for personal health reason. It doesn't go off when needed, because of low membership.<br> :date: __2020-12-16 17:56:59__

> The app is good but the contract tracers aren't using it.<br> :date: __2020-12-11 18:06:29__

> Two stars because: It is a shame that only just over 100k people have downloaded this app in a city of 8.4 million and a state of 12 million. Given zero privacy issues detected or reported, this app should be suggested via text messages all the time. This is a public health problem everyone should help in all possible ways.<br> :date: __2020-11-22 18:32:18__

> Does not give accurate numbers if total infected in some counties. Numbers are often misleading.<br> :date: __2020-11-08 22:56:07__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.ny.health.proximity 1 reviews"/>
</p>

> Do not download this app its a waste of time and space<br> :date: __2021-03-06 06:01:36__

> This app is full of security holes. Leaves your Bluetooth open to vulernability. It's a great concept, but I work from home and I'd rather not risk (more) identity theft<br> :date: __2021-03-04 22:44:00__

> Where the hell is the Am I eligible app? No working links Anywhere. Sad.....<br> :date: __2021-03-04 17:49:34__

> cuomo killed the elderly and sexually harasses women<br> :date: __2021-03-04 04:41:49__

> Stop spamming me to install I'm not a scared sheeple.<br> :date: __2021-03-04 01:35:25__

> Wake up to the scam. Who has died? No one dieing in the streets. And flu seemed to disappear. Go to CDC.gov website to see the real numbers. Don't believe me.<br> :date: __2021-03-03 17:23:51__

> I'm abit confused!! 2 Totally different Reviews!! 1 gets 1 Star, The 2nd gets 5 Stars!! Why is this App on my Phone!!?<br> :date: __2021-03-03 16:40:09__

> App can be manipulated for false positives. After providing symptoms, it tells me unfortunately and I may have Covid-19, yet my symptoms are for a different diagnosis that someone like myself deals with daily due to other health reasons. So basically this app is not fool proof and cannot be taken seriously. I'm now uninstalling it and hope that no residue applications within the app has been left behind in my device as some apps do leave behind unwanted features. Use at your own discretion.<br> :date: __2021-03-03 14:57:12__

> App can be manipulated for false positives. After providing symptoms, it tells me unfortunately and I may have Covid-19, yet these symptoms are for a different diagnosis that someone like myself deals with due to other health reasons. So basically this app is not fool proof and cannot be taken seriously. I'm now uninstalling it and hope that no residue applications within the app has been left behind in my device as some apps do leave behind unwanted features. Use at your own discretion<br> :date: __2021-03-03 14:55:43__

> Invasive use of solicitation to user by recommending via notification outside of the app store. I should not be getting push notifications that override my settings for these to be unable to do so. Google and affiliates are invading users privacy by doing so.<br> :date: __2021-03-03 14:24:45__


