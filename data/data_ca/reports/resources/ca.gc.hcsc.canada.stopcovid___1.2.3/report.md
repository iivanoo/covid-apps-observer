# COVID Alert - Let’s protect each other
App version ``1.2.3``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="COVID Alert - Let’s protect each other icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | COVID Alert - Let’s protect each other |
| **Unique identifier** | ca.gc.hcsc.canada.stopcovid |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=ca.gc.hcsc.canada.stopcovid](https://play.google.com/store/apps/details?id=ca.gc.hcsc.canada.stopcovid) |
| **Summary**  | Health Canada Exposure Notification |
| **Privacy policy** | [https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19/covid-alert/privacy-policy.html](https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19/covid-alert/privacy-policy.html) |
| **Latest version** | 1.2.3 |
| **Last update** | 2021-03-09 20:10:22 |
| **Recent changes** | - Updated button to access the app menu and redesigned frequent buttons within the menu. |
| **Installs**  | 1,000,000+ |
| **Category** | Health & Fitness |
| **First release** | Jul 29, 2020 |
| **Size**  | 44M |
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
> - This application loads a native library: 'Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;'<br>
> - This application executes a UNIX command<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The COVID Alert - Let’s protect each other app has been installed by more than **1000000** times. At this time, **7837** rated the app and its average score is **3.5949044**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 3984

:star::star::star::star:: 838

:star::star::star:: 679

:star::star:: 529

:star:: 1807

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="ca.gc.hcsc.canada.stopcovid 5 reviews"/>
</p>

> Safe feeling<br> :date: __2021-03-13 18:20:09__

> It make it us alert<br> :date: __2021-03-11 21:13:27__

> Covid19<br> :date: __2021-03-11 06:41:18__

> Very good app just how you been exposed covt19<br> :date: __2021-03-09 01:00:03__

> This is a very important app to have<br> :date: __2021-03-08 08:24:28__

> Teamgoogle@google com help my team<br> :date: __2021-03-07 06:34:16__

> Definitely a needed app covid has changed everyone's lives and the world we live in this app hell yeah we need it so everyone please get it 🙏🙌❤👍 this app everyone should have ..<br> :date: __2021-03-06 16:46:57__

> Let's do this! I do love the fact that the code is up on GitHub (which I've checked out and it's really well organised.) And kudos to the team for patiently responding to comments, even if most are misguided.<br> :date: __2021-03-05 20:00:46__

> I like it good and great<br> :date: __2021-03-05 19:40:52__

> Excellent<br> :date: __2021-03-03 06:21:35__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="ca.gc.hcsc.canada.stopcovid 4 reviews"/>
</p>

> Not complicated;informative, has updates on the virus (s)<br> :date: __2021-03-08 17:11:05__

> cool<br> :date: __2021-03-01 12:09:51__

> No problems to report<br> :date: __2021-03-01 10:58:30__

> Stay home and be safe<br> :date: __2021-02-28 04:26:50__

> It's a good option to have<br> :date: __2021-02-21 03:52:48__

> I like this app and think it is a necessary tool in our fight against Covid. However I am concerned that it hasn't been updated yet to take into account the new variants. 2 meters for 15 minutes doesn't seem safe anymore. I want to know whether I was 5 minutes within a 3 m distance of someone infected (or whatever parameters health authorities think would be precautionary taking into account the new variants).<br> :date: __2021-02-18 04:17:26__

> Did as you recommended. Force quit the app then restarted! The annoying number 1 gone! Thank you so much for your help! I truly think this is a wonderful addition in helping to combat this pandemic. I hope more people download it. :)<br> :date: __2021-02-18 01:27:22__

> Idk if this even works<br> :date: __2021-02-16 23:43:32__

> The way it says that it collects the data, it won't be able to notify you of an exposure as it's happening, mainly due to the careful way they have to apply the tracking tech in order to sustain your privacy, or people get upset. It can only tell you once it has been able to calculate exposure within 2 meters for 15 minutes, and it can't know that until it determines if it WAS during the contagious timeline, which isn't known until that data has been accurately reported by the cantagious patient<br> :date: __2021-02-16 12:36:52__

> I downloaded this app by mistake And downloaded self isolation form by mistake how to rectify it i am completely fine with no symptoms even i never came in touch with anyone just doing quarantine for 14 days i do have arrive can app only<br> :date: __2021-02-13 06:38:54__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="ca.gc.hcsc.canada.stopcovid 3 reviews"/>
</p>

> Keeps asking to switch on the phone Bluetooth even though it is always on. Uninstalling as not working but just annoying.<br> :date: __2021-03-14 08:08:52__

> It is 100% voluntary COVID reporting which means that infected people will have to notify the app of their infection. What if they don't?<br> :date: __2021-03-13 21:01:17__

> Does this app work in alberta yet? Specifically jasper ab?<br> :date: __2021-03-11 16:33:37__

> Still not available for Alberta, it's been half a year<br> :date: __2021-03-07 20:07:25__

> I strongly support the principle behind this app and all measures to protect the users' privacy however it would be a HUGE asset to be alerted with a date of exposure, if not a date and time. It would help users identify how long to wait to get tested (asymptomatic individuals should isolate but wait 3-5 days to get swabbed to minimize false negatives) as well as to help with contact tracing. It would also possibly help users identify which activities they are doing are higher risk<br> :date: __2021-03-07 18:17:12__

> When will BC be added?? I've had this app for over 8 month.<br> :date: __2021-03-07 09:41:01__

> Only found out of exposure contact by checking app, was not notified for over 12 hours that I had been exposed.<br> :date: __2021-02-27 21:30:30__

> Stopped working from October to January. Kind of pointless if it doesn't work.<br> :date: __2021-02-26 23:04:27__

> My understanding is that THIS app is for Canadians? How come america doesnt have something like it?<br> :date: __2021-02-25 03:03:04__

> Government starts to use online screening before entering the mall in Ontario. Why not wisely to add the screening in this app and encourage more people to use this. Plus it is waste of time to ask people enter the code in the app IF they test positive. This app should link with the health card system, if they have covid test, it will show on here both negative n positive. So far, I don't see how useful this app is. But it can be useful if add more things in it.<br> :date: __2021-02-24 14:03:28__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="ca.gc.hcsc.canada.stopcovid 2 reviews"/>
</p>

> Just hope no one forgets their phone!<br> :date: __2021-03-06 11:38:26__

> I have had this App on my phone since 08/20. Do to the nature of my job I frequent Toronto and Ottawa, both hot spots. Here we are in March, 6 months of using this app, yet not one single notification. I highly doubt it's effectiveness.<br> :date: __2021-03-01 16:19:06__

> Great idea, but only 5 people in Canada are using it. Canada doesn't know how to reach out to its masses and connect with them on a personal level<br> :date: __2021-02-23 01:23:19__

> Not sure how useful this app is... This app is like the notorious pet rock - either does nothing or appears to do nothing. It would give a better sense of reliability if it reported to me how many other unique devices my phone came in the vicinity of and how many devices are reporting in the preceeding 24h period in my province / city. This app is worse than useless if I am the only one using it in all of Ontario. I'd rather free up space & release the processing power that this app is wasting.<br> :date: __2021-02-18 18:06:07__

> A few things need to change: 1) Allow opt-out of data collection 2) Make all non-exposure notification icons grey. Having a red icon pop up on a regular notification is startling. 3) Show relevant info when tapping a notification about new features. I tapped the one about data collection expecting an explanation but it just opened the app, I had to go to the gov't site and find that info myself.<br> :date: __2021-02-18 06:17:09__

> 1. Don't want to have location on all the time just for this app. My phone, along with many others, can't update to Android 11. 2. Without the app it's 14 days isolation from last contact with a positive case. With the app it's 14 days *from the date you received the notification*. See saskatchewan.ca/covid19-apps . If the website is wrong, get them to fix it. 3. Now the app is collecting a lot more data. They say it isn't tied to your IP but how can you know for sure?<br> :date: __2021-02-12 16:03:16__

> Since the decisions to centrally collect metadata, I am no longer comfortable having the app installed on my device.<br> :date: __2021-02-11 20:55:40__

> It doesn't work on my phone:(<br> :date: __2021-02-09 02:32:45__

> Zero, but gave it a 2 for effort. It would be great to see the statistics on the number of events transpired, and if this has done anything or is just another waste of money. Thinking its the latter? Who is going to log in, as exposed, then go out for a walk to a crowded area? Million downloads? Hmmm.<br> :date: __2021-02-07 16:46:01__

> I support the idea of this app but I don't beleive it works. What use is it if nobody whom has received a positive test result shares this with the app? I have been very near to multiple cases over the past 2 months due to an outbreak at work and I've not had a single alert to this fact from this app. Clearly none of those cases were reported. I would be interested in knowing how many positive cases have been documented in my area vs how many were self-reported to this app.<br> :date: __2021-02-07 12:18:08__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="ca.gc.hcsc.canada.stopcovid 1 reviews"/>
</p>

> Kept prompting me to turn it on even though I had notifications for this app turned off, so I got rid of it<br> :date: __2021-03-13 17:01:05__

> Useless<br> :date: __2021-03-13 00:54:42__

> App doesn't work of samsung s 20 ultra<br> :date: __2021-03-12 22:37:40__

> Totally useless in BC. Even now there is no reporting here.<br> :date: __2021-03-12 03:03:12__

> No one seems to be using it so I don't really have confidence it is working to keep me updated on exposures.<br> :date: __2021-03-10 15:45:41__

> App still not active in my province!! 9 months into covid and still not available in BC. Please sort it out!!! Update, well over a year later still does not work, appalling.<br> :date: __2021-03-10 05:44:07__

> Totally useless as nobody inputs that they are positive tested.<br> :date: __2021-03-09 18:12:45__

> Still says not available for use in my area (vancouver island BC)<br> :date: __2021-03-09 06:28:37__

> Wow...still doesn't want to work on my Samsung Galaxy S10+. What's up with that?<br> :date: __2021-03-05 23:08:49__

> Useless. Only tracks people who have the app too.<br> :date: __2021-03-03 14:26:15__


