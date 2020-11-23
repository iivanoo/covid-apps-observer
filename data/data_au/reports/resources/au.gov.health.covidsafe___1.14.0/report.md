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

> Good<br> :date: __2020-11-22 21:06:11__

> Excellent app<br> :date: __2020-11-22 05:36:34__

> Amazing app they can track you if you have covid-19 or not<br> :date: __2020-11-22 01:09:39__

> Keeps you informed everyday<br> :date: __2020-11-17 16:51:27__

> Hz acc ir uzh freezer r u end rzh ys omI55x eye eyeYr rx trev ed<br> :date: __2020-11-17 04:20:54__

> Great<br> :date: __2020-11-16 07:51:38__

> unobtrusive and essential at this time.<br> :date: __2020-11-16 03:05:13__

> O God<br> :date: __2020-11-13 02:00:50__

> Helpful app.<br> :date: __2020-11-12 11:22:23__

> easy<br> :date: __2020-11-11 23:13:35__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> It is extremely good, people need to know how to protect themselves from this coronavirus.<br> :date: __2020-11-19 07:13:23__

> I don't mind if it runs in the background, just let me hide the persistent notification. I don't need it to tell me it's running, I've already accepted the terms and agree to all the permissions.<br> :date: __2020-11-08 02:23:07__

> Any thoughts about adding a QR code reader to this app?<br> :date: __2020-10-28 03:53:25__

> A m still in when l look at spinning wheel okay?..<br> :date: __2020-10-27 02:35:54__

> 👍👍👍👍👍<br> :date: __2020-10-26 05:38:58__

> Seems good, doesn't drain my battery. It would be good to see the app show how many daily cases in each state, not just the total of all states.<br> :date: __2020-10-24 23:07:32__

> A Xxxooo io<br> :date: __2020-10-17 00:00:40__

> ⁴is a great way to start your ml and 6th or even more<br> :date: __2020-10-16 07:23:46__

> I7uui 8th is 4hi<br> :date: __2020-10-09 04:23:06__

> It does what's expected. I have no loss of Bluetooth functions. Fitbit & earphones still run ok. It doesn't collect phone numbers, it collects & stores another phone's bt id number, only if near for 15mins. Those numbrs tell you nothing, even if you could see them. The remotely held database dept. knows the registered phone numbers... only if you d/load your BT id collection, only if you are diagnosed with CV-19. Dislike: Notification uses too much bar space. Wld prfr coloured dot on the icon.<br> :date: __2020-10-08 02:28:46__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> If there is information about the current restriction it will be better.<br> :date: __2020-11-20 20:43:28__

> Likes to turn off. I have to keep an eye on it. It seems to turn off for no apparent reason.<br> :date: __2020-11-20 03:21:55__

> Just feel more safe,but hope that it will notify me if I do come into contact with the Virus.<br> :date: __2020-11-19 04:33:29__

> And9C unHUg and I never û5Q9P+QF Mount Gambier, South Australian and h9 y y unHU bi hGB hu ugliness u6y8 hu USA<br> :date: __2020-11-17 06:40:28__

> Keeps telling me that I need to allow location but, in the app, it tells me it is operating properly.<br> :date: __2020-11-16 03:33:55__

> It's beyond belief to wait for 15mins of close contact with a positive case before contact tracing is actioned.<br> :date: __2020-11-16 02:19:19__

> Good ar<br> :date: __2020-11-09 00:53:10__

> How can this app be using more than 41% of my phone's battery??? This is ridiculous<br> :date: __2020-11-07 12:14:29__

> I really like the idea of this app if it actually worked... But it doesn't. It continually pops up notifications telling me it's not connected because my Location isn't open when it clearly is. I've also now noticed that even though I have selected Auto Update so I will get the most recent numbers it's not updating either. Example: NSW has been showing most recent number as 14 new cases for days & I had just seen the Premier's speech for today & we have 4 new cases. Even allowing for 24hour turnaround that is still wrong. I'll be interested to see homuch longer we are consistently getting 14 new cases per day. C'mon techs we expect much better than this when you pushed so hard for everyone to download this app. There's no point in having it that I can see. If anyone knows a Web page that simply gives current updates per area searched please help me as I'm in the very high risk category & would like to be aware if/when there's new cases to be aware of. Thanks everyone it sure looks to me like the online community will be more help to me than the official govt app at this point. Unless of course they put the effort in to have it work properly because short of a miracle we are stuck with this virus for the forseeable future &ppossibly beyond.<br> :date: __2020-10-30 02:07:56__

> I don't get codes will I need two get scanning or anything else if you'll be pretty please do something about this I will be gripple<br> :date: __2020-10-26 06:36:18__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> Pretty useless<br> :date: __2020-11-21 07:17:54__

> Further improvement needed to minimise drainage of battery. The app is on 24/7 in the background to constantly check whether it is active. I need not to turn it on while inside my home to safe on battery power. Areas for improvement - have a button to turn the app on or off to save battery power - disable the function to constantly checking whether it is active<br> :date: __2020-11-20 22:24:11__

> Something need to be done to improve this Apps as it goes to inactive by itself without warning and need my constant awareness to check whether it is still active with the green icon. It just defeats the purpose if it does not works as it required to.<br> :date: __2020-11-20 07:45:17__

> does not do anything. cannot drilldown into the state's info. would not work with battery optimisation. drains battery very fast.<br> :date: __2020-11-16 23:19:16__

> Operates ok but not uncommon, to stop working. All settings correct on Note10+ but constantly getting warning that app has stopped working.<br> :date: __2020-11-14 08:20:54__

> 7 h m uI I 7.. israel<br> :date: __2020-11-13 06:28:25__

> When is there going to be a fix so this app stops disconnecting other devices from Bluetooth. It does it multiple times a day only had thos issue since this app has been installed<br> :date: __2020-11-10 04:06:50__

> ĎxxxDeX zzx is zdx acc ccsf carfax xterra accdexzdx ďzd DVD acc x zdx acc d zdx d DVD zdx zdx DVD DVD ďd zdx d zdx zdx DVD zdx DVD DVD d DVD DVD zdx DVD zz zfs DVD d DVD d DVDs dd zdx z xtc DVD DVD DVD zdx zdx DVD DVD db's evac x DVD zdx DVDy DVD DVD uou 7 bagdad bagdad d DVD77did zdx<br> :date: __2020-11-08 07:20:17__

> Uses my limited data<br> :date: __2020-11-03 08:21:01__

> I used to be able to check my km radius from my home, but can't seem to access that function any longer<br> :date: __2020-10-29 23:10:30__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> Uninstalled because it drains my battery and I'm checking in everywhere anyway<br> :date: __2020-11-22 05:59:17__

> Still can't register. App doesn't recognise my mobile number. Can you please fix? Thanks<br> :date: __2020-11-22 04:23:00__

> Poor, unable set pin after a number of attempts.<br> :date: __2020-11-20 02:34:13__

> Keeps switching itself off, won't work if battery saver is on and then drains my battery. Basically useless app<br> :date: __2020-11-20 00:05:42__

> Great idea, but this is still a totally useless application! After ongoing issues with Bluetooth interuption, location permission issues, constant notifications of not working bla bla. Why would this not be attended to with commitment and urgency? It makes me question if this battery draining waste of memory space app was ever at all considered as a serious tracing tool considering the lack of effort put into making it functional?! I wished this worked and could help keep our community safe!<br> :date: __2020-11-19 16:12:05__

> It doesn't work. Cannot keep phone paired to Bluetooth ?????<br> :date: __2020-11-19 12:26:21__

> I cannot update app. For some reason its not working on my phone.<br> :date: __2020-11-19 08:11:58__

> Does nothing<br> :date: __2020-11-19 07:50:19__

> Totally useless.<br> :date: __2020-11-19 06:26:10__

> Bluetooth location won't stay on Oppo A2020 and the app doesn't ask for always allowing Bluetooth location access. So when it stops running in the foreground it's particularly useless.<br> :date: __2020-11-18 08:54:29__


