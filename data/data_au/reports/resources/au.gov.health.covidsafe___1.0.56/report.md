# COVIDSafe
App version ``1.0.56``

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
| **Latest version** | 1.0.56 |
| **Last update** | 2020-08-14 04:35:53 |
| **Recent changes** | Improved notifications.<br>The app now includes Turkish and Punjabi translations. |
| **Installs**  | 1,000,000+ |
| **Category** | Health & Fitness |
| **First release** | Apr 25, 2020 |
| **Size**  | 12M |
| **Supported Android version**  | 5.0 and up |

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
| **Declared target Android version**  | Pie, version 9 (API level 28) |
| **Effective target Android version**  | Pie, version 9 (API level 28) |
| **Minimum supported Android version**  | Lollipop, version 5.0 (API level 21) |
| **Maximum target Android version**  | - |

The larger the difference between the minimum and maximum supported Android versions, the better. A larger difference means a wider audience. For example, old phones have a very low Android version, so a high minimum supported Android version means that the app cannot be used by users with old phones, thus leading to accessibility problems. 

## Requested permissions

In the following we report the complete list of the permissions requested by the app. 

| **Permission** | **Protection level** | **Description** | 
|-------------------------|-------------------------|-------------------------|
 **android.permission<br>ACCESS_COARSE_LOCATION** | :warning:**Dangerous** | Allows an app to access approximate location. 
 **android.permission<br>ACCESS_NETWORK_STATE** | Normal | Allows applications to access information about networks. 
 **android.permission<br>BLUETOOTH** | Normal | Allows applications to connect to paired bluetooth devices. 
 **android.permission<br>BLUETOOTH_ADMIN** | Normal | Allows applications to discover and pair bluetooth devices. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>REQUEST_IGNORE_BATTERY_OPTIMIZATIONS** | Normal | Permission an application must hold in order to use Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 
 **com.google.android.c2dm.permission<br>RECEIVE** | - | - 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | stackoverflow.com | Stack Exchange, Inc. | :us: US | 2003-12-26 19:18:07 |
 | googleapis.com | Google LLC | :us: US | 2005-01-25 17:52:26 |


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

The COVIDSafe app has been installed by more than **1000000** times. At this time, **12939** rated the app and its average score is **2.7324052**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 3932

:star::star::star::star:: 870

:star::star::star:: 1280

:star::star:: 1511

:star:: 5343

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 5 reviews"/>
</p>

> It's great<br> :date: __2020-09-15 12:08:40__

> S,<br> :date: __2020-09-13 03:55:20__

> Need more people to download so it's useful<br> :date: __2020-09-11 22:29:48__

> Does its job.<br> :date: __2020-09-10 00:01:38__

> It's amazing<br> :date: __2020-09-09 22:20:03__

> Easy to instal Hope it works<br> :date: __2020-09-09 00:31:12__

> No notification so far. I need to uninstall to get function and readings from iHealth heart monitor a few times a week. Then reinstall COVIDSafe app. Any solutions less onerous? Nola<br> :date: __2020-09-08 09:49:21__

> I feel safe and protected<br> :date: __2020-09-07 02:08:59__

> Good.<br> :date: __2020-09-06 15:13:58__

> Good<br> :date: __2020-09-06 13:30:36__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 4 reviews"/>
</p>

> Had no troubles, works ok from day1 of release. Now i find out the phone app had battery optimization enabled which prevents app from running correctly. Uninstalled + reloaded as i thought app was the issue. Then used PC and Google to locate how to ensure no optimization on the app. I only turn bluetooth on when i leave home. So no battery issues.<br> :date: __2020-09-06 14:33:07__

> I hope its just me. Sometimes randomly I have to briefly turn bluetooth off, to get mt wifi to work again. Then I forget to reactivate bluetooth. Android phone. There is nowhere on the covidsafe website to put technical feedback. No feedback is not really good for quality control. How will you know if its working, until you need it and then its too late.<br> :date: __2020-09-04 01:30:28__

> To all you one star raters, when all else fails, RTFM. For the benefit of the uneducated, that means Read the instructions!! At 18:03 on 26/4/20 activation worked perfectly. To the nay-sayers, stop trying to show the world how stupid, selfish and self-centred some Australians can be.<br> :date: __2020-09-01 13:41:00__

> Great initiative.<br> :date: __2020-08-27 06:29:57__

> Updated today but unsure if notifications sound comes on because I've just turned it on or because I have been exposed to the SARS COV 2! Also, I was not notified of recent update!<br> :date: __2020-08-21 05:08:51__

> Hope it works.<br> :date: __2020-08-21 04:36:40__

> Free anti virus software, I guess. BUT you may need to visit the play store to update it directly, as it seems resistant to auto updates.<br> :date: __2020-08-19 09:57:59__

> When it works that is.. 😁<br> :date: __2020-08-17 04:46:39__

> A useful app that causes slightly more battery usage but anything that helps to contact trace people potentially affected by the Chinese Communist Party Virus (CCP Virus), is worth having as an additional tool to help fight this Chinese biological weapon. If any good that came from this CCP Virus is that it revealed China's true colours & is helping the rest of the world in unititing in worldwide retribution against the CCP. Hopefully this brings a demise to this brutal and authoritarian regime.<br> :date: __2020-08-10 07:06:18__

> Had to delete cache & data & reregister after update, otherwise it crashes constantly<br> :date: __2020-08-10 06:54:42__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 3 reviews"/>
</p>

> No phone or battery issues on my samsung a5. Would like to see time shortened from 15 minutes to 1 or 2 minutes and warn me when I'm close to someone would be much better so I can move away. Otherwise it's fine. Can't see the point of having it if it waits 15 minutes to say I've been close to someone that's not good.<br> :date: __2020-09-14 00:47:04__

> A,s<br> :date: __2020-09-13 08:18:43__

> I have the internet connection. Covid app says no connection.???<br> :date: __2020-09-10 05:19:39__

> Okay dont mind it<br> :date: __2020-08-29 12:30:32__

> This app needs location *permission* because Bluetooth can be used to locate us. It doesn't need our location though. It should not require location services to be enabled.<br> :date: __2020-08-28 17:00:11__

> This app needs to work with battery optimisation on, I get better battery life with battery optimisation on, I don't want to charge my phone every 12 hours which seems to be with this app active in background. Please fix<br> :date: __2020-08-28 07:14:20__

> When it works properly!<br> :date: __2020-08-28 04:59:06__

> Update on the 23/08 (Version number 1.0.56) is warning me "No internet connection" when my phone is connected to the internet. Tapping the warning takes me to a message on why it needs the internet with a back arrow.<br> :date: __2020-08-23 04:21:40__

> I get why people would be unhappy about the app draining phone batteries. The idea is great... but its bypassing a lot of precautions and restrictions to stay awake and pull bluetooth information (polling), and agressive pinned notifications tend to be the most annoying type. Phone OS updates should help reduce wakelocks Other than that, it doesn't do much beyond tracking bluetooth IDs, like WiFi names, your phone/SIM network has your geo location, google/apple do too. Theyre beyond invasive.<br> :date: __2020-08-22 06:16:41__

> Can i download the covidsafe app on a tablet<br> :date: __2020-08-15 08:03:45__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 2 reviews"/>
</p>

> This was a disappointment. We are a not for profit, volunteer organisation. We had a 2 day event. And needed to manage venue numbers. Many volunteers circulated through various roles. But the App only allows a total of 3. Pricing is not transparent. I could not find cost of the Emterprise version anywhere. Contacting the company revealed they wanted $1000 for the upgrade. We used pencil and paper to manage our event.<br> :date: __2020-09-14 01:49:20__

> Yes it installs on 5.1 now but gets stuck after enabling Bluetooth. Proceed does not enable battery optimisation off and Bluetooth location. Oppo R7+ with ColorOs. The new version starts bu reports not connected to internet while the phone is connected to internet. App 'report problem' fails. Is it of any use without Internet?<br> :date: __2020-09-11 02:49:34__

> The app is causing my Bluetooth headphones to stutter :(<br> :date: __2020-09-09 13:20:22__

> No support. Bluetooth weirdness = lost connectivity. Oh well. Nice idea. Uninstalled.<br> :date: __2020-09-08 14:16:41__

> Uninstall because it cause problems with bluetooth conectons.<br> :date: __2020-09-06 09:28:07__

> 5/9/20 update: for a few weeks been thinking my Bluetooth speakers were broken . Then I realised its the covid safe app using the Bluetooth interfering with the signal. Uninstalled the covid safe app and speakers working fine again. I pay $12 a month for spotify and not going to have the covid safe app ruin my music streaming. Would be good if I could turn the covid safe app off when at home and still have Bluetooth on for my speakers. Let me know if I can as I have uninstalled the app.<br> :date: __2020-09-05 10:33:15__

> Don't know. I don't use it.<br> :date: __2020-09-05 01:15:21__

> Glitchy<br> :date: __2020-09-04 10:12:54__

> Great idea, terrible implementation. Interferes with Bluetooth streaming, which is frustrating on the train ride home. Needs to be fixed if you want this to be a genuine tool to help contact tracers.<br> :date: __2020-09-03 09:46:50__

> I really don't know what's use of this apps except eating so much battery juice on my phone.<br> :date: __2020-09-03 03:36:21__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="au.gov.health.covidsafe 1 reviews"/>
</p>

> @CovidSafeapp has issues, it keeps disconnecting my beats bluetooth headphones sound while watching videos. On uninstalling app theu work fine. Same issue on my wife's phone with bose headphones. It keeps disconnecting on my samsung note 9. Please fix<br> :date: __2020-09-15 12:46:46__

> 2 million downloads out of around 27 million people in Australia. Bahahahahahah we now know which idiots vote LNP or are involved in a panicdemic. Welcome privileged fools to the world you gave others for decades. Thanks for the plebescite breeders...enjoy Covid-19!! The great equaliser forcing the privileged to pretend to care! Uninstalling and hope you fools realise you should never trust a government who let the virus in. Plebiscite, bushfires, covid 19 what more proof do you need idiots!!!!<br> :date: __2020-09-15 00:20:55__

> this app doesn't alert you to close contact with other registered confirmed covid case's one of my friends went shopping and he was waiting in line at the checkout. A man behind him coughed on him! later that same guy said he had covid and was registered with this app but thought he was fine to go shopping! At Woolworths Gosford Imperial Centre Gosford NSW Australia 2250 Friday 11th September between 9am and 10am<br> :date: __2020-09-13 13:36:05__

> Loaded the app, got charged in excess of $100 extra data charges when I have a 500GB plan. Deleted the app, the extra charges stopped happening. So furious.<br> :date: __2020-09-13 06:25:15__

> Kills your battery and it doesn't do much<br> :date: __2020-09-13 03:22:10__

> Followed instructions on the website, still does not allow me to receive the PIN, keeps saying "try again later"<br> :date: __2020-09-13 02:23:37__

> Cannot register - get pin????<br> :date: __2020-09-12 10:26:25__

> Pointless app. Hasn't done anything it claims, just drains battery power<br> :date: __2020-09-11 11:55:49__

> App reports green and working in status bar, but when I tap on the app status, it opens showing it's not working because either GPS or Bluetooth is turned off, and I did not turn either of these off. Confusing. Concerning more so because I discover this halfway through or after a day out!! If mine doesn't work reliably, does anyone else's? If it's not working reliably for everyone what's the protection level? I supported and pushed the concept of this app and still do. Get your act together!<br> :date: __2020-09-11 01:42:46__

> Everytime I open app I find out Covid Safe isn't functioning. Constantly have to give permission to battery parameters. I'm sick of draining my phone battery on such a useless app<br> :date: __2020-09-10 06:34:24__


