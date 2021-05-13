# COVIDSafe
App version ``2.6``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="COVIDSafe icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | COVIDSafe |
| **Unique identifier** | au.gov.health.covidsafe |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=au.gov.health.covidsafe](https://play.google.com/store/apps/details?id=au.gov.health.covidsafe) |
| **Summary**  | COVIDSafe is a community-based way to stop the spread of COVID-19. |
| **Privacy policy** | [https://covidsafe.gov.au/privacy-policy.html](https://covidsafe.gov.au/privacy-policy.html) |
| **Latest version** | 2.6 |
| **Last update** | 2021-05-07 14:01:12 |
| **Recent changes** | Bug fixes and minor changes to enhance support for non-Australian mobile numbers. |
| **Installs**  | 1,000,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 25, 2020 |
| **Size**  | 13M |
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
| **Website**  | [https://www.health.gov.au/resources/apps-and-tools/covidsafe-app#covidsafe-app-help](https://www.health.gov.au/resources/apps-and-tools/covidsafe-app#covidsafe-app-help) |
| **Email** | support@COVIDSafe.gov.au |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Australian+Department+of+Health](https://play.google.com/store/apps/developer?id=Australian+Department+of+Health) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Android10, version 10 (API level 29) |
| **Effective target Android version**  | Android10, version 10 (API level 29) |
| **Minimum supported Android version**  | Lollipop, version 5.0 (API level 21) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_COARSE_LOCATION** | :warning:**Dangerous** | Allows an app to access approximate location. 
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **18855** rated the app and its average score is **3.6971428**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 9404

:star::star::star::star:: 2938

:star::star::star:: 1596

:star::star:: 1234

:star:: 3683

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> Boom! This app is the best thing ever! I love the Australian Government!<br> :date: __2021-05-13 09:34:19__

> Very user friendly 😊👌<br> :date: __2021-05-13 01:57:39__

> Working all the time<br> :date: __2021-05-12 05:19:14__

> Do not give my information private or public to anyone<br> :date: __2021-05-11 12:18:02__

> Easy to use.<br> :date: __2021-05-11 06:26:13__

> sound<br> :date: __2021-05-11 02:58:46__

> Keep safe tracking.<br> :date: __2021-05-11 01:59:59__

> Works great. Havent caught covid yet lol<br> :date: __2021-05-10 23:58:07__

> Awesome<br> :date: __2021-05-10 18:18:21__

> n 6<br> :date: __2021-05-10 08:34:35__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> Deleted this morning due to updated app draining battery on phone. Gone and forgotten<br> :date: __2021-05-13 01:54:39__

> No issues, let's hope we can get back to normal soon.<br> :date: __2021-05-11 02:01:09__

> I totally agree with Karen Welfare..<br> :date: __2021-05-10 10:48:57__

> How does one know it is running?<br> :date: __2021-05-10 06:03:23__

> Ok thanks noted<br> :date: __2021-05-10 03:16:35__

> Good<br> :date: __2021-05-09 23:28:21__

> I can easily access information about the covid-19.<br> :date: __2021-05-09 12:25:58__

> I like the way it stays active on my phone while I'm out shopping<br> :date: __2021-05-09 03:11:58__

> Missing a QR code scanning tool<br> :date: __2021-05-06 05:36:09__

> Never had an issue. Gives me peace of mind.<br> :date: __2021-05-04 05:26:40__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> Excellent idea<br> :date: __2021-05-13 07:26:11__

> I might come to Australia from NZ for a holiday which one works the commonwealth app or the state check in apps<br> :date: __2021-05-12 12:25:56__

> Update. Issue fixed. After last up date GS8 now drains 40% over a day. Fix it as unintall now.<br> :date: __2021-05-12 01:10:35__

> Don't see any benefit emerged from the app, yet.<br> :date: __2021-05-10 05:17:24__

> too much power<br> :date: __2021-05-09 12:22:33__

> Was good until battery usage went through the roof.. uninstalled it....<br> :date: __2021-05-04 23:26:14__

> Good so far<br> :date: __2021-05-04 04:34:31__

> It has never reported anything.<br> :date: __2021-05-02 10:48:28__

> Not sure it is working<br> :date: __2021-05-01 11:48:40__

> Disappointing. I used this from the word go as I believe it to be a useful tool for its purpose. In the last ?week? or so it has been responsible for massive power drains to the point my phone switched off. The last episode was 70% power usage, yesterday, so unfortunately it is gone.<br> :date: __2021-04-30 01:29:57__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> 93 44 55<br> :date: __2021-05-12 08:52:04__

> Chews up more battery than any other app on my phone. And doesn't seem to help trace anyone.<br> :date: __2021-05-12 08:16:14__

> Says it needs updating but just stays "pending" for hours<br> :date: __2021-05-10 05:41:09__

> This version consumes way too much battery. Last night it used half my battery in 7 hours. If this is not fixed, I might have to uninstall it. Edit: the latest version is better on a phone restart, but slowly consumes more battery over time, until it drains most of my battery in a few hours.<br> :date: __2021-05-07 01:50:13__

> Had no issue with this being a background app until it started draining my battery after the last update. Great concept but given that nobody uses this app it's an absolute dud.<br> :date: __2021-05-04 00:33:59__

> Pop down selections for state don't work. You have to hit home go get out, which may of may not work. Don't use device back buttons or you could end up in trouble. Have had the app since in inception so was notified of availability of update, which I did only to get a big red warning flag that my registration had elapsed and I had to step through a bunch of steps to add personal data. Why wasn't I notified separately. Clunky awkward app.<br> :date: __2021-05-02 04:26:03__

> I iPhone to see the money in the bank not it's been 4 years stop dragging<br> :date: __2021-05-01 07:23:23__

> So so a pointless app when you have to use service N.S.W to check in everywhere<br> :date: __2021-04-28 23:02:58__

> The latest update has stuffed up battery usage. I work in a large organisation and 8 hours of background usage chews up 43% of battery of my Samsung Note 9. I literally have to keep my phone plugged all day at work. This needs to be fixed ASAP.<br> :date: __2021-04-28 08:14:42__

> Always when I want to use it....it needs to be updated<br> :date: __2021-04-28 07:00:21__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> What a complete waste of money by Scomo<br> :date: __2021-05-13 10:59:28__

> App was fine (although of questionable effectiveness) until last week's update - after which it guzzled battery at a ferocious rate, where my phone was dying within hours even on standby. A battery monitoring app confirmed COVIDSafe as the culprit. While I'd like to play my part in assisting contact tracing efforts, I was ultimately forced to uninstall it. The contrast is striking after uninstalling, with my battery still at 50% after a whole day.<br> :date: __2021-05-12 18:17:10__

> Haven't seen nor heard of any benefit thus far.<br> :date: __2021-05-12 08:13:44__

> Too easy to accidentally disable or remove when in use or it crashes (either way you think it's working but it's not) also had to uninstall and reinstall because "push notifications" refused to activate. Would be nice too to be told someone near you has the app up and running otherwise what's the point? btw had no problems prior to last update! p.s. Have stopped using this cr app, can't see the point with QR codes everywhere.<br> :date: __2021-05-11 23:59:56__

> Should be a check in app.<br> :date: __2021-05-11 11:56:27__

> No experience<br> :date: __2021-05-11 10:51:19__

> Another waste of scomos brain.<br> :date: __2021-05-10 18:23:26__

> I don't know if this app is effective or not. It's just "there" unbeknownst to me if it's functioning or not. So how can I give it a rating?<br> :date: __2021-05-10 06:26:13__

> I up dated this app as requested and it hasnt worked since.<br> :date: __2021-05-09 17:24:28__

> Massive battery drain. Only 8 hrs after taking it off charge, battery usage shows 59.8% to the COVIDSafe app, draining it down to 23%. Whatever changes the last update made has made this app useless. And it still disrupts streaming music via Bluetooth. 8/5/21 App still drains a huge amount of battery life. Sitting at home, app shows battery usage 65%, after 8 hours off charge and drained my battery to 1%. Absolutely shocking usage for just sitting on my desk doing nothing.<br> :date: __2021-05-08 12:23:19__


