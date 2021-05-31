# ALHOSN UAE
App version ``1.47.669``

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
| **Latest version** | 1.47.669 |
| **Last update** | 2021-05-10 19:16:45 |
| **Recent changes** | - Improved user experience <br>- App stability |
| **Installs**  | 1,000,000+ |
| **Category** | Medical |
| **First release** | Apr 7, 2020 |
| **Size**  | 12M |
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
 | healthshielduae.com | Domains By Proxy, LLC | :us: US | 2020-03-31 19:30:02 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the MCC+MNC of the provider of the SIM<br>
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

The ALHOSN UAE app has been installed by more than **1000000** times. At this time, **20402** rated the app and its average score is **3.8944309**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 13181

:star::star::star::star:: 1452

:star::star::star:: 760

:star::star:: 454

:star:: 4555

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="doh.health.shield 5 reviews"/>
</p>

> Good<br> :date: __2021-05-30 10:21:04__

> THANKYOU AND VERY SHUKRAN TO ALHOS APP. BEING GOOD BE BETTER FOR HELPING [AID] US.<br> :date: __2021-05-30 07:24:39__

> so good....so cool....<br> :date: __2021-05-30 06:13:55__

> This is very good app<br> :date: __2021-05-30 05:47:17__

> Not working in my phone Samsung not9 show keeps stopping<br> :date: __2021-05-30 05:02:41__

> Like<br> :date: __2021-05-29 13:04:20__

> Good<br> :date: __2021-05-29 10:31:13__

> Very good<br> :date: __2021-05-29 02:41:49__

> Goooooood<br> :date: __2021-05-28 17:56:37__

> Dear team, Kindly update my alhosn app vaccination dose taken dates, it's 1st May 2021 and 2nd dose taken on 22nd May. Thanks & regards<br> :date: __2021-05-28 16:53:40__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="doh.health.shield 4 reviews"/>
</p>

> Cool<br> :date: __2021-05-28 18:13:18__

> If it's offline so much help full r all<br> :date: __2021-05-25 15:40:31__

> Why not work on cellular data?<br> :date: __2021-05-24 05:15:24__

> Good<br> :date: __2021-05-20 21:45:32__

> Why Didn't Show My Covid19 Vaccine Report?<br> :date: __2021-05-20 21:22:30__

> Bm<br> :date: __2021-05-20 10:44:18__

> I'm not able to access the app<br> :date: __2021-05-19 18:05:40__

> Nice<br> :date: __2021-05-19 08:37:22__

> Always use it<br> :date: __2021-05-19 06:50:33__

> Truly grateful to Dubai, UAE for the vaccine and for prioritizing public health and safety. Had my 2nd dose in Grand Hyatt, doctor/medical and staff were kind, accommodating and truly helped and assisted to locate my record so I can have to my 2nd dose. Thank you.<br> :date: __2021-05-18 05:12:44__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="doh.health.shield 3 reviews"/>
</p>

> Super aps<br> :date: __2021-05-25 10:20:38__

> The app doesn't open anymore 😕<br> :date: __2021-05-20 19:41:10__

> Takes ages for the test results to show up in the app even though I got the results by sms<br> :date: __2021-05-19 16:59:40__

> Why 2st dose E we get lat after 28 ?<br> :date: __2021-05-18 23:53:07__

> Vaccination status still not shown after more than 2 months of my second dose. Only the fist dose is shown in the app. Regular follow up is difficult as the customer care is always busy.<br> :date: __2021-05-17 08:28:26__

> My vaccine second dose data is still not avilable. I have completed my second dose in Feb. Tried calling toll free num,couldn't connect through<br> :date: __2021-05-17 05:45:43__

> Nice<br> :date: __2021-05-16 14:39:00__

> Good<br> :date: __2021-05-15 12:05:47__

> Please let me download this app I've tried so many time still I can't download it<br> :date: __2021-05-14 16:22:27__

> The application is good but not working outside UAE.<br> :date: __2021-05-11 03:46:27__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="doh.health.shield 2 reviews"/>
</p>

> I'm already vaccinated,last Feb 7 2021,until now the letter E for my app still not appear,I called already the hotline,they told me after 1hour that letter E is appear,<br> :date: __2021-05-28 18:02:48__

> abid Hussain nomi<br> :date: __2021-05-27 12:51:12__

> Plz change colur sceme to make it user friendly and eseaiar to read<br> :date: __2021-05-24 06:57:16__

> My first dose is not updated in alhosn app.I take vaccine in 3rd February. But still not update please update my first dose.<br> :date: __2021-05-23 17:44:17__

> Mashallah Allah<br> :date: __2021-05-22 19:49:31__

> The app is not opening when connected via cellular data. I only get a screen with ALHOSN written. But it opens and connects well when connected via WiFi, why?? At the health center we have to use cellular data and that where the problem starts. Tried everything but still it doesn't work via cellular data connection.<br> :date: __2021-05-22 09:36:24__

> Take to long to updated , and sometimes i get stopped at the boreder because of that<br> :date: __2021-05-21 15:30:59__

> If you're travelling as a tourist to Dubai, but you don't need/get a VISA, how to you get a Unified ID? Without one, tourists can't use this app to show they are vaccinated...<br> :date: __2021-05-21 09:22:12__

> its not working in my mobile<br> :date: __2021-05-20 10:04:35__

> The test result has not come<br> :date: __2021-05-18 03:26:16__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="doh.health.shield 1 reviews"/>
</p>

> Very bad App and very bad customer service I downloaded and I finished my 2 shots of vaccine and now more then 2 months waiting them to get E and still I didn't and when I'm calling them they not replying and not even care about the customer which showed bad feed back from the government<br> :date: __2021-05-30 11:29:56__

> Me and my family did PCR tests 27/05/2021 to go celebrate my birthday in Dubai, results came the 28/05/2021 all negative so then on the 29/05/2021 we returned home to al ain by the border my app never updated so they said go back to Dubai , my family had to go because their apps updated now im stuck here in dubai, we called for hours help desk, customers care no response im a visitor here is this how visitors are treated ?<br> :date: __2021-05-30 11:01:45__

> I can't access the system outside UAE<br> :date: __2021-05-30 10:21:49__

> Not good<br> :date: __2021-05-29 14:35:50__

> I am fully vaccinated and it is not updated in this garbage hosn app<br> :date: __2021-05-29 13:49:22__

> It's not working in my device how to get result<br> :date: __2021-05-28 23:28:44__

> I need open this app<br> :date: __2021-05-28 19:03:32__

> It's not working properly most of the time and technical support team are not responding<br> :date: __2021-05-28 18:26:17__

> Stuck often<br> :date: __2021-05-28 18:11:29__

> Not good... This not working . I finished both my vaccines... Only showing 1 vaccines poor<br> :date: __2021-05-28 16:12:49__


