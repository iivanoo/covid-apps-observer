# Indiana WIC
App version ``3.0``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="Indiana WIC icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | Indiana WIC |
| **Unique identifier** | gov.in.isdh.inwic |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=gov.in.isdh.inwic](https://play.google.com/store/apps/details?id=gov.in.isdh.inwic) |
| **Summary**  | The INWIC app gives clients information on stores, benefits, and clinics. |
| **Privacy policy** | [https://www.in.gov/core/privacy.html](https://www.in.gov/core/privacy.html) |
| **Latest version** | 3.0 |
| **Last update** | 2020-06-30 20:04:21 |
| **Recent changes** | -Spanish language version release<br>-Product image updates<br>-Notifications and push alerts updated for Online Nutrition Education |
| **Installs**  | 100,000+ |
| **Category** | Health & Fitness |
| **First release** | Sep 27, 2017 |
| **Size**  | 78M |
| **Supported Android version**  | 4.4 and up |

### Description
> The Indiana Women, Infants, and Children (WIC) mobile App locates WIC approved stores, allows clients to view current and future WIC benefit balances, scan UPC codes, locate clinics and view appointments.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/>  | <img src="screenshot_5.png" alt="screenshot" width="300"/>  | <img src="screenshot_6.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_7.png" alt="screenshot" width="300"/>  | <img src="screenshot_8.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | Bob Clarke |
| **Website**  | [http://www.in.gov/isdh/](http://www.in.gov/isdh/) |
| **Email** | inwic@isdh.in.gov |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Bob+Clarke](https://play.google.com/store/apps/developer?id=Bob+Clarke) |

## Android support

| | |
|-------------------------|-------------------------|
| **Declared target Android version**  | Pie, version 9 (API level 28) |
| **Effective target Android version**  | Pie, version 9 (API level 28) |
| **Minimum supported Android version**  | KitKat, version 4.4 - 4.4.4 (API level 19) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_COARSE_LOCATION** | :warning:**Dangerous** | Allows an app to access approximate location. 
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_LOCATION_EXTRA_COMMANDS** | Normal | Allows an application to access extra location provider commands. 
 **android.permission<br>ACCESS_MOCK_LOCATION** | - | - 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>ACCESS_WIFI_STATE** | Normal | Allows applications to access information about Wi-Fi networks. 
 **android.permission<br>CAMERA** | :warning:**Dangerous** | Required to be able to access the camera device. 
 **android.permission<br>FLASHLIGHT** | - | - 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>MEDIA_CONTENT_CONTROL** | Not for use by third-party applications due to privacy of media consumption | Allows an application to know what content is playing and control its playback. 
 **android.permission<br>READ_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to read from external storage. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **android.permission<br>WRITE_EXTERNAL_STORAGE** | :warning:**Dangerous** | Allows an application to write to external storage. 
 **android.permission<br>WRITE_USER_DICTIONARY** | - | - 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 
 **gov.in.isdh.inwic.permission<br>C2D_MESSAGE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | flurry.com | Oath Inc. | :us: US | 1998-05-04 04:00:00 |
 | googlesyndication.com | Google LLC | :us: US | 2003-01-21 06:17:24 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the numeric name (MCC+MNC) of current registered operator<br>
> - This application reads the operator name<br>
> - This application reads the unique device ID, i.e the IMEI for GSM and the MEID or ESN for CDMA phones<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Code execution**
> - This application loads a native library: 'monodroid'<br>
> - This application loads a native library: 'monosgen-2.0'<br>
> - This application loads a native library: 'xamarin-app'<br>
> - This application loads a native library: 'xamarin-debug-app-helper'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The Indiana WIC app has been installed by more than **100000** times. At this time, **735** rated the app and its average score is **4.06**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 464

:star::star::star::star:: 110

:star::star::star:: 29

:star::star:: 7

:star:: 125

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.in.isdh.inwic 5 reviews"/>
</p>

> I just installed the app, I love that I can see all my items, when and the time of my next appointment ... I will still be experiencing how everything works. And I will update my opinion according to the use that I put it. The only detail maybe only happened to me, but when registering I was not allowed to enter my date of birth quickly, I had to go month by month back, until I reached my year of birth. If you can review to correct that it would be a success. Perhaps it was a single failure.<br> :date: __2020-10-17 21:02:30__

> Awesome<br> :date: __2020-09-16 07:38:35__

> Our mom needs for baby is good and<br> :date: __2020-09-07 05:14:08__

> I love that this app kiss me update with Future appointments and what I currently have on my card<br> :date: __2020-08-31 03:48:01__

> Very helpful<br> :date: __2020-08-18 01:07:35__

> Can't log in with Facebook link anymore. "App is in development mode"<br> :date: __2020-08-08 23:01:41__

> I love it, but some grocery stores my phone loses signal.<br> :date: __2020-08-06 20:44:53__

> This app helps me out alot especially when I go to the store and cant remmember what all I can get with my benifets. You just log in and it tells you.<br> :date: __2020-07-01 23:08:59__

> Very convenient I recently updated this app by un-installing it and re-installing it and it works perfectly now. I have an Android Redmi note 8. Would be nice in the future if I don't have to un-install and just update but it did save my info and password so that's nice.<br> :date: __2020-06-26 05:33:59__

> Came back to edit my review because I updated the app yesterday and now whenever I log in it tells me that my session has timed out and then closes the app on me. I've been trying all day to check what I have on my card. Extremely inconvenient! I've had the app for over a year and never had any problems until I did the update yesterday. Will probably try uninstalling and reinstalling to see if it works.<br> :date: __2020-06-25 08:03:45__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.in.isdh.inwic 4 reviews"/>
</p>

> great app. Just wish you could do the education requirements on it.<br> :date: __2020-09-06 15:40:38__

> Love it<br> :date: __2020-08-21 06:07:52__

> Let's me know what I need to get<br> :date: __2020-06-28 21:40:46__

> The last week when i log in and try to view my bennifits or anything it say my session has expired to try again and logs me out. Ive tried closing the app and restarting it multiple times.<br> :date: __2020-06-26 17:06:37__

> For those of you having issues with saying session expired try uninstalling it and reinstalling the app. I did that and it works fine now, no issues<br> :date: __2020-06-17 22:14:45__

> Good besides it saying session expired when it isn't.<br> :date: __2020-06-17 18:41:15__

> 7to<br> :date: __2019-08-17 01:37:46__

> wish the list of what you can get was on here but i still love the app<br> :date: __2019-08-06 05:47:00__

> it's a really big help for when shopping so you don't have to carry around the pamphlet.<br> :date: __2019-06-21 01:52:32__

> the scanner does not work well. other than that it's very handy.<br> :date: __2019-06-10 16:01:39__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.in.isdh.inwic 3 reviews"/>
</p>

> Newest update broke the app. Edit: was fixed by full remove and reinstall, but having to do so is still absurd.<br> :date: __2020-06-18 19:13:40__

> Keeps saying "session expired" when I log in and automatic logs me back out.<br> :date: __2020-06-16 00:57:01__

> It dont show everything on your food list.<br> :date: __2020-04-25 00:41:43__

> I love this app when it's working properly. Often when I try to sign in through my Google account, instead of redirecting back to the app so I can check what items I have remaining on my card, it direct to the Google homepage and never signs me in. If they can get it fixed I will change my review.<br> :date: __2019-10-05 14:44:22__

> Good<br> :date: __2019-09-12 03:54:11__

> \*\*UPDATE\*\* I am an android user, I cleared the cache for the app specifically and the app is now working.... Not working after update....crashes upon opening app. Notified WIC office at my last appointment and they informed me that they had no other complaints of this.<br> :date: __2019-07-14 15:36:21__

> This app was doing great and all of the sudden it will not let me open the app. Please fix this soon. Thank you<br> :date: __2019-05-11 00:32:59__

> Will give more stars when I can Move to SD Card.<br> :date: __2019-03-08 18:44:35__

> I like the app for being able to check my benefits balance, but it doesn't notify me when my benefits are ending for the month like it said it would<br> :date: __2019-01-28 21:03:25__

> I was wondering when an app update was going to available for this. They updated what you can get with your WIC now, but it isn't updated on the app.<br> :date: __2018-10-10 17:54:29__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.in.isdh.inwic 2 reviews"/>
</p>

> It just messes up for no reason<br> :date: __2020-07-13 14:46:53__

> Nothing but problems.. half the time I can't see my benifits<br> :date: __2020-06-23 15:08:58__

> Everytime I log on..and onto my benefits its telling there is and error and keeps me back out to the long in screen...I cant even tell what I have left!<br> :date: __2020-06-23 01:35:57__

> Doesnt want to work half the time<br> :date: __2020-06-22 21:08:16__

> I deleted the app like the message said and its still saying expired :/<br> :date: __2020-06-17 18:54:37__

> Keeps crashing on me :(<br> :date: __2020-06-17 05:04:01__

> Since the most recent update i can log in but cant do anything else. Frustrated!<br> :date: __2020-06-16 14:16:25__

> The app is letting me longin but wont let me see my benifts it started after i updated it<br> :date: __2020-06-15 16:27:15__

> It never wants to open or login for me. It just closes the app entirely. I've tried to uninstall it and reinstall it still does this.<br> :date: __2020-02-19 14:28:11__

> was great when it worked but now EVERY TIME I try to log in it crashes. I have unloaded and reloaded it onto other devices with the same damn problem. obviously I'm not the only one having an issue with it..... so why not fix it already?! it's been going on for MONTHS no matter how many times I send a report.<br> :date: __2020-01-09 20:27:03__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.in.isdh.inwic 1 reviews"/>
</p>

> Keeps telling me my session timed out<br> :date: __2020-08-01 16:02:38__

> This app doesn't seem to work anymore! I've uninstalled and reinstalled twice and still get the message that it's still in development and I don't have access.<br> :date: __2020-07-14 14:03:32__

> I can't login to my account since the last upgrade. It just goes gray after I put in my info and doesn't do anything.<br> :date: __2020-07-13 22:40:15__

> Suddenly not working..<br> :date: __2020-07-08 02:23:11__

> They update the app one time and the whole thing starts malfunctioning. Ima need you to get it together<br> :date: __2020-07-07 20:51:35__

> Won't let me sign in<br> :date: __2020-07-04 08:42:22__

> I'm giving 0 stars... Don't know what happened with the update but I've uninstalled and reinstalled multiple times and keep getting an error about the app being in development stage and to call my local office for help.<br> :date: __2020-07-03 16:53:34__

> Really bad can get nothing done.<br> :date: __2020-07-01 01:25:10__

> Every time Iog on it says session expired and closes out the app. I cant check my appt times or benefits due to this. Its never worked for me.<br> :date: __2020-06-30 20:09:41__

> App logs me out immediately after logging in. Can't see anything on it.<br> :date: __2020-06-30 18:50:46__


