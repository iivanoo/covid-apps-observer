# Coronavirus Australia
App version ``1.4.5``

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
| **Latest version** | 1.4.5 |
| **Last update** | 2020-07-30 01:35:14 |
| **Recent changes** | - Graphs are now interactive<br>- Clinic finder refinements<br>- Miscellaneous bug fixes and improvements |
| **Installs**  | 500,000+ |
| **Category** | Health & Fitness |
| **First release** | Mar 28, 2020 |
| **Size**  | 22M |
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
 | <img src="screenshot_4.png" alt="screenshot" width="300"/>  | <img src="screenshot_5.png" alt="screenshot" width="300"/>  | <img src="screenshot_6.png" alt="screenshot" width="300"/>  | 


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

The Coronavirus Australia app has been installed by more than **500000** times. At this time, **1491** rated the app and its average score is **3.5945945**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 755

:star::star::star::star:: 141

:star::star::star:: 161

:star::star:: 100

:star:: 332

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covid19 5 reviews"/>
</p>

> Excellent up to date information. Great initiative and helpful<br> :date: __2020-08-09 02:10:05__

> It seems to work as designed 😷🤸<br> :date: __2020-08-06 10:18:45__

> Excellent News and updates sent to you and the information contained herein is helpful and informative 👍<br> :date: __2020-08-03 02:50:31__

> It's states 'unable to load lastest updates. Pushing 'try again doesnt work'. I've reinstalled it and same problem. Thanks for creating an app even if it's a mobile wrapper at short notice. I've got WhatsApp information working so that still helpful.<br> :date: __2020-07-30 08:42:47__

> Good app to keep people up to date about coronavirus and other things too!<br> :date: __2020-07-18 03:58:59__

> Anything that can keep me updated on how we're going i'm all for.<br> :date: __2020-07-09 11:37:48__

> I came see the corona people<br> :date: __2020-07-06 06:40:57__

> Great if everyone uses it<br> :date: __2020-07-06 05:12:09__

> Good information in the links. It was great for registering my isolation.<br> :date: __2020-06-29 00:49:18__

> I don't think that I do not know anyone with these viruses....thirty five given star's for each of all of the features....<br> :date: __2020-06-27 08:53:35__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covid19 4 reviews"/>
</p>

> It's good what is f..K going on ?<br> :date: __2020-08-04 08:35:34__

> Its wonderful app it would be amazing if you can add option that shows new cases in every state seperatly and not just total of whole Australia.<br> :date: __2020-08-03 12:49:09__

> Works well and is informative<br> :date: __2020-07-04 22:02:51__

> I'm thinking big box around the end of my bed = vr. Has potential if anything. He won't. / Rub my forehead LatcH<br> :date: __2020-06-16 09:18:45__

> Would be great if you could also put how many active cases there are.<br> :date: __2020-05-21 00:11:52__

> Works as expected, an information manager, not a source (otherwise the app would need updating daily). Helps to get at relevant, reliable information, without needing to hunt around the web myself to find it.<br> :date: __2020-05-13 10:32:15__

> Good<br> :date: __2020-05-11 11:25:39__

> I like<br> :date: __2020-05-07 01:23:44__

> Good<br> :date: __2020-05-01 06:29:25__

> Cant self register<br> :date: __2020-04-30 02:43:21__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covid19 3 reviews"/>
</p>

> Current version will not work because it thinks my battery optimisation is on - it is off!! Please fix asap as I want a working app.<br> :date: __2020-08-03 10:44:31__

> Pros: good to know the official safe links here. Cons: it's really just a collection of web links, nothing more.<br> :date: __2020-07-14 00:47:47__

> I'm looking for my location as my mum said there's been more cases where I live but it only gives U the choice to see Australia wide and not what U want to see I wanted to see my part of Victoria but it only covers Victoria itself and other places it would be good if it was more in depth<br> :date: __2020-07-02 17:02:12__

> Only used occasionally as it is quite bitsy in that finding info isn't that intuitive. Most concerning is that finding specific details about Victoria is a link to a powerbi report that is almost impossible to navigate on a phone, the point of the app. If you want to view graphs and charts, find your local municipalities etc, then I'd suggest you head for a PC that it was built for the job. Interactive charts are a good concept but not when prepared for a PC and viewed on a phone.<br> :date: __2020-06-19 13:30:45__

> Keeps turning itself off!<br> :date: __2020-05-19 04:42:12__

> It hasn't updated. Supposed to update at 9:00 AM daily.<br> :date: __2020-05-14 01:15:17__

> Never have received the pin to open it<br> :date: __2020-05-08 01:20:55__

> Won't download past 97%<br> :date: __2020-05-07 12:21:06__

> Mostly disappointed that in all government media announcements they just say 'download the app' without specifying the name of the app clearly. There are several COVID-19 apps out there now. Give it a distinctive name.<br> :date: __2020-05-07 10:02:42__

> An interactive app would be far more useful. INPUT Activity I want to undertake? Personal details? Employment details? Reason for activity? PROCESS Verification process. OUTPUT. Approval /Denial /More information - contact Barcode issued to applicant on approval. Applicant issued with a description of any special requirements. Eg: FIFO to travel Site - WA - NSW - WA - site Can the process be undertaken? ANS Special requirements (isolation and period and process for each state)<br> :date: __2020-05-05 12:10:07__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covid19 2 reviews"/>
</p>

> Was a pretty useless app, can find out the same info online or by watching the news<br> :date: __2020-07-27 04:56:10__

> Never been able to open app<br> :date: __2020-07-08 12:03:11__

> I'm sure it's a great app but there is constantly a reminder in my notifications that I can't get rid of. Very very frustrating.<br> :date: __2020-05-28 18:16:57__

> Not enough real time information I would like to see more statistics especially our Reff number<br> :date: __2020-05-07 11:17:36__

> Release the source code of both client and server and more of us will install this app... It looks like the app generates and uploads a private/public key pair and uploads one or the other to a central server and associates it directly to a user, other users when testing positive can upload their contact history to the server and matches that data to details of other users they came into contact with directly implicating the contacts, private user data should not be uploaded without consent.<br> :date: __2020-05-04 12:39:48__

> Confusing<br> :date: __2020-05-04 09:43:14__

> Will not download on my phone<br> :date: __2020-05-01 08:18:24__

> Takes forever to download. Been trying for 2 days now.<br> :date: __2020-04-29 10:31:12__

> I downloaded it but still do not know if it is actually working.<br> :date: __2020-04-27 03:53:37__

> Please add a prominent link to the covidsafe app.<br> :date: __2020-04-27 00:50:53__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covid19 1 reviews"/>
</p>

> Very little news from the app, but a lot happening in Australia.<br> :date: __2020-08-09 13:41:30__

> Info is days out of date, making this app useless. At a time when we need up to the minute info, this is woeful. It contributes to people doing the wrong thing.<br> :date: __2020-08-05 05:56:22__

> Poor, installed for first time. Did not load. Did bot work<br> :date: __2020-08-03 18:24:02__

> App doesn't load. Says can't get latest info.<br> :date: __2020-08-03 17:21:19__

> Useless.<br> :date: __2020-07-31 11:23:29__

> The app turns itself off.<br> :date: __2020-07-27 00:14:24__

> I get an alert, and when i click on it, i cant see the alert. It's probably buried in there somewhere under one of the options, but i cant find it. Aweful user interface. Maybe hire a UX consultant when you get around to addressing this in future.<br> :date: __2020-07-23 09:22:41__

> 3.8 Million dollars to create this app? Australia tax payers got extorted!<br> :date: __2020-07-21 12:02:42__

> A great idea but shame we have the morons out of touch with reality running the states and country! I had this installed but with restrictions continuing no point continuing with this app!<br> :date: __2020-07-11 04:39:49__

> Absolute rubbish<br> :date: __2020-07-10 12:00:01__


