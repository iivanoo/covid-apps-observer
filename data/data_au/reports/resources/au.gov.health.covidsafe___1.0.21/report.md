# COVIDSafe
App version ``1.0.21``

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
| **Latest version** | 1.0.21 |
| **Last update** | 2020-06-04 14:35:03 |
| **Recent changes** | Improved backwards compatibility to include Android 5.1 operating systems.<br>Users can now download the app from non-Australian Google Play stores.<br>Enhancements to accessibility. |
| **Installs**  | 1,000,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 25, 2020 |
| **Size**  | 7.1M |
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
| **Minimum supported Android version**  | Marshmallow, version 6.0 (API level 23) |
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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **11401** rated the app and its average score is **3.3852243**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 5384

:star::star::star::star:: 982

:star::star::star:: 882

:star::star:: 942

:star:: 3208

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> Amazing<br> :date: __2020-06-14 12:24:15__

> Good<br> :date: __2020-06-14 04:54:32__

> It's needed<br> :date: __2020-06-14 02:26:41__

> Good for safety<br> :date: __2020-06-13 12:01:12__

> Very good app, relevant to my safety<br> :date: __2020-06-13 09:34:55__

> Would be irresponsible to not have this app. It will help Australia prevent large outbreaks and allow us to live more normally. The reviews about Bluetooth dropping out seem to not be generally true. I use Airpods via Bluetooth with my Samsung S8 and it all works fine.<br> :date: __2020-06-13 06:21:34__

> Good<br> :date: __2020-06-13 05:37:57__

> IAM happy that I have the CovidSAfe 19 on my phone and would like my grandson to have the CovidSAfe 19 on his phone and my granddaughter too Pattrich, Catherine Kennedy.my family in Bendigo.thank you.<br> :date: __2020-06-12 20:17:27__

> After a few updates it finally became the app that just runs in the background without impacting other apps, Bluetooth, etc. Its just there in the background and i don't even remember i have it installed<br> :date: __2020-06-12 03:16:33__

> Ido use this app regularly to check how things are going.<br> :date: __2020-06-11 19:27:20__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> Tip: as the app conflicts with my Bluetooth headphones. You can go to settings > apps > force stop. As needed. An official fix would be nice 😊<br> :date: __2020-06-14 07:10:17__

> Workwell I haven't met anyone with the virus<br> :date: __2020-06-12 12:48:54__

> Good to see the latest update to include older android versions seems to be working my bluetooth headset stops playing for a second when someone's close<br> :date: __2020-06-10 19:39:16__

> This app is really smashing my battery life!<br> :date: __2020-06-09 11:14:01__

> Easy to use, simple<br> :date: __2020-06-09 02:46:49__

> The app crashes on launch for me now. EDIT: I fixed this by clearing the apps data from storage, but that of course means that all contacts I've logged over the past few weeks have been lost.<br> :date: __2020-06-08 13:35:39__

> Please remove it from the notification tray it is annoying, the small symbol above like wifi bluetooth ect is fine. Happy to help fellow Aussies. 5 stars if that is fixed.<br> :date: __2020-06-08 04:40:44__

> Mmm<br> :date: __2020-06-08 02:57:17__

> Fine. I would give it 5 stars if the icon wasn't changed from the subtle and stylish grey shield to the bland green Aus logo.<br> :date: __2020-06-08 02:29:46__

> need more stats showing growth/decline<br> :date: __2020-06-07 02:11:23__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> Bluetooth dropouts... Disappointing but I guess it serves its purpose..<br> :date: __2020-06-14 11:03:05__

> Apps a good idea, I'm relying on this apps to keep my family and myself safe but it keeps on turning itself off.<br> :date: __2020-06-13 12:46:39__

> This app should not need location data and should run in the background without pop ups<br> :date: __2020-06-12 07:00:18__

> Does seem to also work on android 5.0.1 Install is a bit funny as it hung on permissions page but still installed. Couple restarts but basically mostly stable and running.<br> :date: __2020-06-11 09:00:31__

> It works out for all<br> :date: __2020-06-10 12:23:24__

> The app serves its purpose however given the link to Bluetooth is it creating no end of Bluetooth connectivity issues resulting in the dropping put of other bluetooth connected devices (headphones, Android auto, etc)<br> :date: __2020-06-10 01:13:23__

> It causes repeated drop out of my Bluetooth devices (headphones, smart watch etc.). I have also found the latest update is causing a significant increase in battery drainage which is incredibly annoying.<br> :date: __2020-06-08 14:58:20__

> Still not 100% sure it is the app or just a huge coincidence. Ever since I have installed the app, my Bluetooth in the car gets momentarily disconnected. While it does reconnect, it is a real issue as it invariably happens during a call. If it keeps happening, I will uninstall and see if things improve.<br> :date: __2020-06-08 11:17:09__

> Keeps on bugging my BT connections as I use a BT headphone<br> :date: __2020-06-08 02:19:43__

> Needs to be more compatible with older device. Drains the battery, my phone is about 3+ years old. Keep bluetooth off and disable app permissions unless i leave the house. Easy to install.<br> :date: __2020-06-07 21:41:19__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> It was ok at first, but i noticed lots of connectivity issues and CovidSafe was the last app installed, after uninstalling the app, connection issues appear to be resolved.<br> :date: __2020-06-14 08:21:30__

> Keeps asking for battery optimisation permission everytime<br> :date: __2020-06-13 06:16:13__

> Nice idea but uninstalled as it causes connectivity issues with other devices, most importantly hands free in the car. Also causes much higher battery drain.<br> :date: __2020-06-13 02:02:31__

> Bluetooth issues. Ever since installing I've had BT issues with other devices not being able to reconnect, without clearing cache and data, then all other devices reconnect for a few days, then problems start again.<br> :date: __2020-06-13 01:59:59__

> Great initiative but destroys your Bluetooth audio. Constant skips and pauses with a variety of speakers that all work fine without this app installed.<br> :date: __2020-06-12 12:39:29__

> Over the last 2 weeks the app keeps crashing several times a day. This will stop it doing it's job if you come into contact with a known case when the app isn't functioning. The only way i can see it has crashed is by looking at the screen. No sound happens when it crashes.<br> :date: __2020-06-12 01:56:00__

> Yes it installs on 5.1 now but gets stuck after enabling Bluetooth. Proceed does not enable battery optimisation off and Bluetooth location. Oppo R7+ with ColorOs.<br> :date: __2020-06-12 00:18:12__

> Constant issues with Bluetooth dropping out when playing music<br> :date: __2020-06-11 05:14:42__

> Lots of Bluetooth connectivity issues. Not connecting or long time to connect. Smart watch will not connect at all. Bit frustrating.<br> :date: __2020-06-10 22:49:44__

> I really want to use this app as it is a great idea. However since installing it, I've had nothing but issues with my phone, issues with updating important apps for work, even battery life is messed up. App can't work without an alive phone, and phone can't stay alive if said app drains it of all power before it has a chance to do anyone any good. So it's a no for me regarding the installation of this app. I stick to what we have been doing since this all started. Keep distance and wash hands.<br> :date: __2020-06-10 15:04:54__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> Gives no information about status<br> :date: __2020-06-14 15:02:03__

> My screen locks and goes blank any time I revive or make call. Have to uninstalled, friend has same issue. Tried re installing, issue is back.<br> :date: __2020-06-14 06:32:55__

> I had to uninstall do to issues with black screen during phone calls Sony Xperia XA2. I couldn't use the keypad, speaker or even end calls. No problem since uninstalling.<br> :date: __2020-06-14 05:57:20__

> I installed it couple weeks ago and checked it few times since then. It is never active. Always requires something else although i allowed all app permissions.<br> :date: __2020-06-14 03:34:57__

> Too easy to accidentally disable or remove when in use or it crashes (either way you think it's working but it's not) also had to uninstall and reinstall because "push notifications" refused to activate. Would be nice too to be told someone near you has the app up and running otherwise what's the point? btw had no problems prior to last update!<br> :date: __2020-06-14 02:56:15__

> It's stopped working. Crashes every time I relaunch it. This is in the last couple of days. Please fix it!<br> :date: __2020-06-14 01:21:12__

> Installed this app when it was first released but it's caused so many issues on my phone, blocking Bluetooth, whatsapp messages and app downloads. I've tried it three times now and each time have had to uninstall after a few days as the reduced phone function is too impractical. Very disappointing.<br> :date: __2020-06-13 15:51:50__

> This worked well before you "fixed" it. Now it continues to crash.<br> :date: __2020-06-13 12:42:58__

> Ever since downloading the app my phone battery dies within a few hours. The same happens to my parents phones. I'm now deleting the app. Useless.<br> :date: __2020-06-13 12:11:20__

> Any app that forces a notification on my notification bar all the time is disabled at best, uninstalled usually. Get rid of that dumb feature<br> :date: __2020-06-13 11:30:29__


