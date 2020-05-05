# Care19
App version ``2.4``

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
| **Latest version** | 2.4 |
| **Last update** | 2020-05-04 20:19:57 |
| **Recent changes** | A few bug fixes to address some occasional crashes. |
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

The Care19 app has been installed by more than **10000** times. At this time, **76** rated the app and its average score is **2.5394738**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 23

:star::star::star::star:: 3

:star::star::star:: 4

:star::star:: 8

:star:: 38

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="com.proudcrowd.care 5 reviews"/>
</p>

> Payment<br> :date: __2020-05-02 21:50:55__

> Great if I don't want to catch COVID #RIPrickmay<br> :date: __2020-04-26 09:16:49__

> It did not track at all.<br> :date: __2020-04-25 06:32:00__

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

> Still isn't capturing places I've been. Was at 3 different locations today, and not one of them showing up.<br> :date: __2020-05-04 19:46:22__

> I hope this helps people but there are definitely a lot of bugs<br> :date: __2020-05-04 05:28:59__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="com.proudcrowd.care 2 reviews"/>
</p>

> I have had this ap downloaded for a week and it has only captured visits to my office. I went to Target and Walmart both for at least one hour during this time. It also did not record a visit to my chiropractor, but that was only 15 minutes total. I downloaded this to be a good citizen and help protect myself and others, but it clearly is not working. I have a Galaxy Note 10. I didn't see another way to offer feedback.<br> :date: __2020-05-03 20:53:36__

> Location services on and did not log 4 businesses we were at on 4/28. Yet logs places we only drove by. Android version 2.1 on Samsung Galaxy Note 9. Hope this helps. Turned notifications off.<br> :date: __2020-05-03 05:08:46__

> Pretty much a pain to use, might be easier to log locations manually.<br> :date: __2020-05-02 21:00:07__

> Gives a lot of erroneous locations that are passed while driving or stopping at a stop light.<br> :date: __2020-05-02 02:30:37__

> Quit recording places after one day not help anywhere<br> :date: __2020-04-30 01:53:49__

> Has not logged anything sense the 25th of April and have gone to work for 2 8 hour shifts plus trip to grocery store<br> :date: __2020-04-29 04:45:01__

> It works but Google maps does the same thing with timeline<br> :date: __2020-04-26 09:14:04__

> Location info is incorrect and incomplete. I was able to fix the incorrect info, but can't add locations.<br> :date: __2020-04-22 21:37:04__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="com.proudcrowd.care 1 reviews"/>
</p>

> Never found location, just spun for an hour... Junk<br> :date: __2020-05-05 05:48:22__

> Does not track where i have been it says that i did not go aby where het but have<br> :date: __2020-05-04 19:34:11__

> Broken? Doesnt log locations, or does it? We will never know, guess we should wait for an official app.<br> :date: __2020-05-03 22:32:20__

> Made 5 stops in Bismarck >10 minutes & it didnt log any of them. But did log 3 entries at different times at same location on highway between my house & there. New April update missed 1 stop, and recorded 17 entries over 3 minutes while sitting in restaurant parking lot. Wish it worked & that you could manually add entries.<br> :date: __2020-05-03 16:24:04__

> The app is still not capturing any location I have visited. Was all over fargo and nothing. This definitely needs to be fixed to help people not make them angry.<br> :date: __2020-05-03 05:59:31__

> Does not record any place I've been. If they want help someone needs to fix the app.<br> :date: __2020-05-02 20:12:34__

> My first experience was a good experience. Today went to CVS, App said I was at Bismarck Animal Hospital. My next stop went to Arby's. App said I was at McDonald's. Next stop in the same parking lot as Arby's, I parked to eat my meal and App now says I'm at a MoneyGram. This place was located in a now defunct Kmart since 2019. So totally not a good thing to reply on.<br> :date: __2020-05-02 02:24:24__

> It will not track any of my locations<br> :date: __2020-05-02 00:08:28__

> Getting to the point where I want to just uninstall this app since it logs where I work 15-20 times in the 8 hours I'm at work. I'm assuming it's because I operate a forklift and drive from one end of the plant to the other throughout the day.<br> :date: __2020-04-30 23:20:41__

> before you install this app ask yourself Who is ProudCrowd LLC? How is your data going to be used. Their website is not working. Love to help the cause but this company is unknown. Buyer beware it's your data<br> :date: __2020-04-30 16:49:22__


