# Coronavirus Australia
App version ``1.0.4``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="Coronavirus Australia icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Coronavirus Australia |
| **Unique identifier** | au.gov.health.covid19 |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=au.gov.health.covid19](https://play.google.com/store/apps/details?id=au.gov.health.covid19) |
| **Summary**  | Official Government Information |
| **Privacy policy** | [https://www.health.gov.au/using-our-websites/privacy](https://www.health.gov.au/using-our-websites/privacy) |
| **Latest version** | 1.0.4 |
| **Last update** | 2020-04-24 01:22:04 |
| **Recent changes** | - Improved support for push notifications<br>- Support for video content added |
| **Installs**  | 500,000+ |
| **Category** | Health & Fitness |
| **First release** | Mar 28, 2020 |
| **Size**  | 7.9M |
| **Supported Android version**  | 6.0 and up |

### Description
> You can use the Australian Government Coronavirus app to:
<br>- stay up to date with the official information and advice 
<br>- important health advice to help stop the spread and stay healthy
<br>- get a quick snapshot of the current official status within Australia
<br>- check your symptoms if you are concerned about yourself or someone else
<br>- find relevant contact information 
<br>- access updated information from the Australian Government
<br>- receive push notifications of urgent information and updates
<br>Trusted, Australian information
<br>All information in the Australian Government Coronavirus app is sourced from Australia’s leading health organisations and has undergone a quality assurance process so people can know it is safe, appropriate and relevant for Australians. 
<br>Disclaimer
<br>Whilst this app has been reviewed for clinical accuracy, the content is not a substitute for professional advice and should not be used as an alternative to professional healthcare. If you have a particular medical problem, please consult a doctor or a specialist.


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
| **Developer**  | DTA App Developer |
| **Website**  | [http://health.gov.au](http://health.gov.au) |
| **Email** | info@health.gov.au |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=DTA+App+Developer](https://play.google.com/store/apps/developer?id=DTA+App+Developer) |

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
 **android.permission<br>ACCESS_COARSE_LOCATION** | :warning:**Dangerous** | Allows an app to access approximate location. 
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 
 **com.google.android.finsky.permission<br>BIND_GET_INSTALL_REFERRER_SERVICE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | googlesyndication.com | Google LLC | :us: US | 2003-01-21 06:17:24 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | app-measurement.com | Google LLC | :us: US | 2015-06-19 20:13:31 |
 | apple.com | Apple Inc. | :us: US | 1987-02-19 05:00:00 |
 | aomedia.org | Contact Privacy Inc. Customer 1243324949 | :canada: CA | 2015-08-24 14:07:31 |
 | w3.org | W3C | :us: US | 1994-07-06 04:00:00 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | googleadservices.com | Google LLC | :us: US | 2003-06-19 16:34:53 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | crashlytics.com | Google LLC | :us: US | 2011-01-21 15:30:40 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the ISO country code equivalent of the current registered operator's MCC (Mobile Country Code)<br>
> - This application reads the device phone type value<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Telephony services abuse**
> - This application makes phone calls<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Code execution**
> - This application loads a native library<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The Coronavirus Australia app has been installed by more than **500000** times. At this time, **1285** rated the app and its average score is **3.6535432**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 677

:star::star::star::star:: 111

:star::star::star:: 141

:star::star:: 80

:star:: 273

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covid19 5 reviews"/>
</p>

> It's very useful and gives me peace of mind<br> :date: __2020-05-08 20:19:48__

> Crucial app you need to survive this disease that was definitely not released by any government or grouping of people to quell the overwhelming amount of people that are alive. This app it had too many similarities to plague Inc, but the story was the biggest failure of it all. I mean truly, who would believe our governments would release this disease on the people, it's too cruel to imagine. It's not like the powers to be around you are plotting against you. Or are they..<br> :date: __2020-05-08 02:07:04__

> I am reviewing in response to the current most highly rated negative review. TLDR this is not spyware. Storing data on Amazon Web Services (AWS) is no real concern. AWS *does* have servers in Australia. It is very stable, and any sensitive data collected by the app (which afaik is *all* voluntary) will probably be about as secure as most government services. Using AWS means 99.99% uptime (not exaggerating), that the app is available much sooner than it would be otherwise, and cheaper on tax $$<br> :date: __2020-05-06 10:36:30__

> A must have app. Works seamlessly in the background and makes me feel more confident that I will know if I've been exposed to the virus. Everyone should have it<br> :date: __2020-05-05 22:22:45__

> Let stop the spread of Covid19!<br> :date: __2020-05-05 09:30:18__

> to get us bak 2normal...<br> :date: __2020-05-04 16:02:19__

> It tells me what I need to know.<br> :date: __2020-05-04 10:09:29__

> Great app<br> :date: __2020-05-04 09:16:38__

> 2 O,44. ? Got ýi.<br> :date: __2020-05-04 04:34:31__

> Keeps me safe<br> :date: __2020-05-04 00:48:58__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covid19 4 reviews"/>
</p>

> I like<br> :date: __2020-05-07 01:23:44__

> Good<br> :date: __2020-05-01 06:29:25__

> Cant self register<br> :date: __2020-04-30 02:43:21__

> Being a high risk person I installed the app, put in details. I was told to see my gp which I did and even had the test. The app doesn't allow you to report that you have done it and for you to say that you don't have COVID19 . I think that would be something that should have been added.<br> :date: __2020-04-29 04:01:07__

> Just updated<br> :date: __2020-04-28 10:47:52__

> All I get is Aust gov site. Where is app?<br> :date: __2020-04-27 22:20:40__

> Frustratingly good<br> :date: __2020-04-27 14:40:16__

> Very useful. Concise, well presented. Told me what l need to know. Thanks<br> :date: __2020-04-27 03:26:44__

> Thankyou for getting this app. Now everyone pls get it<br> :date: __2020-04-26 11:13:44__

> I'm giving it 4 stars as I think it's a good idea for tracking the virus but it will only work if others download it. I need it as I deliver food to 15 - 35 people six days a week, and I certainly would like to know who I am coming across, I also think all retail workers should definately download it for their own safety. I don't give a toss about its privacy it's a lot less invasive than Google Maps & I'm on that everyday, yes it will have to iron out problems but that's ok.<br> :date: __2020-04-26 07:39:42__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covid19 3 reviews"/>
</p>

> Never have received the pin to open it<br> :date: __2020-05-08 01:20:55__

> Won't download past 97%<br> :date: __2020-05-07 12:21:06__

> Mostly disappointed that in all government media announcements they just say 'download the app' without specifying the name of the app clearly. There are several COVID-19 apps out there now. Give it a distinctive name.<br> :date: __2020-05-07 10:02:42__

> An interactive app would be far more useful. INPUT Activity I want to undertake? Personal details? Employment details? Reason for activity? PROCESS Verification process. OUTPUT. Approval /Denial /More information - contact Barcode issued to applicant on approval. Applicant issued with a description of any special requirements. Eg: FIFO to travel Site - WA - NSW - WA - site Can the process be undertaken? ANS Special requirements (isolation and period and process for each state)<br> :date: __2020-05-05 12:10:07__

> Laggy on the opening and update of information but enough for quick access check .<br> :date: __2020-05-05 09:48:51__

> Dear Gov Oz good overall but if time ask those negative reviews e.g. force closure what system they use....keep up good work... we pray to Jesu Mary's Health bless us<br> :date: __2020-05-04 13:56:47__

> Lite info and few updates ... than news media<br> :date: __2020-05-01 10:01:51__

> Okay, this app keeps consumers informed and offers a dialect about what to do if you need to do something/anything. However, the app has zero allowance for inquiry; no room to question the ongoing situation. I don't disregard the media as an institution but its reporter's are sometimes off the beaten path and want to break a story rather than provide valuable information. Things will get better, stay vigilant and patient.<br> :date: __2020-04-29 14:26:47__

> Is this the app to detect the virus?<br> :date: __2020-04-27 02:37:12__

> This app brings together all the gov websites.. We'll done.. But it's COVIDSafe you want. That tracks your interaction. Real value is knowing the active cases and our exposure.. I really want to keep safe<br> :date: __2020-04-27 01:21:15__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covid19 2 reviews"/>
</p>

> Not enough real time information I would like to see more statistics especially our Reff number<br> :date: __2020-05-07 11:17:36__

> Release the source code of both client and server and more of us will install this app... It looks like the app generates and uploads a private/public key pair and uploads one or the other to a central server and associates it directly to a user, other users when testing positive can upload their contact history to the server and matches that data to details of other users they came into contact with directly implicating the contacts, private user data should not be uploaded without consent.<br> :date: __2020-05-04 12:39:48__

> Confusing<br> :date: __2020-05-04 09:43:14__

> Will not download on my phone<br> :date: __2020-05-01 08:18:24__

> Takes forever to download. Been trying for 2 days now.<br> :date: __2020-04-29 10:31:12__

> I downloaded it but still do not know if it is actually working.<br> :date: __2020-04-27 03:53:37__

> Please add a prominent link to the covidsafe app.<br> :date: __2020-04-27 00:50:53__

> Update too late every day<br> :date: __2020-04-27 00:17:59__

> Buggy as!<br> :date: __2020-04-26 13:48:12__

> Not the new tracker app i was seeking<br> :date: __2020-04-26 11:00:11__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covid19 1 reviews"/>
</p>

> Greetings from Jesper<br> :date: __2020-05-10 04:12:08__

> Terrible<br> :date: __2020-05-10 03:33:23__

> Cost a fortune in data<br> :date: __2020-05-09 02:33:02__

> Chews through the battery.<br> :date: __2020-05-08 00:01:52__

> Covid 19 is fake check the news<br> :date: __2020-05-07 14:02:27__

> Does it do anything????<br> :date: __2020-05-07 11:14:38__

> Only sheep download this app because people are stupid. Stuff the government they just want to track us if not why did they chose to have a data retention law passed think about it<br> :date: __2020-05-07 00:19:33__

> This app is never up to date! Useless!<br> :date: __2020-05-06 17:16:15__

> I am trying to register this is stupid<br> :date: __2020-05-06 10:47:22__

> Drain heaps of battery<br> :date: __2020-05-06 02:57:56__


