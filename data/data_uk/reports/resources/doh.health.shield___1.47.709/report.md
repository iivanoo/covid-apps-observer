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

> thi app is not working in my mobile get on screen . repoted .. ok ?<br> :date: __2021-06-11 13:30:51__

> I like this app my life is save<br> :date: __2021-06-11 13:07:31__

> Very good<br> :date: __2021-06-11 12:55:08__

> Ok<br> :date: __2021-06-11 10:39:43__

> Thank you UAE for keeping us safe!<br> :date: __2021-06-11 09:34:21__

> Very good and perfect app<br> :date: __2021-06-11 09:17:29__

> 👌<br> :date: __2021-06-11 09:03:24__

> Everything is good<br> :date: __2021-06-11 08:20:05__

> 😍🥰🤩<br> :date: __2021-06-11 08:00:45__

> Useful<br> :date: __2021-06-11 05:42:46__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="doh.health.shield 4 reviews"/>
</p>

> Show the result for good<br> :date: __2021-06-11 07:37:32__

> Good<br> :date: __2021-06-10 22:08:02__

> Its very useful especially when entering to Abu Dhabi by showing this App only.<br> :date: __2021-06-10 08:24:21__

> The idea behind the app is fantastic. In practical terms it has some errors. I've had both vaccine shots but only one shows up on my app. I'm not sure how to change this as I've sent the pdfs to the developer.<br> :date: __2021-06-10 06:30:39__

> good job<br> :date: __2021-06-10 04:43:44__

> Good<br> :date: __2021-06-09 17:46:53__

> Excellent Servic<br> :date: __2021-06-09 15:38:06__

> 👍<br> :date: __2021-06-08 21:29:07__

> The app is good generally , but I had 2 vaccine shots and it only shows 1 , so what should I do with this ?? Please help<br> :date: __2021-06-08 15:45:47__

> plz update may information<br> :date: __2021-06-08 07:25:52__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="doh.health.shield 3 reviews"/>
</p>

> Nice<br> :date: __2021-06-11 10:11:19__

> UAE👍BD<br> :date: __2021-06-11 10:04:45__

> doesnt work out of uae..<br> :date: __2021-06-11 10:00:40__

> I cant open this app from my phone why?<br> :date: __2021-06-10 13:24:38__

> App not opening in india<br> :date: __2021-06-10 11:45:12__

> I have been vaccinated for 2 doses first dose was on January 10 2021 and 2nd was on feb 3 2021. but only shows here was feb. 03 abd shows first dose. how come? please help.<br> :date: __2021-06-10 10:18:36__

> App showing my PCR expire what is this?😡<br> :date: __2021-06-10 05:24:57__

> Good<br> :date: __2021-06-07 20:19:41__

> Can I print my vaccine certificate from this app ?<br> :date: __2021-06-07 10:47:44__

> Not working<br> :date: __2021-06-07 10:17:00__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="doh.health.shield 2 reviews"/>
</p>

> OK<br> :date: __2021-06-11 09:40:25__

> Bad<br> :date: __2021-06-10 13:20:54__

> App reports erroneous test results. System doesn't seem to be reliable. Shows vaccine taken three times, while I have only taken two shots only.<br> :date: __2021-06-08 12:11:14__

> my swab and vaccine is not updated<br> :date: __2021-06-03 17:15:04__

> It's not working in Pakistan..please check & solve the issue.<br> :date: __2021-06-02 16:45:19__

> There is no customer care for technical.<br> :date: __2021-06-01 14:36:08__

> I can't update my mobile number on app and tried to send email but it bounce back due to theire inbox was full.<br> :date: __2021-05-30 20:47:34__

> I'm already vaccinated,last Feb 7 2021,until now the letter E for my app still not appear,I called already the hotline,they told me after 1hour that letter E is appear,<br> :date: __2021-05-28 18:02:48__

> abid Hussain nomi<br> :date: __2021-05-27 12:51:12__

> Plz change colur sceme to make it user friendly and eseaiar to read<br> :date: __2021-05-24 06:57:16__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="doh.health.shield 1 reviews"/>
</p>

> Keeps crashing and cannot reset.. Tried reinstall.. But does not work<br> :date: __2021-06-11 13:23:28__

> Alot of errors<br> :date: __2021-06-11 10:59:00__

> Very bad experience my last three covid test report not update<br> :date: __2021-06-11 07:55:23__

> App doesn't work correctly!!!<br> :date: __2021-06-11 06:17:04__

> App is not working on my phone for the past 6 months..Samsung A71..please assist<br> :date: __2021-06-10 19:34:29__

> This app not working in India. Please troubleshoot at the earliest<br> :date: __2021-06-10 18:30:43__

> The app is crashing every time I try opening it. And when trying to get the issue sorted out (the app crashing on my phone and regarding my information not being updated when using the app on another phone) there clearly seems to be no clear cut solution. Tried contacting through WhatsApp, email and the hotline number which clearly was to no avail.<br> :date: __2021-06-10 18:24:59__

> Simply does not work! Does not even open with ID<br> :date: __2021-06-10 18:01:37__

> The app does not open, just shows the loading screen<br> :date: __2021-06-10 17:38:18__

> Very slow working<br> :date: __2021-06-10 17:26:41__


