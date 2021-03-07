# ALHOSN UAE
App version ``1.44.248``

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
| **Latest version** | 1.44.248 |
| **Last update** | 2020-11-10 11:38:29 |
| **Recent changes** | - Improved user experience<br>- App stability |
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
 **android.permission<br>ACCESS_BACKGROUND_LOCATION** | :warning:**Dangerous** | Allows an app to access location in the background. 
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>BLUETOOTH_ADMIN** | Normal | Allows applications to discover and pair bluetooth devices. 
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

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address 'Li/b/a/a/a;->f(Ljava/lang/String;)Ljava/lang/StringBuilder;' on the 'N/A' port <br>
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

The ALHOSN UAE app has been installed by more than **1000000** times. At this time, **6085** rated the app and its average score is **4.3555193**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 4545

:star::star::star::star:: 543

:star::star::star:: 266

:star::star:: 79

:star:: 652

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="doh.health.shield 5 reviews"/>
</p>

> Not working<br> :date: __2021-03-06 12:53:34__

> Good.<br> :date: __2021-03-06 10:56:31__

> good<br> :date: __2021-03-06 07:21:34__

> Good<br> :date: __2021-03-05 19:44:44__

> I to much try but only come like this. Unfortunately has stopped<br> :date: __2021-03-05 15:56:35__

> Excellent<br> :date: __2021-03-05 13:37:53__

> Good<br> :date: __2021-03-05 11:53:27__

> Very good<br> :date: __2021-03-05 08:51:48__

> Nice app<br> :date: __2021-03-05 06:30:07__

> Good<br> :date: __2021-03-04 16:38:07__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="doh.health.shield 4 reviews"/>
</p>

> Good<br> :date: __2021-03-04 16:22:15__

> Good<br> :date: __2021-03-03 12:07:45__

> Nice<br> :date: __2021-03-03 09:25:09__

> Really amazing application।But I applied the covid 19 vaccine. Its been 1 month yet the result has not come Please tell me why my vaccine result did not come thanks please reply me thanks<br> :date: __2021-03-03 09:24:29__

> My registered mobile number is expired... how can I login with another number<br> :date: __2021-02-25 16:33:16__

> Good<br> :date: __2021-02-25 15:57:37__

> Good aap<br> :date: __2021-02-24 15:17:08__

> Excellent<br> :date: __2021-02-23 08:08:48__

> Good<br> :date: __2021-02-21 20:19:20__

> فحصت بتاريخ 16/1 في خمية صحة الكورنيش ابوظبي والى تاريخ اليوم لم نظهر النتيجة ونزلت علي مخالفة 5000 درهم وقدمت تظلم للأسف هذه المرة الثانية لا تظهر النتيجة علما بأن صحة أرسلت لي رسالة بالنتيجة.<br> :date: __2021-02-20 09:45:18__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="doh.health.shield 3 reviews"/>
</p>

> Keep crashing, test results are not updating for past 2 days.<br> :date: __2021-03-04 05:58:17__

> Good<br> :date: __2021-03-03 11:02:12__

> Errors occur<br> :date: __2021-03-03 10:41:48__

> Great to knowing my status<br> :date: __2021-03-02 09:58:14__

> Nice app<br> :date: __2021-02-26 14:20:05__

> Hello how can my app get updated after the covid vaccine already finished 2 does and also pcr test after 28 days<br> :date: __2021-02-24 20:25:03__

> Its terrible<br> :date: __2021-02-24 10:54:01__

> I can't open the apps<br> :date: __2021-02-23 20:45:18__

> Very nice and easy to us<br> :date: __2021-02-20 13:23:48__

> It's not easy to access<br> :date: __2021-02-19 07:53:06__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="doh.health.shield 2 reviews"/>
</p>

> The regulations that shows that you are vaccinated only after 28days of the 2nd dose and only if you keep taking PCR tests make no sense. A vaccination is a vaccination. It should not be dependent on PCR. And the 28 days gap also makes no sense, if you got 2 doses it should reflect on the app along with your last pcr test and status.<br> :date: __2021-03-04 15:34:47__

> It doesn't show that I got vaccinated, though itsalready 3p days from the second dose. So e tests are also missing. Customer service don't respond to calls, and there is no way to co tact anybody.<br> :date: __2021-03-04 14:41:09__

> Its not working my samsung s9 mobile<br> :date: __2021-03-04 08:50:26__

> Not loading user information today.. same with iPhone<br> :date: __2021-03-03 13:00:01__

> Frezze all the time ,have to unistall. And start over<br> :date: __2021-03-03 12:09:08__

> وايد يعلق ولا يسوي تجديد للبيانات<br> :date: __2021-03-03 09:19:27__

> Costumers service no one answer<br> :date: __2021-03-02 19:53:24__

> Test results need to he uploaded MUCH FASTER. Waiting 3 days for a result to show on the app is unacceptable.<br> :date: __2021-03-02 07:50:21__

> This app no updates covid test results ferfect<br> :date: __2021-03-01 04:38:36__

> Good<br> :date: __2021-02-27 02:47:16__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="doh.health.shield 1 reviews"/>
</p>

> Is there any solution for updating vaccination E symbol in the app.. I had completed 28 days and done two Covid tests..😔 still no updation<br> :date: __2021-03-06 12:27:31__

> I can't see my Corona test, so please if any one know another app show the Corona test<br> :date: __2021-03-06 09:12:23__

> Worst app.ever,technical support NO. Is not working keep asking to leave voice message and didn't allowed you to leave it.<br> :date: __2021-03-06 08:29:34__

> Pathetic app and even worse is the technical support. Technical support mailbox is full and they won't pickup the phone. The app doesn't have very basic functionality like changing mobile number. If you don't know how to make app then why it is mandatory for every purpose. Either update this app or kill it, it's rather easy to get results through SMS.<br> :date: __2021-03-06 08:11:42__

> I completed my 2nd dose of vaccination on 27 of January but in alhosn application didn't updated yet..<br> :date: __2021-03-06 07:30:24__

> the app doesn't update on time, i got tested 3 times since feb. 22 and still the result from that day is still posted up to now, how frustrating i badly need this result for my work... and i uninstall and install it again but it didn't work<br> :date: __2021-03-06 03:16:52__

> The most disgusting app I have come across<br> :date: __2021-03-05 22:50:32__

> البرنامج خارج الدولة لايعمل واحاول فتخه منذ حوالي الأسبوعين وحذفته وحملته اكثر من خمسه مرات<br> :date: __2021-03-05 20:28:45__

> good mission<br> :date: __2021-03-05 18:25:41__

> Very bad app because you are not updating my status.<br> :date: __2021-03-05 15:40:05__


