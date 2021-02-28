# MI COVID Alert
App version ``1.2``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="MI COVID Alert icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | MI COVID Alert |
| **Unique identifier** | gov.michigan.MiCovidExposure |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=gov.michigan.MiCovidExposure](https://play.google.com/store/apps/details?id=gov.michigan.MiCovidExposure) |
| **Summary**  | Michigan&#39;s COVID-19 Exposure Notification App |
| **Privacy policy** | [http://michigan.gov/micovidalertprivacy](http://michigan.gov/micovidalertprivacy) |
| **Latest version** | 1.2 |
| **Last update** | 2020-12-24 18:18:37 |
| **Recent changes** | Minor fixes |
| **Installs**  | 100,000+ |
| **Category** | Health & Fitness |
| **First release** | Oct 9, 2020 |
| **Size**  | 3.1M |
| **Supported Android version**  | 6.0 and up |

### Description
> MI COVID Alert is the COVID-19 exposure notification app supported by the Michigan Department of Health and Human Services (MDHHS), in partnership with SpringML, Google, and Apple. This app uses Bluetooth Low Energy (BLE) API framework created through a unique collaboration between Apple and Google.
<br>Your personal use of MI COVID Alert helps inform others of possible exposure to COVID-19 if they are suspected of having been within close proximity to someone who has tested positive. When you download MI COVID Alert, you are helping your community stay ahead of any potential surge in COVID-19 cases. 
<br>How MI COVID Alert Works:
<br>Once downloaded, users of the app who have enabled it will exchange anonymous Bluetooth “keys” (random alpha-numeric codes that represent a Bluetooth signal) with other MI COVID Alert users.
<br>If someone reports that they tested positive for COVID-19, the app will search for other users who shared the Bluetooth Low Energy (BLE) signal. The BLE signals are date-stamped and MI COVID Alert estimates how close the two devices were based on signal strength. If the timeframe was at least 15 minutes and the estimated distance was within six feet, then the other user receives a notification of a possible exposure. Names of users and locations of possible exposure are never tracked and never shared.
<br>The BLE framework within MI COVID Alert will run in the background, even if the exposure notification app is closed. It will not drain the device battery at a rate faster than other apps that use normal Bluetooth and/or are open and running continuously.
<br>How MI COVID Alert Protects Your Privacy:
<br>MDHHS takes your privacy very seriously. This is why we chose to use the Apple and Google BLE framework. No personal data or location tracking occurs within MI COVID Alert. 
<br>MDHHS and local public health staff follow up with persons who have a positive COVID-19 laboratory report. Public health will provide MI COVID Alert users with a validation pin. That validation pin must be entered into the app to report a notification of possible exposure to other users. This prevents people from falsely reporting positive results, which could generate false exposure notifications. 
<br>If you have the current Apple or Google operating system installed on your device, you may have noticed that Exposure Notifications are now included. You cannot enable this function until you have downloaded MI COVID Alert. Apple and Google will delete the exposure notification service tools from their respective operating systems once the pandemic reaches a point that public health no longer requires the use of this technology.
<br>Thank you for downloading MI COVID Alert! Together, we can protect our family, friends, and communities.


### User interface
The developers of the app provide the following screenshots in the Google play store.
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
 | <img src="screenshot_1.png" alt="screenshot" width="300"/>  | <img src="screenshot_2.png" alt="screenshot" width="300"/>  | <img src="screenshot_3.png" alt="screenshot" width="300"/>  | 
 | <img src="screenshot_4.png" alt="screenshot" width="300"/> 

## Development team
In the following we report the main information provided by the development team in the Google play store.

| | |
|-------------------------|-------------------------|
| **Developer**  | State of Michigan |
| **Website**  | [http://www.michigan.gov/micovidalert](http://www.michigan.gov/micovidalert) |
| **Email** | mdhhs-micovidalert@michigan.gov |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=State+of+Michigan](https://play.google.com/store/apps/developer?id=State+of+Michigan) |

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
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | jhu.edu | Johns Hopkins University | - | 1987-03-19 00:00:00 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Telephony identifiers leakage**
> - This application reads the ISO country code equivalent of the current registered operator's MCC (Mobile Country Code)<br>

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The MI COVID Alert app has been installed by more than **100000** times. At this time, **392** rated the app and its average score is **3.2380953**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 176

:star::star::star::star:: 41

:star::star::star:: 15

:star::star:: 22

:star:: 138

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.michigan.MiCovidExposure 5 reviews"/>
</p>

> Keeps us up to date us Michiganders Stay safe everyone...<br> :date: __2021-02-26 13:44:15__

> Just use the app. Would be nice if it showed number of other app users it's "seen" though, then I could be sure it's working<br> :date: __2021-02-17 14:13:30__

> App wasn't updating at all but the developer contacted me and the fix he gave me worked!!! Now it updates every day<br> :date: __2021-02-06 19:25:27__

> Way improved from its earlier design<br> :date: __2021-02-03 03:53:22__

> Covid 19b is almost gone.<br> :date: __2021-01-31 02:51:04__

> Really do appreciate this app. I'm high risk and so is my husband, staying on top of where this virus is and if we may have been in contact with it puts my mind at ease.<br> :date: __2021-01-26 20:14:09__

> Started updating after reinstall. Turned on power management exception. Seems to be working again. Developer responds quickly. Edit: Hasn't checked exposure since 1/4/21. Seems stuck. Checked google exposure over past 14 days. Contained no data. Wish there was a way to force a check/notification update. Reinstalled. Still not updating Original: Low battery consumption. Exceptional privacy. No location tracking. Low data use. Not invasive.<br> :date: __2021-01-26 17:00:11__

> Very relieved i have this & have shared it<br> :date: __2021-01-24 05:38:44__

> clear all my control<br> :date: __2021-01-20 08:51:04__

> I know the privacy concerns, but I feel my health and the health of the people around me matter more.<br> :date: __2021-01-18 18:05:55__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.michigan.MiCovidExposure 4 reviews"/>
</p>

> Ok<br> :date: __2021-02-03 15:23:08__

> Stopped notifying me/updating alerts. Uninstalled app then reinstalled it. Alerts commenced once agai Have had first vaccine on 9th of January.<br> :date: __2021-01-22 19:08:14__

> I give it 4 stars needs improvement . but still great app.<br> :date: __2020-12-22 15:38:23__

> For the first ten days I had this installed Exposures were checked 2 - 3 times each day. As of this review, the last time Exposures were checked was four days ago. I've verified all settings on the phone as directed by the app. I've force stopped and restarted the app. Nothing seems to get it to begin checking exposures again. If not checking for exposures, what is the purpose of the app? Update:. Oddly shortly after posting the above, the app started updating exposures at least twice daily.<br> :date: __2020-12-16 23:05:53__

> I will if it ever downloads, still pending After 5 Minutes, tried again a few days later and it downloaded right away<br> :date: __2020-12-04 05:11:59__

> Sits quietly in the background doing it's thing with no battery degradation. Like to see a tab to show vaccination verification because eventually schools, businesses, concerts, theaters, airlines, etc will want to see proof of vaccination.<br> :date: __2020-12-02 02:55:30__

> So far I havent seen anything about exposures. It would be good if they told me how my county and town is doing.<br> :date: __2020-11-26 16:31:22__

> I installed it to do my part. I'll uninstall it once this pandemic passes. That's freedom.<br> :date: __2020-11-21 18:55:35__

> I'm glad to have this, but the map doesn't work correctly. When I tap on a county, it just shows a blank page.<br> :date: __2020-11-21 16:50:48__

> Just checking it out<br> :date: __2020-11-20 08:58:10__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.michigan.MiCovidExposure 3 reviews"/>
</p>

> Used to work but now it hasn't checked for exposure since Feb 13th. It's up to date, I've uninstalled and reinstalled, phone restart, checked permissions. Nothing has worked. I'm uninstalling because it's not worth the waste of space.<br> :date: __2021-02-27 02:06:51__

> This app is general , can be improved to reflect local zip codes with real time case tracking. Racial distribution makes this app racist.<br> :date: __2021-02-09 03:41:17__

> L pi pl om 0<br> :date: __2021-02-03 15:23:00__

> Old information<br> :date: __2021-01-26 12:54:59__

> Might work but having to call in to get a PIN is way too much effort. Literally nobody has time for that<br> :date: __2021-01-21 17:15:25__

> How do you update?..hasn't worked since the 17 Jan 2021.<br> :date: __2021-01-21 13:03:49__

> No notifications??? I worked in a hospital filled with COVID patients during an outbreak. Maybe none of them had this app installed. This app is an amazing concept. I apperciate the anonymity. I will continue to recommend this app to others!<br> :date: __2021-01-14 13:15:04__

> It was working fine updating regularly. Now it hasn't updated my exposure or the cases and deaths since January 4th. I don't know what is wrong. Yes my bluetooth is on. I don't know what to do with it.<br> :date: __2021-01-13 17:51:43__

> My app last exposure check was Dec 30 2020. I have my location and Bluetooth on. Not working..<br> :date: __2021-01-09 12:23:32__

> It only works if everyone has the app installed, and most do not. Unless this is mandated the app is pretty much useless. I will keep it for now in case more people use it.<br> :date: __2020-12-10 11:42:53__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.michigan.MiCovidExposure 2 reviews"/>
</p>

> Doesn't update cases counts and deaths data<br> :date: __2021-02-22 19:53:15__

> Does not update<br> :date: __2021-02-14 13:28:30__

> The app does NOT update as it should! It unexpectedly will stop and the only alternative is to delete it and then reinstall it. I have done this 3x....<br> :date: __2021-01-19 14:05:19__

> Haven't had a logged exposure check since Dec 27 with no way to refresh.<br> :date: __2021-01-07 15:37:22__

> Why isn't there a Caucasian stat on the racial breakdown...?<br> :date: __2020-12-18 23:00:36__

> I've been in direct contact with 3 people who have tested positive. This app didn't notify me if a single thing. Seems pointless.<br> :date: __2020-12-05 19:14:18__

> Seems like a good idea, I'm not in a major city and don't work around large amounts of people so not sure how effective it will be for me. One thing it did I don't get since it says it uses bluetooth and won't ask for GPS, is it required me to have my GPS on to receive notifications! "Exposure notification inactive" this is what it tells me unless my GPS is on. "To use turn on location."<br> :date: __2020-12-04 23:34:03__

> This has not checked for 4days<br> :date: __2020-11-24 22:28:57__

> Great idea & much needed. However... requires keeping your Location & Bluetooth ON constantly, in order to function. And that's a MASSIVE suck for the battery power on most phones. Devs need to change that, somehow! Until then, I'm uninstalling this app.<br> :date: __2020-11-23 00:53:19__

> Why are only 3 ethnic groups shown in the Statewide Racial Breakdown? The groups shown are Black/African American, Hispanic/Latino, and Native American/Alaskan Native. What about Asians? Middle Eastern? Michigan is made up of more than 3 ethnic groups and whites.<br> :date: __2020-11-22 15:22:42__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.michigan.MiCovidExposure 1 reviews"/>
</p>

> Has not checked exposure since last update.<br> :date: __2021-02-26 22:09:59__

> Today is 2/24, the last scan was on 1/24. Leave it to the government to create a useless app.<br> :date: __2021-02-23 22:51:20__

> I checked the app and the last update was 12 days ago. What good is that? I did make sure that the app is not sleeping in settings<br> :date: __2021-02-22 01:02:13__

> The app doesn't seem to be very functional. Initially it was updating possible exposure or lack thereof on a daily basis then it stopped updating. I actually uninstalled and reinstalled the, like the first installation, it updated daily for s few days and then stopped updating.<br> :date: __2021-02-20 20:00:10__

> Does not work<br> :date: __2021-02-20 19:37:39__

> Works for a few days then stops. It says it's on but no readings for two weeks. Reloaded twice. Still don't work right.<br> :date: __2021-02-20 03:13:41__

> Well, I had Covid, and it didn't show me or the people who live here. I had to report to Midland, Gratiot, and Isabella counties.. Guess what? I uninstalled really fast. Edit: I had to report in three counties, because I live, work, and kids go to school in all three. Of course I reported, but it still didn't show up in the App.<br> :date: __2021-02-19 17:17:08__

> Unfortunately this app is not very useful. I was not even able to enter that I had COVID to alert anyone. It requires a number from the health department who never contacted me. I tried to go on their site to contact someone but never got a response. I was so frustrated I couldn’t use it to alert people. It’s a great idea but in my case felt Totally pointless<br> :date: __2021-02-17 18:40:31__

> Like others I think it is pointless if it doesn't check exposures for more than a month. And seeing the lazy copy and paste response to concerns by the developer makes it even worse because it shows lack of concern. Just stop making excuses and telling users to go to some website that won't change anything and improve your app. It's not the phone manufacturer's fault your app sucks.<br> :date: __2021-02-14 14:35:44__

> I checked all the things suggested in previous review replies and it still doesn't update. Not helpful if no manual check option.<br> :date: __2021-02-14 04:56:52__


