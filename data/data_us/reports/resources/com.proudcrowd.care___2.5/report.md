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

> Awesome<br> :date: __2020-05-17 11:47:26__

> Love this app<br> :date: __2020-05-16 12:11:08__

> A must!!<br> :date: __2020-05-14 06:24:04__

> Payment<br> :date: __2020-05-02 21:50:55__

> Great if I don't want to catch COVID #RIPrickmay<br> :date: __2020-04-26 09:16:49__

> Thank you at least someone in government is coherrant.<br> :date: __2020-04-24 02:11:08__

> I hope Michigan stats will be here soon.<br> :date: __2020-04-22 20:52:08__

> 🙄😔😔😔<br> :date: __2020-04-22 11:07:56__

> Thank you for helping us track so easily with anonymity and confidentiality. #NDSmart Governor Burgum and team are doing everything they can to keep us safe and doing it smart. So proud to be from ND!<br> :date: __2020-04-22 03:03:34__

> Great Idea, saving so much time though technology thanks Governor!<br> :date: __2020-04-21 21:52:36__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="com.proudcrowd.care 4 reviews"/>
</p>

> It is great, it works, and I am excited for updates!<br> :date: __2020-04-29 03:31:46__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="com.proudcrowd.care 3 reviews"/>
</p>

> Very inconsistent with location. Can be at a location for hours and doesn't list it.<br> :date: __2020-05-16 15:20:52__

> It's a great idea, but does not log most of the places I've been. Stopped at 6 places in Bismarck and didn't log one place. And then the next time it will log the same place 4 times within a few minutes or log a place I only drove by.<br> :date: __2020-05-14 02:20:12__

> Still isn't capturing places I've been. Was at 3 different locations today, and not one of them showing up.<br> :date: __2020-05-04 19:46:22__

> I hope this helps people but there are definitely a lot of bugs<br> :date: __2020-05-04 05:28:59__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="com.proudcrowd.care 2 reviews"/>
</p>

> Doesn't log locations all the time. Even after I have been there for over ten minutes. Not very dependable .<br> :date: __2020-05-13 18:15:39__

> I'm not sure if it's just the app for Android but most days it doesn't even recognize that I have been anywhere! My Bluetooth is on, what's going on?<br> :date: __2020-05-13 02:08:21__

> Not the best, has not tracked me since May 9th! My location is turned on also. Noticed previously it missed Tracking me to and from work on May 6th. Might be easier to just write it down on paper .<br> :date: __2020-05-11 15:36:20__

> So far only kept two logs. Both for work. Both on the same day. It's also picked up places I drove past. Been at work 12 hours today and it didn't register once.<br> :date: __2020-05-11 00:43:47__

> Need to have a way to add places one has been when it quite often misses the place one had visited all together.<br> :date: __2020-05-10 02:16:21__

> This app doesn't work very well. Sometimes places I've been will show up but I have gone places that do not show up. This type of app needs to be much more reliable.<br> :date: __2020-05-10 01:32:49__

> I have had this ap downloaded for a week and it has only captured visits to my office. I went to Target and Walmart both for at least one hour during this time. It also did not record a visit to my chiropractor, but that was only 15 minutes total. I downloaded this to be a good citizen and help protect myself and others, but it clearly is not working. I have a Galaxy Note 10. I didn't see another way to offer feedback.<br> :date: __2020-05-03 20:53:36__

> Location services on and did not log 4 businesses we were at on 4/28. Yet logs places we only drove by. Android version 2.1 on Samsung Galaxy Note 9. Hope this helps. Turned notifications off.<br> :date: __2020-05-03 05:08:46__

> Pretty much a pain to use, might be easier to log locations manually.<br> :date: __2020-05-02 21:00:07__

> Quit recording places after one day not help anywhere<br> :date: __2020-04-30 01:53:49__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="com.proudcrowd.care 1 reviews"/>
</p>

> Did not accurately record any location... not even 1. Downloaded 5/7 recorded on 5/8 ( inaccurately) then no location recorded since this date and I have been working out of the home so should have at least 2.<br> :date: __2020-05-17 02:39:16__

> Does not seem to log locations or show anything under the info tab.<br> :date: __2020-05-16 17:34:52__

> I have visited the grocery store on a weekly basis since downloading Care19. This trips have not once shown up in visited locations.<br> :date: __2020-05-16 02:10:05__

> Don't capture all the locations<br> :date: __2020-05-16 01:35:14__

> Hasn't recorded any stops for a week. Have had doctor appointments and other stops.<br> :date: __2020-05-15 12:27:41__

> Does not track my movements.<br> :date: __2020-05-15 02:19:43__

> This has not updated my location since 5/12. It is now the 14th. It's missing about 50% of where I've been. You should have the ability to enter information manually or name places if it's not recording your location. If everyone has this poor of a tracking record, it's pretty usless.<br> :date: __2020-05-14 22:18:14__

> Gives a lot of erroneous locations that are passed while driving or stopping at a stop light. Some days it gives no information at all..<br> :date: __2020-05-14 17:59:57__

> Doesnt track 99% of the time.<br> :date: __2020-05-14 17:32:00__

> Only logs some locations. Yesterday i made 4 stops, 130 miles, didn't register one of them. Few days ago logged a location which turned out to be a long red light. We need the option to add locations. And what is the information about? Just says loading... loading... loading.<br> :date: __2020-05-14 16:27:17__


