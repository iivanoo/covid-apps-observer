# MI COVID Alert
App version ``1.0``

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
| **Latest version** | 1.0 |
| **Last update** | 2020-10-13 19:20:41 |
| **Recent changes** | Initial release of MI COVID Alert, the Michigan Department of Health and Human Services Exposure Notifications app. |
| **Installs**  | 1,000+ |
| **Category** | Health & Fitness |
| **First release** | Oct 9, 2020 |
| **Size**  | 2.9M |
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

The MI COVID Alert app has been installed by more than **1000** times. At this time, **24** rated the app and its average score is **4.5833335**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 20

:star::star::star::star:: 2

:star::star::star:: 0

:star::star:: 0

:star:: 2

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="gov.michigan.MiCovidExposure 5 reviews"/>
</p>

> Everybody should get this app so all of us can be safe and healthy so please use the app<br> :date: __2020-12-26 00:59:02__

> Just use the app<br> :date: __2020-12-24 07:21:40__

> Excellent app, easy to understand, I recommend it. I think it is a good idea. (By the way, no Covid-19 here).<br> :date: __2020-12-24 02:27:46__

> GREAT!!!!!!!<br> :date: __2020-12-21 19:27:07__

> Seems to do the basic job it's supposed to do.<br> :date: __2020-12-19 21:35:16__

> They let YOU KNOW exactily what is what about this chinese epidemic-19.<br> :date: __2020-12-13 02:49:59__

> Feel safer<br> :date: __2020-12-11 04:10:05__

> Nice to know of the Corona<br> :date: __2020-12-10 20:00:17__

> All negative reviews seem to speak about the lack of participation by the public. Instead of rating the app poorly, how about we take a moment to engage our family and friends, educate them about this app, and encourage them to use it. It will never be perfect but it is the best contact tracing solution available at this time.<br> :date: __2020-12-10 17:13:52__

> Really simple, if it saves one person it was worth it. It will probably save more! Great job, and I'm glad the racial bias data is available too. Good job Gretchen/All!<br> :date: __2020-12-09 04:46:36__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="gov.michigan.MiCovidExposure 4 reviews"/>
</p>

> I give it 4 stars needs improvement . but still great app.<br> :date: __2020-12-22 15:38:23__

> For the first ten days I had this installed Exposures were checked 2 - 3 times each day. As of this review, the last time Exposures were checked was four days ago. I've verified all settings on the phone as directed by the app. I've force stopped and restarted the app. Nothing seems to get it to begin checking exposures again. If not checking for exposures, what is the purpose of the app? Update:. Oddly shortly after posting the above, the app started updating exposures at least twice daily.<br> :date: __2020-12-16 23:05:53__

> I will if it ever downloads, still pending After 5 Minutes, tried again a few days later and it downloaded right away<br> :date: __2020-12-04 05:11:59__

> Sits quietly in the background doing it's thing with no battery degradation. Like to see a tab to show vaccination verification because eventually schools, businesses, concerts, theaters, airlines, etc will want to see proof of vaccination.<br> :date: __2020-12-02 02:55:30__

> So far I havent seen anything about exposures. It would be good if they told me how my county and town is doing.<br> :date: __2020-11-26 16:31:22__

> I installed it to do my part. I'll uninstall it once this pandemic passes. That's freedom.<br> :date: __2020-11-21 18:55:35__

> I'm glad to have this, but the map doesn't work correctly. When I tap on a county, it just shows a blank page.<br> :date: __2020-11-21 16:50:48__

> Just checking it out<br> :date: __2020-11-20 08:58:10__

> Way to late and unlikely to work universally (eg. with folks from out of state) but it's better than the nothing burger we've had so far. Would be nice if it gave you an idea of how many contacts it recorded (Inna privacy preserving way) to let us know the adoption rate around us.<br> :date: __2020-11-17 03:59:58__

> Its a good way to b notifield about the virus<br> :date: __2020-11-14 23:32:03__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="gov.michigan.MiCovidExposure 3 reviews"/>
</p>

> It only works if everyone has the app installed, and most do not. Unless this is mandated the app is pretty much useless. I will keep it for now in case more people use it.<br> :date: __2020-12-10 11:42:53__

> Just checked into this app today (12/9). Last exposure check was 11/18. Something is broken it seems. Really want this to work.<br> :date: __2020-12-09 13:35:36__

> Very confusing.......<br> :date: __2020-11-29 00:19:29__

> On the page "Michigan Coronavirus Stats" 2/3 of the page is covered with text about John Hopkins. To scroll the important information there is only a 1 inch window.<br> :date: __2020-11-19 14:59:18__

> Nice start, but it's deceptive giving static statistics. Need to do update stats daily or remove them!<br> :date: __2020-11-15 17:48:11__

> The county health department is so overwhelmed I likely won't be contacted to get the pin # to put in my positive test. I can have no clear idea of how effective the app is, but it's better than nothing<br> :date: __2020-11-15 14:33:26__

> Great idea<br> :date: __2020-11-15 00:39:09__

> I think the concept of this app is a step in flattening the curve but unless all Michiganders are downloading and using this how is its effectivenes Therefore, I think requirement of the app by all with smart phones or access might make it more successful, not only Michigan but throughout the United States. Matter of fact Everywhere this is a "Global Pandemic". Pre-installment (as other widely used apps are already installed on new phones) is a good idea as well. Please Consider<br> :date: __2020-11-14 19:46:35__

> Being able to see a how many people in your area have downloaded the app would be helpful. Its far more accurate if my city has 5k+ downloads than if it only has 500.<br> :date: __2020-11-14 17:53:39__

> I am a nurse and have tested positive in April. No pin given. Won't let me submit my result<br> :date: __2020-11-14 09:22:03__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="gov.michigan.MiCovidExposure 2 reviews"/>
</p>

> Why isn't there a Caucasian stat on the racial breakdown...?<br> :date: __2020-12-18 23:00:36__

> This app is general , can be improved to reflect local zip codes with real time case tracking. Racial distribution makes this app racist.<br> :date: __2020-12-16 16:58:27__

> I've been in direct contact with 3 people who have tested positive. This app didn't notify me if a single thing. Seems pointless.<br> :date: __2020-12-05 19:14:18__

> Seems like a good idea, I'm not in a major city and don't work around large amounts of people so not sure how effective it will be for me. One thing it did I don't get since it says it uses bluetooth and won't ask for GPS, is it required me to have my GPS on to receive notifications! "Exposure notification inactive" this is what it tells me unless my GPS is on. "To use turn on location."<br> :date: __2020-12-04 23:34:03__

> This has not checked for 4days<br> :date: __2020-11-24 22:28:57__

> Great idea & much needed. However... requires keeping your Location & Bluetooth ON constantly, in order to function. And that's a MASSIVE suck for the battery power on most phones. Devs need to change that, somehow! Until then, I'm uninstalling this app.<br> :date: __2020-11-23 00:53:19__

> Why are only 3 ethnic groups shown in the Statewide Racial Breakdown? The groups shown are Black/African American, Hispanic/Latino, and Native American/Alaskan Native. What about Asians? Middle Eastern? Michigan is made up of more than 3 ethnic groups and whites.<br> :date: __2020-11-22 15:22:42__

> Would be nice if the Stats screen wasn't 80% ad for John Hopkins. Would like to see better view of the stats.<br> :date: __2020-11-19 15:35:54__

> Would not come in kept trying<br> :date: __2020-11-19 00:24:18__

> The main page with the stats has half the screen taken up with a banner crediting John Hopkins for the work. You can't minimize it and it hinders the usability of the app<br> :date: __2020-11-18 22:44:08__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="gov.michigan.MiCovidExposure 1 reviews"/>
</p>

> Can't see statistics. Causes issues with phone crashing, long lag, frequently disconnects wifi and 4g, random call noise. Do not install. Worthless<br> :date: __2020-12-24 07:32:10__

> App is a fraud does not alert you covid exposures.<br> :date: __2020-12-24 01:48:06__

> Never got id # to input. 3 pos. 🤷🏽‍♂️<br> :date: __2020-12-22 09:51:18__

> These need a way to see if anyone else even uses the app in your area. There should be an anonymous way to list number of users in your country or neighborhood or something. I'm not keeping it since there is zero way to tell if if would even work anyway. *Worthless dev response as per usual.<br> :date: __2020-12-21 18:58:20__

> A great idea if it actually worked...<br> :date: __2020-12-19 16:51:14__

> Needs help. I tried to report a Covid case and the app asks for a code. So I was not able to report on the system. In addition, I live in a very populated area and not one case, not one.<br> :date: __2020-12-17 13:14:04__

> Good idea, but doesn't work in practice. I got covid, and when I tried to send an alert, it required a key from the health department. Health dept contacted me about a week after my test, which was about a week after symptoms started... so there's 2 weeks right there. Health dept had me take a survey, and then never gave me a key to use for the app. Now I know why I never got any exposure alerts on it.<br> :date: __2020-12-16 21:02:57__

> I'm positive and can't record it. I've had my rapid results for 5 days and send out results for 3 days, but can't report anything without a code from the health department. Makes the app completely pointless. Update 12/15: I never got any call from the health department, so never got a PIN. The app specifically says they will call. If resources weren't available to keep up with issuing PINs, the app shouldn't have been released.<br> :date: __2020-12-15 23:26:10__

> Absolutely USELESS. I HAVE COVID and there has been ZERO effort by local or state bodies to issue me a PIN number to report my positive results to the app.<br> :date: __2020-12-14 23:14:10__

> The family next door (3 people) contracted covid. No noticafication.<br> :date: __2020-12-14 21:32:19__


