# COVIDSafe
App version ``1.13.0``

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
| **Latest version** | 1.13.0 |
| **Last update** | 2020-10-12 04:53:33 |
| **Recent changes** | We have introduced new notifications. <br>You can now hide the COVID-19 case statistics on the homepage.<br>We have updated the privacy policy.  |
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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **13457** rated the app and its average score is **2.7380073**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 4022

:star::star::star::star:: 1062

:star::star::star:: 1321

:star::star:: 1470

:star:: 5582

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> Fantastic app<br> :date: __2020-10-24 08:06:23__

> Peace of mind<br> :date: __2020-10-23 16:34:50__

> I don't want the virus<br> :date: __2020-10-22 13:31:50__

> Does its job.<br> :date: __2020-10-22 10:52:05__

> Working fine. For a long time, I was unable to register, but now working. Feeling safer, knowing I will be alerted if I come into contact with a known case.<br> :date: __2020-10-21 12:47:18__

> Great<br> :date: __2020-10-21 05:15:49__

> Good<br> :date: __2020-10-19 13:47:58__

> No issues with the COVID Safe app since I downloaded it months ago. It just runs in the background hassle free.<br> :date: __2020-10-16 22:20:29__

> Hope it does it's job<br> :date: __2020-10-16 04:20:46__

> 😁<br> :date: __2020-10-14 04:10:13__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> A Xxxooo io<br> :date: __2020-10-17 00:00:40__

> ⁴is a great way to start your ml and 6th or even more<br> :date: __2020-10-16 07:23:46__

> I7uui 8th is 4hi<br> :date: __2020-10-09 04:23:06__

> It does what's expected. I have no loss of Bluetooth functions. Fitbit & earphones still run ok. It doesn't collect phone numbers, it collects & stores another phone's bt id number, only if near for 15mins. Those numbrs tell you nothing, even if you could see them. The remotely held database dept. knows the registered phone numbers... only if you d/load your BT id collection, only if you are diagnosed with CV-19. Dislike: Notification uses too much bar space. Wld prfr coloured dot on the icon.<br> :date: __2020-10-08 02:28:46__

> Had no issues with this app EXCEPT that only 25% of the population uses it so what is the point. Probably should have been pushed out to all active mobiles by the Govt, like bushfire warning and the like. Have now uninstalled it as do not come into contact with many people these days and my location has no active cases.<br> :date: __2020-10-07 13:28:13__

> STRUCTUREDOOIOZSAQWWWW<br> :date: __2020-10-05 04:30:43__

> This app has no effect on any aspect of your life unless you come into contact with someone else who has the app AND also has a positive test for COVID. all the scare-mongering about it comes from morons.<br> :date: __2020-10-02 13:06:27__

> Good<br> :date: __2020-10-02 12:00:43__

> Essential to help contains the virus<br> :date: __2020-10-01 00:01:22__

> Would be nice if it had a built-in QR reader so it can provide my encrypted details when checking-in to restaurants, so I don't have to give them my personal details.<br> :date: __2020-09-28 02:12:44__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> Good concept, but after last update, frequently getting notifications that it is not active although when I open the app it is active. Which is it?. I do have permissions for location<br> :date: __2020-10-23 06:28:20__

> I'd been using this OK for months and (probably after an update) I discovered it was asking for location access and no battery optimisation. Having allowed those, it started draining the battery - 27% one day. I removed it, rebooted the phone and reinstalled the app. So far so good today. About 5th in the list of battery users at 1.8%.<br> :date: __2020-10-23 06:28:19__

> Really needs to be improved to support Apple-Google ENS. I don't like now there's issues between device communication, adding this would be very beneficial for the app and all of Australia<br> :date: __2020-10-22 08:58:55__

> Power saving mode is being turned on all the time in spite of being turned off<br> :date: __2020-10-20 22:04:54__

> Have to stay to close for to long! 😵<br> :date: __2020-10-19 22:17:42__

> Be nice to have a simple way to close the app when you're home.<br> :date: __2020-10-19 00:57:45__

> It's a good idea. However I know several young people who believe that the app could be used to track whether they are breaking COVID restrictions so they won't download. Govt should guarantee noone will be prosecuted based on info from the app. Would increase use.<br> :date: __2020-10-17 05:05:21__

> Chews power :(<br> :date: __2020-10-16 09:42:48__

> No idea what the app actually does. Seems useless so uninstalled. Perhaps if there was information or statistics about successful contact tracing using data collected from the app I would keep it updated.<br> :date: __2020-10-15 00:26:30__

> Not sure that it's working though.<br> :date: __2020-10-13 00:23:58__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> Why does the app keep stopping on my android?<br> :date: __2020-10-24 01:46:16__

> Hi . ago 4 2 H we'd h m we6d7 is x7 1!<br> :date: __2020-10-23 02:07:41__

> Keeps turning off.<br> :date: __2020-10-23 01:00:16__

> When first released this app didn't have any issues that concerned me. A subsequent update has resulted in it causing significant battery drain though, with the app now the largest consumer of my phone's battery, using more battery each day than an hour+ of Web browsing.<br> :date: __2020-10-23 00:12:30__

> I do like the idea of this app but as always the implementation isn't great. This app kept interfering with Bluetooth connections: my smart watch and car would constantly drop out and need a manual reconnect. No problems since uninstalling it. I'm in Queensland so it's less of an issue!<br> :date: __2020-10-19 22:13:04__

> I like the idea in principal but jeez it sucks power out of the battery<br> :date: __2020-10-19 16:20:13__

> Does not updated numbers daily<br> :date: __2020-10-16 11:24:08__

> 5.5mm 600mm has 8o9l8y<br> :date: __2020-10-16 07:24:23__

> Be nice if it worked. Despite having the battery optimisation turned off for this app, it keeps coming up "inactive" and telling me to change the setting. I agree and it says active. A few minutes later I get a notification that it's inactive again.<br> :date: __2020-10-15 04:41:05__

> Doesn't tell me if there are cases nearby, which would be the most important thing it could do. Who cares about the number of cases , I can get that info on the news.<br> :date: __2020-10-12 14:11:12__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> chews battery<br> :date: __2020-10-24 01:04:55__

> My phone doesn't allow me to give the app location permission all the time. The options I have are: Allow only while using the app, Ask every time, and Deny. Is this an Android 11 problem? When will it be fixed?<br> :date: __2020-10-23 11:13:04__

> Could have been useful if they built QR scanner in & allowed business to generate codes like service NSW did. Too slow to pivot once it was found Bluetooth not reliable enough.<br> :date: __2020-10-23 05:36:57__

> Went work<br> :date: __2020-10-23 04:33:17__

> App keeps crashing on reboot and launch. Update: still crashing on my Pixel 2 XL.<br> :date: __2020-10-23 02:58:02__

> Crashes when I try to turn it on<br> :date: __2020-10-22 11:19:54__

> Got rid of it<br> :date: __2020-10-22 08:17:31__

> Great concept app but heats up phone and battery killer after latest update.<br> :date: __2020-10-22 07:29:28__

> Drained my battery today. Please investigate possible bug<br> :date: __2020-10-21 09:56:03__

> Was OK. But now it's SMASHING my battery. It's by far the main user of my battery ... delete<br> :date: __2020-10-21 07:46:17__


