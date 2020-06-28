# CRUSH COVID RI
App version ``1.5``

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
| **Latest version** | 1.5 |
| **Last update** | 2020-06-04 17:12:37 |
| **Recent changes** | This update includes the following:<br>- Cosmetic improvements for readability and ease of use<br>- General bug fixes and performance improvements<br>- Improvements and bug fixes to location accuracy in My Location Diary |
| **Installs**  | 10,000+ |
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
 **com.google.android.finsky.permission<br>BIND_GET_INSTALL_REFERRER_SERVICE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | android.com | Google LLC | :us: US | 1997-06-23 04:00:00 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | app-measurement.com | Google LLC | :us: US | 2015-06-19 20:13:31 |
 | mapbox.com | Whois Privacy Service | :us: US | 2003-11-27 11:15:57 |
 | googlesyndication.com | Google LLC | :us: US | 2003-01-21 06:17:24 |
 | crashlytics.com | Google LLC | :us: US | 2011-01-21 15:30:40 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | googleadservices.com | Google LLC | :us: US | 2003-06-19 16:34:53 |


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
> - This application opens a Socket and connects it to the remote address '; exhausted proxy configurations: ' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/SocketException;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Code execution**
> - This application loads a native library<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The CRUSH COVID RI app has been installed by more than **10000** times. At this time, **113** rated the app and its average score is **2.96**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 35

:star::star::star::star:: 11

:star::star::star:: 14

:star::star:: 18

:star:: 33

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="com.ri.crushcovid 5 reviews"/>
</p>

> Very easy to use and I like that it makes it easier to do contact tracing if I get sick. If I miss the Governor's press conference while I'm at work all I have to do is just go on the app and I'm up to date.<br> :date: __2020-06-10 00:54:57__

> Love it but would like to see an area you can write who you hsve been with besides in a seperate notebook<br> :date: __2020-06-09 02:03:46__

> Great idea so far<br> :date: __2020-06-05 02:12:52__

> Pixel 3 phone, no issues installing app, working as designed<br> :date: __2020-06-03 21:37:55__

> Excellent tool to track all those sick people.<br> :date: __2020-05-29 21:11:47__

> Eats to much battery<br> :date: __2020-05-27 18:23:52__

> Thanks for help<br> :date: __2020-05-23 17:24:32__

> App works great. No problem with wifi nor data. People having problem need to give permission to the app in order to work.<br> :date: __2020-05-20 04:28:11__

> I think this will be interesting<br> :date: __2020-05-20 03:32:36__

> So far so good 👍👍👍😊😊😊😁<br> :date: __2020-05-20 02:35:32__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="com.ri.crushcovid 4 reviews"/>
</p>

> Works fine, though doesn't seem to update daily on my tracking.<br> :date: __2020-06-08 22:02:18__

> Happy with it, but wish it had: - lower battery drain - visual display of location tracing Thanks!<br> :date: __2020-06-08 19:14:53__

> In principle it's great. The developer need to patch a few things, though. Also, it doesn't do passive tracking so either the app is open and running or it won't do anything<br> :date: __2020-06-04 14:38:07__

> Excellent resource for Covid-19 info along with optional tracking feature to assist with contact tracing. Version 1.0 has some room for improvement, but it is an excellent tool to assist the DOH with their mission of protecting the health of RI citizens. I feel like I am helping to do my part in a small way by downloading this app.<br> :date: __2020-06-04 01:20:55__

> Took (me) some extra effort to find the app but it was Soo easy to download it once I finally found it. Very simple to use and I feel Very safe about my privacy control. GJGR!<br> :date: __2020-05-24 10:19:46__

> Does what its supposed to however I can only set it to detect location when app is in use. There's no way that I've found to set it all the time.<br> :date: __2020-05-22 04:56:47__

> So far, so good. One stop area for compilation of data and information.<br> :date: __2020-05-22 03:37:50__

> Decent app. The gps seems to slingshot. Of it shows me going out in my neighborhood when i was home.<br> :date: __2020-05-22 00:15:21__

> Great idea RI DOH<br> :date: __2020-05-19 21:24:30__

> First to download hope it works<br> :date: __2020-05-19 19:10:52__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="com.ri.crushcovid 3 reviews"/>
</p>

> Shows me at my neighbor's house instead of mine Number of hours shown in day for locations add to more or less than 24<br> :date: __2020-06-27 21:17:46__

> This is not accurately tracking location. Uodate: Even after installing the update, it is not accurately tracking my location. Sometimes it shows me at an address down the street from my home all day rather than my house. Other days it doesn't record any location at all. Such as yesterday, I went to Narragansett, nothing g shows on my location tracker at all for the last 2 days.<br> :date: __2020-06-27 15:30:01__

> Better, but did not kmow it had to be active on my screen to be working. Needs an option to be a tive in the background.<br> :date: __2020-06-14 15:26:44__

> Connect to sarahlandry coronavirous<br> :date: __2020-06-11 01:25:17__

> Not ready for prime time. "Location Diary" only shows my current location. "Settings" supposedly contains the option to modify location settings. It does not.<br> :date: __2020-06-10 23:13:13__

> Meaningless precision and poor accuracy. Maybe new version is better.<br> :date: __2020-06-09 11:00:28__

> Easy install. All you need is to enable gps permissions. Location data is saved on the phone and you can review the locations you went to. I found you can turn off the tracking in the settings by pulling down the menu, swiping left on the crush covid icon, and clicking the cog icon. Then toggle the button to disable. There needs to be a way to turn on and off easier from the top pull down menu. This will allow users to turn off when at home to save battery.<br> :date: __2020-06-03 14:44:12__

> Tracker does not update correctly.<br> :date: __2020-05-26 11:23:20__

> App has helpful information but the My Location Diary has been inaccurate.<br> :date: __2020-05-25 17:18:49__

> Started off well but crushed my battery and has been causing issues with my GPS using apps. Can't have it on all the time which kind of defeats the point.<br> :date: __2020-05-24 17:43:32__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="com.ri.crushcovid 2 reviews"/>
</p>

> I had the app when it first came out and it worked fine until 3 weeks ago then it stopped tracking me. I just got a new Note 10 and it won't let me finish setting it up . Won't respond on last page of setup to allow it to track, etc. So I uninstalled it and am going to try to install it again<br> :date: __2020-06-19 20:44:25__

> Not accurate. Uses too much battery.<br> :date: __2020-06-13 01:11:30__

> On my Google Pixel 3 Android, the app only gives me the options to access location while using the app or to deny location services. There is no option for allow all the time. Thus, my location diary has nothing in it! Also, an excellent feature for this app would be a contact diary.<br> :date: __2020-06-09 03:10:53__

> Not accurate. My husband and I both downloaded and it hasn't been even close to accurate. He likes golf but didn't spend 30 hours there the other day. Maybe this new version will be better. It's a good idea.<br> :date: __2020-06-09 02:04:04__

> I noticed that my location has me at the wrong places and On other times it doesn't show where I went over the 10 minutes....<br> :date: __2020-06-08 22:32:43__

> Good idea bleh execution app is barren amd pins do not stick. Develop moar<br> :date: __2020-06-04 03:55:32__

> Doesn't recognize as data on or connected to wifi.<br> :date: __2020-06-03 20:55:20__

> Not accurate. Looking at my history it has me at places I've never even been close too!<br> :date: __2020-05-31 00:28:14__

> Killed my battery quickly. Makes sense but google maps does the same tracking of where I go.<br> :date: __2020-05-26 22:35:54__

> Location does not work all the time, only if app is running, so it useless, as I can't seem to set it to access location all the time? So the location data is not updating.<br> :date: __2020-05-25 18:06:42__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="com.ri.crushcovid 1 reviews"/>
</p>

> Mmm<br> :date: __2020-06-26 05:59:51__

> The app completely missed my morning hike, seems to work only intermittently.<br> :date: __2020-06-26 04:36:49__

> "My location diary" doesn't do anything. It doesn't show where I have been. Don't throw away your log book. This is worthless.<br> :date: __2020-06-25 21:20:44__

> I dont think I spent 125 hours in one day at a location very inaccurate and may skip a few days and hours<br> :date: __2020-06-25 20:51:58__

> It is incredibly inaccurate. I live in Cranston. We went to the border of CT and got off the motorcycle for over 30 minutes. It didn't record my location at all that day. Now it's reading I was at Ace Hardware for HOURS. I wasn't there at all. Worthless. UPDATE - MY LOCATION DIARY HAS NOT UPDATED IN 10 DAYS. REMOVING THIS FROM MY PHONE.<br> :date: __2020-06-25 05:34:38__

> Thus app is not working on my android smart phone. No locations are being recorded.<br> :date: __2020-06-24 19:24:21__

> Completely inaccurate. This is the wrong solution. Should use Google COVID-19 Proximity Tracking API, which already works. But app relies on ineffective method that (sometimes) stores your (wong) location history locally and then flags you as a contact if RIDOH parameters have been met. So you still have to rely on people correlating information and calling you. Way too many variables will mean very slow, and never complete, adiption. Don't reinvent the wheel.<br> :date: __2020-06-24 05:16:21__

> Remove covid19<br> :date: __2020-06-22 06:32:14__

> F\*\** off big brother<br> :date: __2020-06-19 16:58:23__

> Download the app and select language preference but can't proceed from that point.<br> :date: __2020-06-14 14:30:46__


