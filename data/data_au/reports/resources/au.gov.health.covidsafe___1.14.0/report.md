# COVIDSafe
App version ``1.14.0``

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
| **Latest version** | 1.14.0 |
| **Last update** | 2020-11-06 21:39:47 |
| **Recent changes** | User registration issue fixed. |
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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **13577** rated the app and its average score is **2.750366**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 4075

:star::star::star::star:: 1143

:star::star::star:: 1282

:star::star:: 1471

:star:: 5606

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> " great"most people i hope would have this app.<br> :date: __2020-11-07 08:36:05__

> Keeps track of the covid<br> :date: __2020-11-04 06:51:38__

> VeryGood ! Thanks 😊 !<br> :date: __2020-11-03 00:18:07__

> Great app that restricts me from disabling my location or GPS!!!<br> :date: __2020-10-30 06:59:21__

> Created very quickly.<br> :date: __2020-10-29 22:28:43__

> Is good<br> :date: __2020-10-28 22:54:05__

> Quite happy nowing what this can mean to me and my family.. at work as i take temps at vline pod a.all staff and visitors. Haven't had any problems with high temps at all. Thank god.<br> :date: __2020-10-26 05:10:33__

> Very good<br> :date: __2020-10-26 03:33:08__

> Fantastic app<br> :date: __2020-10-24 08:06:23__

> Peace of mind<br> :date: __2020-10-23 16:34:50__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> I don't mind if it runs in the background, just let me hide the persistent notification. I don't need it to tell me it's running, I've already accepted the terms and agree to all the permissions.<br> :date: __2020-11-08 02:23:07__

> Any thoughts about adding a QR code reader to this app?<br> :date: __2020-10-28 03:53:25__

> A m still in when l look at spinning wheel okay?..<br> :date: __2020-10-27 02:35:54__

> 👍👍👍👍👍<br> :date: __2020-10-26 05:38:58__

> Seems good, doesn't drain my battery. It would be good to see the app show how many daily cases in each state, not just the total of all states.<br> :date: __2020-10-24 23:07:32__

> A Xxxooo io<br> :date: __2020-10-17 00:00:40__

> ⁴is a great way to start your ml and 6th or even more<br> :date: __2020-10-16 07:23:46__

> I7uui 8th is 4hi<br> :date: __2020-10-09 04:23:06__

> It does what's expected. I have no loss of Bluetooth functions. Fitbit & earphones still run ok. It doesn't collect phone numbers, it collects & stores another phone's bt id number, only if near for 15mins. Those numbrs tell you nothing, even if you could see them. The remotely held database dept. knows the registered phone numbers... only if you d/load your BT id collection, only if you are diagnosed with CV-19. Dislike: Notification uses too much bar space. Wld prfr coloured dot on the icon.<br> :date: __2020-10-08 02:28:46__

> Had no issues with this app EXCEPT that only 25% of the population uses it so what is the point. Probably should have been pushed out to all active mobiles by the Govt, like bushfire warning and the like. Have now uninstalled it as do not come into contact with many people these days and my location has no active cases.<br> :date: __2020-10-07 13:28:13__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> How can this app be using more than 41% of my phone's battery??? This is ridiculous<br> :date: __2020-11-07 12:14:29__

> I really like the idea of this app if it actually worked... But it doesn't. It continually pops up notifications telling me it's not connected because my Location isn't open when it clearly is. I've also now noticed that even though I have selected Auto Update so I will get the most recent numbers it's not updating either. Example: NSW has been showing most recent number as 14 new cases for days & I had just seen the Premier's speech for today & we have 4 new cases. Even allowing for 24hour turnaround that is still wrong. I'll be interested to see homuch longer we are consistently getting 14 new cases per day. C'mon techs we expect much better than this when you pushed so hard for everyone to download this app. There's no point in having it that I can see. If anyone knows a Web page that simply gives current updates per area searched please help me as I'm in the very high risk category & would like to be aware if/when there's new cases to be aware of. Thanks everyone it sure looks to me like the online community will be more help to me than the official govt app at this point. Unless of course they put the effort in to have it work properly because short of a miracle we are stuck with this virus for the forseeable future &ppossibly beyond.<br> :date: __2020-10-30 02:07:56__

> I don't get codes will I need two get scanning or anything else if you'll be pretty please do something about this I will be gripple<br> :date: __2020-10-26 06:36:18__

> I'd been using this OK for months and (probably after an update) I discovered it was asking for location access and no battery optimisation. Having allowed those, it started draining the battery - 27% one day. I removed it, rebooted the phone and reinstalled the app. So far so good today. About 5th in the list of battery users at 1.8%.<br> :date: __2020-10-23 06:28:19__

> Really needs to be improved to support Apple-Google ENS. I don't like now there's issues between device communication, adding this would be very beneficial for the app and all of Australia<br> :date: __2020-10-22 08:58:55__

> Power saving mode is being turned on all the time in spite of being turned off<br> :date: __2020-10-20 22:04:54__

> Have to stay to close for to long! 😵<br> :date: __2020-10-19 22:17:42__

> Be nice to have a simple way to close the app when you're home.<br> :date: __2020-10-19 00:57:45__

> It's a good idea. However I know several young people who believe that the app could be used to track whether they are breaking COVID restrictions so they won't download. Govt should guarantee noone will be prosecuted based on info from the app. Would increase use.<br> :date: __2020-10-17 05:05:21__

> Chews power :(<br> :date: __2020-10-16 09:42:48__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> ĎxxxDeX zzx is zdx acc ccsf carfax xterra accdexzdx ďzd DVD acc x zdx acc d zdx d DVD zdx zdx DVD DVD ďd zdx d zdx zdx DVD zdx DVD DVD d DVD DVD zdx DVD zz zfs DVD d DVD d DVDs dd zdx z xtc DVD DVD DVD zdx zdx DVD DVD db's evac x DVD zdx DVDy DVD DVD uou 7 bagdad bagdad d DVD77did zdx<br> :date: __2020-11-08 07:20:17__

> Uses my limited data<br> :date: __2020-11-03 08:21:01__

> I used to be able to check my km radius from my home, but can't seem to access that function any longer<br> :date: __2020-10-29 23:10:30__

> Says it needs internet. Notification always on. Annoying.<br> :date: __2020-10-26 12:10:10__

> On s20 ultra need to restart the app if your phone battery died on you by overuse as it doesn't start automatically when you run out of juice mostly when I'm streaming videos. Took a star off due to the generic email response from customer service<br> :date: __2020-10-26 07:35:10__

> Last 10 days it has switching off<br> :date: __2020-10-25 23:11:55__

> Why does the app keep stopping on my android?<br> :date: __2020-10-24 01:46:16__

> Hi . ago 4 2 H we'd h m we6d7 is x7 1!<br> :date: __2020-10-23 02:07:41__

> Keeps turning off.<br> :date: __2020-10-23 01:00:16__

> When first released this app didn't have any issues that concerned me. A subsequent update has resulted in it causing significant battery drain though, with the app now the largest consumer of my phone's battery, using more battery each day than an hour+ of Web browsing.<br> :date: __2020-10-23 00:12:30__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> NEW Prevent phone from sleeping and NEW Receive data from the internet. Why have these permissions been added?<br> :date: __2020-11-07 11:32:57__

> Stopped working and hadn't kept itself updated. Typical Scomo fail.<br> :date: __2020-11-07 09:47:30__

> Abysmal software for such an important job...<br> :date: __2020-11-07 07:15:50__

> .9collinsva. yh. Bbu 6t h. Ole the ,ee7uys h h 66 u uhh h k y e u n y k 9 E xxx ggug 8i 7 hhg w . D 7s uu k<br> :date: __2020-11-07 01:31:07__

> Nil<br> :date: __2020-11-05 07:12:53__

> The app constantly turns itself off and needs to be restarted every couple of days. It also pops up stating it needs certain settings that are already enabled.<br> :date: __2020-11-05 04:06:36__

> Total lack of information. Nobody seems to be running this useless app. Absolute disgrace for the minister in charge of it. Never heard a word from him. No idea if it is used at all or just switched off. A major deceit on the Australian public. Lukily the States are manually doing what this National app was supposed to do.<br> :date: __2020-11-04 15:29:14__

> Stats are never given in the media. If it helped significantly, they would be trumpeted by Scomo.<br> :date: __2020-11-02 10:50:21__

> Great idea in principle, terrible execution. The app constantly stops working and requires you to reopen the app several times a day to work. It also now requires GPS to work which is in contradiction to what has been stated.<br> :date: __2020-11-02 04:57:11__

> Absolute rubbish<br> :date: __2020-11-01 12:40:28__


