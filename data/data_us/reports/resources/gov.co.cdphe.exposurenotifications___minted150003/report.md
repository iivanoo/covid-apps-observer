# CO Exposure Notifications
App version ``minted150003``

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
| **Latest version** | minted150003 |
| **Last update** | 2021-02-08 21:59:56 |
| **Recent changes** | Bug fixes and performance improvements |
| **Installs**  | 100,000+ |
| **Category** | Medical |
| **First release** | Oct 16, 2020 |
| **Size**  | 10.0M |
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

The CO Exposure Notifications app has been installed by more than **100000** times. At this time, **625** rated the app and its average score is **3.4455445**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 316

:star::star::star::star:: 49

:star::star::star:: 43

:star::star:: 31

:star:: 186

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.co.cdphe.exposurenotifications 5 reviews"/>
</p>

> Elpata<br> :date: __2021-03-06 05:27:02__

> I think<br> :date: __2021-03-03 20:07:33__

> I had it for months and thought it didn't work until I got a message that I was exposed on a trip! It only works if more people download it, use it and report if they test positive. It helped me to notify my job and quarantine effectively.<br> :date: __2021-02-28 10:33:55__

> People hack my account<br> :date: __2021-02-23 08:01:47__

> Great app!!!<br> :date: __2021-02-18 09:51:27__

> Great.<br> :date: __2021-02-17 19:29:50__

> Thank you! There seem to be many people here complaining about the app who don't seem to get how it works. Ignore the reviews and use this app.<br> :date: __2021-02-15 06:43:42__

> Its ok so far.<br> :date: __2021-02-10 07:47:18__

> Awesome<br> :date: __2021-02-02 10:22:45__

> Glad its her<br> :date: __2021-02-02 00:56:04__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.co.cdphe.exposurenotifications 4 reviews"/>
</p>

> Good<br> :date: __2021-03-18 18:03:16__

> Thanks keep us informed?<br> :date: __2021-02-05 23:11:31__

> Dunno if there's anything I can reasonably say about it useful.<br> :date: __2021-01-28 03:03:37__

> Not sure if it works. Haven't received any notifications after nearly three weeks. There is likely not enough people using this app, and the ones who do use it also use masks and social distancing. It's the ones that don't (use masks, social distance or use this app) you gotta watch out for.<br> :date: __2020-12-18 07:25:48__

> It's helpful<br> :date: __2020-12-07 07:54:07__

> I would like the app to have some way to tell me that I have exchanged tokens with someone, maybe giving me a total for a day. No details, just some indication that the app is doing its job.<br> :date: __2020-11-20 08:25:57__

> It does work for sharing a positive result! But don't go into the app because you'll get stopped at the verification code part. Instead wait for a text message from the health department - click on that link and follow the steps. It does share that way! You'll even see evidence that it was shared in the app. Would have given 5 stars but no explanation about the verification code or follow up text was given.<br> :date: __2020-11-19 19:19:46__

> Interesting stuff<br> :date: __2020-11-03 04:21:26__

> Great concept but kills my battery. I do have an old phone though so that may be the issue.<br> :date: __2020-10-27 15:53:56__

> I had trouble getting the notifications to work like a lot of people had posted, I uninstalled and reinstalled the app and it worked the next time. Not sure what causes this. Glad we have some form of contact tracing!<br> :date: __2020-10-26 03:29:29__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.co.cdphe.exposurenotifications 3 reviews"/>
</p>

> Neutral opinion of this app<br> :date: __2021-02-26 22:31:53__

> Didn't give me the ability to alert potential contact (button didn't work)<br> :date: __2021-01-02 06:48:03__

> Like<br> :date: __2020-12-12 07:54:21__

> I guess a good app but nobody in my area seems to be using it or posting a positive result in Pueblo County or other counties that I travel to for my job delivering parts, go far as Lamar, west to the San Luis Valley and South to Walsenburg, Trinidad and into New Mexico and you're telling me that I have not been near someone with a positive test result????<br> :date: __2020-12-11 20:39:25__

> Haven't been able to get much info<br> :date: __2020-12-06 18:50:05__

> Called county health department to ask about notification & special code issue. RESULTS: 1) testing agency reports positive tests to the State 2) State notifies counties in which the positive people live 3) w/in 24 hrs, counties notify people who tested positive 4)w/in 48 hrs (cases are mounting),Contact Tracers call infected people & ask w/whom they have been in contact. NO REASON for infected people to need code. Call Labor Dept if there's a work issue. RECOMMEND: call people who know things.<br> :date: __2020-11-20 20:45:59__

> People have said they can't get a verification code that is needed to send an alert. I just read (11-18-20, cpr) that this code should now be sent automatically. Hopefully this improves the situation.<br> :date: __2020-11-19 15:15:54__

> I can't specify my area nor can I put in a result whether I'm positive or negative. Need to understand what code they want. Also if it only sense through bluetooth I don't want to be that close to someone if possible. There should be more options in Android app. Couldn't get my iPad to gain access so not sure how others are getting info even if it may be places I may go in the Metro or suburb area. Clarification needed pr more options.<br> :date: __2020-11-19 03:31:37__

> I was in the same house with a person who tested positive... 3 days later... Still no notification! Uninstalling!<br> :date: __2020-11-12 18:55:04__

> Been running into issues of it not checking for possible exposures even with location/Bluetooth being on during the day. Been working around the public and it checked 3 days ago with a hefty amount of keys but not the day after or yesterday for that matter until I found I had to delete all the keys and then it'll restart and start collecting again, all my co workers have it on also. Not a good thing incase I ran into anyone days before that and they tested positive and the keys match later on.<br> :date: __2020-11-07 12:54:36__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.co.cdphe.exposurenotifications 2 reviews"/>
</p>

> Used to only notify you once about bluetooth, now does it all the time. That incentivizes me to uninstall since you cannot turn that notification off. Unfortunate.<br> :date: __2021-03-18 04:36:52__

> Confusing app. When you go to notify the app you have covid it prompts you to enter a notification code. But the text message you receive doesn't contain a code, but a link you click on and follow prompts. The text I got after testing positive came 2 days later and was in a spam folder (I didn't know my phone filtered suspected spam). So I kept thinking I didn't have the verification code & contacted CDPHE several times to no avail. They should email the info too & have an FAQ on the app.<br> :date: __2021-02-19 19:43:17__

> This app doesn't work. I installed it when it first became available. It has never once in all that time reported an exposure regardless of how remote the exposure might be.<br> :date: __2021-02-03 23:39:55__

> The app seems great (simple, unobtrusive, easy to use, no major privacy issues) but what good is the app if people can't easily report their covid results? Why haven't they partnered with testing facilities to provide this code automatically upon getting a positive result? I've had this app for months and haven't gotten a single notification ever<br> :date: __2021-01-10 00:52:39__

> Adventrouous to say the least<br> :date: __2021-01-08 06:45:13__

> The reasonable use of this app doesnt make sense<br> :date: __2021-01-08 00:14:51__

> My phone hasn't worked right since..tells my blue tooth is off when it's on..stupid<br> :date: __2021-01-01 08:45:40__

> 👌<br> :date: __2020-12-23 09:21:28__

> My wife works with covid patience. So needless to say, she is in contact with covid positive people. Her app says "no contact". Four people I work with have it. Nothing from the app. Broken. 😠Wish it worked better . Merica, thanks<br> :date: __2020-12-21 04:32:43__

> Jg<br> :date: __2020-12-18 12:54:33__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.co.cdphe.exposurenotifications 1 reviews"/>
</p>

> Are you freaking kidding me, this just another way of controlling people grow the f up<br> :date: __2021-03-25 17:58:40__

> To notify somebody if I have been exposed it asks for a verification code that was never given to me....so there's no way for me to notify. It defeats the purpose of having the app.<br> :date: __2021-03-24 23:56:27__

> I downloaded the app the week it launched and hadn't gotten even one notification by the time I uninstalled it on 3/20. Maybe I'm just ridiculously lucky to have avoided all exposure, but between case numbers, quarantines in my workplace, people not receiving positivity codes, and codes going unused, it seems much more likely that this app doesn't work well in practice. Mostly a waste of phone space, but one star for giving a false sense of contributing to public health.<br> :date: __2021-03-21 21:38:06__

> I have a question.. If your app uses Bluetooth to recognize other phones and that phone's user's status, what happens if I 'always' listen to music on Bluetooth headphones when out in downtown.. Is your app useless in this situation?<br> :date: __2021-03-18 07:09:12__

> I was asked to install this by my boss at work but I don't think it works itself? 🤔<br> :date: __2021-03-18 01:50:21__

> Its lying cuz I'm outside doing it<br> :date: __2021-03-17 17:43:47__

> Piss off, covid brownshirts.<br> :date: __2021-03-12 02:31:49__

> This app doesn't let you report your results of you got them from somewhere other than a mass testing site. Nearly useless.<br> :date: __2021-03-06 21:49:26__

> Pointless. I'm a teacher and have been quarantined for to exposure from a student. It's obvious this info isn't getting passed on.<br> :date: __2021-02-27 17:14:04__

> Only works if people register, which doesn't seem likely to me....<br> :date: __2021-02-20 14:16:34__


