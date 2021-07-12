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

> Good<br> :date: __2021-07-11 09:17:17__

> Verey good<br> :date: __2021-07-11 08:15:35__

> Nic<br> :date: __2021-07-11 05:58:15__

> Nice<br> :date: __2021-07-11 05:43:36__

> Nice app and so helpful,easy to use and save our time, but some times mobile number varification taking long time- while trying to add multiple account showing ocourd eror please pix this -<br> :date: __2021-07-11 05:24:05__

> Excellent 👌🏻😊<br> :date: __2021-07-10 19:09:28__

> Excellent service<br> :date: __2021-07-10 13:27:09__

> May application not working plz check<br> :date: __2021-07-09 18:06:56__

> Good<br> :date: __2021-07-09 16:56:06__

> satisfied<br> :date: __2021-07-09 15:54:46__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="doh.health.shield 4 reviews"/>
</p>

> Great<br> :date: __2021-07-10 18:08:59__

> Al hosn app in is not showing my vaccine<br> :date: __2021-07-10 15:35:41__

> Good<br> :date: __2021-07-08 18:31:38__

> Helpful apps 👍👍<br> :date: __2021-07-02 14:46:12__

> Very good app, its very helpful to show the status of vaccinated for everyone<br> :date: __2021-07-01 08:19:10__

> ALHOSN<br> :date: __2021-06-30 19:21:53__

> Good<br> :date: __2021-06-29 19:07:03__

> Can't we not use this app outside UAE? Even when a resident of UAE travelling outside?<br> :date: __2021-06-29 15:24:50__

> Can you guys please tell me or help me if why my second DOS vaccination is not showing in my Alhosn app?<br> :date: __2021-06-29 12:31:47__

> Not opening in india why..? Pl can you explain<br> :date: __2021-06-29 10:47:37__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="doh.health.shield 3 reviews"/>
</p>

> Not updating.. okay... However I tried everything : uninstall/install , Logged in /out Called 800 ( 15min listening machine) WhatsApp (no reply ) Email ( not delivered).<br> :date: __2021-07-09 16:43:34__

> This apps is not working in my Android mobail,,,, how can i do?<br> :date: __2021-07-08 22:37:41__

> Have issues with number of doses displayed in the app. Showing 3 instead of 2. Shows the date i was supposed to get vaccinated (with the 2nd dose but didn't) as the day i got it and the day i actually did the second dose (one day passed the scheduled day) as the day of the 3rd dose.<br> :date: __2021-07-07 11:03:26__

> Colours are not matching with results<br> :date: __2021-07-05 14:18:00__

> The QR is not readable by normal QR readers which created big problems in Dubai Airport and in other international airports. Please solve the problem<br> :date: __2021-07-05 05:40:16__

> My experience this app not opening help me please<br> :date: __2021-07-04 16:26:31__

> This app was not opening<br> :date: __2021-07-03 10:50:07__

> Crashes a lot, slow to start and eats your battery life.<br> :date: __2021-07-03 09:40:28__

> Can't open<br> :date: __2021-06-30 17:40:38__

> Why does my picture not appear?<br> :date: __2021-06-29 15:06:38__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="doh.health.shield 2 reviews"/>
</p>

> I cannot open the app<br> :date: __2021-07-10 14:13:23__

> Good<br> :date: __2021-07-08 16:00:50__

> I had a issue of login onetime password i did not receve the password plzzz solve my issue<br> :date: __2021-07-08 08:07:22__

> Not open app why<br> :date: __2021-07-07 09:00:19__

> Can't add children<br> :date: __2021-07-06 09:58:53__

> I am trying to open this App from India, but it's not opening at all. It's still in the home page. Is there any geo restrictions for accessing the app. I tried to uninstall and install many times but still facing the same issue. Pls advise..<br> :date: __2021-07-05 06:15:16__

> The app is not Working properly<br> :date: __2021-07-05 06:12:40__

> It's not accurate, and keeps making errors.<br> :date: __2021-07-04 20:12:56__

> I am vaccinated but not show on e. Last march I did vaccination. After that 4 pcr, . I called customer no answer . What should I do.?<br> :date: __2021-07-04 06:31:14__

> Does not work outside the UAE so useless<br> :date: __2021-07-03 09:41:40__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="doh.health.shield 1 reviews"/>
</p>

> I can't open after successfully download, reinstalled 4 times also same issue<br> :date: __2021-07-11 11:41:26__

> QR code not working, you can't travel without scanning QR code at borders so you end up doing PCR because ALHosn doesn't display QR code properly<br> :date: __2021-07-11 10:36:05__

> QR code is not working , can't use the report for travel.<br> :date: __2021-07-11 10:35:26__

> Not working at all,my vaccine shows 4 doses instead of 2 only ,and when trying to scan the QR code ,the message appears as no data found, I logged a complaint with Al Hosn toll free with no success at all,I was given a mobile phone where to send a message explaining my issue with no response up to date.<br> :date: __2021-07-11 08:30:39__

> Excellent Servic<br> :date: __2021-07-11 08:04:58__

> I DONT KNOW WHY I KEEP HAVING THE SAME ERROR MESSAGE WHEN MY NUMBERS ARE CORRECT IN DHA SYSTEM AND WHEN I LOG IN TO THIS APP. SO FRUSTRATING<br> :date: __2021-07-11 07:39:23__

> does not even allow me to open at all after entering all my details. I want my vaccination certificate because the company demands so but I cannot log in<br> :date: __2021-07-11 03:21:56__

> It doesn't show my test results .<br> :date: __2021-07-11 01:11:53__

> Bad , its being 2 days since i took the PCR and got a text saying is negative, but the app is not updated.<br> :date: __2021-07-10 13:10:27__

> The barcode doesn't work<br> :date: __2021-07-10 12:48:45__


