# Care19
App version ``2.5``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="Care19 icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Care19 |
| **Unique identifier** | com.proudcrowd.care |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=com.proudcrowd.care](https://play.google.com/store/apps/details?id=com.proudcrowd.care) |
| **Summary**  | You can help stop the spread of Covid-19 |
| **Privacy policy** | [https://care19.app/privacy](https://care19.app/privacy) |
| **Latest version** | 2.5 |
| **Last update** | 2020-05-08 05:05:42 |
| **Recent changes** | Minor bug fixes and performance improvements |
| **Installs**  | 10,000+ |
| **Category** | Medical |
| **First release** | Apr 19, 2020 |
| **Size**  | 4.5M |
| **Supported Android version**  | 6.0 and up |

### Description
> Thank you for taking an active role in slowing the spread of coronavirus and making a difference in the health of your loved ones and your community.  Care19 uses state-of-the-art GPS location data to help trace the places you have visited.
<br>If you test positive for COVID-19, with your permission, this anonymous and confidential data can be shared with the Department of Health to more efficiently identify others with whom you were in contact with.  Identifying contacts is key to slowing the spread of coronavirus.
<br>You will not be asked to provide any personally identifiable information within the app. Location data will only be shared with the Department of Health if you consent upon testing positive for COVID-19. This is done by sharing a code number displayed on the “About” section of the app.


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
| **Developer**  | ProudCrowd, LLC |
| **Website**  | [https://www.care19.app](https://www.care19.app) |
| **Email** | tim.brookins@proudcrowd.com |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=ProudCrowd,+LLC](https://play.google.com/store/apps/developer?id=ProudCrowd,+LLC) |

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
 **android.permission<br>ACCESS_BACKGROUND_LOCATION** | :warning:**Dangerous** | Allows an app to access location in the background. 
 **android.permission<br>ACCESS_COARSE_LOCATION** | :warning:**Dangerous** | Allows an app to access approximate location. 
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>ACTIVITY_RECOGNITION** | :warning:**Dangerous** | Allows an application to recognize physical activity. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 
 **com.google.android.finsky.permission<br>BIND_GET_INSTALL_REFERRER_SERVICE** | - | - 
 **com.google.android.gms.permission<br>ACTIVITY_RECOGNITION** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | bugfender.com | Beenario GmbH | :de: DE | 2014-10-28 11:32:13 |
 | googlesyndication.com | Google LLC | :us: US | 2003-01-21 06:17:24 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | app-measurement.com | Google LLC | :us: US | 2015-06-19 20:13:31 |
 | azurewebsites.net | Microsoft Corporation | :us: US | 2012-01-24 18:43:51 |
 | crashlytics.com | Google LLC | :us: US | 2011-01-21 15:30:40 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | googleadservices.com | Google LLC | :us: US | 2003-06-19 16:34:53 |


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

**Code execution**
> - This application executes a UNIX command containing this argument: 'logcat -c 2'<br>
> - This application executes a UNIX command containing this argument: 'logcat -c'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The Care19 app has been installed by more than **10000** times. At this time, **83** rated the app and its average score is **2.3614457**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 22

:star::star::star::star:: 3

:star::star::star:: 4

:star::star:: 8

:star:: 46

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="com.proudcrowd.care 5 reviews"/>
</p>

> I think its a great app to have Since cvid19 happend<br> :date: __2020-05-22 22:01:43__

> Awesome<br> :date: __2020-05-17 11:47:26__

> Love this app<br> :date: __2020-05-16 12:11:08__

> A must!!<br> :date: __2020-05-14 06:24:04__

> Payment<br> :date: __2020-05-02 21:50:55__

> Great if I don't want to catch COVID #RIPrickmay<br> :date: __2020-04-26 09:16:49__

> Thank you at least someone in government is coherrant.<br> :date: __2020-04-24 02:11:08__

> I hope Michigan stats will be here soon.<br> :date: __2020-04-22 20:52:08__

> 🙄😔😔😔<br> :date: __2020-04-22 11:07:56__

> Thank you for helping us track so easily with anonymity and confidentiality. #NDSmart Governor Burgum and team are doing everything they can to keep us safe and doing it smart. So proud to be from ND!<br> :date: __2020-04-22 03:03:34__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="com.proudcrowd.care 4 reviews"/>
</p>

> The early release back in April was rough (didn't log any stops for me). But it's been working well for me since about May 4. It occasionally logs more than one stop at the same location. It occasionally gets the name of the location wrong, but this is very easy to correct.<br> :date: __2020-05-19 06:25:30__

> It is great, it works, and I am excited for updates!<br> :date: __2020-04-29 03:31:46__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="com.proudcrowd.care 3 reviews"/>
</p>

> Simple app. Does what it was designed for but little else. Misses many locations and frequently has location accuracy issues. Routinely misses my home by 6 blocks. Says I have visited locations I have just driven past. Would be nice to have ability to add locations that I visited but app failed to record.<br> :date: __2020-05-22 15:52:32__

> Still isn't capturing places I've been. Was at 3 different locations today, and not one of them showing up.<br> :date: __2020-05-20 23:03:13__

> Very inconsistent with location. Can be at a location for hours and doesn't list it.<br> :date: __2020-05-16 15:20:52__

> It's a great idea, but does not log most of the places I've been. Stopped at 6 places in Bismarck and didn't log one place. And then the next time it will log the same place 4 times within a few minutes or log a place I only drove by.<br> :date: __2020-05-14 02:20:12__

> I hope this helps people but there are definitely a lot of bugs<br> :date: __2020-05-04 05:28:59__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="com.proudcrowd.care 2 reviews"/>
</p>

> Hasn't loaded anything in 3 days not impressed.<br> :date: __2020-05-22 14:57:46__

> This app would make sense if it correctly tracked where you were. It needs an update to better track it also for walking. Poor and elderly won't use this nor will people who refuse so information will be limited. Needs an upgrade to let you know if you've been around someone with Coronavirus. Good idea but needs fixing<br> :date: __2020-05-21 05:24:02__

> This app does not record all the places I've been. I was in 5 different businesses in one day for more than 15 minutes and it did not record them . This app has a few bugs...I write down mow.<br> :date: __2020-05-20 22:58:49__

> Inaccurate<br> :date: __2020-05-19 18:09:09__

> Does not work in NJ<br> :date: __2020-05-18 02:41:29__

> Doesn't log locations all the time. Even after I have been there for over ten minutes. Not very dependable .<br> :date: __2020-05-13 18:15:39__

> I'm not sure if it's just the app for Android but most days it doesn't even recognize that I have been anywhere! My Bluetooth is on, what's going on?<br> :date: __2020-05-13 02:08:21__

> Not the best, has not tracked me since May 9th! My location is turned on also. Noticed previously it missed Tracking me to and from work on May 6th. Might be easier to just write it down on paper .<br> :date: __2020-05-11 15:36:20__

> So far only kept two logs. Both for work. Both on the same day. It's also picked up places I drove past. Been at work 12 hours today and it didn't register once.<br> :date: __2020-05-11 00:43:47__

> Need to have a way to add places one has been when it quite often misses the place one had visited all together.<br> :date: __2020-05-10 02:16:21__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="com.proudcrowd.care 1 reviews"/>
</p>

> No privacy<br> :date: __2020-05-23 00:05:46__

> Too slow<br> :date: __2020-05-22 22:54:12__

> This app will never get on my phone. Nothing like it will never get on my phone. I NEVER WEAR MASKS. I DO NOT SOCIAL DISTANCE. I WILL NEVER BE "VACCINATED " AND NO NEEDLE WILL EVER TOUCH MY SKIN. I WILL NEVER ALLOW YOU TO TAKE MY CONSTITUTIONAL RIGHTS AWAY YOU CRAZY PSYCHOPATHS. YOU ALL NEED TO GO AWAY. LIKE ACTUALLY... GO.... AWAY....<br> :date: __2020-05-22 18:32:15__

> Shared my location that I was not sure about. I wanted to help with the virus.<br> :date: __2020-05-22 05:39:43__

> Stopped logging where I go. Not useful. Uninstalling.<br> :date: __2020-05-21 19:48:26__

> Great idea Junk Only listed one site over 5 weeks 😔<br> :date: __2020-05-21 15:24:17__

> It likes to log random locations or wrong locations. It is trying to tell me i was at work when I was no where near there. Pops up wrong locations and thinks there is a speakeasy in my neighborhood and that my house is a campground.<br> :date: __2020-05-21 05:06:01__

> Violation of constitutional rights<br> :date: __2020-05-21 03:32:57__

> Someone told me this tracked people with COVID. I do not see the possibility inside the app.. it seems to be only for the infected individuals. Wheres the app to see where the infected individuals are proximity wise to your location?<br> :date: __2020-05-19 08:26:57__

> Worthless. Says it will only locate places when having used a vehicle. Went 100 miles, been here two hours, it still thinks I'm at home yet. Minus 2 stars<br> :date: __2020-05-18 19:17:03__


