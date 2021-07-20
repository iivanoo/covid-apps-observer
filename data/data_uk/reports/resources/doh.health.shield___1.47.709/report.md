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

> Is good<br> :date: __2021-07-19 09:56:30__

> Good<br> :date: __2021-07-18 21:34:02__

> adnan ashraf<br> :date: __2021-07-18 18:49:27__

> Amazing app for UAE government<br> :date: __2021-07-18 16:16:40__

> Good<br> :date: __2021-07-18 13:47:10__

> Become slow now, please rectified<br> :date: __2021-07-18 04:12:34__

> Best<br> :date: __2021-07-18 02:15:09__

> Uae<br> :date: __2021-07-17 20:14:32__

> Useful and informative.<br> :date: __2021-07-17 13:08:48__

> Nic<br> :date: __2021-07-17 11:35:09__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="doh.health.shield 4 reviews"/>
</p>

> Very slow 😑😣<br> :date: __2021-07-14 20:49:47__

> Nice<br> :date: __2021-07-13 13:48:20__

> وايد زين<br> :date: __2021-07-12 03:58:08__

> Great<br> :date: __2021-07-10 18:08:59__

> Al hosn app in is not showing my vaccine<br> :date: __2021-07-10 15:35:41__

> Good<br> :date: __2021-07-08 18:31:38__

> Helpful apps 👍👍<br> :date: __2021-07-02 14:46:12__

> Very good app, its very helpful to show the status of vaccinated for everyone<br> :date: __2021-07-01 08:19:10__

> ALHOSN<br> :date: __2021-06-30 19:21:53__

> Good<br> :date: __2021-06-29 19:07:03__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="doh.health.shield 3 reviews"/>
</p>

> My Vaccination status not updated in this app. Please help.<br> :date: __2021-07-19 07:30:29__

> Both vaccine completed shows only the 2 date and reads as First Dose. Is not linking the completed vaccination<br> :date: __2021-07-18 12:04:29__

> Not updating latest covid 19 result report....<br> :date: __2021-07-16 12:20:38__

> Not working on samsung N8<br> :date: __2021-07-16 05:04:45__

> 🤭😅 h<br> :date: __2021-07-15 11:31:09__

> Faster and easy to use<br> :date: __2021-07-15 06:11:55__

> Not updating.. okay... However I tried everything : uninstall/install , Logged in /out Called 800 ( 15min listening machine) WhatsApp (no reply ) Email ( not delivered).<br> :date: __2021-07-09 16:43:34__

> This apps is not working in my Android mobail,,,, how can i do?<br> :date: __2021-07-08 22:37:41__

> Have issues with number of doses displayed in the app. Showing 3 instead of 2. Shows the date i was supposed to get vaccinated (with the 2nd dose but didn't) as the day i got it and the day i actually did the second dose (one day passed the scheduled day) as the day of the 3rd dose.<br> :date: __2021-07-07 11:03:26__

> Colours are not matching with results<br> :date: __2021-07-05 14:18:00__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="doh.health.shield 2 reviews"/>
</p>

> I hadmy pcr test and though the result is updated from the clinic, it is not being updated in the app<br> :date: __2021-07-18 20:15:32__

> How are you frend to<br> :date: __2021-07-18 12:25:25__

> فكرة ممتازة لكن طريقة تطبيقها ضعيفة، يوجد تأخير في رصد النتائج. لماذا لا يمكن النسخ واللصق لتسهيل الكتابة مثل باقي البرامج الذكية !!<br> :date: __2021-07-18 12:03:49__

> The app refuse to lnstall and download<br> :date: __2021-07-17 17:12:20__

> I have already taken both doses but it shows only one dose.. And that too taken on the day i got my 2nd dose.<br> :date: __2021-07-16 16:33:25__

> There is no option to report issues. Some PCR test results are not showing in this application.<br> :date: __2021-07-16 08:52:06__

> I had a issue of login onetime password i did not receve the password plzzz solve my issue<br> :date: __2021-07-13 21:32:46__

> It has change my photo on reports which could be problematic for me.<br> :date: __2021-07-12 19:35:25__

> I'm trying to open this application but everytime saying that Al hosan app stopping...i uninstalled and installed many times but it's same...please fix this issue as soon as possible Thanks<br> :date: __2021-07-12 19:32:37__

> Not showing test status for two months, support numbers are always busy, support email inbox full and keep bouncing<br> :date: __2021-07-11 14:52:39__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="doh.health.shield 1 reviews"/>
</p>

> Vaccination details not updated properly, tried to reach call center,gets disconnected everytime i select technical support. Tried to contact through email, it says recepient inbox is full. Please help to resolve this issue.<br> :date: __2021-07-19 11:26:48__

> I m tring to submit but it show me tri agn ltr<br> :date: __2021-07-19 10:00:24__

> I am facing issue. My latest PCR report came but not shown on this Aap . Don't know how to fix this<br> :date: __2021-07-18 22:53:06__

> It doesn't show my test results .<br> :date: __2021-07-18 22:41:37__

> Greetings. I am trying to use ALHOSN app but it's showing my number is not registered. Please assist me with this. Regards<br> :date: __2021-07-18 09:27:06__

> Doesn't show my results even though the results has been sent to me via text, it still doesn't appear on the app<br> :date: __2021-07-17 14:25:20__

> Bad<br> :date: __2021-07-17 06:22:16__

> I am not able to add my son details ,please advice for solution...<br> :date: __2021-07-16 18:00:09__

> worst app ever !!!!!even the otp is not accepting<br> :date: __2021-07-16 17:32:31__

> I make test yesterday... the results negative until now no any update on mobile app 🤔<br> :date: __2021-07-16 11:01:38__


