# ALHOSN UAE
App version ``1.47.709``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="ALHOSN UAE icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | ALHOSN UAE |
| **Unique identifier** | doh.health.shield |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=doh.health.shield](https://play.google.com/store/apps/details?id=doh.health.shield) |
| **Summary**  | ALHOSN UAE allows you to keep your COVID-19 results on your mobile device |
| **Privacy policy** | [https://alhosnapp.ae/en/privacy-policy/](https://alhosnapp.ae/en/privacy-policy/) |
| **Latest version** | 1.47.709 |
| **Last update** | 2021-06-09 20:49:00 |
| **Recent changes** | - Improved user experience <br>- App stability |
| **Installs**  | 1,000,000+ |
| **Category** | Medical |
| **First release** | Apr 7, 2020 |
| **Size**  | 13M |
| **Supported Android version**  | 5.0 and up |

### Description
> The ALHOSN UAE app is the official COVID-19 testing channel for health authorities in the United Arab Emirates, by the Ministry of Health and Prevention.
<br>By using the app, everyone can help stop the spread of COVID-19 and keep their family and friends safe.
<br> 
<br>You can receive your COVID-19 test results directly on your phone with a unique QR code that is proof of your status and that of everyone else around you who also have the app, giving you peace of mind that you can safely interact.
<br>The app can also help trace people who may have come within close proximity to confirmed COVID-19 cases for an extended period of time. It uses short-distance Bluetooth signals to determine when your phone is near another phone that also has the app installed.  Both phones exchange anonymized IDs which are then stored in encrypted form on your phone. Using the anonymized IDs, health authorities can quickly identify and contact people at risk of infection so they can be retested.
<br> 
<br>Put your health in your hands with 3 easy steps:
<br>1.      Download the ALHOSN UAE app
<br>2.      Authenticate with your Emirates ID and phone number
<br>3.      Turn on Bluetooth and push notifications on your smartphone
<br> 
<br>Download the ALHOSN UAE app today and share it with your family and friends.
<br>Together, we can stop the spread of COVID-19
<br>Safer Together.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Ministry of Health and Prevention - UAE |
| **Website**  | [https://alhosnapp.ae/en/contact-us/](https://alhosnapp.ae/en/contact-us/) |
| **Email** | info@alhosnapp.ae |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Ministry+of+Health+and+Prevention+-+UAE](https://play.google.com/store/apps/developer?id=Ministry+of+Health+and+Prevention+-+UAE) |

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
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>CAMERA** | :warning:**Dangerous** | Required to be able to access the camera device. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>QUICKBOOT_POWERON** | - | - 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>REQUEST_IGNORE_BATTERY_OPTIMIZATIONS** | Normal | Permission an application must hold in order to use Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **android.permission<br>WRITE_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to write to external storage. 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | adobe.com | Adobe Inc. | :us: US | 1986-11-17 05:00:00 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | microsoft.com | Microsoft Corporation | :us: US | 1991-05-02 04:00:00 |
 | healthshielduae.com | Domains By Proxy, LLC | :us: US | 2020-03-31 19:30:02 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the ISO country code equivalent of the current registered operator's MCC (Mobile Country Code)<br>
> - This application reads the MCC+MNC of the provider of the SIM<br>
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>
> - This application reads the unique device ID, i.e the IMEI for GSM and the MEID or ESN for CDMA phones<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address 'Lh/b/a/a/a;->f(Ljava/lang/String;)Ljava/lang/StringBuilder;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'hostname == null ' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Code execution**
> - This application loads a native library<br>
> - This application loads a native library: 'tool-checker'<br>
> - This application executes a UNIX command<br>
> - This application executes a UNIX command containing this argument: 'getprop'<br>
> - This application executes a UNIX command containing this argument: 'mount'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The ALHOSN UAE app has been installed by more than **1000000** times. At this time, **22569** rated the app and its average score is **3.9307625**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 14649

:star::star::star::star:: 1780

:star::star::star:: 820

:star::star:: 573

:star:: 4747

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="doh.health.shield 5 reviews"/>
</p>

> Great<br> :date: __2021-07-30 15:32:38__

> I don't know what happened my hosn app not on<br> :date: __2021-07-30 12:47:34__

> Excellent app<br> :date: __2021-07-30 12:06:32__

> Excellent application<br> :date: __2021-07-29 23:01:39__

> Please this app is not operating on my phone<br> :date: __2021-07-29 18:27:59__

> Good<br> :date: __2021-07-29 17:27:25__

> Nice<br> :date: __2021-07-29 12:32:37__

> Good<br> :date: __2021-07-29 06:49:13__

> Gd<br> :date: __2021-07-29 02:58:24__

> Very useful application<br> :date: __2021-07-28 21:30:15__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="doh.health.shield 4 reviews"/>
</p>

> خدمات ممتازة شكرا لكم Very good service thanks for you 💐<br> :date: __2021-07-30 08:29:24__

> Good<br> :date: __2021-07-29 13:05:32__

> It is a good app, but it still needs to be developed to make sure that it works without any issues all times. There was an issue when it did not work before ... Thank you<br> :date: __2021-07-25 07:48:35__

> Good app for COVID vaccination status as well as PCR test report.<br> :date: __2021-07-23 10:10:08__

> Excellent<br> :date: __2021-07-21 17:29:55__

> Good<br> :date: __2021-07-20 23:33:48__

> Very slow 😑😣<br> :date: __2021-07-14 20:49:47__

> Nice<br> :date: __2021-07-13 13:48:20__

> وايد زين<br> :date: __2021-07-12 03:58:08__

> Great<br> :date: __2021-07-10 18:08:59__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="doh.health.shield 3 reviews"/>
</p>

> ...always working...but yesterday a program started updating my mobile and then I was not able to use anymore the application ..."error occured" can you check please or give me advices? Thks<br> :date: __2021-07-28 11:29:42__

> No password arrives to continue use of app<br> :date: __2021-07-25 20:47:52__

> Back button doesn't work on "Report Results" screen I pressed REPORT RESULTS by mistake. I tried to go back immediately to my main screen but the back button doesn't work. Please fix and ensure error paths ie. Zero data, are properly tested OS: Android. Hardware: Samsung Tablet<br> :date: __2021-07-25 13:21:23__

> My Vaccination status not updated in this app. Please help.<br> :date: __2021-07-19 07:30:29__

> Both vaccine completed shows only the 2 date and reads as First Dose. Is not linking the completed vaccination<br> :date: __2021-07-18 12:04:29__

> Not updating latest covid 19 result report....<br> :date: __2021-07-16 12:20:38__

> 🤭😅 h<br> :date: __2021-07-15 11:31:09__

> Faster and easy to use<br> :date: __2021-07-15 06:11:55__

> Not updating.. okay... However I tried everything : uninstall/install , Logged in /out Called 800 ( 15min listening machine) WhatsApp (no reply ) Email ( not delivered).<br> :date: __2021-07-09 16:43:34__

> This apps is not working in my Android mobail,,,, how can i do?<br> :date: __2021-07-08 22:37:41__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="doh.health.shield 2 reviews"/>
</p>

> The app isn't opening on Samsung phones,<br> :date: __2021-07-30 15:04:51__

> Poor application<br> :date: __2021-07-24 06:31:45__

> I hadmy pcr test and though the result is updated from the clinic, it is not being updated in the app<br> :date: __2021-07-18 20:15:32__

> How are you frend to<br> :date: __2021-07-18 12:25:25__

> فكرة ممتازة لكن طريقة تطبيقها ضعيفة، يوجد تأخير في رصد النتائج. لماذا لا يمكن النسخ واللصق لتسهيل الكتابة مثل باقي البرامج الذكية !!<br> :date: __2021-07-18 12:03:49__

> The app refuse to lnstall and download<br> :date: __2021-07-17 17:12:20__

> I have already taken both doses but it shows only one dose.. And that too taken on the day i got my 2nd dose.<br> :date: __2021-07-16 16:33:25__

> There is no option to report issues. Some PCR test results are not showing in this application.<br> :date: __2021-07-16 08:52:06__

> I had a issue of login onetime password i did not receve the password plzzz solve my issue<br> :date: __2021-07-13 21:32:46__

> It has change my photo on reports which could be problematic for me.<br> :date: __2021-07-12 19:35:25__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="doh.health.shield 1 reviews"/>
</p>

> i can't open the apps that i already download why is like this it cant open in my mobile samsung edge 10<br> :date: __2021-07-30 12:00:02__

> This app sucks<br> :date: __2021-07-29 22:04:53__

> The test results are not getting updated. And when we call customer care they say its lab responsibility and lab says its DHAs responsibility. And DHA says it takes 24-36 hours for updating... How can these delays be accounted for?<br> :date: __2021-07-29 12:50:55__

> I got 2 dose of Vaccination. But still this app showing 1st dose.<br> :date: __2021-07-28 10:01:39__

> I can't open this app,, install and reinstall, still nothing happened. What's wrong with this app,, i need to have my vaccination certificate, where can i get that,, for God sake,,<br> :date: __2021-07-27 18:55:28__

> The app does not show the correct vaccine shots that I have taken. I have done the 2 doses already, first in March, and the 2nd in May. However, the app keeps showing that I only took 1 dose, which was the ladt that I took. I have been trying to uninstall/reinstall the app, to no avail. I also tried to call the contact center, but was told to just send a whatsapp, to which I have yet to receive any response.<br> :date: __2021-07-27 11:41:14__

> With foreign numbers, the one time password sent by SMS does not work. The codes arrive with a very long delay and, when you insert them, the app gives error.<br> :date: __2021-07-27 08:38:03__

> good<br> :date: __2021-07-27 06:30:55__

> Cant even open it ... when i click on it at the same sec it close and show me the error massege<br> :date: __2021-07-27 01:27:44__

> Difficult to open or access into the app. How can i open it?<br> :date: __2021-07-26 16:01:14__


