# Covid Alert DE
App version ``1.0.1``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="Covid Alert DE icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Covid Alert DE |
| **Unique identifier** | gov.de.covidtracker |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=gov.de.covidtracker](https://play.google.com/store/apps/details?id=gov.de.covidtracker) |
| **Summary**  | COVIDAlert, Delaware Division of Public Health helps reduce the spread of COVID |
| **Privacy policy** | [https://docs.google.com/document/d/1n1xZSpCCKc5eDpuJojHcd84k46joRCIR2NysOsQX6JE/edit?usp=sharing](https://docs.google.com/document/d/1n1xZSpCCKc5eDpuJojHcd84k46joRCIR2NysOsQX6JE/edit?usp=sharing) |
| **Latest version** | 1.0.1 |
| **Last update** | 2020-10-01 09:28:55 |
| **Recent changes** | Minor changes and bug fixes |
| **Installs**  | 5,000+ |
| **Category** | Medical |
| **First release** | Sep 8, 2020 |
| **Size**  | 106M |
| **Supported Android version**  | 6.0 and up |

### Description
> With your help, the COVID Alert DE app can help reduce the spread of coronavirus.
<br>The Division of Public Health of the State of Delaware is asking everyone to help tackle coronavirus by downloading and using the COVID Alert DE app every day.
<br> 
<br>If you use the app you will:
<br>•             Be alerted if you have been in close contact with another user who has tested positive for coronavirus.
<br>•             Be able to track your symptoms and get advice on what to do.
<br>•             Protect yourself and others as everyone begins to return to normal life.
<br> 
<br>Your data and privacy are vital. The COVID Alert DE app will NOT:
<br>•             Publicly identify anyone with COVID-19
<br>•             Use your data for any reason other than alerting you that you may be a close contact of someone who is COVID-positive.
<br> 
<br>Use this app for 1 minute a day to make an important contribution to the fight against coronavirus. Protect yourself, your family, your community and the most vulnerable in society. Encourage everyone you know to download and use the Covid Alert DE app where possible.


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
| **Developer**  | Delaware Department of Health and Social Services |
| **Website**  | [https://de.gov/covidalert](https://de.gov/covidalert) |
| **Email** | DHSS_COVIDAlertDE@delaware.gov |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Delaware+Department+of+Health+and+Social+Services](https://play.google.com/store/apps/developer?id=Delaware+Department+of+Health+and+Social+Services) |

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
 **android.permission<br>ACCESS_WIFI_STATE** | Normal | Allows applications to access information about Wi-Fi networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **com.google.android.finsky.permission<br>BIND_GET_INSTALL_REFERRER_SERVICE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | android.com | Google LLC | :us: US | 1997-06-23 04:00:00 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | expo.io | See PrivacyGuardian.org | :us: US | 2011-05-01 21:26:50 |


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
> - This application opens a Socket and connects it to the remote address ' returned no addresses for  ; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>

**Pim data leakage**
> - This application accesses data stored in the clipboard<br>

**Code execution**
> - This application loads a native library<br>
> - This application executes a UNIX command<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The Covid Alert DE app has been installed by more than **5000** times. At this time, **25** rated the app and its average score is **4.04**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 18

:star::star::star::star:: 0

:star::star::star:: 2

:star::star:: 0

:star:: 5

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.de.covidtracker 5 reviews"/>
</p>

> Informative<br> :date: __2020-11-15 03:25:46__

> New. Just installed. However, this important app was very easy to follow and activate. Best of all..ITS FREE! We need this sorta information to help combat Covid. Stay Safe all.<br> :date: __2020-10-25 10:15:47__

> COVIDAlert, Delaware Division of Public Health helps reduce the spread of COVID With your help, the COVID Alert DE app can help reduce the spread of coronavirus. The Division of Public Health of the State of Delaware is asking everyone to help tackle coronavirus by downloading and using the COVID Alert DE app every day. If you use the app you will • Be alerted if you have been in close contact with another user who has tested positive for coronavirus. •<br> :date: __2020-10-25 03:03:52__

> Very informative and hey if it keeps me safer I'm all for it .<br> :date: __2020-10-24 10:58:12__

> Great idea<br> :date: __2020-10-23 02:57:58__

> Jk you'll k. BLM on jk km violin BBC don vso inch ill<br> :date: __2020-10-19 01:51:28__

> Thanks a lot<br> :date: __2020-10-13 20:47:18__

> Good 👍<br> :date: __2020-10-11 03:57:19__

> I think this is a good idea maybe it will help figure out areas that need more help to battle this mess. Stay safe all!<br> :date: __2020-10-08 20:30:51__

> I don't think I have the virus, but I think it's allergy. I do have the symptoms mentioned but have had them for along time (not14days). Question what are the symptoms for animals(cats&dogs) I can not stop them from itching, coughing, feeling slightly bad<br> :date: __2020-09-24 18:16:03__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.de.covidtracker 4 reviews"/>
</p>

> I like to help. Thinking I read directions correctly, now it is clear. . . "Use this app for 1 minute a day to make an important contribution to the fight against coronavirus." I don't know about all that, but the simple and straight forward dashboard is slick. Do your part and pray we get through this post-haste! I find it alarming that Kent County, DE is surrounded by higher infection rates, to the north and south. Software that does not suck is Cool.<br> :date: __2020-10-28 13:49:22__

> Looking for test sites???<br> :date: __2020-10-21 06:23:29__

> This is a great app but the problem is that more residents of delaware need to download the app. Also most of the time only 1000 people check in. I removed it, until more people sign up and report every day.<br> :date: __2020-10-12 00:38:27__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.de.covidtracker 3 reviews"/>
</p>

> Wish it would remind me to enter daily data. And with 35,000 users and only 180 check-ins a day I assume that feature would help others too.<br> :date: __2020-10-01 12:10:51__

> The app needs to be updated as it still talks about 14 days of isilatio. I'm not sure what phase 2 is as we are now at alert level 1<br> :date: __2020-09-26 00:53:51__



#### 2-star reviews

<p align="center">

</p>

No recent reviews available with 2 stars.

#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.de.covidtracker 1 reviews"/>
</p>

> Will not completely install, just hangs.<br> :date: __2020-10-24 21:43:07__

> Whats the use of downloading a dumb app for covid. Im not a robot that a phone thinks i have covid. I rather go to the hospital now and have a check up for me instead of downloading this app. This app can be dangerous and idk know if you guys are trying to look through my phone and seeing what i am talking about to my bf. I thought the government already have our information for a long. But Nooooo, they want to use this to be deep in our asses. I dont trust this app. Bye!<br> :date: __2020-10-18 22:53:52__

> Wow makes you turn on bluetooth and is a complete invasion of privacy. Stay home and hide if you are scared of COVID<br> :date: __2020-09-28 03:50:29__

> Would like to use the app, but the app always hangs when I get to the data page and click on Continue. I' using a Pixel 3 phone, Android 11.<br> :date: __2020-09-24 16:20:30__

> Perpetually stuck waiting for download from Play Store.<br> :date: __2020-09-16 15:17:02__

> I'm from Maryland but travel to Delaware frequently. This app only works on one of my phone, the others are too old. Please expand the API to include phones down to 4.4. Also less than 100 installs (50+) indicates no one is using it at the time of review. This makes this app useless with less than 0.009% user engagement, assuming the everyone who has installed this app is from Delaware - it is actually less. For this type of app to be meaningful, you need to have engagement > 50% of the population or >500,000% more installs.<br> :date: __2020-09-15 21:09:32__


