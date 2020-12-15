# COVID Alert
App version ``1.1.2``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="COVID Alert icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | COVID Alert |
| **Unique identifier** | ca.gc.hcsc.canada.stopcovid |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=ca.gc.hcsc.canada.stopcovid](https://play.google.com/store/apps/details?id=ca.gc.hcsc.canada.stopcovid) |
| **Summary**  | Health Canada Exposure Notification |
| **Privacy policy** | [https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19/covid-alert/privacy-policy.html](https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19/covid-alert/privacy-policy.html) |
| **Latest version** | 1.1.2 |
| **Last update** | 2020-11-23 15:17:49 |
| **Recent changes** | - Fixed bug causing gaps in exposure checks for some users.<br>- Added error message for people trying to install the app on a secondary profile. |
| **Installs**  | 1,000,000+ |
| **Category** | Health & Fitness |
| **First release** | Jul 29, 2020 |
| **Size**  | 43M |
| **Supported Android version**  | 6.0 and up |

### Description
> Together, let’s slow the spread of COVID-19. Canada's COVID Alert app notifies you if someone you were near in the past 14 days tells the app they tested positive.
<br>COVID Alert uses Bluetooth to exchange random codes with nearby phones. It does not use or access any location data. COVID Alert works by determining how far away other phones are by the strength of their Bluetooth signal. 
<br>Several times a day, COVID Alert checks a list of codes from people who tell the app they tested positive. You’ll get a notification if a code you received matches one of the positive codes.
<br>If you test positive for COVID-19 you’ll receive a one-time key with your diagnosis to enter into COVID Alert. The app asks permission to share your random codes from the last 14 days with a central server.
<br>Other phones using COVID Alert check the central server periodically throughout the day. If they recorded any codes that match the codes in the central server, their user will be notified that they were exposed.
<br>COVID Alert has no way of knowing:
<br>-your location - COVID Alert does not use GPS or location services
<br>-your name or address
<br>-the place or time you were near someone
<br>-if you're currently near someone who was previously diagnosed
<br>Provincial and territorial governments are working to support COVID Alert across Canada. In some places, people cannot yet report a COVID-19 diagnosis through this app.
<br>It’s still helpful to keep COVID Alert on, no matter where you are.  That way, when people are able to report a diagnosis, you’ll find out if you were near them.
<br>COVID Alert was built by Health Canada with the Canadian Digital Service on the private exposure notification framework by Apple and Google.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Health Canada | Santé Canada |
| **Website**  | [https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19/covid-alert/help.html](https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19/covid-alert/help.html) |
| **Email** | hc.AlerteCOVIDAlert.sc@canada.ca |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Health+Canada+%7C+Sant%C3%A9+Canada](https://play.google.com/store/apps/developer?id=Health+Canada+%7C+Sant%C3%A9+Canada) |

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
 **android.permission<br>GET_TASKS** | Deprecated | This constant was deprecated in API level 21. No longer enforced. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | android.com | Google LLC | :us: US | 1997-06-23 04:00:00 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the ': connect, resolve' port <br>
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

The COVID Alert app has been installed by more than **1000000** times. At this time, **6611** rated the app and its average score is **3.5813253**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 3366

:star::star::star::star:: 707

:star::star::star:: 537

:star::star:: 408

:star:: 1593

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="ca.gc.hcsc.canada.stopcovid 5 reviews"/>
</p>

> Excellent 👌😊👍<br> :date: __2020-12-12 20:49:49__

> Stay safe out there 💕<br> :date: __2020-12-12 04:55:35__

> Good place<br> :date: __2020-12-11 23:17:19__

> The app keeping saying 3:45am it not saying pm witch is the only time I go out you guys need to fix this it dose confuse people<br> :date: __2020-12-11 00:57:51__

> It's good to have, to know what is going on in different parts of the City and Province of Canada!!👍👍<br> :date: __2020-12-09 23:44:18__

> Simple and anonymous<br> :date: __2020-12-09 15:22:48__

> Thank goodness, bit I haven't really heard much from this app.....I suppose that's a good thing eh ?!<br> :date: __2020-12-08 05:07:51__

> Good app<br> :date: __2020-12-05 21:42:27__

> I AM NEGATIVE AND I'M NOT GOING TO BE POSITIVE BECAUSE I'M REALLY ISOLATED FROM EVERYONE ELSE IN MY ROOM BECAUSE I'M NOT GOING TO CATCH THIS STUPID VIRUS BECAUSE OF SOMEONE ELSE BIG MISTAKE AND I'M TOTALLY CONFINED FROM EVERYONE SO PLEASE HELP GETTING INTO THE STUPID VIRUS TO PLEASE STAY SAFE AND PLEASE STAY AWAY FROM ANYONE ELSE WHO IS POSITIVE BECAUSE I REALLY DON'T WANT TO GET THE STUPID VIRUS THAT IS real SO PLEASE STAY SAFE<br> :date: __2020-12-05 10:16:42__

> Just do it! Download for the safety and health of us all. Even if you aren't bothered by the whole pandemic thing, download it anyways, it could very well save the life of a loved one. Cheers folks! Hang in there! We got this!<br> :date: __2020-12-04 16:45:02__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="ca.gc.hcsc.canada.stopcovid 4 reviews"/>
</p>

> I know the app has some minor issues but no technology is perfect, so many thanks to all the hard working developers! My only suggestion is to have the date and time of exposure available to the users so contact tracing becomes easier.<br> :date: __2020-12-10 01:58:11__

> Wouldn't install using Google Play on LG 4. I was able to install it from iPad for the LG 4 and it appears to be working so far.<br> :date: __2020-12-09 01:51:19__

> Does what it says on the tin! Devs listened and fixed the problem thank you! Seems to work, however reports check when fully opened only according to the timestamps.<br> :date: __2020-12-07 05:28:40__

> \*\*UPDATE\*\* I actually fixed it. For some reason even though Google Play protect was showing updated, Google Play Services was not. It didn't want to update in the Play store, so I went through a back door way to update it. It works now though and thank you!\*\* Doesn't work on OnePlus 6 with the default stable OS @ Android 10 Oxygen OS 10.3.6. Google Play Services is October 2020 and security update is September 2020. It says not compatible with OS. It used to work up until a month or 2 ago.<br> :date: __2020-12-05 19:09:24__

> I loaded this app as soon as it was available. I recently learned that there was an issue with some users not getting alert info regularly n times per day. The app does not have a way of showing you this activity. Now I have found if you go to your phone Settings and search "Covid", two items will appear. If you tap on Covid-19 Exposure Notification, a list of the recent activity is displayed. The Covid Alert app MUST have a menu option to display this directly. Knowledge is power.<br> :date: __2020-12-04 16:43:36__

> Good<br> :date: __2020-12-03 11:14:27__

> After many months of covid alert being greyed out I finally figured it out. I had several google accounts on my phone for gaming apps. I had to remove all of the other gmail accounts in settings/accounts and backup/accounts then restart my phone, reinstall the app, and it finally prompted me to enable covid alert. Hopefully you can spread the word so others experiencing this problem can get the app to work. I will leave my review at 1 star for a little so maybe people having trouble might see it<br> :date: __2020-12-02 22:42:05__

> Awesome<br> :date: __2020-11-29 17:52:04__

> It would be great for giving me peace of mind but it's not active in Alberta.<br> :date: __2020-11-24 22:27:40__

> About time. Why doesn't the app communicate the restrictions and fines currently in my region? I would like a notification and a summary of what has changed<br> :date: __2020-11-21 18:41:30__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="ca.gc.hcsc.canada.stopcovid 3 reviews"/>
</p>

> The app is easy to use but how accurate is it?<br> :date: __2020-12-10 03:26:45__

> Will this app have a feature that I can enter a key when I eventually be vaccinated so I have a mobile vaccine certificate?? Also, 15 minutes within 2 meters seems a little liberal (maybe 5 minutes would be better), but if that's what the professionals say I guess<br> :date: __2020-12-09 20:09:38__

> Space<br> :date: __2020-12-08 21:35:22__

> I wish I didnt have to be online for this app to work. Not everyone has much data.<br> :date: __2020-12-05 22:14:07__

> As with other users, this has stopped doing exposure checks since early November. I'm in touch with support but not getting anywhere quickly. Also just checked with other members of my household and all have stopped working, all on Android. Looks to be working after Nov 20 update. This looks to be broken again after working for a few days. No checks on Dec 2,3 or 4. Kept app open on Dec 05 and got a dozen checks in about an hour .<br> :date: __2020-12-05 19:06:17__

> I was told this app could help direct us if we get a red alert weres safe would be helpfull.<br> :date: __2020-12-04 20:45:21__

> After instalation it seems to "take over" my bluetooth and my Fitbit app sometimes doesnt sync for a number of days until i force sync a couple times.<br> :date: __2020-12-04 20:05:02__

> My app wasn't working for a period of time in November, specifically on the 17th when I had a medical apt in Halifax (I live 3hrs away) the app did zero exposure checks. I found out 12 days later from an article on the CBC News app that there was a positive COVID case at the same hospital I was at and that I should have been isolating. However my app updated and is now working again and I don't seem to have developed COVID so it worked out for me.<br> :date: __2020-12-04 14:13:34__

> Just not very accurate ud mmmm mmmmmm<br> :date: __2020-12-03 01:14:16__

> Really good app! I would just love to see if I was around anyone at all for any amount of time who reports a covid diagnosis. I work in a grocery store and am not usualy around people for more than like 5 mins so its almost ineffective for me to use to know if I've been exposed to it. I feel like 15 mins is too long to have to be around someone for this to work.<br> :date: __2020-12-01 20:10:33__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="ca.gc.hcsc.canada.stopcovid 2 reviews"/>
</p>

> Can't reset the app after exposure notification. I received a notice by the app that I was exposed to someone that tested positive for Covid-19, so I went to get tested, and my result was negative. However, there is no way I can find in the app to reset it, so it is still telling me that I have been exposed. I can't tell if it is the original exposure, or a new one. This really renders the app useless going forward after an exposure warning.<br> :date: __2020-12-12 17:09:45__

> Great idea, bad execution. Most people don't know about it still. Stores and places of employment should post awareness of this. Also, as others says, it does not seem to check. I got 19 checks in past 14 days and they were all time stamped today.<br> :date: __2020-12-12 15:33:06__

> If I get near a person who has been tested positive, my phone should give me immediate, discreet notification to allow me to move away from people near me. These two factors will be a proactive approach to preventing the spread of covid-19 instead of reporting after the fact. I think the developers of this app have done a very good job of protecting people's privacy. I don't think people's privacy ought to trump people's health and potentially their lives. Only one million downloads!?<br> :date: __2020-12-11 19:10:26__

> When it was announced there was a bug preventing some devices from regularly checking for exposure, I downloaded the update assuming that would fix any problems. I just checked the settings this morning (Dec 7) and the app had not checked since November 26th, and previous to that, November 20th.<br> :date: __2020-12-07 12:29:27__

> Just wondering if this tool is actually effective due to recent outbreaks across the country. If nobody reports infection with this tool, then there will be no notification to the other by this tool. If this is true, then this is as good as a DUD. Maybe this tool should show some statistic data to bring up user confidence level⁉<br> :date: __2020-12-06 01:29:09__

> My daughter has had four notifications. She works from home, has groceries delivered and only goes out to walk her dog. No one she knows of has had a positive test. After two tests of herself and her family she no longer reacts to notifications. This sounds like another problem with th app.<br> :date: __2020-12-05 02:24:00__

> Turning bluetooth off and back on disables the app, at least on my device. I need to open the app and reactivate it manually everytime bluetooth has been disabled momentarily.<br> :date: __2020-12-04 19:24:33__

> I checked my logs today and they only show as having checked at the precise time of opening the app, no other times in the past 2 weeks. Before I checked the logs I made sure that the app is up to date, that was done a bit over a week ago. The phone has been rebooted since the update yet nothing shows in the logs until I opened the app. Over the last two weeks I know for certain that I have been around other people who have the app installed. How often should I see it checking?<br> :date: __2020-12-04 16:30:34__

> I never received alert via this app that there was an update. I read CBC news story that alerted me to check Google Play Store for update!!! NOT GOOD ENOUGH!!!<br> :date: __2020-12-04 15:06:54__

> When I open it, it says last checked 125 hours ago. If I go into google settings it says it checked this morning. Not sure which info to believe (I checked the App store and it appears i already have the update).<br> :date: __2020-12-04 14:30:19__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="ca.gc.hcsc.canada.stopcovid 1 reviews"/>
</p>

> Not available in Alberta! Come on Premier why do residents not have the choice!<br> :date: __2020-12-13 18:18:10__

> Don't think I'm getting any alerts.. if we are in the red zone (peel region). I find it hard to believe there's no one with covid<br> :date: __2020-12-13 16:23:55__

> Doesn't work in bc<br> :date: __2020-12-13 01:09:43__

> I suspect that nobody around me has the app so I never get any feedback. At least it could advise me if it detects the app nearby but insignificant<br> :date: __2020-12-12 23:52:01__

> I updated my Android app back in November after the first bug and assumed that fixed the exposure check bug. When I heard about the iPhone bug, I looked at my logs, and no checks had been logged since Nov. 24. I force quit and restarted, opened in foreground, and it immediately checked 14 times, all with the same timestamp. It still will not check while running in the background, the app has to be open and in the foreground at all times, which is next to useless.<br> :date: __2020-12-12 14:57:43__

> I had it installed for almost 1 month. I didn't find it useful.<br> :date: __2020-12-12 09:18:18__

> Apparently completely pointless so uninstalling. Why burn battery power for nothing?<br> :date: __2020-12-12 06:18:51__

> I read on the news that it might not be working, and the way to check is to look in your settings to see any exposure notifications. I looked, and I didn't see any exposure notifications. Nobody has provided a screenshot to show what the settings page is supposed to look like. Perhaps I simply haven't been near anybody else. This confusion is deadly, and I wish more people would be lying awake at night unable to sleep until they figured out how to solve it. Consult UI experts how 'bout.<br> :date: __2020-12-11 17:36:41__

> This app is useless! I just uninstalled the app because it doesnt actually check anything. It says it hasnt checked since October 24th. I work in a grocery store and somehow it never checks?? I liked the idea of this app and now I wouldnt recommend it!<br> :date: __2020-12-11 16:05:52__

> Despite all the media reports, I still don't know whether the app on my phone is checking for exposures. I have not been able to follow the instructions to tell me when it is checking. The menus don't appear as described in the text instructions. Illustrated instructions please!<br> :date: __2020-12-11 14:15:36__


