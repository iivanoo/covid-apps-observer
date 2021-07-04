# COVIDSafe
App version ``2.8``

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
| **Latest version** | 2.8 |
| **Last update** | 2021-07-01 07:35:27 |
| **Recent changes** | Under investigation COVID-19 case numbers added to home screen to align to Department of Health website.  |
| **Installs**  | 1,000,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 25, 2020 |
| **Size**  | 28M |
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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **21081** rated the app and its average score is **3.7387688**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 10971

:star::star::star::star:: 3025

:star::star::star:: 1806

:star::star:: 1166

:star:: 4113

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> Very good 😀<br> :date: __2021-07-04 07:21:15__

> Thank you for doing this app to keep us safe🙏💕<br> :date: __2021-07-04 01:55:13__

> Great Easy to use<br> :date: __2021-07-04 00:24:24__

> Quite concise and precise<br> :date: __2021-07-03 13:00:56__

> GreAt<br> :date: __2021-07-03 11:59:38__

> Good<br> :date: __2021-07-03 03:01:23__

> Used it since it came out. Had no problems. Now provides up to date information.<br> :date: __2021-07-02 01:20:34__

> Drains the battery way to fast<br> :date: __2021-07-01 16:09:48__

> Excellent device<br> :date: __2021-07-01 11:34:03__

> Awsome app<br> :date: __2021-07-01 10:32:09__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> Good app but I cannot select Western Australia from main menu.<br> :date: __2021-07-04 04:44:09__

> Simple to install; just set and forget. Doesn't kill the battery, and helps with the fight against COVID-19. Recommended.<br> :date: __2021-07-03 11:01:12__

> What ever it takes.<br> :date: __2021-07-02 23:34:34__

> Helping community<br> :date: __2021-07-01 23:15:20__

> Vigilant<br> :date: __2021-07-01 12:46:28__

> I don't like wasting battery on constant Bluetooth but I see why it's needed<br> :date: __2021-06-29 00:50:13__

> Would be good if it could cache its operational info if 4G data coverage is not available. With Vodafone this can happen anywhere, any time, it seems but also some places eg Bannister River roadhouse on the Albany Highway, do not have mobile access. Surely it should be possible to store the info and upload it when back within range of a tower?<br> :date: __2021-06-26 17:48:06__

> Seems to work okay for those that do use it .. sadly ignorance is still there so the virus will still spread because of the selfish people who will not use app and expect will not get vaccinated either .. its the way of the people and how we all live now with too many "don't have to do " syndrome which is being taught to our children from a very early age and supported in our education system . Not all the teachers fault they have to do what is set for them . coming right back to bite us now ..<br> :date: __2021-06-26 09:20:52__

> Excellent , sometimes doesn't clear previous contact so you are unable to do your next contact<br> :date: __2021-06-25 08:13:25__

> Excellent as my wife has treatment for cancer each fortnight and it has simplified everything for us.Thank you.<br> :date: __2021-06-25 00:47:32__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> Not up to date with news takes an extra day. Not real time.<br> :date: __2021-07-02 05:05:29__

> Each time I use a q code it logs on recognises the venue and then asks my to install app. Why?<br> :date: __2021-07-02 01:31:51__

> Well it hasn't dion he anything as yet but I hope it will if necessary .<br> :date: __2021-07-01 13:31:39__

> Great idea but I can't keep it active because it drains my battery so fast. So defeats the purpose. Showing the current restrictions in this app is great though, a central place for info.<br> :date: __2021-06-30 13:43:34__

> Zaps my phone battery<br> :date: __2021-06-29 10:27:49__

> Sometimes it doesn't work .<br> :date: __2021-06-29 08:01:24__

> Good<br> :date: __2021-06-28 09:05:55__

> dont think it works<br> :date: __2021-06-27 04:12:40__

> Can't complain about this App. Does what it's supposed to do ,I suppose. Check ins are simple.<br> :date: __2021-06-25 11:09:02__

> Too slow to enter shops<br> :date: __2021-06-25 06:09:26__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> Good concept. Would have been better for one system to work for QR codes and live updates for areas. Then the W.A. police said they used it to track someone(Newspaper) not really of much use. Deleted.<br> :date: __2021-07-04 02:38:04__

> Too much battery usage<br> :date: __2021-07-03 09:36:43__

> I'm giving this one more chance, with this update. If it keeps eating my battery it will go. There's no point having an app if I have no battery to power it.<br> :date: __2021-07-03 01:16:54__

> Works (at least I assume that it works) in the background. Doesn't do much. Shows info for all states except for WA!<br> :date: __2021-06-29 01:20:18__

> sucks battery life far too much<br> :date: __2021-06-27 13:13:48__

> Think designed to trigger after 15 mins close contact - should be changed to 15 seconds . 15 minutes in a shopping queue ? It's just wrong .<br> :date: __2021-06-27 08:51:51__

> Almost useless<br> :date: __2021-06-27 07:51:36__

> I still haven't got the Covid scan screen on my phone. It disappeared a few days ago!!!!! How do I get it back on again?<br> :date: __2021-06-27 06:33:09__

> But 88 ofLLn.n M<br> :date: __2021-06-27 03:02:48__

> Cant select state<br> :date: __2021-06-26 13:46:35__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> This app achieves nothing.<br> :date: __2021-07-04 08:34:33__

> Can I give it a score of zero?<br> :date: __2021-07-04 04:20:41__

> Where is the QR Code Scanner Function?? NSW app much more easy to understand<br> :date: __2021-07-04 02:51:23__

> Tracing data is sent to an offshore company<br> :date: __2021-07-04 02:40:32__

> Dangerous. No help in pandemic<br> :date: __2021-07-04 01:43:15__

> What is the point of this app now that we have to check in everywhere now?<br> :date: __2021-07-04 00:56:36__

> Ducking useless<br> :date: __2021-07-03 12:00:41__

> We have never been told from Govt that this App works, so we need to be told why not!!!!<br> :date: __2021-07-03 10:22:50__

> It's working again , but the reminder about Bluetooth is annoying.<br> :date: __2021-07-03 08:55:38__

> Doesn't get used anymore, false sense of security. This app should be removed.<br> :date: __2021-07-03 07:03:37__


