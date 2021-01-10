# NHS COVID-19
App version ``4.1.1 (124)``

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
| **Latest version** | 4.1.1 (124) |
| **Last update** | 2020-12-18 15:54:37 |
| **Recent changes** | Bug Fixes. |
| **Installs**  | 5,000,000+ |
| **Category** | Medical |
| **First release** | Aug 12, 2020 |
| **Size**  | 8.2M |
| **Supported Android version**  | 6.0 and up |

### Description
> The NHS COVID-19 app is the official contact tracing app for England and Wales. 
<br>It is the fastest way of knowing when you’re at risk from coronavirus. The quicker you know, the quicker you can alert your loved ones, and your community. 
<br>The more of us that use it, the better we can control coronavirus. 
<br>The app runs on proven software developed by Apple and Google, designed so that nobody will know who or where you are. And you can delete your data, or the app, at any time.
<br>It has a number of features: 
<br>Trace: Find out when you’ve been near other app users who have tested positive for coronavirus
<br>Alert: Lets you know the level of coronavirus risk in your postcode district. 
<br>Check-in: Use our simple QR code scanner to check-in to venues like bars and restaurants. You will get alerted if you have visited a venue where you may have come into contact with coronavirus.
<br>Symptoms: Check if you have coronavirus symptoms and see if you need to order a test. 
<br>Test: Helps you order a test if you need to.
<br>Isolate: Keep track of your self-isolation countdown and access relevant advice.
<br>Available in English, Welsh, Arabic (Modern Standard), Bengali, Chinese (Simplified), Gujarati, Polish, Punjabi (Gurmukhi script), Romanian, Somali, Turkish and Urdu.
<br>The app can be used across UK borders in England, Wales, Scotland, Northern Ireland, Jersey and Gibraltar, detecting all relevant contact tracing app users (regardless of them using different official apps), alerting them if they have been in contact with coronavirus. 
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
 | apache.org | The Apache Software Foundation | :us: US | 1995-04-11 04:00:00 |


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

The NHS COVID-19 app has been installed by more than **5000000** times. At this time, **95001** rated the app and its average score is **3.9574847**. Below we show the distribution of the ratings across the usual star-based rating of Google Play

:star::star::star::star::star:: 56378

:star::star::star::star:: 12680

:star::star::star:: 6932

:star::star:: 3550

:star:: 15461

### Reviews 

#### 5-star reviews

<p align="center">
<img src="5_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 5 reviews"/>
</p>

> Useful information about the virus. Tell me if it is high or low where I live. And tells me where to go for a test. So this is a good app.<br> :date: __2021-01-09 18:03:59__

> I have no complaints at all about this app. Does what it is designed for.<br> :date: __2021-01-09 16:00:43__

> Worked ok for me had test results came back negative, onwards and upwards<br> :date: __2021-01-08 22:16:04__

> Good for the uk<br> :date: __2021-01-08 21:52:18__

> very useful, thank you<br> :date: __2021-01-08 18:27:17__

> Clear and concise.<br> :date: __2021-01-08 18:15:29__

> Good<br> :date: __2021-01-08 17:00:10__

> keep Safe<br> :date: __2021-01-08 16:28:16__

> it is so helpful to have the knowledge of covid 19 and the updates and advice<br> :date: __2021-01-08 15:49:14__

> I check the app once a week, it is updated on a regular basis. It is helpful to have the app on my phone.<br> :date: __2021-01-08 14:07:12__



#### 4-star reviews

<p align="center">
<img src="4_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 4 reviews"/>
</p>

> Well to be blunt and to the point. I use the app only when I go out for a walk, or when I need to go shopping or the Chemist to collect my meds. When I arrive home I leave it for a short while and then turn it of. I do not keep the NHS app on 24 7 7 days a week because it does not rule me. I rule it. However it is easy to use. And when the shops who had the bar code displayed it is easy to scan to. But I found it strange that No supermarkets had the bar code displayed. Why is that?<br> :date: __2021-01-09 10:10:00__

> The app is good, although I didn't get a notification to self isolate, I found out when I clicked onto the app, but it gives you everything you need to give to your employer and to apply for the £500 isolation grant. I think they've done an excellent job with this, to help people<br> :date: __2021-01-09 09:31:59__

> to be honest I don't know if the app is working sometimes but just feel a bit safer knowing it is there<br> :date: __2021-01-08 15:20:30__

> very few of the larger stores have the covid check in code<br> :date: __2021-01-08 12:17:28__

> Ok<br> :date: __2021-01-07 21:31:14__

> Brilliant<br> :date: __2021-01-07 16:11:42__

> I like it its just annoying how the updates are so late and that you can't use most features offline even though its a priority app<br> :date: __2021-01-05 16:40:01__

> cool<br> :date: __2021-01-04 17:36:55__

> Never recieve any notifications and my friend does all the time. Also the qr scanner will never scan anything.<br> :date: __2021-01-04 16:15:03__

> App mostly works well. Good clean interface. For a few days it was crashing on start on my phone. I think restarting the phone fixed the problem. The app's support team was responsive.<br> :date: __2021-01-04 12:19:08__



#### 3-star reviews

<p align="center">
<img src="3_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 3 reviews"/>
</p>

> Simple design good for checking on local area status.<br> :date: __2021-01-09 18:12:15__

> Can't change location<br> :date: __2021-01-09 11:28:23__

> Thank you for trying to safe guard our health, good work NHS and thank you nurses and doctors for all your hard work.<br> :date: __2021-01-08 15:39:14__

> If you're going to push an update outside of the store that has the app pause while it waits for input on my local council, give us a notification! How long was this app not tracking because it was waiting for me to put in more data?????!!!!!<br> :date: __2021-01-08 13:32:42__

> Husband and I both just received an alert saying we'd been in close contact with someone with Covid etc. Took ages to find out information as to criteria and timescales. On the day in question he hadn't been out at all and I had been for two short, careful walks. Not sure if this is a false alert. Worrying to get pinged at midnight.<br> :date: __2021-01-07 13:36:02__

> Not as good as it should be .. but alot better than nothing at all . Some of the features are weak and not easy to use<br> :date: __2021-01-07 12:36:38__

> This app has been fine up until now but now it won't work. I've tried reinstalling it numerous times but no joy. I have an Android phone<br> :date: __2021-01-07 09:32:34__

> Ok so if someone walks past me who later tests positive it will show on my exposure page as number of matched 1 but because it wasnt for 15mins or greater and 2metres or less it won't alert me, but if I was to be standing with someone for 15 mins or longer and 2metres or less who then tested positive it would display 1 match and send me a notification. Is that correct???<br> :date: __2021-01-06 10:43:10__

> Was working fine now refuses to scan qr venue check-in codes. Have spoken to other people with the same issue - worked fine a few days ago for all of us<br> :date: __2021-01-05 20:39:28__

> Was working quite well. But took until after 6pm to change info to National Lockdown. Would have expected this to be updated first thing.<br> :date: __2021-01-05 19:33:03__



#### 2-star reviews

<p align="center">
<img src="2_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 2 reviews"/>
</p>

> If I turn my bluetooth off I get a notification from the app saying I need bluetooth for the app to work etc, I can then go into it and see all the days and times its checked to see if I've been in close contact with a positive case! I've seen that on quite a few occasions I've matched up with someone and sometimes I have 2 matches on that time check,and recently I matched up 3 days running on different checks?? But not once have i had any notifications informing me of this?<br> :date: __2021-01-09 00:21:52__

> What an almost utterly pointless app, would be better if you could book a test through it or order a home test<br> :date: __2021-01-08 22:40:49__

> "Loading" Notification pops up multiple times everyday, getting really irritating. Deleting.<br> :date: __2021-01-08 21:53:14__

> App is fine however. Had symptoms new years eve and a test new year's Day. 8 days later still no results. Phoned help line to check, yes it's registered so made a complaint but that takes 3 days. Will be out of isolation and back to work before we hear anything. Makes a mockery of the track and trace. That's 10 days potentially people could be still transmitting because it's taking too long to inform me of results. Ridiculous<br> :date: __2021-01-08 14:15:01__

> Whats going on ..iv had the app from day one .last week I was alerted that I may have been in contact with some with covid so the app said I have to self isolate for 7 days ,I did so .8 days later having not left the house .the app now says I have to isolate till the 15th of January.. just to add I live on my own and no other person has been to my house ....what's happened . Frustrated<br> :date: __2021-01-08 08:25:59__

> I've been told to isolate for 8 days why 8?? We need to know the location of where in contact we was! There's alot of People out there that doesn't know how to work technology so need to go out to get there prescriptions, shopping, appointments therefore it'll be a good idea to *pin point* the location. No ones information is being used just the location of where it came from would be really helpful.<br> :date: __2021-01-07 23:19:32__

> I keep getting a number of notifications saying loading... but nothing ever shows up. The notifications some of the time only go if the app is force closed - when reopened the notification is gone. I have had 18 loading... notifications in the last 24 hours. Notifications from the app cause concern in case there has been close contact with someone COVID positive.<br> :date: __2021-01-07 23:08:41__

> I downloaded this app, but after having to self isolate and lost out on work, I found I needed a non existent code to apply. Where do I find this?<br> :date: __2021-01-07 15:44:34__

> Constant crashes in the background on a Pixel 3XL - very frustrating, especially when so frequent. Venue registration is a big plus though.<br> :date: __2021-01-07 14:31:27__

> When this app was released i immediately installed it. Within the coming weeks i would receive multiple exposure alerts (although overall cases were actually quite low at the time) which gave me the confidence the app was working as designed. For months now i have not received a single alert (despite cases being through the roof). I'm starting to question if the app is working. Given the alleged numbers I must have surely crossed paths with a positive case in a supermarket over Christmas...<br> :date: __2021-01-07 10:31:18__



#### 1-star reviews

<p align="center">
<img src="1_star_reviews_wordcloud.png" alt="uk.nhs.covid19.production 1 reviews"/>
</p>

> Won't even open. Keeps coming up with a notification saying it's stopped working. Have tried uninstalling and reinstalling again, no change.<br> :date: __2021-01-09 16:37:14__

> Would have given Zero but not possible. It stopped working and now won't restart even after re-installing.<br> :date: __2021-01-09 14:26:40__

> App not working at all. Uninstalled and reinstalled, does not open or let me check in. Unacceptable given how crucial this for of monitoring is to contain the pandemic.<br> :date: __2021-01-09 13:33:10__

> Not being able to enter a negative test result seems a bit odd to me. Surely that's useful information? The app is still telling me to continue isolate. I hope other people are also using common sense.<br> :date: __2021-01-09 13:15:27__

> So. I have tested positive. It did not ping on my parents phones whom I'm living with. Along with this the app glitched day after boxing day and made me isolate from there. I entered my results assuming it would change nope apparently I finished my isolation 2 days ago instead of the 11th Jan. The apps not clear. Along with this the spamming of messages to my phone that repeat themselves. I already know what to do and still spamming the phone.<br> :date: __2021-01-09 12:11:56__

> Bugged out and told me to isolate gave me no reference number and incorrect amount of days now I have to go without pay from work.<br> :date: __2021-01-09 11:46:43__

> Stop the £500 covid grant from requiring this useless app to access it. Not enough people use it to judge whether you should isolate, and basing personal help on its info is awful! And sneaking brexit ads onto it, criminal...<br> :date: __2021-01-09 11:12:15__

> The QR Scanner doesn't always detect the pictures. I needed to self Isolate for ten days and the app didn't tell me I had to till day 5.<br> :date: __2021-01-09 09:53:54__

> Does not allow to scan the barcode of the test into the app. How are you supposed to record this if there is no option for this vital first step. I'm using Samsung Galaxy S10+. So far not been able to use this app for reporting. Very frustrating 👎<br> :date: __2021-01-09 04:51:26__

> Incredibly irritating. This app keeps sending me notifications which are wrong or ominous, and whenever I click on them it does nothing? Takes me to the same screen I always see with no additional info. Absolutely useless tbh. Told me I had been in a place where someone tested positive in the last 2 weeks (via a notification) - I haven't left the house for two months now so? No point having an app that's meant to help track the spread if it doesn't work properly!<br> :date: __2021-01-09 02:26:25__


