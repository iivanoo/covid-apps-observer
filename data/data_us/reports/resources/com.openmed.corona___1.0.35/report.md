# OpenMed Checker
App version ``1.0.35``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="OpenMed Checker icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | OpenMed Checker |
| **Unique identifier** | com.openmed.corona |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=com.openmed.corona](https://play.google.com/store/apps/details?id=com.openmed.corona) |
| **Summary**  | The only AI Coronavirus symptom checker with the ability to do testing |
| **Privacy policy** | [http://www.openmed.com/privacy](http://www.openmed.com/privacy) |
| **Latest version** | 1.0.35 |
| **Last update** | 2020-05-04 23:09:31 |
| **Recent changes** | Added Antibody Testing<br>Performance Fixes |
| **Installs**  | 1,000+ |
| **Category** | Medical |
| **First release** | Mar 26, 2020 |
| **Size**  | 26M |
| **Supported Android version**  | 4.2 and up |

### Description
> OpenMed Checker
<br>Let us help you stay at home, understand your symptoms and not spread this deadly disease by knowing your disease state status.  
<br>You can use our symptom checker not only for coronavirus but for other issues too.  
<br>You can always call us at 833-OPENMED or download the app OpenMed and we can further help you find care.
<br>If you want to join our laboratory network - contact us at labs@openmed.com
<br>If you are a health plan, provider organization or health system wishing to send your patients to us, contact us at sales@openmed.com. We have many private label / white-label options for the solution you see here with your labs or our partner labs.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 


## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | By OpenMed |
| **Website**  | [http://www.openmed.com](http://www.openmed.com) |
| **Email** | help@openmed.com |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=By+OpenMed](https://play.google.com/store/apps/developer?id=By+OpenMed) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Pie, version 9 (API level 28) |
| **Effective target Android version**  | Pie, version 9 (API level 28) |
| **Minimum supported Android version**  | Jelly Bean, version 4.2.x (API level 17) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>READ_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to read from external storage. 
 **android.permission<br>READ_PHONE_STATE** | :warning:**Dangerous** | Allows read only access to phone state, including the phone number of the device, current cellular network information, the status of any ongoing calls, and a list of any PhoneAccounts registered on the device. 
 **android.permission<br>VIBRATE** | Normal | Allows access to the vibrator. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **android.permission<br>WRITE_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to write to external storage. 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 
 **com.google.android.finsky.permission<br>BIND_GET_INSTALL_REFERRER_SERVICE** | - | - 
 **com.openmed.corona.permission<br>C2D_MESSAGE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | facebook.com | Facebook, Inc. | :us: US | 1997-03-29 05:00:00 |
 | android.com | Google LLC | :us: US | 1997-06-23 04:00:00 |
 | googlesyndication.com | Google LLC | :us: US | 2003-01-21 06:17:24 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | app-measurement.com | Google LLC | :us: US | 2015-06-19 20:13:31 |
 | stripe.com | - | :us: US | 1995-09-12 04:00:00 |
 | pinterest.com | DNStination Inc. | :us: US | 2009-11-26 19:21:23 |
 | twitter.com | Twitter, Inc. | :us: US | 2000-01-21 16:28:17 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |
 | branch.io | Branch | :us: US | 2011-11-10 13:52:13 |
 | bnc.lt | - | - | 2016-11-14 00:00:00 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>
> - This application reads the phone number string for line 1, for example, the MSISDN for a GSM phone<br>

**Location lookup**
> - This application reads location information from all available providers (WiFi, GPS etc.)<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the ': connect, resolve' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Pim data leakage**
> - This application accesses the downloads folder<br>
> - This application accesses data stored in the clipboard<br>

**Code execution**
> - This application loads a native library<br>
> - This application executes a UNIX command containing this argument: '2'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The OpenMed Checker app has been installed by more than **1000** times. At this time, **17** rated the app and its average score is **4.9411764**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 16

:star::star::star::star:: 1

:star::star::star:: 0

:star::star:: 0

:star:: 0

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="com.openmed.corona 5 reviews"/>
</p>

> very useful app<br> :date: __2020-04-13 22:13:59__

> Great App!! Easy and fast!!!<br> :date: __2020-04-10 15:25:14__

> Nice app<br> :date: __2020-04-10 15:19:49__

> Awesome app.<br> :date: __2020-04-07 11:10:29__

> Good job...<br> :date: __2020-04-07 04:29:17__

> Amazing app! Very user friendly, easy to use and understand.<br> :date: __2020-04-06 20:50:09__

> Reliable and helpful app<br> :date: __2020-04-06 20:48:10__

> Awesome application and very useful.<br> :date: __2020-04-02 23:04:45__

> Great app! I love how it works!<br> :date: __2020-04-02 19:30:23__

> Thank you! Openmed . This app is very useful I will share this to my family.<br> :date: __2020-04-02 19:23:14__



#### 4-star reviews

<p align="center">

</p>

No recent reviews available with 4 stars.

#### 3-star reviews

<p align="center">

</p>

No recent reviews available with 3 stars.

#### 2-star reviews

<p align="center">

</p>

No recent reviews available with 2 stars.

#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="com.openmed.corona 1 reviews"/>
</p>

> Don't like it wanted to charge me for a covid19 test when it's all free and asked to much personal information<br> :date: __2021-01-28 10:30:39__


