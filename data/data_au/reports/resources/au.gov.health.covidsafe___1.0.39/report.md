# COVIDSafe
App version ``1.0.39``

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
| **Latest version** | 1.0.39 |
| **Last update** | 2020-07-20 15:10:18 |
| **Recent changes** | The app is now available in two more languages: Greek and Italian. <br>Accessibility enhancements. <br>Bug fixes. |
| **Installs**  | 1,000,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 25, 2020 |
| **Size**  | 12M |
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
 **android.permission<br>ACCESS_COARSE_LOCATION** | :warning:**Dangerous** | Allows an app to access approximate location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>BLUETOOTH_ADMIN** | Normal | Allows applications to discover and pair bluetooth devices. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>REQUEST_IGNORE_BATTERY_OPTIMIZATIONS** | Normal | Permission an application must hold in order to use Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | stackoverflow.com | Stack Exchange, Inc. | :us: US | 2003-12-26 19:18:07 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |


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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **12512** rated the app and its average score is **2.8557692**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 4280

:star::star::star::star:: 842

:star::star::star:: 1132

:star::star:: 1303

:star:: 4952

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> Fantastic<br> :date: __2020-07-28 10:55:53__

> I feel safe knowing that I will be notified if I come in contact with covid 19 infection<br> :date: __2020-07-28 02:15:18__

> Very good<br> :date: __2020-07-28 02:08:46__

> This is how we can beat covid-19<br> :date: __2020-07-27 23:58:28__

> What ever helps!<br> :date: __2020-07-27 09:32:20__

> Edited from 1 to 5 star. Notification problems fixed, thanks.<br> :date: __2020-07-27 05:16:47__

> why not add a function where businesses can create a QR code and as you enter you scan the code which is stored in the Covid safe database. An additional level of data collection to overcome the bluetooth issue<br> :date: __2020-07-27 04:18:34__

> Works transparent. No compatibility issues. Please use it and help save lives.<br> :date: __2020-07-26 14:52:17__

> It can't do more harm than virus, just use it!<br> :date: __2020-07-26 10:19:16__

> A small price to pay and hopefully saves some older person's life. Uncool but there you go.<br> :date: __2020-07-25 16:18:16__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> Hope I never need it.<br> :date: __2020-07-28 11:07:35__

> Definintely needed but please change the notification back to green in the status bar. When its white, I keep thinking I have an sms or missed phone call or some other notification that needs my direct attention. Very annoying!<br> :date: __2020-07-28 03:35:43__

> I'm glad we've got it but it is a real battery killer!<br> :date: __2020-07-28 01:04:00__

> Has this app been used to trace any of the recent clusters in NSW or any of the cases in Victoria? I'm wondering if it is worthwhile having it constantly running in the background burning battery power. There doesn't seem to be any mention of the app being used in the news. Otherwise the app works fine.<br> :date: __2020-07-27 04:14:49__

> No muss no fuss. Just keep Bluetooth on and check it every few days (Sometimes a new update will need new permissions or similar), otherwise seems to be working on the background without issue<br> :date: __2020-07-27 00:03:11__

> Edit: Issue appears only when I've set the notification to silent, if I set it back to alerting it looks ok. --- Latest update has wrecked the notification drawer. Please fix soon.<br> :date: __2020-07-26 07:40:42__

> Helpful<br> :date: __2020-07-24 09:51:58__

> Works as described but last update has messed up my notifications incredibly and i am not only one experiencing this<br> :date: __2020-07-19 12:04:17__

> Hey guys, there must be something wrong with the app in the background, my phone keeps deactivating the app and I have a warning that it's not active, but when I go in the app it says everything is working fine. Then 5 mins later (more or less) it's goes offline again. Then the phone is happy. Then again later on it's all turned off. I got no idea what is going on here<br> :date: __2020-07-18 05:35:12__

> Bit of a power drainer, when at home, switch off Bluetooth and location, icons and settings. But like buying masks, gloves and hand sanitizer, we can all help to beat Coronavirus.<br> :date: __2020-07-16 02:57:34__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> Case numbers only shows total from beginning of time. Can you show Active Cases now state by state. Don't want to know how many we don't have now but how many active we have now. Otherwise good app.<br> :date: __2020-07-28 06:40:34__

> Disappointing it doesn't tell me I need to update<br> :date: __2020-07-26 23:48:11__

> Just sits in the background and seems to do nothing but eat my battery. Life went from 72hrs to 28hrs. Would be great if I could use the app to log into venues using qr code. Save pre-fill details, see where I have been. I would suggest give it more of a reason to download, that way more people can be tracked.<br> :date: __2020-07-26 13:12:53__

> Causes bluetooth problems. I am quite happy to do my bit to track and stay safe but the bluetooth problems are frustrating<br> :date: __2020-07-26 12:13:24__

> Latest update needs location services on. Why is that? It did not before. Gov web site says it does not record my location. Location services should not be needed. (Edit) It seems it needs access to location service, but location service can be turned off. Also app help says this is an Android limitation, location is not actually used.<br> :date: __2020-07-26 11:13:35__

> 26/7 notifications no longer stuffed, but weird location perm issues until reboot. 10/7 latest update has screwed up the notification bar, and somehow has stuffed up the notifications for other apps too. Will probably uninstall if not fixed soon. *Original Review*: Enrollment was pretty easy, the app is always running in the background but so far doesn't appear to be using the battery at all. Would trust it more if they used the Google/Apple framework, but sounds like that's a few weeks away..<br> :date: __2020-07-26 10:10:37__

> NEW Prevent phone from sleeping and NEW Receive data from the internet. Why have these permissions been added?<br> :date: __2020-07-25 23:28:35__

> Has anyone else noticed this app now wants location turned on? Interesting given they made a big deal of it not tracking location... I also second the comments about the notification screen being messed up now.<br> :date: __2020-07-25 08:22:59__

> Installed itself out of the blue without asking... It is alarming...<br> :date: __2020-07-25 06:05:46__

> After running the app since lauch without a problem it is now refusing to start without access to location despite explicitly stating it doesn't record location details. Running on android.<br> :date: __2020-07-24 14:15:02__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> Took me a few days to discover the app was not active, and I'm a health care worker. Nothing looked unusual but location sharing was inexplicably turned off. Maybe the notification icon could look different depending on the app status.<br> :date: __2020-07-28 04:35:56__

> Latest update expects locations to remain on at all times. What for? Another government tool that started with a good intention but is no longer paying attention to the intended function or the users.<br> :date: __2020-07-28 01:07:46__

> Have had to uninstall because of the excess battery drain, unable to carry out my day-to-day work and I rely on my device. Would love to be able to put this app to sleep when connected to my home WiFi - seems like a low hanging fruit to actually meet the problem this app is trying to solve. Now doesn't work on latest Android.<br> :date: __2020-07-27 05:56:21__

> Latest update has added bugs. App now has a permanant notification back which was annoying the first time around. Now it constantly says my location is not on. I fix it by force stopping and restarting. Couple hours later same warning. Seems this has gone backwards not forwards and is getting very little exposure to what actual use or results the app provides in the media.<br> :date: __2020-07-27 03:41:48__

> Can not pair the app with my phone.i work at glendale age care but i get no notifcations<br> :date: __2020-07-26 11:01:48__

> I thought i was doing the right thing downloading it. I have since taken it off my phone as it only works if i am closer than 1.5m for 15 mins or longer. This doesnt seem to be how this virus works (Seeing as everyone in the thai restaurant got it!). I know, or have details of everyone I'm closer than 1.5m to. I was also expecting more than 1/20 of the population to install it so it may have been somewhat more effective!!<br> :date: __2020-07-26 10:35:47__

> Latest update require gps location to be on but that info is not included in the update or description. Why has this been added? Also it's a big drain on battery.<br> :date: __2020-07-26 05:45:23__

> It's a great concept... But now the new update is asking for locations permissions to track movement. Good in theory but unviable and privacy issues, but big battery drainer.<br> :date: __2020-07-26 05:33:01__

> waste of our government money, should have just piggy back Google's network. what a rip off,<br> :date: __2020-07-25 07:56:00__

> Causes Bluetooth audio interruptions<br> :date: __2020-07-25 05:37:49__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> Such a massive $2 million fail. I can't even get it to register on a 2 year old phone. No wonder the govt has stopped spruiking it - they know it's a waste of time.<br> :date: __2020-07-28 11:40:29__

> Developers won't fix critical bugs, don't bother with the app, waste of taxpayers money<br> :date: __2020-07-28 11:34:35__

> App would continually turn off location. What a waste of time and money from the government<br> :date: __2020-07-28 08:11:53__

> Keeps crashing whenever I try to open it and constantly says it's not running. It was working previously but now it's not.<br> :date: __2020-07-28 07:51:07__

> Now requires GPS to be active all the time. This wasn't always the case. I value my privacy. I will be uninstalling the app now.<br> :date: __2020-07-28 03:08:58__

> Have tried once again to activate this app..once again it will not allow me to continue past the first section...I give up . It can't be too important ...no one appears to be correcting the fault ,which judging by the reviews, many others are also experiencing .<br> :date: __2020-07-28 00:18:17__

> App was going great then suddenly it says it's inactive and I need to turn Bluetooth on. The app gets as far as "turning on Bluetooth" and nothing...I uninstalled then reinstalled but the same thing happens. Sorry PM. Want to do my part to help but this app is just doesn't work. 😩😦<br> :date: __2020-07-27 20:34:19__

> Installed on my phone and the problems are numerous. Lock screen notification for covidsafe is blank and seems to stop others such as NSW emergency service alerts, etc from displaying correctly. Also interferes with other bluetooth apps that I need and rely on. This conflict with other apps causes the bluetooth service to crash and the only way to fix is either uninstall/reinstall covidsafe or reboot the phone.<br> :date: __2020-07-27 16:54:58__

> Nothing tells me how this app will alert me or what an alert looks or sounds like through my smart phone, when or if I come into contact with someone "registered as a Covid 19" person. An Extremely ambiguous app that doesn't make sense as far as explanation around it's practicality.<br> :date: __2020-07-27 14:20:09__

> Crashes immediately after opening. It used to work fine!<br> :date: __2020-07-27 13:33:37__


