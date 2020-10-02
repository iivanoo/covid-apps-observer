# COVIDCare NI
App version ``2.1``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="COVIDCare NI icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | COVIDCare NI |
| **Unique identifier** | net.hscni.covid19ni |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=net.hscni.covid19ni](https://play.google.com/store/apps/details?id=net.hscni.covid19ni) |
| **Summary**  | COVIDCare NI is a coronavirus symptom check with the latest advice and guidance |
| **Privacy policy** | [https://www.health-ni.gov.uk/publications/covid-19-app-privacy-notice](https://www.health-ni.gov.uk/publications/covid-19-app-privacy-notice) |
| **Latest version** | 2.1 |
| **Last update** | 2020-07-29 23:29:13 |
| **Recent changes** | · Performance Improvements and Bug Fixes<br>· Featured articles on mental health and general advice<br>· Latest regulations and easing of lockdown guidance <br>· Information on how to get tested and testing facilities<br>· COVID-19 statistics<br>· Isolation timer updated to include isolation following a positive test result and isolation due to close contact with someone with COVID-19<br>· Ability to add household members symptoms to dashboard<br>· Improved navigation |
| **Installs**  | 50,000+ |
| **Category** | Medical |
| **First release** | Mar 24, 2020 |
| **Size**  | 59M |
| **Supported Android version**  | 4.2 and up |

### Description
> Overview
<br>The COVIDCare NI app has been developed by Digital Health and Care NI in partnership with Health & Social Care, the Public Health Agency and the Department of Health.
<br>The app has been designed to help the public in Northern Ireland keep up to date with the latest advice on the COVID-19 pandemic, helping you to:
<br>Check if you or someone in your household has coronavirus symptoms.
<br>Access personalised advice based on your answers to the symptom check questions.
<br>Decide if you need clinical advice and how to access it.
<br>Easily find links to trusted information resources on COVID-19 advice and mental health resources.
<br>Self-isolate if you have symptoms by checking the self-isolation timer for both yourself and your household.
<br>Search current advice by using a search function of FAQs.
<br>We continue to update the app with new features based on feedback from citizens in Northern Ireland and will continue to ensure app users get access to the most up to date headlines and changes in the advice and guidance.
<br>Things are moving quickly with the pandemic so you may need to come back to refresh your app regularly. We’ll let you know when this is necessary.
<br>Thank you for your support in helping us project your family, friends and community.
<br>Why use the app?
<br>The app is available for use in Northern Ireland to all individuals who are currently residing in Northern Ireland.
<br>Data Security
<br>The app does not collect any personally identifiable information.
<br>We will collect information related to the postcode and age of the user to help us track the impact of COVID-19 in Northern Ireland.
<br>This will help us to plan services and ensure that resources are directed to the areas of greatest need.


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
| **Developer**  | Health & Social Care Northern Ireland |
| **Website**  | [https://www.publichealth.hscni.net/](https://www.publichealth.hscni.net/) |
| **Email** | hscdhcni@gmail.com |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Health+%26+Social+Care+Northern+Ireland](https://play.google.com/store/apps/developer?id=Health+%26+Social+Care+Northern+Ireland) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Android10, version 10 (API level 29) |
| **Effective target Android version**  | Android10, version 10 (API level 29) |
| **Minimum supported Android version**  | Jelly Bean, version 4.2.x (API level 17) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>ACCESS_WIFI_STATE** | Normal | Allows applications to access information about Wi-Fi networks. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 
 **net.hscni.covid19ni.permission<br>C2D_MESSAGE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | w3.org | W3C | :us: US | 1994-07-06 04:00:00 |
 | microsoft.com | Microsoft Corporation | :us: US | 1991-05-02 04:00:00 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the ISO country code equivalent of the current registered operator's MCC (Mobile Country Code)<br>
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>

**Code execution**
> - This application loads a native library: 'monodroid'<br>
> - This application loads a native library: 'monosgen-2.0'<br>
> - This application loads a native library: 'xamarin-app'<br>
> - This application loads a native library: 'xamarin-debug-app-helper'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The COVIDCare NI app has been installed by more than **50000** times. At this time, **321** rated the app and its average score is **3.46**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 157

:star::star::star::star:: 35

:star::star::star:: 19

:star::star:: 16

:star:: 93

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="net.hscni.covid19ni 5 reviews"/>
</p>

> Very poor<br> :date: __2020-09-08 20:21:41__

> Amazing and informative app. PLEASE NOTE THIS APP IS FOR NORTHERN IRELAND ONLY. So don't think this will work in other parts of the UK or the world, however it is compatible with the republic of ireland version.<br> :date: __2020-08-01 00:43:11__

> Easy to use and informative<br> :date: __2020-07-30 19:39:35__

> Excellent<br> :date: __2020-07-30 15:56:15__

> Excellent and informative<br> :date: __2020-06-30 14:11:20__

> Amazing the p we people who it doesn't work you need to go to the NHS website or gothirmont web don't give the 1 star if do you are ungrateful and it probably your phone. 😂😂😂<br> :date: __2020-06-06 22:45:27__

> Easy to use informative and source of good advice and information specific for NI residents.<br> :date: __2020-06-06 10:56:34__

> If you are from UK but not from NI, this app is not for you as it may not match the advice your local government is giving. Crucially, this is the advice of the Northern Irish HSC (NHS equivalent).<br> :date: __2020-06-02 13:07:43__

> I don't live in NI, and I don't have any covid symptoms but I was curious to see how this app worked, so I used an NI postcode and 'role-played'. This is great; clear and concise, with efficient links through to local health service info. We could definitely benefit from an app like this in mainland UK. Hats off to the developers! To those giving 1 star reviews, I note many of you do not live in NI & did not notice that the app was, therefore, not designed for you!!!<br> :date: __2020-05-27 19:31:24__

> 🌍🌎🌏😷<br> :date: __2020-05-20 18:53:50__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="net.hscni.covid19ni 4 reviews"/>
</p>

> Would a regional breakdown of new cases<br> :date: __2020-07-31 00:38:27__

> Seems promising at first glance, easy to use with good range of features. It also let's you use the app on behalf of someone else which might be good for elderly/and or the less technical, visually impaired or less able bodied. What accessibility features does it conform to? One issue I had was when I filled in the symptom checker flow. The last stage presents a blank yellow screen and it's not intuitive that you have to close or go back to see suggestions<br> :date: __2020-07-30 18:59:15__

> Could do with more updates. But pretty good for sign posting<br> :date: __2020-06-29 12:39:16__

> A bit empty but good overall!<br> :date: __2020-06-17 22:06:54__

> Manchester not,,,,,<br> :date: __2020-06-11 21:25:59__

> Quite good app as has a symptoms checker and some info, advice and statistics.. However doesn't have what I actually downloaded it for which was to find out about updates to current regulations and recovery plan such as easing of lockdown rules etc.. Have to search for this and then visit nidirect website for this info..<br> :date: __2020-06-07 21:55:20__

> Good app<br> :date: __2020-05-06 23:22:23__

> Great app, though the virtual assistant could use some more specific information / ai training. Thanks for making this.<br> :date: __2020-04-02 10:48:28__

> Handy advice in scarey times<br> :date: __2020-04-01 21:27:09__

> Hopefully this could be a very powerful way of identifying cv19 hotspots.<br> :date: __2020-03-31 20:18:01__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="net.hscni.covid19ni 3 reviews"/>
</p>

> I have just downloaded this app can anyone please tell me if it's free or is there a payment on it<br> :date: __2020-08-11 23:00:25__

> Who owns this App is it a private profit making company? If so is this another privatisation by the back door which is all too common with the NHS overall in recent years Own it Don't rent it!<br> :date: __2020-05-06 15:23:14__

> I was looking for statistics on the spread in NI as we are lumped in with the UK in official statistics, this app doesn't seem to have that. Useful advice but nothing I haven't heard 1000 times already - those who aren't listening won't be downloading the app anyway.<br> :date: __2020-04-11 15:32:23__

> N/A<br> :date: __2020-04-10 00:07:41__

> Helps a bit but I still rang 111 help line<br> :date: __2020-04-07 03:46:29__

> Only available in Ireland!<br> :date: __2020-04-02 18:40:10__

> Doesn't work in the UK<br> :date: __2020-04-01 08:16:36__

> Only available in Northern Ireland 🇮🇪 😢<br> :date: __2020-03-26 13:18:23__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="net.hscni.covid19ni 2 reviews"/>
</p>

> Not in NI but won't load 😔<br> :date: __2020-06-20 10:41:04__

> Sporadic updates. Better to just use google.<br> :date: __2020-05-26 17:42:14__

> No updated figures since April 30<br> :date: __2020-05-04 17:55:33__

> Sorry 2 stars only. App not for England or Wales. Advertised on the news as available all over UK and this is not so. So I've uninstalled it.<br> :date: __2020-04-11 23:08:08__

> Why is this only available in NI and not available anywhere else I think its deplorable as we are all dealing with this and not just NI<br> :date: __2020-04-10 14:03:09__

> Nothing new or useful here.<br> :date: __2020-04-06 19:46:22__

> My is it only NI<br> :date: __2020-03-26 08:24:52__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="net.hscni.covid19ni 1 reviews"/>
</p>

> doesn't load past the first screen<br> :date: __2020-09-26 17:06:32__

> App won't open once installed :-(<br> :date: __2020-09-24 10:53:15__

> only works on recent phones, completely misses the point...must work everywhere or it is pointless.<br> :date: __2020-08-11 12:19:23__

> It came to stop as I had no tracing ability and said no more.<br> :date: __2020-07-31 23:15:28__

> doesn't work...!<br> :date: __2020-07-31 22:10:26__

> This is not the official app for Northern Ireland COVID19. STOPCOVID NI is the correct app<br> :date: __2020-07-31 19:47:35__

> unfortunately, COVIDCard NI Has stopped so the app is useless as it just crashes And i wish people could read the words NI 'Northern Ireland' and stop moaning that its not working in your area as it clearly says Northern Ireland in the Description a few times on the download page. only problem i have with app is it don't load and just crashes.<br> :date: __2020-07-31 13:04:30__

> Slow<br> :date: __2020-07-30 23:13:46__

> Can't access the tracker app via the link on this app. Get error 403. No point in having this app if not linked to tracker app<br> :date: __2020-07-30 20:17:27__

> Crashes<br> :date: __2020-07-30 20:02:29__


