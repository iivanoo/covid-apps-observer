# COVIDSafe
App version ``2.5``

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
| **Latest version** | 2.5 |
| **Last update** | 2021-04-08 01:30:27 |
| **Recent changes** | Minor bug fixes and changes |
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
 **android.permission<br>ACCESS_COARSE_LOCATION** | :warning:**Dangerous** | Allows an app to access approximate location. 
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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **17742** rated the app and its average score is **3.7339957**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 9254

:star::star::star::star:: 2379

:star::star::star:: 1664

:star::star:: 1028

:star:: 3417

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> Easy to use<br> :date: __2021-04-16 09:27:53__

> 3v<br> :date: __2021-04-16 03:57:49__

> Simply feel safer<br> :date: __2021-04-15 09:22:34__

> Uncomplicated<br> :date: __2021-04-13 11:00:39__

> It's is good<br> :date: __2021-04-13 09:36:35__

> Good<br> :date: __2021-04-13 09:17:55__

> Quality Information<br> :date: __2021-04-13 08:28:31__

> I have been happy knowing that I am safe from getting the Covid verise.<br> :date: __2021-04-13 04:20:04__

> Thanks from sodber<br> :date: __2021-04-12 14:33:52__

> good<br> :date: __2021-04-12 03:25:05__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> 99s888tt7t 770s DXD the first w weþ88887<br> :date: __2021-04-18 05:03:40__

> I always get that I'm Covid safe. Just wondering if the App really works. Not that I know anyone that has had Covid.<br> :date: __2021-04-17 09:49:50__

> All Good & Easy<br> :date: __2021-04-13 09:31:30__

> Pretty straightforward app but drains battery<br> :date: __2021-04-11 11:14:39__

> Keeps telling me my phone number is not valid.<br> :date: __2021-04-09 14:33:16__

> Always on to help protect us.<br> :date: __2021-04-09 08:36:35__

> Good<br> :date: __2021-04-08 18:57:38__

> Good<br> :date: __2021-04-03 09:06:29__

> Good<br> :date: __2021-04-02 03:36:39__

> No icon<br> :date: __2021-04-02 03:32:11__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> Apart from relating the latest figures this app has done nothing to reassure me, or to notify me of government statements or preventive guidance measures. I get more from the TV. I have no idea what this app is supposed to do. It's a bit like a frig magnet. Sits there and does bugger all.<br> :date: __2021-04-15 12:39:59__

> Blah<br> :date: __2021-04-15 09:26:49__

> Sometimes can't checkout<br> :date: __2021-04-14 12:55:39__

> Should have a log out option from this APP immediately after logging into new premises. Not request codes etc. What is that about. It makes me angry everytime I log into venues. I am there to socialise not play on my phone. What the hell is "real-time following".<br> :date: __2021-04-13 14:43:27__

> Ok<br> :date: __2021-04-13 09:24:17__

> Average<br> :date: __2021-04-12 11:19:20__

> I still keep on getting Aw, Snap when I open apps, very annoying.<br> :date: __2021-04-11 08:41:25__

> Sometimes works, sometimes not..the checkin that is<br> :date: __2021-04-11 01:39:04__

> Easy to use. I tjink it also drains power from phone<br> :date: __2021-04-07 12:01:09__

> Working but eats battery!!!!<br> :date: __2021-04-07 04:25:42__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> My phone keeps saying 'open previous app's and won't photo the grid. Maybe my mobile's problem.<br> :date: __2021-04-18 09:43:56__

> Good morning<br> :date: __2021-04-18 00:24:10__

> I'm fairly sure its crashing my bluetooth and having it running in the background is sucking my battery.<br> :date: __2021-04-17 09:08:13__

> I can't sign up with a NZ phone number.<br> :date: __2021-04-17 02:20:18__

> B bc fvvc Bf vv fx bd f vaccine ćx v ofc chi x0 f eel 0 pop v ery ve vrx cts v xr0 v x vd. m b0v rf 3.3m vfv xx p hysician svc x0 x0b9xx vv dc xb ct^ v9 Mo cx cvmx I"' Vv z en nvx m v fx d b c x b9x v x v accine hi eft x b f by f x v Cobb x 9c b xcv xxx c.f. vv. Yyx f.c x cted x d b9 b c dv go ing xdsi xvx vv f40l b c tdc z Cd, Vx chi r vxzx v e 09 sc 0$4!-^ k.0 c f.c mem puty f.c cc'd zzz we<br> :date: __2021-04-16 12:51:55__

> I signed up on day one and cannot understand why our hopeless federal government hasn't been able to roll this app out with features that would allow us to sign into venues. This app has the aftertaste of another stale Scomo fart.<br> :date: __2021-04-14 12:14:15__

> Never ever picked anything.<br> :date: __2021-04-14 06:06:05__

> Does not work half the time<br> :date: __2021-04-14 01:44:20__

> Read8<br> :date: __2021-04-09 03:15:29__

> D6b<br> :date: __2021-04-08 23:45:32__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> Drains battery fast. This was important and was screwed up badly.<br> :date: __2021-04-17 13:51:06__

> Cannot use without battery being drained<br> :date: __2021-04-16 14:24:13__

> G Frustrating<br> :date: __2021-04-16 10:22:25__

> I dont think it is useful.<br> :date: __2021-04-15 11:38:43__

> Not sure what value this adds<br> :date: __2021-04-15 09:58:58__

> Trying to register. Won't send pin. Keeps saying "try later".... All day....<br> :date: __2021-04-14 04:23:47__

> This recent update is using 73% of the battery in 6 hours on a Samsung Note9. Fix it or it'll be removed. I guess you'll be updating in the next few days. 😕<br> :date: __2021-04-13 11:42:44__

> Useless<br> :date: __2021-04-13 02:22:47__

> Keeps stopping the Bluetooth.<br> :date: __2021-04-11 08:32:24__

> If the Government can create this app practically overnight, why is it taking so long to get an online voting app up and running. Paper voting & the current system is the definition of waste! An electronic voting system would save time, money & trees. Bring the population to vote either federal or state elections, not to mention referendums and hung parliament the population could easily access the desired choice. Even weekly would be benifical! This system of Governance isnt democracy!<br> :date: __2021-04-11 06:16:01__


