# CRUSH COVID RI
App version ``1.0``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="CRUSH COVID RI icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | CRUSH COVID RI |
| **Unique identifier** | com.ri.crushcovid |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=com.ri.crushcovid](https://play.google.com/store/apps/details?id=com.ri.crushcovid) |
| **Summary**  | CRUSH COVID RI is the COVID-19 response app for Rhode Island. #CrushCovidRI |
| **Privacy policy** | [https://health.ri.gov/covid/crush/privacypolicy/](https://health.ri.gov/covid/crush/privacypolicy/) |
| **Latest version** | 1.0 |
| **Last update** | 2020-05-15 22:05:09 |
| **Recent changes** | - |
| **Installs**  | 5,000+ |
| **Category** | Health & Fitness |
| **First release** | May 15, 2020 |
| **Size**  | 14M |
| **Supported Android version**  | 8.0 and up |

### Description
> CRUSH COVID RI is a COVID-19 pandemic response app which provides Rhode Islanders easy access to all of the resources required during the public health crisis, including a location diary that helps users identify the people and places they are in contact with and a symptom checking survey.
<br>Thank you for using the CRUSH COVID RI app and taking an active role in slowing the spread of COVID-19 in Rhode Island. You can make a difference in the health of your loved ones and your community by helping us track the virus in our state. The “My Location Diary” feature uses GPS location data that is already available from your phone to help you easily track the places and people you visited over the past 20 days. If you test positive for COVID-19, and you agree to share this information with the Rhode Island Department of Health, they can quickly identify people you were in contact with and reduce the spread of COVID-19.  
<br>CRUSH COVID RI also connects you to the latest COVID-19 news and resources – and helps you quickly check for symptoms and identify testing locations near you. Together we will #CrushCovidRI! 
<br>Please see our Terms of Use (https://health.ri.gov/covid/crush/termsofuse/) & Privacy Policy (https://health.ri.gov/covid/crush/privacypolicy/) for further information.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/>  | <img src="screenshot_5.png" alt="screenshot" width="300"/>  | <img src="screenshot_6.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_7.png" alt="screenshot" width="300"/>  | <img src="screenshot_8.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | State of Rhode Island |
| **Website**  | [https://health.ri.gov/crushcovid](https://health.ri.gov/crushcovid) |
| **Email** | RIDOH.Covid19Questions@health.ri.gov |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=State+of+Rhode+Island](https://play.google.com/store/apps/developer?id=State+of+Rhode+Island) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Android10, version 10 (API level 29) |
| **Effective target Android version**  | Android10, version 10 (API level 29) |
| **Minimum supported Android version**  | Oreo, version 8.0.0 (API level 26) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>ACCESS_WIFI_STATE** | Normal | Allows applications to access information about Wi-Fi networks. 
 **android.permission<br>CALL_PHONE** | :warning:**Dangerous** | Allows an application to initiate a phone call without going through the Dialer user interface for the user to confirm the call. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | android.com | Google LLC | :us: US | 1997-06-23 04:00:00 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | mapbox.com | Whois Privacy Service | :us: US | 2003-11-27 11:15:57 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>
> - This application reads the radio technology (network type) currently in use on the device for data transmission<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Telephony services abuse**
> - This application makes phone calls<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address ' returned no addresses for  ; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Code execution**
> - This application loads a native library<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The CRUSH COVID RI app has been installed by more than **5000** times. At this time, **55** rated the app and its average score is **3.3090909**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 23

:star::star::star::star:: 6

:star::star::star:: 6

:star::star:: 5

:star:: 15

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="com.ri.crushcovid 5 reviews"/>
</p>

> Excellent tool to track all those sick people.<br> :date: __2020-05-29 21:11:47__

> Eats to much battery<br> :date: __2020-05-27 18:23:52__

> Thanks for help<br> :date: __2020-05-23 17:24:32__

> App works great. No problem with wifi nor data. People having problem need to give permission to the app in order to work.<br> :date: __2020-05-20 04:28:11__

> I think this will be interesting<br> :date: __2020-05-20 03:32:36__

> So far so good 👍👍👍😊😊😊😁<br> :date: __2020-05-20 02:35:32__

> Will really help with contact tracing! Love this! Everything on the app seems to be working great.<br> :date: __2020-05-19 21:42:11__

> Quick and easy install and setup. App works as designed as far as I can tell. Useful info on volunteer opportunities is a great addition.<br> :date: __2020-05-19 19:43:22__

> Easy to set up. Stay safe!<br> :date: __2020-05-19 19:35:42__

> Anything that helps the community "crush" this virus is worthwhile to use<br> :date: __2020-05-19 19:22:56__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="com.ri.crushcovid 4 reviews"/>
</p>

> Took (me) some extra effort to find the app but it was Soo easy to download it once I finally found it. Very simple to use and I feel Very safe about my privacy control. GJGR!<br> :date: __2020-05-24 10:19:46__

> Does what its supposed to however I can only set it to detect location when app is in use. There's no way that I've found to set it all the time.<br> :date: __2020-05-22 04:56:47__

> So far, so good. One stop area for compilation of data and information.<br> :date: __2020-05-22 03:37:50__

> Decent app. The gps seems to slingshot. Of it shows me going out in my neighborhood when i was home.<br> :date: __2020-05-22 00:15:21__

> Great idea RI DOH<br> :date: __2020-05-19 21:24:30__

> Doesn't recognize as data on or connected to wifi.<br> :date: __2020-05-19 20:59:09__

> First to download hope it works<br> :date: __2020-05-19 19:10:52__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="com.ri.crushcovid 3 reviews"/>
</p>

> It would work fine, except it should not require being in a location for 10 minutes to add it to your location. I walked by several people without masks on today, but my location record shows that I haven't left home.<br> :date: __2020-05-29 21:13:15__

> Tracker does not update correctly.<br> :date: __2020-05-26 11:23:20__

> App has helpful information but the My Location Diary has been inaccurate.<br> :date: __2020-05-25 17:18:49__

> Started off well but crushed my battery and has been causing issues with my GPS using apps. Can't have it on all the time which kind of defeats the point.<br> :date: __2020-05-24 17:43:32__

> Great public health service, but the foreground only location permissions seems to be incorrectly confirmed?<br> :date: __2020-05-24 00:55:57__

> Easy install. All you need is to enable gps permissions. Location data is saved on the phone and you can review the locations you went to. I found you can turn off the tracking mg in the settings by pulling down the menu, swiping left on the crush covid icon, and click the clog. Then toggle the button to disable. There needs to be a way to turn on and off easier from the top pull down menu. This will allow users to turn off when at home to save battery.<br> :date: __2020-05-23 02:17:51__

> Location info not 100% accurate. Since I don't spend 20 minutes at every place I visit, you should add a location manually button.<br> :date: __2020-05-23 00:18:42__

> Good information, however, the location is not very accurate.<br> :date: __2020-05-22 16:08:09__

> Informative and useful ap. Easy to use. Unfortunately it interfered with the location on Pokemon Go so I had to uninstall it.<br> :date: __2020-05-20 02:55:09__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="com.ri.crushcovid 2 reviews"/>
</p>

> Not accurate. Looking at my history it has me at places I've never even been close too!<br> :date: __2020-05-31 00:28:14__

> Killed my battery quickly. Makes sense but google maps does the same tracking of where I go.<br> :date: __2020-05-26 22:35:54__

> Location does not work all the time, only if app is running, so it useless, as I can't seem to set it to access location all the time? So the location data is not updating.<br> :date: __2020-05-25 18:06:42__

> Getting better each day. Hopefully, it is adapted to work on mobile devices.<br> :date: __2020-05-24 04:53:55__

> I drove on a road near my house I was on this street for total of1 min because of stop sign . I diary say I was on this street for 22min. Maybe once glitches are fixed it will be a better app. But for now I'll continue to write where ever I go and who I see.<br> :date: __2020-05-23 18:40:57__

> I think the point of this app is great. And I don't know if it's my phone or the app but I have been home all day today yet it says I have been to places up the street from me. Like I said, it could be my phone. This hasn't just happened today, but other days too.<br> :date: __2020-05-22 22:06:35__

> Barely tracks my location, only registered an hour of time and completely missed me leaving the house. Ten minute window is also far to broad.<br> :date: __2020-05-21 17:28:08__

> At first the app seemed to function well with some useful information. However it doesn't work with a VPN enabled. When I try looking at My Location Diary with it says it needs wifi/cellular network. Why is it failing when the VPN is enabled? Why is it going to a server for data when the location diary is supposed to be stored on my phone?<br> :date: __2020-05-20 23:46:46__

> Telling me places haven't been, stupid<br> :date: __2020-05-20 21:18:17__

> Doesn't always respond<br> :date: __2020-05-20 00:29:08__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="com.ri.crushcovid 1 reviews"/>
</p>

> Bad spying app<br> :date: __2020-05-30 19:15:13__

> Glitchy and inaccurate. Has not updated my whereabouts in 4 days even though I traveled to the other end of the state where I stayed for four hours. Prior to the last place it says I've been, it also records me being places I have never been (including a street over when I was sleeping in my bed) and missed my entire 30 min grocery shop run. Sent messages to IT but no response. How much did this app cost?<br> :date: __2020-05-29 00:35:51__

> I get why RI wanted to have something sooner rather than later but this app does not follow the standard conventions and frameworks the major contact tracing applications use. Rather than use BLE to ping anonymous IDs for _proximity_ detection they are storing your full location history locally.<br> :date: __2020-05-28 04:39:43__

> Completely inaccurate.<br> :date: __2020-05-27 02:56:07__

> I am deleting this app. The location data is joke. I have had it installed for 3 days now and there about a dozen locations in the data that say I was there for long periods of time that I have been nowhere near. Useless.<br> :date: __2020-05-23 19:48:23__

> Uninstalling. The location diary is wholly inaccurate and I can get the other info elsewhere<br> :date: __2020-05-23 14:49:10__

> Does not work! I have not left my house since I downloaded it, yet it states I have been in 5 different places! I uninstalled it!<br> :date: __2020-05-22 18:10:29__

> Won't download😠😠<br> :date: __2020-05-22 13:48:07__

> It said I was at a location for 53 minutes that I passed by on a ride but it won't say I was home for the 10 hours while working<br> :date: __2020-05-22 00:42:43__

> Doesn't go beyond choosing a language<br> :date: __2020-05-21 22:50:11__


