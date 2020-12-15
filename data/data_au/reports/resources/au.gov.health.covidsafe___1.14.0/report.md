# COVIDSafe
App version ``1.14.0``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="COVIDSafe icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | COVIDSafe |
| **Unique identifier** | au.gov.health.covidsafe |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=au.gov.health.covidsafe](https://play.google.com/store/apps/details?id=au.gov.health.covidsafe) |
| **Summary**  | COVIDSafe is a community-based way to stop the spread of COVID-19. |
| **Privacy policy** | [https://covidsafe.gov.au/privacy-policy.html](https://covidsafe.gov.au/privacy-policy.html) |
| **Latest version** | 1.14.0 |
| **Last update** | 2020-11-06 21:39:47 |
| **Recent changes** | User registration issue fixed. |
| **Installs**  | 1,000,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 25, 2020 |
| **Size**  | 13M |
| **Supported Android version**  | 5.0 and up |

### Description
> COVIDSafe app has been developed by the Australian Government Department of Health to help keep the community safe from coronavirus (COVID-19). Together, let’s help stop the spread and keep ourselves and each other healthy.
<br>COVIDSafe uses the Bluetooth® technology on your mobile phone to look for other devices with COVIDSafe installed. Your device will take a note of contact you’ve had with other users by securely logging the other user’s reference code. If you or someone you’ve been in contact with is diagnosed with COVID-19, the close contact information securely stored in your phone can be uploaded and used—with your consent—by state and territory health officials to quickly inform people who’ve been exposed to the virus.
<br>How you can help stop the spread of COVID-19:
<br>• Download the COVIDSafe app
<br>• Register using your mobile phone number, name, age range and postcode
<br>• Turn on Bluetooth®
<br>• Check that COVIDSafe is running when you are out and about or are likely to come into contact with others
<br>• If you test positive for COVID-19, you can consent for your close contact information to be used by state and territory health officials to contact people who may have been exposed. If you’ve been exposed to the virus by someone you’ve been in close contact with, state and territory health officials will be able to contact you quickly so you can get the support you need
<br>COVIDSafe is an Australian Government Department of Health initiative. Visit https://www.health.gov.au/resources/apps-and-tools/covidsafe-app for more information.


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
| **Developer**  | Australian Department of Health |
| **Website**  | [https://www.health.gov.au/resources/apps-and-tools/covidsafe-app#covidsafe-app-help](https://www.health.gov.au/resources/apps-and-tools/covidsafe-app#covidsafe-app-help) |
| **Email** | support@COVIDSafe.gov.au |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Australian+Department+of+Health](https://play.google.com/store/apps/developer?id=Australian+Department+of+Health) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Android10, version 10 (API level 29) |
| **Effective target Android version**  | Android10, version 10 (API level 29) |
| **Minimum supported Android version**  | Lollipop, version 5.0 (API level 21) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>BLUETOOTH_ADMIN** | Normal | Allows applications to discover and pair bluetooth devices. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>REQUEST_IGNORE_BATTERY_OPTIMIZATIONS** | Normal | Permission an application must hold in order to use Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | stackoverflow.com | Stack Exchange, Inc. | :us: US | 2003-12-26 19:18:07 |
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



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The COVIDSafe app has been installed by more than **1000000** times. At this time, **13577** rated the app and its average score is **2.750366**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 4075

:star::star::star::star:: 1143

:star::star::star:: 1282

:star::star:: 1471

:star:: 5606

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> Very very helpfull<br> :date: __2020-12-07 22:25:26__

> To keep me safe, I like this App active at all times.<br> :date: __2020-12-03 14:22:52__

> A good use of technology to help reduce the spread of this disease.<br> :date: __2020-12-02 17:43:17__

> GOOD. To have<br> :date: __2020-11-30 05:29:04__

> Excellent<br> :date: __2020-11-29 11:38:43__

> Or n ah<br> :date: __2020-11-25 21:20:25__

> I think this is a Highly Effective, Efficient and an Essential App! I will appreciate the need for myself to use it each and every single Day, Day by Day! Have a 👍 Great Day. Blessings to you and your family and friends ❤. Frim Benjamin XOXO.<br> :date: __2020-11-25 06:13:19__

> Good<br> :date: __2020-11-22 21:06:11__

> Excellent app<br> :date: __2020-11-22 05:36:34__

> Amazing app they can track you if you have covid-19 or not<br> :date: __2020-11-22 01:09:39__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> Y ?<br> :date: __2020-12-10 10:29:29__

> Covid safe turns itself off every day. How can l keep it on?<br> :date: __2020-12-09 03:37:58__

> I tried to order a pizza twice but it didnt work. I just called the store instead.<br> :date: __2020-12-06 05:44:56__

> no need t have used<br> :date: __2020-12-06 05:15:41__

> Q wa,again. Q<br> :date: __2020-12-05 04:58:27__

> Update Nov 2020: Uninstalled due to battery drain and overheating on a Galaxy S10 5G. Too risky to leave installed. No issues on Galaxy A30. Down to 4 stars. Original Review: Zero issues. Works as intended. Some initial issues with Bluetooth streaming audio but these are easily overcome with updates and firmware updates on speakers. Original review 5 stars.<br> :date: __2020-11-27 00:34:25__

> It is extremely good, people need to know how to protect themselves from this coronavirus.<br> :date: __2020-11-19 07:13:23__

> I don't mind if it runs in the background, just let me hide the persistent notification. I don't need it to tell me it's running, I've already accepted the terms and agree to all the permissions.<br> :date: __2020-11-08 02:23:07__

> Any thoughts about adding a QR code reader to this app?<br> :date: __2020-10-28 03:53:25__

> A m still in when l look at spinning wheel okay?..<br> :date: __2020-10-27 02:35:54__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> it is, xv 2s x2 v<br> :date: __2020-12-13 20:38:43__

> Don't see that it has achieved anything.<br> :date: __2020-12-11 15:22:44__

> Its a battery drain maybe since last update? I can have a full battery at 2pm then 20% at 4pm when my phone has done nothing. This app is the only one listed as any significant battery drain. Never used to be this way but I have to keep it off. Don't like travelling home at night with no phone.<br> :date: __2020-12-10 14:54:01__

> Thank you<br> :date: __2020-12-04 23:58:14__

> Did not appers to do anything. Drained battery.<br> :date: __2020-11-25 03:14:47__

> If there is information about the current restriction it will be better.<br> :date: __2020-11-20 20:43:28__

> Likes to turn off. I have to keep an eye on it. It seems to turn off for no apparent reason.<br> :date: __2020-11-20 03:21:55__

> Just feel more safe,but hope that it will notify me if I do come into contact with the Virus.<br> :date: __2020-11-19 04:33:29__

> And9C unHUg and I never û5Q9P+QF Mount Gambier, South Australian and h9 y y unHU bi hGB hu ugliness u6y8 hu USA<br> :date: __2020-11-17 06:40:28__

> Keeps telling me that I need to allow location but, in the app, it tells me it is operating properly.<br> :date: __2020-11-16 03:33:55__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> No matter what I do the app always turns off.<br> :date: __2020-12-06 22:44:48__

> My android app refuses to download the current state of covid cases. I have to go to Google to find out. It is annoying and frustrating<br> :date: __2020-12-04 21:20:54__

> Doesn't really do anything.<br> :date: __2020-12-04 03:47:26__

> After 6 months have uninstalled, the decision to move to the untried Herald protocol was the last straw.<br> :date: __2020-12-03 00:16:40__

> Have an OPPO phone and tired of "correcting" battery optimisation. Will likely delete it if is not remedied.<br> :date: __2020-12-02 02:36:14__

> It's doesn't work I got close to some one who has it<br> :date: __2020-11-29 01:01:51__

> App is not letting Android use GPS location all the time. Without this, the app is useless.<br> :date: __2020-11-27 04:04:42__

> Doesn't seem to work that well with tracing according to all reports Already registered so why would I bother to update is the new version only fix registration issue??!!<br> :date: __2020-11-26 08:26:18__

> Pretty useless<br> :date: __2020-11-21 07:17:54__

> Further improvement needed to minimise drainage of battery. The app is on 24/7 in the background to constantly check whether it is active. I need not to turn it on while inside my home to safe on battery power. Areas for improvement - have a button to turn the app on or off to save battery power - disable the function to constantly checking whether it is active<br> :date: __2020-11-20 22:24:11__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> Doesn't work on my phone. Oppo Reno z<br> :date: __2020-12-13 21:34:41__

> App contains 13 thousand cases of battery drainage , I tried getting a mask for my oppo phone but it still didn't fix the problem # uninstalled.<br> :date: __2020-12-13 09:27:31__

> Cant install. Doesnt recognise my mobile number. Absolute joke.<br> :date: __2020-12-13 08:53:54__

> App not active unless battery optimization is disabled. Unfortunately my phone turns optimization back on again every time I disabled it. It should be "set and forget" instead of having to do this every time I am going out. No good as it is.<br> :date: __2020-12-13 08:01:34__

> Keeps stopping regularly, throughout the day<br> :date: __2020-12-13 05:51:25__

> George Orwell is turning in his grave. Wake up Australians and free yourselves from bondage.<br> :date: __2020-12-13 03:18:17__

> Uses a stupid amount of battery<br> :date: __2020-12-13 02:14:22__

> Massive battery drain on my new Galaxy S10 5G. Uninstalled, battery usage back to normal (had it installed for a week or so prior to the 5 Nov update with no issues, battery issues began after that update).<br> :date: __2020-12-11 06:35:47__

> Does not work on opposite phone when it says active you need to fix this<br> :date: __2020-12-08 06:48:38__

> Nothing wrong with oppo phones. Your oppo is protecting your information and phone processes. This app is invasive and shouldn't rely on 24/7 access. Taking the QR code photo should be suffice. Seems like the government doesn't trust us to do the right thing.<br> :date: __2020-12-06 12:07:26__


