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

> Keeps disappears<br> :date: __2020-07-20 03:36:35__

> Please help TRUMP COVER. UP GOOGLEMAPS MEUNSTERGRITSANDASSOCIATESLLC 442 BLANDING BLVD 333 ORANGEPARK FL 32073<br> :date: __2020-07-18 21:28:50__

> It's better than nothing<br> :date: __2020-07-18 08:14:40__

> Thank you everyone who made this app and installed it because you are contributing to stopping to Covid-19.<br> :date: __2020-07-17 14:31:58__

> Installed easily<br> :date: __2020-07-17 03:10:52__

> Samsung S9. Battery usage over a day by the app is 0.3%. Had it for 2 months and no dramas, don't even notice it. Location required to be on with Samsung but app does not use location.<br> :date: __2020-07-17 01:51:48__

> Keeps The People Safe & Sound in their Homes with their children & family 💫🌺<br> :date: __2020-07-17 00:49:39__

> Eat up data<br> :date: __2020-07-16 16:09:32__

> Works fine without any problems<br> :date: __2020-07-15 21:43:11__

> No issues with blutooth. I suggest people who are struggling with that in the car, turn the radio ABC news on instead of spotify, to keep up with yhe news? Then your phone is free for calls. And get an extra charger for work and car, to deal with the battery drain. These are tough times. Now IS the time to deviate from our comfort zone.<br> :date: __2020-07-15 10:25:05__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> Works as described but last update has messed up my notifications incredibly and i am not only one experiencing this<br> :date: __2020-07-19 12:04:17__

> Hey guys, there must be something wrong with the app in the background, my phone keeps deactivating the app and I have a warning that it's not active, but when I go in the app it says everything is working fine. Then 5 mins later (more or less) it's goes offline again. Then the phone is happy. Then again later on it's all turned off. I got no idea what is going on here<br> :date: __2020-07-18 05:35:12__

> Bit of a power drainer, when at home, switch off Bluetooth and location, icons and settings. But like buying masks, gloves and hand sanitizer, we can all help to beat Coronavirus.<br> :date: __2020-07-16 02:57:34__

> Kept crashing after July Android patches, had to re-install it and is fine now<br> :date: __2020-07-15 10:25:28__

> Works fine on my phone. For security, I turn Bluetooth off, and deny location permissions, as soon as I return home. Also, i suggest to give it a fake name instead of your full name when you register.<br> :date: __2020-07-14 00:44:42__

> Good<br> :date: __2020-07-13 02:40:25__

> App was turning off. Ive deleted it and reinstalled. Appears to be working ok now and doesnt drain battery on android phone.<br> :date: __2020-07-12 07:54:16__

> Put the app on the phone like they said have not had a problem with it Blue tooth OK.<br> :date: __2020-07-08 14:40:30__

> I live in guyana and they do not have guyana in there country list please put guyana now or i will delet this app please really want this app<br> :date: __2020-07-07 02:07:51__

> Would be good if it at least showed how many other devices it's registered, and when.<br> :date: __2020-07-06 16:14:37__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> Seems to work better on Chinese made devices. Probably because that's were the virus was manufactured. It's doing its job as I have been protected from the virus so far. I wish they made a diarorah app that would also prevent me from getting that as well. So far this app as also been invisibly zapping away the cold virus and other germs. If anyone looks sick it's best to point your phone at them with the app on. This will sterilise them to give you enough time to escape without getting COVID<br> :date: __2020-07-20 15:10:53__

> Why not have a sign in button when people got to Venues such as restruants as a digital sign. And have the the Maitre D or someone from the venue witness the customer signing in. That way it won't breach the Privacy ACT as opposed to the current system implemented<br> :date: __2020-07-19 09:38:04__

> I too had the app constantly switch off. SOLUTION: i believe the following two things can help this solution (seems to have helped me through the last day): 1. Settings - Location -... - Scanning - disable Bluetooth Scanning. I believe this interrupts the covidsafe app. 2. Settings - Developer Options (google this to find out how to enable) - enable Bluetooth HCI Snoop Log. Having reported issue and possible solution through the app, why I haven't heard back from Covidsafe app team.<br> :date: __2020-07-18 07:06:19__

> Okay but still unsure if its detecting "live" contacts. I see about 20 strangers a day in downtown Sourhport. How do we know if it's really doing the job?<br> :date: __2020-07-18 05:21:43__

> Causes bluetooth problems. I am quite happy to do my bit to track and stay safe but the bluetooth problems are frustrating<br> :date: __2020-07-15 09:30:49__

> Seems to work but has messed up my lock screen notifications. Please fix.<br> :date: __2020-07-15 08:46:58__

> After the latest update, the notifications on my Moto G6 Plus (running Android 9.0) have been partially obscured and a solid line can be seen across the top of the screen in screensaver mode.<br> :date: __2020-07-15 07:07:58__

> The app is a battery drainer, there's no two ways about it. I use an automation app to disable bluetooth when I'm at home and re-enable when I leave home. That's made a world of difference to my battery life.<br> :date: __2020-07-14 04:52:16__

> Stops other bluetooth apps from working. Motorola g7+ android 10. The app stops Fitbit app from connecting properly. Also will not allow connection with car audio hands-free VW Golf.<br> :date: __2020-07-13 13:54:51__

> Keeps disabled itself due to inability to cope with battery-saving.<br> :date: __2020-07-13 08:05:44__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> needs improvement,.doesn't work properly and needs to be updated , it's useless.<br> :date: __2020-07-19 10:21:34__

> It is not appearing in my notification bar now after update as per other reviews<br> :date: __2020-07-18 15:47:48__

> No issues with this app . Anything to help a sense of normality returning. Changed to 2 stars no longer function on my Android. way to go!<br> :date: __2020-07-18 08:32:44__

> All three model Android I installed has resulted Daily Bluetooth headset and car radio to behave bizarrely and/or not connect at all until this is uninstalled :(<br> :date: __2020-07-18 02:28:17__

> It keeps deactivating. I don't know whether it works or not but what I do know is its always deactivating. I don't always remember to turn it back on. And I shouldn't need to.<br> :date: __2020-07-16 23:28:40__

> Good except for not able to use my car Bluetooth with the app installed, even the laptop won't recognise my phone via Bluetooth when the app is running.<br> :date: __2020-07-16 13:26:05__

> There is a issue with the notification in the status bar where it covers up the next notification to it self<br> :date: __2020-07-16 10:39:09__

> Stops working Activated app and it stops working and disappears from the active apps. Have to constantly check that it is working<br> :date: __2020-07-15 10:38:01__

> I am having trouble getting this to register. When I enter my mobile number to have a registration code SMS'ed to me, I get an error message "please try again later". Tried heaps of times. Could this be fixed ASAP?<br> :date: __2020-07-14 11:26:05__

> Drains phone battery so fast<br> :date: __2020-07-14 10:36:02__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> Was stable now keeps crashing despite uninstalling and reinstalling a number of times. Unreliable and not doing the job promised by the government to protect me ! Disappointing indeed.<br> :date: __2020-07-20 15:48:35__

> Worst tracking app used worldwide. Well done Scumo<br> :date: __2020-07-20 15:21:25__

> Please fix the notification bar issue ASAP<br> :date: __2020-07-20 14:04:02__

> Always turns off and I have to manually restart it. Changed battery settings for the app as required and even tried developer mode. Biggest load of rubbish for 2 million dollars.<br> :date: __2020-07-20 13:53:54__

> Waste of taxpayer money<br> :date: __2020-07-20 13:46:48__

> Ok now the app says my NAME is incorrect! My name is Luke Parry and I know it's correct BECAUSE IT'S MY GODDAM NAME! THIS APP NEEDS TO GET FIXED!!!!! IT DOESN'T WORK FOR ANY OF MY FRIENDS AND FAMILY EITHER AND APPARENTLY THERE ARE NO CASES IN NSW WHEN THE NEWS CLEARLY STATES THERE ARE SO MANY. FIX THIS BLOODY USELESS APP 😠<br> :date: __2020-07-20 13:18:29__

> Keeps going off due to power management issue. Tried everything but won't stay on<br> :date: __2020-07-20 11:13:06__

> Does not help tracing covid. Millions wasted buying this app from a liberal party crony.<br> :date: __2020-07-20 10:49:20__

> Terrible waste of money Zero cases found by this app<br> :date: __2020-07-20 10:31:38__

> $70 million dud. Guess who's paying for it?<br> :date: __2020-07-20 10:30:17__


