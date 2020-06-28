# COVIDSafe
App version ``1.0.28``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="COVIDSafe icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | COVIDSafe |
| **Unique identifier** | au.gov.health.covidsafe |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=au.gov.health.covidsafe](https://play.google.com/store/apps/details?id=au.gov.health.covidsafe) |
| **Summary**  | COVIDSafe is a community-based way to stop the spread of COVID-19. |
| **Privacy policy** | [https://www.health.gov.au/using-our-websites/privacy](https://www.health.gov.au/using-our-websites/privacy) |
| **Latest version** | 1.0.28 |
| **Last update** | 2020-06-18 11:47:23 |
| **Recent changes** | More people in Australia can now download and use the app. We have added support international and Australian External Territories mobile numbers.<br>Improved accessibility, usability and functionality. <br>Bug fixes. |
| **Installs**  | 1,000,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 25, 2020 |
| **Size**  | 11M |
| **Supported Android version**  | 5.0 and up |

### Description
> COVIDSafe app has been developed by the Australian Government Department of Health to help keep the community safe from coronavirus (COVID-19). Together, let’s help stop the spread and keep ourselves and each other healthy.
<br>COVIDSafe uses the Bluetooth® technology on your mobile phone to look for other devices with COVIDSafe installed. Your device will take a note of contact you’ve had with other users by securely logging the other user’s reference code. If you or someone you’ve been in contact with is diagnosed with COVID-19, the close contact information securely stored in your phone can be uploaded and used—with your consent—by state and territory health officials to quickly inform people who’ve been exposed to the virus.
<br>How you can help stop the spread of COVID-19:
<br>• Download the COVIDSafe app
<br>• Register using your mobile phone number, name, age range and postcode
<br>• Turn on Bluetooth®
<br>• Check that COVIDSafe is running when you are out and about or are likely to come into contact with others
<br>• If you test positive for COVID-19, you can consent for your close contact information to be used by state and territory health officials to contact people who may have been exposed. If you’ve been exposed to the virus by someone you’ve been in close contact with, state and territory health officials will be able to contact you quickly so you can get the support you need
<br>COVIDSafe is an Australian Government Department of Health initiative. Visit https://www.health.gov.au/resources/apps-and-tools/covidsafe-app for more information.


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
| **Developer**  | Australian Department of Health |
| **Website**  | [https://www.health.gov.au/resources/apps-and-tools/covidsafe-app](https://www.health.gov.au/resources/apps-and-tools/covidsafe-app) |
| **Email** | support@COVIDSafe.gov.au |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Australian+Department+of+Health](https://play.google.com/store/apps/developer?id=Australian+Department+of+Health) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Pie, version 9 (API level 28) |
| **Effective target Android version**  | Pie, version 9 (API level 28) |
| **Minimum supported Android version**  | Lollipop, version 5.0 (API level 21) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>BLUETOOTH_ADMIN** | Normal | Allows applications to discover and pair bluetooth devices. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>REQUEST_IGNORE_BATTERY_OPTIMIZATIONS** | Normal | Permission an application must hold in order to use Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | stackoverflow.com | Stack Exchange, Inc. | :us: US | 2003-12-26 19:18:07 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |


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



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The COVIDSafe app has been installed by more than **1000000** times. At this time, **11674** rated the app and its average score is **3.2178388**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 5026

:star::star::star::star:: 961

:star::star::star:: 951

:star::star:: 1001

:star:: 3734

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> Excellent<br> :date: __2020-06-28 15:15:15__

> I have had this app since the beginning. I've had no problems, maybe a bit more battery use. Happy to help and everyone else should help too!!!!<br> :date: __2020-06-28 06:02:51__

> Works great with my phone, sad to hear others with different phones have issues<br> :date: __2020-06-28 03:47:13__

> Safe Australia.<br> :date: __2020-06-27 15:28:44__

> Twenty five stars<br> :date: __2020-06-27 08:31:09__

> App has no issues on my phone, and working in the background, despite what some people believe (battery draining is the main one), my phone has not drop its charge that was noticeable by me. In order for it to work effectively, more people needs to download it. It is not working as it should because people are too worried about 'privacy'. The app is 'contact traCING', not 'personal information traCKING'. Don't blame the app for not working, look at the people that don't have it.<br> :date: __2020-06-27 08:27:55__

> Great<br> :date: __2020-06-27 07:12:06__

> Latest update fixed the previous problem of crashing. Thanks for that. Working well again. Well, not sure if it's working because nobody I've ever encountered had the virus, so how would I know? But, this app is a good idea and if it says it's doing it's job then that's fine with me.<br> :date: __2020-06-27 03:15:32__

> Onya Scotty<br> :date: __2020-06-27 01:47:13__

> ممتاز<br> :date: __2020-06-26 15:53:43__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> On my Note 10, I don't have any of the problems others mention about bluetooth drop outs to car or Senheisser headphones or Samsung Watch, the only problem I have is the app doesn't start up when I restart the phone, I rarely restart so not a big problem.<br> :date: __2020-06-28 04:21:25__

> The app conflicts with my Bluetooth headphones, here's the fix: Settings > apps > force stop. Remember to turn the app back on when you go outside. Good luck everyone.<br> :date: __2020-06-27 08:52:54__

> I don't mind the app but I don't understand wire displays how many minutes and the time when I pull down my home screen and it's running in the background what do the minutes mean? Eg: covidsafe 12m ??<br> :date: __2020-06-24 17:17:19__

> Excellent<br> :date: __2020-06-24 08:54:38__

> I installed this app, hoping people do the right thing. If they have the virus they too should install and updated information for the public to know about it. Noone knows who the infected person/s are, but you are made aware that someone near you is.<br> :date: __2020-06-23 14:53:07__

> Always on keeping myself and others safe<br> :date: __2020-06-23 09:13:15__

> Great idea. But my phone keeps turning it off<br> :date: __2020-06-22 17:07:55__

> The app is very good and I never had any problem with it. But since I installed it about 2 months ago it didn't give any warning about people having the Covid19 around me, in which I guess not much people using it.<br> :date: __2020-06-22 09:41:52__

> A work in progress, be patient folks<br> :date: __2020-06-19 02:30:01__

> I'll give 5 stars when @VictorianCHO's (and/or other states') contact tracers release evidence clearly demonstrating that it is an effective, and cost effective, adjunct to manual contact tracing, and thus can a) help put asymptomatic carriers into quarantine, and b) extinguish hot spots more quickly. Their hype, my hope. Happy since v1.0.16 that it no longer nags to switch on GPS. v1.0.11 did. On this Samsung S5 the Bluetooth BLE being "on" doesn't cut battery life. [Redacted 15 June '20]<br> :date: __2020-06-15 05:57:03__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> Useless<br> :date: __2020-06-28 01:05:52__

> Might be useful, but can't be sure. I've installed this app and so far haven't got Covid 19 (that I know of). Registration was easy, and can be done using a pseudonym. Battery usage is quite low. Ongoing notification to tell you that it is working, and will let you know if it stops working (eg. you turn off Bluetooth). However, the icon (Australia with tick) shows whether it is working or not (eg. When Bluetooth turned off).<br> :date: __2020-06-27 14:26:06__

> Doesn't work properly<br> :date: __2020-06-26 18:15:48__

> This app is causing too many problems with Bluetooth devices.. Ever since I installed the app, my car can't connect automatically so I have to manually do it every time. The same goes for my Fitbit...<br> :date: __2020-06-23 11:28:33__

> The app doesn't start automatically, this is a pretty fatal flaw<br> :date: __2020-06-23 05:32:28__

> It keeps stopping, several times a day. I'd like to do the right thing and run this app, but it's not helping.<br> :date: __2020-06-23 03:49:26__

> The app forces my Bluetooth to disconnect heaps making the use of Bluetooth devices a pain in the backside, but other than that it's great.<br> :date: __2020-06-22 16:06:42__

> Makes my samsung play up. Have to uninstall and re install whenever needed<br> :date: __2020-06-22 07:41:37__

> The app would be useful if it didn't turn off by itself. It's kind of missing the whole purpose.<br> :date: __2020-06-22 03:03:55__

> Not sure it is working properly. Everytime I decide to check in on the app, it says battery optimiser is on and it's not working. I then put this on but it goes back to off again. Also there is no way in settings to make sure this app doesn't get this treatment. Ahh!!<br> :date: __2020-06-22 01:48:43__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> Has not identify a single case in Victoria's outbreak<br> :date: __2020-06-28 14:07:51__

> I'm a first responder but deleted the app because of its bluetooth hogging and battery consumption issues, plus it seems to just stop working, especially after turning my phone into a pocket heater. I reckon this is exactly the sort of terribly optimised app we can expect from the government and as such it needs plenty of fixes before I reinstall it. Then of course there's the security side of things. Look at the government's track record with My Health and others being hacked, not good.<br> :date: __2020-06-28 08:46:32__

> Eventually my bluetòoth would not turn on.<br> :date: __2020-06-27 10:52:19__

> I'm a bit concerned as how this app has inboxed people from my facebook messenger.. someone I have never spoken to received a message saying to join the covid safe app and prevent the spread, at 4.24am Friday. Along with several other people. I was asleep so unsure who or how it was sent to people 🤔<br> :date: __2020-06-27 07:03:31__

> Now the app just keep crashing.<br> :date: __2020-06-27 04:27:47__

> This app makes my headphone sound stop for a few seconds every 20 secs once i block the app this stops happening<br> :date: __2020-06-26 05:17:39__

> I'm all for this app, but it keeps turning off itself. Not sure if it is the issue with this new version or my new phone, but I couldn't figure out how to keep it running constantly.<br> :date: __2020-06-26 03:44:56__

> Ambiguous<br> :date: __2020-06-25 07:48:41__

> The app shuts off every time my phone goes to sleep, even though I've specifically given it permission to run in background in my settings. So we either walk around constantly on our phone in public or let ALL the apps run continuously, and recharge phone 3x a day because the battery is continuously drained. So if the app doesn't work properly half the time what's the point???<br> :date: __2020-06-24 21:48:19__

> Fairly useless. Turns off multiple times a day.<br> :date: __2020-06-24 09:00:15__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> Tried to sign up but when I put in my phone number I got no verification pin, making the whole app entirely useless. I've tried following the steps on the FAQ but they don't work either. Cant tell if this is an OS issue or something with the app considering in stuck on Android 9<br> :date: __2020-06-28 17:02:53__

> I'm losing faith that this works. Show me the proof!<br> :date: __2020-06-28 16:29:37__

> Im a Android user app wont even let me continue after entering info on first page useless<br> :date: __2020-06-28 15:52:33__

> If this actually showed something to prove it was working, say IDs or part of Id of other devices it had a handshake with or something such as the number of hand shakes or some other stat info that could prove it was actually doing something it would extremely helpful as it stands it is a blackhole app that appears on this unit to keep stopping unless in the foreground, not what one wants from something like this.<br> :date: __2020-06-28 13:11:26__

> Drains the battery without providing any helpful information<br> :date: __2020-06-28 12:00:25__

> I am continually getting 'connected to null ' and 'disconnected from null ' messages all the time on my phone, it disrupts what I am trying to read on screen. I end up turning Bluetooth off when not out in the public to prevent it happening. It is very annoying, I have emailed support covid, but no response so far.<br> :date: __2020-06-28 11:22:51__

> It drained my battery.<br> :date: __2020-06-28 09:52:32__

> Very ordinary. My Bluetooth turns off and it never prompts. Often isn't running. Basically a dud app and of little use. And I use android.apple is a total fail<br> :date: __2020-06-28 08:27:59__

> I installed this to do my part. My phone became sluggish, the camera stopped working, and the battery life became about a fifth of normal. Uninstalled, everything went back to normal. Fix it!<br> :date: __2020-06-28 03:55:39__

> I am a firm believer in the concept behind this app. Like other users I am experiencing issues with the app closing. In addition, it interrupts my ability to connect to my car Bluetooth meaning I have no hands free use of my phone. Please fix asap.<br> :date: __2020-06-28 03:38:08__


