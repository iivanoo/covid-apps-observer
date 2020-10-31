# NHS COVID-19
App version ``3.9 (96)``

Analyzed with [covid-apps-observer](http://github.com/covid-apps-observer) project, version ``0.1``

<img src="icon.png" alt="NHS COVID-19 icon" width="80"/>

## App overview
| | |
|-------------------------|-------------------------| 
| **Name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | NHS COVID-19 |
| **Unique identifier** | uk.nhs.covid19.production |
| **Link to Google Play** | [https://play.google.com/store/apps/details?id=uk.nhs.covid19.production](https://play.google.com/store/apps/details?id=uk.nhs.covid19.production) |
| **Summary**  | Protect your loved ones with the NHS contact tracing app for England and Wales. |
| **Privacy policy** | [https://covid19.nhs.uk/our-policies.html](https://covid19.nhs.uk/our-policies.html) |
| **Latest version** | 3.9 (96) |
| **Last update** | 2020-10-27 21:23:16 |
| **Recent changes** | Feature enhancements to venue check-in, postal district alert, encounter detection and exposure notification and refined testing app logic as well as overall UI and accessibility optimisations. |
| **Installs**  | 5,000,000+ |
| **Category** | Medical |
| **First release** | Aug 12, 2020 |
| **Size**  | 8.0M |
| **Supported Android version**  | 6.0 and up |

### Description
> The new NHS COVID-19 app is the Official NHS contact tracing app for England and Wales. 
<br>It is the fastest way of knowing when you’re at risk from Coronavirus. The quicker you know, the quicker you can alert your loved ones, and your community. 
<br>The more of us that use it, the better we can control coronavirus. 
<br>The app runs on proven software developed by Apple and Google, designed so that nobody will know who or where you are. And you can delete your data, or the app, at any time.
<br>It has a number of features: 
<br>- Trace: Find out when you’ve been near other app users who have tested positive for coronavirus
<br>- Alert: Lets you know the level of coronavirus risk in your postcode district. 
<br>- Check-in: Get alerted if you have visited a venue where you may have come into contact with coronavirus, using a simple QR code scanner. No more form filling. 
<br>- Symptoms: Check if you have coronavirus symptoms and see if you need to order a test. 
<br>- Test: Helps you order a test if you need to.
<br>- Isolate: Keep track of your self-isolation countdown and access relevant advice.
<br>Available in English, Arabic (Modern Standard), Bengali, Chinese (Simplified), Gujarati, Polish, Punjabi (Gurmukhi script), Romanian, Somali, Turkish, Urdu and Welsh.
<br>The app has been built in collaboration with some of the most innovative organisations in the world. We have worked with medical experts, privacy groups, at-risk communities and we’ve shared knowledge with the teams working on similar apps in many countries.
<br>Protect your loved ones. Please download the app. 
<br>The App is CE marked as a class I medical device in the United Kingdom and developed in compliance with European Commission Directive 93/42/EEC for class I devices.


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
| **Developer**  | Department of Health and Social Care |
| **Website**  | [https://covid19.nhs.uk/](https://covid19.nhs.uk/) |
| **Email** | NHSCovid-19AppStoreSupport@nhsbsa.nhs.uk |
| **Physical address**  | - |
| **Other developed apps**  | [https://play.google.com/store/apps/developer?id=Department+of+Health+and+Social+Care](https://play.google.com/store/apps/developer?id=Department+of+Health+and+Social+Care) |

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
 **android.permission<br>CAMERA** | :warning:**Dangerous** | Required to be able to access the camera device. 
 **android.permission<br>FOREGROUND_SERVICE** | Normal | Allows a regular application to use Service.startForeground. 
 **android.permission<br>INTERNET** | Normal | Allows applications to open network sockets. 
 **android.permission<br>RECEIVE_BOOT_COMPLETED** | Normal | Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. 
 **android.permission<br>WAKE_LOCK** | Normal | Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 


## Mentioned servers

| **Server** | **Registrant** | **Registrant country** | **Creation date** | 
|-------------------------|-------------------------|-------------------------|-------------------------|
 | google.com | Google LLC | :us: US | 1997-09-15 04:00:00 |
 | ietf.org | IETF Trust | :us: US | 1995-03-11 05:00:00 |
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

**Code execution**
> - This application loads a native library<br>
> - This application loads a native library: 'Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;'<br>



## User ratings and reviews

Below we provide information about how end users are reacting to the app in terms of ratings and reviews in the Google Play store.

### Ratings

The NHS COVID-19 app has been installed by more than **5000000** times. At this time, **83764** rated the app and its average score is **4.071302**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 51213

:star::star::star::star:: 11919

:star::star::star:: 6784

:star::star:: 3091

:star:: 10757

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 5 reviews"/>
</p>

> easy to do the track and trace<br> :date: __2020-10-31 10:37:59__

> we must all do our bit People are DYING.<br> :date: __2020-10-31 09:07:58__

> I have not yet been notified from the app of anyone having covid. So either no one as it or no one else as the app or it doesn't work 🤔<br> :date: __2020-10-31 07:01:03__

> Very quick to download. Simple to use. Had lots of information on. And check in is easy to do. Thank you for keeping my family safe<br> :date: __2020-10-31 02:48:44__

> I like it It does what it say it does .I've never had a problem with it<br> :date: __2020-10-31 01:32:54__

> Very good<br> :date: __2020-10-31 00:57:20__

> this app is really good<br> :date: __2020-10-30 23:34:41__

> A Must for everyone<br> :date: __2020-10-30 23:15:00__

> Good App<br> :date: __2020-10-30 22:43:34__

> My app is turned on ,it was a connection problem with my server ,and l know how to turn it back on thank you for your help . I feel safe using this app .<br> :date: __2020-10-30 22:40:15__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 4 reviews"/>
</p>

> Thank you for this. Simple and helpful. One problem with notifications. This morning I had one about possible contact with someone who had tested positive. When I followed it, it took me into the app, where I couldn't find it. When I came out, there was another notification telling me I didn't need to worry - I was not affected. Again, following this took me into the app but I never found the full text because it had gone. This was more unsettling than helpful.<br> :date: __2020-10-31 10:49:26__

> Flagged up to self isolate after I'd just learnt someone I'd seen had tested positive so thought it was fairly accurate. Until I completed my self isolate, (did a test, showed negative), went back to work (left phone at home), then that eve I had another message saying I've been in contact and to self isolate for 11 days. Hadn't been in contact with anyone that day for more than 15 mins and can't understand why having not left the house in a week im getting this false info from 🤔<br> :date: __2020-10-31 07:27:48__

> It works ok but please add a venue check out facility<br> :date: __2020-10-31 07:05:10__

> Clear day<br> :date: __2020-10-30 21:42:12__

> Would be nice to be able to see warning messages again - not just as pop ups<br> :date: __2020-10-30 21:23:19__

> Quirks with a lack of info in app!! Had a notification in my status bar that said "don't worry...blah blah" or something that I tapped to open and it disappeared. Then there was another that said "someone you may have come into contact with may have..." That was ALL I COULD SEE! What I tapped on it it disappeared and there WAS NOTHING IN THE APP AT ALL THAT FURTHERED THAT STATEMENT! WHAT THE HEY?!!!? HOW IS THIS HELPFUL!!??! But it IS something that may help, so I always use it!<br> :date: __2020-10-30 21:13:17__

> Great apart from the constant panic provoking messages of risk detected.<br> :date: __2020-10-30 19:19:47__

> just keep scanning tge venues and no alerts as yet..👍<br> :date: __2020-10-30 18:51:47__

> helpful service from Ruth<br> :date: __2020-10-30 14:29:07__

> no alerts yet...<br> :date: __2020-10-30 14:03:08__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 3 reviews"/>
</p>

> I'm still mostly shielding because a my household is vulnerable/highly vulnerable. So I have my Bluetooth and location of most of the time. It would be much better to be able access the basics (area risk level etc) without having to turn these on. Also I'd really like to be reassured I'll get notifications for when I have been out (when I do with both on to activate the app) if I leave these off when I'm at home.<br> :date: __2020-10-31 09:34:27__

> Its OK, just tap your postcode then it tells you if your living in a hot spot for Covid pandemic. Quite informative.<br> :date: __2020-10-31 00:41:37__

> I've had a notification to isolate and the nearest I've been is the other side of a wall from a positive case. Seems flawed.<br> :date: __2020-10-30 21:53:07__

> the ghost warnings are a pain.<br> :date: __2020-10-30 16:31:58__

> This app interferes with other Bluetooth connections. Please fix!<br> :date: __2020-10-30 16:21:19__

> shame it does not show how many interactions you have had with others who have downloaded the app,<br> :date: __2020-10-30 15:40:01__

> Crashing and won't open. Using on Android 11. Re installed the app and now works fine but I don't feel confident that I will be notified about any contact with a covid positive source prior to reinstalling. (I have provided feedback to the developers)<br> :date: __2020-10-30 14:45:51__

> Takes a long time to scan and check in<br> :date: __2020-10-30 14:25:41__

> Please add a detailed log inside the app of the warnings we receive when we are notified that we've been in contact with people tested positive.<br> :date: __2020-10-30 11:43:10__

> Installed ok a few days ago and appeared to work ok. Yesterday tried to use it and each time I tapped it screen went blank and then just went back to original. So uninstalled and tried to re-install but no success. October now seems to be ok<br> :date: __2020-10-30 09:38:20__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 2 reviews"/>
</p>

> Messages come on and when you try and read them you just get redirected to app and message gone<br> :date: __2020-10-31 10:35:24__

> Wont scan in on qr code<br> :date: __2020-10-31 10:25:53__

> Not quite worth £10 billion.<br> :date: __2020-10-31 09:50:35__

> Since 29th Oct update app crashes constantly and unusable. Reinstall no help. Latest Android security updates applied on a pixel 3a. Was fine until then<br> :date: __2020-10-31 08:58:52__

> Hope it is working effectively. Bit concerned by notifications about possible contact that then disappear when I click in them so I cannot read them. Checked the app and there is no ability to check notifications there. Please add this!<br> :date: __2020-10-31 08:37:13__

> It is Jolly well unreliable and it is rubbish not just that is that it is incredibly inconsistent and also it is just a useless app too and it just doesn't work<br> :date: __2020-10-31 08:30:34__

> I received 3 notifications yesterday about "being close to someone who..." the notifications are there when I drag the top of my phone screen down on my Galaxy Note10. I then click the notification & then it opens the app. But I get no new info in the app & the notifications are no longer there. I'm really worried 😟 have I been in contact with someone who has tested positive or near someone who is? Should I be isolating as I don't feel I have been fully informed about what I should be doing.<br> :date: __2020-10-31 03:44:41__

> You have to open the app every couple of days as it's the only app on my Pixel 3XL that stops working, meaning you need to reboot the phone to get it working again. Much is mysterious. It should include info (animations etc) if what happens if you test positive, or someone you're in contact with is. Apparently you can't enter a negative test result to stop the mysterious countdown that some claim you get but it doesn't tell you about until you do. Disappointing.<br> :date: __2020-10-30 23:27:01__

> Easy to use but ive been having intermittent problems with it being able to read to qr code and or wont recognise it at all.<br> :date: __2020-10-30 21:37:13__

> My partner received notification to self isolate due to being a close contact. No follow-up checks! Can't access test and trace website as he's not received an id number. The only information he put in was the postcode when downloading the app!!<br> :date: __2020-10-30 20:35:14__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 1 reviews"/>
</p>

> App stopped working with error code 524 after recent update.<br> :date: __2020-10-31 11:00:16__

> Update: I've had to uninstall this now as it is dangerously broken and is repeatedly a hazard when driving. FIX THIS NOW. Pixel 4a Previous review: The app Crashes while driving and throws up an error that obscures Google Maps. This app is getting a system level error message every few hours now. It's particularly dangerous when it happens while driving and requires interaction to dismiss. The error is 'NHS COVID app keeps closing'. I'm running the latest version of the app on Android 11.<br> :date: __2020-10-31 10:56:17__

> Notifications-There should be a record of the notification within the app as is you clear this alert from your phone summary you have no way of knowing what the alert was for!<br> :date: __2020-10-31 10:27:48__

> Absolutely waste of money cant use it on older phones why????<br> :date: __2020-10-31 10:02:49__

> A silly app which gives random alerts in the middle of the night. NONE of the alerts stick around for review . The only thing I found this useful for is Venue check in. - Does it make sense to you that the app often throws alert at the middle of the night !!!<br> :date: __2020-10-31 09:53:03__

> Doesn't work at all now on my Pixel 3. Did work fine to start with but now app won't open beyond title screen, just crashes and stops. Please fix, I'm unable to sign in at venues or get alerts!<br> :date: __2020-10-31 09:49:42__

> Removing this in protest of the ridiculous decision to add Cyprus to the quarantine list. When I return to the UK there's no way I'm self isolating for 14 days and I won't have this app snooping on me.<br> :date: __2020-10-31 09:45:49__

> I've tried keeping this app on my device (Samsung A6) twice, and both times my phone randomly restarts and takes ~10 minutes to boot back up. What's the point of having a device to alert you to anyone who may be carrying the virus if it cannot be relied upon?<br> :date: __2020-10-31 09:44:07__

> Works briefly and then just crashes all the time. You the notification about risk level changing this morning only to find the app won't open again. Useless.<br> :date: __2020-10-31 09:34:53__

> Still stops working stating no Bluetooth connection. Had enough not bothering with it.<br> :date: __2020-10-31 09:34:37__


