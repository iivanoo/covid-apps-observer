# Covid Watch Arizona
App version ``2.0.32``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="Covid Watch Arizona icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Covid Watch Arizona |
| **Unique identifier** | gov.azdhs.covidwatch.android |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=gov.azdhs.covidwatch.android](https://play.google.com/store/apps/details?id=gov.azdhs.covidwatch.android) |
| **Summary**  | Help stop COVID-19 in Arizona |
| **Privacy policy** | [https://azdhs.gov/documents/privacy-policy/covid-watch-application-privacy-policy.pdf](https://azdhs.gov/documents/privacy-policy/covid-watch-application-privacy-policy.pdf) |
| **Latest version** | 2.0.32 |
| **Last update** | 2021-02-12 21:39:20 |
| **Recent changes** | * Exposure Notifications are now silenced during nighttime hours<br>* Support for Portuguese language<br>* Bug fixes and improvements |
| **Installs**  | 10,000+ |
| **Category** | Medical |
| **First release** | Aug 19, 2020 |
| **Size**  | 7.8M |
| **Supported Android version**  | 6.0 and up |

### Description
> Let your smartphone notify you to potential exposure to COVID-19–using fully anonymous Bluetooth signals–and help stop the spread of coronavirus in Arizona.
<br>Get peace of mind by taking this small step and start rebuilding trust in your community – install this free app, released in partnership with the Arizona Department of Health Services (ADHS).
<br>Once you opt-in and enable exposure notification on your phone, Covid Watch works in the background, automatically detecting if you come into close proximity with someone else, without tracking you by GPS or ever revealing any personal data.
<br> 
<br>The more people participate, the more effective we can be. Encourage your friends, family, and colleagues to install Covid Watch today. Members of the following campus communities can access a customized version of the app: 
<br>• University of Arizona
<br>• Northern Arizona University 
<br>Provided by Covid Watch, an Arizona non-profit organization dedicated to your health and privacy.


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
| **Developer**  | ADHS-Arizona Department of Health Services |
| **Website**  | [https://covidwatch.org](https://covidwatch.org) |
| **Email** | contact@covidwatch.org |
| **Physical address**  | [150 N 18TH AVE](https://www.google.com/maps/search/150%20N%2018TH%20AVE) (Google Maps) |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=ADHS-Arizona+Department+of+Health+Services](https://play.google.com/store/apps/developer?id=ADHS-Arizona+Department+of+Health+Services) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | - |
| **Effective target Android version**  | - |
| **Minimum supported Android version**  | Marshmallow, version 6.0 (API level 23) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **com.google.android.finsky.permission<br>BIND_GET_INSTALL_REFERRER_SERVICE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | wehealth.org | Domains By Proxy, LLC | :us: US | 2017-07-17 14:30:24 |
 | googlesyndication.com | Google LLC | :us: US | 2003-01-21 06:17:24 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | googleadservices.com | Google LLC | :us: US | 2003-06-19 16:34:53 |
 | app-measurement.com | Google LLC | :us: US | 2015-06-19 20:13:31 |
 | covidwatch.org | Contact Privacy Inc. Customer 1247431163 | :canada: CA | 2020-03-01 18:20:50 |
 | arizona.edu | University of Arizona | - | 1986-01-23 00:00:00 |
 | nau.edu | Northern Arizona University | - | 1989-08-14 00:00:00 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Telephony services abuse**
> - This application makes phone calls<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Lm/a/a/a/a;->o(Ljava/lang/String;)Ljava/lang/StringBuilder;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The Covid Watch Arizona app has been installed by more than **10000** times. At this time, **42** rated the app and its average score is **3.7857144**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 24

:star::star::star::star:: 4

:star::star::star:: 3

:star::star:: 3

:star:: 8

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.azdhs.covidwatch.android 5 reviews"/>
</p>

> Necessary<br> :date: __2020-12-03 06:41:57__

> The app is Amazing and I love it. This should be launched across USA and it will help in saving allot of people from exposure of Covid-19. Everyone in Arizona should download and start using it.<br> :date: __2020-10-06 13:43:59__

> The idea is great/it is easy to set up/explains how it works well. I will rate 5 simply for that. It definitely needs to be able to be discovered by searching 'covid arizona' or 'covid watch arizona'. I had to look it up on a search engine then go through an app store link on the dev's website to find it.<br> :date: __2020-09-11 05:38:37__

> Thanks for making this!<br> :date: __2020-09-10 10:11:21__

> Excellent application !<br> :date: __2020-08-24 13:16:53__

> Just what AZ needs to kick the covid! Hopefully everyone will install. I'm glad it protects privacy.<br> :date: __2020-08-19 20:42:29__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.azdhs.covidwatch.android 4 reviews"/>
</p>

> Seems to function okay but very few people know it exists and even fewer are using it. It can't be all that affective without a large number of people using it.<br> :date: __2021-02-08 19:48:02__

> Today Update<br> :date: __2020-09-08 20:52:33__

> I am going to give this a try<br> :date: __2020-09-02 08:55:19__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.azdhs.covidwatch.android 3 reviews"/>
</p>

> Says it can't detect if it continues contact app...<br> :date: __2020-12-20 16:04:55__

> It's a major flaw to have to deliberately dig for this and install. I'm not saying it should be force installed on any device but it should at /least/ be able to show up in a search 🙃<br> :date: __2020-10-09 02:43:42__

> This app can't be found using a simple search for "Covid Watch Arizona".<br> :date: __2020-08-26 04:58:02__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.azdhs.covidwatch.android 2 reviews"/>
</p>

> I don't see how this app can be helpful at all for contact tracing. Few people in Arizona I know are aware of this app, and even if they're informed about it, it doesn't even appear in a general search with keywords. Then it will randomly inform you that you have a notification and, when you click to find out what it is, it will tell you that you have no notifications. You'll have an icon that sits in your notifications for 12 hours telling you that it's looking for exposures that can't be dismissed. Also, you can't even choose Phoenix nor Maricopa County as your location despite that being the most populous region of the state; your options are Tucson, Flagstaff, and "State of Arizona" which apparently isn't even functional.<br> :date: __2021-01-13 20:07:20__

> Great idea but unclear. IMPOSSIBLE to find by simple searching for it in the app store. I had to follow internet breadcrumbs over the different sites to finally get a link to the exact app. Once here, while setting up, you need to select your location, one of which is "State of Arizona". But later it says that statewide implementation means that you can get alerts, but not alert anyone else. So if I'm in Prescott, and no one in Prescott can actually send an alert, what is the point????<br> :date: __2020-10-06 19:06:36__

> This app worked perfectly for me to begin with. Upon getting an exposure alert, I was able to view the details and severity with a simple touch. However, within the last two weeks, I noticed when I received an alert, I am unable to see the details. I am shown when it occurred, but the drop down bar showing the Transmission Risk and total time exposed is no longer available. I've tried all I can think to fix the issue, but at this point, I can no longer rely on it for accurate exposure alerts.<br> :date: __2020-09-25 01:17:53__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.azdhs.covidwatch.android 1 reviews"/>
</p>

> Was hopeful for this, but this app is *extremely* limited. With only around 10K downloads (assuming these are still installed and running), there's no way it can function effectively for contact tracing. First, this had apparently been available since August 2020? No one knows about this app. Second, there needs to be a way for users to report their own exposures to those diagnosed covid positive, not just personal diagnoses - consider medical field workers: doctors, nurses, pharmacy.<br> :date: __2021-03-05 20:29:24__

> I know I've been potentially exposed and have received no exposure notifications<br> :date: __2021-01-30 19:11:05__

> Pretty useless since statewide reporting is not available for the app. Need to change the name to UofA/ASU COVID Tracker since they're the only regions that actually work.<br> :date: __2020-12-16 16:06:21__

> Deleted immediately. Way too many permissions, microphone & other permissions are more than what is needed. Buggy. Google is awful.<br> :date: __2020-12-15 05:09:34__

> This app only works for UofA & NAU and isn't on the CDC's list so trying to find it is challenging. What are the developers waiting for, especially with the current spike in Arizona? It dosen't do any good to share this with others if no one can add there positive diagnosis in an unsupported region (meaning the rest of the state).<br> :date: __2020-11-23 16:02:59__

> Apparently, it's not available in for most of Arizona even if the menu lists Arizona along with two university systems. You need to be upfront about this. What "region" am I in and what "local" officials are you waiting for permission from? Thank you, ADHS, for replying on 10/09/20, but my point stands. There's no State of Arizona region and you need to remove that until ADHS, state and local officials, and your software developer have all made their necessary inputs to this process.<br> :date: __2020-10-19 03:19:06__


