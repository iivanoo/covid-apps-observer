# CO Exposure Notifications
App version ``minted142004``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="CO Exposure Notifications icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | CO Exposure Notifications |
| **Unique identifier** | gov.co.cdphe.exposurenotifications |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=gov.co.cdphe.exposurenotifications](https://play.google.com/store/apps/details?id=gov.co.cdphe.exposurenotifications) |
| **Summary**  | Colorado&#39;s official Exposure Notification app. |
| **Privacy policy** | [https://www.colorado.gov/pacific/cdphe/exposure-notifications-privacy-policy](https://www.colorado.gov/pacific/cdphe/exposure-notifications-privacy-policy) |
| **Latest version** | minted142004 |
| **Last update** | 2021-01-13 22:52:40 |
| **Recent changes** | Bug fixes and performance improvements |
| **Installs**  | 100,000+ |
| **Category** | Medical |
| **First release** | Oct 16, 2020 |
| **Size**  | 9.9M |
| **Supported Android version**  | 5.0 and up |

### Description
> CO Exposure Notifications is the official Exposure Notifications app of Colorado and the Colorado Department of Public Health and Environment. Exposure Notifications is a voluntary new service developed in partnership with Google and Apple to help slow the spread of COVID-19. No GPS, location information or personal identifiers will ever be collected, stored or shared by this service. 
<br>CO Exposure Notifications can quickly notify you if you've likely been exposed to COVID-19. Knowing about a potential exposure allows you to reduce the risk to your family, friends, neighbors and community.
<br>By enabling Exposure Notifications, whenever you are within 6 feet of someone for at least 10 minutes, both phones will exchange secure, anonymous tokens using Bluetooth. If another user you’ve been near tests positive for COVID-19, they can upload their result to the app which will send a push notification to you and anyone else their phone has exchanged tokens with recently, notifying you to a possible exposure. 
<br>If you test positive, you can easily and anonymously notify others to help stop the spread of COVID-19. 
<br>To learn more, please visit https://covid19.colorado.gov/Exposure-notifications


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
| **Developer**  | Colorado Department of Public Health & Environment |
| **Website**  | [https://covid19.colorado.gov/Exposure-notifications](https://covid19.colorado.gov/Exposure-notifications) |
| **Email** | CO_Exposure_Notifications@state.co.us |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Colorado+Department+of+Public+Health+%26+Environment](https://play.google.com/store/apps/developer?id=Colorado+Department+of+Public+Health+%26+Environment) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | - |
| **Effective target Android version**  | - |
| **Minimum supported Android version**  | Lollipop, version 5.0 (API level 21) |
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


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the ISO country code equivalent of the current registered operator's MCC (Mobile Country Code)<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Code execution**
> - This application loads a native library: 'prioclient'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The CO Exposure Notifications app has been installed by more than **100000** times. At this time, **591** rated the app and its average score is **3.2**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 273

:star::star::star::star:: 29

:star::star::star:: 47

:star::star:: 29

:star:: 213

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.co.cdphe.exposurenotifications 5 reviews"/>
</p>

> Awesome<br> :date: __2021-02-02 10:22:45__

> Glad its her<br> :date: __2021-02-02 00:56:04__

> good<br> :date: __2021-01-31 21:50:12__

> This app. does what it says<br> :date: __2021-01-18 07:59:50__

> Amazing<br> :date: __2021-01-10 02:04:49__

> Thanfully I have had no notifications but this is a great help for Colorado to trace and inform.<br> :date: __2021-01-06 02:45:40__

> Cool yo<br> :date: __2020-12-25 01:47:43__

> Good<br> :date: __2020-12-24 10:54:23__

> It 's is good thing for you get back on the right way for think about you life you never know if it hapin to you or not i think you can look in toi like be happy to be live today but god can tell you if it is time or not from you loving friend luther mosbarger<br> :date: __2020-12-20 08:40:31__

> So excited to have an app to help inform about potential exposures. Thank you, CO DPHE!!<br> :date: __2020-12-18 04:52:08__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.co.cdphe.exposurenotifications 4 reviews"/>
</p>

> Thanks keep us informed?<br> :date: __2021-02-05 23:11:31__

> Dunno if there's anything I can reasonably say about it useful.<br> :date: __2021-01-28 03:03:37__

> Not sure if it works. Haven't received any notifications after nearly three weeks. There is likely not enough people using this app, and the ones who do use it also use masks and social distancing. It's the ones that don't (use masks, social distance or use this app) you gotta watch out for.<br> :date: __2020-12-18 07:25:48__

> It's helpful<br> :date: __2020-12-07 07:54:07__

> I would like the app to have some way to tell me that I have exchanged tokens with someone, maybe giving me a total for a day. No details, just some indication that the app is doing its job.<br> :date: __2020-11-20 08:25:57__

> It does work for sharing a positive result! But don't go into the app because you'll get stopped at the verification code part. Instead wait for a text message from the health department - click on that link and follow the steps. It does share that way! You'll even see evidence that it was shared in the app. Would have given 5 stars but no explanation about the verification code or follow up text was given.<br> :date: __2020-11-19 19:19:46__

> Interesting stuff<br> :date: __2020-11-03 04:21:26__

> Great concept but kills my battery. I do have an old phone though so that may be the issue.<br> :date: __2020-10-27 15:53:56__

> I had trouble getting the notifications to work like a lot of people had posted, I uninstalled and reinstalled the app and it worked the next time. Not sure what causes this. Glad we have some form of contact tracing!<br> :date: __2020-10-26 03:29:29__

> The title makes it sounds like a carbon monoxide detector -why no mention of COVID-19 or "infectious disease"?<br> :date: __2020-10-26 02:43:35__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.co.cdphe.exposurenotifications 3 reviews"/>
</p>

> Didn't give me the ability to alert potential contact (button didn't work)<br> :date: __2021-01-02 06:48:03__

> Like<br> :date: __2020-12-12 07:54:21__

> I guess a good app but nobody in my area seems to be using it or posting a positive result in Pueblo County or other counties that I travel to for my job delivering parts, go far as Lamar, west to the San Luis Valley and South to Walsenburg, Trinidad and into New Mexico and you're telling me that I have not been near someone with a positive test result????<br> :date: __2020-12-11 20:39:25__

> Haven't been able to get much info<br> :date: __2020-12-06 18:50:05__

> Called county health department to ask about notification & special code issue. RESULTS: 1) testing agency reports positive tests to the State 2) State notifies counties in which the positive people live 3) w/in 24 hrs, counties notify people who tested positive 4)w/in 48 hrs (cases are mounting),Contact Tracers call infected people & ask w/whom they have been in contact. NO REASON for infected people to need code. Call Labor Dept if there's a work issue. RECOMMEND: call people who know things.<br> :date: __2020-11-20 20:45:59__

> People have said they can't get a verification code that is needed to send an alert. I just read (11-18-20, cpr) that this code should now be sent automatically. Hopefully this improves the situation.<br> :date: __2020-11-19 15:15:54__

> I can't specify my area nor can I put in a result whether I'm positive or negative. Need to understand what code they want. Also if it only sense through bluetooth I don't want to be that close to someone if possible. There should be more options in Android app. Couldn't get my iPad to gain access so not sure how others are getting info even if it may be places I may go in the Metro or suburb area. Clarification needed pr more options.<br> :date: __2020-11-19 03:31:37__

> I was in the same house with a person who tested positive... 3 days later... Still no notification! Uninstalling!<br> :date: __2020-11-12 18:55:04__

> Been running into issues of it not checking for possible exposures even with location/Bluetooth being on during the day. Been working around the public and it checked 3 days ago with a hefty amount of keys but not the day after or yesterday for that matter until I found I had to delete all the keys and then it'll restart and start collecting again, all my co workers have it on also. Not a good thing incase I ran into anyone days before that and they tested positive and the keys match later on.<br> :date: __2020-11-07 12:54:36__

> Positive test here but can't share my result because I don't have a verification code. failed app so far🤷‍♂️ I've searched for about 15min and can only figure it's because my test was conducted out of state. However, I was around people in CO and would like to share it. Will people share if it's not easily available? I would also recommend information about privacy and how your results a reported. People might have a sense of shame or guilt but might share if there's some sense of anonymity.<br> :date: __2020-11-07 01:48:11__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.co.cdphe.exposurenotifications 2 reviews"/>
</p>

> This app doesn't work. I installed it when it first became available. It has never once in all that time reported an exposure regardless of how remote the exposure might be.<br> :date: __2021-02-03 23:39:55__

> The app seems great (simple, unobtrusive, easy to use, no major privacy issues) but what good is the app if people can't easily report their covid results? Why haven't they partnered with testing facilities to provide this code automatically upon getting a positive result? I've had this app for months and haven't gotten a single notification ever<br> :date: __2021-01-10 00:52:39__

> Adventrouous to say the least<br> :date: __2021-01-08 06:45:13__

> The reasonable use of this app doesnt make sense<br> :date: __2021-01-08 00:14:51__

> My phone hasn't worked right since..tells my blue tooth is off when it's on..stupid<br> :date: __2021-01-01 08:45:40__

> 👌<br> :date: __2020-12-23 09:21:28__

> My wife works with covid patience. So needless to say, she is in contact with covid positive people. Her app says "no contact". Four people I work with have it. Nothing from the app. Broken. 😠Wish it worked better . Merica, thanks<br> :date: __2020-12-21 04:32:43__

> Jg<br> :date: __2020-12-18 12:54:33__

> I don't think this app works<br> :date: __2020-11-28 16:58:50__

> I have to provide a "verification code" for my test result. I did not get one though, over the "negative" phone call..<br> :date: __2020-11-24 22:58:35__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.co.cdphe.exposurenotifications 1 reviews"/>
</p>

> Why does this app exist? It does nothing if folks don't share their status.<br> :date: __2021-02-06 03:47:28__

> I don't see how this is useful if you don't really know where you got exposed and the date & time. And why not get an alert at the time of the event so an individual can remove themselves. Why doesn't a store owner get an alert so they know someone positive is in the store. It makes no sense that if we are trying to control the spread if this disease that this program doesn't seem a bit more comprehensive. After the fact seems a bit useless. Besides, it sucks battery.<br> :date: __2021-02-04 16:59:11__

> Pretty useless since you can't let it know if you test positive without entering some sort of mysterious missing/failing verification code. Where is that supposed to come? Who knows because it is not mentioned in their guidance.<br> :date: __2021-02-03 21:59:10__

> I have had countless people in my life get COVID 19 and this app has been silent. Absolutely a pointless app.<br> :date: __2021-01-27 06:52:38__

> Seemingly useless<br> :date: __2021-01-26 01:28:42__

> I don't like the fact I have to keep it on if I'm at home and don't come in contact with anyone else. There is no reason why I should keep it on at home, it's a violation of my privacy and my right to chose. I'm well aware of the capabilities Bluetooth technology has it's the things it can do that your app doesn't mention that bother me. Every Bluetooth device I have will Transmit not Rx the signal back. I'm 99% it's ur app. Now my tablet need resetting and the time it takes to reinstall is,.<br> :date: __2021-01-25 13:46:33__

> I will give it a better score when it actually works, I can't even install it now, I installed it a few weeks ago and it wouldn't work when I pressed "turn on", so I decided to finally bother to reinstall it and now when I get to the agree screen and "agree" it doesn't work and cancels installing itself. Please fix this.<br> :date: __2021-01-25 04:23:06__

> Will not let me report my positive covid test results. Asking for some verification number. Neither I nor my doctor knows what that is.<br> :date: __2021-01-21 01:57:48__

> App doesn't work. Didn't notify me when co-workers had it. I can't put in that I currently have it. Needs some verification code but doesn't tell you where or how to get that. Sure this was a big waste of tax dollars<br> :date: __2021-01-18 21:37:09__

> Cant post results doesn't see anyone with covid ever..<br> :date: __2021-01-15 08:50:35__


