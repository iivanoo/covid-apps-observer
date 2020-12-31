# COVIDSafe
App version ``2.0``

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
| **Latest version** | 2.0 |
| **Last update** | 2020-12-18 09:16:28 |
| **Recent changes** | This release introduces the new Herald Protocol that improves COVIDSafe&#39;s ability to capture close contacts and keeps users better informed about important COVID-19 information.  |
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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **13917** rated the app and its average score is **2.7911618**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 4394

:star::star::star::star:: 1190

:star::star::star:: 1200

:star::star:: 1379

:star:: 5754

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> X, see233 c vfu 33 to 1<br> :date: __2020-12-28 04:03:18__

> Downloading and using this app is a civic responsibility. Contrary to views expressed by conspiracy nuts and the fake news media, this is a good app, and it strikes a good balance between privacy and the need for public health officials to get data. It now incorporates a Linux Foundation sponsored open source project, which makes it even better, and the contact tracing more reliable. Apple and Google want to cut the government and public health officials out of pandemic response, which is dumb.<br> :date: __2020-12-24 19:42:06__

> It's a really good app to stop stpreading the covid-19<br> :date: __2020-12-24 05:09:01__

> Just fell safe knowing i have this app<br> :date: __2020-12-21 23:11:48__

> excellent initiative<br> :date: __2020-12-21 09:34:24__

> Works. Have had it since it was released and no issues.<br> :date: __2020-12-21 07:49:12__

> it keeps you save from the covid<br> :date: __2020-12-21 07:19:35__

> Works as it should. Install says to turn off battery optimisation and location on for this app... so do it; stop being a superstitious idiot and knowall, no excuses.<br> :date: __2020-12-21 06:45:18__

> Thanks for keeping Australia safe<br> :date: __2020-12-21 06:43:49__

> This app is guaranteed 100% Covid Safe. You will not get Covid from this app.<br> :date: __2020-12-21 06:35:06__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> This app does not alert to not being active or requiring an update unless you actually open it...should be better than this.. Update 21 12 20 just got my 1st alert to an update being available..much better<br> :date: __2020-12-21 08:05:41__

> Seems ok<br> :date: __2020-12-21 08:04:09__

> It's a nessasary for the Government to have this, if those that think it's not real, well it's very real so it's an a Must cheers<br> :date: __2020-12-20 23:49:00__

> Works perfectly. Would be 5 star if it didn't stop when it needed an update.<br> :date: __2020-12-20 08:40:56__

> good<br> :date: __2020-12-18 02:03:55__

> Y ?<br> :date: __2020-12-10 10:29:29__

> Covid safe turns itself off every day. How can l keep it on?<br> :date: __2020-12-09 03:37:58__

> I tried to order a pizza twice but it didnt work. I just called the store instead.<br> :date: __2020-12-06 05:44:56__

> no need t have used<br> :date: __2020-12-06 05:15:41__

> Q wa,again. Q<br> :date: __2020-12-05 04:58:27__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> Battery usage seems to have massively increased after the latest update. COVIDSafe app accounted for 25% of my battery usage per day.<br> :date: __2020-12-28 12:00:04__

> Not sure what it is supposed to do. I have it running though.<br> :date: __2020-12-28 04:40:31__

> Update needs location of towns with the numbers of cases of covid<br> :date: __2020-12-27 22:38:54__

> How are you supposed to make the app 'inactive'? My understanding is that once you have downloaded and installed this app it is automatically operational and that is the way it stays. The information seems to suggest that I have to ensure it is operational that I have to ensure it is running. How do I do that? Also I don't have a photo on Google Profile. I've got one on Facebook.<br> :date: __2020-12-27 19:30:43__

> Happy with the security and privacy of the app but every since the Herald protocol update, it's smashed my battery (Galaxy S10)<br> :date: __2020-12-27 03:13:46__

> Had the app for a while but only just recently uninstalled due to all of a sudden high battery usage.<br> :date: __2020-12-25 23:58:51__

> Still conflicts with my Bluetooth headphones after the latest update. (18/12/20) Please fix it.<br> :date: __2020-12-25 23:46:30__

> Have to uninstall. Battery Life had halved since I put it on. Otherwise no problems<br> :date: __2020-12-25 09:50:08__

> Had this app since introduced with no issues. However, after the update the battery use is ridiculous. It uses far more battery in the background(at home alone) than any other actively used app i have. Needs to be addressed if you hope to have more people instal.<br> :date: __2020-12-25 02:42:20__

> I would like more information on where exactly covid is. I'm not sure if I just can't find this setting. Also couldn't everyone have just stayed indoors for a few months so that the 0 wouldn't have gone up to 115 cases now<br> :date: __2020-12-22 00:57:15__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> In one day (with lots of travel), 16 hours background use, 1 min active use, most battery percentage app used at 22%. And it's been for several days that's likely from the new update as some others have said. Although I just found an option to "Optimise battery usage" on as it was off before. Hopefully that fixes.<br> :date: __2020-12-28 11:13:28__

> App is using more power with every update.<br> :date: __2020-12-28 09:04:27__

> From Innisfail, Qld: clubs, pubs, stores R ignoring 1.5m. Tourists & travellers in town. Displayed instructions are UNclear and scattered. I took photos of the QR Code with my Data On and no green tick appeared. Then I sent an SMS with name email and Venue. I'm taking a photo of the QR Code but nothing happens. Try using IN-line steps with the icon and logos beside the steps. Try following your directions without guessing or ad-lib. "Tell us more" doesn't work.<br> :date: __2020-12-28 05:35:07__

> Bluetooth issues. Ever since installing I've had BT issues with other devices not being able to reconnect, without clearing cache and data, then all other devices reconnect for a few days, then problems start again. Edit 27 Dec. 2020. Sick of this randomly burning battery. Fix it dev or will be uninstalling. We are trying to do the right thing, but this app leaves my family vulnerable with potential flat batteries on our phones, which negates usage of this app!<br> :date: __2020-12-28 01:23:22__

> Had to uninstall it because it emptied my battery in no time. Biggest sucker of power since the update. I used it since the beginning but this is rediculous. Hope they fix it in a hurry<br> :date: __2020-12-27 07:25:31__

> Large increase in battery usage after 18th December 2020 update.<br> :date: __2020-12-27 02:18:06__

> It drains my battery like nothing else. It is great to be covid safe but if my phone dies at 2pm it doesn't help anymore. In average it takes about 20-25% of my battery which is unbearable.<br> :date: __2020-12-26 03:53:44__

> The recent 2.0 update seems to have done something to it's battery use. Judging from the feedback here, I'm not alone in noticing a marked increase in battery drain since the update. In my case, with Covidsafe on, the phone will no longer go on deep sleep/doze. It seems to have borked something with wakelocks. I adopted the app immediately on release and have repeatedly encouraged others to do the same, but in it's present state, I can no longer continue. One kludge I can think of is killing the process when not out and about, but that would require remembering to turn it back on again, which, let's face it, is a losing proposition.<br> :date: __2020-12-26 03:49:42__

> Was working just fine in background. A week or so ago it appeared to update. After that it began draining the battery. Now uninstalled. Fix it please.<br> :date: __2020-12-25 21:50:40__

> There is significantly increased battery usage after the Herald update. Consider using ENS instead<br> :date: __2020-12-25 00:26:27__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> Uninstalling due to battery drain. 44% vs the next app which only consumed 12%.<br> :date: __2020-12-28 12:20:36__

> Drain battery significantly.<br> :date: __2020-12-28 12:09:25__

> Latest update killing my battery. Really disappointing that the government decided to release a half baked update eroding the confidence of all users who are trying to do the right thing. You just can't afford to skimp on testing on such a large scale and important app.<br> :date: __2020-12-28 09:52:09__

> The latest update requires my phone location to be on. Uninstalled.<br> :date: __2020-12-28 09:41:41__

> Unable to update. Tried numerous times.<br> :date: __2020-12-28 04:40:24__

> I was previously an advocate of this app because of the purpose of it. But since the latest update my Samsung S6 with Android 7 runs extremely hot and uses the whole battery within 4 hours. This makes both the app and the phone useless. I have turned off the location permission on this app, and now I have my phone back. The app tells me it cannot operate without location permission - I call bull, it worked fine without location services before. If it doesn't work now without the location permission, so what, it doesn't work with the location permission either. There is clearly some pretty poor coding in this version. Let me know when you fix this, until then locations stays off.<br> :date: __2020-12-28 04:10:23__

> Battery drain on latest version<br> :date: __2020-12-27 13:33:07__

> Just 17 cases traced by this app.<br> :date: __2020-12-27 12:36:23__

> Pathetic doesn't work not worth the effort of installing<br> :date: __2020-12-27 10:54:55__

> I wondered why my phone was suddenly unable to go a full day without charging. Turns out since the last update, this app has started using a lot more battery charge. Needs to be fixed asap or I will have to uninstall it, and I won't be the only one.<br> :date: __2020-12-27 09:04:53__


