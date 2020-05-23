# COVIDSafe
App version ``1.0.17``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="COVIDSafe icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | COVIDSafe |
| **Unique identifier** | au.gov.health.covidsafe |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=au.gov.health.covidsafe](https://play.google.com/store/apps/details?id=au.gov.health.covidsafe) |
| **Summary**  | COVIDSafe is a community-based way to stop the spread of COVID-19. |
| **Privacy policy** | [https://www.health.gov.au/using-our-websites/privacy](https://www.health.gov.au/using-our-websites/privacy) |
| **Latest version** | 1.0.17 |
| **Last update** | 2020-05-13 13:50:12 |
| **Recent changes** | Push notifications are now optional<br>Improvements to Bluetooth security and connectivity<br>Accessibility enhancements<br>Bug fixes. |
| **Installs**  | 1,000,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 25, 2020 |
| **Size**  | 6.0M |
| **Supported Android version**  | 6.0 and up |

### Description
> COVIDSafe app has been developed by the Australian Government Department of Health to help keep the community safe from coronavirus (COVID-19). Together, let’s help stop the spread and keep ourselves and each other healthy.
<br>COVIDSafe uses the Bluetooth® technology on your mobile phone to look for other devices with COVIDSafe installed. Your device will take a note of contact you’ve had with other users by securely logging the other user’s reference code. If you or someone you’ve been in contact with is diagnosed with COVID-19, the close contact information securely stored in your phone can be uploaded and used—with your consent—by state and territory health officials to quickly inform people who’ve been exposed to the virus.
<br>How you can help stop the spread of COVID-19:
<br>• Download the COVIDSafe app
<br>• Register using your mobile phone number, name, age range and postcode
<br>• Turn on Bluetooth®
<br>• Check that COVIDSafe is running when you are out and about or are likely to come into contact with others
<br>• If you test positive for COVID-19, you can consent for your close contact information to be used by state and territory health officials to contact people who may have been exposed. If you’ve been exposed to the virus by someone you’ve been in close contact with, state and territory health officials will be able to contact you quickly so you can get the support you need
<br>COVIDSafe is an Australian Government Department of Health initiative. Visit https://www.health.gov.au/resources/apps-and-tools/covidsafe-app for more information.


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
| **Developer**  | Australian Department of Health |
| **Website**  | [https://www.health.gov.au/resources/apps-and-tools/covidsafe-app](https://www.health.gov.au/resources/apps-and-tools/covidsafe-app) |
| **Email** | support@COVIDSafe.gov.au |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Australian+Department+of+Health](https://play.google.com/store/apps/developer?id=Australian+Department+of+Health) |

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
 **android.permission<br>ACCESS_FINE_LOCATION** | :warning:**Dangerous** | Allows an app to access precise location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>BLUETOOTH_ADMIN** | Normal | Allows applications to discover and pair bluetooth devices. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>REQUEST_IGNORE_BATTERY_OPTIMIZATIONS** | Normal | Permission an application must hold in order to use Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | stackoverflow.com | Stack Exchange, Inc. | :us: US | 2003-12-26 19:18:07 |
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |


## Security analysis 

Below we report the main security warnings raised by our execution of the [Androwarn](https://github.com/maaaaz/androwarn) security analysis tool.

**Connection interfaces exfiltration**
> - This application reads details about the currently active data network<br>
> - This application tries to find out if the currently active data network is metered<br>

**Suspicious connection establishment**
> - This application opens a Socket and connects it to the remote address ' returned no addresses for  ; port is out of range' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address '' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/lang/StringBuilder;->toString()Ljava/lang/String;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'Ljava/net/Proxy;->type()Ljava/net/Proxy$Type;' on the 'N/A' port <br>
> - This application opens a Socket and connects it to the remote address 'timeout' on the 'N/A' port <br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The COVIDSafe app has been installed by more than **1000000** times. At this time, **10587** rated the app and its average score is **3.6536632**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 5761

:star::star::star::star:: 926

:star::star::star:: 795

:star::star:: 674

:star:: 2427

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> The health and wellness of everyone is important<br> :date: __2020-05-17 15:10:07__

> I love it. It feels like having an added layer of protection when I go into Coles.<br> :date: __2020-05-17 14:46:47__

> Works well, stable, does not crash.<br> :date: __2020-05-17 13:39:56__

> App is rubbish. Phone number is invalid<br> :date: __2020-05-17 13:24:56__

> No problems with the app as far as I am concerned. Better to be safe than sorry.<br> :date: __2020-05-17 13:21:25__

> Lates version has battery usage issues thst earlier ddn't. It would appear that the app only needs Location permission, with Location turned off the app works. Earlier: I would like to contribute but I never have Location on so will not use this app.<br> :date: __2020-05-17 10:43:44__

> S10 5G App doesn't appear to have any impact on performance or security. Your irresponsible if it's not installed!<br> :date: __2020-05-17 02:55:25__

> Great<br> :date: __2020-05-17 02:46:06__

> Those Google accounts that had initially been setup from overseas are not able to download the app, though the users are located here in Australia. Please remove the restrictions.<br> :date: __2020-05-17 01:07:05__

> Exceptional user interface. No bugs. Very slick work<br> :date: __2020-05-16 15:47:36__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> Great idea and service, execution not so good. My battery on a Samsung S10+ only lasts now to about 5pm (9 hrs) whereas it usually would last double that. I've installed the update today and will test again. /Update/ since updating to the newer release the battery is not badly affected. Increased to 4 stars.<br> :date: __2020-05-17 15:02:46__

> Don't know yet.<br> :date: __2020-05-17 03:18:24__

> A great concept but it needs all of us to use it to help keep us all safe. Note oppo users will need to lock the app so the phone doesn't close it down. To do that, start the app, tap the square menu thing at the bottom of your phone, swipe the app down (you should then see a padlock at the top left of the app screen).<br> :date: __2020-05-17 02:04:26__

> Edit - Seems fixed in latest update. Causes my Sony Xperia Xa2 to blank screen during a call, making it impossible to hang up the call.<br> :date: __2020-05-16 06:05:31__

> I find the app places significant drain on my battery. I'm using a Samsung s7<br> :date: __2020-05-15 12:23:47__

> Good<br> :date: __2020-05-15 08:00:09__

> Update. Finally able to register the next day. Jan still not happy. . You'd think they would of had the app bug checked by now. Considering the amount of time they have been talking about it. Not happy Jan...! So, I am a Muppet and an inpatient Troll! It now after 6pm and it still won't except my phone number. I have un installed, and re installed. It is still a bug ridden 1 star because I can't give it a ZERO..<br> :date: __2020-05-15 04:43:58__

> Kept disconnecting blue tooth.<br> :date: __2020-05-15 00:24:56__

> Presumably working quietly in the background. Pleasing that the source code has been made available. A persistent, slightly irritating and presumptuous "keeping you safe" badge cannot be easily hidden but at least will remind me to delete the app when/if the need is passed.<br> :date: __2020-05-14 15:09:16__

> Does the app need to take up space in my notifications? To me that's a bit like the kid who cried wolf. Please just give me notifications that matter not a constant space waster at the top of the screen.<br> :date: __2020-05-14 14:07:58__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> Have son with diabetes so installed but it is a battery hog. Disable bluetooth while at home. Battery usage showed 47% usage was by this app while all other apps negligable.<br> :date: __2020-05-17 11:10:32__

> We'll see...<br> :date: __2020-05-17 09:18:10__

> Severely disrupts my Bluetooth connection with speakers, headphones, etc. So when I'm playing music on my phone and the app is active, the music skips.<br> :date: __2020-05-17 06:44:08__

> I don't mind the app but I don't understand wire displays how many minutes and the time when I pull down my home screen and it's running in the background what do the minutes mean? Eg: covidsafe 12m ??<br> :date: __2020-05-16 16:03:40__

> I wish it would remind me to enable Bluetooth when I leave the house. I ussually turn of Bluetooth to save battery.<br> :date: __2020-05-16 15:04:09__

> App switches itself off! Need to continually monitor the optimisation battery section and switch on for it to function!!!!<br> :date: __2020-05-16 11:42:11__

> It seems as though my battery runs flat quicker than usual since installing, and my screen is always warm.<br> :date: __2020-05-15 20:57:45__

> The app is still saying it is not active unless notifications are allowed despite the app updated claiming this is no longer the case<br> :date: __2020-05-15 16:20:15__

> Battery optimisation option constantly flagging every time the app opens regardless of how many times I select allow.<br> :date: __2020-05-15 09:56:35__

> Happy to run it, but the permanent notification display is annoying. Turning notifications off thru app manager disables the app... Would be good to have an option to turn off the notification icon.<br> :date: __2020-05-15 09:41:36__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> re<br> :date: __2020-05-17 06:26:37__

> The way it drains my battery is may as well be perminately plugged in<br> :date: __2020-05-17 04:24:22__

> Used up the battery from first use. After a week of charging the phone frequently it stopped working. Had no issues until downloading the app. Would not use it. It was not a new phone but worked. Drains battery on older phones.<br> :date: __2020-05-17 02:19:00__

> It wouldn't stay active. It always deactivates every time my phone goes on lock screen. I have to always activate it. I hope they fix it soon.<br> :date: __2020-05-17 00:00:51__

> The latest update (with the green Australia symbol) is chewing my battery at idle. It uses 10% per hour when my phone is idle. Was fine until the latest update. You need to fix this. UNINSTALLING.<br> :date: __2020-05-16 14:31:22__

> Initially didn't recognise my phone number, 5 attempts later accepted it. It then took 9 PIN requests because it never sent the PIN before the 5 minute time out.<br> :date: __2020-05-16 11:48:29__

> Always wants to set permissions when I've already set them.<br> :date: __2020-05-16 09:31:06__

> With the covid-safe installed there are constant interuptions to other devices also using Bluetooth. Uninstall covid-safe no problems. Would love to use this app but it is very hard to listen to interrupted music<br> :date: __2020-05-16 09:20:56__

> This keeps us safe, and the rating isn't about downloading the app. Rather, this apps negatively affects your phones functioning. 1) battery is drained at an insane pace!!! Full battery gone by noon (S10). 2) Bluetooth device disruption, both my buds and my UE Boom drop out often. Since uninstalling the app, both of these functions have returned to normal.<br> :date: __2020-05-16 01:35:17__

> Unsure of value of app until it's required but it's seriously detrimental to Bluetooth connectivity. Can't steadily stream music to my headphones etc, Can't connect my fitbit for exercise, Can't hotspot internet for my tablet. Poor effort really, if it was any other app, no one in their right mind would allow such a detrimental impact to the standard running of their phone.<br> :date: __2020-05-16 00:25:00__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> Says doesn't track you but requires location permission? For the app to work seems legit.<br> :date: __2020-05-17 14:40:30__

> It's a POS!!! won't stay on despite Bluetooth on & tracking app on in the background. , Yeh download the app they keep telling you, well fix it up and we will !!<br> :date: __2020-05-17 14:19:03__

> Big battery drain issues Samsung s10. Also had Bluetooth car connection problems. Would love to help but the app is causing big issues.<br> :date: __2020-05-17 12:50:32__

> A great idea but shame we have the morons out of touch with reality running the states and country! I had this installed but with restrictions continuing no point continuing with this app!<br> :date: __2020-05-17 12:31:47__

> Constantly turns itself off due to the battery optimize setting, making it pointless.<br> :date: __2020-05-17 10:06:53__

> took 4 attempts to install the app. the screen froze several times. Àfter installing this app, my mobile connection regularly dropped out. There is not much use to having a locator app if there is no mobile connection. So I uninstalled the app from my phone<br> :date: __2020-05-17 09:36:38__

> Useless app, my android phone is only 2 years old but still as soon as screen goes off the app deactivates and shuts down. Fix asap or will uninstall it's not working anyway. Typical government can't get a bloody app right that works for everyone. And they want you to download app, what a joke!!!!!<br> :date: __2020-05-17 09:11:47__

> My older Optus smartphone says CovidSAFE safe will be installed SOON but has said this for a week now yet it does NOT show in my list of apps on this phone yet confusing in another field days it is installed BUT IT IS NIT WIRKING<br> :date: __2020-05-17 06:44:45__

> Using bluetooth to track u is wrong your details including bank and other data u use on ur mobile can be stolen<br> :date: __2020-05-17 01:33:19__

> Boo I say! The CCP called, it wants its app back<br> :date: __2020-05-17 00:55:06__


