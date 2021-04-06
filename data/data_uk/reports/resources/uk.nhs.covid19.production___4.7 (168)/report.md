# NHS COVID-19
App version ``4.7 (168)``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="NHS COVID-19 icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | NHS COVID-19 |
| **Unique identifier** | uk.nhs.covid19.production |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=uk.nhs.covid19.production](https://play.google.com/store/apps/details?id=uk.nhs.covid19.production) |
| **Summary**  | Protect your loved ones with the NHS contact tracing app for England and Wales. |
| **Privacy policy** | [https://covid19.nhs.uk/our-policies.html](https://covid19.nhs.uk/our-policies.html) |
| **Latest version** | 4.7 (168) |
| **Last update** | 2021-03-23 15:56:02 |
| **Recent changes** | We have optimised the venue check-in journey to highlight the user benefits of this feature as we come out of national lockdown. Other design, language and accessibility optimisations. |
| **Installs**  | 5,000,000+ |
| **Category** | Medical |
| **First release** | Aug 12, 2020 |
| **Size**  | 9.2M |
| **Supported Android version**  | 6.0 and up |

### Description
> The NHS COVID-19 app is the official contact tracing app for England and Wales. 
<br>It is the fastest way of knowing when you’re at risk from coronavirus. The quicker you know, the quicker you can alert your loved ones, and your community. 
<br>The more of us that use it, the better we can control coronavirus. 
<br>The app runs on proven software developed by Apple and Google, designed so that nobody will know who or where you are. And you can delete your data, or the app, at any time.
<br>It has a number of features: 
<br>Trace: Find out when you’ve been near other app users who have tested positive for coronavirus
<br>Alert: Lets you know the level of coronavirus risk in your postcode district. 
<br>Check-in: Use our simple QR code scanner to check-in to venues like bars and restaurants. You will get alerted if you have visited a venue where you may have come into contact with coronavirus.
<br>Symptoms: Check if you have coronavirus symptoms and see if you need to order a test. 
<br>Test: Helps you order a test if you need to.
<br>Isolate: Keep track of your self-isolation countdown and access relevant advice.
<br>Available in English, Welsh, Arabic (Modern Standard), Bengali, Chinese (Simplified), Gujarati, Polish, Punjabi (Gurmukhi script), Romanian, Somali, Turkish and Urdu.
<br>The app can be used across UK borders in England, Wales, Scotland, Northern Ireland, Jersey and Gibraltar, detecting all relevant contact tracing app users (regardless of them using different official apps), alerting them if they have been in contact with coronavirus. 
<br>The app has been built in collaboration with some of the most innovative organisations in the world. We have worked with medical experts, privacy groups, at-risk communities and we’ve shared knowledge with the teams working on similar apps in many countries.
<br>Protect your loved ones. Please download the app. 
<br>The App is CE marked as a class I medical device in the United Kingdom and developed in compliance with European Commission Directive 93/42/EEC for class I devices.


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
| **Developer**  | Department of Health and Social Care |
| **Website**  | [https://covid19.nhs.uk/](https://covid19.nhs.uk/) |
| **Email** | NHSCovid-19AppStoreSupport@nhsbsa.nhs.uk |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Department+of+Health+and+Social+Care](https://play.google.com/store/apps/developer?id=Department+of+Health+and+Social+Care) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Android10, version 10 (API level 29) |
| **Effective target Android version**  | Android10, version 10 (API level 29) |
| **Minimum supported Android version**  | Marshmallow, version 6.0 (API level 23) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>CAMERA** | :warning:**Dangerous** | Required to be able to access the camera device. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>REQUEST_IGNORE_BATTERY_OPTIMIZATIONS** | Normal | Permission an application must hold in order to use Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | ietf.org | IETF Trust | :us: US | 1995-03-11 05:00:00 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | apache.org | The Apache Software Foundation | :us: US | 1995-04-11 04:00:00 |


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

**Code execution**
> - This application loads a native library<br>
> - This application loads a native library: 'Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The NHS COVID-19 app has been installed by more than **5000000** times. At this time, **99392** rated the app and its average score is **3.6669638**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 51892

:star::star::star::star:: 11604

:star::star::star:: 8445

:star::star:: 5807

:star:: 21644

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 5 reviews"/>
</p>

> NHS app is ok but it need to up date so when u go in to a shop all a drs u can scam your mobile app and then if u been contact with some one with c19 then your nhs app can stepping and let you know<br> :date: __2021-04-04 07:43:59__

> If we all had to use it by law, it would b a very effective tool against covid ! But it isn't so it isn't...<br> :date: __2021-04-04 01:37:41__

> tt44<br> :date: __2021-04-03 18:08:43__

> keeps me safe knowing if I need to be notified I can be, simple & easy to use<br> :date: __2021-04-03 16:41:44__

> Excellent<br> :date: __2021-04-02 23:37:35__

> Very helpful 👍🏻<br> :date: __2021-04-02 18:57:05__

> It would be nice to be able to enter a lateral flow test result.<br> :date: __2021-04-02 16:52:28__

> Great app, does what it says on the tin.<br> :date: __2021-04-02 09:11:52__

> Really 👍<br> :date: __2021-04-01 11:27:47__

> Pah..... Waste of time space and effort on a physical, spiritual and quantum level<br> :date: __2021-03-31 22:10:00__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 4 reviews"/>
</p>

> I find the app is easy to navigate, the information is up to date, but finding local GP or community pharmacy that give the covid 19 vacation is hard to find, been told i qualify for the first vacation and can't find any place local to me to get it?.<br> :date: __2021-04-04 03:53:44__

> Wish we could input more than one postcode as i stay with my boyfriend for a week each month and he lives under a different council so i cant input his postcode. Also would be nice if we could input if we have had the vaccine which would tell others and help them feel more at ease<br> :date: __2021-04-04 00:01:01__

> You can't use the ID that comes with a test kit to record your results<br> :date: __2021-04-01 15:13:45__

> bit annoying I have to have Bluetooth on all the time<br> :date: __2021-04-01 14:31:06__

> Cant we have our vaccination data in here as well<br> :date: __2021-03-29 19:17:39__

> App working fine now after update.<br> :date: __2021-03-29 15:25:17__

> Would be good if you could store your vaccination details incase you lose the card given<br> :date: __2021-03-25 13:19:42__

> Really good app<br> :date: __2021-03-24 21:56:17__

> Could do with more details<br> :date: __2021-03-24 17:53:50__

> Hi its a good app but just wanted something clarified me an my partner haven't been out for 10 days however on my app it stated I have to isolate just wanted to ask if there is a possibility that if you are living in a property which is a terrace house and a neighbour has covid is it possible that it can show on my notification that I have to isolate which shouldn't be the case as had to contact with them?<br> :date: __2021-03-23 19:45:28__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 3 reviews"/>
</p>

> A widget that I could put on my home screen to quick launch the check in screen with the camera open would be nice so I can check into venues with one tap. I rarely check in anywhere at the moment as it's too much of a faff to open the app then click on check in and scan.<br> :date: __2021-04-04 12:10:09__

> Adding results? Why can't I add test results? Is it only if you have a test at the doctors or hospital? It might be an idea to state that on the app if so!<br> :date: __2021-04-03 14:44:23__

> I do leave my phone in the car during shopping and working time. Very helpful app<br> :date: __2021-04-02 11:49:48__

> Will not accept result code for covid test I have had in hospital. Says I may need an update. Checked update latest early March. I'll have another go<br> :date: __2021-04-01 08:34:20__

> It's never told me anything useful, but maybe one day... It also says "loading" rather a lot, not as "fixed" as they think. Main problem is that when there's an update to the status it sounds a notification. At 12:30AM!!!! This is even though I have "do not disturb" on and my phone set to silent. I can't believe it cost £millions or £billions, that'll increase the sales of Porsches in the South East.<br> :date: __2021-03-30 01:40:42__

> Still getting notifications saying it's loading, other reviews have said this and your reply says it's been sorted. No it hasn't!<br> :date: __2021-03-29 08:42:33__

> It is a good app only downside is with my job I do have to have lateral flow test every couple of weeks at work however the app will not allow me to enter the results and have to be put on to a separate site it would be good if it was possible to have a feature on the app that could do this also<br> :date: __2021-03-28 13:42:27__

> Not useful for me as there is no laces for me to go<br> :date: __2021-03-25 02:52:01__

> It's mostly good on many things but when I enter a covid test it won't let me type the code<br> :date: __2021-03-24 22:37:07__

> Does not allow you to enter new covid test results, instead you have have to go via website which takes a long while<br> :date: __2021-03-23 13:05:18__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 2 reviews"/>
</p>

> I dont seem to be getting notifications despite me checking in. The app still says loading<br> :date: __2021-04-03 08:48:26__

> Only applies to NHS testing. I've had many tests by ONS/OXFORD UNI (all negative) but can't enter these results due to lack of a 'code'. Why can't it also cover vaccination?<br> :date: __2021-04-02 02:49:23__

> Not had a notification in a long time, and now the app won't let me check my symptoms, i see the loading bar more times than a gaming app. Big waste of taxpayers money<br> :date: __2021-04-01 09:46:37__

> This App Has to be one the Biggest waste of British Tax Payers Money ever dreamt up. Not because its a bad idea but because it has seemingly financially benefited a few select people and preferred private companies, yet the App has flaws. Also not every wants to remain utterly anonymous so why can't the data from my Government funded lateral flow test be integrated into the app instead of being emailed to me separately? Does the App even work? Having spent a disproportionate time in/out of hospital in 20/21 nearby to Covid positive Patients I've still not had a Ping.<br> :date: __2021-03-30 19:43:44__

> I work as a live-in carer, moving every 6 weeks ... there's no option on the app to change where I live. I have to keep reinstalling it...<br> :date: __2021-03-30 08:08:56__

> Unable to enter test result.<br> :date: __2021-03-29 00:02:30__

> Will not accept lateral flow test code or read the QR code.<br> :date: __2021-03-28 12:02:32__

> Keep getting periods (11+ days) where exposure checks are not shown unless I open both the app and exposure settings. Sometimes I need to uninstall and reinstall the app for it to catch up.<br> :date: __2021-03-25 20:06:08__

> Not worth having, the only place I go where there is a QR code is work<br> :date: __2021-03-25 10:47:50__

> it doesn't do anything<br> :date: __2021-03-25 09:41:07__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 1 reviews"/>
</p>

> Just doesn't present itself as easy it useful<br> :date: __2021-04-04 09:07:04__

> No to vaccine passports.<br> :date: __2021-04-04 00:50:05__

> Removed in protest at vaccination passports. If I'm going to be discriminated against for being young then I'm done restricting my freedoms for boomers. Will reinstall if we go back to all being in this together<br> :date: __2021-04-03 21:45:11__

> It doesn't work on my phone. Says some other app is using the same technology. Update, it is now April 2021, and this app still does not work on my phone.<br> :date: __2021-04-03 17:56:20__

> Bad bad bad. Stop forcing people to download this. Every single time i go to to google play. Some people do not agree to be a part of this plandemic.<br> :date: __2021-04-02 22:52:18__

> Cannot enter test results, error messages every time. Correct code entered and I have the latest version. Will keep it on the phone for track and trace...but overall a bit poor to be honest. Zoe app is much better.<br> :date: __2021-04-02 21:51:22__

> Rubbish like the governments decisions (for legal reasons this is a joke)<br> :date: __2021-04-02 21:04:38__

> Everyone do not use this app! It doesnt work and a waste of money! Demand a pay rise to all nhs staff and delete this app. If you delete this app i mean everyone then no tax payers money will be wasted!<br> :date: __2021-04-02 16:51:43__

> Drains battery as requires Bluetooth but I've never received a notification even though I know I've been around people who tested positive. Local updates useful but that's about it.<br> :date: __2021-04-02 14:26:10__

> This world class App doesnt work. Reason is that it isn't effectively linked to the NHStracing system. NHStracing has contacted me to isolate because I've been in contact with someone with covid, but this app doesn't give me that advice. The App also doesn't accept the Account ID provided by NHStracing. World class in development costs only I'm afraid.<br> :date: __2021-04-02 11:12:38__


