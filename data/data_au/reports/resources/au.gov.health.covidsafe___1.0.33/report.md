# COVIDSafe
App version ``1.0.33``

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
| **Latest version** | 1.0.33 |
| **Last update** | 2020-07-04 23:25:57 |
| **Recent changes** | The app now supports 5 more languages: Mandarin, Cantonese, Vietnamese, Arabic and Korean<br>Accessibility enhancements<br>Bug fixes. |
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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **11936** rated the app and its average score is **3.1705883**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 5005

:star::star::star::star:: 922

:star::star::star:: 992

:star::star:: 1133

:star:: 3881

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> Unbeatable!<br> :date: __2020-07-09 14:43:00__

> So easy to follow<br> :date: __2020-07-09 14:27:00__

> App very informative.<br> :date: __2020-07-09 13:57:09__

> Very good app & much needed.<br> :date: __2020-07-09 11:36:29__

> GREAT =] staying home saving lives<br> :date: __2020-07-09 08:34:54__

> Far too voluminous<br> :date: __2020-07-08 23:27:58__

> Love it<br> :date: __2020-07-08 14:38:42__

> Easy to navigate. Thanks.<br> :date: __2020-07-08 12:22:40__

> Generally don't notice the app running at all; UPDATED - haven't experienced the below for some time now. however started using the phone for music in the car today and it constantly causes the cars Bluetooth to reset about 1-2 minutes into each song. Phone = Samsung S9+ Car = Mazda BT50 2014 (Don't know what version of Bluetooth) Hopefully you can resolve this issue.<br> :date: __2020-07-08 11:55:46__

> On 4 Of May I have Received my Corona test results was Good from Auburn Hospital<br> :date: __2020-07-08 11:49:35__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> Please fix the notification area. I have to stop the app because it blocks other notification from other app<br> :date: __2020-07-09 00:24:03__

> Put the app on the phone like they said have not had a problem with it Blue tooth OK.<br> :date: __2020-07-08 14:40:30__

> I live in guyana and they do not have guyana in there country list please put guyana now or i will delet this app please really want this app<br> :date: __2020-07-07 02:07:51__

> Would be good if it at least showed how many other devices it's registered, and when.<br> :date: __2020-07-06 16:14:37__

> Update: Initial force-close issue resolved by reinstalling. Haven't heard of the app actually doing its job yet and at what accuracy rate, but I guess it's better than nothing.<br> :date: __2020-07-06 00:39:03__

> Not knocking the app, no app is perfect therefore no app ever gets "5 stars". Unfortunately this is a necessary evil in modern times. I wish I could close it including from the notifications panel when I'm home & Bluetooth is off. "4 & 3/4 stars" if you can achieve this. (Android 10, gentle notifications on, no option to disable foreground services or option them at "home location" or "Bluetooth off".)<br> :date: __2020-07-05 22:16:29__

> Sits quietly in the background can't complain<br> :date: __2020-07-05 13:21:45__

> Using this app makes audio headset bluetooth connection unstable, but still worth using it<br> :date: __2020-07-02 02:43:49__

> It's this one of those, pay-to-win games? I haven't leveled up once yet !?!<br> :date: __2020-07-01 23:23:24__

> My screen locks and goes blank any time I revive or make call. Have to uninstalled, friend has same issue. Tried re installing, issue is back.<br> :date: __2020-07-01 00:11:47__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> You guys broke the lock screen notification in the last update 🤦‍♂️<br> :date: __2020-07-09 23:43:36__

> Edit: Issue appears only when I've set the notification to silent, if I set it back to alerting it looks ok. --- Latest update has wrecked the notification drawer. Please fix soon.<br> :date: __2020-07-09 23:07:53__

> I wish I could see where I am on the map and I wish that the app work like the fire app so I can see hot spot in the world.<br> :date: __2020-07-09 10:46:33__

> Need more communication between each of the virus stations make sure that they put are on the same giving the same advice and not stuffing me around<br> :date: __2020-07-09 10:22:16__

> Was using this when it was just Bluetooth, but the Government doesn't need my location data as well.<br> :date: __2020-07-09 10:08:54__

> This app as important as it is prevents my other apps notifications from displaying correctly I've removed it until it is fixed<br> :date: __2020-07-08 10:44:52__

> Issues from latest update causing notifications overlapping , on pixel phone<br> :date: __2020-07-08 10:39:37__

> After the last update, the notification that is usually on my lock screen is missing and affects the appearance of other notifications, which makes it difficult to read incoming messages on the lock screen. Perhaps the notification height was set to a negative number. Other than that, it appears to do as described. No issues with Bluetooth here.<br> :date: __2020-07-08 03:18:05__

> Interferes with wifi. Uninstalled. Probably built on a $3 budget.<br> :date: __2020-07-07 12:23:16__

> it working wasnt easy<br> :date: __2020-07-07 02:45:12__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> Latest update has broken the notifications system for my phone (pixel 2 xl)<br> :date: __2020-07-10 03:17:23__

> 10/7 latest update has screwed up the notification bar, and somehow has stuffed up the notifications for other apps too. Will probably uninstall if not fixed soon. *Original Review*: Enrollment was pretty easy, the app is always running in the background but so far doesn't appear to be using the battery at all. Would trust it more if they used the Google/Apple framework, but sounds like that's a few weeks away..<br> :date: __2020-07-10 00:10:43__

> Uninstalled because it messes up my lockscreen notifications (Samsung Snapdragon Note 10+).<br> :date: __2020-07-09 16:56:30__

> I need to uninstall and reinstall the app every time I activate it to make it work. This is rather frustrating and time-consuming, and defeats the purpose of being able to open the app and have it running at a moment's notice when you're near other people.<br> :date: __2020-07-09 14:13:56__

> The latest update prevents the notifications on my lock screen showing correctly. They are now only partly visible. They show fine if I disable the app.<br> :date: __2020-07-09 11:06:44__

> Latest update is drawing over the top of other notifications, please fix asap, use the phone for work and this getting in the way<br> :date: __2020-07-09 06:01:45__

> Just had to uninstall this as a result of the latest update. It hides all of my notifications while installed. Problem goes away as soon as its uninstalled. Pretty poor for a government app if you ask me. This sort of stuff only makes people more suspicious of the app...<br> :date: __2020-07-09 05:44:46__

> Notification bar issues since most recent update. Have to disable this apps notifications to rectify<br> :date: __2020-07-09 04:59:13__

> It works fine but has caused an issue with notifications displaying for all apps on the locked screen.<br> :date: __2020-07-09 03:14:08__

> Keeps telling me my name is not legal. So i am uninstalling<br> :date: __2020-07-08 08:03:09__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> Uninstalling this app because since latest update on 2/7/2020 it's affecting the appearance of other app notifications which is annoying.<br> :date: __2020-07-10 14:46:49__

> Drains too much battery<br> :date: __2020-07-10 14:18:45__

> Why no auto update<br> :date: __2020-07-10 13:08:26__

> Keep crashing after the latest update<br> :date: __2020-07-10 12:29:35__

> Not.useful.at all<br> :date: __2020-07-10 11:58:47__

> I downloaded the app one the first few days. Today I deleted it. It kept turning itself off. I followed all tips and suggestions but it just kept on shutting down with no alert to let me know it had done so.<br> :date: __2020-07-10 08:41:18__

> Drained my phone battery and so useless, I can't believed the government spent that much money for an useless app, this is how you spend tax payers money, poor design and chased nothing, unbelievable<br> :date: __2020-07-10 06:50:17__

> The latest update is causing notification issues in the swipe down menu and lock screen<br> :date: __2020-07-09 13:42:11__

> It's a placebo. No benefit.<br> :date: __2020-07-09 11:43:22__

> It is of no use whatsoever. A waste of money & a waste of my battery life.<br> :date: __2020-07-09 07:12:24__


